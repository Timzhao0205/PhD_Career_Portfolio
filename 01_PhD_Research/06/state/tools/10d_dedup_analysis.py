"""Stage 10D: dedup analysis across the three lane CSVs (read-only)."""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILES = [
    ROOT / "evidence" / "10A_GAN_WBG_SOURCES.csv",
    ROOT / "evidence" / "10B_FUSION_DIAGNOSTICS_SOURCES.csv",
    ROOT / "evidence" / "10C_METHODS_SOURCES.csv",
]

EXPECTED_HEADER = (
    "source_id,citation,title,authors,year,venue,doi,url,source_type,"
    "peer_review_status,quality_tier,topic_tags,claims_supported,"
    "verification_basis,access_level,notes"
).split(",")


def norm_doi(d):
    d = d.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", "", t.lower())


rows = []
for f in FILES:
    with open(f, encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh)
        if r.fieldnames != EXPECTED_HEADER:
            print(f"HEADER MISMATCH in {f.name}: {r.fieldnames}")
            sys.exit(1)
        n = 0
        for row in r:
            row["_file"] = f.name
            rows.append(row)
            n += 1
        print(f"{f.name}: {n} rows")

print(f"TOTAL rows: {len(rows)}")

# DOI duplicates
doi_map = {}
for row in rows:
    doi_map.setdefault(norm_doi(row["doi"]), []).append(row["source_id"])
dups = {d: ids for d, ids in doi_map.items() if len(ids) > 1}
print(f"\nDuplicate normalized DOIs: {len(dups)}")
for d, ids in dups.items():
    print(f"  {d}: {ids}")

# Title duplicates (across different DOIs)
title_map = {}
for row in rows:
    title_map.setdefault(norm_title(row["title"]), []).append(
        (row["source_id"], norm_doi(row["doi"]))
    )
tdups = {t: v for t, v in title_map.items() if len(v) > 1}
print(f"\nDuplicate normalized titles: {len(tdups)}")
for t, v in tdups.items():
    dois = {d for _, d in v}
    flag = "SAME-DOI" if len(dois) == 1 else "*** DIFFERENT DOIs ***"
    print(f"  [{flag}] {[i for i, _ in v]} -> {dois}")

# Empty required fields
required = [
    "source_id", "citation", "title", "authors", "year", "venue", "doi",
    "url", "source_type", "peer_review_status", "quality_tier",
    "topic_tags", "claims_supported", "verification_basis", "access_level",
]
for row in rows:
    for k in required:
        if not row[k].strip():
            print(f"EMPTY FIELD {k} in {row['source_id']}")

# Enum checks
for row in rows:
    if row["peer_review_status"] != "verified_peer_reviewed":
        print(f"NON-VERIFIED STATUS: {row['source_id']} = {row['peer_review_status']}")
    if row["quality_tier"] not in ("A", "B", "C"):
        print(f"BAD TIER: {row['source_id']} = {row['quality_tier']}")
    if row["access_level"] not in ("full_text", "abstract_metadata", "metadata_only"):
        print(f"BAD ACCESS: {row['source_id']} = {row['access_level']}")
    if row["source_type"] not in ("journal_article", "review_article", "conference_paper"):
        print(f"UNUSUAL SOURCE_TYPE: {row['source_id']} = {row['source_type']}")
    if not re.match(r"^10\.\d{4,9}/\S+$", row["doi"].strip()):
        print(f"MALFORMED DOI: {row['source_id']} = {row['doi']}")
    y = row["year"].strip()
    if not (y.isdigit() and 1900 <= int(y) <= 2026):
        print(f"BAD YEAR: {row['source_id']} = {y}")

print(f"\nUnique DOIs after dedup: {len(doi_map)}")
print("Source types:", Counter(r["source_type"] for r in rows))
print("Checks complete.")
