# PILOT SAMPLE — NOT FINAL

# B00 Inventory — pilot corpus map

Support stage. Factual mapping only — no ranking, scoring, or portfolio
decisions appear anywhere in this document. Every manifest-derived fact
below is attributed to `evidence/SOURCE_MANIFEST.json` and was not
independently re-verified (this agent has no hashing/code-execution
capability).

## The four corpus roots

### sources/old06 — completed prior "Folder 06" mission
Imported as an immutable 419-file corpus (archive `06_ideas(9).zip`,
`included_files: 419`). Per its own `00_README_START_HERE.md`, it is a
one-command Claude Code mission targeting >=600 sources, >=48 candidates,
and a final portfolio of 24 startup ideas for 2030 company formation.
Numbered top-level structure runs `01_MISSION` through `99_AUDIT`
(`01_MISSION`, `05_STATE`, `10_SOURCE_ATLAS`, `20_OPPORTUNITY_POOL`,
`30_SCREENING`, `40_DEEP_DIVES`, `50_GEOGRAPHY`, `60_FINAL_PORTFOLIO`,
`90_BIBLIOGRAPHY`, `98_RUN_LOGS`, `99_AUDIT`), plus `_claude_source/` and
`tools/` holding renamed (inert) former agent/executable files.

### sources/new06 — rerun/current package layered on old06
Archive `06_ideas_new(3).zip` (`included_files: 255`,
`skipped_duplicate_files: 419` — the 419 old06 files, recognized as
duplicates at build time). Per `INPUT_PROVENANCE.md`, the imported old06
corpus is kept for provenance only and "the new rerun must not use their
conclusions as judgment inputs." Structure: root policy/manifest docs,
`prompts/`, `pilot/`, `outputs/` (per-stage; canonical release under
`outputs/70_audit/FINAL`), `state/`, `logs/`, `quarantine/`,
`tests/fixtures/`, `_claude_source/`.

### sources/phd — repaired PhD-research package
Archive `01_phd_work(4).zip` (`included_files: 1145`). Paths were
shortened during a build-time repair (`PHD_HYBRID_2026-07-27` -> `P`,
`01_PhD_Research` -> `01`, `06_PhD_Strategy_and_HSX_Publication_2026-07`
-> `06`) per `sources/phd/P/EXTRACTION_FIX_REPORT.md`. Research arc, per
`P/01/01_Folder_Info.md`: GaN Hall-effect magnetic sensing for fusion
diagnostics (HSX stellarator). Contains publications/hardware folders
(`02_HSX_Hall_Sensor_Readout`, `03_HSX_Vector_Probe_RSI2026`), raw HSX
data (`07_HSX_august2025_results`), a completed PhD research-strategy
mission (`06/`), and a newer, in-progress sibling mission
(`08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07`) that explicitly reads
folder `06` as prior completed work.

### sources/startup — multi-project startup corpus
Archive `02_Startup(6).zip` (`included_files: 524`,
`skipped_duplicate_files: 420` — see duplicate relationship below).
Not one single arc but several parallel sub-missions at different
completion states: `01_Startup_Opportunity_Research_2026-07` (complete,
audited), `03_C12_C10_Strategy_IP_2026-07` (in progress), `04_Cocktail_
Dilution_Sensor_2026-07` and `05_CryoFree_HTS_RND_2026-07` (hardware R&D,
early/not started), and `99_Archive` (legacy pre-staged notes). A
top-level `02_Startup_Folder_Info.md` file exists but is empty on disk.

## Exactly one canonical artifact per corpus (pilot scope)

| Corpus | Canonical artifact | Status evidence |
|---|---|---|
| old06 | `sources/old06/60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md` (+ sibling files in the same folder) | `05_STATE/MASTER_STATE.json` mission=COMPLETE; `99_AUDIT/FINAL_AUDIT.md` VERDICT PASS, dated 2026-07-14 |
| new06 | `sources/new06/outputs/70_audit/FINAL/` (primary file `PORTFOLIO/PORTFOLIO.json`) | `outputs/70_audit/AUDIT.md`: "the canonical release under FINAL/ validates"; `state/RUN_COMPLETE.json` status=COMPLETE, completed_at_utc=2026-07-28T07:34:04Z |
| phd | `sources/phd/P/01/06/outputs/FINAL_EXECUTIVE_STRATEGY.md` (+ `FINAL_ACTION_PLAN.md`, `FINAL_DELIVERABLE_INDEX.md`, `FINAL_AUDIT.md`) | `06/outputs/FINAL_AUDIT.md` FINAL STATUS: PASS, validators re-run 2026-07-25 |
| startup | `sources/startup/01_Startup_Opportunity_Research_2026-07/60_PHASE6_SYNTHESIS/00_EXECUTIVE_SUMMARY.md` | `05_STATE/MASTER_STATE.json` mission=COMPLETE (all 8 phases); `99_AUDIT/FINAL_AUDIT.md` VERDICT PASS-WITH-EXCEPTIONS |

Full reasoning, sibling-file lists, and quoted evidence for each choice
are in `INPUT_MAP.json`.

## The old-06 duplicate relationship

Per `evidence/SOURCE_MANIFEST.json`'s `deduplicated` array (attributed
claim only): the 419-file old06 tree nested inside both the `new06`
supplied package (`new06/src/06`) and the `startup` archive
(`startup/06_Frontier_Idea_Research_2026-07`, plus its own redundant
nested transport zip) was recognized as a byte-for-byte duplicate of
`sources/old06` ("419/419 files matched by relative path and SHA-256
before build") and was **not** re-included in this built package. Archive
counters corroborate this: old06's archive shows
`skipped_duplicate_files: 0`, while new06's and startup's archives show
`skipped_duplicate_files: 419` and `420` respectively (startup's extra 1
is the redundant nested zip member). A Glob spot check on this
filesystem confirmed `sources/new06/src/**`,
`sources/startup/06_Frontier_Idea_Research_2026-07/**`, and
`sources/startup/*.zip` all return no files — consistent with, but not an
independent cryptographic proof of, the manifest's claim. Full file-count
recounts were explicitly out of pilot scope.

## What the full run must still add

- Complete recursive inventory of all four roots (Glob results were
  capped at 100 entries per call; only partial recursive listings were
  read for old06/phd/startup, and new06 was inventoried mainly via
  targeted `SOURCE_MANIFEST.json` greps rather than full Glob).
- A full read-through of `evidence/SOURCE_MANIFEST.json`'s `files` array
  (814KB; only sampled via targeted patterns in this pilot).
- Inventory of every non-canonical deliverable inside each corpus (source
  atlases, deep dives, screening evidence, quarantine folders, the phd
  `08` in-progress mission's stage outputs, and the startup corpus's
  `03`/`04`/`05`/`99` sub-projects).
- Any hash-level verification of manifest claims (outside this agent's
  capability — no code execution).
- Reconciliation guidance for the old06-vs-new06 scoring discrepancy
  noted in `CONFLICTS.md` (this is a Fable/strategic decision, not a
  pilot- or support-stage task).
- Web-based freshness-gap checks for any primary source touched (not
  performed in this pilot; see `RUN_META.md`).
