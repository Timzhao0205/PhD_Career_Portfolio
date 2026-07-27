"""Stage 30 deterministic validation.

Checks:
  1. 03_REVIEWER_RESPONSE_MATRIX.csv: exact required header, 13 fields per
     row, unique comment_id, allowed source/priority values, valid UTF-8,
     no Markdown fences.
  2. Coverage: the ten stage-prompt topic areas each match at least one row.
  3. Every S#### cited in the CSV and both MD files resolves to
     01_SOURCE_LEDGER.csv.
  4. Every inline [S####](https://doi.org/...) link's DOI matches that
     ledger row's DOI (case-insensitive, URL-decoded).
  5. Every S-ID cited in an MD file has at least one linked occurrence in
     that same file.
  6. Every relative link in both MD files resolves to an existing file.

Run from the mission root:  python state/tools/30_validate.py
"""
import csv
import os
import re
import sys
import urllib.parse

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "outputs")
CSV_PATH = os.path.join(OUT, "03_REVIEWER_RESPONSE_MATRIX.csv")
MD_PATHS = [
    os.path.join(OUT, "03_MANUSCRIPT_DIAGNOSIS.md"),
    os.path.join(OUT, "03_PUBLICATION_ROUTE_DECISION.md"),
]
LEDGER = os.path.join(OUT, "01_SOURCE_LEDGER.csv")

REQUIRED_HEADER = (
    "comment_id,source,comment_summary,underlying_issue,"
    "current_manuscript_location,current_evidence_status,"
    "can_fix_without_new_data,required_action,proposed_evidence_or_analysis,"
    "publication_route_relevance,priority,disposition,notes"
)
ALLOWED_SOURCES = {"Associate Editor", "Reviewer 1", "Reviewer 2"}
ALLOWED_PRIORITY = {"P0", "P1", "P2"}
COVERAGE = {
    "novelty": r"novelty",
    "absolute_field_output": r"intended sensing output|absolute|field units|magnetic-field values|tesla",
    "calibration": r"calibrat",
    "repeatability_fabrication": r"repeatab|fabrication iteration",
    "conventional_probe": r"B-dot|conventional",
    "bandwidth": r"bandwidth|1 MHz",
    "parasitics_packaging": r"parasitic|packaging|wire.bond|bond.pad",
    "gan_literature_comparison": r"comparison table|GaN Hall",
    "figure_presentation": r"Fig\. 5|overlay|re-plot",
    "mirnov_reference": r"Mirnov",
}

errors, notes = [], []

# --- ledger ---
with open(LEDGER, encoding="utf-8") as f:
    ledger = {r["source_id"]: r for r in csv.DictReader(f)}
notes.append(f"ledger rows: {len(ledger)}")

# --- CSV checks ---
raw = open(CSV_PATH, "rb").read()
try:
    text = raw.decode("utf-8")
except UnicodeDecodeError as e:
    errors.append(f"CSV not valid UTF-8: {e}")
    text = raw.decode("utf-8", "replace")
if "```" in text:
    errors.append("CSV contains Markdown fence")
first_line = text.splitlines()[0].lstrip("﻿")
if first_line != REQUIRED_HEADER:
    errors.append(f"CSV header mismatch:\n got: {first_line}")

with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
notes.append(f"matrix rows: {len(rows)}")
ids = [r["comment_id"] for r in rows]
if len(ids) != len(set(ids)):
    errors.append("duplicate comment_id values")
for r in rows:
    if None in r.values() or None in r:
        errors.append(f"{r['comment_id']}: field-count mismatch")
    if r["source"] not in ALLOWED_SOURCES:
        errors.append(f"{r['comment_id']}: bad source '{r['source']}'")
    if r["priority"] not in ALLOWED_PRIORITY:
        errors.append(f"{r['comment_id']}: bad priority '{r['priority']}'")
for role, prefix in [("Associate Editor", "AE-"), ("Reviewer 1", "R1-"),
                     ("Reviewer 2", "R2-")]:
    n = sum(1 for r in rows if r["source"] == role)
    if n == 0:
        errors.append(f"no rows for {role}")
    notes.append(f"{role}: {n} rows")
    for r in rows:
        if r["source"] == role and not r["comment_id"].startswith(prefix):
            errors.append(f"{r['comment_id']}: id/source prefix mismatch")

all_csv_text = text
for key, pat in COVERAGE.items():
    if not re.search(pat, all_csv_text, re.IGNORECASE):
        errors.append(f"coverage area '{key}' matches no CSV content")

# --- S-ID and link checks (CSV + MD) ---
def check_sids(path, content):
    sids = set(re.findall(r"S(\d{4})", content))
    missing = sorted(f"S{n}" for n in sids if f"S{n}" not in ledger)
    if missing:
        errors.append(f"{os.path.basename(path)}: unknown source IDs {missing}")
    return {f"S{n}" for n in sids}

check_sids(CSV_PATH, all_csv_text)

link_re = re.compile(r"\[S(\d{4})\]\((https://doi\.org/([^)]+))\)")
rel_link_re = re.compile(r"\]\((?!https?://|#)([^)]+)\)")
for md in MD_PATHS:
    content = open(md, encoding="utf-8").read()
    base = os.path.basename(md)
    cited = check_sids(md, content)
    linked = set()
    for m in link_re.finditer(content):
        sid = f"S{m.group(1)}"
        linked.add(sid)
        if sid not in ledger:
            continue
        want = ledger[sid]["doi"].strip().lower()
        got = urllib.parse.unquote(m.group(3)).strip().lower()
        if want and got != want:
            errors.append(f"{base}: {sid} DOI mismatch (link {got} vs ledger {want})")
    unlinked = sorted(cited - linked)
    if unlinked:
        errors.append(f"{base}: cited without any doi-linked occurrence: {unlinked}")
    for m in rel_link_re.finditer(content):
        target = m.group(1).split("#")[0]
        if not target:
            continue
        tp = os.path.normpath(os.path.join(os.path.dirname(md), target))
        if not os.path.exists(tp):
            errors.append(f"{base}: broken relative link '{m.group(1)}'")
    notes.append(f"{base}: {len(cited)} source IDs cited, {len(linked)} linked")

print("\n".join("NOTE  " + n for n in notes))
if errors:
    print("\n".join("ERROR " + e for e in errors))
    print(f"RESULT: FAIL ({len(errors)} errors)")
    sys.exit(1)
print("RESULT: PASS")
