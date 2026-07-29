# Stage 10D output validator (reusable): parses the final ledger, new-source
# audit, and evidence map; checks schema, uniqueness, enums, numeric gates,
# and cross-file referential integrity. Exit code 0 = all gates pass.
import csv, re, sys
from collections import Counter

BASE = r"D:\timzhao\Downloads\P_FIXED\P\01\08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07"
SIX = r"D:\timzhao\Downloads\P_FIXED\P\01\06\outputs\01_SOURCE_LEDGER.csv"
LHDR = ("source_id,citation,title,authors,year,venue,doi,url,source_type,"
        "peer_review_status,quality_tier,topic_tags,claims_supported,"
        "verification_basis,access_level,notes").split(",")
AHDR = ["source_id", "normalized_doi", "normalized_title",
        "found_in_folder_06", "evidence", "new_source_flag"]
EHDR = ["claim_id", "claim", "claim_type", "source_ids", "evidence_strength",
        "counterevidence_ids", "limitations", "used_by_stage"]

def norm_doi(d):
    d = (d or "").strip().lower()
    for p in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/",
              "http://dx.doi.org/", "doi:"):
        if d.startswith(p):
            d = d[len(p):]
    return d

def norm_title(t):
    t = (t or "").lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def load(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

fails = []
def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    if not cond:
        fails.append(name)

# ---- ledger ----
led = load(BASE + r"\outputs\01_SOURCE_LEDGER.csv")
check("ledger header exact", list(led[0].keys()) == LHDR)
ids = [r["source_id"] for r in led]
check("ledger source_id unique", len(ids) == len(set(ids)), f"{len(ids)} rows")
dois = [norm_doi(r["doi"]) for r in led]
check("ledger normalized DOI unique", len(dois) == len(set(dois)))
titles = [norm_title(r["title"]) for r in led]
check("ledger normalized title unique", len(titles) == len(set(titles)))
ST = {"verified_peer_reviewed", "not_peer_reviewed", "peer_review_uncertain"}
check("peer_review_status enum", all(r["peer_review_status"] in ST for r in led))
check("quality_tier enum", all(r["quality_tier"] in {"A", "B", "C"} for r in led))
check("access enum", all(r["access_level"] in
      {"full_text", "abstract_metadata", "metadata_only"} for r in led))
ver = [r for r in led if r["peer_review_status"] == "verified_peer_reviewed"]
check("gate: >=120 verified", len(ver) >= 120, f"{len(ver)} verified / {len(led)} rows")

six = load(SIX)
six_doi = {norm_doi(r["doi"]) for r in six}
six_t = {norm_title(r["title"]) for r in six}
new_ver = [r for r in ver if norm_doi(r["doi"]) not in six_doi
           and norm_title(r["title"]) not in six_t]
check("gate: >=75 verified new vs 06", len(new_ver) >= 75, f"{len(new_ver)} new")

qc = Counter()
for r in ver:
    for t in r["topic_tags"].split(";"):
        if t.startswith("quota_"):
            qc[t] += 1
for tag, need in [("quota_hybrid_coil", 25), ("quota_radiation", 30),
                  ("quota_applications_alternatives", 25),
                  ("quota_calibration_observability", 20)]:
    check(f"gate: {tag} >= {need}", qc[tag] >= need, f"{qc[tag]}")

# ---- audit ----
aud = load(BASE + r"\outputs\01_NEW_SOURCE_AUDIT.csv")
check("audit header exact", list(aud[0].keys()) == AHDR)
check("audit rows == ledger rows", len(aud) == len(led), f"{len(aud)}")
check("audit ids match ledger 1:1", [a["source_id"] for a in aud] == ids)
bad = []
for a in aud:
    is06 = norm_doi_hit = a["normalized_doi"] in six_doi or a["normalized_title"] in six_t
    flag_ok = (a["new_source_flag"] == "reused") == bool(is06)
    f06_ok = (a["found_in_folder_06"] != "no") == bool(is06)
    if not (flag_ok and f06_ok):
        bad.append(a["source_id"])
check("audit flags consistent with recomputed 06 overlap", not bad, str(bad))

# ---- evidence map ----
ev = load(BASE + r"\outputs\01_EVIDENCE_MAP.csv")
check("evidence-map header exact", list(ev[0].keys()) == EHDR)
cids = [e["claim_id"] for e in ev]
check("claim_id unique", len(cids) == len(set(cids)), f"{len(cids)} claims")
CT = {"observed", "derived", "inferred", "proposed", "unknown"}
check("claim_type enum", all(e["claim_type"] in CT for e in ev))
idset = set(ids)
dangling = [(e["claim_id"], s) for e in ev
            for s in (e["source_ids"].split(";") + e["counterevidence_ids"].split(";"))
            if s and s not in idset]
check("all claim source/counter IDs exist in ledger", not dangling, str(dangling))

# ---- summary counts for the coverage doc ----
print("\n--- summary (verified rows) ---")
print("status:", dict(Counter(r["peer_review_status"] for r in led)))
print("tier:", dict(Counter(r["quality_tier"] for r in ver)))
print("access:", dict(Counter(r["access_level"] for r in ver)))
print("type:", dict(Counter(r["source_type"] for r in ver)))
print("lane:", dict(Counter(r["source_id"][0] for r in ver)))
print("quotas:", dict(qc))
yrs = Counter((r["year"][:3] + "0s") for r in ver if r["year"])
print("decades:", dict(sorted(yrs.items())))
roles = Counter()
for r in ver:
    tg = set(r["topic_tags"].split(";"))
    if "direct_hybrid" in tg: roles["direct_hybrid"] += 1
    if tg & {"direct_hall_neutron", "direct_hall_gamma",
             "direct_hall_proton_electron_heavyion"}: roles["direct_hall_radiation"] += 1
    if tg & {"enabling_only", "enabling_physics_wbg", "enabling_physics_iii_v",
             "enabling_physics_si_soi"}: roles["enabling"] += 1
    if "context_only" in tg: roles["context_only"] += 1
    if r["source_type"] == "review_article": roles["review_article"] += 1
print("roles:", dict(roles))
new_all = sum(1 for a in aud if a["new_source_flag"] == "new")
print("audit: new", new_all, "reused", len(aud) - new_all)

print(f"\n{'ALL GATES PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}")
sys.exit(1 if fails else 0)
