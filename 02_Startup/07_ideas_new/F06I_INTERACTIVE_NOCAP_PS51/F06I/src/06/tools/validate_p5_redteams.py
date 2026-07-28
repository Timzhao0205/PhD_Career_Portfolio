#!/usr/bin/env python3
"""Validate the six P5 red-team packets before portfolio adjudication."""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
REDTEAM = ROOT / "30_SCREENING" / "REDTEAM"

GROUPS = {
    "G01": {"P3R2-D-02", "P3R2-G-03", "P3R2-D-13", "P3R2-F-06", "P3R2-A-13"},
    "G02": {"P3R2-C-22", "P3R2-C-01", "P3R2-B-01", "P3R2-D-19", "P3R2-F-12"},
    "G03": {"P3R2-A-14", "P3R2-G-01", "P3R2-C-08", "P3R2-E-02", "P3R2-D-16"},
    "G04": {"P3R2-F-01", "P3R2-E-04", "P3R2-A-10", "P3R2-F-23", "P3R2-A-02"},
    "G05": {"P3R2-D-01", "P3R2-C-13", "P3R2-C-04", "P3R2-D-12", "P3R2-A-21"},
    "G06": {"P3R2-E-14", "P3R2-A-05", "P3R2-A-22", "P3R2-F-02", "P3R2-F-03"},
}

REQUIRED_CONCEPTS = (
    "bear",
    "disconfirm",
    "steelman",
    "falsification",
)


def main() -> int:
    errors: list[str] = []
    seen: set[str] = set()
    for group, expected in GROUPS.items():
        path = REDTEAM / f"P5_RT_{group}.md"
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")
            continue
        text = path.read_text(encoding="utf-8-sig")
        found = set(re.findall(r"\bP3R2-[A-G]-\d{2}\b", text))
        missing = expected - found
        extra = found - expected
        if missing:
            errors.append(f"{group} missing ideas {sorted(missing)}")
        if extra:
            errors.append(f"{group} contains unassigned ideas {sorted(extra)}")
        overlap = seen & found
        if overlap:
            errors.append(f"{group} duplicates prior assignments {sorted(overlap)}")
        seen |= found
        lower = text.lower()
        for concept in REQUIRED_CONCEPTS:
            if lower.count(concept) < len(expected):
                errors.append(
                    f"{group} has fewer than {len(expected)} occurrences of required concept {concept!r}"
                )
        if "kill probability" not in lower:
            errors.append(f"{group} does not label kill probability")
        percentages = re.findall(r"\b(?:100|\d{1,2})%", text)
        if len(percentages) < len(expected):
            errors.append(f"{group} has fewer than {len(expected)} percentage kill estimates")
        decisions = re.findall(r"\b(?:KEEP|HOLD|KILL)\b", text, flags=re.I)
        if len(decisions) < len(expected):
            errors.append(f"{group} has only {len(decisions)} KEEP/HOLD/KILL decision markers")
        gate_labels = set(re.findall(r"\bG([1-7])\b", text, flags=re.I))
        if gate_labels != set("1234567"):
            errors.append(f"{group} does not address every hard gate G1-G7")
        if len(text.split()) < 900:
            errors.append(f"{group} is too short for five substantive reviews ({len(text.split())} words)")

    expected_all = set().union(*GROUPS.values())
    if seen and seen != expected_all:
        errors.append(f"coverage mismatch: reviewed={len(seen)} expected={len(expected_all)}")

    if errors:
        print("P5 RED-TEAM VALIDATION FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("P5 RED-TEAM VALIDATION PASS")
    print(f"- packets={len(GROUPS)} ideas={len(seen)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
