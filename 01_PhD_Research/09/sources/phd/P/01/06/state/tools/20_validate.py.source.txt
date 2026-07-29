"""Stage 20 deterministic validation.

Checks:
  A. 02_DIRECTION_SCORECARD.csv — exact header, row count, score ranges,
     weighted-score recomputation against the stated baseline weights,
     rank consistency, valid UTF-8, no markdown fences.
  B. 02_RESEARCH_DIRECTION_DECISION.md — every [S####] resolves to the
     231-row ledger; every doi.org link attached to an [S####] citation
     matches that row's DOI (URL-decoded comparison); relative file links
     resolve on disk.
Exit 0 with "PASS" on success; exit 1 with named failures otherwise.
"""
import csv
import os
import re
import sys
import urllib.parse

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCORECARD = os.path.join(BASE, "outputs", "02_DIRECTION_SCORECARD.csv")
DECISION = os.path.join(BASE, "outputs", "02_RESEARCH_DIRECTION_DECISION.md")
LEDGER = os.path.join(BASE, "outputs", "01_SOURCE_LEDGER.csv")

EXPECTED_HEADER = (
    "option_id,option_name,scope,24_month_publishability,novelty_strength,"
    "evidence_strength,cleanroom_burden,experimental_burden,"
    "software_simulation_leverage,advisor_group_fit,startup_optionality,"
    "schedule_risk,key_dependency,weighted_score,rank,decision"
)
SCORE_COLS = [
    "24_month_publishability", "novelty_strength", "evidence_strength",
    "cleanroom_burden", "experimental_burden",
    "software_simulation_leverage", "advisor_group_fit",
    "startup_optionality", "schedule_risk",
]
WEIGHTS = {
    "24_month_publishability": 0.20, "novelty_strength": 0.15,
    "evidence_strength": 0.10, "cleanroom_burden": 0.10,
    "experimental_burden": 0.08, "software_simulation_leverage": 0.10,
    "advisor_group_fit": 0.12, "startup_optionality": 0.07,
    "schedule_risk": 0.08,
}

fails = []

# --- A. scorecard ---
raw = open(SCORECARD, "rb").read()
try:
    text = raw.decode("utf-8")
except UnicodeDecodeError as e:
    fails.append(f"CSV not valid UTF-8: {e}")
    text = raw.decode("utf-8", "replace")
if "```" in text:
    fails.append("CSV contains markdown fences")
lines = [l for l in text.splitlines() if l.strip()]
if lines[0] != EXPECTED_HEADER:
    fails.append("CSV header mismatch")

rows = list(csv.DictReader(text.splitlines()))
if len(rows) != 4:
    fails.append(f"expected 4 option rows, found {len(rows)}")
ids = [r["option_id"] for r in rows]
if len(set(ids)) != len(ids):
    fails.append("duplicate option_id")
scored = []
for r in rows:
    for c in SCORE_COLS:
        v = int(r[c])
        if not 1 <= v <= 5:
            fails.append(f"{r['option_id']}.{c}={v} out of 1-5")
    ws = sum(WEIGHTS[c] * int(r[c]) for c in SCORE_COLS)
    stated = float(r["weighted_score"])
    if abs(ws - stated) > 0.005:
        fails.append(
            f"{r['option_id']} weighted_score stated {stated} != computed {ws:.4f}")
    scored.append((r["option_id"], ws, int(r["rank"])))
    if not r["key_dependency"].strip() or not r["decision"].strip():
        fails.append(f"{r['option_id']} empty key_dependency/decision")
# rank consistency: higher score -> better (lower) rank
by_score = sorted(scored, key=lambda t: -t[1])
for expect_rank, (oid, ws, stated_rank) in enumerate(by_score, 1):
    if stated_rank != expect_rank:
        fails.append(f"{oid} rank stated {stated_rank} != score-order {expect_rank}")
wsum = sum(WEIGHTS.values())
if abs(wsum - 1.0) > 1e-9:
    fails.append(f"weights sum to {wsum}, not 1.00")

# --- B. decision report citations ---
ledger = {}
with open(LEDGER, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        ledger[row["source_id"]] = row["doi"].strip().lower()
if len(ledger) != 231:
    fails.append(f"ledger rows {len(ledger)} != 231")

md = open(DECISION, encoding="utf-8").read()
cited = sorted(set(re.findall(r"\[S(\d{4})\]", md)))
cited_ids = [f"S{c}" for c in cited]
for sid in cited_ids:
    if sid not in ledger:
        fails.append(f"citation {sid} not in ledger")

linked = re.findall(r"\[S(\d{4})\]\(https://doi\.org/([^)]+)\)", md)
for num, doi_part in linked:
    sid = f"S{num}"
    md_doi = urllib.parse.unquote(doi_part).strip().lower()
    led = ledger.get(sid, "")
    if md_doi != led:
        fails.append(f"{sid} doi link {md_doi!r} != ledger {led!r}")

# every cited sid should have at least one linked (first-use) occurrence
linked_ids = {f"S{n}" for n, _ in linked}
for sid in cited_ids:
    if sid not in linked_ids:
        fails.append(f"{sid} cited but never linked with doi.org URL")

# relative file links resolve (from outputs/ dir)
outdir = os.path.join(BASE, "outputs")
for target in re.findall(r"\]\((?!https?://)([^)#]+)\)", md):
    p = os.path.normpath(os.path.join(outdir, target))
    if not os.path.exists(p):
        fails.append(f"relative link does not resolve: {target}")

print(f"cited sources: {len(cited_ids)}; doi-linked citation instances: {len(linked)}")
if fails:
    print("FAIL")
    for f_ in fails:
        print(" -", f_)
    sys.exit(1)
print("PASS")
