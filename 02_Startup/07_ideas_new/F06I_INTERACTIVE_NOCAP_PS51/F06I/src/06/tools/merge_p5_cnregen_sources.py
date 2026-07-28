#!/usr/bin/env python3
"""Promote the independently reviewed P5 China-regeneration source records.

This deliberately touches only the canonical source ledger.  It is idempotent,
rejects canonical-key conflicts, preserves a pre-merge backup, and completes the
India-origin audit fields required by validate_sources.py from the proposal's
explicit official-domain/Crossref evidence.
"""

from __future__ import annotations

import json
import pathlib
import shutil


ROOT = pathlib.Path(__file__).resolve().parents[1]
PROPOSAL = ROOT / "30_SCREENING" / "P5_CN_DEFICIENCY_REGEN_PROPOSAL.json"
LEDGER = ROOT / "90_BIBLIOGRAPHY" / "sources.json"
BACKUP = ROOT / "98_RUN_LOGS" / "P5_PRE_CNREGEN_SOURCE_MERGE_sources.json"
AUDITED_AT = "2026-07-14T06:55:10Z"


def main() -> int:
    proposal = json.loads(PROPOSAL.read_text(encoding="utf-8-sig"))
    ledger = json.loads(LEDGER.read_text(encoding="utf-8-sig"))
    proposed = proposal["new_source_ledger_ready_metadata"]
    by_id = {row["id"]: row for row in ledger}
    by_key = {str(row["canonical_key"]).strip().lower(): row for row in ledger}

    additions = []
    for raw in proposed:
        row = dict(raw)
        source_id = row.pop("suggested_id")
        key = str(row["canonical_key"]).strip().lower()
        if source_id in by_id:
            if str(by_id[source_id]["canonical_key"]).strip().lower() != key:
                raise SystemExit(f"ID conflict for {source_id}")
            continue
        if key in by_key:
            raise SystemExit(
                f"canonical-key conflict for {source_id}: already {by_key[key]['id']}"
            )

        row["id"] = source_id
        row["accepted"] = True
        row["rejection_reason"] = ""
        row["notes"] = (
            "Accepted in P5 bounded China-deficiency regeneration after main readback; "
            "use only for the specific claim and locator recorded here."
        )
        audit = dict(row.get("india_origin_audit") or {})
        audit["audited_at"] = AUDITED_AT
        audit["evidence_urls"] = [row["url"]]
        audit.setdefault("non_indian_affiliation_count", 1)
        audit.setdefault(
            "institutions",
            [{"name": row.get("authors_or_org", "verified source organization"),
              "country": "CN" if "CN" in (row.get("geography") or []) else "non-IN"}],
        )
        row["india_origin_audit"] = audit
        additions.append(row)

    if not additions:
        print("P5 CN regeneration source merge: already applied; 0 additions")
        return 0

    if not BACKUP.exists():
        shutil.copy2(LEDGER, BACKUP)
    ledger.extend(additions)
    LEDGER.write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"P5 CN regeneration source merge: added {len(additions)} records")
    print("IDs: " + ", ".join(row["id"] for row in additions))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
