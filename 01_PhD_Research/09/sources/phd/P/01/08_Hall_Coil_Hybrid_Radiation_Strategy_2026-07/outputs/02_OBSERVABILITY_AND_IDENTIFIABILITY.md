# 02 — Observability and identifiability of the Hall + coil pair

Stage 20 (`20_observability`). Produced and signed off by Fable 5 (xhigh).
Source IDs (`Hxxx`, `Rxxx`, `Pxxx`) refer to `outputs\01_SOURCE_LEDGER.csv`;
claim IDs (`Cxx`) refer to `outputs\01_EVIDENCE_MAP.csv`. Every substantive
statement is labeled **Observed**, **Derived**, **Inferred**, **Proposed**, or
**Unknown** per `CLAUDE.md`. All mathematics in this file is **Derived** from
the stated model assumptions; the numerical rank tests in §7 are reproducible
synthetic demonstrations (`tools\observability_rank_tests.py`) and are **not
experimental validation**.

---

## 1. Question and method

Can the Hall channel and the inductive-coil channel calibrate each other —
and exactly which states/parameters are observable under which excitation and
reference conditions? Folder `06` and stage 10D established that no published
source answers this jointly for the Hall+coil pair (claim C03, [H021], [H012],
[H015]–[H017]); this stage therefore derives the answer from first principles
and checks each step with a numerical Fisher-information rank test.

Method per stage requirements: explicit measurement model (§2); a structural
(global, symmetry-group) non-identifiability proof (§3); identifiable
combinations (§4); nine required cases analyzed by algebraic elimination plus
numerical FIM rank (§5); six required confounding tests (§6); numerical
protocol and reproducibility (§7); assumptions register (§8). We do **not**
use "complementary bandwidth" as an identifiability argument anywhere; where
crossover-fusion prior art is cited ([H045], [H066]), it is cited as signal
combination practice, explicitly not as an identifiability proof.

---

## 2. Measurement model

### 2.1 Direct-readout form

```text
y_H(t) = S_H(t) · B(t) + b_H(t) + n_H(t)          (Hall)
y_C(t) = K_C(t) · dB/dt(t) + b_C(t) + n_C(t)      (coil, direct readout)
```

- `B(t)` — true field component along the shared sensing axis [T].
- `S_H(t)` — Hall sensitivity (gain), [V/T]; drifts with temperature and
  radiation dose (Observed for InSb under thermal-spectrum neutrons [R001],
  [R002], [R003]; **Unknown** for GaN/AlGaN Hall plates under neutrons — no
  dataset exists, claim C14).
- `b_H(t)` — Hall offset [V]. Current-spinning reduces but does not
  eliminate it; a residual floor survives (Observed, [H034], [H035], claim
  C07), so `b_H` must be kept as a free state even with spinning active.
- `K_C(t)` — coil transduction gain, `K_C = N·A_eff·G_ro` [V·s/T] including
  readout gain; drifts via geometry/thermal expansion and readout gain.
- `b_C(t)` — coil-chain additive offset [V]: amplifier offset, thermoelectric
  EMFs, and under radiation the RIEMF of mineral-insulated cabling (Observed
  mechanism, [R056], claim C19).
- `n_H, n_C` — measurement noises, modeled white Gaussian with variances
  `σ_H², σ_C²` (1/f knees and EMI treated as part of the drift/offset band,
  §2.5).

Sign convention: physically the EMF is `−N·A_eff·dB/dt`; `K_C` absorbs the
sign and readout gain. A wiring/sign error appears as `K_C < 0` and is
detectable through the sign of the identifiable gain ratio (§4).

### 2.2 Integrated-coil form

For integrator-based readout (the fusion-relevant implementation, [H025],
[H026], [H027]), the coil channel is replaced by the integrator state:

```text
dx_I/dt = −x_I/τ_L + g·dB/dt + m(t),   y_I(t) = x_I(t) + n_I(t)
```

- `x_I(0)` — unknown initial condition (flux baseline at estimator start);
- `g = K_C/τ_i` — effective integrated-coil gain;
- `τ_L` — leakage time constant (droop);
- `m(t) = V_os(t)/τ_i` — integrator drift rate from input-referred offset;
  the dominant long-pulse error (Observed, [H025], [H004], claim C02);
- timing/phase: a sampling skew `δt` between channels multiplies the coil
  transfer function by `e^{−jωδt}`; treated in case 9.

### 2.3 State vector, parameters, inputs (stage-required definitions)

- **State vector** (augmented): `x = [B, x_I, S_H, b_H, K_C (or g), b_C (or
  m), τ_L, θ_env]` where `θ_env` optionally holds temperature/dose drift
  coefficients (case 7). Parameters enter as slowly varying states.
- **Unknown parameters:** `S_H, b_H, K_C, b_C, x_I(0), m, τ_L`, and, when not
  externally referenced, the field trajectory `B(t)` itself.
- **Known inputs:** none in the unreferenced pair. In referenced cases:
  machine coil currents `I(t)` with a field model `B = G(r)·I` (case 4);
  injected calibration current `I_cal(t)` with transfer `G_cal` (case 5);
  the identity of a repeated waveform (case 6); measured temperature `T(t)`
  and dose proxy `D(t)` (case 7).
- **Process noise / slow-drift priors:** parameter drifts modeled as random
  walks or Ornstein–Uhlenbeck processes band-limited to a drift band
  `ω < ω_d`, with `ω_d` well below the field signal band. This spectral
  separation is a *prior*, not a theorem; where a conclusion depends on it,
  that dependence is stated. (Standard augmented-bias-state practice,
  Observed as method in [H015], [H004].)
- **Measurement noise:** white `n_H, n_C, n_I` as above.
- **Calibration/excitation signal:** any intentional field variation —
  machine ramps, injected `I_cal`, thermal excursions (case 7/J).
- **Reference measurement:** any externally trusted quantity — `I(t)` +
  field model, characterized `G_cal`, zero-field epochs, NMR-class absolute
  probes ([H041], [H042], [H064]), a material-diverse Hall channel ([R071]).

### 2.4 Terms added only with reason (stage rule)

- **Temperature and radiation history** enter as drift drivers of
  `S_H, b_H` (case 7, case J): required because the mission's central use
  case is radiation-induced drift (claims C12–C16).
- **Cross-axis/misalignment** enters only in case 4: a misalignment angle
  `θ_m` makes the reference comparison read `S_H·cosθ_m`, biasing the gain
  estimate; it is inseparable from `S_H` with a single-axis reference
  (Derived; consistent with vertical-Hall cross-sensitivity evidence
  [H047]).
- **Nonlinearity** is excluded from the identifiability core: with
  `S_H = S_H(B)`, gain estimated at one field level does not transfer to
  another, which *strengthens* (never weakens) the case-4 requirement of
  multiple field levels; bench linearity characterization is assumed
  (Proposed for the Tier-1 bench, `DECISION_FRAMEWORK.md`).
- **Saturation** enters case 9 only: air-core coils are linear, but cored
  sensors, readout stages, and integrators clip; analog: CT saturation
  detection [H051], [H052].

### 2.5 Frequency-band convention

`Ḃ_LF` denotes field content inside the drift band `ω < ω_d`; "AC band"
means `ω > ω_d`. Coil noise floor `σ_C` and drift `b_C` define a minimum
detectable rate: field drift with `|K_C·Ḃ| ≲ σ(b_C)` is invisible to the
coil — used repeatedly below.

---

## 3. Structural non-identifiability of the unreferenced pair (required counterexample)

**Theorem 1 (two-parameter gauge group). Derived.** Let `S_H ≠ 0, b_H,
K_C ≠ 0, b_C` be constant and `B(·)` an arbitrary C¹ field trajectory. For
any `α ≠ 0` and `β ∈ ℝ`, the transformed configuration

```text
B'(t)  = α·B(t) + β
S_H'   = S_H / α          b_H' = b_H − β·S_H/α
K_C'   = K_C / α          b_C' = b_C
```

produces outputs identical to the original for every `t`:

```text
y_H' = (S_H/α)(αB+β) + b_H − βS_H/α = S_H B + b_H = y_H
y_C' = (K_C/α)(α·dB/dt) + b_C       = K_C dB/dt + b_C = y_C
```

Since this holds for **every** field waveform, no excitation whatsoever can
break it. The parameter-to-output map is non-injective along a 2-dimensional
orbit through every truth point. ∎

**Consequences (Derived):**

1. **Absolute scale is never identifiable from the pair alone.** The data
   cannot distinguish "field is `αB`" from "both gains dropped by the factor
   `α`". A *common-mode* gain drift of Hall and coil is invisible — it is
   observationally equivalent to a genuine field change. This is the formal
   content of `MISSION.md`'s warning that redundancy does not reveal which
   device drifted.
2. **Hall offset is never identifiable from the pair alone.** The `β`
   direction trades `b_H` against a static field shift, which the coil
   cannot see (it measures only `dB/dt`).
3. Any claim that an unreferenced Hall+coil pair "self-calibrates" in the
   absolute sense is **false as stated**; only orbit-invariant combinations
   (§4) can be estimated. No source in the ledger contradicts this; the
   absence of a joint identifiability proof in the literature (C03) is
   consistent with it.

The numerical FIM null space of the all-unknown case reproduces exactly
these two directions to machine precision (§7, CASE A: rank 5/7, both
analytic null vectors matched with residual ~1e−15).

---

## 4. What the unreferenced pair CAN identify

**Derived (local identifiability = orbit-invariant functions; confirmed
numerically, CASE A).** With `B(t)` containing AC content whose derivative
has no component inside the drift band:

- **Gain ratio `ρ = S_H/K_C`** — identifiable (null-space component
  ~1.6e−15, CASE A). In the AC band, `ẏ_H ≈ S_H·Ḃ` and
  `y_C − b_C ≈ K_C·Ḃ`, so `ρ` follows from cross-channel regression without
  knowing `B`. Its drift is a **differential drift alarm**: a change in `ρ`
  proves at least one gain changed, without attributing which (§6.2, §6.6).
- **Coil offset `b_C`** — identifiable *conditionally* on `Ḃ` having no
  unknown component in the drift band (orbit-invariant, and full-rank in
  CASE A's AC basis; confounded when the field may ramp — CASE C1, §5.1).
- **Field shape up to the affine orbit** — `B(t)` is recovered up to
  `(α, β)`, i.e., relative waveform, not absolute scale/offset.
- **Relative timing and relative dynamics** in the overlap band (case 9).

Everything else — `S_H`, `K_C`, `b_H`, absolute `B` — requires a reference
or anchor. The rest of the analysis is about which reference buys which
parameter.

---

## 5. The nine required cases

Each case states: setup → identifiability argument → verdict → conditions.
Numerical cross-references are to §7 (CASE letters). Verdict vocabulary:
**identifiable / conditionally identifiable / not identifiable**, applied
per-parameter (the stage forbids forcing symmetry, and none appears).

### 5.1 Case 1 — S_H stable/known; b_H drifts; K_C stable/known; integrator drifts

Setup: both gains pre-calibrated and assumed stable over the analysis
window; unknowns are the offset/drift trajectories `b_H(t)`, `b_C(t)` (or
`x_I(0), m, τ_L`) and the field.

**Derived.** Write `b_H(t) = b_{H0} + b_{H1}t`, `b_C(t) = b_{C0} + b_{C1}t`
(low-order drift basis) and let the field contain DC, ramp, quadratic, and
AC components. Algebraic elimination leaves the observable combinations
`{S_H c_0 + b_{H0}, S_H c_1 + b_{H1}, K_C c_1 + b_{C0}, c_2 (AC), c_3
(quadratic), b_{C1}}` — a rank deficiency of exactly 2 (numerically: CASE
C1, rank 6/8; null directions = field-DC↔Hall-offset and
field-ramp↔both-offsets, matched to 1e−14).

Two structural insights (Derived, both confirmed in CASE C1):

- **Cross-channel disambiguation works for components with distinguishable
  time signatures.** With `S_H` known, the Hall channel pins the quadratic
  field coefficient (`t²` is outside the drift basis), and that in turn
  makes the coil's linear drift `b_{C1}` identifiable. This is genuine —
  and bounded — mutual help.
- **The residual confounding is exactly the LF trio** {slow field, Hall
  offset drift, coil offset}: within the drift band the pair has 2 equations
  and 3 unknown trajectories per time (§2.5).

**Anchors close the gap.** Adding pre/post-shot epochs where `B = 0` (field
off, ambient known) and `dB/dt = 0` pins `b_H` and `b_C` directly; the
augmented problem is full rank (CASE C2, 8/8). Between-shot zero-field
access is routine in pulsed machines; validity requires remanent/ambient
field at the sensor to be negligible or independently known (**assumption**,
flagged).

**Integrated-coil variant.** With the Hall channel calibrated, the
integrator's `{x_I(0), g, m, τ_L}` are jointly identifiable **given dB/dt
variation** (CASE I, full rank 4/4). Under a constant-slope ramp they are
not: `g·r + m` is invariant (CASE I-ramp, rank 3/4, analytic null matched)
— **coil gain and integrator drift are structurally confounded until the
waveform contains at least two distinct dB/dt values** (e.g., ramp +
flat-top). This is the precise content behind the stage's requirement to
distinguish coil gain from integrator drift.

**Verdict:** conditionally identifiable — fully identifiable with zero-field
anchors (offsets) and dB/dt variation (gain-vs-drift separation); without
anchors, deficiency 2 (LF trio).

**Evidence:** the Hall-corrects-coil direction of this case is the
hardware-proven one: CERN bench Kalman correction of integrator drift using
a non-integrating reference (Observed, [H004], [H005]; 59.9–120 ppm/s →
0.02–0.08 ppm/s) and ITER OVSS system-level practice (Observed at metadata
level, [P003]) — claim C02. Estimator precedent: augmented bias-state
filtering (Observed as method, [H015], [H004]).

### 5.2 Case 2 — S_H and b_H both drift; coil chain trusted

Setup: `K_C, b_C` known/stable (trusted coil chain); unknowns `S_H, b_H, B`.

**Derived.** The coil supplies `Ḃ = (y_C − b_C)/K_C`, hence the field
*increment* `ΔB(t) = B(t) − B(0)` exactly; `B(0)` stays unknown. Then

```text
y_H(t) = S_H·ΔB(t) + [S_H·B(0) + b_H]
```

is linear regression on the known regressor `ΔB(t)`: `S_H` and the lumped
intercept `β* = S_H B(0) + b_H` are identifiable iff `ΔB` is persistently
exciting (takes ≥2 sufficiently separated values). `b_H` alone is **not**
separable from `S_H·B(0)` (CASE B: rank 4/5, null = DC direction; `S_H`
verified identifiable).

**Interpretation (Derived):**

- **The coil CAN calibrate Hall gain in situ** — the mission's most-wanted
  reverse direction — under three conditions: (i) trusted `K_C, b_C` at the
  target accuracy; (ii) field excursion `ΔB` with SNR (Fisher variance
  `var(Ŝ_H) ≈ σ_H²/Σ(ΔB_k − ΔB̄)²`); (iii) `S_H, b_H` quasi-constant over
  the regression window (drift timescale ≫ window).
- **The coil can NEVER supply Hall offset**; that requires `B(0)` known
  (zero-field start) or an absolute reference.
- Coil-chain errors propagate multiplicatively: a bias `δ(ΔB)` gives
  `δS_H/S_H ≈ −δ(ΔB)/ΔB`; integrator noise makes the reference `ΔB` a
  random walk, bounding the usable window length.

**Evidence:** exactly this structure — cryogenic Hall sensors cross-
calibrated in situ against induction coils during **driven, known magnet
ramps** — is abstract-confirmed in one non-fusion source (Observed,
[H059]; claim C11), the only coil-calibrates-Hall instance in the ledger.
No fusion or radiation-environment demonstration exists (claim C06). The
excitation-conditionality is the GPS/INS analog (Observed as analog,
[H018], [H019]; claim C04).

**Verdict:** `S_H` conditionally identifiable (trusted coil + excitation);
`b_H` not identifiable without an anchor.

### 5.3 Case 3 — everything drifts (S_H, b_H, K_C, integrator)

**Derived.** Theorem 1 applies in full: 2-dimensional orbit, no excitation
helps (CASE A: rank 5/7). Identifiable content is §4's list: gain ratio
`ρ`, conditionally `b_C`, field shape up to affine orbit. Practical
consequences:

- differential drift **detection** (ρ-alarm) works;
- **attribution is impossible** from the pair: a ρ-jump cannot be assigned
  to Hall vs coil, and common-mode drift produces no alarm at all;
- any estimator that "converges" in this case (e.g., an EKF given all five
  unknowns) is silently resolving the orbit with its prior — the answer is
  the prior, not the data. This failure mode is invisible in simulation
  studies that initialize near truth (**Inferred** — and consistent with the
  fact that the closest fusion Kalman-fusion papers assume the Hall gain
  known/stable rather than estimating it: [H001], [H002]; claims C06, C09).

**Verdict:** not identifiable (beyond §4's invariants). This is the
mission's central negative result and the second required counterexample.

### 5.4 Case 4 — known machine coil current + trustworthy field model

Setup: `B_ref(t) = G(r)·I(t)` from measured coil currents and a validated
vacuum-field model; unknowns `S_H, b_H, K_C, b_C`.

**Derived.** With `B` known, the two channels decouple into two linear
regressions: Hall on `[B_ref, 1]` (rank 2 iff `B_ref` takes ≥2 values) and
coil on `[Ḃ_ref, 1]` (rank 2 iff `Ḃ_ref` takes ≥2 values, e.g. ramp +
flat-top). All four parameters identifiable (CASE D, 4/4); a constant-field
reference degenerates to rank 2 (CASE D-flat) — **a trusted reference still
needs field variation** to separate gain from offset in each channel.

Error budget (Derived): reference error `δB/B` maps 1:1 into `δS_H/S_H`;
misalignment gives `S_H cosθ_m` (inseparable single-axis, §2.4); position
uncertainty maps through the field gradient `∇G·δr`; model trust holds in
vacuum shots — during plasma operation the plasma contribution invalidates
`G·I` unless separately modeled. Timing skew between the current log and
the sensor DAQ enters `Ḃ_ref` directly (case 9 mechanics).

**Evidence:** in-situ known-current calibration of magnetic sensor arrays is
demonstrated practice (Observed: HBT-EP "artificial plasma" calibrates 216
Mirnov coils + Rogowski, [H040]; claim C08 — note it calibrates inductive
sensors, not a Hall channel); machine-current-referenced correction is the
mechanism of [H004] (current-model update mode) and the ITER OVSS pairing
[P003] (claim C02). Stellarator vacuum fields are validated to high
accuracy by e-beam mapping (Observed, [P013]; claim C32) — supporting
"trustworthy model" as realistic for vacuum shots, while claim C32 also
records that no Hall+coil hybrid stellarator mapping literature exists.

**Verdict:** identifiable (all four parameters), conditional on vacuum-shot
access, ≥2 field levels, nonzero-dB/dt segments, and reference/geometry
error budget. This is the workhorse absolute anchor available to the
mission's HSX context.

### 5.5 Case 5 — embedded calibration/test coil with characterized transfer function

Setup: injected field `B_inj(t) = G_cal·I_cal(t)` with `I_cal` measured and
`G_cal` characterized; superimposed on unknown ambient field.

**Derived.** With AC injection spectrally disjoint from ambient content,
the scale null direction is removed: **both gains `S_H` and `K_C` become
identifiable** (CASE E: rank 6/7, both gain functions verified
identifiable). What survives is exactly the DC null — **AC injection cannot
deliver Hall offset** (`b_H` trades against static ambient field). Two
sharp caveats, both numerically demonstrated:

- **Spectral collision destroys the gain information**: if the ambient
  field may contain an unknown component with the injection's signature,
  the deficiency returns (CASE E-collide: rank 5/7). Injection must be
  orthogonal to ambient content by frequency placement, coding, or on/off
  toggling — a design requirement, not a nicety.
- **Only the product `S_H·G_cal` is identifiable.** A drift of the
  reference chain (`G_cal` geometry, `I_cal` source, insulation leakage)
  is indistinguishable from Hall gain drift. Same-die references cannot
  detect common-mode (shared radiation/thermal) drift by construction —
  the documented limitation of the JET RHP microsolenoid architecture
  (Observed record: 11.5 yr, SD ≈ 0.07 % sensitivity stability, [H003],
  [H007]; limitation per claim C05). Mechanism diversity (geometric coil
  constant vs semiconductor transport) makes common-mode drift physically
  unlikely but not logically excluded (**Inferred**).

DC-capable injection with toggling extends gain calibration to the DC
operating point (difference of toggled states cancels `b_H` — it measures
gain at DC, still not the offset itself).

**Evidence:** chip-scale reference actuator (Observed at metadata level,
[H038]; ~392 mT/A figures snippet-sourced, flagged in C08); JET RHP
microsolenoid ([H003], [H007]); integrated self-test practice ([H039]).
Under radiation, injected-current integrity and RIEMF pickup in the cal
circuit are open risks (mechanism from [R056]; **Inferred** transfer).

**Verdict:** gains conditionally identifiable (reference-chain stability +
spectral orthogonality); `b_H` not identifiable from AC injection.

### 5.6 Case 6 — repeated reference waveform/shot

Setup: the machine reproduces a nominally identical field waveform across
shots `k = 0, 1, 2, …` (e.g., standard vacuum ramp each run day); channel
parameters drift *between* shots.

**Derived.** Regressing shot `k` on shot 0 channel-by-channel:

```text
y_H^k(t) = (S_H^k/S_H^0)·y_H^0(t) + [b_H^k − (S_H^k/S_H^0)·b_H^0]
```

The slope identifies the **gain drift ratio** `S_H^k/S_H^0` (and likewise
`K_C^k/K_C^0` for the coil) without knowing `B(t)` at all; the intercept
gives an offset-drift lump. Requirements: waveform reproducibility error
≪ drift to be detected (verifiable from machine current logs), ≥2 field
levels within the waveform, and stationarity within each shot. Absolute
values remain anchored to the shot-0 calibration — this converts the
absolute problem into an initial-calibration + change-tracking problem,
which is exactly what radiation-trend monitoring needs (`S_H(dose)/S_H(0)`).

**Evidence:** no source demonstrates repeated-shot Hall recalibration in
fusion (absence per claims C03/C06); the JET RHP >19,000-pulse record
[H003] is the operational cousin (same-die reference rather than repeated
waveform). This case is therefore **Proposed** practice supported by
derived algebra, not by prior demonstration.

**Verdict:** relative gain drift (both channels) identifiable; offsets only
as lumps; absolute scale inherited from the initial calibration epoch.

### 5.7 Case 7 — material-diverse redundant Hall channel + temperature/dose proxies

Setup: two Hall channels of different materials (e.g., GaN + metallic-Cu
[R071]) plus the coil; measured temperature `T(t)`; dose proxy `D(t)` from
dosimetry; all gains/offsets unknown.

**Derived.** Redundancy does **not** remove the structural nulls: the scale
and DC orbits extend over the enlarged parameter set (CASE G: rank 7/9,
both analytic nulls matched). What redundancy adds is the **gain ratio
`S_1/S_2`** (verified identifiable, CASE G) and a second offset lump.
Attribution then proceeds by mechanism diversity, not by observability
alone:

- with pre-characterized temperature coefficients and measured `T`, the
  temperature-corrected ratio drift isolates the *differential* radiation
  term `f_1(D) − f_2(D)`;
- if the reference material is radiation-null — the Cu-Hall datum: no
  measurable sensitivity change to ~1e18 n/cm², 100–250 °C (Observed,
  single-source, [R071]; claim C18) — the ratio drift estimates the GaN
  channel's radiation-induced gain drift `f_1(D)` directly (**Inferred**,
  resting on that single source; the inference is this mission's, per C18);
- dosimetry corroborates dose attribution (Observed practice, foil
  dosimetry validated at 14 MeV reference fields and in-machine, [R072]–
  [R076], [R078]; claim C26).

Temperature-vs-dose separability requires their time histories to be
decorrelated: with `T(t) ∝ D(t)` the FIM is exactly singular (CASE J-corr,
rank 1/2); engineered thermal excursions restore full rank (CASE J-decorr,
2/2). Annealing couples the two histories (hysteresis; Observed for GaN
TID partial recovery, [R024], claim C22) — separability then holds only
within windows where the history model is valid (**assumption**, flagged).

**Evidence for the gap this fills:** in-situ material-diverse Hall
recalibration is unreported for any material (claim C21) — this case is a
**Proposed** architecture whose observability properties are derived here,
not taken from literature.

**Verdict:** differential drift attribution conditionally identifiable
(mechanism/material diversity + measured T + decorrelated histories);
absolute scale still requires case 4/5-type anchoring.

### 5.8 Case 8 — quasi-static field, little persistent excitation

Setup: `Ḃ ≈ 0` over the window (long flat-top, steady state, standby).

**Derived.** The coil output carries no field information (`y_C = b_C +
n_C`); the Hall output is one equation in the lump `S_H·B + b_H`. Of the
five unknowns `{B, S_H, b_H, K_C, b_C}`, only two lumps are observable —
`K_C` is entirely invisible (CASE F: rank 2/5). **There is no mutual
calibration content at all**: the pair degenerates to two open-loop
channels. Hall drift (gain or offset) is indistinguishable from true slow
field drift; coil health is untestable.

This is the Hall+coil instance of the documented degeneracies: GPS/INS
bias/state confounding absent maneuvering (Observed analog, [H018],
[H019]; claim C04) and the persistent-mode magnet case, where a coil is
structurally blind to a static trapped field and the accepted reference is
NMR (Observed, [P042]; claim C28). It is also why steady-state machines
state non-inductive DC sensing as a *requirement* (Observed, [H065];
claim C33).

**Remedies are all external:** injected excitation (case 5) restores gain
observability; zero-field/known-field epochs restore offsets (case 1);
scheduled reference shots restore trend tracking (case 6).

**Verdict:** not identifiable (nothing beyond the two lumps). "Mutual
calibration" is **misleading** in this regime, which is precisely the
long-pulse regime that motivates hybrid sensing — the architecture's value
there rests entirely on engineered excitation/references, not on the pair
itself.

### 5.9 Case 9 — fast transient with poor Hall bandwidth or coil saturation

Setup: Hall channel has finite bandwidth (unknown or drifting pole `a`,
possible delay `δt`); transient content extends above the Hall band; coil
(or its readout/integrator) may clip.

**Derived.**

- **Overlap band:** with excitation near/above the Hall pole and the coil
  chain trusted, the Hall dynamic response is identifiable alongside the
  static parameters (CASE H-broad: rank 5/6, only the DC null survives;
  the pole direction is well-conditioned). The coil can therefore
  characterize Hall *dynamics* — gain roll-off, pole, delay — from shared
  transient content, via cross-spectral transfer-function estimation.
  Identifiability of a pure delay requires broadband content (phase slope
  vs frequency); with narrowband excitation, delay and phase-of-gain are
  confounded (Derived; fusion delay-uncertainty context [H053]).
- **Excitation below the pole degrades this smoothly:** moving all content
  a decade below the pole collapses the pole-carrying singular value by an
  order of magnitude (CASE H-narrow: 1.2e−1 → 1.4e−2, consistent with the
  analytic ω/a sensitivity scaling `|∂H/∂a| ≈ ω/a²` for `ω ≪ a`); with
  realistic noise the pole becomes practically unidentifiable — near-DC
  operation cannot verify Hall bandwidth.
- **Out-of-band content is single-channel:** above the Hall band only the
  coil reports; there is no redundancy, hence no fault coverage, for that
  content (**Derived**; mirror of case 8 with roles swapped).
- **Saturation/clipping is detectable only in the overlap band:** with the
  Hall channel as linear witness, coil-chain clipping appears as a
  residual burst against `ρ·(dy_H/dt)`-consistency; direct analogs are CT
  saturation detection/restoration (Observed analogs, [H051], [H052]).
  Air-core coils themselves do not saturate; the risk sits in cored
  designs, readout stages, and integrator rails (§2.4).

**Evidence:** crossover signal-combination practice exists (TMR+Rogowski
composite sensor [H045]; merged search-coil+fluxgate data product on
Parker Solar Probe [H066]) but is signal fusion, **not** an
identifiability proof — per the stage prohibition, none of this section's
conclusions rest on "complementary bandwidth" as an argument. Hall-channel
fault detection precedent: [H050]; B-dot/Mirnov operational limits:
[H048], [H049].

**Verdict:** relative dynamics conditionally identifiable (overlap-band
excitation + trusted coil); out-of-band content and out-of-band faults not
identifiable; saturation detectable only where the bands overlap.

---

## 6. Required confounding tests

Each row is Derived, with its breaking condition and the case where it is
demonstrated.

| # | Confounding | Structural status | What breaks it | Where shown |
|---|---|---|---|---|
| 1 | `B` ↔ `S_H` scale | Never separable from the pair alone (Theorem 1, α-direction) | External absolute reference: current+field model (case 4), characterized injection (case 5), NMR-class probe [H041, H042, H064] | §3; CASE A |
| 2 | Simultaneous Hall & coil gain drift | Common-mode component invisible (α-direction); differential component detectable via `ρ = S_H/K_C` | Attribution needs a third, mechanism-diverse channel (case 7) or a reference (cases 4/5); detection alone needs only AC excitation | §4, §5.3; CASE A, G |
| 3 | Hall offset ↔ slowly changing field | Confounded inside the drift band (β-direction; LF trio of case 1); coil helps only for field drift above its noise floor `|K_C Ḃ| > σ(b_C)` | Zero-field/known-field epochs (case 1 anchors); absolute reference | §5.1; CASE C1 vs C2 |
| 4 | Coil/integrator offset ↔ low-frequency field | A steady ramp is exactly degenerate with coil offset (`K_C c_1 + b_{C0}` lump); under constant dB/dt, gain and drift also merge (`g·r + m`) | Calibrated Hall channel supplies the LF/DC field (the hardware-proven direction, C02); dB/dt variation separates gain from drift | §5.1; CASE C1, I, I-ramp |
| 5 | Temperature ↔ radiation effects | Exactly collinear when `T(t)` and `D(t)` co-evolve (rank 1/2) | Measured `T` + pre-characterized coefficients + engineered thermal excursions decorrelated from dose; species-appropriate dosimetry — cross-species scaling can err ~14× (Observed, [R042]; claim C16); annealing hysteresis bounds window validity ([R024], C22) | §5.7; CASE J |
| 6 | Sensor failure ↔ model mismatch | A residual/ρ-jump proves "something changed", not what; with all parameters free (case 3) attribution is structurally impossible | Redundancy exceeding the unidentifiable orbit: third channel voting (case 7), injected self-test (case 5), reference shot (case 6); abrupt-vs-slow signature separates failure from drift only as a heuristic prior (**Inferred**, not proof). Fault-detection precedents: [H050], [H044], [H021] | §5.3, §5.7 |

---

## 7. Numerical rank tests: protocol and results

**Reproducibility (Derived, synthetic).** `tools\observability_rank_tests.py`
(deterministic, no RNG; numpy 2.5.1; N = 1500 samples on t ∈ [0,1];
complex-step Jacobians, step 1e−20; rank threshold 1e−9 relative; raw output
retained in `tools\observability_rank_tests_output.txt`). The unknown field
is restricted to a finite known basis — a **best case** for identifiability:
rank deficiency under this restriction implies the corresponding confounding
in the unrestricted problem (the exhibited null directions remain valid
whenever the true field class contains the basis); full-rank results are
**conditional** on the excitation actually containing the assumed
components, and are reported as excitation conditions, not unconditional
claims. Nominal parameter values are stated in the script; unit noise on all
channels. These are demonstrations of structure, **not** experimental
validation and not simulations of any specific device.

| CASE | Stage case | Unknowns | Rank | Null dim | Matches analytic |
|---|---|---|---|---|---|
| A | 3 (all drift) | 7 | 5 | 2 | scale + DC orbits (1e−15); `ρ = S_H/K_C` identifiable; `S_H` alone not |
| B | 2 (coil trusted) | 5 | 4 | 1 | DC only; `S_H` identifiable |
| C1 | 1 (in-shot) | 8 | 6 | 2 | LF trio nulls; `b_C1`, `c_3` identifiable |
| C2 | 1 + zero-field anchors | 8 | 8 | 0 | full rank |
| D | 4 (reference field) | 4 | 4 | 0 | full rank |
| D-flat | 4, constant field | 4 | 2 | 2 | gain/offset merge per channel |
| E | 5 (AC injection) | 7 | 6 | 1 | DC only; both gains identifiable |
| E-collide | 5, spectral collision | 7 | 5 | 2 | scale null returns |
| F | 8 (quasi-static) | 5 | 2 | 3 | two lumps only |
| G | 7 (2 Hall + coil) | 9 | 7 | 2 | same orbits; `S_1/S_2` identifiable |
| H-broad | 9 (pole in band) | 6 | 5 | 1 | pole well-conditioned (s ≈ 1.2e−1) |
| H-narrow | 9 (below band) | 6 | 5 | 1 | pole s.v. collapses to 1.4e−2 |
| I | integrator, rich dB/dt | 4 | 4 | 0 | full rank |
| I-ramp | integrator, const dB/dt | 4 | 3 | 1 | `g·r + m` null matched |
| J-corr / J-decorr | 7 (T vs dose) | 2 | 1 / 2 | 1 / 0 | collinear vs separable |

---

## 8. Assumptions and limitations register

1. **Linearity and single-axis projection** assumed throughout;
   misalignment handled only as a case-4 bias term (§2.4). Cross-axis
   response of the real devices must come from bench characterization.
2. **Spectral separation prior** (`ω_d` drift band below signal band) is an
   assumption, not a theorem; conclusions relying on it are flagged in
   cases 1 and confounding rows 3–4.
3. **Quasi-stationarity windows**: gain/offset drift assumed slow relative
   to each regression/estimation window; radiation transients (e.g., SETs
   in readout, [R052] context via claim C25) violate this and belong to
   fault detection, not calibration.
4. **Positive verdicts are excitation-conditional** (see §7 protocol note);
   every "identifiable" above carries its stated excitation/reference
   condition. Negative (rank-deficient) results are robust in the a
   fortiori direction.
5. **Noise-free structural analysis**: ranks address structural
   identifiability; practical identifiability adds SNR thresholds (Fisher
   variances stated where load-bearing, §5.2). No numeric here represents
   any measured device's noise floor.
6. **Radiation-specific magnitudes are Unknown** for the user's device
   family: no GaN/AlGaN Hall-plate neutron dataset exists (claim C14), so
   drift rates, and hence required excitation cadence and window lengths,
   cannot be sized from evidence yet — they are design unknowns for stage
   30/60, not derivable here.
7. **Single-source dependencies**: the radiation-null metallic-Hall
   reference rests on [R071] alone (single fluence/temperature envelope,
   abstract-level access; claim C18); the coil-calibrates-Hall precedent
   rests on [H059] alone (non-fusion, abstract-level; claim C11). Both are
   flagged, not hidden.
8. **No experimental validation is claimed anywhere in this file.** The
   numerical results are synthetic-structure demonstrations; hardware
   language ("proven") is used only for cited external hardware results
   ([H004], [H005], [H003]).

---

## 9. Source support summary

Load-bearing observed evidence: [H004], [H005] (hardware coil-drift
correction from non-integrating reference), [H003], [H007] (same-die
self-test record + limitation), [H059] (coil-calibrates-Hall, driven ramp,
non-fusion), [H021] (bias/state/unknown-input rank condition excluding
gain), [H018], [H019] (excitation-conditional observability analog),
[H034], [H035] (offset residual floor), [H038], [H039], [H040] (embedded/
in-situ calibration references), [H015]–[H017] (bias/unknown-input
estimation methods), [H025]–[H027] (integrator drift), [H041], [H042],
[H064] (absolute references), [H045], [H066] (crossover practice, not
proof), [H047]–[H053] (cross-axis, Mirnov/B-dot limits, saturation, fault
detection, delay), [H065], [P003], [P042], [P013] (steady-state need, OVSS,
persistent-mode NMR reference, stellarator field verification), [R001]–
[R003], [R024], [R042], [R056], [R071], [R072]–[R078] (radiation drift
evidence, RIEMF, metallic Hall, dosimetry practice). Claim-level mapping:
C02–C08, C11, C14, C16, C18, C19, C21, C22, C25, C26, C28, C32, C33.

Everything not tied to a source ID above is this stage's **Derived**
mathematics or is explicitly labeled Inferred/Proposed/Unknown in place.
