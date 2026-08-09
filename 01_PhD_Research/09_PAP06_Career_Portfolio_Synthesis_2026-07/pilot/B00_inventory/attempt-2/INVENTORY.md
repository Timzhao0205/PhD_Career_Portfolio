# PILOT SAMPLE — NOT FINAL

# B00 Inventory — pilot corpus map (attempt 2, repair)

Support stage. Factual mapping only — no ranking, scoring, or portfolio
decisions appear anywhere in this document. This is a repair of attempt-1,
which was rejected solely because its `RUN_META.md` lacked this banner.
Content below was re-verified by this agent against the sources it cites
(Glob existence checks, direct file reads, and targeted Grep on
`evidence/SOURCE_MANIFEST.json`) before being carried forward; corrections
found during re-verification are marked **[attempt-2 correction]** inline.
Manifest-derived facts remain attributed to `evidence/SOURCE_MANIFEST.json`
(this agent still has no hashing/code-execution capability, so SHA-256
"matched" claims themselves are attributed, not independently recomputed).

## The four corpus roots

### sources/old06 — completed prior "Folder 06" mission
Imported as an immutable 419-file corpus (archive `06_ideas(9).zip`,
`included_files: 419`, `skipped_duplicate_files: 0`). Per its own
`00_README_START_HERE.md`, it is a one-command Claude Code mission
targeting >=600 sources, >=48 candidates, and a final portfolio of 24
startup ideas for 2030 company formation. Numbered top-level structure
runs `01_MISSION` through `99_AUDIT` (`01_MISSION`, `05_STATE`,
`10_SOURCE_ATLAS`, `20_OPPORTUNITY_POOL`, `30_SCREENING`, `40_DEEP_DIVES`,
`50_GEOGRAPHY`, `60_FINAL_PORTFOLIO`, `90_BIBLIOGRAPHY`, `98_RUN_LOGS`,
`99_AUDIT`), plus `_claude_source/` and `tools/` holding renamed (inert)
former agent/executable files. Re-Globbed at the root and at
`60_FINAL_PORTFOLIO` in this attempt; structure confirmed unchanged.

### sources/new06 — rerun/current package layered on old06
Archive `06_ideas_new(3).zip` (`included_files: 255`,
`skipped_duplicate_files: 419` — the 419 old06 files, recognized as
duplicates at build time). Per `INPUT_PROVENANCE.md`, the imported old06
corpus is kept for provenance only and "the new rerun must not use their
conclusions as judgment inputs." Structure: root policy/manifest docs,
`prompts/`, `pilot/`, `outputs/` (per-stage; canonical release under
`outputs/70_audit/FINAL`), `state/`, `logs/`, `quarantine/`,
`tests/fixtures/`, `_claude_source/`. Re-Globbed at the root and at
`outputs/70_audit/FINAL` (recursive) in this attempt; structure and the
20-file FINAL/ release confirmed unchanged.

### sources/phd — repaired PhD-research package
Archive `01_phd_work(4).zip` (`included_files: 1145`). Paths were
shortened during a build-time repair (`PHD_HYBRID_2026-07-27` -> `P`,
`01_PhD_Research` -> `01`, `06_PhD_Strategy_and_HSX_Publication_2026-07`
-> `06`) per `sources/phd/P/EXTRACTION_FIX_REPORT.md`, whose recorded
source SHA-256 (`52cdf744aab33c6c2a477c5652461e7881d7af8bf3a0cbd2bc25be1849dd3af1`)
was re-read verbatim in this attempt and matches exactly. Research arc,
per `P/01/01_Folder_Info.md`: GaN Hall-effect magnetic sensing for fusion
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
top-level `02_Startup_Folder_Info.md` file exists but is empty on disk
(re-confirmed in this attempt).

## Exactly one canonical artifact per corpus (pilot scope)

| Corpus | Canonical artifact | Status evidence |
|---|---|---|
| old06 | `sources/old06/60_FINAL_PORTFOLIO/00_EXECUTIVE_PORTFOLIO.md` (+ sibling files in the same folder) | `05_STATE/MASTER_STATE.json` mission=COMPLETE; `99_AUDIT/FINAL_AUDIT.md` opens "## PASS", dated 2026-07-14 |
| new06 | `sources/new06/outputs/70_audit/FINAL/` (primary file `PORTFOLIO/PORTFOLIO.json`) | `outputs/70_audit/AUDIT.md`: "the canonical release under FINAL/ validates"; `state/RUN_COMPLETE.json` status=COMPLETE, completed_at_utc=2026-07-28T07:34:04Z |
| phd | `sources/phd/P/01/06/outputs/FINAL_EXECUTIVE_STRATEGY.md` (+ `FINAL_ACTION_PLAN.md`, `FINAL_DELIVERABLE_INDEX.md`, `FINAL_AUDIT.md`) | `06/outputs/FINAL_AUDIT.md` closing line "FINAL STATUS: PASS", validators re-run 2026-07-25 (line 52, re-located in this attempt) |
| startup | `sources/startup/01_Startup_Opportunity_Research_2026-07/60_PHASE6_SYNTHESIS/00_EXECUTIVE_SUMMARY.md` | `05_STATE/MASTER_STATE.json` mission=COMPLETE (all 8 phases); `99_AUDIT/FINAL_AUDIT.md` VERDICT PASS-WITH-EXCEPTIONS |

Full reasoning, sibling-file lists, and quoted evidence for each choice
are in `INPUT_MAP.json`. All four canonical-artifact paths were re-opened
and their canonicity evidence re-read verbatim in this attempt; no
correction was needed for the old06, new06, or phd rows. The phd row's
red-team-disposition summary is stated more precisely here than in
attempt-1 — see **[attempt-2 correction]** below.

**[attempt-2 correction]** Attempt-1 described the phd corpus's stage-70
red-team disposition as "0 critical/0 high findings," which is accurate
but incomplete: `FINAL_AUDIT.md` section 7, re-read in this attempt,
states the full breakdown as "0 critical, 0 high, 1 medium, 6 low, 4
informational." This attempt quotes the full breakdown in `INPUT_MAP.json`
to avoid any implied "zero findings" reading. This is a precision
correction, not a reversal of attempt-1's PASS conclusion.

## The old-06 duplicate relationship

Per `evidence/SOURCE_MANIFEST.json`'s `deduplicated` array (attributed
claim only, re-Grepped and re-read verbatim at lines 1512-1528 in this
attempt): the 419-file old06 tree nested inside both the `new06` supplied
package (`new06/src/06`) and the `startup` archive
(`startup/06_Frontier_Idea_Research_2026-07`, plus its own redundant
nested transport zip) was recognized as a byte-for-byte duplicate of
`sources/old06` ("419/419 files matched by relative path and SHA-256
before build") and was **not** re-included in this built package. Archive
counters corroborate this: old06's archive shows
`skipped_duplicate_files: 0`, while new06's and startup's archives show
`skipped_duplicate_files: 419` and `420` respectively (startup's extra 1
is the redundant nested zip member) — re-Grepped and re-confirmed in this
attempt. A Glob spot check on this filesystem, re-run in this attempt,
confirmed `sources/new06/src/**`,
`sources/startup/06_Frontier_Idea_Research_2026-07/**`, and
`sources/startup/*.zip` all still return no files — consistent with, but
not an independent cryptographic proof of, the manifest's claim. Full
file-count recounts remain out of pilot scope.

## Newly found during attempt-2 re-verification (not in attempt-1)

`sources/startup/01_Startup_Opportunity_Research_2026-07/05_STATE/
MASTER_STATE.json` records `unique_sources: 689`. The same corpus's own
`99_AUDIT/FINAL_AUDIT.md` section 1, re-read in this attempt, states
"Unique-URL count: 690 entries, 690 distinct `id` values, 690 `url`
fields" for the same bibliography (`90_BIBLIOGRAPHY/sources.json`). This
is a genuine 1-record numeric conflict between two of the corpus's own
cited documents that attempt-1 did not catch (it quoted only the
MASTER_STATE.json figure). Recorded, not resolved — see `CONFLICTS.md`
#6.

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
- Reconciliation of the newly-found 689-vs-690 startup unique-source-count
  discrepancy, and reconciliation guidance for the old06-vs-new06 scoring
  discrepancy noted in `CONFLICTS.md` (these are Fable/strategic
  decisions, not pilot- or support-stage tasks).
- Web-based freshness-gap checks for any primary source touched (not
  performed in this pilot; see `RUN_META.md`).
