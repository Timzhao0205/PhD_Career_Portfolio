"""Deterministic validation for stage 50 outputs."""
import csv, os, re, sys

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(BASE, "outputs")
LEDGER = os.path.join(OUT, "05_PRIOR_ART_LEDGER.csv")
CONCEPTS = os.path.join(OUT, "05_CANDIDATE_PROTECTABLE_CONCEPTS.md")
CHECKLIST = os.path.join(OUT, "05_DISCLOSURE_HOLD_CHECKLIST.md")
SOURCES = os.path.join(OUT, "01_SOURCE_LEDGER.csv")

EXPECTED_HEADER = ("art_id,type,title,identifier_or_citation,priority_or_publication_date,"
                   "assignee_or_authors,url,relevant_features,overlap_with_supplied_work,"
                   "potential_distinction,evidence_accessed,confidence,notes")

errors, notes = [], []

# --- CSV structural checks -------------------------------------------------
raw = open(LEDGER, "rb").read()
try:
    text = raw.decode("utf-8")
except UnicodeDecodeError as e:
    errors.append(f"CSV not valid UTF-8: {e}")
    text = raw.decode("utf-8", "replace")
if "```" in text:
    errors.append("CSV contains markdown fence")

with open(LEDGER, encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
header = ",".join(rows[0])
if header != EXPECTED_HEADER:
    errors.append(f"Header mismatch: {header!r}")
body = rows[1:]
ids = [r[0] for r in body]
if len(ids) != len(set(ids)):
    errors.append("Duplicate art_id values")
for r in body:
    if len(r) != 13:
        errors.append(f"Row {r[0]} has {len(r)} columns (expected 13)")
    if not re.match(r"^PA-[PN]\d\d$", r[0]):
        errors.append(f"Bad art_id format: {r[0]}")
    if r[11] not in ("high", "medium", "low"):
        errors.append(f"Row {r[0]}: bad confidence {r[11]!r}")
patents = [r for r in body if r[1] in ("patent", "patent_application")]
npl = [r for r in body if r[1] not in ("patent", "patent_application")]
notes.append(f"CSV rows: {len(body)} total = {len(patents)} patent/application + {len(npl)} NPL")

# --- S#### cross-references vs source ledger --------------------------------
with open(SOURCES, encoding="utf-8", newline="") as f:
    src = {r["source_id"]: r for r in csv.DictReader(f)}
sid_checked = 0
for r in body:
    for sid in re.findall(r"(?<![A-Z0-9])S\d{4}(?!\d)", ",".join(r)):
        sid_checked += 1
        if sid not in src:
            errors.append(f"Row {r[0]}: unknown source id {sid}")
    m = re.search(r"ledger \((S\d{4})\)", r[10])
    if m:
        doi_in_row = re.search(r"10\.\d{4,9}/[^\s;,\"]+", r[3] + " " + r[6])
        if doi_in_row:
            led_doi = src[m.group(1)]["doi"].strip().lower()
            row_doi = doi_in_row.group(0).strip().lower().rstrip(".")
            if led_doi and led_doi not in (row_doi, row_doi.rstrip("/")):
                errors.append(f"Row {r[0]}: DOI {row_doi} != ledger {m.group(1)} DOI {led_doi}")
notes.append(f"S-ID references checked: {sid_checked}")

# --- Markdown checks -------------------------------------------------------
req_labels = ["RESEARCH SCREEN", "NOT LEGAL ADVICE", "NO PATENTABILITY CONCLUSION",
              "NO FREEDOM-TO-OPERATE CONCLUSION"]
for path in (CONCEPTS, CHECKLIST):
    md = open(path, encoding="utf-8").read()
    for lab in req_labels:
        if lab not in md:
            errors.append(f"{os.path.basename(path)}: missing label {lab!r}")
    # relative links resolve
    for link in re.findall(r"\]\(((?!https?:)[^)#]+)\)", md):
        target = os.path.normpath(os.path.join(os.path.dirname(path), link))
        if not os.path.exists(target):
            errors.append(f"{os.path.basename(path)}: broken link {link}")
    # PA references resolve to CSV ids
    for pa in set(re.findall(r"PA-[PN]\d\d", md)):
        if pa not in ids:
            errors.append(f"{os.path.basename(path)}: unknown prior-art id {pa}")

md = open(CONCEPTS, encoding="utf-8").read()
for cc in [f"CC-{i}" for i in range(1, 7)]:
    if cc not in md:
        errors.append(f"Concepts doc missing {cc}")
pa_used = len(set(re.findall(r"PA-[PN]\d\d", md)))
notes.append(f"Concepts doc cites {pa_used} distinct prior-art rows")

ck = open(CHECKLIST, encoding="utf-8").read()
for sect in ["Materials to preserve", "advisor", "OTL", "inventorship",
             "arXiv", "Sequence and decision owner", "policy links",
             "accessed 2026-07-25"]:
    if sect.lower() not in ck.lower():
        errors.append(f"Checklist missing expected content: {sect!r}")
for url_frag in ["otl.stanford.edu", "doresearch.stanford.edu", "uspto.gov", "wipo.int"]:
    if url_frag not in ck:
        errors.append(f"Checklist missing official link domain {url_frag}")

print("\n".join("NOTE: " + n for n in notes))
if errors:
    print("\n".join("ERROR: " + e for e in errors))
    print("RESULT: FAIL")
    sys.exit(1)
print("RESULT: PASS")
