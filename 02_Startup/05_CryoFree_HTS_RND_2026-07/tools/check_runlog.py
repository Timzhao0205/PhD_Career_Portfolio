#!/usr/bin/env python3
"""check_runlog.py -- conformance check for the run-log standard.

Verifies the three state files exist and are well-formed, that every
PROGRESS_LOG wave line carries a greppable models= tag, and that Fable-gated
waves carry the down-route caveat. Exit 0 = green, 1 = problems (printed).

Run from the project root:  python tools/check_runlog.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "80_STATE"


def main() -> int:
    problems = []

    rs = STATE / "RUN_STATE.json"
    if not rs.exists():
        problems.append("missing 80_STATE/RUN_STATE.json")
    else:
        try:
            d = json.loads(rs.read_text(encoding="utf-8"))
            for key in ("phase", "wave", "models", "budget_tokens", "gates"):
                if key not in d:
                    problems.append(f"RUN_STATE.json missing key: {key}")
        except Exception as e:
            problems.append(f"RUN_STATE.json not valid JSON: {e}")

    pl = STATE / "PROGRESS_LOG.md"
    if not pl.exists():
        problems.append("missing 80_STATE/PROGRESS_LOG.md")
    else:
        lines = [l for l in pl.read_text(encoding="utf-8").splitlines()
                 if l.strip().startswith("W")]
        for l in lines:
            if "models=" not in l:
                problems.append(f"PROGRESS_LOG line without models= tag: {l[:60]}")
            if re.search(r"fable", l, re.I) and "unverifiable" not in l.lower():
                problems.append(
                    f"Fable-gated line missing down-route caveat: {l[:60]}")

    if not (STATE / "ASSUMPTIONS.md").exists():
        problems.append("missing 80_STATE/ASSUMPTIONS.md")

    if problems:
        print("RUN-LOG CHECK: PROBLEMS")
        for p in problems:
            print("  -", p)
        return 1
    print("RUN-LOG CHECK: green")
    return 0


if __name__ == "__main__":
    sys.exit(main())
