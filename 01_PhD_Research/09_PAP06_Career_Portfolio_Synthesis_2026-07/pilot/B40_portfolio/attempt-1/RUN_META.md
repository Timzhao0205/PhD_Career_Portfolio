# RUN_META — B40_portfolio PILOT attempt-1

**PILOT SAMPLE — NOT FINAL.**

- Stage: `B40_portfolio`
- Mode: `PILOT`
- Attempt: 1
- Target: `pilot/B40_portfolio/attempt-1/`
- Named agent: `pap06-fable-xhigh`
- Requested model: Fable 5
- Requested effort: xhigh
- Observed model: `claude-fable-5` — the runtime system prompt explicitly
  states "You are powered by the model named Fable 5. The exact model ID is
  claude-fable-5." Recorded as an explicit runtime exposure of model
  identity, consistent with the requested model. This is self-reported
  runtime context, not an independent provider audit.
- Observed effort: NOT_EXPOSED (no runtime effort evidence exists in this
  environment; per MODEL_POLICY, missing observation is neither a mismatch
  nor proof).
- Run date: 2026-07-28. Start/end wall-clock times: not exposed by the
  environment; recorded as NOT_EXPOSED.

## Sources consulted (all read this run, within the task card's allowance)

Prerequisite outputs (read directly):
- `state/CURRENT_TASK.md`; `workflow/stages/B40_portfolio.md`
- Root policies: `SOURCE_POLICY.md`, `LIT_POLICY.md`, `MODEL_POLICY.md`,
  `MODEL_PLAN.md`; project `CLAUDE.md` contract
- `outputs/B20_align/attempt-1/ALIGNMENT.csv` (all 39 rows) and
  `ALIGNMENT.md` §3 class table (grep-targeted)
- `outputs/B25_power/attempt-1/POWER_MAP.csv` (all 32 rows) and
  `POWER.md` §8-§10 (incl. the full §9 wedge verdict)
- `outputs/B30_skills/attempt-1/SKILLS.md` (full) and `BRIDGES.json` (full)
- `outputs/B15_lit_synth/attempt-1/LIT_REVIEW.md` §4-§8 read directly
  (evidence boundaries); §1-§3 via section outline plus the carried
  adjudications in B20/B25/B30 — disclosed as partial-depth
- `outputs/A30_verify/attempt-1/COMPARE.json` (set definitions, membership,
  pairwise metrics, SEM ledger), `VERDICT.md` (full), `SOURCES.csv` (full)
- `outputs/B10_phd/attempt-1/OPT2.md` (full)
- `outputs/B20_align/attempt-1/SOURCES.csv` and
  `outputs/B25_power/attempt-1/SOURCES.csv` (rows S-B25-01..05) for exact
  URLs/limitations of reused opened primaries

Not read: `sources/`, `evidence/`, `archive/`, other pilots, any B12 raw
ledger content beyond what B15 carries. No file outside the allowance was
opened; nothing outside the target directory was written.

## Web activity

- WebSearch x2 (discovery only, snippets not cited as evidence):
  1. "ABB SACE Infinitus solid-state circuit breaker DC data center available"
  2. "Siemens SENTRON 3QD2 solid-state circuit breaker DC availability"
- WebFetch x3:
  1. `press.siemens.com` SENTRON 3QD2 launch press release — OPENED
     (SOURCES.csv B40P-01)
  2. `new.abb.com` SACE Infinitus product page — FAILED (60s timeout)
  3. `abb.com` innovation-news page (Infinitus) — FAILED (60s timeout)
- Purpose: one decision-critical recheck of the record-vintage claim that
  merchant 800VDC-class SSCBs already ship (presses P3R2-C-01's window;
  B25 had flagged "live verification would settle it"). Result: Siemens
  launch verified on an opened primary; ABB remains discovery-level —
  carried honestly in RANKING.csv/DECISION.json/SOURCES.csv.
- No other live opens; all other current-market facts rest on A30/B20/B25
  opened primaries (reused without re-opening, flagged per row) or are
  labeled corpus-dated.

## Retries / anomalies

- Two WebFetch timeouts (ABB pages), disclosed above and in SOURCES.csv
  B40P-02; no retry loop beyond the two attempts (different ABB URLs).
- No provider safeguards, refusals, account limits, or model mismatch
  events were encountered. No budget/turn/time threshold was applied.

## Limitations of this run

- Pilot scope: six ideas only; every artifact is labeled
  "PILOT SAMPLE — NOT FINAL" and ranks nothing outside the sample.
- Scores are coarse ordinal aggregates with disclosed overlapping bands;
  ranks 1-3 are not statistically separated.
- Sensitivity stability (zero flips) is provable within this sample but is
  partly a sample-construction artifact; the caveat is recorded in
  DECISION.json.
- The ABB shipping-status leg of the SSCB window question could not be
  live-verified (timeouts); the Siemens leg was.
- B15 §1-§3 were not re-read line-by-line this run (section outline +
  carried adjudications); §4-§8 — the sections this stage's judgments
  lean on — were read directly.
- Startup-corpus records (ST01/ST03) are used only as B25/B30 carried
  them: documented engineering analyses, not verified market facts.
