#!/usr/bin/env python3
"""Rebuild this snapshot tree from the canonical folders in the repository.

The PAP06 package originally vendored a full copy of the PhD and startup
corpora under `sources/`. Every one of those files also lives in its own
project folder in this repository, so the copies were removed during the
2026-08 reorganisation and replaced by `SNAPSHOT_MANIFEST.csv`, which records
`snapshot_path -> canonical_path` for each removed file. Files with no
canonical twin were left in place and are not listed in the manifest.

Usage (from anywhere):

    python3 rehydrate.py            # restore every removed file
    python3 rehydrate.py --check    # report only; write nothing
    python3 rehydrate.py --subset phd/P/01     # restore one subtree

Each manifest row carries a `match` column:

  exact         the canonical file is byte-identical to the removed snapshot
                file once CRLF is normalised to LF, and is copied verbatim.
  path_variant  the snapshot predates a folder rename, so the two differ only
                in the folder-path strings embedded in the text. The rules in
                `SNAPSHOT_PATH_RULES.json` are applied to the canonical bytes
                to reproduce the snapshot file exactly.

`sha256_lf` is always the hash of the LF-normalised *snapshot* file, so it
verifies the restored result either way.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import sys
from pathlib import Path

SNAPSHOT_ROOT = Path(__file__).resolve().parent
MANIFEST = SNAPSHOT_ROOT / "SNAPSHOT_MANIFEST.csv"
PATH_RULES = SNAPSHOT_ROOT / "SNAPSHOT_PATH_RULES.json"


def find_repo_root(start: Path) -> Path:
    for parent in [start, *start.parents]:
        if (parent / ".git").exists():
            return parent
    raise SystemExit("could not locate the repository root (no .git found above this file)")


def load_rules() -> list[tuple[bytes, bytes]]:
    if not PATH_RULES.exists():
        return []
    spec = json.loads(PATH_RULES.read_text(encoding="utf-8"))
    return [(a.encode(), b.encode()) for a, b in spec.get("rules", [])]


def snapshot_bytes(source: Path, match: str, rules: list[tuple[bytes, bytes]]) -> bytes:
    """Reconstruct the removed snapshot file's LF-normalised content."""
    data = source.read_bytes().replace(b"\r\n", b"\n")
    if match == "path_variant":
        for old, new in rules:
            data = data.replace(old, new)
    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="report what would happen; write nothing")
    parser.add_argument("--subset", default="", help="only act on snapshot paths under this prefix")
    args = parser.parse_args(argv)

    if not MANIFEST.exists():
        raise SystemExit(f"missing manifest: {MANIFEST}")
    repo = find_repo_root(SNAPSHOT_ROOT)
    rules = load_rules()

    restored = present = missing_source = mismatched = 0
    with MANIFEST.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            snapshot_rel = row["snapshot_path"]
            if args.subset and not snapshot_rel.startswith(args.subset):
                continue
            target = SNAPSHOT_ROOT / snapshot_rel
            source = repo / row["canonical_path"]

            if target.exists():
                present += 1
                continue
            if not source.exists():
                missing_source += 1
                print(f"MISSING SOURCE  {row['canonical_path']}  (needed by {snapshot_rel})")
                continue

            match = row.get("match", "exact")
            data = snapshot_bytes(source, match, rules)
            if hashlib.sha256(data).hexdigest() != row["sha256_lf"]:
                mismatched += 1
                print(f"CONTENT DRIFT   {row['canonical_path']}  no longer reproduces {snapshot_rel}")
                continue

            if not args.check:
                target.parent.mkdir(parents=True, exist_ok=True)
                if match == "exact":
                    shutil.copy2(source, target)
                else:
                    target.write_bytes(data)
            restored += 1

    verb = "would restore" if args.check else "restored"
    print(f"\n{verb} {restored} files; {present} already present; "
          f"{missing_source} canonical sources missing; {mismatched} drifted")
    return 1 if (missing_source or mismatched) else 0


if __name__ == "__main__":
    sys.exit(main())
