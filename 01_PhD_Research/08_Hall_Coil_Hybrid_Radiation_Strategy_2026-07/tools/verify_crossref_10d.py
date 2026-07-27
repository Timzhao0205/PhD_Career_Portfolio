# Stage 10D independent verification: re-check every final-ledger DOI against
# the live Crossref API; compare normalized title and year; capture author
# lists for rows whose lane metadata left authors unresolved.
import json, re, time, urllib.request, urllib.error

BASE = r"D:\timzhao\Downloads\P_FIXED\P\01\08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07"
MAILTO = "timzhao@stanford.edu"

def norm_title(t):
    t = (t or "").lower()
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def overlap(a, b):
    A, B = set(norm_title(a).split()), set(norm_title(b).split())
    if not A or not B:
        return 0.0
    return len(A & B) / min(len(A), len(B))

def fetch(doi, tries=3):
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}?mailto={MAILTO}"
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)["message"], None
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None, "404"
            if e.code == 429:
                time.sleep(3 + 3 * i)
                continue
            return None, f"http {e.code}"
        except Exception as e:
            time.sleep(1 + i)
            err = str(e)[:80]
    return None, err if 'err' in dir() else "retries exhausted"

def year_of(m):
    for k in ("published-print", "published-online", "issued", "created"):
        try:
            return m[k]["date-parts"][0][0]
        except Exception:
            continue
    return None

def main():
    rows = json.load(open(BASE + r"\tools\rows_for_verification.json", encoding="utf-8"))
    results, mismatches = [], []
    for i, r in enumerate(rows):
        m, err = fetch(r["doi"])
        rec = {"id": r["id"], "doi": r["doi"]}
        if m is None:
            rec.update(status="FETCH_FAIL", error=err)
            mismatches.append(rec)
        else:
            cr_title = (m.get("title") or [""])[0]
            cr_year = year_of(m)
            cr_venue = (m.get("container-title") or [""])[:1]
            auth = m.get("author") or []
            rec.update(status="ok",
                       cr_title=cr_title,
                       cr_year=cr_year,
                       cr_venue=cr_venue[0] if cr_venue else "",
                       cr_type=m.get("type", ""),
                       n_authors=len(auth),
                       authors="; ".join(
                           f"{a.get('given','')} {a.get('family','')}".strip()
                           for a in auth)[:1200],
                       title_overlap=round(overlap(r["title"], cr_title), 2),
                       ledger_year=r["year"])
            try:
                ydiff = abs(int(cr_year) - int(r["year"]))
            except Exception:
                ydiff = 99
            if rec["title_overlap"] < 0.6 or ydiff > 1:
                rec["status"] = "MISMATCH"
                mismatches.append(rec)
        results.append(rec)
        if (i + 1) % 25 == 0:
            print(f"{i+1}/{len(rows)} checked, {len(mismatches)} flagged")
        time.sleep(0.25)
    with open(BASE + r"\tools\crossref_verification_10d.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1)
    ok = sum(1 for x in results if x["status"] == "ok")
    print(f"\nDONE: {len(results)} rows, {ok} clean, {len(mismatches)} flagged")
    for x in mismatches:
        print(json.dumps(x, indent=None)[:400])

if __name__ == "__main__":
    import urllib.parse
    main()
