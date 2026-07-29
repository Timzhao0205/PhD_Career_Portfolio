# Worklog

## Package preparation

- Created a new sibling mission so folder `06` remains intact.
- Encoded twelve model-routed stages, evidence gates, Fable retry/pause
  behavior, raw event logging, performance metrics, and durable resume.
- Seeded direct hybrid, radiation, application, and alternative searches.
- No research-stage output has yet been generated.

## 2026-07-27 — Stage 00 (`00_inventory`, Sonnet 5 / high, attempt 1)

- Read all mission policy/prompt files (`README_START.md`, `MISSION.md`,
  `SOURCE_POLICY.md`, `DECISION_FRAMEWORK.md`, `LITERATURE_SEEDS.md`,
  `AGENTS.md`, `CLAUDE.md`, `EXECUTION_PLAN.md`, `MODEL_POLICY.md`,
  `CHECKPOINT_PROTOCOL.md`, `PACKAGE_MANIFEST.md`, `RESUME_GUIDE.md`,
  `OFFICIAL_SETUP_REFERENCES.md`) and the runner's stage table/model-
  integrity logic in `RUN_HYBRID_RADIATION_ANALYSIS.ps1`.
- Inspected folder `06` read-only: all `outputs\*` files (00–07 series,
  `FINAL_*`), `06\CLAUDE.md`, `06\MISSION.md`,
  `06\inputs\ORIGINAL_REQUEST.txt`. Confirmed 231-row verified ledger,
  OPT2 ADJUST decision, and `FINAL STATUS: PASS` in `06\outputs\FINAL_
  AUDIT.md`.
- Inspected folder `07_HSX_august2025_results` at file/inventory level
  only (per-shot `.dat`/`.png`, MATLAB figure scripts, coil-current logs).
- Reconstructed the user's Hall-first/hybrid-second/module-third
  hypothesis against `06`'s actual text: verdict PARTLY CONFIRMED (Hall-
  first is a genuine hard gate; hybridization-second holds only as a
  paper-numbering label, not a strict serial dependency; the "reusable
  module and simulation package" third phase has no precedent in `06`).
- Identified and dispositioned 6 conflicts (C1–C6): Codex/MCP-fallback
  deviation (inherited from `06`), a root-`CLAUDE.md` documentation gap
  naming only `06`, a topic-taxonomy mismatch between `06` and this
  mission's quotas, a precedent-vs-derivation gap on hybrid-fusion
  identifiability, the sequencing-hypothesis gap, and a radiation-
  architecture-vs-no-experiment-scope note.
- Wrote all 3 required outputs (`00_INPUT_INVENTORY.md`,
  `00_REQUIREMENTS_TRACE.csv` [21 rows, CSV-parse-verified],
  `00_CONFLICT_LEDGER.md`); verified no sibling file was modified.
- Next action: run/resume the launcher into `10a_literature_hybrid`
  (Sonnet 5 / xhigh).

## 2026-07-27 — Stage 10A (`10a_literature_hybrid`, Sonnet 5 / xhigh, attempt 1)

- Read `README_START.md`, `MISSION.md`, `SOURCE_POLICY.md`,
  `DECISION_FRAMEWORK.md`, `LITERATURE_SEEDS.md`, `AGENTS.md`, `CLAUDE.md`,
  `CHECKPOINT_PROTOCOL.md`, and the stage 10A prompt. Re-inspected `06`'s
  full 232-row `01_SOURCE_LEDGER.csv` and pulled all hybrid/Kalman/
  integrator/Mirnov/Rogowski/observer/drift-tagged rows as a dedup baseline.
- Ran 7 parallel research subagents (general-purpose, web search + Crossref/
  PMC verification), one per search domain from the stage prompt: (A) direct
  seed verification + citation network, (B) observer/Kalman/Luenberger/
  unknown-input theory, (C) coil/integrator drift beyond `06`'s coverage,
  (D) calibration/self-test/spinning-current/embedded-actuator literature,
  (E) Rogowski/bandwidth/cross-axis/saturation/fault-detection, (F) non-fusion
  Hall+coil hybrid applications (power electronics, accelerator magnets,
  rotating machinery, space physics), (G) Hall absolute-reference literature.
- Compiled 73 raw candidates, removed 7 exact within-set duplicates (66
  unique DOIs), programmatically cross-checked all 66 against `06`'s ledger
  (15 exact-DOI overlaps found and individually flagged, not hidden; 51
  genuinely new). Resolved two `LITERATURE_SEEDS.md` errors during
  verification: (1) DOI `10.3390/s19245455`'s actual title is "...by
  Feed-Forward Correction" with an NMR reference, not "...by Extended Kalman
  Filtering" as the seed claimed — `06`'s ledger already had the correct
  title, seed doc was wrong; (2) confirmed the 2007 Bolshakova "self-
  diagnostic" DOI (`10.1166/sl.2007.004`) is legitimate but downgraded its
  peer-review status to `peer_review_uncertain` after venue-quality concerns
  surfaced and full text remained unreachable across 3 independent attempts;
  identified the stronger, unambiguously peer-reviewed IEEE TNS 2012 paper
  (same author group) as the better citation for the same claim. Caught and
  discarded one hallucinated DOI from an initial subagent search pass (did
  not enter the ledger).
- Wrote `evidence\10A_HYBRID_SOURCES.csv` (66 rows; 65
  verified_peer_reviewed, 1 peer_review_uncertain; 0 duplicate DOIs/
  source_ids/normalized titles; parse-verified via PowerShell Import-Csv)
  and `evidence\10A_HYBRID_SYNTHESIS.md` (search strategy, 15-row direct-
  prior-art timeline, measured/estimated-state table, performance/
  validation-type table, 5 unresolved identifiability questions, novelty/
  sequencing implications, 8 material limitations).
- Central technical finding: no verified source proves joint identifiability
  of field + Hall gain + Hall bias + coil gain + coil bias from a Hall+coil
  pair; the strongest identifiability proof found (H021, Zhou et al. 2016)
  explicitly excludes an unknown sensor-gain term. The closest fusion-
  specific Kalman-fusion prior art (H001/H002, 2025) is simulation-only or
  validation-unconfirmed, while the strongest hardware-validated drift
  correction (H004/H005) is non-fusion and does not address Hall gain.
- Verified no sibling file (`06`, `07_HSX_august2025_results`, root `01`
  files, this mission's own runner/policy files) was modified; deleted one
  scratch dedup-input text file created and no longer needed in `tools\`.
- Next action: run/resume the launcher into `10b_literature_radiation`.

## 2026-07-27 — Stage 10B (`10b_literature_radiation`, Sonnet 5 / xhigh, attempt 1)

- Read `README_START.md`, `MISSION.md`, `SOURCE_POLICY.md`,
  `DECISION_FRAMEWORK.md`, `LITERATURE_SEEDS.md`, `AGENTS.md`, `CLAUDE.md`,
  `CHECKPOINT_PROTOCOL.md`, and the stage 10B prompt. Confirmed via the
  live `state\attempts\10b_literature_radiation.json` and
  `logs\run_2026-07-27_005332_821\10b_literature_radiation\...\stream.jsonl`
  that no prior partial attempt existed to resume — this session's own
  Bash calls were what populated that stream file; started fresh.
- Pulled the 30 radiation/irradiation/neutron/gamma/proton/fluence/dose/TID
  -matching rows from `..\06\outputs\01_SOURCE_LEDGER.csv` (232 rows total)
  via a Python CSV parse, to use as a dedup/exclusion baseline for every
  research subagent (matching stage 10A's method of pulling a topic-matched
  baseline before searching).
- Ran 8 parallel general-purpose research subagents (web search + Crossref/
  PubMed/publisher-metadata verification), one per required evidence layer:
  (A) direct Hall-device neutron irradiation, (B) direct Hall-device
  gamma/TID irradiation, (C) direct Hall-device proton/electron/heavy-ion
  irradiation, (D) GaN/AlGaN/AlN enabling device/material physics, (E)
  Si/SOI/GaAs/InSb/InAs enabling device/material physics, (F) measurement-
  chain electronics (bias/AFE/ADC/cabling/packaging), (G) coil/insulation/
  integrator/fiber-optic radiation and temperature effects, (H) fusion
  diagnostic qualification/calibration/dosimetry practice. One subagent
  (domain B, gamma/TID) diverted its final message into an unprompted
  question about logging to a `NOTES.md` file it correctly determined does
  not exist in this project, instead of returning its verified source list;
  recovered its actual findings via `SendMessage` resuming the same agent
  and explicitly redirecting it back to the required output format —
  its research work was not lost, only its first reply was malformed.
- Compiled 8 domains' raw candidates (~90 blocks) into a single ledger,
  merging 5 same-DOI pairs independently found by two agents each
  (Jankowski TNS 2019 by both A and E; Sanders REDW 2008 and Adamiec TNS
  2016 by both B and C; Fan Sensors 2020 by both B [as a required
  LITERATURE_SEEDS.md seed-correction] and E; Gusarov Sensors 2025 by both
  G and H) into single dual-tagged rows rather than duplicate rows, per
  `SOURCE_POLICY.md`'s DOI-dedup rule. Cross-checked the merged set against
  both `..\06\outputs\01_SOURCE_LEDGER.csv` and this mission's own
  `evidence\10A_HYBRID_SOURCES.csv` by normalized DOI; found and
  individually flagged (not hid) 2 further duplicates against each (R005/
  R077 vs 10A H007/H031; R066/R069 vs 06 S0082/S0151).
  Corrected one `LITERATURE_SEEDS.md` seed error during verification:
  the PMC7412317 URL given as "Effects of ionizing radiation on Hall
  sensors based on fully depleted silicon-on-insulator technology" does not
  match any real paper with that title — the paper actually at that URL is
  Fan, Bi, Xi & Yan, Sensors 20(14) (2020) 3946, "...by TCAD Simulations,"
  confirmed simulation-only, not an experimental gamma/TID measurement;
  documented as a correction rather than silently substituted (R044).
- Wrote `evidence\10B_RADIATION_SOURCES.csv` (79 rows; 76
  verified_peer_reviewed, 3 peer_review_uncertain; 0 duplicate DOIs/
  source_ids/normalized titles; parse-verified via Python csv module) via a
  one-off compilation script (`tools\build_10b_ledger.py`, deleted after
  use once the CSV was verified) and `evidence\10B_RADIATION_SYNTHESIS.md`
  (mechanism primer, material x species matrix, enabling-physics deep dive,
  measurement-chain failure pathways, fusion qualification practice, a
  modelable/monitorable/calibratable/only-boundable framework tied to
  `DECISION_FRAMEWORK.md`'s state model, 7 evidence gaps, 3 retained
  contradictions, acceptance-gate status).
- Central technical finding: no bare GaN/AlGaN Hall-plate device has been
  irradiated and reported under any neutron spectrum in the peer-reviewed
  literature — all GaN neutron evidence is HEMT/2DEG-structure or bulk-AlN
  enabling physics, not a fabricated Hall sensor. The strongest real-fusion-
  neutron (14 MeV D-T, in-machine) radiation-effects dataset in the entire
  ledger belongs to a fiber-optic current sensor (FOCS), not a Hall device.
  A proton-to-gamma NIEL-scaling extrapolation for InAs/InAsSb was shown to
  under-predict gamma damage by ~14x (R042) — a concrete counter-example
  against cross-species extrapolation that any compensation-strategy stage
  must respect.
- Verified no sibling file (`06`, `07_HSX_august2025_results`, root `01`
  files, this mission's own runner/policy files, the 10A lane outputs) was
  modified; deleted the one scratch compilation script created in `tools\`,
  matching stage 10A's precedent for non-reusable scratch files.
- Next action: run/resume the launcher into `10c_literature_applications`.

## 2026-07-27 — Stage 10C (`10c_literature_applications`, Sonnet 5 / high, attempt 1)

- Read `README_START.md`, `MISSION.md`, `SOURCE_POLICY.md`,
  `DECISION_FRAMEWORK.md`, `LITERATURE_SEEDS.md`, `AGENTS.md`, `CLAUDE.md`,
  `CHECKPOINT_PROTOCOL.md`, and the stage 10C prompt. Confirmed via
  `state\attempts\10c_literature_applications.json` (status
  `CLAUDE_IN_PROGRESS`, no session ID recorded) and an absent checkpoint that
  no prior partial attempt existed to resume — started fresh, matching the
  10A/10B pattern.
- Pulled a combined dedup baseline (357 normalized DOIs from `06`'s 231-row
  ledger plus this mission's own 10A 66-row and 10B 79-row ledgers) and a
  68-row application/alternative-tagged context excerpt from `06`, written to
  scratch files in `tools\` for reuse by every research subagent.
- Ran 8 parallel general-purpose research subagents (web search + Crossref
  verification), one per required evidence layer: (A) long-pulse tokamak
  equilibrium/control diagnostics, (B) stellarator field mapping/error-field
  verification, (C) z-pinch/pulsed-power current/field measurement, (D)
  plasma-jet/magneto-inertial fusion diagnostics, (E) superconducting/HTS
  magnets/trapped-field rotors/motors-generators, (F) accelerator magnets/
  high-field metrology, (G) alternative sensor technologies (fluxgate,
  AMR/GMR/TMR/planar Hall, fiber-optic/Faraday, NMR, SQUID, NV/quantum,
  standalone baseline), (H) current official group/facility landscape
  discovery (documentation only, no outreach).
- Compiled 77 raw candidate rows from the 8 domains, found 0 internal
  exact-DOI collisions, then independently re-verified all 77 DOIs against
  the live Crossref API (not just accepted from subagent-reported metadata)
  with a title-match check — all 77 resolved and matched. One row (Morisaki
  et al., "Flux Surface Mapping in LHD," `10.13182/fst10-a10832`) was caught
  during this verification pass as a genuine duplicate of `06`'s S0130 — the
  domain-B subagent had mistaken it for a distinct companion sequential-DOI
  paper — and was removed, leaving 76 final rows with 0 overlap against the
  combined `06`/10A/10B baseline.
- Wrote `evidence\10C_APPLICATION_SOURCES.csv` (76 rows; 75
  verified_peer_reviewed, 1 peer_review_uncertain [P063, TMR radiation paper,
  author list unconfirmed]; 0 duplicate DOIs/source_ids/normalized titles;
  parse-verified via Python csv module) and
  `evidence\10C_APPLICATION_SYNTHESIS.md` (application requirement matrix
  across 6 lanes, incumbent-diagnostic/limitation matrix with an explicit
  per-lane Hall+coil-hybrid-literature-found assessment, 7-family
  alternative-technology map, 9-group official-page-sourced current-landscape
  table, promising/poor-fit case list, 6 explicitly labeled unresolved gaps,
  acceptance-gate status).
- Central technical finding: ITER's outer-vessel steady-state sensor (OVSS)
  system (P003) is the strongest real-machine precedent found anywhere in
  this mission for the DC-Hall-corrects-coil-drift half of the proposed
  hybrid, but it is a system-level pairing of separate sensor heads, not a
  co-located single-package hybrid, and no source demonstrates the reverse
  direction (coil identifying Hall drift) as tested on any tokamak.
  Persistent-mode superconducting/HTS magnets are the clearest documented
  poor-fit case (a coil cannot sense a static trapped field; NMR is the
  field's accepted reference instead, P042). Accelerator magnets already
  combine Hall+coil(+NMR) mapping as mature, decades-old production practice
  (P052/P057/P058) — a genuine novelty risk for later stages to address
  directly.
- Verified no sibling file (`06`, `07_HSX_august2025_results`, root `01`
  files, this mission's own runner/policy files, the 10A/10B lane outputs)
  was modified; deleted all 4 scratch files created in `tools\` during
  compilation and verification, matching stage 10A/10B precedent for
  non-reusable scratch files.
- Next action: run/resume the launcher into `10d_evidence_merge` (Fable 5,
  xhigh).

## 2026-07-27 — Stage 10D (`10d_evidence_merge`, Fable 5 / xhigh, attempt 1)

- Read all mission policy files, the 10D prompt, `state\PROJECT_STATE.md`,
  `state\WORKLOG.md`, and `state\attempts\10d_evidence_merge.json` (status
  `CLAUDE_IN_PROGRESS`, no session ID, no checkpoint) — confirmed fresh
  start, matching the 10B/10C pattern. Read all three lane CSVs in full
  (66+79+76 rows) and all three lane syntheses; loaded `..\06`'s 231-row
  ledger as the dedup baseline.
- Merged the three lanes by normalized DOI/title: exactly 2 cross-lane DOI
  collisions found and merged (R005→H007, R077→H031 — the two the lanes had
  pre-flagged; no additional collisions and 0 title-only collisions
  surfaced); 17 folder-06 overlaps confirmed programmatically (15 from 10A,
  R066/R069 from 10B — identical to lane self-reports).
- Independent Fable verification (not lane-trust): re-queried ALL 219 final
  DOIs against the live Crossref API — 214 exact title/year matches, 5 old
  IEEE proceedings records with no Crossref year field but exact
  title/author matches (noted per-row); re-confirmed all 6 PMC IDs behind
  `full_text` access claims via NCBI eutils; attempted Semantic Scholar
  content retrieval for 5 rows whose content claims were flagged unverified
  — retrieved and read H059's abstract, CONFIRMING its previously
  snippet-only central claim (cryogenic Hall sensors cross-calibrated in
  situ by induction coils), the only confirmed coil-calibrates-Hall
  instance in the evidence base (non-fusion, driven-ramp excitation).
  Verification artifacts retained in `tools\`.
- Corrections applied and documented in-row: P063 upgraded
  peer_review_uncertain→verified (Crossref resolved its 15-author list, the
  sole blocker); P008 first author corrected (lane had "Y. Chen"; Crossref
  gives D. L. Chen — author-metadata error, right paper); P011 author list
  resolved; R011 tier A→B (digital Hall switch IC, one step removed from
  metrological linear Hall sensing); H059 kept A with confirmation note.
- Wrote all 7 outputs: `01_SOURCE_LEDGER.csv` (219 rows, 215 verified ≥120;
  quota tags embedded; 0 dup IDs/DOIs/titles), `01_NEW_SOURCE_AUDIT.csv`
  (219 rows, 198 verified-new ≥75), `01_EVIDENCE_MAP.csv` (37 typed claims
  C01–C37, referential integrity checked), `01_SOURCE_COVERAGE.md`,
  `01_HYBRID_LITERATURE_REVIEW.md`, `01_RADIATION_LITERATURE_REVIEW.md`,
  `01_APPLICATIONS_ALTERNATIVES_REVIEW.md`. Quotas (verified): hybrid/coil
  70, radiation 79, applications 76, calibration/observability 50 — all
  ≥2× their gates with zero relabeling (quota mapping deterministic from
  lane tags). Validator `tools\validate_10d_outputs.py`: 21/21 PASS.
- Both required review statements are explicit: existing Hall+coil drift
  correction corrects the coil chain from an absolute reference and does
  NOT prove in-situ Hall radiation-sensitivity calibration (hybrid review
  §4, radiation review §6, claim C06 with H059 as direction-only
  counterevidence).
- Kept reusable tools (validator + Crossref-verification script/evidence);
  deleted the 3 non-reusable build scripts after validation, per lane
  precedent. No sibling file modified.
- Next action: run/resume the launcher into `20_observability`.

## 2026-07-27 — Stage 20 (`20_observability`, Fable 5 / xhigh, attempt 1)

- Read all mission policy files, the stage-20 prompt (verified the
  generated effective prompt contains the stage prompt verbatim),
  `state\PROJECT_STATE.md`, `state\WORKLOG.md`, and
  `state\attempts\20_observability.json` (status `CLAUDE_IN_PROGRESS`, no
  session ID, no prior `02_*` outputs) — confirmed fresh start. Loaded the
  10D evidence base (219-row ledger, 37-claim evidence map, 10A/10B
  syntheses) and confirmed folder `06` has no stage-20-equivalent
  observability output (its `02_*` files are direction scorecards).
- Derived the stage's core structural result from the required measurement
  model: the unreferenced Hall+coil pair carries an exact two-parameter
  gauge group — (B,S_H,K_C)→(αB+β, S_H/α, K_C/α) with b_H absorbing βS_H/α
  — valid for EVERY waveform, so absolute scale, both absolute gains, and
  Hall offset are never identifiable from the pair alone; common-mode gain
  drift is observationally identical to a field change (the formal content
  of MISSION.md's redundancy warning, and the required non-identifiable
  counterexample). Identifiable invariants: gain ratio S_H/K_C
  (differential-drift alarm without attribution), conditionally b_C, field
  shape up to the affine orbit.
- Built `tools\observability_rank_tests.py`: deterministic complex-step
  Fisher-information rank tests (finite known field basis = best-case,
  a-fortiori argument stated; N=1500, tol 1e-9; no RNG). 16 runs, all
  matching the analytic predictions: CASE A 5/7 with both analytic null
  vectors matched to ~1e-15 and S_H/K_C verified identifiable while S_H
  alone is not; B 4/5 (coil-trusted: S_H identifiable, offset null
  survives); C1 6/8 vs C2 8/8 (zero-field anchors close the LF trio);
  D 4/4 vs D-flat 2/4; E 6/7 vs E-collide 5/7 (injection must be
  spectrally orthogonal to ambient content); F 2/5 (quasi-static: nothing);
  G 7/9 (material-diverse redundancy: S1/S2 identifiable, scale/DC nulls
  survive); H-broad vs H-narrow (Hall-pole singular value 1.2e-1 → 1.4e-2,
  ~ω/a scaling — one honest mid-work correction: the first "narrowband"
  variant still contained a 7 Hz basis component exciting the pole, muting
  the collapse; fixed so both components sit a decade below the pole);
  I 4/4 vs I-ramp 3/4 (coil gain vs integrator drift confound g·r+m under
  constant dB/dt — separation requires dB/dt variation); J-corr 1/2 vs
  J-decorr 2/2 (temperature-vs-dose collinearity and its cure). Raw output
  retained as `tools\observability_rank_tests_output.txt`.
- Wrote all 3 required outputs: `02_OBSERVABILITY_AND_IDENTIFIABILITY.md`
  (model with all seven stage-required definitions, Theorem 1, all 9
  required cases each with algebra + rank cross-reference and per-case
  verdicts, all 6 required confounding tests, numerical protocol,
  assumptions register, source summary), `02_MUTUAL_CALIBRATION_
  FEASIBILITY.md` (direction-dependent plain-language verdict, 13×6
  F/C/N matrix, minimum reference/excitation requirements, radiation
  implications, honest scope), `02_ESTIMATOR_REQUIREMENTS.csv` (15 rows =
  9 cases + 6 confounding tests, exact stage header, csv-module-generated).
- Acceptance self-check: every case has an explicit
  observability/identifiability argument (no "complementary bandwidth"
  reasoning anywhere; crossover prior art H045/H066 cited as signal
  combination, explicitly not proof); multiple non-identifiable
  counterexamples (Theorem 1/CASE A, F, E-collide, I-ramp, J-corr,
  D-flat); Hall gain vs Hall offset distinguished (gain conditionally
  coil-derivable, offset never — needs zero-field/absolute anchor); coil
  gain vs integrator drift distinguished (CASE I-ramp condition);
  literature not overextended to radiation calibration (C06/C14 restated
  in both outputs; H059 kept non-fusion/abstract-level; R071 flagged
  single-source); numerical work labeled synthetic-structural, never
  experimental validation.
- Validation pass: CSV parsed (15 rows, header exact); all evidence_ids in
  the CSV and all 49+11 bracketed source IDs plus every cited claim ID in
  the two MDs verified present in `01_SOURCE_LEDGER.csv` /
  `01_EVIDENCE_MAP.csv`; zero invented IDs. Kept both tools scripts as
  reusable (rank tests will be re-run by stages 30/60; CSV builder avoids
  hand-edit quoting errors); no scratch files left. No sibling file
  modified.
- Checkpoint: `state\checkpoints\CP_20_observability_20260727-031849.md`.
- Next action: run/resume the launcher into `30_radiation_compensation`.

## 2026-07-27 — Stage 30 (`30_radiation_compensation`, Fable 5 / xhigh, attempt 1)

- Read all mission policy files, the stage-30 prompt (verified the
  generated effective prompt contains the shared contract + stage prompt;
  only the heading em-dash differs by encoding), `state\PROJECT_STATE.md`,
  `state\WORKLOG.md`, and `state\attempts\30_radiation_compensation.json`
  (status `CLAUDE_IN_PROGRESS`, no session ID, no `03_*` outputs) —
  confirmed fresh start, matching the 10B/10C/10D/20 pattern. Loaded the
  stage-20 verdicts in full (both MDs + 15-row estimator CSV), the
  37-claim evidence map, both literature reviews, and stage 00's conflict
  ledger (C6 supplies the binding radiation-vs-HSX-scope discipline).
  Confirmed folder `06` outputs are strategy/publication documents with
  no compensation-architecture equivalent (no conflict to record beyond
  stage 00's C4/C6 dispositions).
- Wrote `outputs\03_RADIATION_COMPENSATION_ARCHITECTURE.md`: compared
  required options A–G plus an added layered option H (composition of
  anchored + self-test + diversity layers), each option's verdict tied
  to a specific stage-20 CASE (no claim exceeds the feasibility matrix).
  Recommended MVD = "anchored hybrid" (pair + vacuum-shot machine-model
  anchor per CASE D + zero-field offset epochs per CASE C2 + bench
  absolute traceability) and higher-accuracy = "triangulated self-test
  hybrid" (+ embedded winding with spectrally-orthogonal/toggled
  injection and dual lock-in per CASE E, + repeated-waveform ratios per
  CASE 6, + material-diverse witness per CASE G at top tier only).
  Embedded-winding analysis answers the stage question directly: the
  winding isolates gain ONLY as products S_H·G_cal / K_C·G_cal under
  spectral orthogonality (CASE E-collide counterexample enforced as a
  design requirement), can never deliver Hall offset (Theorem-1 β-null;
  DC toggling measures gain at the DC point, not offset), carries a
  heating self-interference ceiling (derived inequality
  |α_S|·R_th·R_cal·I_rms² ≪ δ_S), and is itself referenced by
  anchor-epoch triangulation (G_cal solved at each CASE-D epoch) plus a
  derived triangle-closure test π_H/π_C ≡ ρ_HC that validates the
  instrumentation paths while providing zero drift attribution
  (explicitly no free lunch vs Theorem 1). Four compensation modes
  (online / scheduled / fault detection / post-exposure) each mapped to
  their identifiability basis; in-situ vs ex-situ mechanism table
  (16 mechanisms); uncertainty budget in 6 terms with the between-anchor
  common-mode blindness carried as an honest growth term; budget tiers
  T0–T3 (≥3 required) with entry/exit gates G0–G5 and per-tier stop
  rules; §9.4 binding statement that rungs 5–7 are collaborator-led and
  NOT a prerequisite for any HSX first-author deliverable.
- Wrote `outputs\03_SIMULATION_AND_VALIDATION_PLAN.md`: complete truth-
  model equations (field, injection, integrator, per-parameter drift
  decompositions, annealing hysteresis state, RIEMF term, R_H witness
  output, foil-read fluence output); placeholder policy making the C14
  gap structural (per-curve `basis` field, watermarking of placeholder
  outputs, species-vector config that programmatically refuses scalar
  fluence — C16/C17 discipline as code); 12 scenarios S1–S12 with
  pre-registered stage-20 expected behaviors (incl. S8 common-mode with
  pre-registered NO-alarm); 14 fault injections F1–F14; metrics M1–M8
  incl. the non-identifiability honesty test T-NI (estimator must not
  "converge" in proven-blind directions); regression suite binding the
  package's Jacobians to `tools\observability_rank_tests.py` rank-for-
  rank; 7-rung ladder with named generic standards (no invented vendors/
  facilities/prices), sample sizes where defensible (rung 2: ≥3 cal
  cycles; rung 5: ≥5 irradiated + ≥3 control per material, scaled
  against R003's 9-sample precedent, labeled Proposed), acceptance
  thresholds and bidirectional stop rules (drift-below-floor → simplify;
  drift-unattributable → falsified, pivot); module interface spec with
  the frozen-science boundary; explicit simulated/bench/radiation
  evidence-class table.
- Wrote `outputs\03_RADIATION_RISK_REGISTER.csv` via deterministic
  builder `tools\build_03_risk_register.py` (kept as reusable): 24 rows
  RR-01…RR-24 spanning die (displacement/transmutation/TID/offset
  floor), electronics (synergy, SETs, packaged ICs), coil chain (RIEMF,
  effective-area, insulation, integrator, timing), references (cal
  winding chain, machine-model, zero-field ambient, witness
  single-source), structural blindness (Theorem-1 common mode), and
  program-level traps (cross-species ~14×, mixed-field non-additivity,
  dosimetry flux gap, EMI collision, saturation); exact 15-column stage
  header; every evidence_ids entry resolves.
- Validation: `tools\validate_30_outputs.py` (kept as reusable) 13/13
  PASS — existence/nontriviality, exact CSV header, 24 rows, unique
  risk_ids, evidence_ids resolution, enum/gate vocab, and all 54+10
  bracketed source IDs plus 24+11 claim IDs in the two MDs resolve
  against `01_SOURCE_LEDGER.csv`/`01_EVIDENCE_MAP.csv`; zero invented
  IDs; simulation never described as validation anywhere; R050-class
  simulation-only sources not cited as experimental.
- Acceptance self-check: architecture consistent with stage 20 (every
  "covers" claim cites its CASE; estimator required to freeze in
  proven-blind regimes); accuracy claims all carry an
  uncertainty/reference basis (relative-to-anchor form only); 4 budget
  tiers ≥ required 3, with stop/go gates; radiation testing explicitly
  decoupled from the HSX first-author paper (ARCH §9.4 + plan §1, per
  conflict C6); simulation package interfaces/tests sufficient without
  inventing scientific content (plan §2–§11 frozen-science boundary).
- Verified no sibling file (`..\06`, `..\07_HSX_august2025_results`,
  root `01` files, this mission's runner/policy files, prior-stage
  outputs) was modified; no scratch files left in `tools\`.
- Checkpoint: `state\checkpoints\CP_30_radiation_compensation_20260727-033513.md`.
- Next action: run/resume the launcher into
  `40_applications_collaboration` (Sonnet 5 / xhigh).

## 2026-07-27 — Stage 40 (`40_applications_collaboration`, Sonnet 5 / xhigh, attempt 1)

- Read `README_START.md`, `MISSION.md`, `SOURCE_POLICY.md`,
  `DECISION_FRAMEWORK.md`, `CHECKPOINT_PROTOCOL.md`, `LITERATURE_SEEDS.md`,
  `AGENTS.md`, root and project `CLAUDE.md`, `MODEL_POLICY.md`, and the
  stage 40 prompt. Confirmed via `state\attempts\40_applications_collaboration.json`
  that this session is the live attempt (no prior partial work to resume);
  the generated effective prompt matched the stage-prompt file verbatim.
- Reused, without repeating, all stage 10C/10D application evidence
  (`outputs\01_APPLICATIONS_ALTERNATIVES_REVIEW.md`,
  `evidence\10C_APPLICATION_SYNTHESIS.md`, `01_EVIDENCE_MAP.csv` claims
  C27–C36) and the stage 20/30 vetoes (Theorem 1; CASE A/F; C28 SC/HTS
  structural blindness; C30 z-pinch no-advantage; C35 MIF probe
  abandonment; C29 accelerator-magnet novelty veto; stage-30 tiers
  T0–T3/gates G0–G5 and the binding §9.4 HSX-radiation decoupling).
- Ran 4 parallel general-purpose research subagents (read-only, discovery-
  only, explicitly no-outreach) to verify CURRENT official pages for
  candidate groups across all 6 application lanes: (1) tokamak/ITER —
  ITER ITPA Diagnostics Topical Group, IPP CAS Prague, KFE/KSTAR, CEA/WEST;
  (2) stellarator — W7-X MHD Research Unit (IPP Greifswald), PPPL; (3)
  z-pinch/MIF — Sandia Z/Mykonos, LANL P-24; (4) SC/HTS/accelerator —
  Cambridge Bulk Superconductivity Group, CERN TE-MSC Magnetic
  Measurements. All group official-page URLs independently fetched and
  confirmed live as of 2026-07-27 except two, honestly flagged rather than
  asserted: CERN's `te-msc-mm.web.cern.ch` micro-site (DNS resolution
  failure from this environment on repeated attempts, including a direct
  fetch I ran myself after the subagent's failure — search-engine-indexed
  as live, content unverified) and the canonical `www.pppl.gov` domain
  (site-wide HTTP 403 to automated fetch; mitigated with a live Google
  Sites NSTX-U mirror).
- Scored all 6 required applications (tokamak long-pulse, stellarator
  mapping, z-pinch/pulsed-power, MIF/plasma-jet, SC/HTS/motors-generators,
  plus accelerator magnets as the sixth evidence-supported application)
  against a documented 0–5 rubric (technical_score = mean of hybrid_value/
  identifiability_path/radiation_fit; strategic_score = mean of access/
  publication/collaboration_leverage/cost-inverted/dilution-inverted;
  rubric recorded in `04_COLLABORATION_STRATEGY.md` §2 since the required
  CSV header has no notes column). Applied hard vetoes per
  `DECISION_FRAMEWORK.md` (no score override) to z-pinch (C30), SC/HTS
  (C28), and accelerator magnets (C29 novelty); MIF received a partial
  veto (C35, core region only). Ranked: 1 stellarator (HSX, internal/
  approach-now), 2 tokamak (approach-after-bench-proof), 3 accelerator
  (monitor, technique-only), 4 SC/HTS (monitor, data-only), 5 MIF
  (do-not-prioritize), 6 z-pinch (do-not-prioritize).
- Wrote all 3 required outputs via deterministic builder scripts (kept as
  reusable, matching the stage-20/30 precedent):
  `outputs\04_APPLICATION_SCORECARD.csv` (6 rows, exact stage header, via
  `tools\build_04_application_scorecard.py`); `outputs\04_COLLABORATION_STRATEGY.md`
  (ranked recommendations, scoring rubric, per-application prerequisites
  and non-sent scientific-ask outlines, cross-cutting risks, fallback
  path, consistency statement); `outputs\04_COLLABORATOR_CANDIDATES.csv`
  (10 ranked candidates across all 6 lanes, via
  `tools\build_04_collaborator_candidates.py`) — every
  `proposed_scientific_ask` cell explicitly labeled "PROPOSED, NOT SENT."
- Validation: `tools\validate_40_outputs.py` (new, kept as reusable)
  21/21 PASS — existence/nontriviality; exact CSV headers; 6/10 row
  counts; unique application/group values; rank is a clean 1..N
  permutation in both CSVs; every do-not-prioritize row states a veto;
  all `evidence_ids`/`relevant_publication_ids` resolve against
  `01_SOURCE_LEDGER.csv`/`01_EVIDENCE_MAP.csv` (zero invented IDs); every
  candidate ask carries the PROPOSED-NOT-SENT label; zero email addresses
  or phone-shaped strings in any of the 3 outputs (no contact-detail
  leakage).
- Verified no sibling file (`..\06`, `..\07_HSX_august2025_results`, root
  `01` files, this mission's runner/policy files, prior-stage outputs) was
  modified; no outreach, contact, or external write occurred at any point
  (all subagent research was explicitly briefed read-only/discovery-only).
- Checkpoint: `state\checkpoints\CP_40_applications_collaboration_20260727.md`.
- Next action: run/resume the launcher into `50_limitations_comparison`
  (per `outputs\01_APPLICATIONS_ALTERNATIVES_REVIEW.md` §4 and
  `README_START.md` reading order; model/effort per `MODEL_POLICY.md`).

## 2026-07-27 — Stage 50 (`50_limitations_comparison`, Fable 5 / xhigh, attempt 1)

- Read the full required context before acting: shared contract, stage
  prompt, `MISSION.md`/`SOURCE_POLICY.md`/`DECISION_FRAMEWORK.md`/
  `CHECKPOINT_PROTOCOL.md`, `state\PROJECT_STATE.md`, WORKLOG tail,
  attempt/marker state (no prior stage-50 attempt output existed — fresh
  start, nothing to resume), stage-20 outputs (Theorem 1, CASE A–J,
  feasibility matrix), stage-30 architecture + 24-row risk register,
  stage-40 scorecard/vetoes, the 10A/10C syntheses (to pin the
  2007/2022/2025 direct prior art to [H006]/[H007], [H003]/[H004],
  [H001]/[H002]), and a compact index of all 219 ledger rows for
  evidence-ID selection. No new web searches were needed: the stage is a
  synthesis/adversarial-analysis stage over the existing verified
  evidence base, and every technical claim cites existing ledger/claim
  IDs (no new sources introduced, so no new verification burden).
- Wrote `outputs\05_LIMITATIONS_AND_FAILURE_MODES.md`: 18 failure modes
  (FM-01…FM-18) with the seven required fields each, mapped explicitly
  onto all 15 stage-required areas; §3 separates potential into 6 value
  classes, each conditional on measurable advantage + identifiable
  calibration; §3.6 states plainly that the broad hybrid idea is NOT
  novel (C01/C27/C29) and defines the narrowest defensible contribution
  as gap (a)+(b) of C36 realized at HSX in the gap-(d) niche, with gap
  (c) collaborator-led; §4 lists 7 counterexamples where a simpler
  sensor wins (Mirnov, Rogowski/CER, inductive-pair z-pinch, NMR,
  accelerator triple, TMR-in-gamma, optical-in-core).
- Wrote `outputs\05_TECHNOLOGY_COMPARISON.csv` via deterministic builder
  `tools\build_05_technology_comparison.py`: 15 rows × exact 20-column
  header; qualitative cells tied to ledger evidence; the only numbers
  quoted are numbers already in the evidence map (C02/C05/C12/C13/C18/
  C20/C26/C28/C30/C31); `unknown`/`not_applicable` wherever evidence is
  absent (fluxgate/NMR/SQUID/planar-Hall radiation cells, TMR/AMR
  neutron cells, field ranges not in ledger); 5 rows carry explicit
  COUNTEREXAMPLE best-fit entries; SQUID fusion-unsuitability kept as a
  labeled inference per the 10C gap note, not asserted.
- Wrote `outputs\05_FALSIFICATION_TESTS.md`: FT-01…FT-12 ordered desk →
  simulation → bench → machine-piggyback → irradiation; each with
  hypothesis/setup/reference/metric/pass-fail threshold/confounders/
  decision/evidence; thresholds defined relative to T0 predictions,
  measured noise floors, or emulated drift wherever true magnitudes are
  Unknown (C14) — no invented absolute numbers; FT-01…FT-10 are
  radiation-free and each can stop/descope the project (stage acceptance
  gate); FT-06-fail, FT-07-fail and FT-11(a) branches are explicitly
  documented as good simplifying outcomes; FT-11/FT-12 stay
  collaborator-led behind G0–G3, preserving the stage-30 §9.4 HSX
  decoupling and the root no-radiation-experiments scope rule.
- Validation: `tools\validate_50_outputs.py` (new, kept as reusable)
  33/33 PASS — existence/nontriviality; exact CSV header; ≥10/≥15/≥8
  counts (actual 15/18/12); no empty CSV cells; every evidence_id/
  source/claim/risk ID resolves (zero invented IDs); `unknown` +
  `not_applicable` present; ≥3 counterexamples (5); all 7 FM fields and
  all 8 FT fields present per item; FM↔FT cross-references closed; 10
  radiation-free rows confirmed in the FT summary table.
- Acceptance-gate check against the stage prompt: ≥15 failure modes ✔
  (18); ≥10 technologies without fake precision ✔ (15); counterexamples
  where a simpler sensor wins ✔ (5 CSV rows + §4); potential conditional
  on measurable advantage + identifiable calibration ✔ (§3 table);
  falsification can stop the project before expensive radiation work ✔
  (FT-01…FT-10 radiation-free with stop decisions).
- No sibling file (`..\06`, `..\07_HSX_august2025_results`, root `01`
  files, runner/policy files, prior-stage outputs) was modified; no
  outreach or external write occurred.
- Checkpoint: `state\checkpoints\CP_50_limitations_comparison_20260727-041056.md`.
- Next action: run/resume the launcher into `60_research_program`
  (model/effort per `MODEL_POLICY.md`).

## 2026-07-27 — Stage 60 (`60_research_program`, Fable 5 / xhigh, attempt 1)

- Read the full required context before acting: shared contract, stage-60
  prompt (verified the generated effective prompt path in
  `state\attempts\60_research_program.json`; status `CLAUDE_IN_PROGRESS`,
  no session ID, no `06_*` outputs — fresh start, matching the
  10B–50 pattern), all mission policy files, `state\PROJECT_STATE.md`,
  full WORKLOG, stage-20 feasibility verdict, stage-30 architecture
  (tiers T0–T3, gates G0–G5, binding §9.4) and simulation plan (rungs,
  §11 module boundary), stage-40 scorecard + collaboration strategy,
  stage-50 limitations (§3.6 narrowest contribution) + full FT-01…FT-12
  ladder, and — as read-only integration context — folder 06's
  `FINAL_ACTION_PLAN.md` and `06_24_MONTH_PHD_ROADMAP.md` (critical
  path, two-paper floor P1/P2, MVG-vs-upside M28, direction gate M34,
  disclosure gates). No new web searches: stage 60 is a synthesis/
  program-design stage over the verified evidence base; every technical
  claim cites existing ledger/claim/test IDs (no new sources, no new
  verification burden).
- Identified and recorded a naming conflict: folder 06 and this mission
  both define gates named G0–G5 with different meanings (06: inventory/
  anomaly/campaign/direction; here: stage-30 tier gates). Resolved in
  all stage-60 outputs via explicit `06-G*` / `HY-G*` prefixes with
  both originals preserved (CLAUDE.md conflict rule).
- Wrote `outputs\06_INTEGRATED_RESEARCH_PROGRAM.md`: the required
  direct conclusion on the user's three-step interpretation — CONFIRMED
  IN SUBSTANCE, REFINED IN ORDER AND SCOPE: (1) Hall-first confirmed as
  a hard gate (already folder-06 critical path; Theorem 1 makes the
  bench anchor non-optional); (2) hybrid-second confirmed with two
  corrections (the riskiest claim, reverse-direction C36b, is tested at
  bench-days cost via FT-05 inside the first bench block; the research
  claim narrowed to the §3.6 gaps — broad hybrid NOT novel per
  C01/C27/C29); (3) module-third REORDERED — the T0 estimator/
  simulation core moves first as the falsification instrument (HY-G0,
  FT-02/FT-03 gate every later dollar per FM-18), while the frozen
  §11-bounded package + publication stays last. All five stage-prompt
  alternatives dispositioned with citations (early bench hybrid test:
  adopted; embedded actuation from the start: rejected as default,
  drawing-level winding provision retained, gated at FT-06 with descope;
  rad-hard Hall reference: rejected as primary (R071 single-source,
  C18), retained as top-tier witness; defer radiation to collaborator/
  coauthored: adopted and binding (§9.4, root scope rule); abandon-if-
  simpler: kept live via FT-07 and kill criteria K5/K6). Phases 0–6
  each carry the 9 stage-required fields (deliverables, reference
  instrument, acceptance metrics, cost category, time range,
  dependencies, collaborator need, publication value, stop/pivot rule);
  publication map P1 (SENSL, unchanged), P2 (two-paper-floor WP-D paper
  = gap-(a) theory + honesty-tested estimator + bench validation), P3
  (RSI, gap-(d)/(b) in-machine), P4 (coauthored radiation, optional);
  collaboration timing per stage-40 with per-lane evidence packs and
  hard no-radiation-commitment boundary; budget Tiers 1–3 with
  accuracy-lost and upgrade-forcing evidence gap per tier (only sourced
  prices: folder-06's own ~$90 BOM / ~$8 REF200 internal figures,
  labeled; everything else cost drivers + FT-ladder categories);
  boundaries B1–B8 and kill criteria K1–K10.
- Wrote `outputs\06_DECISION_GATES_AND_ROADMAP.md`: ordered master
  gates DG-00…DG-11 with order = execution = cost (every expensive step
  behind a cheaper falsification gate — stage acceptance property);
  per-gate entry dependencies, pass→ and fail→pivot paths tied to
  K1–K10; external gates marked (06-G1 anomaly closure binds Phase 1
  exactly as folder 06 requires; campaign windows; 06-M28 MVG
  checkpoint and 06-G5 direction gate as standing synchronization
  points; disclosure gates 06-G-A…G-H bind all public artifacts);
  text dependency graph showing the P1/P2 critical path touches this
  program only at DG-03 and DG-11; checkpoints CP-A…CP-H with the
  three-question review discipline; 7 concrete resume-ready next tasks
  (items 1–3 desk-executable immediately; 4–5 behind 06-G1; nothing
  adds a folder-06 critical-path element); honest limitations
  (C14 provisionality, single-source H059/R071, external schedule
  authority, no Phase-4 facility/commitment claimed).
- Wrote `outputs\06_ADVISOR_MEETING_BRIEF.md`: one-sentence decision +
  5 sub-decisions, designed to ride the already-planned folder-06
  advisor meeting (06-M01/M02) rather than add one; 30-second technical
  summary (Theorem 1, C02 direction asymmetry, anchor-based absolute
  accuracy, §3.6 claim); evidence-base summary with counts; "what
  changes: almost nothing" section (P1 unchanged; +2 bench tests
  ~3–6 days; WP-D becomes the T0 package; campaigns piggyback-only;
  radiation explicitly removed from the first-author path); 5 unresolved
  risks stated plainly; lowest-cost next experiments (FT-02
  zero-hardware honesty test; FT-04 one bench-day); 6 questions for the
  advisor; bring-list.
- Validation: `tools\validate_60_outputs.py` (new, kept as reusable)
  34/34 PASS — existence/nontriviality of all three outputs; ledger
  header exact on parsed fields + 219 rows; evidence map 37 claims;
  risk register 24 rows; all cited IDs resolve (17 bracketed source IDs,
  22 claim IDs, 12 FT, 6 FM, 4 RR — zero invented IDs); all 7 phases,
  3 budget tiers, K1–K10, DG-00…DG-11, HY-G/06-G disambiguation,
  critical-path-decoupling and module-boundedness markers present;
  labels convention declared in all three; all 9 outputs CSVs re-parsed
  clean. Two initial validator false-failures (raw-line vs parsed-field
  header comparison; line-wrapped label phrase) were validator bugs,
  fixed in the validator — outputs unchanged.
- Acceptance self-check against the stage prompt: sequence evaluated,
  not repeated (confirmed/reordered/narrowed with stage-20/30/40/50
  rationale) ✔; radiation not silently added to the immediate HSX
  critical path ✔ (B1/B2, DG-09 no-agreement branch = zero impact);
  every expensive step has a preceding cheaper falsification gate ✔
  (DG order = FT-ladder cost order); collaboration recommendations
  specify when to approach and what evidence to bring ✔ (program §5,
  DG-08 pack); module/simulation deliverable has a realistic bounded
  PhD position ✔ (program §3.8, DG-11 freeze rule).
- No sibling file (`..\06`, `..\07_HSX_august2025_results`, root `01`
  files, runner/policy files, prior-stage outputs) was modified; no
  outreach or external write occurred; no auxiliary model used.
- Checkpoint: `state\checkpoints\CP_60_research_program_20260727-042418.md`.
- Next action: run/resume the launcher into `70_redteam` (model/effort
  per `MODEL_POLICY.md`).
