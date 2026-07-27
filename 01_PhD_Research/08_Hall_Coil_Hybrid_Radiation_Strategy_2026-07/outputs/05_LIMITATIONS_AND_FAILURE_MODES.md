# 05 — Limitations, failure modes, and the narrowest defensible contribution

Stage 50 (`50_limitations_comparison`). Produced and signed off by Fable 5
(xhigh). Source IDs (`Hxxx`, `Rxxx`, `Pxxx`) refer to
`outputs\01_SOURCE_LEDGER.csv`; claim IDs (`Cxx`) refer to
`outputs\01_EVIDENCE_MAP.csv`; risk IDs (`RR-xx`) refer to
`outputs\03_RADIATION_RISK_REGISTER.csv`; falsification-test IDs (`FT-xx`)
refer to `outputs\05_FALSIFICATION_TESTS.md`; CASE/§ references refer to
`outputs\02_OBSERVABILITY_AND_IDENTIFIABILITY.md`. Labels: **Observed /
Derived / Inferred / Proposed / Unknown** per `CLAUDE.md`.

This file is deliberately adversarial to the mission's own working
hypothesis. Its job is to state where the hybrid architecture breaks, what
that breakage looks like, and which claims survive.

---

## 1. Scope and method

Eighteen failure modes (FM-01…FM-18) cover every area the stage requires.
Each mode states cause, symptom, detectability, consequence, mitigation,
residual risk, and a test. Structural claims are **Derived** from stage 20;
radiation and hardware claims are **Observed** with source IDs; transfers
across species or domains are labeled **Inferred**; anything without
evidence is **Unknown**. Where a failure mode restates a stage-30 risk row,
the RR-xx ID is given and the content here adds the failure-analysis fields
rather than repeating the register.

Coverage map (stage-required area → failure mode): non-identifiable
simultaneous gain drift → FM-01; Hall sensitivity/offset/noise/
nonlinearity/cross-axis/temperature → FM-02, FM-03, FM-04; radiation
species/spectrum and device variability → FM-05; coil effective-area/gain/
phase/resonance/temperature/geometry → FM-06, FM-07; integrator → FM-08;
bandwidth overlap and timing → FM-09; common-mode field-model/reference
failure → FM-10; calibration winding aging/self-heating/EMI/ambient →
FM-11; shielding/placement/cabling/readout radiation → FM-12; dynamic
range/saturation → FM-13; radiation-vs-temperature/annealing separation →
FM-14; traceability and uncertainty floor → FM-15; packaging/
manufacturability/maintenance/channel-count cost → FM-16; prior-art/novelty
→ FM-17; false confidence from estimator tuning/simulation → FM-18.

---

## 2. Failure-mode register

### FM-01 — Common-mode gain drift is structurally invisible (RR-13)

- **Cause (Derived):** any shared stressor (radiation, temperature,
  common supply/reference) that scales `S_H` and `K_C` by the same factor
  moves the system along the Theorem-1 gauge orbit (stage-20 §3, CASE A,
  rank 5/7). This is not a noise or SNR problem; no excitation whatsoever
  breaks it in-pair.
- **Symptom:** none. The data remain exactly consistent with a genuine
  field change of factor α. The differential-drift alarm `ρ = S_H/K_C`
  stays silent by construction.
- **Detectability:** zero between anchors. Caught only at a CASE-D
  machine-current anchor epoch, at a bench recalibration, or by a
  mechanism-diverse witness channel (CASE G attribution conditions).
- **Consequence:** silently mis-scaled absolute field for the whole
  inter-anchor interval; every downstream consumer (mapping result,
  drift-trend curve, any feedback use) inherits the error with no flag.
- **Mitigation:** anchor cadence sized to bound the exposure window;
  material-diverse witness at the top tier (Option D); reported
  uncertainty that *grows* between anchors (stage-30 §6.3.2) instead of a
  constant accuracy claim.
- **Residual risk:** irreducible in-pair. The residual equals whatever
  common-mode drift can accumulate within one anchor interval — and for
  GaN devices the drift rate itself is Unknown (C14), so the residual is
  currently unbounded by evidence.
- **Test:** FT-03 (simulation: pre-registered no-alarm scenario S8 —
  the architecture must *fail honestly*); FT-08 (anchor epochs on real
  vacuum shots). Evidence: C03; H021; stage-20 Theorem 1.

### FM-02 — Hall sensitivity drift: radiation and temperature (RR-01, RR-02)

- **Cause (Observed for other materials / Unknown for GaN):**
  displacement damage and carrier removal (InSb mobility −75…−90 % at
  6.6–7.0e17 fast n/cm², sample ~200 °C, [R003], C13); transmutation
  under thermal-inclusive spectra — permanent, non-annealable at service
  temperature ([R001], [R002], [R025], C12, C24); TID two-regime response
  in the GaN family ([R024], C22); ordinary temperature coefficient
  `α_S·ΔT`.
- **Symptom:** gradual gain change; rising device resistance `R_H`;
  rising noise floor. Under thermal-inclusive spectra, drift continues
  without saturation as transmutants accumulate.
- **Detectability:** relative gain drift is in-situ measurable (lock-in
  products, anchor ratios, repeated waveforms — CASE E/6, stage-30 §7);
  `R_H` is a reference-free in-situ witness. Mechanism attribution is
  *not* in-situ detectable (FM-14).
- **Consequence:** absolute field error growing with fluence; if
  uncompensated, the Hall channel poisons the very coil-drift correction
  (C02 direction) that motivates the hybrid.
- **Mitigation:** layered anchors (stage-30 Option H); species-matched
  screening before any environment commitment (rung 5); `R_H` and noise
  telemetry as early-warning channels.
- **Residual risk:** **no GaN/AlGaN Hall-plate neutron dataset exists
  (C14)** — magnitude, shape, and even sign of `f_S(Φ)` are Unknown;
  every tracking cadence is provisional until screening data exists.
- **Test:** FT-05, FT-06, FT-09 (drift-tracking machinery works on
  emulated drift); FT-11 (species-matched screening). Evidence: C12–C15,
  C22, C24.

### FM-03 — Hall offset drift and the residual spinning floor (RR-04, RR-24)

- **Cause (Observed):** current spinning leaves a residual offset floor
  that itself drifts ([H034], [H035], C07); TID trapped charge shifts
  offset with partial annealing ([R024], C22); thermoelectric EMFs at
  contacts.
- **Symptom:** a DC error observationally identical to a static field
  shift (Theorem-1 β-orbit) — no in-pair signature at all.
- **Detectability:** zero-field (or independently known-field) epochs
  only. AC injection from the embedded winding is *structurally blind*
  to offset (CASE E; stage-30 §5.1). This is the most commonly
  mis-claimed capability in hybrid design documents.
- **Consequence:** DC field bias; if the zero-field anchor itself is
  contaminated by remanent/ambient field, the mis-calibration is
  *replicated into all downstream data* (RR-24).
- **Mitigation:** per-shot-cycle zero-field reads; 180°-flip protocol
  (field term reverses, electrical offset does not); documented ambient
  audit at the sensor location.
- **Residual risk:** offset drift *between* epochs is unobserved by
  construction; in-vessel remanence may vary shot-to-shot.
- **Test:** FT-04 (flip/zero-field protocol repeatability); scenario S10
  (anneal-aware windows). Evidence: C07, C22.

### FM-04 — Hall noise growth, nonlinearity, and cross-axis/misalignment error

- **Cause:** radiation-induced noise increase (mechanism class Observed
  for irradiated Hall materials via `R_H` rise, [R003], [R043]);
  field-dependent sensitivity `S_H(B)` (nonlinearity); geometric
  misalignment `θ_m` and intrinsic cross-axis response ([H047]).
- **Symptom:** SNR loss shrinking every regression's information content
  (stage-20 Fisher variances); gain estimated at one field level failing
  to transfer to another; anchor comparisons biased by `cos θ_m`.
- **Detectability:** noise — yes, in situ (quiescent-period PSD
  monitoring). Nonlinearity — only with multi-level anchors (CASE D at
  ≥2 field levels; single-level anchoring cannot see it). Misalignment —
  **not separable from gain with any single-axis reference** (stage-20
  §2.4); requires multi-axis bench characterization.
- **Consequence:** calibration transfer error across field levels;
  a hidden `cos θ_m` factor masquerading as a sensitivity change after
  any remount; noise-driven widening of all drift-detection thresholds.
- **Mitigation:** Tier-1 bench linearity and cross-axis map before
  install; multi-level vacuum-shot anchors; PSD trend telemetry;
  mechanical registration of the head.
- **Residual risk:** in-situ misalignment stays a budget term, not an
  estimated state; nonlinearity drift under irradiation is Unknown for
  all Hall materials in the ledger.
- **Test:** FT-05 (bench multi-level gain recovery), FT-08 (multi-level
  machine anchors). Evidence: H047; C13 (noise/mobility mechanism);
  stage-20 §2.4, §6.3.

### FM-05 — Radiation species/spectrum mismatch and device-to-device variability (RR-16, RR-17, RR-19)

- **Cause (Observed as mechanism):** planning or compensation built on
  wrong-species data. Cross-species scaling demonstrably fails at the
  ~14× level even within III-V materials (proton→gamma NIEL
  underprediction, [R042], C16); spectrum matters as much as species
  (InSb: degrades under thermal-inclusive fission spectrum, stable under
  purely fast at comparable fluence — C12); mixed neutron+gamma effects
  are non-additive with structure-dependent direction (C17);
  device-to-device spread is documented for irradiated thin films
  (9-sample spread within R003's campaign, doping-dependent direction of
  carrier-density change, C13) and for COTS lots (RR-22).
- **Symptom:** none until too late — the failure appears as compensation
  models that mispredict observed drift in the target environment, or as
  qualification results that do not transfer between facilities.
- **Detectability:** only via species/spectrum-matched screening with
  co-located dosimetry (foil two-step protocol, C/E = 1.05 ± 0.13 class,
  C26) and multi-sample statistics.
- **Consequence:** mis-sized design margins (documented ~14× error
  class); a compensation architecture tuned on protons or gamma that is
  simply wrong under D-D/D-T neutrons; single-device calibration curves
  that do not represent the installed population.
- **Mitigation:** species-vector enforcement in the simulation schema
  (refuses scalar fluence, stage-30); no per-species curve summation
  without a labeled mechanism argument; screening sample sizes set for
  spread estimation, not single-coupon demonstration.
- **Residual risk:** surrogate-facility flux can sit 3–5 orders below
  the target environment ([R074]) leaving dose-rate effects (ELDRS
  class, [R047]) unprobed; no Hall-device mixed-field dataset exists.
- **Test:** FT-11 (species-matched screening design), FT-12
  (representative-spectrum qualification); schema unit tests at T0.
  Evidence: C12, C16, C17, C26.

### FM-06 — Coil effective-area/gain/geometry/temperature change (RR-08)

- **Cause:** thermal expansion of the former; radiation-induced
  dimensional/insulation change; readout-gain drift. **No measurement of
  radiation-induced effective-area drift exists for any coil**
  (radiation-review gap; metrology baseline [R069], [R070]).
- **Symptom:** AC-band scale change; a shift in `ρ = S_H/K_C` that the
  pair cannot attribute (FM-01 mirror: differential this time, so the
  alarm fires but points at no one).
- **Detectability:** per-epoch CASE-D re-solve of `K_C`; the coil-side
  lock-in product `π_C = K_C·G_cal`; no in-situ separation of `A_eff`
  from readout gain.
- **Consequence:** mis-scaled dB/dt; critically, it corrupts the
  coil-as-reference role in the coil→Hall gain direction (CASE B):
  a coil-chain scale error maps 1:1 into the inferred Hall gain
  (`δS_H/S_H ≈ −δ(ΔB)/ΔB`, stage-20 §5.2) — the hybrid's most-wanted
  capability silently inherits the coil's own drift.
- **Mitigation:** ceramic formers ([R062] tolerance basis); anchor
  triangulation; explicit between-anchor drift allowance in the budget.
- **Residual risk:** dose-to-geometry response is evidence-free in both
  directions; assuming stability and assuming drift are both
  unsupported. A rung-6 campaign would be the first-ever measurement.
- **Test:** rung-4 thermal cycling; FT-08 (per-epoch `K_C` history);
  rung 6. Evidence: C19 context; R069, R070.

### FM-07 — Coil phase/resonance/bandwidth change

- **Cause:** L/R corner shift with temperature/aging, cable capacitance
  change, mechanical resonance shift, anti-alias filter drift.
- **Symptom:** frequency-dependent gain/phase error; growing overlap-band
  residuals against the Hall channel; distorted fast transients.
- **Detectability:** only with overlap-band content — injected tone near
  the corner or natural broadband transients (CASE H-broad); near-DC
  operation verifies nothing about the coil transfer function
  (CASE H-narrow collapse).
- **Consequence:** fast-transient reconstruction and Hall-dynamics
  identification (case 9) both degrade; phase error is indistinguishable
  from timing skew with narrowband excitation.
- **Mitigation:** scheduled injection sweeps near the band edges;
  shared-clock digitization; bench transfer-function baseline.
- **Residual risk:** out-of-band changes are invisible until content
  arrives there; resonance drift between sweeps unmonitored.
- **Test:** FT-06 (injection sweep); fault injection F12 (skew).
  Evidence: stage-20 case 9; H053.

### FM-08 — Integrator offset, leakage, saturation, initial condition (RR-10)

- **Cause (Observed):** input-offset drift `m(t)` — the dominant
  long-pulse error ([H025], [H004], C02); leak `τ_L`; rail saturation;
  unknown start flux `x_I(0)`.
- **Symptom:** ramp error growing with pulse length; droop toward zero;
  clipped output during fast events.
- **Detectability:** good — this is the hardware-proven correction
  direction (Hall-anchored Kalman filtering reduced drift from
  59.9–120 ppm/s to 0.02–0.08 ppm/s on the CERN bench, [H004], [H005];
  system-level at ITER OVSS, [P003], C02); zero-dB/dt segments read the
  additive terms directly.
- **Consequence:** unbounded DC error in coil-only operation; in the
  hybrid, the residual trap is structural: under constant dB/dt, coil
  gain and integrator drift merge (`g·r + m`, CASE I-ramp) — a ramp-only
  waveform cannot separate them.
- **Mitigation:** chopper-stabilized/remote-sited integrator
  electronics; waveforms containing ≥2 distinct dB/dt values; augmented
  bias-state estimator.
- **Residual risk:** radiation response of integrator/timing electronics
  is the thinnest evidence area in the ledger (single space-context
  source [R067], RR-11).
- **Test:** FT-05 (bench), scenario S11 (I vs I-ramp), rungs 2/4.
  Evidence: C02; H025–H027.

### FM-09 — Bandwidth overlap gaps and timing misalignment (RR-11, RR-23)

- **Cause:** transient content above the Hall pole (single-channel-only
  band); sampling skew `δt` between channels; oscillator shift under
  radiation ([R067]).
- **Symptom:** no cross-channel redundancy for fast content; phase-slope
  errors in the overlap band; delay confounded with gain phase under
  narrowband excitation (stage-20 case 9).
- **Detectability:** overlap-band cross-spectral monitoring with
  injected or natural broadband content; near-DC operation cannot verify
  Hall bandwidth at all (CASE H-narrow: pole singular value collapses
  ×~10 a decade below the pole).
- **Consequence:** faults and saturation above the Hall band are
  invisible (no witness channel); misaligned timing biases `Ḃ_ref` in
  anchor regressions and corrupts fused estimates.
- **Mitigation:** shared clock; injection placed near the Hall pole
  (identifies dynamics as a by-product, CASE H-broad); explicit skew
  budget in the anchor error chain.
- **Residual risk:** out-of-band content is forever single-channel — a
  physical limit of the pairing, not an engineering defect.
- **Test:** FT-06 (near-pole injection); fault injection F12.
  Evidence: stage-20 case 9; H053; R067.

### FM-10 — Common-mode field-model/reference failure (RR-21)

- **Cause:** the CASE-D anchor inherits every error of the machine
  current logs and vacuum field model: model applied during plasma
  (invalid by construction), coil-current measurement error (an
  ~1e-4-class relative field-accuracy design criterion is documented for
  LHD, [P016] — stage-70 correction of a W7-X misattribution; HSX's own
  current-log accuracy must be characterized, not assumed), position/
  alignment error through `∇G·δr`, machine configuration changes after
  the e-beam validation epoch ([P013]).
- **Symptom:** anchor-epoch residuals versus the model grow or become
  waveform-shaped; or — the dangerous case — nothing, if the model error
  is smooth and absorbed into the estimated gains.
- **Detectability:** partial: residual-vs-model monitoring across
  multiple field levels and waveforms; cross-check against an
  independent bench transfer standard at vents. A model bias common to
  all anchor epochs is *not* detectable from inside the system — it is
  the reference-level instance of FM-01.
- **Consequence:** the entire absolute calibration chain is biased
  identically at every anchor; all four "absolutely identified"
  parameters (CASE D) carry the bias; the system is precise and wrong.
- **Mitigation:** anchor only in vacuum shots (procedural, RR-21);
  ≥2 field levels + ramp/flat-top per epoch; periodic traceable bench
  recalibration ([H041], [H042], [H064]) as the independent leg;
  residual archive per epoch (stage-30 ledger S5).
- **Residual risk:** anchor cadence is hostage to machine operations;
  between model validations the model-drift term is an assumption.
- **Test:** FT-08 (residual structure on real vacuum shots); rung-7
  procedure validation. Evidence: C32; P013, P016; stage-20 case 4
  error budget.

### FM-11 — Calibration winding aging, self-heating, EMI, ambient-field separation (RR-12, RR-20)

- **Cause:** `G_cal` geometry/insulation aging (no dose-to-geometry data
  exists — same gap as FM-06); current-source drift; RIEMF coupling into
  the cal circuit ([R056] mechanism; Inferred transfer); winding
  self-heating `ΔT_die = R_th·R_cal·I_rms²` feeding the very `α_S·ΔT`
  term being monitored (stage-30 §5.3); spectral collision of the
  injection tone with ambient/EMI lines (Hall EMI susceptibility
  documented in adjacent contexts, [P021], [P022], [P028], C30).
- **Symptom:** apparent gain drift (only the products `S_H·G_cal`,
  `K_C·G_cal` are identifiable — CASE E); nonzero triangle-closure
  residual for measurement-path faults; silently corrupted gain products
  under spectral collision (rank deficiency returns, CASE E-collide).
- **Detectability:** the closure test `π_H/π_C ≡ ρ_HC` catches *path*
  faults continuously but — by construction — provides **no attribution**
  and cannot see slow common `G_cal` drift (stage-30 §5.5); anchor
  epochs re-solve `G_cal`; a collision detector verifies the demodulated
  output tracks the injection schedule.
- **Consequence:** false drift diagnosis (winding drift booked as Hall
  drift), or masked drift; self-heating biases the temperature term;
  a collided tone yields confident, wrong gain tracking.
- **Mitigation:** sense-at-winding current readback; guarded/twisted
  feeds; PRBS/hopped or toggled injection with schedule verification;
  pre-operation spectral survey; heating-ceiling inequality
  characterized on the bench; anchor triangulation as the winding's own
  reference (stage-30 §5.4).
- **Residual risk:** common-mode die+winding drift between anchors is
  invisible to self-test — the documented limitation class of the JET
  RHP same-die architecture (11.5 yr, SD ≈ 0.07 % record
  notwithstanding, [H003], [H007], C05).
- **Test:** FT-06 (spectral survey, closure, heating ceiling); fault
  injections F7/F8; FT-10 (in-machine EMI). Evidence: C05, C19, C30;
  CASE E/E-collide.

### FM-12 — Shielding, placement, cabling, and readout radiation (RR-05, RR-06, RR-07, RR-09)

- **Cause (Observed mechanisms):** RIEMF in mineral-insulated cables —
  additive, flux-correlated EMF (five-paper cluster [R056]–[R060], C19;
  Cu-core activation avoidable via steel core, [R048], [R049]); op-amp
  offset/bias-current degradation with neutron+gamma synergy ([R046]);
  ELDRS dose-rate sensitivity ([R047]); millisecond single-event
  transients ([R052]); ADC TID/SEU ([R051]); insulation and mechanical
  faults under combined radiation+EM stress (JET in-vessel Mirnov
  precedent, [R066]).
- **Symptom:** flux-correlated additive errors on the coil chain;
  electronics drift indistinguishable from sensor drift if the chain is
  unmonitored; ms-scale data-corruption bursts.
- **Detectability:** zero-dB/dt segments expose additive coil-chain
  terms; channel-level electrical self-test and fault-bank burst
  detection; siting determines how much of the chain is exposed at all.
- **Consequence:** the coil chain loses reference authority exactly in
  the environment where the Hall channel needs it (the mission's
  circularity trap, stage-20 feasibility §4); sub-threshold SETs can
  bias estimates undetected.
- **Mitigation:** remote/shielded electronics siting (stage-30 §4.3);
  steel-core MI cable; radiation-tolerant part selection with lot
  screening ([R011], [R018], [R019], [R051]); explicit RIEMF budget
  term; channel-level separation so one event cannot take both channels.
- **Residual risk:** dose-to-RIEMF magnitude is unquantified in the
  open literature (C19 note); n+γ synergy defeats part-level prediction
  (C17/C25); the ITER-class integration environment imposes its own
  constraints ([R054]).
- **Test:** fault injections F9/F10; rung-6 in-flux measurement.
  Evidence: C19, C25, C17.

### FM-13 — Dynamic range and saturation (RR-23)

- **Cause:** fast transients exceeding Hall AFE headroom or integrator
  rails; cored components saturating (air-core coils are linear; the
  chain is not).
- **Symptom:** clipped waveforms; in the overlap band, residual bursts
  against `ρ`-consistency (the CT-saturation-detection analog, [H051],
  [H052]).
- **Detectability:** in the overlap band only, with the Hall channel as
  linear witness; **out-of-band clipping is invisible** (no redundancy
  above the Hall pole, FM-09).
- **Consequence:** corrupted transient field estimates; restoration is
  heuristic, not calibration ([H052]); a clipped integrator loses the
  flux baseline (FM-08 interaction: re-anchoring required).
- **Mitigation:** headroom design against the machine's worst-case
  dB/dt; range switching; hardware clip flags in the AFE.
- **Residual risk:** content above the Hall band has no witness; a
  saturated event there is unrecoverable and unflagged.
- **Test:** fault injection F11; rung-2 dynamic tests. Evidence: H048,
  H049, H051, H052; stage-20 case 9.

### FM-14 — Radiation vs temperature/annealing inseparable without proxies (RR-14, RR-15)

- **Cause (Derived + Observed):** when temperature history and dose
  accumulation co-evolve, the attribution regression is exactly singular
  (CASE J-corr, rank 1/2); annealing adds hysteresis that recouples the
  histories after exposure stops (GaN-family partial recovery,
  [R024], [R033], C22; micro-Hall partial anneal recovery, [R012],
  [R013], C15).
- **Symptom:** ill-conditioned attribution fits; drift that partially
  reverses after shutdown (anneal) and can be misread as instrument
  recovery or as field change.
- **Consequence:** the "radiation compensation" story collapses into
  "environmental drift compensation of unknown cause"; post-exposure
  reconstruction `S_H(Φ)` cannot claim a dose axis without
  species-matched dosimetry (C16, C26); transmutation share never
  anneals (C24), so extrapolating recovery is wrong.
- **Detectability:** conditioning monitor on the attribution regression
  (reported, not regularized away — stage-30 §6.3.5); temperature
  telemetry at the die.
- **Mitigation:** engineered thermal excursions decorrelated from dose
  accumulation (CASE J-decorr restores rank); anneal-aware validity
  windows; co-located foil dosimetry as the dose proxy.
- **Residual risk:** the recoverable fraction for GaN Hall plates is
  Unknown; windows shrink exactly when the environment is most active.
- **Test:** scenarios S6/S7/S10; rung-4 thermal rehearsal; FT-11
  includes a decorrelation schedule. Evidence: C22, C15, C16, C24, C26.

### FM-15 — Calibration traceability and the uncertainty floor

- **Cause (Derived):** by Theorem 1, every in-situ scheme is
  change-tracking anchored to an epoch; the floor is set by the anchor
  chain — vacuum-model error mapping 1:1 into gain, position via
  `∇G·δr`, misalignment `cos θ_m`, current-log accuracy, timing skew
  (stage-20 case-4 budget; stage-30 §6.3) — plus random-walk growth of
  frozen states between anchors.
- **Symptom:** not a malfunction but a claim-level failure: any stated
  unconditional absolute accuracy ("the hybrid measures B to X %") is
  unsupportable; honest output is "X % relative to the anchor epoch,
  growing at the stated rate."
- **Detectability:** audit-level — compare claimed uncertainty against
  the assembled budget; gate G1 requires bench repeatability to match
  the T0-predicted uncertainty across ≥3 cycles.
- **Consequence:** if the floor exceeds the scientific requirement
  (e.g., error-field-relevant accuracy at a stellarator), the
  architecture is not fit for that purpose regardless of how well the
  estimator works; over-claiming would fail review (FM-17 interaction).
- **Mitigation:** NMR-class traceable transfer standard at the bench
  root ([H041], [H042], [H064], [P058]); layered anchors; per-epoch
  archived uncertainty (calibration ledger).
- **Residual risk:** the floor is irreducible below the anchor-chain
  accuracy; no in-situ mechanism exists to beat it (Theorem 1).
- **Test:** FT-05 closure against the transfer standard; FT-08 anchor
  repeatability; gate G1. Evidence: C02, C29 context; stage-20 §6.3.

### FM-16 — Packaging, manufacturability, maintenance, channel-count cost

- **Cause (Derived from the architecture; cost classes are labeled
  estimates, no vendor prices in evidence):** each hybrid head bundles a
  GaN die, pickup coil, optional cal winding, temperature sensor,
  optional witness die, MI cabling with guarded feeds, plus per-channel
  spinning AFE, lock-in, shared-clock digitization, and anchor
  procedures. Complexity scales roughly linearly with channel count.
- **Symptom:** cost/effort per channel several times a bare Mirnov coil;
  maintenance or bench recalibration of in-vessel heads requires vents
  and — after any neutron campaign — activated-hardware handling
  (Option E logistics, stage-30 §3); real in-vessel coil suites already
  see fault attrition ([R066]).
- **Detectability:** programmatic — design review at G2 with an explicit
  per-channel cost/complexity table; not a physics observable.
- **Consequence:** at array scale (hundreds of channels — WEST-class
  suites run ~469 sensors, [P004], C33) the hybrid-per-channel model is
  implausible; the realistic topology is few anchored hybrid heads
  calibrating many simple coils — which changes the value claim from
  "a better sensor" to "a calibration node" and must be stated that way.
- **Mitigation:** sparse hybridization (calibration-node topology);
  modular head design; gen-2 die/packaging development kept inside the
  existing project-03 LCC/ceramic-cube plan rather than a new line.
- **Residual risk:** manufacturability and yield of multi-axis GaN heads
  at even modest counts is Unknown; channel-count economics are a
  labeled estimate until a costed design exists.
- **Test:** FT-07 (does added complexity buy measurable accuracy over
  scheduled recalibration?); G2 design review. Evidence: C33; P004;
  R066; DECISION_FRAMEWORK.md tier structure.

### FM-17 — Prior-art and novelty constraints

- **Cause (Observed):** the architecture-level idea has 26 years of
  direct prior art (1999–2025): HOKA Hall+coil current probe ([H055]),
  chip-scale Hall array with embedded calibration coil ([H038]), the
  2007 fusion self-diagnostic Hall concept ([H006] — peer-review
  status uncertain, weak venue; the rigorous citation is the 2012 JET
  RHP paper [H007]), the 2022 JET RHP operational record ([H003]) and
  CERN Kalman drift-free integration ([H004]), the 2025 fusion
  Kalman-fusion papers ([H001], [H002]), ITER's deployed OVSS pairing
  ([P003], C27), and decades of routine Hall+coil+NMR accelerator
  metrology ([P052], [P057], [P058], C29).
- **Symptom:** reviewer/proposal rejection: "this is OVSS," "this is
  the RHP self-test," "accelerator labs have done this for decades."
- **Detectability:** cheap and immediate — a dedicated prior-art search
  on the narrowest intended claim *before* any writing (FT-01).
- **Consequence:** a broad novelty claim is dead on arrival; worse, a
  paper built on it dilutes the thesis (stage-40 dilution scoring).
- **Mitigation:** claim only the C36 gaps (see §3.6 below); position
  hybridization as method, not contribution (C37).
- **Residual risk:** the C36 gaps are absence claims bounded by this
  mission's search scope; a competitor may close them first (the 2025
  papers show the space is active — two author clusters, C01 note).
- **Test:** FT-01 (prior-art kill search, repeated before each
  manuscript). Evidence: C01, C27, C29, C36.

### FM-18 — False confidence from estimator tuning and simulation

- **Cause (Derived + Observed pattern):** an estimator handed a
  non-identifiable parameter set does not fail — it "converges" by
  resolving the gauge orbit with its prior; simulation initialized near
  truth hides this completely (stage-20 §5.3). The field's own
  literature exhibits the validation-strength inversion: the fusion
  Kalman-fusion papers closest to this mission are synthetic-only or
  validation-unconfirmed, while the hardware-validated results are
  non-fusion and never estimate Hall gain (C09).
- **Symptom:** clean synthetic recovery of `{B, S_H, b_H, K_C, b_C}` in
  regimes where stage 20 proves rank deficiency — the recovered values
  are the prior, restated; strong sensitivity of "results" to
  initialization and tuning.
- **Detectability:** the T-NI honesty test — on CASE-A/F scenarios the
  estimator must freeze states and inflate reported uncertainty, not
  converge (binding stage-30 rule §6.1); prior-sensitivity sweeps;
  pre-registered no-alarm scenario S8.
- **Consequence:** hardware money spent on a fictional capability;
  a publication claiming simulation as validation (explicitly forbidden
  here — and the ledger contains a cautionary simulation-only rad-hard
  design, [R050], never citable as experimental).
- **Mitigation:** regression-bind the simulator to the stage-20 rank
  tests; pre-registered scenarios and metrics before tuning; independent
  re-run of the estimator with perturbed priors as a standing check.
- **Residual risk:** subtle prior leakage in practical filters survives
  even honest design; only hardware gates (G1–G3) retire it.
- **Test:** FT-02 (T-NI + prior-sensitivity); FT-03 (no-alarm
  common-mode scenario). Evidence: C09; stage-20 §5.3; stage-30 §6.1.

---

## 3. Potential — separated by value class, each conditional (stage-required)

Every entry below is **conditional on a measurable advantage and an
identifiable calibration path**; none is claimable today. The condition
column names the gate/test that would convert it into a claim.

| # | Value class | What is actually available | Condition to claim it | Status |
|---|---|---|---|---|
| 3.1 | Better measurement performance | Only vs *coil-only long-pulse operation*: DC restoration + drift-bounded integration (the C02 hardware-proven direction). Not better than TMR/FOCS/NMR/simple coils in their own niches (§4). Not shown better than a single well-anchored Hall channel plus scheduled recalibration. | FT-07 shows the hybrid's drift resolution measurably beats scheduled-recal-only at G2; G1 repeatability met | Proposed; conditional |
| 3.2 | Radiation compensation | In-situ *relative* gain tracking `S_H(t)/S_H(t_0)` + per-epoch offset re-anchoring + post-exposure reconstruction with a dose axis from foils. Attribution needs the diversity tier. | Species-matched screening (FT-11) shows drift is (a) large enough to matter and (b) above the tracking floor; anchors demonstrated (FT-08) | Proposed; magnitude Unknown (C14) |
| 3.3 | Fault detection / self-diagnostics | The cheapest genuine value: ρ-alarm, triangle closure, `R_H` and noise telemetry cost nothing extra and work even where calibration is impossible. Detection ≠ attribution (confounding row 6). | FT-06/FT-10 false-alarm and detection rates characterized | Proposed; strongest near-term case |
| 3.4 | Modular packaging / simulation package | The T0 truth-model + honesty-tested estimator + head design is reusable engineering; publishable as instrumentation/methods. | G0 pass with the honesty test intact | Proposed; engineering value, not novelty |
| 3.5 | Application-specific value | Stellarator commissioning/mapping niche is literature-empty (C32) and is the user's own machine; tokamak long-pulse reverse-direction demonstration targets the sharpest documented gap (C06). | Stage-40 gate sequence (G0→G1 at HSX); FT-08/FT-09 on real shots | Proposed; ranked 1–2 in stage 40 |
| 3.6 | Scientific novelty vs engineering integration | See below. | FT-01 re-run before each claim | Derived |

### 3.6 The narrowest defensible contribution (stage-required verdict)

**The broad hybrid idea is not novel. Stated plainly (Observed):**
combining a Hall/DC channel with an inductive/AC channel is 26-year-old,
multi-domain prior art (C01), adopted in a real-machine final design
(ITER OVSS, C27 — manufactured, not yet operating; stage-70 correction)
and routine in accelerator metrology (C29). After the 2007 concept line
([H006] — full-text-confirmed at stage 70 to disclose the embedded
winding, AC injection, and synchronous detection, with companion 2009/2010
patents; [H007] as the rigorous 2012 citation), the 2022 results
([H003] operational record *and* §5 hybrid-probe proposal including
passive coil→Hall recalibration; [H004] Kalman drift-free integration),
and the 2025 fusion Kalman papers ([H001], [H002]), **no publishable
claim can rest on "we hybridized a Hall sensor with a coil."**

What the prior art does *not* contain (Derived, C03/C06/C36, absence
bounded by this mission's documented search):

- (a) a joint identifiability analysis of the Hall+coil pair with gains,
  offsets, and field simultaneously unknown (every prior estimator
  assumes `S_H` known/stable; the strongest published rank condition
  explicitly excludes unknown sensor gain, [H021]);
- (b) a hardware demonstration of the *reverse* direction — **passive**
  coil-derived Hall-gain tracking — in any fusion or radiation
  environment (the one demonstrated precedent is a driven-ramp HTS
  magnet, [H059], C11). Stage-70 narrowing: the *concept* is published
  prior art ([H003] §5 passive dry-run/ramp recalibration; ITER OVSS
  calibration plan, [H067]), and *active* microsolenoid recalibration
  under D-T/fission irradiation is demonstrated (C05, [H011]) — only the
  passive demonstration plus its identifiability treatment is open;
- (c) in-situ radiation-aware Hall recalibration against a
  material-diverse **passive witness sensor** (unreported, C21;
  actuator-winding recalibration under irradiation is demonstrated,
  [H011] — the distinction is load-bearing);
- (d) any Hall+coil work for stellarator field mapping (C32; adjacent
  KSTAR Hall-array + pickup-coil + e-beam commissioning practice
  [P077] must be cited-and-distinguished).

Stage-70 addition: 2009/2010 patents on combined sensors for in-situ
Hall calibration (GB2427700/FR2887991 formats, via [H003] refs 66–67)
mean a patent search is mandatory before any embedded-actuation novelty
claim (C36 limitations).

**Narrowest defensible contribution (Proposed):** an
identifiability-grounded, anchor-referenced drift-tracking demonstration
on a stellarator — i.e., gap (a) as the theory piece (Theorem 1 plus the
excitation/anchor conditions, already derived in stage 20) realized as
gap (b)'s first in-machine hardware demonstration at HSX, in the
application niche of gap (d), with the estimator's honest
non-identifiability behavior presented as a feature. Gap (c) remains a
later, collaborator-led extension (stage-30 §9.4 boundary). This is
predominantly **engineering integration with one bounded theoretical
contribution**; it should be framed exactly so. Anything broader is
vetoed by FM-17.

---

## 4. Counterexamples: where a simpler sensor wins outright

Recorded here and in `05_TECHNOLOGY_COMPARISON.csv` (stage-required).
Each is Observed from the ledger, not conceded grudgingly:

1. **Fast MHD/fluctuation measurement:** a plain B-dot/Mirnov coil is
   simpler, cheaper, faster, and fully proven ([H048], [H049], [P017]);
   a Hall channel adds nothing above its pole (FM-09). Coil wins.
2. **Total plasma/conductor current:** Rogowski/CER is the standard
   ([H024], [R069], [R070]); where EMI+radiation dominate, FOCS is the
   credible upgrade with the only in-machine D-T dataset (±4 % Verdet
   shot-to-shot through ~8.5e20 n, C20, C34). Neither needs a Hall die.
3. **Z-pinch/pulsed power:** the community fused two *inductive* sensors
   (B-dot + Rogowski, ±13–15 %) and deliberately bypassed Hall (C30);
   ns–µs timescales leave no DC baseline to anchor. Inductive pair wins;
   hybrid vetoed (stage 40).
4. **Persistent-mode SC/HTS magnets:** a coil is structurally blind to a
   trapped static field; NMR is the field's own reference (>2 yr at
   ~3e-5 ppm/h with NMR cross-check, C28). NMR + Hall array wins; the
   coil half of the hybrid is dead weight.
5. **Precision accelerator-magnet metrology:** Hall + rotating coil +
   NMR is decades-old production practice (C29); the hybrid adds nothing
   to a solved problem.
6. **Gamma-only, compact DC-to-broadband sensing:** a single TMR channel
   spans DC-to-broadband and survived 5 Mrad(Si) gamma/X-ray with no
   key-parameter degradation (C31) — one device where the hybrid needs
   two channels plus an estimator. TMR wins on simplicity (neutron
   response: no evidence either way, C31 caveat).
7. **In-plasma-core / highest-stress regions:** practitioners already
   abandoned magnetic probes for optical/spectroscopic methods (PDV,
   Zeeman — C35); no magnetic architecture competes there.

---

## 5. Limitations of this analysis itself

- Absence claims (C03, C06, C14, C21, C32 and the §3.6 gaps) are bounded
  by this mission's documented search scope; they are strong systematic
  absences, not proofs of nonexistence.
- Single-source dependencies persist: the metallic-Hall witness rests on
  [R071] (C18); the coil-calibrates-Hall precedent on [H059] (C11);
  several quantitative figures (JT-60SA 200 °C/9 MGy, ITER 1 µV RIEMF
  target, chip-actuator 392 mT/A) are secondary-sourced and flagged in
  the evidence map, not independently re-read.
- Cost categories anywhere in stage 50 are order-of-magnitude labels
  (labeled estimates); no vendor pricing exists in the evidence base.
- All identifiability statements inherit the stage-20 assumptions
  register (linearity, spectral separation prior, quasi-stationarity
  windows, noise-free structural ranks).
- Nothing in this file is experimental validation of the hybrid; the
  only hardware-validated element remains the Hall→coil correction
  direction (C02) plus component-level radiation data on non-GaN
  materials.
