"""Stage 10D: deterministic validation of outputs/01_SOURCE_LEDGER.csv."""
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "outputs" / "01_SOURCE_LEDGER.csv"

EXPECTED_HEADER = (
    "source_id,citation,title,authors,year,venue,doi,url,source_type,"
    "peer_review_status,quality_tier,topic_tags,claims_supported,"
    "verification_basis,access_level,notes"
).split(",")
REQUIRED_NONEMPTY = EXPECTED_HEADER[:15]  # all but notes
DISALLOWED_TYPES = {"arxiv", "preprint", "patent", "standard", "webpage",
                    "thesis", "supplied_file", "book"}
ALLOWED_TYPES = {"journal_article", "review_article", "conference_paper"}

fails = []


def norm_doi(d):
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", d.strip().lower())


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", "", t.lower())


with open(LEDGER, encoding="utf-8", newline="") as fh:
    r = csv.DictReader(fh)
    if r.fieldnames != EXPECTED_HEADER:
        fails.append(f"header mismatch: {r.fieldnames}")
    rows = list(r)

print(f"rows: {len(rows)}")

# 1. nonempty required fields
for row in rows:
    for k in REQUIRED_NONEMPTY:
        if not row[k].strip():
            fails.append(f"empty {k} in {row['source_id']}")

# 2. unique, well-formed, sequential source IDs
ids = [row["source_id"] for row in rows]
if len(ids) != len(set(ids)):
    fails.append("duplicate source_id")
for i, sid in enumerate(ids, 1):
    if sid != f"S{i:04d}":
        fails.append(f"non-sequential id {sid} at position {i}")
        break

# 3. unique normalized DOI (no blanks present)
dois = [norm_doi(row["doi"]) for row in rows]
blank = [row["source_id"] for row in rows if not row["doi"].strip()]
dupdoi = [d for d, c in Counter(dois).items() if c > 1]
if blank:
    fails.append(f"blank DOIs: {blank}")
if dupdoi:
    fails.append(f"duplicate DOIs: {dupdoi}")
for row in rows:
    if not re.match(r"^10\.\d{4,9}/\S+$", row["doi"].strip()):
        fails.append(f"malformed DOI {row['source_id']}: {row['doi']}")
    if not row["url"].strip().startswith("https://doi.org/"):
        fails.append(f"non-DOI url {row['source_id']}: {row['url']}")

# 3b. unique normalized titles
titles = Counter(norm_title(row["title"]) for row in rows)
duptitle = [t for t, c in titles.items() if c > 1]
if duptitle:
    fails.append(f"duplicate normalized titles: {len(duptitle)}")

# 4. verified peer-reviewed count and type rules
vpr = [row for row in rows if row["peer_review_status"] == "verified_peer_reviewed"]
print(f"verified_peer_reviewed rows: {len(vpr)}")
if len(vpr) < 150:
    fails.append(f"only {len(vpr)} verified_peer_reviewed rows (<150)")
for row in vpr:
    st = row["source_type"].strip().lower()
    if st in DISALLOWED_TYPES:
        fails.append(f"{row['source_id']} disallowed type {st} counted as verified")
    if st not in ALLOWED_TYPES:
        fails.append(f"{row['source_id']} unexpected type {st}")

# 5. enum checks
for row in rows:
    if row["quality_tier"] not in ("A", "B", "C"):
        fails.append(f"bad tier {row['source_id']}")
    if row["access_level"] not in ("full_text", "abstract_metadata", "metadata_only"):
        fails.append(f"bad access {row['source_id']}")
    y = row["year"].strip()
    if not (y.isdigit() and 1900 <= int(y) <= 2026):
        fails.append(f"bad year {row['source_id']}: {y}")

# 6. coverage across SOURCE_POLICY categories (topic_tags + claims_supported)
CATS = {
    "1 GaN/WBG Hall & device physics":
        ["algan", "gan", "inaln", "2deg", "sic", "wbg", "iii-nitride",
         "wide bandgap", "hemt", "ga2o3", "inas", "insb", "gaas"],
    "2 Hall geometry/offset/noise/temp/packaging/calibration":
        ["hall geometry", "offset", "sensitivity", "noise", "spinning",
         "chopper", "temperature", "packaging", "calibration", "bandwidth",
         "linearity", "drift", "van der pauw", "planar hall"],
    "3 MCF & plasma magnetic diagnostics":
        ["tokamak", "fusion", "plasma", "mirnov", "flux loop", "diamagnetic",
         "iter", "demo", "jet", "magnetic diagnostic", "rogowski",
         "equilibrium"],
    "4 Stellarator/HSX-relevant field measurement":
        ["stellarator", "hsx", "w7-x", "quasi-helical", "lhd", "tj-ii",
         "ncsx", "cth", "heliotron", "muse", "torsatron", "w7-as",
         "quasisymmetr", "helically symmetric"],
    "5 Direct vs inductive sensing & drift":
        ["hall probe", "hall sensor", "b-dot", "mirnov", "integrator",
         "pickup coil", "fluxgate", "inductive", "steady-state sensor",
         "drift"],
    "6 Uncertainty/repeatability/traceability/instrumentation":
        ["uncertainty", "calibration", "traceab", "metrology",
         "reproducib", "qualification", "allan", "gum", "monte carlo",
         "repeatab", "device-to-device", "instrument"],
    "7 Low-fabrication novelty methods (modeling/inverse/ML/software)":
        ["kalman", "bayesian", "neural", "machine learning",
         "physics-informed", "digital twin", "inverse", "reconstruction",
         "sensor fusion", "surrogate", "signal processing",
         "reinforcement learning", "system identification", "estimation",
         "regulariz", "lock-in", "correlated double sampling"],
}
print("\nCategory coverage (rows matching topic_tags+claims_supported):")
for cat, keys in CATS.items():
    hits = [
        row["source_id"] for row in rows
        if any(k in (row["topic_tags"] + " " + row["claims_supported"]).lower()
               for k in keys)
    ]
    print(f"  {cat}: {len(hits)}")
    if len(hits) < 10:
        fails.append(f"thin coverage: {cat} = {len(hits)}")

# 7. distributions for the coverage report
print("\nsource_type:", dict(Counter(row["source_type"] for row in rows)))
print("quality_tier:", dict(Counter(row["quality_tier"] for row in rows)))
print("access_level:", dict(Counter(row["access_level"] for row in rows)))
years = [int(row["year"]) for row in rows]
bins = Counter()
for y in years:
    if y < 1990: bins["pre-1990"] += 1
    elif y < 2000: bins["1990-1999"] += 1
    elif y < 2010: bins["2000-2009"] += 1
    elif y < 2015: bins["2010-2014"] += 1
    elif y < 2020: bins["2015-2019"] += 1
    elif y < 2024: bins["2020-2023"] += 1
    else: bins["2024-2026"] += 1
print("year bins:", dict(bins))
print(f"year range: {min(years)}-{max(years)}")
venues = Counter(row["venue"] for row in rows)
print(f"distinct venues: {len(venues)}")
print("top venues:")
for v, c in venues.most_common(15):
    print(f"  {c:3d}  {v}")
tiers_by_lane = Counter()
for row in rows:
    m = re.search(r"Provenance: ([ABC])0", row["notes"])
    if m:
        tiers_by_lane[m.group(1)] += 1
print("rows by lane of origin:", dict(tiers_by_lane))
reverified = sum(1 for row in rows if "re-verified at stage 10D" in row["verification_basis"])
print(f"rows re-verified at 10D: {reverified}")

print("\n" + ("VALIDATION: PASS" if not fails else "VALIDATION: FAIL"))
for f in fails:
    print("  FAIL:", f)
