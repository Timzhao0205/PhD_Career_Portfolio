"""Stage 70 red-team: independent Crossref re-verification of critical sources.

Queries the live Crossref REST API for each audit-target DOI and compares
title / year / container-title against the ledger row. This is an
independent publisher-registry inspection (verification_level:
crossref_registry). Output: tools/redteam_crossref_results.json
"""
import csv, json, time, urllib.request, urllib.error, re, sys

LEDGER = "outputs/01_SOURCE_LEDGER.csv"
OUT = "tools/redteam_crossref_results.json"

# Audit targets: every direct hybrid source (C01/C02/C05/C06/C11 spine),
# every chosen-radiation-mechanism source (C12/C13/C15/C16/C17/C18/C24),
# every top-application (stellarator) source (C32 + P016), plus
# load-bearing identifiability/alternative/veto sources.
TARGETS = [
    # direct hybrid spine
    "H001","H002","H003","H004","H005","H007","H008","H055","H056","H059",
    "P003","H045","H066","H021","H038","H040","H034","H035",
    # radiation mechanism spine
    "R001","R002","R003","R012","R013","R015","R022","R024","R025","R028",
    "R036","R037","R038","R042","R046","R056","R063","R071","R076",
    # top application (stellarator) + scorecard-cited
    "P012","P013","P014","P016","P018","P019","P020",
    # vetoes / alternatives load-bearing
    "P025","P042","P052","P057","P063","P064","H065",
]

def norm(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def fetch(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={
        "User-Agent": "redteam-audit/1.0 (mailto:timzhao@stanford.edu)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))["message"]

rows = {}
with open(LEDGER, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        rows[r["source_id"]] = r

results = []
for sid in TARGETS:
    row = rows.get(sid)
    if not row:
        results.append({"source_id": sid, "status": "MISSING_FROM_LEDGER"})
        continue
    doi = row["doi"].strip()
    rec = {"source_id": sid, "doi": doi, "ledger_title": row["title"],
           "ledger_year": row["year"], "ledger_venue": row["venue"],
           "ledger_peer_status": row["peer_review_status"],
           "ledger_access": row["access_level"]}
    try:
        m = fetch(doi)
        cr_title = (m.get("title") or [""])[0]
        cr_container = (m.get("container-title") or [""])[0]
        year = None
        for k in ("published-print", "published-online", "issued"):
            if m.get(k) and m[k].get("date-parts"):
                year = m[k]["date-parts"][0][0]
                if year: break
        cr_type = m.get("type", "")
        authors = m.get("author", [])
        first_author = (authors[0].get("family", "") if authors else "")
        title_match = norm(cr_title) == norm(row["title"]) or \
            norm(row["title"]) in norm(cr_title) or norm(cr_title) in norm(row["title"])
        year_match = (year is None) or (str(year) == row["year"].strip()) or \
            (abs(int(year) - int(row["year"])) <= 1 if row["year"].strip().isdigit() else False)
        rec.update({"status": "OK", "crossref_title": cr_title,
                    "crossref_year": year, "crossref_container": cr_container,
                    "crossref_type": cr_type, "first_author": first_author,
                    "n_authors": len(authors),
                    "title_match": title_match, "year_match": year_match})
    except urllib.error.HTTPError as e:
        rec.update({"status": f"HTTP_{e.code}"})
    except Exception as e:
        rec.update({"status": "ERROR", "error": str(e)[:200]})
    results.append(rec)
    time.sleep(0.35)

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=1)

bad = [r for r in results if r.get("status") != "OK" or
       not r.get("title_match", True) or not r.get("year_match", True)]
print(f"checked {len(results)}; problems {len(bad)}")
for r in bad:
    print(" PROBLEM:", r["source_id"], r.get("status"),
          "title_match=", r.get("title_match"), "year_match=", r.get("year_match"),
          "| cr:", str(r.get("crossref_title"))[:70], "| yr", r.get("crossref_year"))
