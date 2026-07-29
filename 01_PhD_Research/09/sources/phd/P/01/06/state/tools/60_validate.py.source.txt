#!/usr/bin/env python3
"""Deterministic validation for stage 60_timeline outputs.

Checks:
  1. 06_MILESTONES.csv: exact header, unique IDs, 13 cols/row, dates parse,
     target_date >= start_date, status is a known value, dependency
     references (Mxx tokens) all resolve to existing milestone IDs.
  2. The three markdown deliverables exist and are non-trivial in size.
  3. Every relative markdown link ([text](path)) in the four outputs
     resolves to a file that exists in outputs/.
  4. A crude scan for accidental immigration/legal-advice language in the
     markdown outputs (the stage prompt forbids immigration/legal claims).
"""
import csv
import os
import re
import sys

BASE = os.path.join(os.path.dirname(__file__), "..", "..")
OUT = os.path.join(BASE, "outputs")

CSV_PATH = os.path.join(OUT, "06_MILESTONES.csv")
MD_PATHS = [
    os.path.join(OUT, "06_24_MONTH_PHD_ROADMAP.md"),
    os.path.join(OUT, "06_STARTUP_READINESS.md"),
    os.path.join(OUT, "06_ADVISOR_MEETING_BRIEF.md"),
]

EXPECTED_HEADER = [
    "milestone_id", "start_date", "target_date", "workstream", "milestone",
    "deliverable", "dependency", "owner_or_decision_maker", "effort_estimate",
    "success_gate", "slip_trigger", "fallback", "status",
]

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MID_RE = re.compile(r"\bM\d{2}\b")
STATUS_VALUES = {"not_started", "in_progress", "blocked", "complete"}

FORBIDDEN_TERMS = [
    "visa status", "green card", "immigration attorney", "work authorization",
    "legal advice regarding", "h-1b", "opt extension", "cpt authorization",
]

errors = []
warnings = []


def check_csv():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r)
        if header != EXPECTED_HEADER:
            errors.append(f"CSV header mismatch: {header}")
        rows = list(r)

    ids = []
    for i, row in enumerate(rows, start=2):
        if len(row) != len(EXPECTED_HEADER):
            errors.append(f"CSV line {i}: {len(row)} cols, expected {len(EXPECTED_HEADER)}")
            continue
        rec = dict(zip(EXPECTED_HEADER, row))
        ids.append(rec["milestone_id"])
        for key in ("start_date", "target_date"):
            if not DATE_RE.match(rec[key]):
                errors.append(f"CSV line {i} ({rec['milestone_id']}): bad {key} '{rec[key]}'")
        if DATE_RE.match(rec["start_date"]) and DATE_RE.match(rec["target_date"]):
            if rec["target_date"] < rec["start_date"]:
                errors.append(
                    f"CSV line {i} ({rec['milestone_id']}): target_date "
                    f"{rec['target_date']} before start_date {rec['start_date']}"
                )
        if rec["status"] not in STATUS_VALUES:
            errors.append(f"CSV line {i} ({rec['milestone_id']}): unknown status '{rec['status']}'")

    if len(ids) != len(set(ids)):
        dupes = {x for x in ids if ids.count(x) > 1}
        errors.append(f"CSV duplicate milestone_id(s): {dupes}")

    id_set = set(ids)
    for i, row in enumerate(rows, start=2):
        if len(row) != len(EXPECTED_HEADER):
            continue
        rec = dict(zip(EXPECTED_HEADER, row))
        for field in ("dependency",):
            for token in MID_RE.findall(rec[field]):
                if token not in id_set:
                    errors.append(
                        f"CSV line {i} ({rec['milestone_id']}): dependency references "
                        f"unknown milestone_id '{token}'"
                    )
    print(f"CSV: {len(ids)} rows, {len(id_set)} unique IDs")
    return id_set


def check_markdown(valid_ids):
    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for path in MD_PATHS:
        if not os.path.isfile(path):
            errors.append(f"Missing required file: {path}")
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        if len(text) < 2000:
            warnings.append(f"{os.path.basename(path)} is short ({len(text)} chars)")

        for m in link_re.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "#")):
                continue
            target_path = os.path.normpath(os.path.join(OUT, target))
            if not os.path.isfile(target_path):
                errors.append(f"{os.path.basename(path)}: broken relative link '{target}'")

        referenced = set(MID_RE.findall(text))
        unknown = referenced - valid_ids
        if unknown:
            warnings.append(f"{os.path.basename(path)}: references unknown milestone IDs {unknown}")

        lower = text.lower()
        for term in FORBIDDEN_TERMS:
            if term in lower:
                errors.append(f"{os.path.basename(path)}: forbidden immigration/legal term '{term}' found")


def main():
    valid_ids = check_csv()
    check_markdown(valid_ids)

    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    for w in warnings:
        print("WARNING:", w)
    for e in errors:
        print("ERROR:", e)

    if errors:
        sys.exit(1)
    print("VALIDATION PASS")


if __name__ == "__main__":
    main()
