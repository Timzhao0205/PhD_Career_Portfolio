#!/usr/bin/env python3
"""Append one checkpoint line to 05_STATE/PROGRESS_LOG.md."""
import datetime
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOG = ROOT / "05_STATE" / "PROGRESS_LOG.md"


def main(argv):
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    line = f"[{stamp}] " + " ".join(argv)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
