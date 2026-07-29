# Project state

- Status: STAGE_60_COMPLETE
- Current stage: `60_research_program` (complete) → next: `70_redteam`
  (model/effort per `MODEL_POLICY.md`)
- Completed stages: 10 / 12
- Next action: run/resume the parent one-command launcher to start
  `70_redteam` (adversarial review of the full output set, now
  including the stage-60 program/gates/brief trio).

## Stage 60 outputs (this run)

- `outputs\06_INTEGRATED_RESEARCH_PROGRAM.md` — three-step verdict:
  CONFIRMED IN SUBSTANCE, REFINED IN ORDER AND SCOPE (Hall-first
  confirmed as hard gate; hybrid-second confirmed with FT-05 pulled
  into the first bench block and the claim narrowed to the §3.6 C36
  gaps; module-third REORDERED — T0 estimator/simulation core first as
  the falsification instrument, frozen package + publication last).
  All 5 prompt alternatives dispositioned (early bench test adopted;
  embedded actuation gated not default; rad-hard reference demoted to
  witness; radiation deferred collaborator-led — binding; abandon-if-
  simpler kept live via FT-07/K5/K6). Phases 0–6 with all 9 required
  fields each; publication map P1–P4 integrated with folder-06 routes;
  collaboration timing with per-lane evidence packs; budget Tiers 1–3
  (only sourced prices are folder-06's own ~$90/~$8 BOM figures,
  labeled; all else cost drivers + categories); boundaries B1–B8;
  kill criteria K1–K10.
- `outputs\06_DECISION_GATES_AND_ROADMAP.md` — ordered gates
  DG-00…DG-11 (order = cost; every expensive step behind a cheaper
  falsification gate) with dependencies, pass/fail/pivot paths,
  external-gate marking (06-G1 anomaly, campaign windows, 06-M28,
  06-G5), checkpoints CP-A…CP-H, 7 resume-ready next tasks. Gate-name
  collision between folder-06 G0–G5 and stage-30 G0–G5 recorded as a
  conflict and resolved via 06-G*/HY-G* prefixes (originals preserved).
- `outputs\06_ADVISOR_MEETING_BRIEF.md` — one-sentence decision + 5
  sub-decisions; rides the existing folder-06 advisor meeting;
  30-second technical summary; unresolved-risk list (C14, RR-13
  common-mode blindness, single-source H059/R071, P2 novelty race,
  06-G1 inheritance); lowest-cost next experiments (FT-02
  zero-hardware; FT-04 one bench-day); 6 advisor questions.
- Validation: `tools\validate_60_outputs.py` (new, reusable) 34/34
  PASS — existence/nontriviality, exact ledger header (parsed fields),
  219/37/24 row counts, all cited source/claim/FT/FM/RR IDs resolve
  (zero invented IDs), all acceptance markers present, all 9 outputs
  CSVs re-parsed.
- Checkpoint: `state\checkpoints\CP_60_research_program_20260727-042418.md`.
- Produced and signed off by Fable 5 (xhigh); no auxiliary models; no
  sibling or prior-stage file modified; no outreach or external write.

## Stage 50 outputs (this run)

- `outputs\05_LIMITATIONS_AND_FAILURE_MODES.md` — 18 failure modes
  FM-01…FM-18 (gate ≥15), each with cause/symptom/detectability/
  consequence/mitigation/residual-risk/test and a coverage map onto all
  15 stage-required areas; potential separated into 6 value classes,
  every one conditional on a measurable advantage and an identifiable
  calibration path; narrowest-defensible-contribution verdict after the
  2007/2022/2025 direct prior art ([H006]/[H007]; [H003]/[H004];
  [H001]/[H002]) — the broad hybrid idea is stated plainly as NOT novel
  (C01/C27/C29); 7 counterexamples where a simpler sensor wins.
- `outputs\05_TECHNOLOGY_COMPARISON.csv` — 15 technologies (gate ≥10),
  exact 20-column stage header, deterministic builder
  `tools\build_05_technology_comparison.py`; all required classes
  (hybrid; GaN/InSb/metal-film/graphene Hall; B-dot/Mirnov; Rogowski/
  CT+zero-flux DCCT; fluxgate; TMR; AMR; planar Hall; FOCS; NMR; SQUID;
  NV); `unknown`/`not_applicable` in place of fake precision; 5 rows
  explicitly marked COUNTEREXAMPLE; every evidence_id resolves.
- `outputs\05_FALSIFICATION_TESTS.md` — 12 tests FT-01…FT-12 ordered
  cheapest→most expensive; hypothesis/setup/reference/metric/threshold/
  confounders/decision/evidence for each; FT-01…FT-10 radiation-free,
  each carrying a stop/descope decision, so the project can stop before
  any radiation work; FT-11/FT-12 collaborator-led behind G0–G3
  (stage-30 §9.4 decoupling preserved).
- Validation: `tools\validate_50_outputs.py` 33/33 PASS (existence/
  nontriviality, exact header, row/mode/test counts, per-item required
  fields, honesty markers, counterexample count, full ID resolution
  against ledger/evidence map/risk register, FM↔FT cross-references).
- Reusable tools kept: `tools\build_05_technology_comparison.py`,
  `tools\validate_50_outputs.py`.
- Checkpoint: `state\checkpoints\CP_50_limitations_comparison_20260727-041056.md`.
- Produced and signed off by Fable 5 (xhigh); no auxiliary models; no
  sibling or prior-stage file modified; no outreach or external write.

## Stage 40 outputs (prior run, unchanged)

- `outputs\04_APPLICATION_SCORECARD.csv` — 6 rows (tokamak long-pulse,
  stellarator mapping, z-pinch/pulsed-power, MIF/plasma-jet, SC/HTS/
  motors-generators, accelerator magnets as the 6th evidence-supported
  application); exact stage header; documented 0–5 rubric with vetoes
  from stage 20/30 (Theorem 1, C28, C30, C35 partial) and stage-10C/10D
  novelty finding (C29) applied without score override, per
  `DECISION_FRAMEWORK.md`. Ranked 1 stellarator (HSX, internal) → 2
  tokamak → 3 accelerator (monitor) → 4 SC/HTS (monitor) → 5 MIF → 6
  z-pinch (both do-not-prioritize).
- `outputs\04_COLLABORATION_STRATEGY.md` — scoring rubric/weights (no
  `notes` column in the scorecard, so recorded here per stage
  instruction); ranked recommendation table; per-application
  prerequisites tied to stage-30 gates G0–G5; non-sent scientific-ask
  outlines (all explicitly labeled PROPOSED, NOT SENT); cross-cutting
  risks (radiation scope creep, competitor framing on C06, export
  control, access-verification honesty); fallback path showing no
  dissertation-relevant claim depends on external collaboration
  succeeding; consistency statement (no veto relaxed by score).
- `outputs\04_COLLABORATOR_CANDIDATES.csv` — 10 ranked candidates across
  all 6 lanes (IPP CAS Prague, KFE/KSTAR, W7-X/IPP Greifswald, PPPL/
  NSTX-U, ITER/ITPA, CEA/WEST, Cambridge Bulk Superconductivity, CERN
  TE-MSC, Sandia Z/Mykonos, LANL P-24); every official_url independently
  fetched/verified live 2026-07-27 except two honestly flagged as
  unreachable-this-session (CERN micro-site DNS failure; www.pppl.gov
  site-wide 403, mitigated with a live NSTX-U mirror) rather than
  asserted; no personal contact details anywhere.
- Validation: `tools\validate_40_outputs.py` 21/21 PASS (existence,
  exact headers, row counts, rank permutations, veto-present-on-every-
  do-not-prioritize-row, evidence/publication ID resolution against
  `01_SOURCE_LEDGER.csv`/`01_EVIDENCE_MAP.csv`, PROPOSED-NOT-SENT label
  on every ask, zero contact-detail leakage).
- Reusable tools kept: `tools\build_04_application_scorecard.py`,
  `tools\build_04_collaborator_candidates.py`, `tools\validate_40_outputs.py`.
- Checkpoint: `state\checkpoints\CP_40_applications_collaboration_20260727.md`.
- No sibling file (`..\06`, `..\07_HSX_august2025_results`, root `01`
  files, runner/policy files, prior-stage outputs) was modified; no
  outreach, contact, or external write occurred.

## Stage 30 outputs (prior run, unchanged)

- `outputs\03_RADIATION_COMPENSATION_ARCHITECTURE.md` — 8-option
  comparison (A–G + layered option H); recommended MVD "anchored hybrid"
  (pair + machine-current/field-model anchor + zero-field epochs) and
  higher-accuracy "triangulated self-test hybrid" (+ embedded cal
  winding/lock-in + repeated-waveform tracking, + material-diverse
  witness at top tier); full parameterization, block interfaces,
  embedded-winding analysis (gain products only; offset structurally
  blind to AC injection; triangle-closure test; winding referenced by
  anchor triangulation, never assumed stable); 4 compensation modes;
  uncertainty budgets; in-situ vs ex-situ mechanism table; budget tiers
  T0–T3 with gates G0–G5 and stop rules; §9.4 binding HSX-paper
  decoupling (radiation testing is NOT a prerequisite — conflict C6
  discipline).
- `outputs\03_SIMULATION_AND_VALIDATION_PLAN.md` — state-space truth
  model, parameter schema (species-vector + placeholder-basis
  enforcement so no fake GaN numbers can enter), 12 pre-registered
  scenarios, 14 fault injections, 8 metrics (incl. non-identifiability
  honesty test), regression binding to stage-20 rank tests, 7-rung
  ladder with standards/sample sizes/stop rules, module interface spec,
  simulated/bench/radiation evidence boundary.
- `outputs\03_RADIATION_RISK_REGISTER.csv` — 24 rows RR-01…RR-24, exact
  stage header, parse-verified, all evidence_ids resolve.
- Validation: `tools\validate_30_outputs.py` 13/13 PASS (headers, counts,
  ID resolution for CSV + both MDs; zero invented IDs).
- Reusable tools kept: `tools\build_03_risk_register.py`,
  `tools\validate_30_outputs.py`.
- Checkpoint: `state\checkpoints\CP_30_radiation_compensation_20260727-033513.md`.
- Fable downgrade count in current cycle: 0 (stage 30 outputs and final
  response produced by Fable 5 / xhigh; no auxiliary models).
- No sibling file (`..\06`, `..\07_HSX_august2025_results`, root `01`
  files, runner/policy files, prior-stage outputs) was modified.

## Stage 20 verdicts (consumed by stage 30, unchanged)

- Theorem-1 two-parameter gauge non-identifiability of the unreferenced
  pair; Hall→coil feasible (C02), coil→Hall gain-only conditional, offset
  never; quasi-static regime yields nothing; absolute scale always
  external. See `outputs\02_*`.

## Evidence base (stage 10D, unchanged)

- `outputs\01_SOURCE_LEDGER.csv`: 219 unique rows, 215 verified
  peer-reviewed (gate ≥120); quotas all met; 0 duplicate IDs/DOIs/titles.
- `outputs\01_EVIDENCE_MAP.csv`: 37 typed claims (C01–C37).

## Earlier stages (00, 10A–10D, 20)

See `state\WORKLOG.md` and per-stage checkpoints in `state\checkpoints\`.

The PowerShell attempt JSON and completion markers become authoritative
after execution starts.
