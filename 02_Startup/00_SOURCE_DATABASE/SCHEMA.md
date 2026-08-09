# Source record schema

One record describes one document. `sources.json` carries every field;
`sources.sqlite` carries all of them except `source_types_raw`, `project_ids`
and the nested `occurrences` (those become the `occurrences` and `usage`
tables); `sources.csv` carries the subset most useful in a spreadsheet.

A field is `null` (JSON) or empty (CSV/SQLite) when no project recorded it.
Nothing is invented — if the corpus never stated a publication year, `year` is
null rather than guessed from the access date.

## Identity

| Field | Type | Meaning |
|---|---|---|
| `uid` | string | `S` + the first 12 hex of `sha1(canonical_key)`. Stable across rebuilds as long as the canonical key does not change. Use it to cite a source in notes. |
| `canonical_key` | string | What identity was established on, in precedence order: `doi:…`, `patent:…` (country + serial, no kind code), `arxiv:…`, `url:…` (normalised), `title:…` (slug), or `record:<file>#<id>` when nothing identifying survived. |

## Bibliographic

| Field | Type | Meaning |
|---|---|---|
| `title` | string | Best available title. A Latin-script title wins over a CJK one when both exist, because the English gloss is what the analyses quote. |
| `titles_seen` | list | Every distinct title any project recorded for this document. More than one means a paraphrase, a translation, or a shared index page. |
| `title_original` | string | Non-English original title, when recorded separately. |
| `authors_or_org` | string | Authors, inventors, or the issuing organisation. Formatting is inherited from the source project and is not consistent. |
| `publisher` | string | Journal, venue, publisher, issuing body — or, for records that came from the Gen-1/2 CSV ledger, a bare domain. |
| `year` | int | Publication year. Taken from an explicit year field, else parsed from a date. |
| `date` | string | Publication date as recorded. Format varies (`2025-09-12`, `2024-10`, `2023-n.d.`). |
| `language` | string | ISO-ish code as recorded: `en`, `zh`, `zh-cn`, `ja`, `ko`, `hi`. |
| `geography` | list | Country/region codes the source speaks to, not where it was published. |

## Locators

| Field | Type | Meaning |
|---|---|---|
| `url` | string | Primary URL — the first of `all_urls` in sort order. |
| `all_urls` | list | Every distinct URL recorded for this document, e.g. publisher page plus PMC mirror. |
| `doi` | string | Lowercased, trailing punctuation stripped. URL-derived DOIs are truncated at the first suffix segment. |
| `arxiv_id` | string | Bare `NNNN.NNNNN`, no version suffix. |
| `patent_number` | string | Fullest publication number seen, kind code included. |
| `patent_family` | list | Other numbers the record listed for the same invention. |
| `jurisdiction` | string | `US`, `CN`, `EP`, `WO`, `JP`, `KR`, … |
| `assignee` | string | Patent assignee. |
| `cpc` | list | CPC classification codes, patents only. |

## Classification

| Field | Type | Meaning |
|---|---|---|
| `source_type` | string | One of `academic`, `preprint`, `patent`, `government`, `standards`, `industry`, `company`, `news`, `think_tank`, `dataset`, `book`, `other`. |
| `source_types_raw` | list | The original free-text labels, before folding. JSON only. |
| `tier` | string | `T1` primary/official, `T2` peer-reviewed or established secondary, `T3` other secondary. The strongest tier any project assigned. |
| `tiers_seen` | list | Every tier assigned, so a disagreement stays visible. |

## Evidence quality

| Field | Type | Meaning |
|---|---|---|
| `verification` | string | How firmly the content was confirmed: `fetched` (page actually retrieved) > `abstract` > `snippet` (search result only) > `not_fetched`. |
| `access_level` | string | Paywall status as recorded: `public`, `open`, `paywalled`, … Kept separate from `verification`. |
| `peer_review_status` | string | As recorded by project 06/07, which checked this against Crossref. |
| `accepted` | bool | Whether every project that graded it accepted it. `false` means at least one rejected it — read `notes` before reusing. |
| `claim_supported` | string | What the source was cited to evidence. The longest such statement across projects, which is normally the most specific. **Read this before reusing a source**: it says what the source actually establishes, not what it is about. |
| `notes` | string | Merged caveats, limitations and rejection reasons. |

## Provenance

| Field | Type | Meaning |
|---|---|---|
| `projects` | list | Project folders that recorded this source. |
| `project_ids` | object | `{project: [original record ids]}`. JSON only. |
| `used_in` | list | Idea, lane, candidate, domain and cluster ids the source was cited under — `C12`, `L04`, `V03`, `D07`, `P01`, `CF-3`, … |
| `first_accessed` / `last_accessed` | string | Earliest and latest access date recorded. |
| `n_occurrences` | int | How many raw records merged into this one. |
| `occurrences` | list | `{project, stage, file, record_id}` for every distinct place it appears. JSON only; the SQLite `occurrences` table holds the same rows. |

## SQLite tables

```sql
sources      -- one row per unique source; list fields joined with ' | '
occurrences  -- uid, project, stage, file, record_id     (14,018 rows)
usage        -- uid, used_in                             (6,292 rows)
sources_fts  -- FTS5 over title, authors_or_org, publisher, claim_supported, notes
```

Indexed on `occurrences(uid)`, `occurrences(project)`, `usage(uid)`,
`usage(used_in)`, `sources(source_type)`, `sources(tier)`, `sources(year)`,
`sources(jurisdiction)`.

The FTS5 index uses the `unicode61` tokenizer, which does not segment Chinese,
Japanese or Korean. `tools/query.py` detects a CJK query and switches to `LIKE`
automatically; if you query the database directly, do the same.
