#!/usr/bin/env python3
"""Build the unified startup source database from every project under 02_Startup.

Seven research projects each recorded their sources in their own shape: five
JSON dialects, a CSV evidence ledger, a patent ledger, and a hand-kept markdown
ledger. This script reads all of them, maps every record onto one schema,
merges records that describe the same document, and writes:

    sources.json      one array of merged source records
    sources.csv       the same records flattened for spreadsheets
    sources.sqlite    sources + occurrences + usage tables, with an FTS5 index
    STATISTICS.md     coverage report
    build_log.json    what was read, what was skipped, and why

The build is deterministic and idempotent: rerunning it on an unchanged tree
produces byte-identical output apart from the timestamp in build_log.json.

    python3 tools/build_source_database.py            # rebuild everything
    python3 tools/build_source_database.py --dry-run  # report, write nothing
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sqlite3
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

DB_DIR = Path(__file__).resolve().parent.parent
STARTUP_ROOT = DB_DIR.parent

# Trees that hold copies rather than research: the deduplicated F06I snapshot,
# offline test fixtures, and Python caches.
EXCLUDED_DIR_PARTS = {"__pycache__", "_adjudication_workdir"}
EXCLUDED_PATH_FRAGMENTS = (
    "07_Frontier_Ideas_Interactive_2026-07/src/06/",
    "07_Frontier_Ideas_Interactive_2026-07/tests/",
    "07_Frontier_Ideas_Interactive_2026-07/pilot/",
    "00_SOURCE_DATABASE/",
)

# Filename patterns that hold source records.
SOURCE_FILE_RE = re.compile(
    r"(sources?\.json|_sources\.json|SOURCES\.json|ADD_SOURCES\.json"
    r"|patent_ledger\.json|_patents\.json|source_evidence_ledger.*\.csv)$",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Field mapping
# ---------------------------------------------------------------------------

TITLE_KEYS = ("title", "source_title", "title_en", "title_original",
              "title_translation", "title_translated")
ORIGINAL_TITLE_KEYS = ("title_original", "title_zh")
URL_KEYS = ("url", "source_url_or_citation", "peer_review_evidence_url")
PUBLISHER_KEYS = ("publisher", "venue", "journal", "domain")
AUTHOR_KEYS = ("authors_or_org", "authors", "author", "inventors")
DATE_KEYS = ("date", "published_at", "publication_date", "pub_date",
             "grant_date", "filing_date", "priority_date")
ACCESSED_KEYS = ("accessed", "accessed_at", "date_accessed")
TIER_KEYS = ("tier", "source_tier")
LANG_KEYS = ("lang", "language")
TYPE_KEYS = ("source_type", "type")
CLAIM_KEYS = ("claim_supported", "claim", "relevance_sentence", "evidence_note",
              "finding", "indep_claim_gist", "supports")
NOTE_KEYS = ("notes", "note", "limitations", "status_note", "rejection_reason",
             "publication_note")
USED_IN_KEYS = ("used_in", "used_for", "lane_ids", "idea_ids", "used_in_idea_ids",
                "candidate", "cluster", "alt_ids", "ids_pool")
VERIFY_KEYS = ("verified", "fetched")
ACCESS_KEYS = ("access_level", "access")

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
ARXIV_RE = re.compile(r"(?:arxiv\.org/(?:abs|pdf)/)?(\d{4}\.\d{4,5})(?:v\d+)?")
# Patent publication numbers run to at least six digits; the 4-digit floor a
# looser pattern would allow swallows bare years out of date strings.
PATENT_NUM_RE = re.compile(r"([A-Z]{2}\d{6,}(?:[A-Z]\d?)?)")


def patent_stem(number):
    """Country code + serial, with the kind code dropped.

    `US12196792` and `US12196792B2` are the same publication recorded with and
    without its kind code, so identity is compared on the stem while the fuller
    form is kept for display.
    """
    if not number:
        return None
    m = re.match(r"([A-Z]{2})(\d+)", str(number).upper())
    return m.group(1) + m.group(2) if m else str(number).upper()

TYPE_CANON = {
    "academic_peer_reviewed": "academic",
    "academic": "academic",
    "journal": "academic",
    "paper": "academic",
    "peer_reviewed": "academic",
    "preprint": "preprint",
    "arxiv": "preprint",
    "patent": "patent",
    "patent_application": "patent",
    "government": "government",
    "government_policy": "government",
    "policy": "government",
    "regulatory": "government",
    "standard": "standards",
    "standards": "standards",
    "industry": "industry",
    "industry_report": "industry",
    "market_report": "industry",
    "analyst": "industry",
    "company": "company",
    "company_primary": "company",
    "vendor": "company",
    "datasheet": "company",
    "news": "news",
    "news_media": "news",
    "media": "news",
    "trade_press": "news",
    "dataset": "dataset",
    "database": "dataset",
    "thesis": "academic",
    "conference": "academic",
    "book": "book",
}

# The projects also used ~120 free-text type labels ("wire (reuters)",
# "standards-body roadmap", "sec 10-k"). Fold them onto the canonical set by
# keyword, first match wins. The original label is kept in source_types_raw.
TYPE_KEYWORDS = (
    ("patent", "patent"),
    ("preprint", "preprint"),
    ("arxiv", "preprint"),
    ("peer-review", "academic"),
    ("peer review", "academic"),
    ("journal", "academic"),
    ("academic", "academic"),
    ("conference", "academic"),
    ("proceedings", "academic"),
    ("npl", "academic"),
    ("thesis", "academic"),
    ("university", "academic"),
    ("research institute", "academic"),
    ("national_lab", "academic"),
    ("national lab", "academic"),
    ("standard", "standards"),
    ("think", "think_tank"),
    ("sec ", "company"),
    ("10-k", "company"),
    ("filing", "company"),
    ("company", "company"),
    ("vendor", "company"),
    ("datasheet", "company"),
    ("product", "company"),
    ("regulat", "government"),
    ("gov", "government"),
    ("agency", "government"),
    ("federal", "government"),
    ("intergovernmental", "government"),
    ("intl agency", "government"),
    ("intl-agency", "government"),
    ("international agency", "government"),
    ("solicitation", "government"),
    ("procurement", "government"),
    ("legal", "government"),
    ("statistic", "dataset"),
    ("dataset", "dataset"),
    ("benchmark", "dataset"),
    ("market", "industry"),
    ("analyst", "industry"),
    ("industry", "industry"),
    ("consultancy", "industry"),
    ("consortium", "industry"),
    ("association", "industry"),
    ("trade", "industry"),
    ("research report", "industry"),
    ("journalism", "news"),
    ("press", "news"),
    ("wire", "news"),
    ("news", "news"),
    ("media", "news"),
    ("relay", "news"),
)


# Values that mean "nothing recorded here". The translation fields in the
# CryoFree prior-art ledgers use several of these instead of null.
# How firmly the content behind the URL was confirmed, strongest first.
VERIFICATION_CANON = {
    "true": "fetched", "fetched": "fetched", "full_page": "fetched",
    "full": "fetched", "verified": "fetched", "fetched_full": "fetched",
    "abstract-only": "abstract", "abstract_only": "abstract",
    "snippet": "snippet", "search-snippet": "snippet",
    "false": "not_fetched", "not_fetched": "not_fetched",
    "asserted": "not_fetched", "unverified": "not_fetched",
}

def canon_verification(value):
    """Fold the recorded verification wording onto four levels.

    A handful of entries append a reason ("search-snippet (direct fetch
    blocked: expired tls cert)"), so fall back to a prefix match.
    """
    if value is None:
        return None
    text = str(value).strip().lower()
    if text in VERIFICATION_CANON:
        return VERIFICATION_CANON[text]
    for key, canon in VERIFICATION_CANON.items():
        if text.startswith(key):
            return canon
    return text or None


PLACEHOLDER_RE = re.compile(
    r"^(n/?a|none|null|n\.d\.|-{1,2}|unknown|tbd|same|same as original"
    r"|n/?a \(english original\)|see original|english original)$",
    re.IGNORECASE,
)


def first(rec: dict, keys, allow_blank=False):
    for k in keys:
        if k in rec:
            v = rec[k]
            if v is None:
                continue
            if isinstance(v, str):
                v = v.strip()
                if v or allow_blank:
                    if PLACEHOLDER_RE.match(v):
                        continue
                    return v
            elif isinstance(v, (list, tuple)):
                flat = [str(x).strip() for x in v if x not in (None, "")]
                if flat:
                    return "; ".join(flat)
            else:
                return v
    return None


def as_list(value):
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        out = []
        for v in value:
            out.extend(as_list(v))
        return out
    text = str(value).strip()
    if not text or text.lower() in {"n/a", "none", "null", "-"}:
        return []
    parts = re.split(r"[;,]\s*|\s*\|\s*", text)
    return [p.strip() for p in parts if p.strip()]


def collect_used_in(rec: dict):
    out = []
    for k in USED_IN_KEYS:
        if k in rec:
            out.extend(as_list(rec[k]))
    return out


def norm_tier(value):
    if value is None:
        return None
    text = str(value).strip().upper()
    m = re.search(r"([123])", text)
    return f"T{m.group(1)}" if m else None


def norm_type(rec: dict):
    raw = first(rec, TYPE_KEYS)
    if raw:
        text = str(raw).strip().lower()
        key = text.replace("-", "_").replace(" ", "_")
        if key in TYPE_CANON:
            return TYPE_CANON[key]
        for needle, canon in TYPE_KEYWORDS:
            if needle in text:
                return canon
    # Infer from the record's own shape.
    if rec.get("number") and rec.get("jurisdiction"):
        return "patent"
    if rec.get("doi"):
        return "academic"
    if rec.get("arxiv") or rec.get("arxiv_id"):
        return "preprint"
    url = (first(rec, URL_KEYS) or "").lower()
    if "patents.google" in url or "patentscope" in url:
        return "patent"
    if "arxiv.org" in url:
        return "preprint"
    if any(d in url for d in (".gov", ".gov.cn", "europa.eu", "ndrc.gov", "iea.org")):
        return "government"
    if any(d in url for d in ("doi.org", "ieeexplore", "springer", "sciencedirect",
                              "mdpi.com", "iopscience", "nature.com", "pubmed",
                              "wiley.com", "acs.org", "aps.org")):
        return "academic"
    return "other"


def norm_year(rec: dict):
    for k in ("year", "approx_year", "year_approx"):
        v = rec.get(k)
        if v not in (None, "", "n.d."):
            m = re.search(r"(1[89]\d{2}|20\d{2})", str(v))
            if m:
                return int(m.group(1))
    date = first(rec, DATE_KEYS)
    if date:
        m = re.search(r"(1[89]\d{2}|20\d{2})", str(date))
        if m:
            return int(m.group(1))
    return None


def clean_doi(text, from_url=False):
    """Trim the trailing rubbish that DOI-bearing URLs drag in.

    A DOI lifted out of a publisher URL often keeps the rest of the path, e.g.
    `10.1063/1.3006441/15032353/094902_1_online.pdf`. DOI suffixes with an
    embedded slash are rare, so for URL-derived values keep only the first
    suffix segment. Explicitly recorded `doi` fields are trusted as-is apart
    from trailing punctuation.
    """
    if not text:
        return None
    doi = str(text).strip().rstrip("./,;)").lower()
    if from_url:
        prefix, _, suffix = doi.partition("/")
        if suffix:
            doi = prefix + "/" + suffix.split("/")[0]
    return doi or None


def extract_doi(rec: dict):
    v = rec.get("doi")
    if v:
        m = DOI_RE.search(str(v))
        if m:
            return clean_doi(m.group(0))
    ck = str(rec.get("canonical_key") or "")
    if ck.lower().startswith("doi:"):
        m = DOI_RE.search(ck)
        if m:
            return clean_doi(m.group(0))
    url = first(rec, URL_KEYS) or ""
    if "doi.org/" in url or "/doi/" in url:
        m = DOI_RE.search(url)
        if m:
            return clean_doi(m.group(0), from_url=True)
    return None


def extract_arxiv(rec: dict):
    for k in ("arxiv", "arxiv_id"):
        v = rec.get(k)
        if v:
            m = ARXIV_RE.search(str(v))
            if m:
                return m.group(1)
    url = first(rec, URL_KEYS) or ""
    if "arxiv.org" in url:
        m = ARXIV_RE.search(url)
        if m:
            return m.group(1)
    return None


def extract_patent_numbers(rec: dict):
    """All publication numbers a record mentions, most canonical first.

    The prior-art ledgers are inconsistent here: some rows carry a single
    number, some a slash-joined family, some a number plus a parenthetical
    ("US11101059B2 (also published as US20180294077A1)"). Pull every number
    out; the first becomes the identity and the rest join the family list.
    """
    found = []
    for k in ("number", "application_number", "numbers", "family", "ids_pool"):
        v = rec.get(k)
        if not v:
            continue
        text = re.sub(r"\([^)]*\)", " ", " ".join(as_list(v)) if isinstance(v, (list, tuple)) else str(v))
        for num in PATENT_NUM_RE.findall(re.sub(r"[\s,]", "", text).upper()):
            if num not in found:
                found.append(num)
        if found and k in ("number", "application_number"):
            break
    if not found:
        url = first(rec, URL_KEYS) or ""
        m = re.search(r"patents\.google\.com/patent/([A-Z]{2}[A-Z0-9]+)", url, re.IGNORECASE)
        if m:
            found = [m.group(1).upper()]
    return found


TRACKING_PARAMS = re.compile(r"^(utm_|fbclid|gclid|ref|src|source)$", re.IGNORECASE)


def norm_url(url):
    if not url:
        return None
    url = str(url).strip()
    if not url.lower().startswith(("http://", "https://")):
        return None
    url = re.sub(r"^https?://", "", url, flags=re.IGNORECASE)
    url = re.sub(r"^www\.", "", url, flags=re.IGNORECASE)
    if "?" in url:
        base, _, query = url.partition("?")
        kept = [p for p in query.split("&") if p and not TRACKING_PARAMS.match(p.split("=")[0])]
        url = base + ("?" + "&".join(sorted(kept)) if kept else "")
    url = url.split("#", 1)[0].rstrip("/")
    return url.lower() or None


CJK_RE = re.compile(r"[぀-ヿ㐀-䶿一-鿿가-힯]")


def title_slug(title):
    if not title:
        return None
    text = unicodedata.normalize("NFKC", str(title)).lower()
    text = re.sub(r"[^\w\s]+", " ", text).strip()
    return re.sub(r"\s+", " ", text) or None


def slug_is_distinctive(slug):
    """Long enough that an exact match means the same document.

    CJK and Hangul pack far more meaning per character than Latin script, so a
    short run of them is already as distinctive as a long English title.
    """
    if not slug:
        return False
    return len(slug) >= 30 or len(CJK_RE.findall(slug)) >= 6


# ---------------------------------------------------------------------------
# Reading
# ---------------------------------------------------------------------------

def project_of(path: Path):
    rel = path.relative_to(STARTUP_ROOT)
    return rel.parts[0]


def stage_of(path: Path):
    rel = path.relative_to(STARTUP_ROOT)
    return rel.parts[1] if len(rel.parts) > 2 else "(root)"


def iter_source_files():
    for dirpath, dirnames, filenames in os.walk(STARTUP_ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIR_PARTS and not d.startswith(".")]
        rel_dir = str(Path(dirpath).relative_to(STARTUP_ROOT)).replace(os.sep, "/") + "/"
        if any(frag in rel_dir or rel_dir.startswith(frag) for frag in EXCLUDED_PATH_FRAGMENTS):
            continue
        for name in sorted(filenames):
            if SOURCE_FILE_RE.search(name):
                yield Path(dirpath) / name


def read_records(path: Path):
    """Yield raw dicts out of one source file, whatever container it uses."""
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as fh:
            yield from csv.DictReader(fh)
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ValueError(f"unparseable JSON: {exc}") from exc
    if isinstance(data, list):
        yield from (r for r in data if isinstance(r, dict))
    elif isinstance(data, dict):
        for key in ("sources", "value", "entries", "records", "items", "patents"):
            if isinstance(data.get(key), list):
                yield from (r for r in data[key] if isinstance(r, dict))
                return
        # A dict keyed by source id.
        if data and all(isinstance(v, dict) for v in data.values()):
            for k, v in data.items():
                yield {"id": k, **v}


def parse_markdown_ledger(path: Path):
    """04's hand-kept `- [S-001] what -- where -- accessed -- used for` ledger."""
    text = path.read_text(encoding="utf-8")
    entries, current = [], None
    for line in text.splitlines():
        m = re.match(r"\s*-\s*\[(S-?\d+)\]\s*(.*)", line)
        if m:
            if current:
                entries.append(current)
            current = {"id": m.group(1), "_raw": m.group(2)}
        elif current is not None and line.startswith("  ") and line.strip():
            current["_raw"] += " " + line.strip()
        elif current is not None and not line.strip():
            entries.append(current)
            current = None
    if current:
        entries.append(current)
    out = []
    for e in entries:
        parts = [p.strip() for p in e["_raw"].split("--")]
        out.append({
            "id": e["id"],
            "title": parts[0] if parts else e["_raw"],
            "publisher": parts[1] if len(parts) > 1 else None,
            "accessed": parts[2] if len(parts) > 2 else None,
            "claim_supported": parts[3] if len(parts) > 3 else None,
            "source_type": "other",
        })
    return out


# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------

def normalise(rec: dict, path: Path):
    title = first(rec, TITLE_KEYS)
    url = first(rec, URL_KEYS)
    # A "url" field that is really a bare citation string (the CSV ledger does this).
    if url and not str(url).lower().startswith(("http://", "https://")):
        if not title:
            title = url
        url = None

    doi = extract_doi(rec)
    arxiv = extract_arxiv(rec)
    patent_numbers = extract_patent_numbers(rec)
    patent = patent_numbers[0] if patent_numbers else None
    stype = norm_type(rec)

    verify_raw = first(rec, VERIFY_KEYS)
    if isinstance(rec.get("fetched"), bool):
        verify_raw = "fetched" if rec["fetched"] else (verify_raw or "not_fetched")
    verify_raw = canon_verification(verify_raw)

    accepted = rec.get("accepted")
    if accepted is None:
        accepted = rec.get("count_toward_300")
    if isinstance(accepted, str):
        accepted = accepted.strip().lower() in {"true", "yes", "y", "1"}

    peer = rec.get("peer_review_status")
    if peer is None and rec.get("peer_reviewed") is not None:
        peer = "verified" if rec["peer_reviewed"] in (True, "true", "yes") else "no"

    return {
        "record_id": str(rec.get("id") or rec.get("source_id") or "") or None,
        "title": title,
        "title_original": first(rec, ORIGINAL_TITLE_KEYS) if first(rec, ORIGINAL_TITLE_KEYS) != title else None,
        "authors_or_org": first(rec, AUTHOR_KEYS),
        "publisher": first(rec, PUBLISHER_KEYS),
        "url": str(url) if url else None,
        "doi": doi,
        "arxiv_id": arxiv,
        "patent_number": patent,
        "jurisdiction": (str(rec["jurisdiction"]).strip().upper() if rec.get("jurisdiction") else None),
        "assignee": first(rec, ("assignee",)),
        "source_type": stype,
        "tier": norm_tier(first(rec, TIER_KEYS)),
        "language": (str(first(rec, LANG_KEYS)).strip().lower() if first(rec, LANG_KEYS) else None),
        "geography": as_list(rec.get("geography")),
        "year": norm_year(rec),
        "date": first(rec, DATE_KEYS),
        "accessed": first(rec, ACCESSED_KEYS),
        "verification": (str(verify_raw).strip().lower() if verify_raw is not None else None),
        "access_level": (str(first(rec, ACCESS_KEYS)).strip().lower() if first(rec, ACCESS_KEYS) else None),
        "source_type_raw": (str(first(rec, TYPE_KEYS)).strip() if first(rec, TYPE_KEYS) else None),
        "peer_review_status": (str(peer).strip().lower() if peer else None),
        "accepted": accepted if isinstance(accepted, bool) else None,
        "claim_supported": first(rec, CLAIM_KEYS),
        "notes": first(rec, NOTE_KEYS),
        "used_in": collect_used_in(rec),
        "cpc": as_list(rec.get("cpc")),
        "patent_family": sorted(set(patent_numbers[1:]) | set(as_list(rec.get("family")))),
    }


# ---------------------------------------------------------------------------
# Union-find dedup
# ---------------------------------------------------------------------------

class Union:
    """Union-find that refuses merges which would conflate distinct documents.

    Each component tracks the strong identifiers (DOI, patent number, arXiv id)
    of its members. Two components may only merge if they agree on every strong
    identifier they both carry. Without this guard a shared title would collapse
    the members of a patent family — they are published under one title but are
    separate documents with separate claims.
    """

    STRONG = ("doi", "patent_number", "arxiv_id")

    def __init__(self):
        self.parent = {}
        self.ids = {}
        self.conflicts = []

    def add(self, x, record):
        self.parent.setdefault(x, x)
        self.ids.setdefault(x, {k: set() for k in self.STRONG})
        for k in self.STRONG:
            value = record.get(k)
            if value:
                self.ids[x][k].add(patent_stem(value) if k == "patent_number" else value)

    def find(self, x):
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def compatible(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return True
        ia, ib = self.ids.get(ra, {}), self.ids.get(rb, {})
        for k in self.STRONG:
            left, right = ia.get(k) or set(), ib.get(k) or set()
            if left and right and left != right:
                return False
        return True

    def union(self, a, b, evidence=""):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return True
        if not self.compatible(ra, rb):
            conflict = {
                "evidence": evidence,
                "left": {k: sorted(self.ids[ra][k]) for k in self.STRONG if self.ids[ra][k]},
                "right": {k: sorted(self.ids[rb][k]) for k in self.STRONG if self.ids[rb][k]},
            }
            if conflict not in self.conflicts:
                self.conflicts.append(conflict)
            return False
        keep, drop = min(ra, rb), max(ra, rb)
        self.parent[drop] = keep
        for k in self.STRONG:
            self.ids[keep][k] |= self.ids[drop][k]
        return True


def longest(values):
    values = [v for v in values if v]
    return max(values, key=len) if values else None


def most_common(values):
    values = [v for v in values if v]
    return Counter(values).most_common(1)[0][0] if values else None


def merge_group(items):
    """items: list of (normalised_record, occurrence_dict)."""
    recs = [r for r, _ in items]
    occs = [o for _, o in items]

    def vals(field):
        return [r[field] for r in recs if r.get(field)]

    # Prefer a Latin-script title when one exists; they are the merged-in English glosses.
    titles = vals("title")
    latin = [t for t in titles if sum(ch.isascii() for ch in t) > len(t) * 0.6]
    title = longest(latin) or longest(titles)

    tiers = vals("tier")
    tier = min(tiers) if tiers else None          # T1 beats T3 when projects disagree
    verifications = vals("verification")
    strength = {"fetched": 0, "abstract": 1, "snippet": 2, "not_fetched": 3}
    verification = min(verifications, key=lambda v: strength.get(v, 3)) if verifications else None

    doi = most_common(vals("doi"))
    patent_number = longest(vals("patent_number"))
    urls = sorted({r["url"] for r in recs if r.get("url")})
    used_in = sorted({u for r in recs for u in r.get("used_in", [])})
    geography = sorted({g for r in recs for g in r.get("geography", [])})
    accessed = sorted({r["accessed"] for r in recs if r.get("accessed")})
    projects = sorted({o["project"] for o in occs})
    accepted_flags = [r["accepted"] for r in recs if r["accepted"] is not None]

    slug = title_slug(title)
    canonical_key = (f"doi:{doi}" if doi else
                     f"patent:{patent_stem(patent_number)}" if patent_number else
                     f"arxiv:{most_common(vals('arxiv_id'))}" if vals("arxiv_id") else
                     f"url:{norm_url(urls[0])}" if urls else
                     f"title:{slug}" if slug else
                     # Nothing identifying survived; anchor on where it was found so
                     # the record is still addressable and never collides.
                     "record:" + occs[0]["file"] + "#" + (recs[0]["record_id"] or "0"))
    uid = "S" + hashlib.sha1(canonical_key.encode("utf-8")).hexdigest()[:12]

    project_ids = defaultdict(set)
    for r, o in items:
        if r["record_id"]:
            project_ids[o["project"]].add(r["record_id"])

    return {
        "uid": uid,
        "canonical_key": canonical_key,
        "title": title,
        # Records merged on a shared URL sometimes titled that page differently
        # — a paraphrase, a translation, or (for a rolling index page such as
        # ITER's open-tender list) a different item on the same page. Keep them
        # all so a merge never silently swallows a distinct title.
        "titles_seen": sorted({t for t in titles}),
        "title_original": longest(vals("title_original")),
        "authors_or_org": longest(vals("authors_or_org")),
        "publisher": most_common(vals("publisher")) or longest(vals("publisher")),
        "url": urls[0] if urls else None,
        "all_urls": urls,
        "doi": doi,
        "arxiv_id": most_common(vals("arxiv_id")),
        "patent_number": patent_number,
        "jurisdiction": most_common(vals("jurisdiction")),
        "assignee": most_common(vals("assignee")),
        "cpc": sorted({c for r in recs for c in r.get("cpc", [])}),
        "patent_family": sorted({c for r in recs for c in r.get("patent_family", [])}),
        "source_type": most_common([v for v in vals("source_type") if v != "other"]) or "other",
        "source_types_raw": sorted({r["source_type_raw"] for r in recs if r.get("source_type_raw")}),
        "access_level": most_common(vals("access_level")),
        "tier": tier,
        "tiers_seen": sorted(set(tiers)),
        "language": most_common(vals("language")),
        "geography": geography,
        "year": most_common(vals("year")),
        "date": most_common(vals("date")),
        "first_accessed": accessed[0] if accessed else None,
        "last_accessed": accessed[-1] if accessed else None,
        "verification": verification,
        "peer_review_status": most_common(vals("peer_review_status")),
        "accepted": (all(accepted_flags) if accepted_flags else None),
        "claim_supported": longest(vals("claim_supported")),
        "notes": longest(vals("notes")),
        "used_in": used_in,
        "projects": projects,
        "project_ids": {k: sorted(v) for k, v in sorted(project_ids.items())},
        # n_occurrences counts raw records; occurrences lists distinct places,
        # since a pre-dedupe merge snapshot can hold the same row twice.
        "n_occurrences": len(occs),
        "occurrences": sorted(
            ({"project": p, "stage": st, "file": f, "record_id": rid}
             for p, st, f, rid in {(o["project"], o["stage"], o["file"], r["record_id"])
                                   for r, o in items}),
            key=lambda o: (o["file"], o["record_id"] or ""),
        ),
    }


# ---------------------------------------------------------------------------
# Emitters
# ---------------------------------------------------------------------------

CSV_COLUMNS = [
    "uid", "canonical_key", "title", "authors_or_org", "publisher", "year", "date",
    "source_type", "tier", "language", "geography", "url", "doi", "arxiv_id",
    "patent_number", "jurisdiction", "assignee", "verification", "access_level", "peer_review_status",
    "accepted", "first_accessed", "last_accessed", "projects", "used_in",
    "n_occurrences", "claim_supported", "notes",
]


def flatten(value):
    if isinstance(value, list):
        return " | ".join(str(v) for v in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    if value is None:
        return ""
    return str(value)


def write_csv(records, path: Path):
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(CSV_COLUMNS)
        for r in records:
            writer.writerow([flatten(r.get(c)) for c in CSV_COLUMNS])


def write_sqlite(records, path: Path):
    if path.exists():
        path.unlink()
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.executescript(
        """
        CREATE TABLE sources (
            uid TEXT PRIMARY KEY, canonical_key TEXT, title TEXT, title_original TEXT,
            titles_seen TEXT, authors_or_org TEXT, publisher TEXT, url TEXT,
            all_urls TEXT, doi TEXT,
            arxiv_id TEXT, patent_number TEXT, jurisdiction TEXT, assignee TEXT,
            cpc TEXT, patent_family TEXT, source_type TEXT, tier TEXT, language TEXT,
            geography TEXT, year INTEGER, date TEXT, first_accessed TEXT,
            last_accessed TEXT, verification TEXT, access_level TEXT,
            peer_review_status TEXT, accepted INTEGER, claim_supported TEXT,
            notes TEXT, projects TEXT, n_occurrences INTEGER
        );
        CREATE TABLE occurrences (
            uid TEXT, project TEXT, stage TEXT, file TEXT, record_id TEXT,
            FOREIGN KEY (uid) REFERENCES sources(uid)
        );
        CREATE TABLE usage (
            uid TEXT, used_in TEXT,
            FOREIGN KEY (uid) REFERENCES sources(uid)
        );
        CREATE INDEX idx_occ_uid ON occurrences(uid);
        CREATE INDEX idx_occ_project ON occurrences(project);
        CREATE INDEX idx_usage_uid ON usage(uid);
        CREATE INDEX idx_usage_used_in ON usage(used_in);
        CREATE INDEX idx_sources_type ON sources(source_type);
        CREATE INDEX idx_sources_tier ON sources(tier);
        CREATE INDEX idx_sources_year ON sources(year);
        CREATE INDEX idx_sources_jur ON sources(jurisdiction);
        CREATE VIRTUAL TABLE sources_fts USING fts5(
            uid UNINDEXED, title, authors_or_org, publisher, claim_supported, notes,
            tokenize='unicode61'
        );
        """
    )
    for r in records:
        cur.execute(
            "INSERT INTO sources VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (r["uid"], r["canonical_key"], r["title"], r["title_original"],
             flatten(r["titles_seen"]), r["authors_or_org"], r["publisher"],
             r["url"], flatten(r["all_urls"]),
             r["doi"], r["arxiv_id"], r["patent_number"], r["jurisdiction"],
             r["assignee"], flatten(r["cpc"]), flatten(r["patent_family"]),
             r["source_type"], r["tier"], r["language"], flatten(r["geography"]),
             r["year"], r["date"], r["first_accessed"], r["last_accessed"],
             r["verification"], r["access_level"], r["peer_review_status"],
             None if r["accepted"] is None else int(r["accepted"]),
             r["claim_supported"], r["notes"], flatten(r["projects"]),
             r["n_occurrences"]),
        )
        cur.executemany(
            "INSERT INTO occurrences VALUES (?,?,?,?,?)",
            [(r["uid"], o["project"], o["stage"], o["file"], o["record_id"])
             for o in r["occurrences"]],
        )
        cur.executemany("INSERT INTO usage VALUES (?,?)",
                        [(r["uid"], u) for u in r["used_in"]])
        cur.execute(
            "INSERT INTO sources_fts VALUES (?,?,?,?,?,?)",
            (r["uid"], r["title"] or "", r["authors_or_org"] or "", r["publisher"] or "",
             r["claim_supported"] or "", r["notes"] or ""),
        )
    con.commit()
    con.execute("VACUUM")
    con.close()


def write_statistics(records, log, path: Path):
    def tally(key, transform=lambda r, k: [r.get(k)] if r.get(k) else ["(unset)"]):
        c = Counter()
        for r in records:
            c.update(transform(r, key))
        return c

    def table(counter, header, total=None):
        total = total or sum(counter.values())
        lines = [f"| {header} | Sources | Share |", "|---|---:|---:|"]
        for k, n in counter.most_common():
            lines.append(f"| {k} | {n} | {100*n/total:.1f}% |")
        return "\n".join(lines)

    n = len(records)
    by_project = Counter()
    for r in records:
        by_project.update(r["projects"])
    shared = Counter(len(r["projects"]) for r in records)
    years = Counter(r["year"] for r in records if r["year"])
    ids = Counter()
    for r in records:
        if r["doi"]:
            ids["has DOI"] += 1
        if r["patent_number"]:
            ids["is patent"] += 1
        if r["arxiv_id"]:
            ids["has arXiv id"] += 1
        if r["url"]:
            ids["has URL"] += 1

    recent = sorted(((y, c) for y, c in years.items() if y >= 2015), reverse=True)
    out = f"""# Source database — coverage statistics

Generated by `tools/build_source_database.py`. Do not hand-edit.

- **{n:,} unique sources** merged from **{log['raw_records']:,} raw records**
  across **{log['files_read']} files** in **{len(by_project)} projects**.
- Deduplication collapsed {log['raw_records'] - n:,} duplicate records
  ({100*(log['raw_records']-n)/max(log['raw_records'],1):.1f}% of the raw corpus).

## Sources per project

A source counted in two projects was gathered once and reused.

{table(by_project, "Project", n)}

## Cross-project reuse

{table(Counter({f"{k} project{'s' if k>1 else ''}": v for k, v in shared.items()}), "Appears in", n)}

## By type

{table(tally("source_type"), "Type", n)}

## By tier

T1 is primary/official, T2 peer-reviewed or established secondary, T3 other
secondary. Where projects disagreed the strongest tier is kept; `tiers_seen`
in `sources.json` preserves every grading.

{table(tally("tier"), "Tier", n)}

## By verification strength

{table(tally("verification"), "Verification", n)}

## By language

{table(tally("language"), "Language", n)}

## Identifier coverage

{table(ids, "Identifier", n)}

## Publication year (2015 and later)

| Year | Sources |
|---:|---:|
""" + "\n".join(f"| {y} | {c} |" for y, c in recent) + f"""

Undated or pre-2015: {n - sum(c for _, c in recent):,}.

## Top publishers

{table(Counter(r['publisher'] for r in records if r['publisher']).most_common(25) and Counter(dict(Counter(r['publisher'] for r in records if r['publisher']).most_common(25))), "Publisher", n)}
"""
    path.write_text(out, encoding="utf-8")


# ---------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="report only, write nothing")
    args = parser.parse_args(argv)

    log = {"generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "files_read": 0, "raw_records": 0, "files": [], "skipped": [], "errors": []}

    items = []          # (normalised record, occurrence)
    for path in iter_source_files():
        rel = str(path.relative_to(STARTUP_ROOT)).replace(os.sep, "/")
        try:
            raw = list(read_records(path))
        except ValueError as exc:
            log["errors"].append({"file": rel, "error": str(exc)})
            continue
        if not raw:
            log["skipped"].append({"file": rel, "reason": "no records"})
            continue
        occ = {"project": project_of(path), "stage": stage_of(path), "file": rel}
        for rec in raw:
            items.append((normalise(rec, path), occ))
        log["files_read"] += 1
        log["raw_records"] += len(raw)
        log["files"].append({"file": rel, "records": len(raw)})

    # The one markdown ledger that never became JSON.
    md = STARTUP_ROOT / "04_Cocktail_Dilution_Sensor_2026-07/90_REFERENCES/SOURCES.md"
    if md.exists():
        rel = str(md.relative_to(STARTUP_ROOT)).replace(os.sep, "/")
        occ = {"project": project_of(md), "stage": stage_of(md), "file": rel}
        recs = parse_markdown_ledger(md)
        for rec in recs:
            items.append((normalise(rec, md), occ))
        log["files_read"] += 1
        log["raw_records"] += len(recs)
        log["files"].append({"file": rel, "records": len(recs)})

    # Drop records with no identifying content at all.
    keep = []
    for rec, occ in items:
        if rec["title"] or rec["url"] or rec["doi"] or rec["patent_number"]:
            keep.append((rec, occ))
        else:
            log["skipped"].append({"file": occ["file"], "reason": "no title, url, doi or patent number",
                                   "record_id": rec["record_id"]})
    items = keep

    # Link records that describe the same document. Strong identifiers first,
    # then URL, then title — so a weak signal can never override a strong one.
    uf = Union()
    for i, (rec, _) in enumerate(items):
        uf.add(i, rec)

    for field in ("doi", "patent_number", "arxiv_id"):
        index = {}
        for i, (rec, _) in enumerate(items):
            key = rec[field]
            if field == "patent_number":
                key = patent_stem(key)
            if key:
                if key in index:
                    uf.union(index[key], i, f"{field}={key}")
                else:
                    index[key] = i

    by_url = {}
    for i, (rec, _) in enumerate(items):
        key = norm_url(rec["url"])
        if key:
            if key in by_url:
                uf.union(by_url[key], i, f"url={key}")
            else:
                by_url[key] = i

    by_title = {}
    for i, (rec, _) in enumerate(items):
        slug = title_slug(rec["title"])
        if slug_is_distinctive(slug):
            if slug in by_title:
                uf.union(by_title[slug], i, f"title={slug[:80]}")
            else:
                by_title[slug] = i

    groups = defaultdict(list)
    for i, item in enumerate(items):
        groups[uf.find(i)].append(item)
    groups = list(groups.values())

    # canonical_key is the identity of a source, so two groups that produce the
    # same key are the same source and must become one record. Merging can
    # promote a key (title -> url -> doi), so repeat until it settles.
    for _ in range(5):
        by_key = defaultdict(list)
        for g in groups:
            by_key[merge_group(g)["canonical_key"]].append(g)
        if all(len(v) == 1 for v in by_key.values()):
            break
        groups = [[item for g in v for item in g] for v in by_key.values()]
    else:
        raise SystemExit("canonical_key did not converge after 5 consolidation passes")

    records = [merge_group(g) for g in groups]
    records.sort(key=lambda r: (-r["n_occurrences"], r["title"] or "", r["uid"]))

    # A uid collision would silently drop a source; fail loudly instead.
    dupes = [u for u, c in Counter(r["uid"] for r in records).items() if c > 1]
    if dupes:
        raise SystemExit(f"uid collision on {dupes[:5]} — canonical_key is not unique")

    log["unique_sources"] = len(records)
    log["blocked_merges"] = uf.conflicts
    print(f"{log['files_read']} files -> {log['raw_records']:,} raw records "
          f"-> {len(records):,} unique sources")
    if uf.conflicts:
        print(f"  {len(uf.conflicts)} merges blocked by conflicting identifiers "
              f"(logged in build_log.json)")
    if log["errors"]:
        print(f"  {len(log['errors'])} unreadable files")
    if args.dry_run:
        return 0

    DB_DIR.mkdir(parents=True, exist_ok=True)
    (DB_DIR / "sources.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    write_csv(records, DB_DIR / "sources.csv")
    write_sqlite(records, DB_DIR / "sources.sqlite")
    write_statistics(records, log, DB_DIR / "STATISTICS.md")
    (DB_DIR / "build_log.json").write_text(
        json.dumps(log, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    for name in ("sources.json", "sources.csv", "sources.sqlite", "STATISTICS.md", "build_log.json"):
        print(f"  wrote {name}  ({(DB_DIR/name).stat().st_size/1e6:.2f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
