# 00_SOURCE_DATABASE — every startup source, in one place

**3,432 unique sources**, merged from **14,543 raw records** across **177 files**
in all seven `02_Startup` research projects. Deduplication collapsed 76 % of the
raw corpus: the same document was, on average, recorded four times.

The point of this folder is that a future research round should never have to
re-find or re-verify a source this portfolio already owns. Search here first.

## Files

| File | Use it for |
|---|---|
| `sources.sqlite` | Querying. Full-text index plus `sources`, `occurrences` and `usage` tables. |
| `sources.json` | Programmatic access to the complete records, including every occurrence. 9.3 MB. |
| `sources.csv` | Spreadsheets and pandas. One row per source, list fields joined with ` \| `. |
| `STATISTICS.md` | Coverage: by project, type, tier, verification, language, year, publisher. |
| `build_log.json` | Which files were read, how many records each contributed, what was skipped, and every merge the builder refused to make. |
| `SCHEMA.md` | Field-by-field definition of a source record. |
| `tools/build_source_database.py` | Rebuild everything from the projects. |
| `tools/query.py` | Command-line search. |

## Quick start

```bash
cd 02_Startup/00_SOURCE_DATABASE

python3 tools/query.py "no-insulation winding"          # full-text
python3 tools/query.py "超导" --lang zh                  # Chinese works too
python3 tools/query.py --used-in C12                    # everything behind idea C12
python3 tools/query.py --type patent --jurisdiction US --since 2020
python3 tools/query.py --uid S310b6bee2962 --show       # one source, in full
python3 tools/query.py --type academic --tier T1 --format bib > seed.bib
```

`--show` prints the claim the source was cited for, the idea/lane ids it
supports, and every file that recorded it — which is usually the fastest way to
find the analysis that already used it.

Ask what two rounds had in common:

```bash
python3 tools/query.py --shared-by 01_Startup_Opportunity_Research_2026-07 \
                       --shared-by 06_Frontier_Idea_Research_2026-07
```

Or go straight to SQL:

```bash
sqlite3 sources.sqlite "
  SELECT jurisdiction, COUNT(*) FROM sources
  WHERE source_type='patent' GROUP BY 1 ORDER BY 2 DESC;"

sqlite3 sources.sqlite "
  SELECT s.title, s.url FROM sources_fts f JOIN sources s ON s.uid=f.uid
  WHERE sources_fts MATCH '\"quench detection\"' ORDER BY rank LIMIT 10;"
```

## What it covers

| Project | Sources |
|---|---:|
| 02_Novel_Lanes_Research_2026-07 | 1,638 |
| 06_Frontier_Idea_Research_2026-07 | 1,291 |
| 01_Startup_Opportunity_Research_2026-07 | 686 |
| 03_C12_C10_Strategy_IP_2026-07 | 448 |
| 07_Frontier_Ideas_Interactive_2026-07 | 331 |
| 05_CryoFree_HTS_RND_2026-07 | 164 |
| 04_Cocktail_Dilution_Sensor_2026-07 | 4 |

Rows sum to more than 3,432 because 974 sources are shared between projects.

Included: every `*sources*.json` and `SOURCES.json` in each project, the
per-lane source atlases, the red-team and deep-dive evidence files, the Gen-1/2
CSV evidence ledgers, `30_PATENTS/patent_ledger.json` plus the ten per-cluster
patent files, the CryoFree prior-art ledgers, and project 04's hand-kept
markdown ledger.

Deliberately excluded, and why:

- `07_Frontier_Ideas_Interactive_2026-07/tests/` and `pilot/` — offline
  fixtures, not gathered evidence.
- `07_Frontier_Ideas_Interactive_2026-07/src/06/` — a deduplicated snapshot of
  project 06, which is already read directly.
- `90_BIBLIOGRAPHY/BIBLIOGRAPHY.md` in projects 01 and 02 — human-readable
  renderings of the `sources.json` next to them, with no extra records.
- `99_AUDIT/_adjudication_workdir/` — scratch files from an audit run.

The intermediate merge snapshots under
`06_Frontier_Idea_Research_2026-07/98_RUN_LOGS/` *are* read. They add no new
sources, but they show which records existed before each dedupe pass, which is
useful provenance.

## How records are merged

Two records become one source when they agree on a strong identifier — DOI,
patent publication number (compared without its kind code, so `US12196792` and
`US12196792B2` are one document), or arXiv id — or when they share a normalised
URL, or an identical distinctive title.

A weak signal never overrides a strong one. If two records share a title but
carry different patent numbers they stay separate: patent family members are
published under one title but are different documents with different claims.
Every merge the builder refused is written to `build_log.json` under
`blocked_merges` — 14 of them, all correct on inspection.

When merged records disagree, the builder keeps:

- the **strongest tier** anyone assigned (all gradings survive in `tiers_seen`);
- the **strongest verification** anyone reached (`fetched` > `abstract` >
  `snippet` > `not_fetched`);
- the **longest** claim, note and author string, on the grounds that the longer
  one is the more informative;
- the **most common** publisher, year, language and type;
- the **union** of URLs, geographies, usage ids and projects.

Nothing is dropped: `occurrences` records every file and original record id the
source came from, so any merge can be traced back and undone by hand.

## Rebuilding

```bash
python3 tools/build_source_database.py --dry-run   # report, write nothing
python3 tools/build_source_database.py             # regenerate all five outputs
```

The build is deterministic — rerunning it on an unchanged tree reproduces
byte-identical output apart from the timestamp in `build_log.json`. Rerun it
after any research round that adds sources; new projects are picked up
automatically as long as their source files match the usual naming.

## Known rough edges

These are properties of the underlying corpus, not bugs to hide:

- **1,034 sources (30 %) are typed `other`.** They are mostly records that
  carried no type field at all and whose URL gave no reliable hint. The
  original free-text label, where there was one, survives in `source_types_raw`.
- **`publisher` mixes names and bare domains** (`IEEE Spectrum` next to
  `nih.gov`). The Gen-1/2 CSV ledger recorded a domain where the JSON dialects
  recorded a name, and inventing names for domains would be guessing.
- **299 sources have no tier** and 242 no verification status — those fields did
  not exist in every project's schema.
- **286 sources carry more than one recorded title.** Usually a paraphrase or a
  translation of the same page. In a handful of cases a project cited a rolling
  index page — ITER's open-tender list is the clearest — for several different
  items on it, so those items merge into one record. The underlying records
  never had per-item URLs, so splitting them would not recover distinct
  documents. Every recorded title survives in `titles_seen`, and
  `query.py --show` prints them.
- **A URL-only source that a later project recorded with a DOI stays split** if
  the titles were also written differently. This is the residual failure mode of
  identifier-based merging; the true unique count is a little below 3,432.
