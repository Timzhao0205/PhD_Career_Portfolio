"""Stage 70 independent deterministic audit of outputs/01_SOURCE_LEDGER.csv.

Written fresh for the red-team stage (does not reuse 10d_validate.py logic)
so that a bug in the original validator cannot hide the same bug here.
"""
import csv
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "outputs" / "01_SOURCE_LEDGER.csv"

EXPECTED_HEADER = (
    "source_id,citation,title,authors,year,venue,doi,url,source_type,"
    "peer_review_status,quality_tier,topic_tags,claims_supported,"
    "verification_basis,access_level,notes"
).split(",")

ALLOWED_STATUS = {"verified_peer_reviewed"}
DISALLOWED_TYPES = {
    "preprint", "arxiv", "patent", "thesis", "dissertation", "vendor_note",
    "application_note", "standard", "book", "book_chapter", "news", "blog",
    "university_page", "grant_page", "ai_summary", "website", "webpage",
    "report", "white_paper", "dataset",
}
ALLOWED_TIERS = {"A", "B", "C"}
ALLOWED_ACCESS = {"full_text", "abstract_metadata", "metadata_only"}


def norm_doi(doi: str) -> str:
    d = doi.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d


def norm_title(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9]+", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()


def main() -> int:
    problems = []
    with open(LEDGER, encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [r for r in reader if any(cell.strip() for cell in r)]

    if header != EXPECTED_HEADER:
        problems.append(f"HEADER MISMATCH: {header}")

    n = len(rows)
    print(f"rows (excluding header): {n}")

    widths = Counter(len(r) for r in rows)
    if set(widths) != {len(EXPECTED_HEADER)}:
        problems.append(f"COLUMN WIDTHS: {dict(widths)}")

    recs = [dict(zip(EXPECTED_HEADER, r)) for r in rows]

    ids = [r["source_id"] for r in recs]
    dup_ids = [k for k, v in Counter(ids).items() if v > 1]
    if dup_ids:
        problems.append(f"DUPLICATE source_id: {dup_ids}")
    bad_ids = [i for i in ids if not re.fullmatch(r"S\d{4}", i)]
    if bad_ids:
        problems.append(f"BAD ID FORMAT: {bad_ids}")

    id_nums = sorted(int(i[1:]) for i in ids if re.fullmatch(r"S\d{4}", i))
    gaps = []
    if id_nums:
        expected = set(range(id_nums[0], id_nums[-1] + 1))
        gaps = sorted(expected - set(id_nums))
    print(f"id range: S{id_nums[0]:04d}..S{id_nums[-1]:04d}, gaps: "
          f"{['S%04d' % g for g in gaps] if gaps else 'none'}")

    dois = [norm_doi(r["doi"]) for r in recs if r["doi"].strip()]
    missing_doi = [r["source_id"] for r in recs if not r["doi"].strip()]
    dup_dois = {k: v for k, v in Counter(dois).items() if v > 1}
    if dup_dois:
        for d in dup_dois:
            owners = [r["source_id"] for r in recs if norm_doi(r["doi"]) == d]
            problems.append(f"DUPLICATE DOI {d}: {owners}")
    if missing_doi:
        print(f"rows without DOI: {missing_doi}")

    titles = Counter(norm_title(r["title"]) for r in recs)
    dup_titles = [t for t, v in titles.items() if v > 1]
    if dup_titles:
        for t in dup_titles:
            owners = [r["source_id"] for r in recs if norm_title(r["title"]) == t]
            problems.append(f"DUPLICATE TITLE '{t[:60]}': {owners}")

    bad_status = [(r["source_id"], r["peer_review_status"]) for r in recs
                  if r["peer_review_status"] not in ALLOWED_STATUS]
    if bad_status:
        problems.append(f"NON-VERIFIED STATUS ROWS: {bad_status}")
    n_verified = sum(1 for r in recs
                     if r["peer_review_status"] == "verified_peer_reviewed")
    print(f"verified_peer_reviewed rows: {n_verified} (minimum 150)")
    if n_verified < 150:
        problems.append(f"COUNT BELOW MINIMUM: {n_verified} < 150")

    type_counts = Counter(r["source_type"] for r in recs)
    print(f"source_type counts: {dict(type_counts)}")
    bad_types = [(r["source_id"], r["source_type"]) for r in recs
                 if r["source_type"].lower() in DISALLOWED_TYPES]
    if bad_types:
        problems.append(f"DISALLOWED SOURCE TYPES: {bad_types}")

    bad_tier = [(r["source_id"], r["quality_tier"]) for r in recs
                if r["quality_tier"] not in ALLOWED_TIERS]
    if bad_tier:
        problems.append(f"BAD TIER: {bad_tier}")
    print(f"tier counts: {dict(Counter(r['quality_tier'] for r in recs))}")

    bad_access = [(r["source_id"], r["access_level"]) for r in recs
                  if r["access_level"] not in ALLOWED_ACCESS]
    if bad_access:
        problems.append(f"BAD ACCESS LEVEL: {bad_access}")
    print(f"access counts: {dict(Counter(r['access_level'] for r in recs))}")

    bad_years = []
    for r in recs:
        y = r["year"].strip()
        if not re.fullmatch(r"(19|20)\d{2}", y):
            bad_years.append((r["source_id"], y))
        elif not (1950 <= int(y) <= 2026):
            bad_years.append((r["source_id"], y))
    if bad_years:
        problems.append(f"BAD YEARS: {bad_years}")
    ydist = Counter(r["year"] for r in recs)
    print("year distribution: " + ", ".join(
        f"{y}:{c}" for y, c in sorted(ydist.items())))

    bad_url = []
    for r in recs:
        u = r["url"].strip()
        if not u.startswith("https://"):
            bad_url.append((r["source_id"], u[:50]))
        d = r["doi"].strip()
        if d and u.startswith("https://doi.org/"):
            if norm_doi(u) != norm_doi(d):
                bad_url.append((r["source_id"], f"url/doi mismatch {u}"))
    if bad_url:
        problems.append(f"URL ISSUES: {bad_url}")

    empty_fields = defaultdict(list)
    for r in recs:
        for col in ("citation", "title", "authors", "venue", "topic_tags",
                    "claims_supported", "verification_basis"):
            if not r[col].strip():
                empty_fields[col].append(r["source_id"])
    if empty_fields:
        problems.append(f"EMPTY REQUIRED FIELDS: {dict(empty_fields)}")

    # access-level vs verification-basis consistency: a row claiming
    # full_text should not have a metadata-only basis, and vice versa a
    # metadata_only row must not claim abstract/body reading.
    suspicious_access = []
    for r in recs:
        basis = r["verification_basis"].lower()
        if r["access_level"] == "metadata_only" and (
                "abstract confirmed" in basis or "full text" in basis
                or "read the pdf" in basis):
            suspicious_access.append((r["source_id"], "metadata_only+body-read basis"))
    if suspicious_access:
        problems.append(f"ACCESS/BASIS INCONSISTENCY: {suspicious_access}")

    # topic-group coverage snapshot (audit-oriented, coarse regex buckets)
    groups = {
        "gan_wbg_hall": r"gan|algan|2deg|hemt|wide.?bandgap|sic\b",
        "hall_metrology": r"hall|offset|spinning|sensitivit|magnetometer|noise",
        "fusion_diag": r"fusion|tokamak|stellarator|plasma|diagnost|mirnov|b-dot|bdot|pickup",
        "hsx_stell": r"hsx|quasi.?helic|stellarator",
        "uncertainty_cal": r"calibrat|uncertaint|traceab|metrolog|gum\b|repeatab",
        "methods_ml": r"machine learning|neural|inverse|reconstruct|bayesian|kalman|digital twin|data fusion|signal",
    }
    cov = Counter()
    for r in recs:
        hay = (r["topic_tags"] + ";" + r["title"]).lower()
        for g, pat in groups.items():
            if re.search(pat, hay):
                cov[g] += 1
    print(f"coarse topic coverage: {dict(cov)}")

    print()
    if problems:
        print("PROBLEMS FOUND:")
        for p in problems:
            print(" -", p)
        return 1
    print("DETERMINISTIC LEDGER AUDIT: PASS (no schema/count/duplicate/type defects)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
