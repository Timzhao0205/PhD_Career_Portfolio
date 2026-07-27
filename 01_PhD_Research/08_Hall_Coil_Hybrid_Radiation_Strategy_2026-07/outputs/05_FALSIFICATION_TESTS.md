# 05 — Falsification tests, ordered cheapest to most expensive

Stage 50 (`50_limitations_comparison`). Produced and signed off by Fable 5
(xhigh). Source/claim/risk/CASE conventions as in
`05_LIMITATIONS_AND_FAILURE_MODES.md` (FM-xx references point there).
Labels: **Observed / Derived / Inferred / Proposed / Unknown** per
`CLAUDE.md`. Every test below is **Proposed**; its premises are cited.

## 0. Design principles

1. **Order = cost.** FT-01 costs a literature day; FT-12 costs a
   collaborator-led irradiation campaign. Tests are run in order; each has
   an explicit stop/pivot decision.
2. **The project can die cheaply.** FT-01 through FT-10 involve **zero
   radiation exposure** and collectively test every load-bearing
   assumption of the architecture. If any of them fails its threshold,
   the project stops or descopes *before* any radiation work — the
   stage-required property. FT-11/FT-12 are entered only if FT-01…FT-10
   pass and stage-30 gates G0–G3 hold, and they remain collaborator-led
   (stage-30 §9.4: no HSX deliverable depends on them).
3. **Thresholds without fake precision.** Where the evidence base
   contains a number (C02 ppm/s class, C26 dosimetry C/E), thresholds
   use it. Where the true magnitude is Unknown (all GaN radiation drift,
   C14), thresholds are defined *relative* — against the T0-predicted
   uncertainty, the bench-measured noise floor, or a deliberately
   emulated drift — never against an invented absolute number.
4. Falsifying a *component* hypothesis descopes that layer (per the
   stage-30 stop rules); falsifying a *structural* hypothesis (FT-02,
   FT-03, FT-05) stops or reframes the project.

Cost classes are order-of-magnitude labels (labeled estimates; no vendor
prices exist in the evidence base): desk < simulation < bench-day <
bench-soak < machine-piggyback < irradiation campaign.

---

## FT-01 — Prior-art kill search (desk; cheapest)

- **Hypothesis at risk:** "The narrowest defensible contribution
  (`05_LIMITATIONS_AND_FAILURE_MODES.md` §3.6) is still open: no
  publication jointly proves Hall+coil gain/offset/state identifiability
  (C36a), demonstrates coil-derived Hall-drift tracking in a fusion or
  radiation environment (C36b), demonstrates in-situ material-diverse
  Hall recalibration (C36c), or applies Hall+coil to stellarator mapping
  (C36d)."
- **Setup:** dedicated database/citation search on each gap, run
  *forward* from the known prior-art anchors ([H001]–[H004], [H021],
  [H059], [P003], [P057]) — who has cited them since 2025, and what did
  they add? Repeat before every manuscript/proposal submission.
- **Reference:** the mission's own documented search scope (10A–10D
  ledgers) as the baseline; any new hit is compared against the C36 gap
  definitions.
- **Metric:** count of publications closing any gap, with source IDs.
- **Pass/fail threshold:** pass = zero publications close a claimed gap.
  Fail = any gap demonstrably closed.
- **Confounders:** absence-of-evidence vs evidence-of-absence (search
  scope); near-miss papers that partially close a gap (judged per gap
  definition, recorded in the conflict ledger).
- **Decision:** fail on (a) or (b) → drop that novelty claim and rebuild
  the contribution around what remains (worst case: pure engineering/
  instrumentation paper, C37 framing); fail on (d) → the RSI-track
  application story needs repositioning; fail on all → stop the hybrid
  *research-claim* track entirely (the HSX instrumentation work proceeds
  on its own merits).
- **Evidence:** C01, C03, C06, C21, C29, C32, C36. Risk: FM-17.

## FT-02 — Estimator honesty test (simulation; T0)

- **Hypothesis at risk:** "Our estimator reports what the data cannot
  determine instead of inventing it" — i.e., the T0 package is a
  trustworthy instrument for every later decision (FM-18).
- **Setup:** run the stage-30 simulation plan's pre-registered scenarios,
  specifically the non-identifiable ones (CASE-A all-drift; CASE-F
  quasi-static) plus prior-sensitivity sweeps: re-run each scenario with
  deliberately wrong estimator priors (initialization offsets on
  `S_H, K_C, b_H`) and compare converged estimates.
- **Reference:** stage-20 rank tests (`tools\observability_rank_tests.py`)
  as the regression baseline — the simulator must reproduce the null
  spaces before any estimator is judged.
- **Metric:** (i) T-NI honesty metric: does the estimator freeze
  gauge-orbit states and inflate reported covariance on CASE-A/F
  scenarios? (ii) prior-dependence: shift of "converged" parameter
  estimates between prior sets, in units of the reported posterior sigma.
- **Pass/fail threshold:** pass = frozen/inflated behavior on every
  non-identifiable scenario AND prior-shifted runs agree within their
  reported uncertainty on identifiable scenarios. Fail = any run
  "recovers" a Theorem-1 orbit parameter with confident covariance, or
  identifiable-scenario results track the prior rather than the data.
- **Confounders:** regularization hiding as convergence; too-easy
  scenario noise levels; simulator sharing code (and bugs) with the
  estimator — mitigate with the independent rank-test regression.
- **Decision:** fail → **stop all hardware planning** until the
  estimator/simulator is fixed; a package that flatters itself would
  poison every subsequent gate (G0 entry condition).
- **Evidence:** stage-20 §5.3, §7; C09; stage-30 §6.1 binding rule.
  Risks: FM-18, RR-16.

## FT-03 — Anchor-cadence sufficiency under common-mode drift (simulation; T0)

- **Hypothesis at risk:** "Realistic anchor cadence bounds the
  common-mode blind spot to an acceptable uncertainty" (FM-01; the MVD's
  central accuracy claim).
- **Setup:** pre-registered no-alarm scenario S8: inject synthetic
  common-mode gain drift (both `S_H` and `K_C` scaled together) between
  anchor epochs at a *swept range* of drift rates (magnitude is Unknown
  for GaN, C14 — so sweep, do not assume); anchor epochs at the cadence
  HSX operations actually permit (vacuum shots per run day, zero-field
  epochs per shot cycle).
- **Reference:** truth model of the simulation plan; anchor cadence from
  real HSX operational patterns (logged shot schedules).
- **Metric:** (i) confirmation that the ρ-alarm stays silent (the
  pre-registered *expected failure* — honesty check); (ii) maximum
  absolute field error accumulated between anchors as a function of
  drift rate; (iii) the drift rate at which between-anchor error exceeds
  the science requirement of the target application (error-field-
  relevant accuracy for the stellarator lane; requirement documented at
  T0 from P013/P016-class inputs, not invented).
- **Pass/fail threshold:** pass = the science requirement is met for all
  drift rates up to the *worst documented analog* in the ledger
  (InSb/graphene campaign-scale drift classes, C12/C13, used as a
  labeled bounding analog, not as GaN data). Fail = requirement violated
  at drift rates that cannot be excluded for GaN.
- **Confounders:** the bounding-analog choice itself (species and
  material mismatch — labeled Inferred); optimistic anchor-accuracy
  assumptions (must use FT-08-measured values once available).
- **Decision:** fail → MVD alone is insufficient: either raise anchor
  cadence (operational cost), add the HA winding layer (Option B), or
  add the witness channel (Option D) — and if none of those closes it in
  re-simulation, the long-duration value claim is falsified and the
  project descopes to short-window relative measurements.
- **Evidence:** Theorem 1; CASE A; RR-13; C12/C13 (bounding analogs
  only). Risks: FM-01, FM-15.

## FT-04 — Zero-field/flip offset-anchor validity (bench-day)

- **Hypothesis at risk:** "Zero-field epochs recover `b_H` (and `b_C`)
  at the accuracy the architecture books for them" (FM-03; CASE C2's
  full-rank result depends on it).
- **Setup:** bench mu-metal/compensated zero-field environment; repeated
  offset reads across thermal excursions; 180°-flip protocol (rotating
  the head reverses the field term but not the electrical offset);
  deliberate small ambient contamination to measure sensitivity to an
  imperfect zero.
- **Reference:** fluxgate-class ambient audit of the "zero" (the
  fluxgate's one job in this program — comparison CSV row), plus the
  traceable transfer standard for the field term.
- **Metric:** repeatability (SD) of `b̂_H` across ≥10 read cycles;
  flip-consistency residual; measured error per unit of uncompensated
  ambient field.
- **Pass/fail threshold:** pass = offset repeatability at or below the
  T0-predicted offset uncertainty AND flip residual consistent with the
  noise model. Fail = repeatability worse than prediction with cause
  unfound, or flip test exposes a systematic (e.g., orientation-
  dependent thermoelectrics).
- **Confounders:** thermal transients during flips; remanent
  magnetization of fixtures; time-correlated 1/f noise mimicking drift.
- **Decision:** fail → the offset half of the calibration story is
  unsupported; since AC injection can never supply offset (CASE E),
  there is no fallback — the architecture's offset claims must be
  withdrawn and every downstream accuracy budget re-derived (this also
  degrades the stellarator-mapping value case). G1 blocker.
- **Evidence:** C07; H034; H035; CASE C2; RR-04, RR-24. Risk: FM-03.

## FT-05 — Coil-referenced Hall-gain recovery (bench-days)

- **Hypothesis at risk:** "A trusted coil chain + field excursions can
  identify Hall gain in situ" — the CASE-B reverse direction, the
  mission's most-wanted capability (C36b), demonstrated once, non-fusion
  ([H059], C11).
- **Setup:** Helmholtz/driven magnet delivering ramp+flat-top waveforms
  with ≥2 distinct dB/dt values and ≥2 field levels; coil chain
  pre-calibrated against the transfer standard; Hall gain deliberately
  "mis-set" in software by known factors (emulated drift); recover
  `Ŝ_H` by the CASE-B regression; separately, run the CASE-D two-channel
  anchor regression and the CASE-I integrator identification.
- **Reference:** NMR-class/traceable transfer standard ([H041], [H042],
  [H064]) as ground truth for the field; precision current
  measurement for the drive.
- **Metric:** relative error of recovered `Ŝ_H` vs the emulated truth;
  its scaling with excursion size `Σ(ΔB−ΔB̄)²` (must follow the stage-20
  Fisher prediction); CASE-I: recovery of `{x_I(0), g, m, τ_L}` under
  rich dB/dt and demonstration of the g-vs-m confound under constant
  ramp (a *predicted failure* that must appear).
- **Pass/fail threshold:** pass = recovered gains within the
  Fisher-predicted confidence interval across ≥3 repetitions AND the
  predicted ramp-degeneracy appears as predicted. Fail = errors exceed
  prediction with cause unfound, or the degeneracy does not behave as
  derived (which would indict the stage-20 model itself).
- **Confounders:** coil-chain calibration error mapping 1:1 into `Ŝ_H`
  (δS_H/S_H ≈ −δ(ΔB)/ΔB — measure the chain first); temperature drift
  during runs (log T; α_S characterization is a T1 deliverable);
  misalignment cosθ_m (fixture-controlled).
- **Decision:** fail structurally → the reverse-calibration direction is
  falsified in practice even under ideal bench conditions: the
  architecture collapses to the already-proven Hall→coil direction
  (C02), the C36b novelty claim dies, and the project reframes as
  incremental instrumentation. Fail marginally → revise SNR/window
  budgets and re-run FT-03 with measured values.
- **Evidence:** CASE B/D/I; C04, C11; H059. Risks: FM-02, FM-06, FM-08.

## FT-06 — Embedded winding: orthogonality, closure, self-heating (bench-days to weeks)

- **Hypothesis at risk:** "The HA tier's calibration winding delivers
  continuous gain products without polluting the measurement" (FM-11;
  stage-30 Option B layer).
- **Setup:** prototype head with cal winding; spectral survey of the
  bench (and later machine) environment; lock-in recovery of
  `π_H = S_H·G_cal` and `π_C = K_C·G_cal` under (i) clean injection,
  (ii) deliberately collided injection (interferer at `f_inj`),
  (iii) PRBS/hopped injection; triangle-closure residual
  `ε_Δ = π_H/π_C − ρ_HC` logged throughout; winding drive stepped
  through amplitudes to measure die heating `ΔT_die(I_rms²)`.
- **Reference:** transfer-standard field for absolute cross-check;
  independent die-temperature sensor for the heating inequality.
- **Metric:** lock-in variance vs the stage-30 §5.2 formula; collision
  detector's catch rate on (ii); closure-residual stability over a
  multi-day soak; measured `|α_S|·R_th·R_cal·I_rms²` against the target
  gain resolution `δ_S`.
- **Pass/fail threshold:** pass = gain-product tracking at the
  T0-required resolution with the heating term ≪ δ_S and 100 % collision
  detection on engineered collisions. Fail = injected-reference
  stability cannot beat the drift resolution target (stage-30 G2/G3 stop
  rule), heating ceiling binds below usable SNR, or collisions pass
  undetected.
- **Confounders:** bench EMI differing from machine EMI (why FT-10
  exists); `G_cal` temperature coefficient conflated with `S_H`
  temperature coefficient (separate by independent T logging);
  mutual-inductance contamination of the coil's field path (notch
  verification).
- **Decision:** fail → **descope to MVD** (drop the winding layer,
  anchor-only architecture) — an explicitly planned good outcome, not a
  project failure; the quasi-static gain-tracking claim (CASE-F remedy)
  is then withdrawn.
- **Evidence:** CASE E/E-collide; C05, C08, C19, C30; stage-30 §5.
  Risks: FM-11, RR-12, RR-20.

## FT-07 — Drift race: hybrid tracking vs scheduled recalibration alone (bench-soak, weeks)

- **Hypothesis at risk:** "The hybrid's continuous tracking measurably
  beats the *simpler* alternative — a single Hall channel with periodic
  recalibration" (the stage-required measurable-advantage condition;
  counterexample discipline of §4, FM-16).
- **Setup:** two identical Hall channels under the same emulated drift
  program (software-injected gain/offset walks + real thermal cycling):
  channel A runs the full hybrid stack (coil + winding + estimator);
  channel B gets only scheduled recalibrations at realistic epochs.
  Multi-week soak.
- **Reference:** the emulated drift program is ground truth; transfer
  standard at each scheduled recal.
- **Metric:** time-resolved field/gain error of A vs B; specifically the
  *between-recal* interval where A's continuous tracking should win.
- **Pass/fail threshold:** pass = A's error is lower than B's by a
  margin exceeding A's added uncertainty contributions, over the drift
  classes swept in FT-03. Fail = B matches A within uncertainty — the
  hybrid layer is not earning its complexity for slow drift.
- **Confounders:** emulated-drift realism (magnitudes Unknown for GaN —
  sweep classes, label the limitation); shared-environment correlations
  between A and B (deliberate, since both see the same truth).
- **Decision:** fail → the "better measurement performance" value class
  (limitations §3.1) is falsified for slow drift; the hybrid survives
  only on its fault-detection value (§3.3) and fast/long-pulse coil
  correction (C02) — report exactly that, and cut the HA tier from any
  cost proposal. This is the cheapest honest exit from over-claiming.
- **Evidence:** DECISION_FRAMEWORK.md veto ("no credible advantage over
  a simpler single-sensor solution"); C05 (the JET RHP line achieved
  0.07 %-class stability with same-die self-test + scheduled practice).
  Risks: FM-16, FM-17.

## FT-08 — Machine-current anchor on real vacuum shots (machine-piggyback; HSX)

- **Hypothesis at risk:** "CASE D works on a real machine at useful
  accuracy: logged coil currents + validated vacuum field model identify
  all four channel parameters per epoch" (FM-10; the MVD's absolute
  anchor).
- **Setup:** piggyback on HSX vacuum shots (no dedicated machine time
  initially): head installed at a mapped location; ≥2 field levels and
  ramp+flat-top waveforms; per-epoch least squares for
  `{S_H, b_H, K_C, b_C}`; residual-vs-model archive per epoch.
- **Reference:** HSX coil-current logs + vacuum field model (validated
  by flux-surface mapping practice, C32/[P013]-class); bench transfer
  standard before install and at the next vent as the independent leg.
- **Metric:** anchor repeatability across ≥3 epochs (SD of each
  parameter); residual structure vs the model (white vs waveform-shaped);
  closure between bench calibration and first in-machine anchor.
- **Pass/fail threshold:** pass = epoch-to-epoch repeatability
  consistent with the T0-predicted anchor uncertainty AND bench→machine
  closure within the combined budget (position/misalignment terms
  included). Fail = waveform-shaped residuals (model error), or
  bench→machine discrepancy exceeding budget with cause unfound.
- **Confounders:** sensor position/alignment error (∇G·δr — surveyed
  mount); Earth/ambient field (measured, FT-04 kit); timing skew into
  `Ḃ_ref` (shared clock); remanent fields from prior operation.
- **Decision:** fail → the absolute-anchoring premise of the whole
  architecture is unsupported at the only accessible machine; the
  project cannot claim absolute calibration in situ (Theorem 1 leaves no
  alternative in-pair) and reduces to relative/differential monitoring —
  a fundamental reframing that must precede any collaboration outreach
  (stage-40 gate logic).
- **Evidence:** CASE D/D-flat; C08 ([H040] machine-scale precedent),
  C32; P013, P016. Risks: FM-10, RR-21.

## FT-09 — Repeated-waveform reproducibility floor (machine-piggyback; HSX)

- **Hypothesis at risk:** "Standard vacuum ramps are reproducible enough
  that shot-to-shot regression tracks gain drift" (CASE 6; the Option-E
  layer and the radiation-trend tool `S_H(t)/S_H(0)`).
- **Setup:** repeated nominally identical vacuum waveforms across run
  days; channel-by-channel shot-k-vs-shot-0 regression; machine current
  logs used to *verify* reproducibility independently.
- **Reference:** coil-current logs (the reproducibility witness); FT-08
  anchors bracketing the sequence.
- **Metric:** distribution of recovered gain ratios `S_H^k/S_H^0`,
  `K_C^k/K_C^0` over a period with no plausible real drift; this
  distribution's width *is* the method's detection floor.
- **Pass/fail threshold:** pass = detection floor at or below the drift
  resolution the FT-03 sweep says matters. Fail = floor above it —
  waveform irreproducibility masks any drift of interest.
- **Confounders:** genuine slow drift during the baseline period
  (bracketing anchors separate this); machine configuration changes
  between run days (logged); temperature differences (T telemetry).
- **Decision:** fail → drop the repeated-waveform layer from the
  architecture (it costs nothing to remove) and rely on anchors +
  injection; note the loss in the uncertainty budget between anchors.
- **Evidence:** CASE 6 algebra (stage-20 §5.6); C05 (JET's >19,000-pulse
  operational cousin). Risk: FM-02 tracking leg.

## FT-10 — Plasma-operations EMI and collision robustness (machine-piggyback; HSX plasma shots)

- **Hypothesis at risk:** "The tracking layers survive the real EM
  environment: injection stays orthogonal, the ρ-alarm's false-positive
  rate is usable, and Hall EMI susceptibility does not dominate"
  (FM-11/FM-12 EMI legs; C30's documented Hall EMI susceptibility is an
  unfavorable prior from an adjacent domain, labeled Inferred here).
- **Setup:** run the full head + tracking stack during ordinary plasma
  operation (data-only, no control role); spectral survey during shots;
  injection on/off blocks; log ρ-alarm events against shot logs.
- **Reference:** shot-synchronized machine logs; the FT-06 bench
  baselines as the quiet-environment control.
- **Metric:** injection-schedule tracking validity (collision detector
  rate during shots); ρ-alarm false-positive rate per shot; excess Hall/
  coil noise during shots vs bench.
- **Pass/fail threshold:** pass = collision-free frequency plan exists
  (possibly after re-placement) and false-positive rate low enough that
  an alarm is actionable (pre-registered rate target from T0). Fail = no
  usable spectral window exists, or alarms are so frequent they carry no
  information.
- **Confounders:** shot-type dependence of EMI; aliasing from the DAQ;
  gain drift genuinely occurring during the test (bracketing anchors).
- **Decision:** fail on injection → HA tier is machine-incompatible at
  HSX: descope to MVD (as FT-06 fail); fail on ρ-alarm → the
  fault-detection value class (§3.3) — the architecture's cheapest
  claimed value — is falsified in the real environment; with FT-07 also
  failed, the hybrid would retain only the C02 coil-correction role, and
  the honest conclusion is "deploy a Hall channel + coil as separate
  instruments, skip the fusion layer."
- **Evidence:** C30 (P021, P022, P028); CASE E-collide; RR-20.
  Risks: FM-11, FM-12.

## FT-11 — Species-matched component screening (irradiation facility; collaborator-led; expensive)

- **Hypothesis at risk:** three at once, all currently Unknown:
  (i) "GaN Hall-plate drift under the target neutron spectrum is large
  enough to need in-situ tracking" (if it is *below* the FT-09/FT-06
  detection floor, the radiation-compensation story is unnecessary);
  (ii) "the metallic-Hall witness is radiation-null as claimed"
  (C18's single unreplicated source, RR-18); (iii) "winding/coil
  materials hold `G_cal`/`A_eff` under dose" (evidence-free either way,
  RR-08).
- **Setup (per stage-30 rung 5; only after G0–G3 pass):** multi-sample
  coupon irradiation of GaN dies, witness material, and wound/PCB coil
  coupons at a species/spectrum-matched facility; co-located activation-
  foil dosimetry (two-step protocol: reference-field calibration then
  in-situ validation); temperature logged and *deliberately decorrelated*
  from fluence accumulation (CASE J-decorr schedule); bias states
  recorded; pre/post plus, where possible, in-situ powered measurement.
- **Reference:** foil dosimetry (C/E = 1.05 ± 0.13 class at a 14 MeV
  reference field, 8 % in-machine validation, C26); pre/post traceable
  bench calibration; unirradiated control samples from the same lots.
- **Metric:** `f_S,s(Φ_s)` and `f_b,s(Φ_s)` per material with
  uncertainty and sample spread; witness-material sensitivity change;
  coil-coupon geometry/inductance/insulation-resistance change;
  annealing behavior on a controlled post-exposure temperature ramp.
- **Pass/fail threshold:** this test cannot "fail" as a project — it
  *decides*: (a) GaN drift below detection floor → in-situ radiation
  recal is unnecessary; simplify to MVD + scheduled recal (stage-30 stop
  rule — explicitly a good outcome); (b) drift measurable and monotonic
  → compensation architecture proceeds to FT-12 with real parameters;
  (c) drift large, non-monotonic, and unattributable, or witness fails
  replication → hybrid compensation falsified for this material set;
  pivot to material change (Option F/D) or accept scheduled-recal-only
  operation.
- **Confounders:** surrogate-facility flux gap (3–5 orders below target
  rates, [R074]) leaving dose-rate/ELDRS effects unprobed — report the
  flux-gap factor with every number (RR-19); lot-to-lot spread
  (multi-sample design); T–D history correlation (engineered schedule);
  species mismatch (this is the one place money buys the right spectrum —
  a wrong-species campaign is worse than none, C16's ~14× lesson).
- **Decision:** as per the three-way threshold above. In every branch,
  the user's first-author HSX work is unaffected (stage-30 §9.4
  decoupling; MISSION.md boundary).
- **Evidence:** C12–C18, C22, C24, C26; R071, R074, R042.
  Risks: FM-02, FM-05, FM-06, RR-18, RR-19.

## FT-12 — Representative-spectrum / mixed-field qualification (most expensive; collaborator-led)

- **Hypothesis at risk:** "Per-species screening results compose into
  the real mixed neutron+gamma environment" — documented to be false in
  direction-dependent ways for other device classes (C17: GaN HEMT
  leakage sub-additive vs cascode threshold super-additive; bipolar
  op-amp offset synergistic) and untested for any Hall device.
- **Setup:** full compensated head (die + coil + winding + witness +
  electronics siting per stage-30 §4.3) in a representative mixed-field
  exposure with the complete anchor/tracking protocol running in situ;
  dosimetry per C26; the FOCS/JET-DTE2 campaign is the operational
  template of what this must produce (C20): in-service cross-validation
  against an independent reference through the exposure.
- **Reference:** an independent, material-diverse field reference at the
  head location plus the machine/facility field model; pre/post
  traceable calibration.
- **Metric:** closed-loop compensation error — the difference between
  the compensated field estimate and the independent reference —
  tracked vs fluence; comparison of observed drift against the
  FT-11-built per-species composition.
- **Pass/fail threshold:** pass = compensation closes the loop within
  the stage-30 G5 target uncertainty *and* discrepancies from per-species
  composition are within the stated non-additivity allowance. Fail =
  compensated error exceeds target, or non-additivity invalidates the
  FT-11-derived model class.
- **Confounders:** everything FT-11 lists, plus RIEMF on all cabling in
  flux (zero-dB/dt segments budget it, C19), activation handling limits
  on post-test measurement access, and facility-schedule realities.
- **Decision:** pass → the radiation-compensation claim (§3.2) is, for
  the first time anywhere (C21), experimentally supported — publishable
  as the capstone of the collaborator-led track. Fail → the
  compensation claim is falsified at full-system level; the architecture
  retreats to detection-plus-scheduled-recal, and that retreat is
  reported, not spun.
- **Evidence:** C17, C19, C20, C21, C26. Risks: FM-05, FM-12, RR-17.

---

## Summary table (order = cost = execution order)

| ID | Cost class | Kills/decides | Radiation-free? |
|---|---|---|---|
| FT-01 | desk | novelty claims (FM-17) | yes |
| FT-02 | simulation | trust in every later gate (FM-18) | yes |
| FT-03 | simulation | MVD sufficiency vs common-mode blindness (FM-01) | yes |
| FT-04 | bench-day | offset-anchor validity (FM-03) | yes |
| FT-05 | bench-days | the reverse-calibration direction itself (C36b) | yes |
| FT-06 | bench-weeks | HA winding layer (FM-11) | yes |
| FT-07 | bench-soak | "measurable advantage over simpler" (FM-16/§3.1) | yes |
| FT-08 | machine-piggyback | absolute anchoring on a real machine (FM-10) | yes |
| FT-09 | machine-piggyback | repeated-waveform tracking layer | yes |
| FT-10 | machine-piggyback | EMI survival of tracking + alarms (FM-11/12) | yes |
| FT-11 | irradiation campaign | whether radiation compensation is even needed; witness replication; coil dose response | no (collaborator-led) |
| FT-12 | full qualification | the compensation claim at system level | no (collaborator-led) |

Stage-required property, restated: ten of twelve tests are radiation-free,
each with a stop/descope decision, and the two radiation tests are entered
only through gates G0–G3 with collaborator leadership — the project can be
stopped, descoped, or reframed at any rung **before** expensive radiation
work, and several branches (FT-06 fail, FT-07 fail, FT-11a) are explicitly
*good* outcomes that simplify the architecture rather than embarrass it.
