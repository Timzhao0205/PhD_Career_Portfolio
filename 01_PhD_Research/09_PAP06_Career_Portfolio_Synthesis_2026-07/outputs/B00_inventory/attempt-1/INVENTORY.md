# B00 Inventory — full corpus map (attempt 1)

Support stage. Factual mapping only — no ranking, scoring, or portfolio
decisions appear anywhere in this document. Extends the accepted pilot
(`pilot/B00_inventory/attempt-2/`): its four roots, four canonical artifacts,
and the old06 duplicate relationship were re-confirmed present by fresh Glob
this attempt; no discrepancy from the pilot's own re-verified content was
found. Full quoted evidence and machine-readable detail are in
`INPUT_MAP.json`; this file is the human-readable map and Fable handoff.

## The four corpus roots

### sources/old06 — completed prior "Folder 06" mission (419 files)
Archive `06_ideas(9).zip`, `included_files: 419`, `skipped_duplicate_files: 0`.
Mission ran 2026-07-12 to 2026-07-14 (98_RUN_LOGS/ jsonl timestamps, plus a
2026-07-13 ChatGPT continuation for P4 scoring per
`CHATGPT_CONTINUATION_LOG.md` — this is the source of the "CONTRADICTED"
decision-layer provenance flag carried over from `outputs/A30_verify/`).
Structure: `01_MISSION` (brief/rubric/spec/templates), `05_STATE`
(MASTER_STATE.json), `10_SOURCE_ATLAS` (16 lane ledgers, raw+verified+t1topup
variants), `20_OPPORTUNITY_POOL` (incl. the elegance/duplicate-cluster
adjudication file), `30_SCREENING` (EVIDENCE/REDTEAM/SCORECARDS, the frozen
65-idea longlist), `40_DEEP_DIVES` (10 reports), `50_GEOGRAPHY`,
`60_FINAL_PORTFOLIO` (canonical release), `90_BIBLIOGRAPHY` (sources.json
only, no companion .md ledger), `98_RUN_LOGS` (raw transcripts, routing log,
ChatGPT handoff backup), `99_AUDIT`. `_claude_source/` and `tools/` hold
renamed/inert former agent and script files.

### sources/new06 — rerun/current package layered on old06 (255 files)
Archive `06_ideas_new(3).zip`, `included_files: 255`,
`skipped_duplicate_files: 419` (old06's files, recognized as duplicates).
Completed **2026-07-28T07:34:04Z** — the freshest of the four corpora,
same-day as this session. Per `INPUT_PROVENANCE.md`, old06's P4-P8
conclusions are provenance-only and must not be used as judgment inputs by
the rerun. Structure: root policy/manifest docs, `prompts/` (one per stage),
`outputs/` (10_refresh through 70_audit, canonical release under
`outputs/70_audit/FINAL/` — `README.md` line 100 literally labels this
"Canonical audited package"), `state/`, `logs/`, `pilot/` (this package's
own internal pilot-stage self-tests, not to be confused with this project's
`pilot/` directory), `quarantine/` (two dated incident folders — see "New
findings" below), `tests/fixtures/` (deterministic outputs/ mirror for
validator testing), `_claude_source/`.

### sources/phd — repaired PhD-research package (1145 files)
Archive `01_phd_work(4).zip`, `included_files: 1145`,
`skipped_duplicate_files: 0`. Paths shortened at build time
(`PHD_HYBRID_2026-07-27`→`P`, `01_PhD_Research`→`01`,
`06_PhD_Strategy_and_HSX_Publication_2026-07`→`06`) per
`P/EXTRACTION_FIX_REPORT.md`. Research arc: GaN Hall-effect magnetic sensing
for fusion diagnostics (HSX stellarator). Contains publication/hardware
folders (`02_HSX_Hall_Sensor_Readout`, `03_HSX_Vector_Probe_RSI2026`), raw
HSX data (`07_HSX_august2025_results`), a **completed** PhD
research-strategy mission (`06/`, validators re-run 2026-07-25), and the
**"Opt2" continuation mission** (`08_Hall_Coil_Hybrid_Radiation_Strategy_
2026-07/`, in progress — see below).

### sources/startup — multi-project startup corpus (524 files)
Archive `02_Startup(6).zip`, `included_files: 524`,
`skipped_duplicate_files: 420` (419 old06 files + 1 redundant nested
transport zip). Five sub-missions at different completion states (see
"Startup sub-mission states" below): `01_Startup_Opportunity_Research_
2026-07` (complete, audited — the corpus's selected canonical),
`03_C12_C10_Strategy_IP_2026-07` (in progress, blocked since 2026-07-04),
`04_Cocktail_Dilution_Sensor_2026-07` (not started),
`05_CryoFree_HTS_RND_2026-07` (self-reports complete but has no audit
folder — see "New findings"), `99_Archive` (legacy pre-staged notes, no
completion marker).

## The Opt2 corner (phd folder 08) — for B10_phd

`workflow/stages/B10_phd.md` defines "Opt2" as the PhD corpus's future
continuation option: (1) calibrate/validate a Hall sensor as an
uncertainty-bounded instrument, (2) integrate Hall plus inductive coils as a
hybrid diagnostic, (3) deliver a reusable module plus simulation package.
The literal string "Opt2" does not appear inside `sources/phd` (Grep
returned zero files); it is a workflow label, and its three elements match
`sources/phd/P/01/08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07/`'s subject
matter exactly.

**Status, re-confirmed unchanged from the pilot this attempt:**
`state/PROJECT_STATE.md` — "Status: STAGE_60_COMPLETE", "Completed stages:
10 / 12", next stage `70_redteam`. 12 stages are defined in `prompts/`
(00_inventory through 80_synthesis); 10 have output files under `outputs/`
(31 files total, listed in `INPUT_MAP.json`); **`70_redteam` and
`80_synthesis` have no output files yet** — no `FINAL_*`-pattern deliverable
exists for folder 08, unlike folder 06. `P/01/README_HYBRID_RADIATION_
ANALYSIS.md` describes 08 as reading 06's completed work; the dependency is
one-directional.

**Handoff note for B10_phd:** the most synthesis-like documents currently
available are `06_INTEGRATED_RESEARCH_PROGRAM.md` and
`06_DECISION_GATES_AND_ROADMAP.md` under 08's `outputs/`, but these are
*pre-redteam and pre-synthesis* by the corpus's own process — B10 should
mark claims drawn from them accordingly (not yet adversarially reviewed at
the corpus's own internal stage-gate level), independent of B10's own
no-ranking rule.

## Startup sub-mission states (full sweep)

| Sub-mission | State (self-reported) | Audit folder present? |
|---|---|---|
| `01_Startup_Opportunity_Research_2026-07` | `mission: COMPLETE` (8/8 phases) | Yes — `99_AUDIT/FINAL_AUDIT.md`, PASS-WITH-EXCEPTIONS |
| `03_C12_C10_Strategy_IP_2026-07` | `mission: IN_PROGRESS`, round 3; phase5/phase6 pending; blocked 2026-07-04 (API session limit) | `99_AUDIT/` exists but only holds `_about.md` — no FINAL_AUDIT-equivalent found |
| `04_Cocktail_Dilution_Sensor_2026-07` | `phase_status: NOT_STARTED`, budget_spent_usd=0 | No |
| `05_CryoFree_HTS_RND_2026-07` | `phase: COMPLETE` (self-reported, RUN_STATE.json) | **No** `99_AUDIT/`-equivalent folder found anywhere in the tree |
| `99_Archive` | No completion marker | No |

Only `01_Startup_Opportunity_Research_2026-07` was selected as the startup
corpus's one canonical artifact, because it is the only sub-mission with
BOTH a self-reported COMPLETE state AND an independent audit folder. This
is a factual, attributed selection criterion, not a judgment about the
value of the other four sub-missions' content.

## New findings this attempt (beyond pilot scope)

1. **new06 quarantine records a documented in-run model event.**
   `quarantine/model_event_20260728/ADJUDICATION.json` (read in full):
   during context compaction, `claude-opus-5` (xhigh) was observed as an
   auxiliary compaction model after two Fable-5 compaction attempts were
   rejected by Fable safeguards. The package's own disposition:
   `files_written_under_non_fable_model: []`, classification
   `auxiliary_compaction_model_only`, `fable_downgrade_of_accepted_work:
   false`. A companion `package_repair_20260728/REPAIR.json` records a
   same-day hooks/settings.json repair. This event is timestamped
   ~50 minutes before new06's own `RUN_COMPLETE.json` completion time.
   Recorded as an attributed, corpus-internal fact; not adjudicated here.

2. **05_CryoFree_HTS_RND_2026-07 self-reports COMPLETE but has two open
   provenance gaps of its own.** No `99_AUDIT/`-equivalent folder exists
   anywhere in its tree (unlike old06, new06, phd/06, and startup/01). All
   21 of its own gate records (7 candidates × G-PHYS/G-NOVEL/G-CLAIM) pair
   `"model_intended": "GATE:fable-5"` with `"model_served_verified":
   false`. Neither gap is resolved by this stage.

3. **03_C12_C10_Strategy_IP_2026-07 remains blocked in progress**, unchanged
   in kind from what a partial pilot read would have shown, now confirmed
   in full detail: 216 tracked patent records, 14 invention disclosures at
   varying redteam maturity, phase5/phase6 explicitly `pending`.

## Duplicate groups (full sweep)

1. **old06 canonical relationship** (build-time dedup, manifest-attributed):
   `new06/src/06` and `startup/06_Frontier_Idea_Research_2026-07` (+ its own
   nested zip) were both omitted from the built package as duplicates of
   `sources/old06` ("419/419 files matched by relative path and SHA-256
   before build"). Re-confirmed by a Glob spot check this attempt
   (`sources/new06/src/**`, `sources/startup/06_Frontier_Idea_
   Research_2026-07/**`, `sources/startup/*.zip` — all three return zero
   files). **old06 is represented exactly once in this filesystem and
   exactly once in this inventory's roots list.**
2. **startup 99_Archive files echoed in 01's saturation-check REFERENCE/
   folder** (`june25_research.md`, `china_feasibility_deep_dive.md`,
   `frontier_rank_red_team.md`) — path-observed, not hash-verified.
3. **new06 tests/fixtures mirrors outputs/ by name** — deterministic
   validator test fixtures, inferred from context (BUILD_FIXTURES.py.source.txt
   present alongside), not independently hash-verified.
4. **startup/03's 00_PRIOR_CORPUS/DEEPDIVES echoes filenames from startup/01's
   40_PHASE4_DEEPDIVES** — expected/documented reuse (03 imports 01's
   baseline by its own design), not an anomaly.

No hash-level verification was possible for any of these (no code execution
available to this agent); all are attributed or path-observed claims.

## Conflicts (see CONFLICTS.md for full text)

Six items carried forward from the pilot and re-confirmed unresolved
(idea-ID score mismatch P3R2-D-02; phd 06-vs-08 completion asymmetry;
startup's no-single-final structure; the 70_SATURATION_CHECK date/numbering
anomaly; the attributed-not-verified old06 dedup claim; the startup
689-vs-690 unique-source count). Plus new items opened this attempt (see
CONFLICTS.md #7-#9): the new06 model-event/repair quarantine record, the
05_CryoFree audit-folder-absence and gate-model-service gap, and a
restated/expanded 03_C12_C10 blocked-in-progress record.

## Freshness gaps for later stages to close

Corpus run dates relative to the session's current date (2026-07-28):
old06 (2026-07-14, 14 days stale), startup/01 and startup/03 (~2026-07-04,
24 days stale), startup/04 (2026-07-07, 21 days stale), startup/05
(2026-07-10, 18 days stale), phd/06 (2026-07-25, 3 days stale), phd/08
(2026-07-27, still incomplete), new06 (2026-07-28, same day). Primary-source
domain types observed across bibliographies: peer-reviewed journals/IEEE/IOP
(low freshness risk), standards/government/OSTI/USPTO, and — highest
freshness risk — vendor/press/product-announcement pages and patent-office
records that change on weekly-to-monthly timescales. Two targeted web
checks were performed this attempt (EPA EtO NESHAP page currency;
USPTO Patent Public Search domain currency) — see SOURCES.csv and
`INPUT_MAP.json.freshness_gaps` for full results; neither check resolved or
re-adjudicated any strategic disagreement already recorded in
`outputs/A30_verify/attempt-1/COMPARE.json`.

## Handoff: what each later Fable stage should read first

- **B10_phd** (PhD + Opt2 fact extraction): start with
  `sources/phd/P/01/06/outputs/FINAL_EXECUTIVE_STRATEGY.md` and
  `FINAL_DELIVERABLE_INDEX.md` for the completed baseline, then
  `sources/phd/P/01/08_.../outputs/06_INTEGRATED_RESEARCH_PROGRAM.md` and
  `06_DECISION_GATES_AND_ROADMAP.md` for Opt2 — marking the latter two as
  pre-redteam/pre-synthesis per the corpus's own process. `01_SOURCE_LEDGER.csv`
  (06) and `01_SOURCE_LEDGER.csv`/`01_EVIDENCE_MAP.csv` (08) are the
  claim-to-source traceability files. Do not treat 08 as complete or as
  superseding 06.
- **B20_align** and **B50_execution** (per their own specs, not read in
  depth by this support stage beyond confirming they also reference "Opt2"):
  should treat `outputs/A30_verify/attempt-1/COMPARE.json` as the existing
  old06-vs-new06-vs-blind reconciliation and NOT re-derive it; this
  inventory's `duplicate_groups` and `conflicts` sections tell them where
  the same idea IDs and source counts diverge across corpora so they don't
  silently pick one.
- **Any stage touching startup**: read `01_Startup_Opportunity_
  Research_2026-07/60_PHASE6_SYNTHESIS/00_EXECUTIVE_SUMMARY.md` for the
  corpus's one audited synthesis; treat `03_C12_C10_Strategy_IP_2026-07`'s
  content as real-but-unaudited IP material, and `05_CryoFree_HTS_RND_
  2026-07`'s content as real-but-self-reported-complete-without-audit
  material — do not upgrade either to "audited" status.
- **Any stage needing current facts**: consult `INPUT_MAP.json.
  freshness_gaps` for the domain-type list and corpus-date table before
  treating any corpus's market/regulatory/product claim as current.
