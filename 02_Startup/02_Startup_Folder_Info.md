# 02_Startup — folder index

Venture research and product-development work, kept separate from the PhD
(`../01_PhD_Research/`) and from investing (`../03_Investments_and_Finance/`).

Two things live here. **Projects 01→03 and 06→07** are successive rounds of one
long search for a company to found around 2029–2030, each round narrowing or
deliberately widening the previous one. **Projects 04 and 05** are hands-on
technical projects spun out of that search.

## Start here

| If you want… | Go to |
|---|---|
| Every source ever gathered, in one queryable place | `00_SOURCE_DATABASE/` |
| The current best answer to "what should I found?" | `06_Frontier_Idea_Research_2026-07/60_FINAL_PORTFOLIO/` |
| The two locked winners and their IP position | `03_C12_C10_Strategy_IP_2026-07/60_STRATEGY/` |
| A buildable side product | `04_Cocktail_Dilution_Sensor_2026-07/` |

## The search rounds

### `01_Startup_Opportunity_Research_2026-07` — Round 1: opportunity landscape
Seven phases across 10 domain landscapes → ≥36 candidate ideas (C01–C40) →
scored matrix → red-team → 12 deep dives → US/China policy brief → Top-7 plus a
2026→2030 roadmap. 689 sources. Phase folders are numbered `10_`→`70_`;
`90_BIBLIOGRAPHY/` and `99_AUDIT/` close it out.

### `02_Novel_Lanes_Research_2026-07` — Round 2: novel lanes and showdown
Searches only the lanes Round 1 never covered, under a hard exclusion of all
~100 prior concepts, then merges the survivors (V01–V15) with the incumbent
best-of-best for a final Top-5. Carries Round 1 forward in `00_PRIOR_CORPUS/`.
1 217 sources — the largest single bibliography in this folder.

### `03_C12_C10_Strategy_IP_2026-07` — Round 3: competitors, patents, whitespace
Takes the two locked winners — **C12** (NI/MI-HTS winding cells with inline QC
and recipe software) and **C10** (fast-dynamics precision magnet power
converters) — and builds a competitor map, a US+CN patent landscape, scored
whitespace slots, and drafted invention disclosures with FILE / REWORK / DROP
verdicts. Patents live in `30_PATENTS/patent_ledger.json`, not in the
bibliography.

### `06_Frontier_Idea_Research_2026-07` — Round 4: clean-slate frontier search
Restarts from zero with the founder's EE background deliberately downweighted
to a 2 % feasibility prior, so background does not choose the lanes. 16 lanes
(L01–L16) → 48+ concepts → a final portfolio of 24 ideas aimed at a 2030
launch. 1 289 sources, the most heavily verified set here (Crossref-checked
DOIs, per-source peer-review evidence). This is the current state of the
search.

### `07_Frontier_Ideas_Interactive_2026-07` — Round 4 rerun, interactive harness
The same Round 4 corpus re-run through a rewritten package: interactive Claude
Code instead of PowerShell child processes, no budget/turn stop, hook and stage
fixtures, per-stage checkpoints. Results in `outputs/`, staged `10_refresh` →
`70_audit`. Its `src/06/` used to hold a second full copy of Round 4 — see
that folder's `README.md`.

## The technical projects

### `04_Cocktail_Dilution_Sensor_2026-07`
Real-time dilution/ABV instrument for stirred drinks: capacitive permittivity
sensing plus thermistor and IMU. Phased build — benchtop dipstick → clip-on
inner-wall probe → instrumented barspoon. Deliberately separable from PhD work.
Sources are a short hand-maintained ledger in `90_REFERENCES/SOURCES.md`.

### `05_CryoFree_HTS_RND_2026-07`
Patent-discovery engine for cryogen-free / conduction-cooled HTS components,
following C12 out of Round 3. Simulates, novelty-checks and patent-shapes
candidates CF-1…CF-7; prior art per candidate in `60_PRIOR_ART/`, drafted
disclosures in `70_DISCLOSURES/`, 112 sources in `90_SOURCES/`.

## Shared conventions

- Two-digit prefixes order both projects and the stages inside them. `01_`
  mission, `05_`/`80_` durable state, `90_` sources, `98_` run metrics,
  `99_` audit.
- Every research round is a self-contained Claude Code package with its own
  `CLAUDE.md` (binding rules), `00_README_START_HERE.md`, and `.claude/agents/`.
  Launch `claude` from the project folder, not from here.
- Source records are JSON, one array of objects per file, and are graded by
  tier (T1 primary/official → T3 secondary). `SOURCE_STANDARDS.md` in each
  mission folder defines that project's rules.
- Nothing in a `99_AUDIT/` folder is decorative — those are the self-audits
  that decide whether a round's conclusions were allowed to stand.

## Cross-project source reuse

`00_SOURCE_DATABASE/` unifies every source record from all seven projects into
one schema — deduplicated, provenance-tagged, and queryable as JSON, CSV or
SQLite. Use it before starting a new round so the same URL never has to be
re-verified twice. See its `README.md` for the schema and query recipes.
