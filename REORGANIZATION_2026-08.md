# Reorganisation — 2026-08-08

Three things were asked for: import the HSX IP/arXiv package into
`01_PhD_Research`, de-duplicate and reorganise `01_PhD_Research` and
`02_Startup`, and build one reusable database of every source the startup
research ever gathered.

The working tree went from **1.04 GB to 0.39 GB**. No content was lost — every
deletion was either a byte-identical duplicate of something still in the
repository, or is reconstructible by a script committed alongside it. Git
history holds the originals regardless.

---

## 1. HSX IP/arXiv package imported

`HSX_IP_ARXIV_2026-08.zip` → `01_PhD_Research/10_HSX_IP_and_arXiv_Screen_2026-08/`

The archive nested the payload two levels deep
(`HSX_IP_ARXIV_2026-08/HSX_IP_ARXIV/…`); that was flattened. All 66 files
imported unchanged.

The package is a publication-only IP triage for the manuscript submitted
2026-07-02. Its verdict is
`NO_PUBLICATION_SPECIFIC_FILING_CASE_IDENTIFIED`, with a pre-posting
ownership/sponsor checkpoint still recommended. Start at
`outputs/70_EXEC_SUMMARY.md`.

---

## 2. Content recovered

**`01_Publications/submitted/regular_lsens/`** — the complete LaTeX project for
the submitted manuscript (sources, five figures, graphical abstract, IEEE class
file, compiled PDF; 4.4 MB) existed *only* inside a package input snapshot,
where nothing would have found it. It now sits in the publications folder.
The same files are also archived inside
`10_HSX_IP_and_arXiv_Screen_2026-08/inputs/manuscript/source_original.zip`.

---

## 3. Duplicates removed

Each was verified byte-identical (after normalising CRLF to LF, which git
introduces on checkout) before deletion.

| Removed | Why | Freed |
|---|---|---|
| `01_PhD_Research/06/` | A stale copy of `06_PhD_Strategy_and_HSX_Publication_2026-07` recorded before that folder was renamed. Same session ids, same timestamps, same 334 files; the 60 that differed differ only in the folder-path strings embedded in their text. | 58 MB |
| `02_Startup/06_Frontier_Idea_Research_2026-07.zip` | Exact archive of the folder next to it (419/419 files). | 36 MB |
| `02_Startup/06_ideas_new.zip` | Exact archive of the F06I package (674/674 files). | 37 MB |
| `02_Startup/99_Archive/` | All 12 files duplicated `02_Novel_Lanes_Research_2026-07/00_PRIOR_CORPUS/GEN1_GEN2/`, which is where the Novel Lanes round actually reads them from. | 1.2 MB |
| `__pycache__/` trees | Python bytecode. Now covered by `.gitignore`. | small |

---

## 4. Vendored snapshots replaced by manifest + rehydration

Two run packages each shipped with a full copy of research that still lives in
its own project folder, so the package could run standalone from a ZIP. Inside
this repository those copies were pure duplication.

| Snapshot | Was | Now |
|---|---|---|
| `01_PhD_Research/09_…/sources/` | 2,344 files, 366 MB | 98 files, 1.6 MB — 2,236 removed; 41 genuinely unique files and 57 empty placeholders kept |
| `02_Startup/07_…/src/06/` | 405 files, 164 MB | manifest + tooling only — all 405 were byte-identical to `06_Frontier_Idea_Research_2026-07` |

Each snapshot root now carries:

- `SNAPSHOT_MANIFEST.csv` — one row per removed file: `snapshot_path`,
  `canonical_path`, `bytes`, `sha256_lf`, `match`.
- `SNAPSHOT_PATH_RULES.json` — folder-rename substitutions needed to reproduce
  `path_variant` rows exactly.
- `rehydrate.py` — restores every removed file and verifies each against its
  recorded hash.
- `README.md` and a generated `.gitignore` so restored copies do not dirty
  `git status`.

```bash
python3 01_PhD_Research/09_PAP06_Career_Portfolio_Synthesis_2026-07/sources/rehydrate.py
python3 02_Startup/07_Frontier_Ideas_Interactive_2026-07/src/06/rehydrate.py
```

**Round trip verified.** Both snapshots were fully restored and every one of the
2,641 files matched its recorded LF-normalised SHA-256, then removed again.

60 of the 2,236 rows are `path_variant`: they came from `01/06/`, the pre-rename
name of `06_PhD_Strategy_and_HSX_Publication_2026-07`. They are the same run —
identical session ids and timestamps — recorded under the old folder names, and
`rehydrate.py` reproduces them byte-for-byte from the surviving folder.

---

## 5. Renames

| Before | After | Why |
|---|---|---|
| `01_PhD_Research/09` | `01_PhD_Research/09_PAP06_Career_Portfolio_Synthesis_2026-07` | A bare `09` said nothing. This is the PAP06 native package: Operation A rebuilds the 126-idea blind pool score-free, Operation B runs PhD core → literature → alignment → power → skills → portfolio → execution. Paused at stage B50. |
| `02_Startup/07_ideas_new/F06I_INTERACTIVE_NOCAP_PS51/F06I` | `02_Startup/07_Frontier_Ideas_Interactive_2026-07` | Three nested folders for one package, none of them descriptive. The only references to the old path are historical Windows paths inside log records. |
| `04_Magnetic_Sensor_Review_Sensors2026/.codex_tmp` | `…/advisor_review` | Not a temp directory — it holds the advisor's marked-up abstract, the comment set, and the accepted-changes renders. |

`07_HSX_august2025_results` was left alone despite its inconsistent casing: 194
files reference that exact path.

---

## 6. The startup source database

New: **`02_Startup/00_SOURCE_DATABASE/`**

3,432 unique sources merged from 14,543 raw records across 177 files in all
seven startup projects — five JSON dialects, a CSV evidence ledger, a patent
ledger, and a hand-kept markdown ledger, all mapped onto one schema.
Deduplication collapsed 76 % of the corpus: the average document had been
recorded four times.

- `sources.sqlite` — `sources`, `occurrences` and `usage` tables plus an FTS5
  index.
- `sources.json` / `sources.csv` — the same records for code and spreadsheets.
- `tools/query.py` — search by text (CJK included), type, tier, language,
  jurisdiction, year, project, or the idea/lane id a source was cited under;
  output as text, JSON, CSV or BibTeX.
- `tools/build_source_database.py` — deterministic rebuild; rerun after any
  round that adds sources.
- `STATISTICS.md`, `SCHEMA.md`, `build_log.json` — coverage, field definitions,
  and a record of every file read, every record skipped, and every merge the
  builder refused to make.

Merging is identifier-first: DOI, then patent number compared without its kind
code, then arXiv id, then normalised URL, then distinctive title. A weak signal
never overrides a strong one — records sharing a title but carrying different
patent numbers stay separate, because patent family members publish under one
title. The 14 refused merges are logged and were checked by hand.

`README.md` in that folder lists the known rough edges honestly, including the
30 % of sources typed `other` and the handful of rolling index pages whose
distinct items merge into one record.

---

## 7. Documentation rewritten

- `README.md` at the repository root — new; indexes all three tracks.
- `01_PhD_Research/01_PhD_Research_Folder_Info.md` — covered only projects
  01–03; now covers 01–10.
- `01_PhD_Research/CLAUDE.md` — folder map extended to every package, with the
  note that each carries its own binding `CLAUDE.md`.
- `02_Startup/02_Startup_Folder_Info.md` — was an empty file; now describes the
  five search rounds, the two technical projects, and the shared conventions.
- `.gitignore` — new; Python caches, editor noise, and per-machine Claude
  settings.

---

## What was deliberately not done

- `03_Investments_and_Finance/` was left untouched — outside the request.
- `07_HSX_august2025_results` keeps its lowercase name (194 references).
- No research output, state file, workflow specification, or measured value was
  edited anywhere. The only file contents that changed are the documentation
  listed in section 7.
