"""Stage 70 red-team: OpenAlex fallback abstracts for sources Crossref/S2 lack."""
import json, time, urllib.request, urllib.parse

DOIS = {
    "R071": "10.1016/j.fusengdes.2013.02.055",
    "H007": "10.1109/TNS.2012.2188816",
    "H002": "10.1016/j.fusengdes.2025.115180",
    "P012": "10.1016/j.fusengdes.2005.06.124",
    "P016": "10.1016/0920-3796(93)90027-f",
    "R022": "10.1063/1.4929583",
    "R046": "10.1016/j.nima.2016.05.072",
    "R063": "10.3390/s25216552",
    "R076": "10.1016/j.fusengdes.2019.03.055",
    "H021": "10.3390/s16091407",
    "H038": "10.1016/s0924-4247(01)00857-3",
    "H056": "10.1016/j.sna.2007.08.030",
    "R028": "10.3390/nano12132126",
    "H040": "10.1063/1.4808366",
    "P025": "10.1063/5.0076741",
}

def deinvert(inv):
    if not inv: return None
    pos = {}
    for w, idxs in inv.items():
        for i in idxs: pos[i] = w
    return " ".join(pos[i] for i in sorted(pos))

out = {}
for sid, doi in DOIS.items():
    url = "https://api.openalex.org/works/https://doi.org/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={"User-Agent": "redteam/1.0 (mailto:timzhao@stanford.edu)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            m = json.loads(r.read().decode())
        out[sid] = {"doi": doi, "title": m.get("title"),
                    "year": m.get("publication_year"),
                    "venue": (m.get("primary_location") or {}).get("source", {}).get("display_name") if (m.get("primary_location") or {}).get("source") else None,
                    "abstract": deinvert(m.get("abstract_inverted_index"))}
    except Exception as e:
        out[sid] = {"doi": doi, "error": str(e)[:150]}
    time.sleep(0.4)

with open("tools/redteam_openalex.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)

for sid, e in out.items():
    print("=" * 20, sid, e.get("doi"))
    print(e.get("title"), "|", e.get("year"), "|", e.get("venue"))
    a = e.get("abstract") or e.get("error") or "(no abstract)"
    print(a[:1300])
    print()
