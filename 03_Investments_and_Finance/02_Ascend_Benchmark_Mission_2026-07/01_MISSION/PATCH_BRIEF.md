# PATCH_BRIEF — Accuracy Patch: +5 names and a Fable critical-review pass over all names

Amends the completed v1 mission. All CLAUDE.md hard rules remain binding (PAPER-ONLY,
NUMBER TRUTH RULE, disclaimers, spoiler boundary, zero user interaction, Chinese-language
search). Never overwrite a v1 artifact: patch outputs use `FR_<ticker>.md`, `*_v2.*`, and
new V_/F_/VAL_ files for the added names only. Educational benchmark; simulated
allocations; not investment advice.

## Division of labor (rationale, binding)
Fable is reserved for **judgment**: evidence adjudication, figure-conflict rulings,
implied-expectations reasoning, rescoring, adversarial review, portfolio construction,
changelog synthesis. Source **gathering stays on the sonnet-pinned workers**: extraction
accuracy is bounded by source access and diligence, not model capability, and burning the
Fable pool on fetch/extract buys no accuracy. critical-reviewer and red-team-critic have
NO model pin and inherit this session's Fable — never add pins to them.

## FABLE-FRUGALITY rules (binding — protects the remaining ~45% weekly Fable pool)
F1. critical-reviewer: ≤2 WebFetches and ≤120 output lines per ticker; judges from the
    v1 files, not from raw filings.
F2. Reviews run in batches of 4 tickers (3 parallel max); after each batch: update
    PATCH_STATE.json, one PROGRESS_LOG line, SAFE-STOP point (a kill/resume here loses
    nothing).
F3. Orchestrator keeps its own context lean: read summaries and CSVs, not every V_/F_
    file in full.
F4. Fallback trigger: if the run is interrupted by a Fable weekly cap, the resume
    priority order is: 5 new names first, then v1 top-10 by SCORES.csv total, then the
    remainder; un-reviewed names are marked FR-DEFERRED in SCORES_v2.csv (column
    fr_status) rather than silently reusing v1 scores.

## Phases

### PP0 — Setup
Read MASTER_STATE.json (must be COMPLETE), SCORES.csv, VERIFIED_WATCHLIST.csv,
99_AUDIT/AUDIT_REPORT.md. Init PATCH_STATE.json. Verify v1 artifacts present; list them
read-only.

### PP1 — Universe expansion (+5)
Candidate pool = documented leads only, in priority order: (a) discovery leads logged in
ASSUMPTIONS/PROGRESS_LOG during v1 (e.g., the A10 noted-not-added name; the S204
西部证券 backplane-connector names not yet in universe such as 意华股份 002897 / 航天电器
002025), (b) prior-corpus WATCHLIST layers currently absent or thin in the universe
(power: 泰嘉股份 002843, 杰华特 688141; cooling: 英维克 002837; PCB/substrate: 兴森科技
002436, 南亚新材 688519; packaging materials: 华海诚科 688535; switching: 盛科通信).
**Fable selects the 5** by lead strength (tier-B-or-better evidence available) and layer
diversity vs the existing 14; selection rationale to `10_PHASE1_VERIFICATION/
EXPANSION_SELECTION.md` (no rankings of existing names). Then the sonnet workers run the
FULL v1 treatment on the 5 (filing-auditor → fundamentals-analyst → valuation-analyst,
same schemas, same gates), appending to the v1 CSVs with a `patch=1` marker column left
out — instead add rows normally and note additions in the file header comment line.
**Gate PG1:** 5 new V_/F_/VAL_ files + CSV rows + ledger merged, no S-ID collisions
(patch block: S900+ then S1000+ as needed).

### PP2 — Fable critical review (all 19)
critical-reviewer per ticker (spec in its agent file): evidence-tier adjudication,
3-figure verification (≤2 re-fetches), implied-expectations re-derivation, full 6-cell
rescore with delta table. Outputs `30_PHASE3_VALUATION_SCORING/FR_<ticker>.md`.
Orchestrator consolidates `SCORES_v2.csv` (schema = v1 + columns total_v1, delta,
fr_status). **Re-red-team:** every name with |delta| ≥ 0.5 and every new top-8 entrant
gets a red-team-critic pass (inherits Fable) + written response appended to
`REDTEAM_RESPONSES_v2.md`; rescore again where conceded.
**Gate PG2:** 19 FR_ files (or FR-DEFERRED per F4); every changed cell justified; every
triggered red team answered; SCORES_v2.csv complete.

### PP3 — Deliverables v2
- `40_PHASE4_PORTFOLIO/ANSWER_KEY_BENCHMARK_v2.md` — full reasoning + **CHANGELOG
  section**: every name whose rank or portfolio status changed vs v1, with the specific
  evidence or adjudication that moved it (this is the highest-learning-value artifact of
  the patch).
- `BENCHMARK_PORTFOLIO_v2.csv` — same construction rules (max 2 names/layer, ≤40%/layer,
  cash if <4 names clear 3.0).
- `SELF_TEST.md` — append a v2 addendum: if the blind attempt hasn't been done yet, v2 is
  now the answer key and 10_/20_ (including the 5 new names) is the evidence base; if the
  v1 self-test was already scored, re-score the same MY_ATTEMPT against v2 and treat the
  v1→v2 changelog as a worked example of how better adjudication changes conclusions.
- `BENCHMARK_WORKBOOK_v2.xlsx` (same 6 tabs, 19 names, v1/v2 score columns side by side;
  openpyxl round-trip test).
- `PREDICTIONS_APPEND_v2.csv` — new/changed predictions only.
**Gate PG3:** disclaimers, spoiler scan (rankings only in 30_/40_), workbook opens.

### PP4 — Mini-audit
source-auditor (sonnet): re-fetch spot check on 12 CHANGED figures (bias toward cells
that moved scores), ledger dedupe across v1+patch blocks, spoiler scan, deliverables
checklist. Output `99_AUDIT/PATCH_AUDIT.md`. "patch":"COMPLETE" only on PASS or on FAIL
with fixes applied and re-audited.

## Sizing (estimate, not promise)
5 names × full v1 treatment ≈ 20–35 fetches (Sonnet pool). Fable side: 19 reviews ×
(≤2 fetches + ≤120 lines) + ~4–8 re-red-teams + synthesis — designed to fit comfortably
inside the remaining ~45% weekly Fable budget with the F1–F4 guards; the SAFE-STOP
batching means a cap interruption costs nothing beyond a `-Resume` after Sunday 4:00 AM.
