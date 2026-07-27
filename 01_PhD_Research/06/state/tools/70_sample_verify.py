"""Stage 70 stratified source verification.

Deterministic, documented sampling rule (independent of stage 10d's sample,
which was weighted toward 10C/2025-2026/unusual venues):

1. Lane-of-origin (A/B/C from the [Provenance: ...] token) x access_level
   (full_text / abstract_metadata / metadata_only) = 9 cells; the 2 rows
   per cell with the lowest md5(source_id) hex rank are selected.
2. One row per 7-year band (pre-1990, 1990s, 2000-09, 2010-14, 2015-19,
   2020-23, 2024-26) not already selected, again by md5 rank.
3. All tier-C rows not already selected, up to 2, by md5 rank.
4. Targeted load-bearing adds (claims in stages 20-60 lean on them):
   S0128 (QHS wording), S0132 (HSX overview), S0068 (JET Hall probes),
   S0035 (continuous spinning current), S0033 (Munter spinning current),
   S0071 (Mirnov), S0002 (GaN radiation tolerance numbers), S0054
   (Pearton review), S0108 (Strait review), S0121/S0122 (rows corrected
   at 10d - regression check).

Each sampled row is fetched from api.crossref.org and compared on title,
year, venue, first-author family name, and DOI agreement. Output:
state/tools/70_sample_report.json for manual adjudication.
"""
import csv
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "outputs" / "01_SOURCE_LEDGER.csv"
OUT = Path(__file__).with_name("70_sample_report.json")

TARGETED = ["S0128", "S0132", "S0068", "S0035", "S0033", "S0071",
            "S0002", "S0054", "S0108", "S0121", "S0122"]


def h(sid):
    return hashlib.md5(sid.encode()).hexdigest()


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", s.lower())).strip()


def year_band(y):
    y = int(y)
    if y < 1990: return "pre1990"
    if y < 2000: return "1990s"
    if y < 2010: return "2000s"
    if y < 2015: return "2010-14"
    if y < 2020: return "2015-19"
    if y < 2024: return "2020-23"
    return "2024-26"


def lane(row):
    m = re.search(r"\[Provenance:\s*([ABC])\d{4}", row["notes"])
    return m.group(1) if m else "?"


def pick(rows):
    chosen = {}
    # 1. lane x access, 2 each
    cells = {}
    for r in rows:
        cells.setdefault((lane(r), r["access_level"]), []).append(r)
    for key in sorted(cells):
        for r in sorted(cells[key], key=lambda r: h(r["source_id"]))[:2]:
            chosen[r["source_id"]] = f"cell:{key[0]}/{key[1]}"
    # 2. year bands
    bands = {}
    for r in rows:
        bands.setdefault(year_band(r["year"]), []).append(r)
    for b in sorted(bands):
        for r in sorted(bands[b], key=lambda r: h(r["source_id"])):
            if r["source_id"] not in chosen:
                chosen[r["source_id"]] = f"band:{b}"
                break
    # 3. tier C up to 2
    tc = [r for r in rows if r["quality_tier"] == "C"
          and r["source_id"] not in chosen]
    for r in sorted(tc, key=lambda r: h(r["source_id"]))[:2]:
        chosen[r["source_id"]] = "tierC"
    # 4. targeted
    for sid in TARGETED:
        if sid not in chosen:
            chosen[sid] = "targeted"
    return chosen


def fetch(doi):
    url = f"https://api.crossref.org/works/{doi}"
    try:
        p = subprocess.run(
            ["curl", "-s", "--max-time", "30", url],
            capture_output=True, text=True, timeout=40)
        return json.loads(p.stdout)["message"]
    except Exception as e:  # noqa: BLE001
        return {"_error": str(e)}


def main():
    with open(LEDGER, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    by_id = {r["source_id"]: r for r in rows}
    chosen = pick(rows)
    print(f"sample size: {len(chosen)}")

    report = []
    for sid in sorted(chosen):
        r = by_id[sid]
        msg = fetch(r["doi"])
        item = {"source_id": sid, "stratum": chosen[sid],
                "doi": r["doi"], "tier": r["quality_tier"],
                "access": r["access_level"], "year_led": r["year"],
                "led_title": r["title"], "led_venue": r["venue"],
                "led_first_author": r["authors"].split(";")[0].strip(),
                "flags": []}
        if "_error" in msg or "title" not in msg:
            item["flags"].append(f"FETCH_FAIL:{msg.get('_error','no title')}")
            report.append(item)
            print(f"{sid}: FETCH_FAIL")
            continue
        cr_title = (msg.get("title") or [""])[0]
        cr_venue = (msg.get("container-title") or [""])[0]
        years = set()
        for k in ("published-print", "published-online", "issued",
                  "created"):
            v = msg.get(k, {}).get("date-parts", [[None]])
            if v and v[0] and v[0][0]:
                years.add(v[0][0])
        authors = msg.get("author", [])
        cr_first = ""
        for a in authors:
            if a.get("sequence") == "first":
                cr_first = a.get("family", "")
                break
        if not cr_first and authors:
            cr_first = authors[0].get("family", "")
        item.update({"cr_title": cr_title, "cr_venue": cr_venue,
                     "cr_years": sorted(years), "cr_first_author": cr_first,
                     "cr_type": msg.get("type", "")})
        if norm(cr_title) != norm(r["title"]):
            item["flags"].append("TITLE_DIFF")
        if int(r["year"]) not in years:
            item["flags"].append("YEAR_DIFF")
        if norm(cr_venue) != norm(r["venue"]) and \
                norm(r["venue"]) not in norm(cr_venue) and \
                norm(cr_venue) not in norm(r["venue"]):
            item["flags"].append("VENUE_DIFF")
        led_fam = norm(item["led_first_author"].split()[-1]) if \
            item["led_first_author"] else ""
        if led_fam and norm(cr_first) != led_fam and \
                led_fam not in norm(cr_first):
            item["flags"].append("AUTHOR_DIFF")
        report.append(item)
        print(f"{sid}: {'OK' if not item['flags'] else item['flags']}")

    OUT.write_text(json.dumps(report, indent=1), encoding="utf-8")
    n_flag = sum(1 for i in report if i["flags"])
    print(f"\nwrote {OUT.name}: {len(report)} rows, {n_flag} flagged for "
          "manual adjudication")


if __name__ == "__main__":
    sys.exit(main())
