# Project state

- Mission status: `COMPLETE` (all 12 stages; `outputs/FINAL_AUDIT.md`
  states `FINAL STATUS: PASS`; launcher post-completion result-model
  verification and marker write pending as its normal final step)
- Completed stages: 12 / 12 (`00_inventory`; `10a_literature_gan`;
  `10b_literature_fusion`; `10c_literature_methods`;
  `10d_literature_merge`; `20_direction`; `30_manuscript`;
  `40_experiment`; `50_patent`; `60_timeline`; `70_redteam`;
  `80_synthesis`)
- Current stage: `80_synthesis` (`COMPLETE`, attempt 1, cycle 0,
  session 4607ee04-07c9-41fe-8969-12b552782585, run_2026-07-24_231243_734;
  requested Fable 5 / Extra High; started 2026-07-25T02:57:00-07:00 true
  local time; see `state/checkpoints/CP_80_synthesis_20260725-030800.md`).
- Stage 80 result summary: four final outputs written strictly from the
  accepted red-team-corrected prior-stage work (no new direction,
  invention, experiment, or source-dependent claim). (1)
  FINAL_EXECUTIVE_STRATEGY.md — direct answer CONTINUE-with-substantial-
  adjustment (ADJUST/OPT2; scores 4.29 vs 3.45/3.34/2.58 re-verified),
  thesis + three evidence pillars, manuscript diagnosis + A→C route with
  modified-Route-D fallback, minimum next experiment (B-01 anomaly first,
  Tier-1 ≈19–29 bench-days, zero cleanroom), 24-month strategy (P1+P2
  MVG floor, campaign-independent critical path, defense Q2 2028),
  startup preparation, IP hold (G-C hard), five reversal triggers +
  contingency ladder, 07_RED_TEAM §3 limitations carried, operational
  observations (F-10/F-11 + stage-70 telemetry extension, C3/C4
  launcher deviations, C1 parent-record correction) surfaced. (2)
  FINAL_ACTION_PLAN.md — 72h/30d/90d/6mo/12mo/24mo tables each with
  owner, dependency, acceptance gate, fallback; 10-item do-not-do-yet
  list; 9-item advisor-meeting materials list. (3)
  FINAL_DELIVERABLE_INDEX.md — all 31 outputs with purpose/stage/
  validation + two reading orders. (4) FINAL_AUDIT.md — R001–R025 trace
  (all satisfied; R012/R013 documented deviations; R014 resume-path
  unexercised), ledger 231/231 verified ≥150, schema/dedup PASS,
  reviewer coverage 16 rows 1:1, model audit (0 downgrades/retries/
  quarantines/handoffs; stage-70 stream personally re-verified this
  stage: Fable init + Fable final main message), red-team disposition
  (11 findings: 9 corrected, 2 documented), 11 noncritical open gates,
  limitation statement; final line exactly `FINAL STATUS: PASS`.
  Validation this session: all six stage validators + both stage-70
  audit tools re-run PASS; stage-80 link/citation/final-line check PASS.
- Open gates at mission end (all noncritical, owned in
  FINAL_ACTION_PLAN.md): C017/G1 anomaly; I-4 module custody; die
  supply; U-1..U-9; advisor decisions 1–7; G-A..G-H (G-C hard); SENSL
  lapse query; RSI live-page recheck; metadata-only reconfirmation
  rule; C1 parent-record correction; optional provider-independent
  review via manual ChatGPT continuation.
- Previous stage: `70_redteam` (`COMPLETE`, attempt 1, cycle 0,
  session 779a7cec-ad19-4a78-a1af-e55b964deec5, run_2026-07-24_231243_734;
  requested Fable 5 / Extra High; final main response produced by the
  Fable session; started 2026-07-25T02:30:00-07:00 true local time; see
  `state/checkpoints/CP_70_redteam_20260725-034500.md`).
- Stage 70 result summary: adversarial audit of all 10 completed stages,
  method-independent (fresh deterministic scripts, md5-stratified 36-row
  sample distinct from 10D's, new verification channels) with
  provider-level independence explicitly NOT claimed. (1)
  07_SOURCE_AUDIT.csv — 46 rows, exact 11-col header: 36/36 stratified
  bibliographic-identity matches (9/9 lane×access cells, 7/7 year bands,
  all tiers, all 7 SOURCE_POLICY topic groups), deep checks (S0068
  full-text numbers, S0128 verbatim QHS sentence, S0002 secondary
  corroboration, PA-P01 patent status), external-policy re-verifications
  (SENSL live-verified; RSI wording verified verbatim via Internet
  Archive snapshot 2025-11-15 of the official page — stage-30 open gate
  CLOSED, with a new sharpening criterion "a previously published
  instrument is not considered to be novel" annotated into
  03_PUBLICATION_ROUTE_DECISION.md; Stanford EE year-3-committee/
  year-4-oral claims confirmed against ee.stanford.edu). (2)
  07_RED_TEAM.md — 11 findings: F-1 medium (M15 pre-ship gate depended
  on M09/M10 completion dated after its own target — corrected to
  status-freeze wording), F-2..F-7 low (roadmap M26→M27 arrow
  overstatement; "4.8-week post-acceptance" mislabel; missing Stanford
  URLs; Tier-1 burden 19–28→19–29; two "#4"→"#3" advisor-question
  cross-refs; RSI gate resolution), F-8..F-11 info (PA-P03 "102 prior
  art" softened to counsel wording; 4.1%→4.0% rounding; UTC-mislabeled
  -07:00 stamps in stage-written state entries and CP_50/CP_60 names —
  documented, not renamed; stage-30 security_fallback telemetry
  contradiction refuted by raw stream evidence: init + final main
  assistant message both claude-fable-5, Haiku only in aggregate
  modelUsage). Verdict: NO critical/high defects; source count,
  recommendation logic (stage 20/40 arithmetic recomputed exactly),
  novelty bounding, reviewer coverage (letter PDF re-read, 16/16 rows
  map 1:1), and safety/legal wording all clean. (3) 07_CORRECTION_LOG.md
  — 11 corrections across 7 earlier output files, before/after +
  validation; post-correction re-runs: 30/40/50/60 validators PASS,
  70 audits PASS.
- Stage 70 adds to the open-gate register: nothing new technical —
  existing gates carried unchanged (C017/G1 anomaly, I-4, die supply
  decision 3, U-1, U-9/G4, SENSL lapse query, G-A..G-H). New
  observations for the user: launcher telemetry items F-10/F-11;
  re-check the live RSI policy page before any actual submission.
- Previous stage: `60_timeline` (`COMPLETE`, attempt 1, cycle 0,
  session e289323f-da56-45ed-b54b-17e2b55db454, run_2026-07-24_231243_734;
  requested Sonnet 5 / High, non-Fable stage; started
  2026-07-25T09:35:00-07:00; see
  `state/checkpoints/CP_60_timeline_20260725-103000.md`)
- Stage 60 result summary: (1) `06_MILESTONES.csv` — 44 rows, exact
  13-column header, spanning 2026-07-25 to 2028-07-01 across 12
  workstream tags; every row cites the upstream stage 20/30/40/50 gate/
  work-package ID it schedules and carries a named slip_trigger +
  fallback. (2) `06_24_MONTH_PHD_ROADMAP.md` — critical path deliberately
  independent of HSX campaign success (bench→calibration→P1→P2→
  dissertation); month-by-month detail Aug 2026–Jan 2027, quarterly
  thereafter; low-cleanroom allocation; a 5-scenario slip/decision-point
  table; minimum-viable-graduation plan (P1+P2) vs. stronger-upside plan
  (P1+P2+P3); weekly rhythm + progress indicators; reconciles the
  stage-20-vs-project-03 P3-timing ambiguity and flags the tight
  Aug-2026 campaign-#1 target against today's date. (3)
  `06_STARTUP_READINESS.md` — discovery/validation/IP-coordination
  (defers entirely to stage 50's screen)/portfolio-artifacts/
  collaborator-boundaries/go-no-go sections, explicitly with no
  investment or transaction instructions. (4)
  `06_ADVISOR_MEETING_BRIEF.md` — the 7 decision-requested items,
  bench-only must-have measurements, the A→C venue route, the
  pre-publication hard gate, resource/HSX/collaborator questions, and
  dated 30/90/180-day commitments. Grounded committee/defense timing in
  two dated web lookups (Stanford EE graduate-degree-progress pages,
  accessed 2026-07-25) rather than inventing it. Deterministic validation
  PASS (`state/tools/60_validate.py`: exact header, 44 unique IDs, date
  parsing/ordering, dependency-ID cross-refs resolve, all relative links
  resolve, no immigration/legal-advice terms found).
- Stage 60 adds to the open-gate register: no technical/IP/route gate is
  resolved by this scheduling stage; it only dates the existing ones
  (advisor decisions 1–7 -> M02; UW e-mail/gate G-A -> M03; anomaly/gate
  G1 -> M06; die supply -> feeds M11/M21; advisor+OTL IP screen -> M13;
  arXiv hard gate G-C -> M19). One new judgment call for stage 70 to
  audit: the P3-timing reconciliation (upside ~Mar 2027 vs. realistic
  2027–2028 window) and the campaign-#1 August-target tightness flag —
  both are schedule arithmetic on already-established dependencies, not
  new technical claims.
- Previous stage: `50_patent` (`COMPLETE`, attempt 1, cycle 0,
  session 25d9ca42-2714-48b2-bfa2-86fda2cc9756,
  run_2026-07-24_231243_734; requested Fable 5 / Extra High; final
  result produced by the Fable main session, no auxiliary subagents
  used; see `state/checkpoints/CP_50_patent_20260725-093000.md`)
- Stage 50 result summary: (1) 05_PRIOR_ART_LEDGER.csv — 35 rows, exact
  13-column header: 11 patent/application rows (10 verified full-record
  on Google Patents 2026-07-25: Infineon spinning-current families
  US9389284B2 + US10663535B2, Ohio State GaN-2DEG Hall US20140266159A1
  (abandoned), DOE tokamak steady-state hybrid US5804965A (expired),
  Hall+coil US4994742A (expired), drift auto-cal US8134358B2 (active),
  GE cal-coil US6750644B1 (expired), MEMSIC US9658298B2, Everspin
  US8390283B2 (ceased), TI dual-path US10197638B2 (active); 1
  metadata-only WO2011119317A1) + 24 NPL rows (22 S-ID-resolved to the
  231-source ledger with DOI match; Dowling thesis + Popovic teslameter
  as new metadata rows). (2) 05_CANDIDATE_PROTECTABLE_CONCEPTS.md —
  six concepts ranked by maturity × urgency (CC-2 readout chain,
  CC-1 packaging stack, CC-5 vacuum-field anchor, CC-3 cube vector
  probe, CC-4 hybrid architecture, CC-6 retroactive conversion), each
  with concrete feature combinations, documentary basis without
  inventorship decisions, closest art, conditional distinctions,
  enablement status, and risks; all three disclaimer labels present.
  Key screen findings: thin-claims expectation confirmed (CC-2's
  controlling art is the group's own PA-N03 + active Infineon/TI
  patents; CC-4's core is 2025 journal art PA-N19/N20); most specific
  unclaimed feature found = grounded graphite GDC shield over the
  encapsulated in-vessel sensor (absence observation only); no
  Stanford/Senesky GaN-Hall patent found in bounded searches.
  (3) 05_DISCLOSURE_HOLD_CHECKLIST.md — preservation list, advisor/OTL/
  counsel questions (incl. AI-assisted-contribution flag for CC-4/CC-6,
  DOE DE-AC02-76SF00515/SLAC FWP 101264 + NSF ECCS-2026822 + TomKat
  sponsor questions, UW/WARF collaboration questions), disclosure gates
  G-A..G-H with arXiv (G-C) as the advisor's hard gate, sequence +
  decision owners with no external contact made, official Stanford/
  USPTO/WIPO links dated 2026-07-25 with change warning. Deterministic
  validation PASS (state/tools/50_validate.py: header, 35 unique IDs,
  13 cols, S-ID/DOI cross-refs, relative links, PA-ID resolution,
  labels, link domains).
- Stage 50 adds to the open-gate register: advisor/OTL/counsel
  conversations are the human unblocks before any disclosure event;
  G-A (July UW email) is the earliest third-party disclosure and needs
  an advisor confidentiality decision; G-C (arXiv) stays closed until
  advisor + OTL sign-off; inventory of any already-given talks/demos is
  NOT ESTABLISHED FROM SUPPLIED FILES; I-4 (deployed-module custody)
  now doubles as an evidence-preservation item.
- Previous stage: `40_experiment` (`COMPLETE`, attempt 1, cycle 0,
  session f2b49370-0ee2-4fda-b3aa-dcad1e3fe27c, run_2026-07-24_231243_734;
  requested Fable 5 / Extra High; final result produced by the Fable
  main session, no auxiliary subagents used; see
  `state/checkpoints/CP_40_experiment_20260725-073000.md`)
- Stage 40 result summary: (1) 04_MEASUREMENT_REQUIREMENTS.csv — 34
  rows, exact 14-column header, groups A (6 supplied-data analyses),
  B (6 chain verification/bandwidth/noise/parasitics), C (8
  calibration/characterization), D (3 repeatability), E (3 reference
  strategy), F (7 campaign), G-01 (retroactive 2025 conversion); every
  row carries min/preferred design, hardware gate, justified
  replicates, acceptance metric, uncertainty component, dependency,
  priority, fallback. (2) 04_HSX_EXPERIMENT_PLAN.md — inventory gates
  I-1..I-9 (nothing assumed in-hand; the 02 plan's testbench is a
  shopping list, not an inventory), UW gates U-1..U-9 (one
  advisor-authorized July email), go/no-go ladder G0/G1/G-cal/G-die/G2;
  anomaly-first rule (C017 gates all calibration); new load-bearing
  finding: the 2025 data was taken with the 2023 voltage-bias G=200
  chain, so retroactive tesla conversion needs a distinct
  voltage-bias-mode S_v calibration (C-03) of the deployed die —
  making I-4 (deployed-module location/health, never recorded in
  supplied files) the stage's most consequential new gate; WP-B >=3-die
  design with honest single-device fallback; bench-vs-HSX reference
  separation (no gaussmeter assumed available); Tier-1 SENSL package is
  fully campaign-independent (~19-28 bench/desk-days, zero cleanroom);
  Tier-2 RSI adds anchors/stability/1:1 comparison. (3)
  04_DATA_ANALYSIS_PLAN.md — provenance chain, metadata schemas,
  pipelines, conversion equations (changes-only for voltage-bias data,
  V_off honesty), 1:1 metrics with block-bootstrap CIs, shot-as-unit
  rules, leakage safeguards, 16-artifact figure-to-claim map,
  reproducibility/release structure. (4)
  04_UNCERTAINTY_AND_STATISTICS_PLAN.md — worked symbolic budget
  (placeholder set gives u(m)/m ~2.1%, coil constant 92% of variance),
  unit hierarchy with unit-and-n reporting rule, replication logic from
  1/sqrt(2(n-1)) and detectable-effect formulas (no invented sample
  sizes; A-02 supplies the power-analysis input from the archive),
  sensitivity analysis, six pre-drafted limitations statements.
  Deterministic validation PASS (state/tools/40_validate.py: header,
  34 unique IDs, 32 links, 25 S-ID/DOI citations, 252 requirement
  cross-refs all resolve).
- Stage 40 adds to the open-gate register: inventory gates I-1..I-9
  (I-4 deployed-module whereabouts is new and blocks the AE-01/AE-05
  answer via C-03/G-01; I-6 2023-chain existence decides
  measured-vs-derived bandwidth basis); UW gates U-1..U-9 consolidated
  into the advisor-decision-4 email (U-1 = R1-02's fork:
  analysis-now vs campaign); the ~185x bench-to-machine field
  extrapolation (E-03) is a named systematic that F-01 or a borrowed
  electromagnet session (I-9) must close, else it is a stated
  limitation in every HSX-scale tesla claim.
- Previous stage: `30_manuscript` (`COMPLETE`, attempt 1, cycle 0, session
  889c02e6-ed56-43a3-85a2-f61b7ce65e88, run_2026-07-24_231243_734;
  requested Fable 5 / Extra High; final result produced by the Fable main
  session, no auxiliary subagents used; see
  `state/checkpoints/CP_30_manuscript_20260725-060000.md`)
- Stage 30 result summary: (1) 03_REVIEWER_RESPONSE_MATRIX.csv — 16 rows
  (AE 8 / R1 5 / R2 3), exact 13-column header, all ten prompt-named
  concern areas covered; P0 set = calibration/absolute-output (AE-01/04/05,
  R1-01), repeatability (AE-03, R2-02), comparison table (AE-02), novelty
  reframing (R2-01). (2) 03_MANUSCRIPT_DIAGNOSIS.md — claim-by-claim audit
  from regular_lsens.tex (line-referenced): supported-now vs
  requires-qualification (QHS wording to S0128; 68-shot count; 'cannot be
  deployed' overclaim; voltage-domain 'tracking' wording; conclusion's
  neutron-facility future-work sentence conflicts with the no-radiation
  scope rule) vs requires-new-data (tesla output, multi-die stats,
  bandwidth basis, 1:1 probe comparison); WP-A table dimensions (12) and
  candidate rows; six supplied-data-recoverable analyses (shot recount,
  operational-repeatability stats, correlation quantification,
  bias-scaling check, noise floor, figure re-plots) vs seven
  nonexistent-data items. (3) 03_PUBLICATION_ROUTE_DECISION.md — decision
  derived from the letter (conflict C2 honored): primary = A→C (revise
  SENSL after bench package closes, then RSI vector-probe study = stage
  20's P1→P3), optional IP-screened arXiv of the *revised* version at
  resubmission; fallback = modified user route D (IP-screened arXiv of a
  strengthened-uncalibrated version + RSI) with explicit triggers; the
  literal user route (rejected version to arXiv) not recommended, reasons
  documented. Official policies verified 2026-07-25: SENSL 4-page +
  4.8-week median; IEEE preprint policy (verbatim PDF); AIP preprint/
  embargo; RSI previously-published refusal (search-extraction confidence,
  source 403-blocked); arXiv permanence/irrevocable license.
  Deterministic validation PASS (`state/tools/30_validate.py`: header,
  16 unique rows, coverage, 31+8 S-IDs resolve with DOI-link match,
  relative links resolve).
- Stage 30 adds to the open-gate register: SENSL invitation has no stated
  deadline (letter-lapse question = costless editorial query for the
  user); RSI duplicate-publication wording needs one direct re-verification
  before stage-80 reliance; matrix P0 rows are stage 40's work-order
  (anomaly closure → WP-C, die supply → WP-B, bench bandwidth sweep, UW
  co-located B-dot request); pre-disclosure IP screen (stage 50) is the
  hard gate before any arXiv action.
- Earlier stage: `20_direction` (`COMPLETE`, attempt 1, cycle 0, session
  c2ec39df-6fd3-4476-be64-f0d680765702, run_2026-07-24_231243_734)
- Requested model / effort (stage 20, complete): Fable 5 / Extra High
  (final result produced by the Fable main session; no auxiliary subagents
  used in this stage; see
  `state/checkpoints/CP_20_direction_20260725-044500.md`)
- Requested model / effort (stage 10d, complete): Fable 5 / Extra High
  (final result produced by the Fable main session; auxiliary lane work
  re-read, sampled, and corrected before acceptance)
- Requested model / effort (stage 10c, complete): Sonnet 5 / Extra High
- Requested model / effort (stage 10b, complete): Sonnet 5 / Extra High
- Requested model / effort (stage 10a, complete): Sonnet 5 / Extra High
- Requested model / effort (stage 00, complete): Sonnet 5 / High
- Active completion markers: `00_inventory`, `10a_literature_gan`,
  `10b_literature_fusion`, `10c_literature_methods`,
  `10d_literature_merge`, `20_direction`, `30_manuscript`, and
  `40_experiment` deliverables validated in-session (stage 40:
  `state/checkpoints/CP_40_experiment_20260725-073000.md`; stage 30:
  `state/checkpoints/CP_30_manuscript_20260725-060000.md`; earlier stages:
  `state/checkpoints/CP_00_inventory_20260724-232500.md`,
  `state/checkpoints/CP_10a_literature_gan_20260724-235500.md`,
  `state/checkpoints/CP_10b_literature_fusion_20260725-013000.md`,
  `state/checkpoints/CP_10c_literature_methods_20260725-021500.md`,
  `state/checkpoints/CP_10d_literature_merge_20260725-031500.md`, and
  `state/checkpoints/CP_20_direction_20260725-044500.md`)
- Active resumable sessions: session 8a61fcb5-1295-4361-851a-a73099b02968,
  run_2026-07-24_231243_734, cycle_0_attempt_1
- Model policy: `fable_final_result_only`
- Fable requirement: Fable 5 must perform the final review, validation, and
  accepted result for all seven Fable-assigned critical stages. Stages 10a,
  10b, and 10c are Sonnet-assigned; no Fable-downgrade enforcement applies
  to any of them.
- Temporary and auxiliary models: allowed and logged.
- Usage check: manual; the runner does not poll usage.
- Inactivity timeout: disabled; the user may stop PowerShell manually.
- Pre-restart archive: `_history\r0` (audit-only; not active progress)
- Next operation: none — `80_synthesis` was the final stage and is
  complete. The launcher's normal post-completion steps (result-model
  verification, `state/markers/80_synthesis.done.json`) close the run.
  Next human act: Tim reads `outputs/FINAL_EXECUTIVE_STRATEGY.md` and
  `outputs/FINAL_ACTION_PLAN.md` and schedules the advisor meeting
  (72-hour item 1 of the action plan).
- Stage 20 result summary: direction verdict CONTINUE-with-substantial-
  adjustment (ADJUST, adopt OPT2 — finished absolutely-calibrated sensing
  output as non-negotiable centerpiece plus campaign-uncoupled novelty
  layer WP-A comparison table / WP-B multi-die repeatability / WP-C
  calibration + GUM uncertainty / WP-D hybrid Hall+inductive drift
  fusion). Baseline weighted scores (1-5 beneficial-direction scale,
  9 criteria, weights sum 1.00): OPT2 4.29 adopt; OPT1 3.45
  fold_into_OPT2; OPT3 3.34 hold_as_fallback; OPT4 2.58 reject. OPT2 #1
  robust to ±1-point score uncertainty (margin 0.84 vs ±0.50) and to two
  adversarial re-weightings; OPT1-vs-OPT3 ordering is a stated tie.
  Falsifiability register (5 reversal conditions) and stop/pivot gates
  G1-G5 with campaign-slip fallbacks defined. Deterministic validation
  PASS (`state/tools/20_validate.py`): exact CSV header, weighted scores
  recomputed, 53 cited sources all resolve to the ledger with matching
  DOIs, all relative links resolve.
- Stage 20 adds to the open-gate register: advisor decisions 1-7 (report
  §10) are the exact human unblocks — notably novelty re-centering
  approval, WP-D thesis-scope approval, gen-2 die status/count (also a
  stage-40 prerequisite), and the July UW email including co-located
  B-dot data access + HSX archive sizing (prices the OPT3 fallback);
  venue route deliberately NOT decided (stage 30); direction verdict is
  falsifiable per report §11 — stages 70/80 should re-check the named
  reversal conditions.
- Stage 10D result summary: 233 lane rows merged to 231 unique verified
  peer-reviewed sources (two same-DOI pairs merged: A0068/B0041 -> S0068,
  A0070/B0054 -> S0070); 32 DOIs (~14%) re-verified by the Fable session
  via Crossref with 32/32 match; metadata corrections applied
  (Duran/Coisson author fixes, volume enrichments, venue normalization);
  deterministic validation PASS (unique IDs/DOIs/titles, exact header,
  231 >= 150 verified rows, no disallowed source types, material coverage
  59-133 rows per SOURCE_POLICY category); review cites 158 sources with
  programmatically checked links.
- Open gates carried into later stages: publication-status conflict (C1/C2),
  automatic-fallback deviations (C3/C4), project 02 "calibrated" language is
  aspirational (C6), project 04 reference registry needs re-verification
  before counting toward the 150-source minimum — see
  `outputs/00_CONFLICT_LEDGER.md` and `outputs/00_CLAIM_BASELINE.csv`. Stage
  10A adds: no peer-reviewed GaN/AlGaN Hall sensor deployed inside a
  stellarator/tokamak was found in this search (novelty anchor, but an
  absence-of-evidence finding); no GaN-specific calibration uncertainty
  budget or unified cross-material comparison table was found; 41% of
  Stage 10A's 70 rows are metadata-only (no independently read
  abstract/body) — see `evidence/10A_SYNTHESIS.md` sections 4 and 6. Stage
  10B independently corroborates the GaN-in-fusion absence finding (no GaN/
  AlGaN Hall sensor found in any fusion-context deployment across 14 direct-
  sensing precedent rows) and adds: the manuscript's "first quasi-helically
  symmetric stellarator" claim has peer-reviewed support but with a more
  precise wording ("first...stellarator experiment optimized for QHS,"
  Garcia et al. 2025) that stage 30_manuscript should match rather than
  paraphrase loosely; no HSX-specific Hall-sensor calibration/uncertainty/
  conventional-probe-comparison literature exists; row B0054 shares a DOI
  with Stage 10A's A0070 (flagged for stage 10d's merge, not an error); one
  off-topic peer-reviewed candidate (CERN accelerator metrology) was
  excluded rather than padding the count — see `evidence/10B_SYNTHESIS.md`
  sections 3, 4, and 6. Stage 10C adds: strong method-level precedent for
  physics-informed/ML plasma-equilibrium reconstruction exists (14 rows,
  several stellarator-class) but no evidence any such method has been
  demonstrated on HSX specifically, and no existing large HSX
  discharge-magnetics database at the scale used by the KSTAR/W7-X
  precedents this batch found — a data-prerequisite gap for stage
  40_experiment to size explicitly; no source quantifies the spatial/
  vector-coverage advantage a 2-3 axis HSX probe (project 03) would have
  over HSX's existing pickup-coil belts; 25 candidate rows independently
  found by 10C's lanes were excluded as cross-stage DOI duplicates of
  already-counted 10A/10B rows (full list in `evidence/10C_SYNTHESIS.md`
  section 6) rather than re-counted, a stricter proactive dedup than 10A/
  10B's single-incidental-overlap precedent, given the larger overlap
  scale (~25%); 84% of Stage 10C's 74 rows are abstract_metadata or
  metadata_only — see `evidence/10C_SYNTHESIS.md` sections 1, 3, 6, and 7.
- Stage 10D adds to the open-gate register: the merged ledger's novelty
  anchor remains an absence finding (bounded search, three independent
  lanes); stage 30 must align the facility-priority claim to S0128's
  exact wording; 75/231 ledger rows are metadata_only -- re-confirm any
  specific number from them against the primary source before manuscript
  use; no removal of any lane source was required (empty removal set).
- Updated: 2026-07-25T03:10:00-07:00 true local time (stage 80 complete;
  mission complete)
