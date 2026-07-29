# 00 — Input inventory, boundary, and option-2 reconstruction (Stage 00)

Prepared by: Claude Code, stage `00_inventory`, requested model Sonnet 5 /
High. This file separates **reconstruction** (what folder `06` and the
mission-08 policy files actually say) from **new recommendation**, which is
explicitly out of scope for this stage. No technical conclusion about
calibration feasibility, radiation compensation, or application priority is
asserted here; those belong to stages 20/30/40/50/60.

---

## 1. Inspected paths and purpose

All items below were read-only. No sibling file was modified (verified: only
the `Read`/`Grep`/`Glob` tools were used outside this folder's `outputs`).

### 1.1 This mission (`08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07`)

| Path | Purpose |
|---|---|
| `README_START.md` | Run command, the 4 decision questions, evidence gates, model policy summary, final reading order |
| `MISSION.md` | Scope, the identifiability framing, boundary conditions, success criterion |
| `SOURCE_POLICY.md` | Ledger schema, peer-review/tier/access enums, lane and final numeric gates, topic quotas, radiation-record fields, dedup rule |
| `DECISION_FRAMEWORK.md` | Minimal measurement model (`y_H`, `y_C`), 5-scenario observability table, research-direction scoring rubric + vetoes, 3-tier accuracy/budget framework, collaboration decision criteria |
| `LITERATURE_SEEDS.md` | Discovery-only seed list (hybrid/coil, radiation/fusion Hall, application, alternative-technology); explicitly not pre-accepted evidence |
| `AGENTS.md` | Write-boundary contract, model-integrity rule, no-external-provider rule |
| `CLAUDE.md` (this folder) | Restates the shared research contract (identical to `prompts\_shared_system.md`) |
| `EXECUTION_PLAN.md` | The 12-stage table: model/effort/purpose/required outputs per stage — authoritative for what each later stage must produce |
| `MODEL_POLICY.md` | Routing rationale, Fable integrity rule, 2-event downgrade protocol, log-file inventory |
| `CHECKPOINT_PROTOCOL.md` | Durable-file inventory, checkpoint format, first/second Fable-failure procedure, resume behavior |
| `PACKAGE_MANIFEST.md` | Full file/folder manifest and read-only-context declaration |
| `RESUME_GUIDE.md` | Exact resume/dry-run/guarded-mode commands |
| `OFFICIAL_SETUP_REFERENCES.md` | Exact Claude Code CLI flags used by the runner, incl. `--disallowedTools mcp__*` |
| `RUN_HYBRID_RADIATION_ANALYSIS.ps1` | Ground truth for stage order, exact `Expected` output filenames per stage, and the model-integrity/downgrade state machine (read for lines 1–1079 of ~2226; the stage table, model-integrity logic, and downgrade/retry/pause functions were inspected — the remainder is child-process plumbing not needed for this stage) |
| `prompts\_shared_system.md` | Shared contract identical in substance to this folder's `CLAUDE.md` |
| `prompts\00_inventory.md` | The current stage's own prompt (goal, work list, 3 required outputs, acceptance gates) |
| `prompts\10a…80_synthesis.md` (11 files) | Skimmed for each stage's declared output filenames only, to cross-check against `EXECUTION_PLAN.md` and the runner's `Expected` arrays |
| `state\PROJECT_STATE.md`, `state\WORKLOG.md` | Pre-run status: `READY_TO_START`, 0/12 stages complete, no research output yet |
| `state\attempts\00_inventory.json` | Confirms this is attempt 1, requested model `sonnet` / effort `high` — matches `EXECUTION_PLAN.md` |
| `state\generated_prompts\00_inventory_attempt_1_cycle_0_*.md`, `logs\run_2026-07-27_005332_821\00_inventory\…` | The exact effective prompt and raw stream directory for this attempt |
| `state\checkpoints`, `state\markers`, `state\sessions`, `state\handoff_history` | All empty — no prior stage work exists to reuse |
| `evidence\`, `outputs\`, `logs\` (other than the current run) | Empty prior to this stage |

### 1.2 Folder `06` (read-only sibling; the prior mission this extends)

| Path | Purpose |
|---|---|
| `06\MISSION.md`, `06\CLAUDE.md`, `06\AGENTS.md` | 06's own scope and contract (8-item request; low-cleanroom, application/software-novelty preference; no neutron/gamma scope) |
| `06\inputs\ORIGINAL_REQUEST.txt` | The user's verbatim original request that spawned 06 (decision-letter text + Tim's own message) — the only verbatim-user-text artifact found anywhere in this provenance chain |
| `06\outputs\00_INPUT_INVENTORY.md`, `00_REQUIREMENTS_TRACE.csv`, `00_CONFLICT_LEDGER.md`, `00_CLAIM_BASELINE.csv` | 06's own stage-00 baseline |
| `06\outputs\01_SOURCE_LEDGER.csv`, `01_LITERATURE_REVIEW.md`, `01_SOURCE_COVERAGE.md`, `01_EVIDENCE_MAP.csv` | 231-row verified peer-reviewed ledger and its coverage report |
| `06\outputs\02_RESEARCH_DIRECTION_DECISION.md`, `02_DIRECTION_SCORECARD.csv` | The OPT1–OPT4 scored decision; OPT2 adopted |
| `06\outputs\03_MANUSCRIPT_DIAGNOSIS.md`, `03_PUBLICATION_ROUTE_DECISION.md`, `03_REVIEWER_RESPONSE_MATRIX.csv` | Manuscript/venue-route analysis |
| `06\outputs\04_HSX_EXPERIMENT_PLAN.md`, `04_MEASUREMENT_REQUIREMENTS.csv`, `04_DATA_ANALYSIS_PLAN.md`, `04_UNCERTAINTY_AND_STATISTICS_PLAN.md` | Bench/experiment plan (WP-A/B/C/D) |
| `06\outputs\05_CANDIDATE_PROTECTABLE_CONCEPTS.md`, `05_PRIOR_ART_LEDGER.csv`, `05_DISCLOSURE_HOLD_CHECKLIST.md` | IP research screen |
| `06\outputs\06_24_MONTH_PHD_ROADMAP.md`, `06_MILESTONES.csv`, `06_ADVISOR_MEETING_BRIEF.md`, `06_STARTUP_READINESS.md` | Roadmap and startup framing |
| `06\outputs\07_RED_TEAM.md`, `07_SOURCE_AUDIT.csv`, `07_CORRECTION_LOG.md` | Independent red-team audit: 0 critical/high findings, 1 medium + 6 low + 4 info, all correctable ones fixed |
| `06\outputs\FINAL_EXECUTIVE_STRATEGY.md`, `FINAL_ACTION_PLAN.md`, `FINAL_AUDIT.md`, `FINAL_DELIVERABLE_INDEX.md` | Final synthesis; `FINAL_AUDIT.md` states `FINAL STATUS: PASS` |

### 1.3 Folder `07_HSX_august2025_results` (read-only sibling; raw campaign data)

Inspected at file/inventory level only, per stage instruction. Contents:
`hsx_20250821\` holds per-shot `.dat`/`.png` files (density, stored-energy,
overview plots for shots #18–#21+), MATLAB figure-generation scripts
(`figure3.m`…`figure5.m`, `bigfigure.m`, `hsx_test_result_matlab.m`),
generated figures (`Fig3_SensorVerification_*.png`,
`Fig4_PlasmaDynamics_*.png`, `fig5.eps`), and main-coil-current text logs
(`hsxMainCoilCurrent*.txt`), plus subfolders `1T_qhs_backup`, `plots`,
`qhs_1T_fft`, and a `New folder`. This matches folder 06's description of
the immutable Aug-2025 raw archive (claims C001/C002 in `06`'s baseline). No
file was opened at content level beyond directory listing, per the stage-00
scope ("opening only the most relevant context").

### 1.4 Parent launchers and root instructions

| Path | Purpose |
|---|---|
| `..\CLAUDE.md` (root `01`) | Owner/trajectory framing, folder map, session workflow, model/effort escalation ladder, the explicit no-neutron/gamma scope rule |
| `..\RUN_HYBRID_RADIATION_ANALYSIS.ps1` (parent copy) | Same runner referenced by `README_START.md`'s run command (`.\RUN_HYBRID_RADIATION_ANALYSIS.ps1` invoked from `01`) |

---

## 2. Option-2 reconstruction: is Hall-first / hybrid-second / module-third folder 06's stated sequence?

**Verdict: PARTLY CONFIRMED**, with three distinguishable sub-claims and
three different outcomes. This is a reconstruction of what `06` says, not a
new recommendation — stage 60 of this mission decides the actual
recommendation.

### 2.1 "Hall sensor/device validation and metrology first" — supported by a genuine hard gate

`06`'s action plan states as a **hard rule**: *"No calibration work before
B-01 anomaly closure (the ~109× emulator magnitude anomaly)"*
(`06\outputs\FINAL_ACTION_PLAN.md` §7 item 3), and the gate table makes WP-C
(calibration) conditional on G1 passing: *"G1: bench-truth gate … Pass →
WP-C proceeds; P1 drafting starts"* (`06\outputs\FINAL_EXECUTIVE_STRATEGY.md`
§4 item 1; `06\outputs\02_RESEARCH_DIRECTION_DECISION.md` §8). This is a real,
explicit dependency: Hall-device bench calibration is a documented
precondition for calibration-bearing claims. **Confirmed** at this narrow
scope.

### 2.2 "Hybridization with an inductive coil second" — confirmed only as a paper-sequence label, not a strict serial dependency

`06`'s 24-month paper sequence places **P1** (finished-calibration Hall
sensor paper, months 0–7) before **P2** (hybrid Hall+inductive
drift-corrected architecture paper, WP-D, months 6–18)
(`06\outputs\02_RESEARCH_DIRECTION_DECISION.md` §6). However, `06` explicitly
allows WP-D/P2 work to proceed **in parallel** with, not strictly after, P1:
*"P2 draft begins (M27, parallel to P1 review)"*
(`06\outputs\FINAL_ACTION_PLAN.md` §4 item 5), and names an explicit fallback
in which WP-D proceeds *before* full real-die calibration exists: *"WP-D
proceeds on 2025 + synthetic data"* if campaign #1 slips
(`06\outputs\FINAL_EXECUTIVE_STRATEGY.md` §8, gate G2 fallback F1). So the
*paper-numbering* order is Hall-first, but the *engineering-work* order
permits substantial overlap. **Partly confirmed.**

### 2.3 "Reusable module and simulation package third" — no direct precedent found in folder 06

No file in `06\outputs` uses language matching "reusable module" or
"simulation package" as a named third deliverable phase (checked by
targeted grep across all of `06`'s outputs, evidence, prompts, and logs;
zero substantive matches). `06`'s actual third paper, **P3**, is the RSI
**vector-probe hardware instrument paper** tied to HSX campaign #2
(`06\outputs\02_RESEARCH_DIRECTION_DECISION.md` §6) — a physical-probe
deployment paper, not a software module or simulation package. The nearest
adjacent language is career-framing, not a deliverable: *"durable, ownable
assets it produces are the calibration infrastructure, firmware, demod/
fusion codebase, and qualification datasets"*
(`06\outputs\02_RESEARCH_DIRECTION_DECISION.md` §9). **Not confirmed** — this
specific three-phase framing (Hall validation → hybridization → reusable
module/simulation package) is the user's own new articulation for this
mission, not a restatement of a `06` conclusion. This mission's own
`MISSION.md` also frames it as a hypothesis to test rather than a settled
finding: *"Treat that as a hypothesis to test. Do not make the conclusion
fit it."*

### 2.4 What follows for this mission

Stages 20/30/60 must independently determine sequencing rather than assume
either `06`'s paper order or the user's three-phase framing is already
established. In particular: `06`'s OPT2 decision endorsed WP-D (hybrid
fusion) as *feasible by precedent* — citing tokamak Kalman-filter
coil+Hall fusion papers as a template (`06\outputs\02_RESEARCH_DIRECTION_
DECISION.md` §3.2, citing the 2025 *Nuclear Fusion* and *Fusion Engineering
and Design* papers already named in this mission's `LITERATURE_SEEDS.md`) —
but did **not** perform a state/parameter observability derivation specific
to the Hall+coil confounding problem this mission's `DECISION_FRAMEWORK.md`
requires (§C4 of `00_CONFLICT_LEDGER.md`). That derivation is stage 20's job,
not something inherited from `06`.

---

## 3. Existing evidence vs. missing evidence

### 3.1 What `06` already established (available for reuse, not re-derivation)

- A 231-row verified peer-reviewed ledger (`06\outputs\01_SOURCE_LEDGER.csv`)
  with a red-team-audited 154%-of-minimum count, 0 duplicate DOIs/titles,
  and a documented verification-depth breakdown (10% full-text, 58%
  abstract, 32% metadata-only).
- A scored, sensitivity-tested research-direction decision (OPT2 ADJUST)
  with named falsifiers.
- A manuscript/reviewer diagnosis and venue-route comparison grounded in the
  actual decision letter.
- A bench-only, campaign-independent experiment plan (WP-A/B/C/D) with
  measurable acceptance criteria.
- An IP research screen (6 candidate concepts, prior-art ledger, disclosure
  checklist).
- A 24-month roadmap with 44 dated milestones and named stop/pivot gates.
- An independent red-team audit (`07_RED_TEAM.md`) with a clean disposition
  log and a final `FINAL STATUS: PASS`.

### 3.2 What `06` did **not** establish (this mission's actual work)

- **No dedicated radiation-effects lane.** `06`'s seven topic categories
  (`01_SOURCE_COVERAGE.md` §5) have no standalone "radiation" bucket; the
  nearest is a combined "temperature/radiation/packaging/calibration" tag
  (117 rows) that does not isolate radiation-specific evidence. This
  mission's `SOURCE_POLICY.md` requires a dedicated ≥45-row radiation lane
  and a ≥30-row final quota — new work, not a re-count of `06`.
- **No derived observability/identifiability result** for the specific
  Hall-gain/bias vs. coil-gain/integrator-drift confounding problem (see
  §2.4 above and `00_CONFLICT_LEDGER.md` C4).
- **No radiation-compensation architecture, simulation/validation plan, or
  risk register** — `06` scoped radiation experiments out entirely
  (root `01\CLAUDE.md`: *"No neutron/gamma radiation experiments are
  planned"*); this mission's stage 30 must design a compensation
  architecture as a specification, not as work Tim will personally execute
  (see `00_CONFLICT_LEDGER.md` C6).
- **No technology-comparison ledger against the full alternative-sensor
  landscape** (fluxgate, AMR/GMR/TMR, fiber-optic/Faraday, NMR, SQUID,
  NV-center, resonant/MEMS) at the depth `DECISION_FRAMEWORK.md`/
  `LITERATURE_SEEDS.md` specify — `06`'s ledger touches some of this
  incidentally via its "low-fabrication novelty" category (65 rows) but was
  not built to this mission's comparison structure.
- **No application/collaborator scorecard covering the six named domains**
  (tokamak, stellarator, z-pinch/pulsed power, magneto-inertial fusion,
  HTS magnets/rotating machinery, other) — `06`'s scope was narrowly HSX/
  Senesky-group-fit; this mission's stage 40 is broader by design.
- **No accuracy-vs-budget tiering** in `06`'s own vocabulary (Tier 1 bench
  truth / Tier 2 self-test hybrid / Tier 3 environmental qualification) —
  `06` has cost/burden numbers (e.g., ~$90 calibration BOM) but not this
  mission's 3-tier structure.

### 3.3 New-evidence delta obligation

`SOURCE_POLICY.md` requires **≥75 verified sources new relative to
`06\outputs\01_SOURCE_LEDGER.csv`** (normalized DOI/title comparison), on
top of the ≥120-unique-source final-ledger floor. This is a numeric
acceptance gate for stage 10d, not something stage 00 can satisfy or
pre-check beyond confirming the comparison baseline file exists and is
readable (confirmed: `06\outputs\01_SOURCE_LEDGER.csv` is present, 231 rows,
exact `SOURCE_POLICY.md`-schema header).

---

## 4. Read-only / write boundary

- **Written by this mission:** only inside
  `08_Hall_Coil_Hybrid_Radiation_Strategy_2026-07\{outputs,evidence,state,
  logs}`. This stage wrote only `outputs\00_INPUT_INVENTORY.md` (this file),
  `outputs\00_REQUIREMENTS_TRACE.csv`, `outputs\00_CONFLICT_LEDGER.md`, plus
  the required `state\PROJECT_STATE.md` update, a `state\WORKLOG.md`
  append, and a `state\checkpoints\CP_00_inventory_*.md` checkpoint.
- **Read-only, not modified:** `..\06\**` (entire folder, incl. `_history`,
  `evidence`, `logs`, `state`, `inputs`), `..\07_HSX_august2025_results\**`,
  `..\CLAUDE.md`, `..\RUN_HYBRID_RADIATION_ANALYSIS.ps1` (parent copy), and
  all other `01`-level siblings not explicitly named above (not opened,
  per the stage-00 inspection list, which names only `06`, `07`, and the
  root launcher/instructions).
- **Not touched at all:** the mission's own runner
  (`RUN_HYBRID_RADIATION_ANALYSIS.ps1`), `INVOKE_CLAUDE_CHILD.ps1`,
  `VALIDATE_PACKAGE.ps1`, `TEST_CLAUDE_MODELS.ps1`, any policy file
  (`SOURCE_POLICY.md`, `DECISION_FRAMEWORK.md`, `MODEL_POLICY.md`,
  `CHECKPOINT_PROTOCOL.md`, `AGENTS.md`, `MISSION.md`, `EXECUTION_PLAN.md`,
  `LITERATURE_SEEDS.md`, `PACKAGE_MANIFEST.md`), any prompt file, any
  completion marker, or any rejected-attempt archive — consistent with
  `AGENTS.md`'s and the shared contract's write-boundary rule.

## 5. Scope caveat

This mission does not claim, and this stage's outputs do not imply, that
Tim (or this mission) has performed, is performing, or will personally
perform any neutron, gamma, proton, electron, or heavy-ion irradiation
experiment. Per root `01\CLAUDE.md` ("No neutron/gamma radiation
experiments are planned") and this mission's own `MISSION.md` ("The user's
current first-author HSX work does not automatically acquire a
radiation-test requirement"), radiation work in this mission's later stages
is literature-, simulation-, and architecture-level analysis, with any
actual exposure testing scoped as a possible future collaborator- or
co-author-led activity (echoing the co-authored TCAD radiation-modeling
paper already in preparation, per root `01\CLAUDE.md`'s trajectory item 4),
never as an experiment attributed to Tim's own HSX program.
