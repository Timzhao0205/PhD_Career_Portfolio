"""Stage 40 deterministic validation.

Checks:
  1. All four required outputs exist, are non-empty, valid UTF-8.
  2. 04_MEASUREMENT_REQUIREMENTS.csv: exact 14-column header, every row
     14 fields, unique requirement_ids matching ^[A-G]-\\d{2}$ (G-01
     allowed), priority starts with P0/P1/P2, no Markdown fences.
  3. Every requirement ID referenced in the three MD files exists in the
     CSV.
  4. Every relative Markdown link in the three MD files resolves on disk
     (relative to outputs/).
  5. Every [S####](https://doi.org/...) citation resolves to
     01_SOURCE_LEDGER.csv with a matching DOI; every bare S#### mention
     exists in the ledger.
Exit 0 with 'VALIDATION: PASS' on success; exit 1 with failures listed.
"""
import csv
import re
import sys
import urllib.parse
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "outputs"
CSV_PATH = OUT / "04_MEASUREMENT_REQUIREMENTS.csv"
MD_PATHS = [
    OUT / "04_HSX_EXPERIMENT_PLAN.md",
    OUT / "04_DATA_ANALYSIS_PLAN.md",
    OUT / "04_UNCERTAINTY_AND_STATISTICS_PLAN.md",
]
LEDGER = OUT / "01_SOURCE_LEDGER.csv"

EXPECTED_HEADER = (
    "requirement_id,reviewer_or_science_driver,measurement,minimum_design,"
    "preferred_design,hardware_or_signal_needed,replicates,"
    "independent_variable,dependent_variable,acceptance_metric,"
    "uncertainty_component,dependency,priority,fallback_if_unavailable"
).split(",")

fails = []
notes = []


def norm_doi(s: str) -> str:
    s = urllib.parse.unquote(s.strip().lower())
    for pre in ("https://doi.org/", "http://doi.org/", "doi.org/", "doi:"):
        if s.startswith(pre):
            s = s[len(pre):]
    return s.rstrip("/")


# --- 1. existence / UTF-8 ---
texts = {}
for p in [CSV_PATH] + MD_PATHS:
    if not p.exists():
        fails.append(f"missing file: {p.name}")
        continue
    raw = p.read_bytes()
    if not raw:
        fails.append(f"empty file: {p.name}")
        continue
    try:
        texts[p] = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        fails.append(f"not valid UTF-8: {p.name} ({e})")

# --- 2. CSV structure ---
req_ids = set()
if CSV_PATH in texts:
    if "```" in texts[CSV_PATH]:
        fails.append("CSV contains a Markdown fence")
    rows = list(csv.reader(texts[CSV_PATH].splitlines()))
    if rows[0] != EXPECTED_HEADER:
        fails.append(f"CSV header mismatch: {rows[0]}")
    for i, row in enumerate(rows[1:], start=2):
        if len(row) != len(EXPECTED_HEADER):
            fails.append(f"CSV line {i}: {len(row)} fields (want 14)")
            continue
        rid, prio = row[0], row[12]
        if not re.fullmatch(r"[A-G]-\d{2}", rid):
            fails.append(f"CSV line {i}: bad requirement_id {rid!r}")
        if rid in req_ids:
            fails.append(f"CSV line {i}: duplicate requirement_id {rid!r}")
        req_ids.add(rid)
        if not re.match(r"P[0-2]\b", prio):
            fails.append(f"CSV line {i}: bad priority {prio!r}")
    notes.append(f"CSV rows: {len(rows) - 1}, unique IDs: {len(req_ids)}")

# --- ledger map ---
ledger = {}
with open(LEDGER, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        ledger[row["source_id"]] = (row.get("doi", ""), row.get("url", ""))
notes.append(f"ledger sources: {len(ledger)}")

# --- 3-5. MD checks ---
link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
sid_link_re = re.compile(r"\[(S\d{4})\]\((https?://[^)]+)\)")
sid_any_re = re.compile(r"\bS\d{4}\b")
reqref_re = re.compile(r"\b([A-G]-\d{2})\b")

n_links = n_sid_links = n_sids = n_reqrefs = 0
for p in MD_PATHS:
    if p not in texts:
        continue
    text = texts[p]
    for target in link_re.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        n_links += 1
        tgt = (OUT / target).resolve()
        if not tgt.exists():
            fails.append(f"{p.name}: broken relative link {target!r}")
    for sid, url in sid_link_re.findall(text):
        n_sid_links += 1
        if sid not in ledger:
            fails.append(f"{p.name}: cited {sid} not in ledger")
            continue
        doi, lurl = ledger[sid]
        cand = {norm_doi(doi), norm_doi(lurl)}
        if norm_doi(url) not in cand:
            fails.append(
                f"{p.name}: {sid} DOI mismatch {url!r} vs ledger {doi!r}/{lurl!r}"
            )
    for sid in sid_any_re.findall(text):
        n_sids += 1
        if sid not in ledger:
            fails.append(f"{p.name}: mentioned {sid} not in ledger")
    for rid in reqref_re.findall(text):
        n_reqrefs += 1
        if rid not in req_ids:
            fails.append(f"{p.name}: references requirement {rid} absent from CSV")

notes.append(
    f"relative links checked: {n_links}; S-ID links: {n_sid_links}; "
    f"S-ID mentions: {n_sids}; requirement refs: {n_reqrefs}"
)

for n in notes:
    print("NOTE:", n)
if fails:
    for msg in fails:
        print("FAIL:", msg)
    print(f"VALIDATION: FAIL ({len(fails)} issue(s))")
    sys.exit(1)
print("VALIDATION: PASS")
