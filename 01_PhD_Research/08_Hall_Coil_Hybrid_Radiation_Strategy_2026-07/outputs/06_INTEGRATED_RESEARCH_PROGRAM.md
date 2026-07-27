# 06 — Integrated research program

Stage 60 (`60_research_program`). Produced and signed off by Fable 5
(xhigh). Source IDs (`Hxxx`, `Rxxx`, `Pxxx`) cite
`outputs\01_SOURCE_LEDGER.csv`; claim IDs (`Cxx`) cite
`outputs\01_EVIDENCE_MAP.csv`; `CASE x`/Theorem 1 cite
`outputs\02_OBSERVABILITY_AND_IDENTIFIABILITY.md`; `FT-xx` cite
`outputs\05_FALSIFICATION_TESTS.md`; `FM-xx` cite
`outputs\05_LIMITATIONS_AND_FAILURE_MODES.md`; `RR-xx` cite
`outputs\03_RADIATION_RISK_REGISTER.csv`. Labels: **Observed / Derived /
Inferred / Proposed / Unknown** per `CLAUDE.md`.

**Gate-name disambiguation (binding for this file and its two
companions):** folder `06`'s PhD strategy defines its own gates G0
(bench inventory), G1 (~109× anomaly closure), G-cal, G2–G4 (campaign
gates), G5 (direction gate, milestone M34), and G-A…G-H (disclosure).
This mission's stage-30 tier gates are a *different* G0–G5 series. To
prevent silent collision (recorded as a conflict, per `CLAUDE.md`), this
stage writes folder-06 gates as **06-G\*** and this mission's hybrid
gates as **HY-G\*** (HY-G0 = stage-30 G0, etc.). Neither series is
renamed in its home documents.

---

## 1. Direct conclusion on the user's three-step interpretation

The working hypothesis under test (`MISSION.md`): *validate and measure
the Hall device first; add an inductive coil as a complementary hybrid;
then provide a reusable module and simulation package.*

**Verdict (Derived from Stages 20–50): CONFIRMED IN SUBSTANCE, REFINED
IN ORDER AND SCOPE.** Three specific corrections, each with its
rationale:

### 1.1 Step 1 — "Hall validation and metrology first": CONFIRMED as a hard gate

Hall bench validation is already the folder-06 critical path (WP-C
calibration, gates 06-G1/06-G-cal), and every identifiability result of
this mission *presupposes* a bench-calibrated Hall channel: the
hardware-proven correction direction is Hall→coil (C02, [H004], [H005],
[P003]), and it works only from a calibrated, traceable Hall channel.
Nothing in this mission weakens Hall-first; Stage 20 strengthens it
(Theorem 1: the pair alone never yields absolute scale or Hall offset —
an external bench anchor is not optional). **Confirmed** — and it is
already scheduled work (folder-06 M08–M12), not new work.

### 1.2 Step 2 — "hybrid second": CONFIRMED, with two scope corrections

- **The hybrid's riskiest claim must be tested cheaply and early, not
  "second."** The alternative sequencing the stage prompt names — *run
  an early low-cost identifiability/bench hybrid test before deep Hall
  radiation work* — is **adopted**. The reverse-calibration direction
  (coil-derived Hall-gain tracking, gap C36b — the mission's most-wanted
  novel capability, single non-fusion precedent [H059], C11) is
  falsifiable for bench-days cost (FT-05) using the *same* bench, field
  source, and transfer standard that Phase-1 Hall metrology needs
  anyway. Deferring it behind a long Hall-only phase would spend months
  before testing the claim the whole hybrid program stands on. FT-05
  therefore runs inside the first bench block (Phase 1/2 boundary), at a
  marginal cost of a wound/PCB coil plus ~2–3 bench-days (labeled
  estimate).
- **"Hybrid" as a research claim is narrowed to the §3.6 verdict.** The
  broad Hall+coil idea is 26-year-old, multi-domain prior art (C01),
  deployed at machine scale (ITER OVSS, C27, [P003]) and routine in
  accelerator metrology (C29, [P052]-class). The defensible content is
  the four C36 gaps, realized as: gap (a) joint-identifiability theory
  (Theorem 1 + anchor/excitation conditions — already derived, Stage
  20), gap (b) first in-machine demonstration of coil-referenced
  Hall-gain tracking, in the gap-(d) stellarator niche (C32, literature-
  empty) at HSX, with gap (c) collaborator-led (Phase 4). Framing:
  **engineering integration with one bounded theoretical contribution**
  (C37; FM-17 veto on anything broader).

### 1.3 Step 3 — "reusable module and simulation package third": REORDERED

This is the one structural correction. The step splits in two:

- **The estimator/simulation core moves FIRST.** Stage 30 makes T0
  simulation the mandatory first spend (HY-G0), and Stage 50 makes the
  estimator honesty test (FT-02) and the anchor-cadence sweep (FT-03)
  the gatekeepers of every later dollar: an estimator that "converges"
  on a Theorem-1 gauge orbit would poison every subsequent gate (FM-18).
  The simulation package is not a deliverable that follows the hardware
  — it is the falsification instrument that *precedes* it.
- **The frozen, citable package + publication stays LAST.** The
  *release* position of the user's step 3 survives: the module is built
  incrementally from Phase 0, then frozen at the `03_SIMULATION_AND_
  VALIDATION_PLAN.md` §11 boundary and published as consolidation
  (Phase 6). The §11 interface spec, the frozen-science rule (the
  measurement equations, freeze policy, species-vector discipline, and
  pre-registered expectations may not change without a stage-20-class
  review), and the fixed scenario/metric set (S1–S12, M1–M8) are what
  keep this a bounded engineering deliverable rather than an open-ended
  software project (stage acceptance requirement; §3.8 below).

### 1.4 The remaining prompt alternatives — dispositions

| Alternative | Disposition | Basis |
|---|---|---|
| Early low-cost identifiability/bench hybrid test before deep Hall radiation work | **Adopted** (§1.2; FT-05 in the first bench block; all deep radiation work is behind HY-G0–G3 anyway) | FT ladder ordering; stage-30 §9.4 |
| Embedded calibration actuation with the Hall device from the start | **Rejected as a default; retained as a gated option with a cheap design provision.** The winding is the HA/T2 layer behind HY-G1 and FT-06, with an explicit descope-to-MVD stop rule (an anticipated *good* outcome). But the head design from Phase 1 onward reserves the winding footprint and feed routing (a drawing-level provision, near-zero cost), so the T2 option is not foreclosed by packaging. AC injection can never deliver Hall offset (CASE E; Theorem-1 β-null) — "actuation from the start" would buy less than its proponents assume. | Stage-30 §5, §9; FT-06; FM-11 |
| Radiation-hard Hall reference instead of compensating a sensitive device | **Rejected as the primary architecture; retained as the top-tier witness channel.** Option F is a single channel with no redundancy; its evidence base is one unreplicated null result ([R071], C18, RR-18) and metallic-Hall SNR at HSX-class fields is Unknown. As Option D's mechanism-diverse witness inside the layered architecture it is the *only* route to drift attribution (CASE G) — kept at the collaborator-enabled tier, contingent on FT-11(ii) replication. | Stage-30 §3 Options D/F; C18; C21 |
| Defer radiation to a collaborator/coauthored work package | **Adopted — and binding.** Stage-30 §9.4: tiers T0–T2 involve no radiation and are the complete architecture-validation content relevant to first-author HSX work; T3 (FT-11/FT-12) is collaborator-led, coauthored, and never a prerequisite for any HSX deliverable. Mirrors the existing TCAD-paper precedent (root `CLAUDE.md`: radiation is cited as complementary/outlook in first-author work, never claimed experimentally). | Stage-30 §9.4; root scope rule; conflict C6 |
| Abandon the hybrid if a simpler diagnostic meets the use case | **Kept live as a standing kill criterion, not decided now.** Seven documented counterexamples where a simpler sensor wins outright (limitations §4); FT-07 (drift race vs scheduled recalibration) is the dedicated executioner, and its fail branch — "the hybrid earns only its fault-detection and C02 roles" — is pre-scripted as an honest exit (§7 kill criteria K5/K6). For the chosen use case (stellarator mapping + long-pulse drift), no simpler single sensor currently meets the documented need (C32, C33), which is why the program proceeds — conditionally. | Limitations §4; FT-07/FT-10; C32/C33 |

**One-sentence answer:** keep the user's three steps as the *publication*
arc (Hall metrology → hybrid demonstration → released package), but
execute them with the simulation/estimator core first, the cheap
reverse-direction bench falsification inside the first bench block,
the calibration winding and witness channel as gated options rather than
defaults, and all radiation work collaborator-led behind HY-G3.

---

## 2. Recommended architecture and research claim

- **Architecture (Proposed; Stage 30):** the **MVD "anchored hybrid"**
  at HSX — existing current-spun GaN Hall channel + one wound/PCB coil
  on the same axis + co-located temperature sensor + shared-clock DAQ;
  referenced by (i) vacuum-shot machine-current anchors (CASE D, all
  four channel parameters per epoch), (ii) pre/post-shot zero-field
  epochs for offsets (CASE C2), (iii) an initial bench absolute
  calibration traceable to an NMR-class transfer standard ([H041],
  [H042], [H064]). The **HA "triangulated self-test hybrid"** (embedded
  winding + dual lock-in + triangle closure; witness die at top tier)
  is adopted *only* if FT-06/FT-07 prove it earns its complexity
  (HY-G2/G3 stop rules).
- **Research claim (Proposed; limitations §3.6):** an
  identifiability-grounded, anchor-referenced drift-tracking
  demonstration on a stellarator — gap (a) theory + gap (b) first
  in-machine hardware demonstration in the gap-(d) niche — with the
  estimator's honest non-identifiability behavior (state freezing +
  uncertainty growth between anchors) presented as a feature. Accuracy
  claims only ever in the form "X % relative to the anchor epoch,
  growing at the stated rate" (Theorem 1; FM-15).
- **What is explicitly NOT claimed:** that Hall and coil "calibrate each
  other" symmetrically (Stage-20 verdict: direction-dependent and
  misleading if stated symmetrically); any unconditional absolute
  accuracy; any experimental radiation result in first-author work
  (C14: no GaN/AlGaN Hall-plate neutron dataset exists — the program
  measures nothing it does not have).

---

## 3. Phased program

Phase names follow the stage prompt. Cost classes use the FT-ladder
scale (desk < simulation < bench-day < bench-soak < machine-piggyback <
irradiation campaign) — order-of-magnitude labels; the evidence base
contains no vendor prices (labeled-estimate rule, stage-30 §9). Time
ranges are tied to the folder-06 roadmap (base date 2026-07-25) and
inherit its slip logic; all are Proposed.

### 3.0 Summary table

| Phase | Content | Gate(s) | Cost class | Time range | Collaborator need | Publication value |
|---|---|---|---|---|---|---|
| 0 | Evidence/novelty/identifiability closure + T0 estimator honesty | FT-01; HY-G0 (FT-02, FT-03) | desk + simulation | substantially complete; T0 build Aug–Dec 2026 | none | P2 backbone |
| 1 | Hall bench validation + uncertainty budget | 06-G1 (external), FT-04, HY-G1 entry | bench-days | Aug–Oct 2026 (rides folder-06 WP-C block) | none | P1 + P2 |
| 2 | Coil/integrator characterization + hybrid observer | FT-05; HY-G1 exit | bench-days | Sep–Dec 2026 | none | P2 |
| 3 | Long-duration, temperature, injected-drift validation (+ in-machine piggyback) | FT-06, FT-07, FT-08, FT-09, FT-10; HY-G2/G3 | bench-soak + machine-piggyback | Nov 2026 – Jun 2027 | none (HSX access via existing collaboration) | P2 strength; P3 |
| 4 | Radiation screening/qualification — collaborator-led | HY-G3 + agreement → FT-11 → HY-G4 → FT-12 → HY-G5 | irradiation campaign | 2027–2028, optional for thesis | **required** (facility + coauthors) | P4 (coauthored) |
| 5 | Application/collaborator demonstration | rung-7 HSX demo; outreach gate | machine-piggyback | mid-2027 onward | optional (tokamak lane) | P3; external validation of P2 claims |
| 6 | Reusable module/simulation package + publication | HY-G0 maintained → freeze at P2 submission | desk | freeze Q1–Q2 2027; release with P2/P3 | none | P2 artifact; software/methods note (optional) |

### 3.1 Phase 0 — evidence/novelty/identifiability closure

- **Deliverables:** (done, this mission) 219-row verified ledger,
  37-claim evidence map, Theorem 1 + CASE analyses, §3.6 narrowest-
  contribution verdict; (to build) the T0 simulation package per
  `03_SIMULATION_AND_VALIDATION_PLAN.md` §2–§8 with FT-02 (estimator
  honesty) and FT-03 (anchor-cadence sweep) passed; FT-01 prior-art
  kill search re-run before every manuscript/proposal.
- **Reference instrument:** none (desk/simulation); the stage-20 rank
  tests (`tools\observability_rank_tests.py`) are the regression
  baseline the simulator must reproduce before any estimator is judged.
- **Acceptance metrics:** FT-01 pass (zero publications close a claimed
  C36 gap); FT-02 pass (state freezing + covariance inflation on
  CASE-A/F scenarios; prior-shifted runs agree within reported
  uncertainty); FT-03 pass (science requirement met up to the worst
  documented bounding-analog drift rates, C12/C13, labeled Inferred).
- **Cost category:** desk + simulation (engineering time only).
- **Time range:** evidence closure complete 2026-07-27; T0 build
  Aug–Dec 2026 (desk work, deliberately overlapping Phases 1–2 — it is
  folder-06 WP-D/M17 work under another name).
- **Dependencies:** none external. FT-05's thresholds need T0-predicted
  Fisher CIs, so the T0 core must exist before Phase-2 FT-05 execution
  — this is the sequencing correction of §1.3.
- **Collaborator need:** none.
- **Publication value:** the P2 paper's theory + methods backbone
  (identifiability analysis, honesty-tested estimator).
- **Stop/pivot rule:** FT-01 fail on gap (a)/(b) → drop that novelty
  claim, rebuild contribution around what remains (worst case: pure
  instrumentation framing, C37); FT-02 fail → **stop all hardware
  planning** until fixed; FT-03 fail → MVD alone insufficient — raise
  anchor cadence, add HA layer, or descope to short-window relative
  measurements (FT-03 decision branch).

### 3.2 Phase 1 — Hall bench validation and uncertainty budget

- **Deliverables:** absolute Hall calibration with a GUM-class
  uncertainty budget (folder-06 WP-C: 06-M08–M10); temperature
  coefficients `α_S`, `β_b` mapped; noise floor + `R_H` telemetry
  baseline; FT-04 zero-field/flip offset-anchor validation (≥10 read
  cycles, 180°-flip residual); cross-axis/misalignment bench map
  (FM-04 mitigation).
- **Reference instrument:** traceable transfer standard (NMR-class or
  equivalent, [H041], [H042], [H064]); fluxgate-class ambient audit of
  the zero-field environment (its one job in this program, FT-04);
  precision current measurement for the field source.
- **Acceptance metrics:** offset repeatability at or below T0-predicted
  uncertainty; flip residual consistent with the noise model; `α_S`,
  `β_b` characterized over the operating range; folder-06 06-G-cal
  criteria (u(k)/k ≤ 2 %, <0.5 % linearity per its plan) unchanged.
- **Cost category:** bench-days. The only sourced prices anywhere in
  this program are folder-06's own BOM estimates (~$90 calibration BOM
  + ~$8 REF200, folder-06 `FINAL_ACTION_PLAN.md` §1 — internal
  planning figures, not vendor quotes); marginal hybrid additions:
  wound/PCB coil + fixture, ~1 additional bench-day for FT-04 (labeled
  estimate).
- **Time range:** Aug–Oct 2026, riding the folder-06 WP-C bench block
  unchanged.
- **Dependencies:** **06-G1 (the ~109× anomaly closure) — hard external
  gate; folder 06's own rule "no calibration work before B-01 closes"
  binds this phase too.** T0-predicted uncertainties (Phase 0) needed
  for acceptance comparison.
- **Collaborator need:** none.
- **Publication value:** P1 (SENSL resubmission — calibration content);
  P2 (bench-validation section).
- **Stop/pivot rule:** FT-04 fail → the offset half of the calibration
  story is unsupported and AC injection can never substitute (CASE E):
  withdraw offset claims, re-derive every downstream budget, degrade
  the stellarator-mapping value case (HY-G1 blocker). 06-G1 fail →
  folder-06's own fault-isolation sprint; this program waits (it never
  jumps the queue).

### 3.3 Phase 2 — coil/integrator characterization and hybrid observer

- **Deliverables:** coil-chain transfer function + effective-area
  calibration ([R069], [R070] metrology baseline); integrator
  identification `{x_I(0), g, m, τ_L}` under rich dB/dt including the
  *predicted* g-vs-m confound under constant ramp (CASE I-ramp — a
  failure that must appear, validating the theory); **FT-05:
  coil-referenced Hall-gain recovery against emulated drift** (the
  reverse direction, C36b); augmented-state KF running on real bench
  data with the C02 correction direction demonstrated.
- **Reference instrument:** transfer standard as field truth; the
  pre-calibrated coil chain (its error maps 1:1 into inferred Hall
  gain, δS_H/S_H ≈ −δ(ΔB)/ΔB — measured first, FM-06).
- **Acceptance metrics:** recovered gains within Fisher-predicted CIs
  across ≥3 repetitions; variance scaling with excursion size
  `Σ(ΔB−ΔB̄)²` per the stage-20 prediction; ramp-degeneracy appears as
  derived; HY-G1 exit = anchored-hybrid calibration repeatable across
  ≥3 cycles within T0-predicted uncertainty.
- **Cost category:** bench-days (~2–3 marginal for FT-05, labeled
  estimate; shares Phase-1 hardware).
- **Time range:** Sep–Dec 2026 (interleaved with folder-06 M11–M12
  bench blocks at Tim's scheduling discretion; never displacing P1
  critical-path tasks — §7 boundary B6).
- **Dependencies:** Phase-1 calibration; T0 CIs (Phase 0).
- **Collaborator need:** none.
- **Publication value:** P2 core result (first hardware validation of
  the identifiability conditions; bench-scale gap-(b) evidence).
- **Stop/pivot rule:** FT-05 structural fail → **the reverse direction
  is falsified under ideal conditions**: the architecture collapses to
  the proven Hall→coil direction (C02), the C36b novelty claim dies,
  P2 reframes as incremental instrumentation + theory (the honest
  branch); FT-05 marginal fail → revise SNR/window budgets, re-run
  FT-03 with measured values.

### 3.4 Phase 3 — long-duration, temperature, and injected-drift validation

- **Deliverables:** rung-3 emulated gain/offset drift recovery on real
  hardware; rung-4 multi-day/week soak with scheduled anchors and
  engineered thermal excursions decorrelated from any dose proxy
  (CASE J-decorr rehearsal); **FT-06** (winding orthogonality/closure/
  self-heating — only if the HA layer is pursued); **FT-07** (drift
  race: full hybrid stack vs scheduled-recalibration-only twin — the
  measurable-advantage test); in-machine piggyback legs at HSX:
  **FT-08** (vacuum-shot machine-current anchors, ≥3 epochs), **FT-09**
  (repeated-waveform reproducibility floor), **FT-10** (plasma-ops EMI
  and ρ-alarm false-positive rate).
- **Reference instrument:** transfer standard (bench legs); HSX
  coil-current logs + validated vacuum field model (CASE D; C32,
  [P013]-class practice; W7-X's ~1e-4 coil-current accuracy criterion
  [P016] as the documented precision context); bracketing anchors for
  FT-09.
- **Acceptance metrics:** per-test thresholds as written in FT-06…FT-10
  (closure-residual stability over multi-day soak; heating inequality
  `|α_S|·R_th·R_cal·I_rms² ≪ δ_S`; A-vs-B margin in FT-07 exceeding
  A's added uncertainty; anchor repeatability consistent with
  T0-predicted uncertainty; detection floor at or below the FT-03
  drift resolution of interest; pre-registered ρ-alarm false-positive
  target).
- **Cost category:** bench-soak + machine-piggyback (no dedicated
  machine time initially; vacuum-shot piggyback and campaign-window
  ride-alongs on folder-06 campaigns #1/#2).
- **Time range:** Nov 2026 – Jun 2027 (FT-08/09 align with the
  campaign-#2 window Nov 2026–Feb 2027; soak tests Q1–Q2 2027; the
  HA go/no-go decision lands ~Q2 2027).
- **Dependencies:** HY-G1 (Phase 2); HSX campaign windows (upside
  scheduling — a slip degrades this phase's timing, not the P1/P2
  floor, mirroring folder-06 fallback logic F1/F2).
- **Collaborator need:** none beyond the existing UW-Madison HSX
  collaboration (Goodman, Gallenberger, Geiger).
- **Publication value:** P2 hardening (long-duration + honesty
  behavior on real data); P3/RSI in-machine content; FT-08/09 results
  are the evidence pack for any tokamak outreach (§5).
- **Stop/pivot rule:** FT-06 fail → descope to MVD (planned good
  outcome; quasi-static tracking claim withdrawn); FT-07 fail → the
  "better measurement performance" class is falsified for slow drift —
  hybrid survives on fault detection (§3.3 value class) + C02
  correction; cut the HA tier from any cost proposal; FT-08 fail →
  no absolute in-situ claim at the only accessible machine — reframe
  to relative/differential monitoring **before** any outreach; FT-10
  fail on both injection and ρ-alarm (with FT-07 failed) → deploy
  Hall and coil as separate instruments, drop the fusion layer (the
  honest full-retreat branch).

### 3.5 Phase 4 — radiation screening/qualification (collaborator-led; coauthored)

- **Deliverables:** FT-11 species-matched multi-sample coupon
  screening (GaN dies ≥5 irradiated + ≥3 control per condition,
  witness-material replication of [R071], coil/winding coupons) with
  co-located activation-foil dosimetry (two-step protocol,
  C/E = 1.05 ± 0.13 class, C26) and engineered T–Φ decorrelation;
  then, only on HY-G4 pass, FT-12 full-head mixed-field qualification
  per the FOCS/JET-DTE2 template (C20).
- **Reference instrument:** activation-foil dosimetry (C26); pre/post
  traceable bench calibration; unirradiated same-lot controls;
  independent material-diverse field reference at the head (FT-12).
- **Acceptance metrics:** measured `f_S,s(Φ_s)`, `f_b,s(Φ_s)` with
  stated uncertainty and sample spread; witness null replicated or
  refuted; FT-12 closed-loop compensation error within the HY-G5
  target against the independent reference.
- **Cost category:** irradiation campaign (the most expensive class;
  facility access, activated-hardware logistics, multi-sample
  fabrication — no facility, schedule, or price is assumed to exist).
- **Time range:** 2027–2028 at the earliest, and **optional for the
  thesis** — every branch of FT-11's three-way decision leaves the
  HSX first-author work unaffected (stage-30 §9.4).
- **Dependencies (binding):** HY-G0–G3 all passed + a collaborator
  agreement. **Radiation is not on the HSX critical path and is not
  silently added to it** (stage acceptance requirement; conflict-C6
  discipline; root `CLAUDE.md` no-neutron/gamma-experiments rule for
  first-author work).
- **Collaborator need:** **required** — facility, dosimetry, and
  radiation-effects expertise; coauthored publication model (the
  existing TCAD-paper precedent).
- **Publication value:** P4, coauthored: the first GaN Hall-plate
  neutron dataset (closing C14) and, if FT-12 passes, the first
  experimentally supported in-situ radiation-compensation claim
  anywhere (C21) — high value, not first-author-dependent.
- **Stop/pivot rule:** FT-11(a) drift below detection floor → in-situ
  radiation recal unnecessary; simplify to MVD + scheduled recal
  (explicitly a good outcome); FT-11(c) large/non-monotonic/
  unattributable drift or witness fails replication → hybrid
  compensation falsified for this material set; pivot to material
  change or scheduled-recal-only; FT-12 fail → compensation claim
  falsified at system level; retreat to detection + scheduled recal,
  reported plainly.

### 3.6 Phase 5 — selected application/collaborator demonstration

- **Deliverables:** rung-7 MVD demonstration on a full HSX
  vacuum+plasma cycle (anchoring, offset epochs, integrator
  correction, ρ-alarm — no radiation content needed); the stage-40
  outreach sequence for the tokamak lane executed **only after HY-G1**
  with the specified evidence pack (§5); W7-X benchmarking contact
  only after an HSX-side result exists (stage-40 monitor rule).
- **Reference instrument:** HSX machine-current anchor chain (as
  Phase 3); the demonstration *is* the reference validation.
- **Acceptance metrics:** the §3.6-claim demonstration: drift-tracking
  with honest uncertainty growth between anchors on real machine data;
  every accuracy statement in anchor-relative form.
- **Cost category:** machine-piggyback (own facility).
- **Time range:** mid-2027 onward (after HY-G1; overlaps P3 writing).
- **Dependencies:** Phases 1–3; stage-40 gating (approach-after-
  bench-proof for tokamak; no outreach before evidence exists).
- **Collaborator need:** optional — the dissertation-relevant claims
  are fully supportable from HSX alone (stage-40 fallback path §6);
  IPP-Prague/KFE conversations strengthen but do not gate.
- **Publication value:** P3/RSI (vector probe + in-machine hybrid
  demonstration, upside branch per folder-06 M29/M30); external
  validation pathway for P2's claims.
- **Stop/pivot rule:** if HSX access is lost entirely, folder-06's own
  reversal condition governs (stage-20(06) §11; OPT3 pivot) — this
  program's in-machine legs die with it and P2 stands on
  simulation + bench alone (degraded but publishable; C09 discipline:
  simulation is never called validation).

### 3.7 Phase 6 — reusable research module/simulation package and publication

- **Deliverables:** the T0 package frozen at the
  `03_SIMULATION_AND_VALIDATION_PLAN.md` §11 module boundary
  (model/schema/estimator/faults/scenarios/metrics/report/tests) with
  the rank-test regression binding intact; versioned release
  accompanying P2 (and P3 data-analysis reuse); optional short
  software/methods note only if the advisor judges it worth the
  review-cycle cost (default: the package is P2's artifact, not a
  separate paper).
- **Reference instrument:** none (the package's "reference" is its
  regression binding to `tools\observability_rank_tests.py` and its
  pre-registered scenario expectations).
- **Acceptance metrics:** HY-G0 metrics still passing at freeze; T-NI
  honesty test in the released test suite; placeholder watermarking
  active (no fake GaN numbers can enter silently — species-vector
  schema discipline).
- **Cost category:** desk.
- **Time range:** built continuously from Phase 0; **frozen at P2
  submission (~Q1–Q2 2027); release with P2 acceptance.** Post-freeze
  changes only via the frozen-science rule.
- **Dependencies:** Phase 0 build; P2 timeline (folder-06 M27/M31).
- **Collaborator need:** none. Disclosure honesty: any public code
  release passes folder-06's disclosure gates (06-G-C…G-G class) —
  the IP screen governs release timing, not this program.
- **Publication value:** P2 artifact + reproducibility strength; the
  reusable asset for any Phase-4/5 extension and for the group after
  the PhD.
- **Stop/pivot rule:** if maintenance effort competes with the P1/P2
  critical path, freeze earlier at whatever passes HY-G0 — scope is
  bounded by the §11 interface, and *feature growth is not a goal*
  (stage acceptance requirement: a realistic position in the PhD, not
  an open-ended software project).

### 3.8 Why the module deliverable is bounded (stage acceptance item)

The package has: a fixed interface (§11), a frozen scientific core
(measurement equations, freeze policy, species discipline,
pre-registered scenarios), a fixed metric set (M1–M8), a regression
anchor (rank tests), a freeze date tied to P2, and an explicit
earlier-freeze rule under time pressure. Its PhD position is: Phase-0
falsification instrument → Phase 2–3 analysis engine → P2 artifact →
dissertation-chapter material (folder-06 M37 hybrid chapter). Nothing
in the program rewards adding features after freeze. (Derived from
stage-30 plan §11 + folder-06 critical-path discipline.)

---

## 4. Publication map (integrates folder-06 routes; Proposed)

| Paper | Content from this program | Venue/route (folder-06) | Timing | Depends on |
|---|---|---|---|---|
| P1 | Phase-1 calibration + uncertainty budget content only (no hybrid claims) | SENSL resubmission (Route A) | resubmit ~Nov 2026 | 06-G1, WP-C, IP screen (06-M13) |
| P2 | Gap (a) theory + honesty-tested estimator + Phase-2/3 bench validation; §3.6 framing; **the two-paper-floor second paper** | folder-06 WP-D architecture paper | draft Jan 2027, submit Q1–Q2 2027 | Phase 0–2 (Phase 3 strengthens) |
| P3 | Vector probe + in-machine demonstration (gap (d) niche; gap (b) in-machine evidence if campaign data allows) | RSI instrument study (Route C; upside Mar 2027, realistic later per 06-M29/M30) | per campaign #2 outcome | Phases 3/5; folder-06 G3/G4 gates |
| P4 | FT-11/FT-12 results: first GaN Hall neutron dataset (C14 closure); compensation-closure claim if achieved (C21) | coauthored, collaborator-led | 2027–2028+, optional | Phase 4; never gates P1–P3 |
| (opt) | Software/methods note on the frozen package | advisor's call | with/after P2 | Phase 6 |

Novelty maintenance: FT-01 re-runs before each submission; the 2025
Kalman-fusion papers ([H001], [H002]) prove two active competitor
clusters on the C06 gap — the P2 window is real but not indefinite
(FM-17 residual risk; folder-06 already flags P2 novelty as a watch
item).

---

## 5. Collaboration timing (stage acceptance item: when, and with what evidence)

From Stage 40, unchanged in ranking, with the evidence pack now
specified (all asks remain PROPOSED, NOT SENT; no outreach occurs in
this mission):

| Lane | When to approach | What evidence to bring | What NOT to do |
|---|---|---|---|
| Stellarator/HSX (rank 1) | **Now — internal**; it is the existing UW-Madison collaboration; the August-2026 install target is folder-06 scheduled work | n/a (internal); share the T0 honesty results and anchor-shot request list as they mature | do not treat the low external-collaboration score as a weakness (it reflects the partner already exists) |
| Tokamak long-pulse — IPP CAS Prague, KFE/KSTAR (rank 2) | **Only after HY-G1** (bench anchored-hybrid repeatability), ideally with FT-08 vacuum-shot anchors from HSX | (1) stage-20 identifiability proof (Theorem 1 + feasibility matrix); (2) FT-02/T0 honesty-test results; (3) HY-G1 bench result with uncertainty budget; (4) a one-page note on the C06 gap framed as offered contribution (lead with the derivation, not a data request — they are the closest competitors, C05/H001 lines) | no approach before G1; no implied radiation commitment (T3 stays collaborator-led, stage-30 §9.4 — hard boundary) |
| Radiation facility / rad-effects group (Phase 4) | **Only after HY-G3**, with an FT-11 screening design in hand | (1) the FT-11 protocol (species-matched, foil dosimetry per C26, T–Φ decorrelation, sample sizes); (2) the C14 gap statement (first-ever GaN Hall-plate neutron dataset — a publishable contribution for *them*); (3) coupon-level ask first, never a full-system campaign | do not let the conversation put radiation on the HSX critical path; coauthored framing from the first conversation |
| W7-X (monitor), CERN/Cambridge (monitor) | Only after an HSX-side HY-G1/FT-08 result exists (W7-X); never as application targets (CERN C29 veto, Cambridge C28 veto) | benchmarking comparison for W7-X; technique citations already absorbed for the others | no outreach for vetoed lanes |

---

## 6. Accuracy/budget tiers

No vendor prices exist in the evidence base; the only sourced figures
are folder-06's internal BOM estimates (~$90 + ~$8, its
`FINAL_ACTION_PLAN.md` §1). Everything else: cost drivers + relative
categories (labeled estimates), per the stage rule.

### Tier 1 — minimum defensible (= MVD path; Phases 0–3 without the HA layer)

- **Content:** T0 package; existing GaN Hall + wound/PCB coil +
  folder-06 bench (field source, transfer-standard access,
  temperature logging); vacuum-shot anchors + zero-field epochs at
  HSX; augmented-state KF + ρ-alarm.
- **Cost drivers:** bench-days (marginal ~3–6 over folder-06's
  ≈19–29-day Tier-1 estimate); transfer-standard access; coil
  fabrication (PCB-class); engineering time for T0.
- **What accuracy is lost:** no gain tracking during quasi-static
  periods (CASE F — blind between anchors); no drift attribution
  (detection only, ρ-alarm); between-anchor common-mode drift
  unbounded by measurement (RR-13) — uncertainty grows at the
  anchor-cadence rate; absolute floor = anchor-chain accuracy (FM-15).
- **Evidence gap that forces an upgrade:** FT-03 showing HSX-feasible
  anchor cadence cannot meet the mapping-relevant requirement for
  drift rates that cannot be excluded (C14 makes the GaN rate
  Unknown — the bound comes from labeled analogs C12/C13).

### Tier 2 — balanced/recommended (= MVD + HA self-test layer; Phase 3 full)

- **Content:** Tier 1 + embedded calibration winding + traceable
  current reference + dual lock-in + triangle-closure test +
  soak-validated emulated-drift recovery (HY-G2/G3).
- **Cost drivers:** winding fabrication/characterization; reference
  electronics (current source, shunt readback, demodulation);
  long-run bench occupancy (weeks-scale soak); spectral-survey time
  at HSX.
- **What it buys over Tier 1:** continuous relative gain products
  `S_H·G_cal`, `K_C·G_cal` through quasi-static periods (CASE E);
  scheduled self-test during quiescence (the only coverage that
  exists there, CASE 8); instrumentation-path fault detection at zero
  marginal cost (closure residual).
- **What accuracy is still lost:** attribution (which channel
  drifted) — needs the witness tier; Hall offset between zero-field
  epochs (structurally, CASE E β-null — no tier fixes this);
  common-mode die+winding drift between anchors (C05 limitation
  class).
- **Evidence gap that forces an upgrade:** FT-07 requiring attribution
  or radiation-validated compensation for the target application; or
  the C36c/C21 claim being pursued at all (it needs Tier 3 by
  definition).
- **Recommendation basis (Derived):** this is the recommended ceiling
  for *first-author* work — every Tier-2 element is radiation-free,
  HSX-compatible, and P2/P3-relevant; and it carries its own descope
  rule back to Tier 1 (FT-06/FT-07) so the spend is falsification-
  gated, not faith-gated.

### Tier 3 — high-accuracy/collaborator-enabled (= + witness + Phase 4)

- **Content:** Tier 2 + material-diverse witness die (metallic-Hall
  class, [R071] basis) + FT-11 screening + FT-12 qualification with
  foil dosimetry; three-channel voting attribution (CASE G).
- **Cost drivers:** irradiation facility access + campaign logistics
  (activated-hardware handling, scheduling); multi-sample coupon
  fabrication; dosimetry; collaborator/coauthor effort; witness-die
  sourcing and characterization.
- **What it buys:** drift *attribution* (mechanism diversity); the
  measured GaN `f_S,s(Φ_s)` curves that convert every provisional
  cadence/threshold in the architecture from assumption to number
  (RR-01/RR-02 closure); the C21-first compensation-closure claim.
- **What is lost at the lower tiers:** exactly those items — Tier 1/2
  can *track and detect* but never attribute, and can never state a
  radiation-drift magnitude for GaN (C14) because no measurement
  exists.
- **Evidence gap that makes this tier necessary (if pursued):** C14 —
  it is closable only by species/spectrum-matched exposure; no
  cheaper substitute is scientifically valid (C16's ~14×
  cross-species error; C17 non-additivity).

---

## 7. Scope boundaries and kill criteria

### 7.1 Boundaries (binding)

- **B1 — No first-author radiation experiments.** Root `CLAUDE.md` +
  `MISSION.md` + stage-30 §9.4. Phase 4 is collaborator-led and
  coauthored; radiation appears in first-author work only as cited
  complement/outlook.
- **B2 — Radiation never enters the HSX critical path.** No HSX
  deliverable, P1/P2/P3 milestone, or HY-G0–G3 gate depends on any
  Phase-4 event (stage acceptance item).
- **B3 — No symmetric "mutual calibration" claim** in any manuscript
  or proposal without the Stage-20 conditions attached (feasibility
  verdict §1).
- **B4 — No absolute-accuracy claim** except in anchor-relative form
  (Theorem 1; FM-15).
- **B5 — No simulation described as experimental validation** (C09
  discipline; the field's own validation-strength inversion is the
  cautionary tale).
- **B6 — The folder-06 two-paper floor outranks every hybrid upside.**
  Any resource conflict resolves in favor of the P1→P2 critical path
  (folder-06 §2.2 cut order: cut CAMPAIGN-2/VECTOR/P3-class upside
  first, never BENCH-CAL/P1/P2).
- **B7 — No outreach before its gate** (§5); no contact, submission,
  or external write occurred in this mission.
- **B8 — Module scope frozen at the §11 boundary** (§3.8).

### 7.2 Kill criteria (each names its trigger and its pre-scripted action)

| ID | Trigger | Action (pre-scripted) |
|---|---|---|
| K1 | FT-01 finds gap (a) or (b) closed by a new publication | Drop that novelty claim; rebuild P2 around remaining gaps or pure instrumentation framing (C37); if all four C36 gaps close → stop the hybrid *research-claim* track entirely; HSX instrumentation work proceeds on its own merits |
| K2 | FT-02 fail (estimator flatters itself) | Stop all hardware planning until fixed — no spend passes HY-G0 with a dishonest instrument |
| K3 | FT-04 fail (offset anchor invalid) | Withdraw offset claims; re-derive budgets; HY-G1 blocked — no fallback exists (AC injection is structurally blind to offset) |
| K4 | FT-05 structural fail (reverse direction dead under ideal conditions) | C36b claim dies; collapse to C02-only architecture; P2 reframes as theory + incremental instrumentation |
| K5 | FT-06 fail or FT-07 fail | Descope HA→MVD (good outcome) / cut "better performance" claim to fault-detection + C02 roles; cut HA from all cost proposals |
| K6 | FT-07 **and** FT-10 both fail | Hybrid retains no earning value class → deploy Hall + coil as separate instruments; drop the fusion layer; report the retreat plainly |
| K7 | FT-08 fail (machine anchor unusable) | No absolute in-situ claim; reframe to relative/differential monitoring **before** any outreach (stage-40 gate logic) |
| K8 | 06-G5 direction gate (Jul 2027) fails or MVG checkpoint (06-M28) commits to floor-only | Hybrid program shrinks to whatever P2 has already banked; Phases 3+ stop; no sunk-cost continuation (folder-06 OPT3 pivot governs) |
| K9 | FT-11(c) or FT-12 fail (Phase 4, if entered) | Compensation claim falsified for this material set; retreat to detection + scheduled recal; report, do not spin (per FT-12 decision text) |
| K10 | HSX access lost entirely | In-machine legs die; P2 stands on simulation + bench alone; folder-06 reversal condition 3 governs the larger direction question |

---

## 8. Consistency statement

The program confirms, reorders, and narrows the user's sequence using
only Stage 20–50 results: every phase gate is an existing FT/HY-G/06-G
item; no new technical judgment is introduced. Radiation appears
exclusively in Phase 4 behind HY-G3 + collaborator agreement (never on
the HSX critical path). Every expensive step has a preceding cheaper
falsification gate (the FT ladder ordering is the program ordering).
Collaboration recommendations specify timing and evidence packs (§5).
The module deliverable is bounded (§3.8). No sibling file was modified;
no outreach occurred. Honest residuals: the GaN drift magnitude is
Unknown (C14) until Phase 4; the witness and reverse-direction
precedents are single-source ([R071]/C18, [H059]/C11); absence-based
novelty claims are bounded by this mission's documented search scope;
all cost categories except folder-06's own BOM figures are labeled
estimates.
