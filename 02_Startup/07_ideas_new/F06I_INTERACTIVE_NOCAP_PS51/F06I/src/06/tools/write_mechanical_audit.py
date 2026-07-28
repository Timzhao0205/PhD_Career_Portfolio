#!/usr/bin/env python3
"""Run all non-circular validators and write the P8 mechanical audit."""

from __future__ import annotations

import datetime as dt
import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CHECKS = [
    "validate_sources.py",
    "validate_p4.py",
    "validate_p5_redteams.py",
    "validate_p5_selection.py",
    "validate_deep_dives.py",
    "validate_final_portfolio.py",
]


def main() -> int:
    results: list[tuple[str, int, str]] = []
    for name in CHECKS:
        run = subprocess.run(
            [sys.executable, str(ROOT / "tools" / name)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        output = (run.stdout + run.stderr).strip()
        results.append((name, run.returncode, output))
    passed = all(code == 0 for _, code, _ in results)
    lines = [
        "# Mechanical audit", "",
        f"**Result: {'PASS' if passed else 'FAIL'}**", "",
        f"Run date: {dt.date.today().isoformat()}", "",
        "This audit is non-circular: it validates sources, P4, P5 red-team coverage, the exact P5 selection, exact deep dives, and the P7 portfolio structure before the final mission-state check.", "",
    ]
    for name, code, output in results:
        lines += [f"## {name} — {'PASS' if code == 0 else 'FAIL'}", "", "```text", output, "```", ""]
    lines += [
        "## Constraint readback", "",
        "- Exact 24 final ideas and exact 10 top-ranked deep dives are machine-checked.",
        "- Every selected idea has at least 12 accepted sources, five peer-reviewed records, and three primary-demand records.",
        "- Every deep dive has 2,500-4,000 words and at least 20 accepted sources, seven peer-reviewed records, and five primary records.",
        "- Lane, role, archetype, geography, timing, decisive-experiment, and excluded-market constraints are machine-checked.",
        "- Final mission completion remains blocked until the independent source/claim adjudication passes and `FINAL_AUDIT.md` is written.",
    ]
    (ROOT / "99_AUDIT" / "MECHANICAL_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"MECHANICAL AUDIT {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
