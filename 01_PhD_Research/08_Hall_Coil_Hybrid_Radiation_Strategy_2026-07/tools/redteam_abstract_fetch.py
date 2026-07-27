"""Stage 70 red-team: fetch publisher-deposited abstracts for deep checks.

For each DOI: try Crossref 'abstract' field (publisher-deposited JATS), then
Semantic Scholar Graph API. Saves tools/redteam_abstracts.json and prints
plain-text abstracts for inspection.
"""
import json, re, time, urllib.request, urllib.parse

DOIS = {
    "R042": "10.1063/5.0318998",
    "R003": "10.3390/s22145258",
    "R001": "10.1063/1.3479115",
    "R002": "10.1109/TNS.2019.2912720",
    "R071": "10.1016/j.fusengdes.2013.02.055",
    "P003": "10.1063/1.4964435",
    "H059": "10.1109/TASC.2018.2801325",
    "H004": "10.3390/s22010182",
    "H001": "10.1088/1741-4326/adb599",
    "H002": "10.1016/j.fusengdes.2025.115180",
    "H003": "10.1088/1741-4326/ac8aad",
    "H007": "10.1109/TNS.2012.2188816",
    "P013": "10.1088/1361-6587/aae96b",
    "P012": "10.1016/j.fusengdes.2005.06.124",
    "P016": "10.1016/0920-3796(93)90027-f",
    "R012": "10.1063/1.4805357",
    "R025": "10.1038/s41598-020-72862-2",
    "P057": "10.1063/1.3675578",
    "P042": "10.1088/1361-6668/ac2120",
    "H065": "10.1016/j.fusengdes.2019.01.013",
}

def strip_jats(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", s).strip()

def crossref_abs(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={"User-Agent": "redteam/1.0 (mailto:timzhao@stanford.edu)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        m = json.loads(r.read().decode())["message"]
    return strip_jats(m.get("abstract", ""))

def s2_abs(doi):
    url = ("https://api.semanticscholar.org/graph/v1/paper/DOI:" + urllib.parse.quote(doi)
           + "?fields=title,abstract,year,venue,openAccessPdf")
    req = urllib.request.Request(url, headers={"User-Agent": "redteam/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        m = json.loads(r.read().decode())
    return m

out = {}
for sid, doi in DOIS.items():
    entry = {"doi": doi}
    try:
        entry["crossref_abstract"] = crossref_abs(doi)
    except Exception as e:
        entry["crossref_abstract_error"] = str(e)[:120]
    time.sleep(0.3)
    try:
        m = s2_abs(doi)
        entry["s2_title"] = m.get("title")
        entry["s2_year"] = m.get("year")
        entry["s2_venue"] = m.get("venue")
        entry["s2_abstract"] = m.get("abstract")
        oa = m.get("openAccessPdf") or {}
        entry["s2_oa_pdf"] = oa.get("url")
    except Exception as e:
        entry["s2_error"] = str(e)[:120]
    time.sleep(0.5)
    out[sid] = entry

with open("tools/redteam_abstracts.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)

for sid, e in out.items():
    a = e.get("crossref_abstract") or e.get("s2_abstract") or "(no abstract retrieved)"
    print("=" * 20, sid, e["doi"])
    print("S2:", e.get("s2_title"), "|", e.get("s2_year"), "|", e.get("s2_venue"), "| OA:", e.get("s2_oa_pdf"))
    print(a[:1400])
    print()
