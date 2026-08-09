#!/usr/bin/env python3
"""Search the unified startup source database.

Examples
--------
    # full-text search across title, authors, publisher and claim
    python3 tools/query.py "no-insulation winding"

    # narrow it
    python3 tools/query.py "quench" --type patent --jurisdiction US --since 2020
    python3 tools/query.py --tier T1 --lang zh --project 06_Frontier_Idea_Research_2026-07

    # everything that evidenced one idea, lane or candidate
    python3 tools/query.py --used-in C12
    python3 tools/query.py --used-in L04 --type academic

    # look one source up and see every place it was used
    python3 tools/query.py --uid S3f2a91c0b7de --show

    # what did two projects both rely on?
    python3 tools/query.py --shared-by 01_Startup_Opportunity_Research_2026-07 \\
                           --shared-by 06_Frontier_Idea_Research_2026-07

    # feed a new research run
    python3 tools/query.py --type academic --tier T1 --format bib > seed.bib
    python3 tools/query.py "hall sensor" --format json | jq '.[].url'
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import textwrap
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "sources.sqlite"


def connect():
    if not DB_PATH.exists():
        raise SystemExit(f"{DB_PATH} not found — run tools/build_source_database.py first")
    con = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


# FTS5 reads bare punctuation as syntax, so "no-insulation winding" parses as a
# column reference and errors out. Quote the terms unless the caller is clearly
# writing an FTS expression on purpose.
FTS_SYNTAX = re.compile(r'\b(AND|OR|NOT|NEAR)\b|["*^():]')

# FTS5's unicode61 tokenizer does not segment Chinese, Japanese or Korean, so a
# CJK query matches nothing. Those searches go through LIKE instead.
CJK = re.compile(r"[぀-ヿ㐀-䶿一-鿿가-힯]")


def prepare_fts(text, raw=False):
    if raw or FTS_SYNTAX.search(text):
        return text
    terms = [t for t in re.split(r"\s+", text.strip()) if t]
    return " AND ".join('"' + t.replace('"', "") + '"' for t in terms)


def build_query(args):
    where, params = [], []
    joins = ""

    if args.text and CJK.search(args.text) and not args.raw:
        needle = f"%{args.text.strip()}%"
        where.append("(s.title LIKE ? OR s.title_original LIKE ? OR s.authors_or_org LIKE ?"
                     " OR s.publisher LIKE ? OR s.claim_supported LIKE ?)")
        params.extend([needle] * 5)
    elif args.text:
        joins += " JOIN sources_fts f ON f.uid = s.uid"
        where.append("sources_fts MATCH ?")
        params.append(prepare_fts(args.text, args.raw))
    if args.type:
        where.append("s.source_type = ?")
        params.append(args.type)
    if args.tier:
        where.append("s.tier = ?")
        params.append(args.tier)
    if args.lang:
        where.append("s.language LIKE ?")
        params.append(args.lang + "%")
    if args.jurisdiction:
        where.append("s.jurisdiction = ?")
        params.append(args.jurisdiction.upper())
    if args.since:
        where.append("s.year >= ?")
        params.append(args.since)
    if args.until:
        where.append("s.year <= ?")
        params.append(args.until)
    if args.publisher:
        where.append("s.publisher LIKE ?")
        params.append(f"%{args.publisher}%")
    if args.doi:
        where.append("s.doi IS NOT NULL AND s.doi != ''")
    if args.verified:
        where.append("s.verification = 'fetched'")
    if args.uid:
        where.append("s.uid = ?")
        params.append(args.uid)
    if args.project:
        where.append("EXISTS (SELECT 1 FROM occurrences o WHERE o.uid = s.uid AND o.project = ?)")
        params.append(args.project)
    if args.used_in:
        where.append("EXISTS (SELECT 1 FROM usage u WHERE u.uid = s.uid AND u.used_in = ?)")
        params.append(args.used_in)
    for project in args.shared_by or []:
        where.append("EXISTS (SELECT 1 FROM occurrences o WHERE o.uid = s.uid AND o.project = ?)")
        params.append(project)

    sql = f"SELECT s.* FROM sources s{joins}"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY s.n_occurrences DESC, s.year DESC, s.title"
    # --count reports the whole match set; --limit only trims what gets printed.
    if not args.count:
        sql += " LIMIT ?"
        params.append(args.limit)
    return sql, params


def occurrences(con, uid):
    return con.execute(
        "SELECT project, stage, file, record_id FROM occurrences WHERE uid = ? ORDER BY file",
        (uid,),
    ).fetchall()


def used_in(con, uid):
    return [r[0] for r in con.execute(
        "SELECT used_in FROM usage WHERE uid = ? ORDER BY used_in", (uid,))]


def bibtex_key(row, seen):
    author = (row["authors_or_org"] or row["publisher"] or "anon").split(";")[0]
    stem = re.sub(r"[^A-Za-z]", "", author)[:12].lower() or "anon"
    key = f"{stem}{row['year'] or 'nd'}"
    n, base = 1, key
    while key in seen:
        n += 1
        key = f"{base}{chr(ord('a') + n - 2)}"
    seen.add(key)
    return key


def escape_bib(text):
    return (text or "").replace("{", "").replace("}", "").replace("\\", "")


def emit_bibtex(rows):
    seen = set()
    for row in rows:
        entry = "misc"
        if row["source_type"] == "academic":
            entry = "article"
        elif row["source_type"] == "patent":
            entry = "patent"
        elif row["source_type"] == "preprint":
            entry = "unpublished"
        fields = [("title", escape_bib(row["title"])),
                  ("author", escape_bib(row["authors_or_org"])),
                  ("howpublished" if entry == "misc" else "journal", escape_bib(row["publisher"])),
                  ("year", row["year"]),
                  ("doi", row["doi"]),
                  ("number", row["patent_number"]),
                  ("url", row["url"]),
                  ("note", escape_bib(row["first_accessed"] and f"accessed {row['first_accessed']}")),
                  ]
        print(f"@{entry}{{{bibtex_key(row, seen)},")
        for name, value in fields:
            if value:
                print(f"  {name} = {{{value}}},")
        print("}\n")


def emit_table(con, rows, show):
    for row in rows:
        bits = [b for b in (row["tier"], row["source_type"], str(row["year"] or ""),
                            row["language"]) if b]
        print(f"\n{row['uid']}  [{' · '.join(bits)}]  seen {row['n_occurrences']}× "
              f"in {row['projects'].replace(' | ', ', ')}")
        for line in textwrap.wrap(row["title"] or "(untitled)", 96):
            print(f"  {line}")
        meta = " · ".join(b for b in (row["authors_or_org"], row["publisher"]) if b)
        if meta:
            for line in textwrap.wrap(meta, 96):
                print(f"  {line}")
        ident = " · ".join(b for b in (
            f"doi:{row['doi']}" if row["doi"] else None,
            row["patent_number"],
            f"arXiv:{row['arxiv_id']}" if row["arxiv_id"] else None,
            row["verification"]) if b)
        if ident:
            print(f"  {ident}")
        if row["url"]:
            print(f"  {row['url']}")
        if show:
            others = [x for x in (row["titles_seen"] or "").split(" | ")
                      if x and x != row["title"]]
            if others:
                print("  also recorded as:")
                for other in others:
                    for line in textwrap.wrap(other, 92):
                        print(f"    {line}")
            if row["claim_supported"]:
                print("  claim:")
                for line in textwrap.wrap(row["claim_supported"], 92):
                    print(f"    {line}")
            uses = used_in(con, row["uid"])
            if uses:
                print(f"  used in: {', '.join(uses)}")
            print("  recorded in:")
            for occ in occurrences(con, row["uid"]):
                print(f"    {occ['file']}  [{occ['record_id'] or '-'}]")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("text", nargs="?", help="FTS5 query over title/authors/publisher/claim")
    parser.add_argument("--type", help="academic, patent, government, company, news, industry, "
                                       "standards, preprint, dataset, think_tank, other")
    parser.add_argument("--tier", choices=["T1", "T2", "T3"])
    parser.add_argument("--lang", help="language prefix, e.g. en or zh")
    parser.add_argument("--jurisdiction", help="patent jurisdiction, e.g. US, CN, EP, WO")
    parser.add_argument("--since", type=int, metavar="YEAR")
    parser.add_argument("--until", type=int, metavar="YEAR")
    parser.add_argument("--publisher", help="substring match on publisher")
    parser.add_argument("--project", help="only sources recorded by this project folder")
    parser.add_argument("--shared-by", action="append", metavar="PROJECT",
                        help="repeatable; keeps sources present in every named project")
    parser.add_argument("--used-in", metavar="ID",
                        help="idea, lane or candidate id, e.g. C12, L04, V03, D07")
    parser.add_argument("--uid", help="look up one source by its database uid")
    parser.add_argument("--doi", action="store_true", help="only sources that carry a DOI")
    parser.add_argument("--verified", action="store_true",
                        help="only sources whose content was actually fetched")
    parser.add_argument("--show", action="store_true",
                        help="also print the supported claim, usage ids and source files")
    parser.add_argument("--format", choices=["text", "json", "csv", "bib"], default="text")
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--count", action="store_true", help="print the match count only")
    parser.add_argument("--raw", action="store_true",
                        help="pass the search text to FTS5 verbatim instead of quoting terms")
    args = parser.parse_args(argv)

    con = connect()
    sql, params = build_query(args)
    try:
        rows = con.execute(sql, params).fetchall()
    except sqlite3.OperationalError as exc:
        raise SystemExit(f"query error: {exc}\n(FTS5 syntax: quote phrases, use OR / NOT / prefix*)")

    if args.count:
        print(len(rows))
        return 0
    if not rows:
        print("no matches", file=sys.stderr)
        return 1

    if args.format == "json":
        out = []
        for row in rows:
            rec = dict(row)
            rec["used_in"] = used_in(con, row["uid"])
            rec["occurrences"] = [dict(o) for o in occurrences(con, row["uid"])]
            out.append(rec)
        print(json.dumps(out, ensure_ascii=False, indent=1))
    elif args.format == "csv":
        import csv as _csv
        writer = _csv.writer(sys.stdout)
        writer.writerow(rows[0].keys())
        for row in rows:
            writer.writerow(list(row))
    elif args.format == "bib":
        emit_bibtex(rows)
    else:
        emit_table(con, rows, args.show)
        print(f"\n{len(rows)} match{'es' if len(rows) != 1 else ''}"
              f"{' (limit reached)' if len(rows) == args.limit else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
