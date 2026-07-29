# 03 — Radiation compensation architecture

Stage 30 (`30_radiation_compensation`). Produced and signed off by Fable 5
(xhigh). Source IDs (`Hxxx`, `Rxxx`, `Pxxx`) refer to
`outputs\01_SOURCE_LEDGER.csv`; claim IDs (`Cxx`) refer to
`outputs\01_EVIDENCE_MAP.csv`. Stage-20 citations (`§x`, `CASE x`) refer to
`outputs\02_OBSERVABILITY_AND_IDENTIFIABILITY.md` and
`outputs\02_MUTUAL_CALIBRATION_FEASIBILITY.md`. Labels: **Observed /
Derived / Inferred / Proposed / Unknown** per `CLAUDE.md`.

**Scope discipline (binding, from `00_CONFLICT_LEDGER.md` C6 and
`MISSION.md`):** everything in this file is a *specification* of what an
architecture and its validation would require. Nothing here commits the
user's current first-author HSX work to any radiation experiment; all
irradiation content is written for a later, coauthored, or collaborator-led
work package. Radiation testing is **not** a prerequisite for any HSX
deliverable in this plan (see §9.4 and the validation plan §10).

---

## 1. Design problem, inherited constraints

Stage 20 fixed the ground rules the architecture must respect (all Derived
there, restated for use):

1. **Theorem 1 (two-parameter gauge group):** an unreferenced Hall+coil
   pair can never identify absolute scale or Hall offset; common-mode gain
   drift is observationally identical to a field change (§3, CASE A).
2. **Direction asymmetry:** Hall→coil correction is hardware-proven
   ([H004], [H005], [P003]; claim C02); coil→Hall works for **gain only**,
   conditionally (trusted coil chain + ΔB excitation, CASE B; single
   non-fusion precedent [H059], C11), and **never for offset**.
3. **Quasi-static blindness:** during flat-top/steady field the pair alone
   provides nothing (CASE F); all calibration value there comes from
   engineered anchors (C04 analog).
4. **Attribution requires diversity:** with everything drifting, detection
   (ρ = S_H/K_C alarm) survives but attribution does not; a third,
   mechanism-diverse channel or an absolute anchor is required (CASE G,
   confounding tests 2 and 6).
5. **Radiation magnitudes for the user's device family are Unknown:** no
   GaN/AlGaN Hall-plate neutron dataset exists (C14); cross-species
   scaling can err ~14× (C16, [R042]); mixed fields are non-additive (C17).
   The architecture must therefore *measure* drift, not assume a model of
   it, and must treat every drift-magnitude number as a parameter to be
   determined by the validation ladder — never as an input taken from
   evidence that does not exist.

The design question is therefore **not** "can the pair self-calibrate"
(answered: no, §3) but **"which minimal set of anchors, references, and
diversity keeps every drift parameter of interest observable at the target
accuracy, at each budget level."** (Derived framing.)

---

## 2. Parameterization

### 2.1 Hall channel

```text
y_H(t) = S_H(t) · [B(t) + B_inj(t)] + b_H(t) + n_H(t)
```

with the drift decomposition (Derived structure; magnitudes per-term
Observed/Unknown as flagged):

```text
S_H(t) = S_H0 · [ 1 + α_S·(T(t)−T0) + f_S,s(Φ_s(t), φ̇_s, T_irr) + h_S(a(t)) ]
b_H(t) = b_H0 + β_b·(T(t)−T0) + f_b,s(Φ_s(t), …) + h_b(a(t)) + w_b(t)
```

- `S_H0` [V/T at fixed bias]: bench-calibrated initial sensitivity;
  absolute value only ever from an external anchor (§3, Theorem 1).
- `α_S` [1/K]: temperature coefficient, pre-characterized on the bench
  (Tier 1); required input for confounding test 5 (CASE J).
- `f_S,s(Φ_s)` : radiation-induced gain drift as a function of fluence
  `Φ_s` **indexed by species/spectrum s** (thermal-inclusive fission,
  fast-fission, 14 MeV D-T, gamma, proton kept strictly separate —
  `SOURCE_POLICY.md` discipline). Observed for InSb: spectrum-dependent,
  transmutation-attributed under thermal-inclusive spectra ([R001],
  [R002], C12) and mobility −75…−90 % at 6.6–7.0e17 fast n/cm² ([R003],
  C13). **Unknown for GaN/AlGaN Hall plates under any neutron spectrum**
  (C14); proton data on AlGaN/GaN micro-Hall sensors exists ([R012],
  [R013], [R015], C15) but must not be scaled across species (C16).
- `h_S(a)` : annealing/recovery term with hysteresis state `a(t)`
  (temperature-history functional). Observed for GaN-family TID: two-regime
  behavior, partial recovery at 200 °C/25 min ([R024], [R033], C22);
  partial anneal recovery of proton-degraded micro-Hall sensors ([R012],
  C15). Transmutation contributions are **non-annealable at service
  temperature** ([R025], [R001], C24) — `h_S` recovers only the
  displacement/ionization share.
- `b_H0, w_b` : residual offset floor and its random walk. Current
  spinning reduces but does not eliminate offset ([H034], [H035], C07),
  so `b_H` stays a free state in every estimator here.
- `R_H(t)` [Ω]: device input/output resistance. Carrier removal and
  mobility loss raise it (Observed for irradiated Hall materials, [R003],
  [R043]); it sets thermal noise `σ_H² ∝ 4kT·R_out·Δf` and shifts the
  bias operating point. **`R_H` is cheaply measurable in situ** (known
  bias current, measured voltage drop) and is carried as an auxiliary
  monitored output — a drift *witness* that requires no field reference
  at all (Derived; see §7).
- `n_H` : noise, variance `σ_H²`; 1/f knee and EMI live in the drift band
  (stage-20 §2.5 convention). Radiation-induced noise increase is a
  monitorable in-situ quantity (§7).
- Bias state during exposure matters and is recorded as a condition
  (Observed as reporting requirement, `SOURCE_POLICY.md`; bias-state
  dependence documented for packaged ICs [R011], [R018], [R019]).

### 2.2 Coil channel

```text
y_C(t) = K_C(t) · (h_C ∗ d[B+B_inj]/dt)(t) + b_C(t) + n_C(t)     (direct)
dx_I/dt = −x_I/τ_L + g·dB/dt + m(t),  y_I = x_I + n_I            (integrated)
```

- `K_C = N·A_eff·G_ro` [V·s/T]: turns × effective area × readout gain.
  `A_eff(T, Φ, t)` drifts via thermal expansion and — under radiation —
  via insulation/former dimensional change. **No radiation-induced
  effective-area drift measurement exists for any coil** (gap recorded in
  the radiation review; effective-area metrology itself is documented,
  [R069], [R070]). Do not assume `A_eff` is radiation-stable.
- `h_C(t)`, phase/bandwidth: coil L/R corner, cable, and anti-alias
  filter; a sampling skew `δt` multiplies the transfer function by
  `e^{−jωδt}` (stage-20 case 9). Verifiable only with overlap-band
  excitation (CASE H-broad vs H-narrow).
- `b_C(t)` : additive chain offset = amplifier offset + thermoelectric
  EMFs + **RIEMF** of mineral-insulated cabling under flux (Observed
  mechanism, five-paper cluster [R056]–[R060], C19; dose-to-RIEMF curve
  unquantified). Core-material choice matters: Cu-core activation
  (⁶⁶Cu β-decay) is a named, avoidable contributor — steel core
  sidesteps it ([R049]).
- Insulation: organic (Kapton [R061]) vs ceramic (alumina [R062])
  radiation tolerance differ; JET in-vessel Mirnov coils suffered real
  faults under combined radiation+EM stress ([R066]). Insulation
  resistance `R_ins(t)` is an ex-situ (or dedicated-megger) check.
- Integrator: `x_I(0)` (unknown start), `g = K_C/τ_i`, drift rate
  `m(t) = V_os(t)/τ_i` (the dominant long-pulse error, [H025], [H004],
  C02), leak `τ_L`. Radiation response of the integrator/timing chain is
  the thinnest evidence area (single space-context quartz source
  [R067]) — treated as a budgeted unknown, not modeled.
- Readout electronics (both channels): op-amp offset/bias degradation
  with neutron+gamma synergy ([R046]), ELDRS ([R047]), millisecond
  single-event transients ([R052]), COTS ADC TID/SEU methodology
  ([R051]) — claim C25. Electronics siting (in-vessel vs remote) is a
  block-level design variable (§4.3).

### 2.3 References and environment states

- `T(t)` : sensor-head temperature, first-class measured state (required
  by CASE J; tracked in the strongest radiation datasets [R003], [R071]).
- `Φ_s(t)` / `D(t)` : fluence per species / ionizing dose. In a machine
  campaign: activation-foil dosimetry co-located with the head (mature,
  validated practice: C/E = 1.05 ± 0.13 at a 14 MeV reference field,
  in-machine validation to 8 % — [R076], [R075], [R072], C26). Foils
  integrate in situ but are **read out ex situ** (§7).
- `I_cal(t)`, `G_cal(T,Φ,t)` : calibration-winding current and transfer
  [T/A]. `I_cal` is bench-traceable (precision shunt + DMM chain,
  Proposed, standard metrology); `G_cal` is geometry — **assumed known
  only at characterization time, never assumed radiation/temperature
  stable** (stage rule; §5.4).
- `I_m(t)`, `G(r)` : machine coil currents and validated vacuum-field
  model — the workhorse absolute anchor (CASE D; stellarator vacuum
  fields verified by e-beam mapping, [P013], C32).
- Absolute bench references: NMR/traceable transfer standards
  ([H041], [H042], [H064]).

---

## 3. Option comparison

Verdicts use stage-20 identifiability results directly. "Covers" means the
option makes the listed drift parameters observable under its stated
conditions; no option is credited with anything CASE-level analysis denies.

| Opt | Architecture | Identifiability basis | Covers | Does NOT cover | Radiation-specific weakness | Cost class (labeled estimate) |
|---|---|---|---|---|---|---|
| A | Hall+coil fusion only, no injected reference | CASE A: rank 5/7 | ρ-alarm (differential drift detection); coil LF correction *if* Hall trusted; field shape | absolute scale, S_H, K_C, b_H; attribution; anything in quasi-static (CASE F) | common-mode drift invisible (Theorem 1) — the radiation failure class | lowest (no added hardware) |
| B | A + embedded cal winding + traceable current source | CASE E: rank 6/7 | S_H·G_cal and K_C·G_cal products (gain tracking incl. quasi-static periods); Hall dynamics (inject near pole); scheduled self-test | b_H (AC injection structurally blind); common-mode of die+winding (C05); absolute scale unless G_cal absolutely known | G_cal itself unreferenced under radiation (no dose-to-geometry data); RIEMF in cal circuit ([R056] mechanism, Inferred transfer) | low-moderate (winding + current ref + demod) |
| C | A + machine-current/field-model reference | CASE D: rank 4/4 | ALL four channel parameters absolutely, per vacuum-shot epoch; b_H via known/zero-field | anything *during* plasma (model invalid); drift between anchor epochs | reference is external to the radiation zone (robust), but cadence-limited: fast drift between vacuum shots aliases | low (uses machine infrastructure; software + logging) |
| D | A + material-diverse redundant Hall channel | CASE G: rank 7/9 | drift attribution via ratio S_1/S_2 + mechanism diversity; three-channel voting; differential radiation term f_1(D)−f_2(D) | absolute scale (null survives); common-mode of all channels; T-vs-dose when histories correlate (CASE J-corr) | rests on single-source radiation-null reference ([R071], C18) — itself unvalidated; in-situ material-diverse recal unreported anywhere (C21) | moderate (second die/material + channel) |
| E | A + periodic external reference calibration (repeated waveform / removal & bench recal) | CASE 6 algebra; CASE D at each recal | gain-drift ratios S^k/S^0, K^k/K^0 between epochs; post-exposure absolute re-anchor | drift *within* an epoch; offset decomposition; anything if waveform reproducibility is poor | removal/handling of activated hardware; epoch cadence vs drift rate unknown (C14) | low-moderate (procedure + logistics) |
| F | Radiation-hard Hall technology alone (no coil) | single channel; no redundancy | DC field with a hard device (metallic Hall: no measurable sensitivity change to ~1e18 n/cm², 100–250 °C, [R071]) | AC/bandwidth; any in-situ drift check (no second channel); fault detection during operation | [R071] is a single source, one envelope (C18); metallic Hall sensitivity is low (its null result is on *stability*, not signal level — practical SNR unquantified in ledger: Unknown); InSb hard only vs fast spectra (C12) | moderate (technology change) |
| G | Coil/optical/other, no semiconductor Hall | n/a (removes the DC channel) | AC field (coil); enclosed current (FOCS, real D-T-campaign evidence [R063], C20); NMR where field is homogeneous/quiet (C28) | local DC field — the requirement that motivates the mission (steady-state machines need non-inductive DC sensing, [H065], C33); FOCS measures enclosed current, not local field (C34) | concedes the measurement objective rather than solving it | varies |
| **H** | **Layered anchor architecture (added): A core + C scheduled anchor + zero-field epochs + B online gain tracking (+ D witness at the top tier)** | composition of CASE D + C2 + E (+ G) | absolute scale per anchor epoch; b_H per zero-field epoch; S_H·G_cal and K_C·G_cal continuously between anchors; triangle closure (§5.5); attribution at top tier | common-mode of *everything simultaneously* between anchor epochs (bounded by anchor cadence); absolute accuracy better than the anchor chain | inherits each layer's weakness but no single-point calibration reference remains | tiered (see §9) |

**Derived comparison summary:**

- No single-reference option is sound under radiation: B's winding is
  unreferenced under dose, C is cadence-limited, D rests on one source,
  E leaves in-epoch blindness. Only the **layered** composition (H) gives
  every drift parameter at least one observable path *and* cross-checks
  each reference against a mechanism-diverse alternative — which is
  exactly what stage 20's feasibility matrix implies (no column except
  the machine-model anchor delivers absolutes; every in-situ scheme is
  change-tracking anchored to an epoch, §2 of the feasibility verdict).
- F and G are not competitive as *architectures* for the mission's
  objective (local DC+AC field under drift stress) but both contribute
  *elements*: F's metallic-Hall device is option D's witness channel;
  G's dosimetry/qualification practice (FOCS template, C20; foil
  protocol, C26) is the validation model.
- A is never sufficient alone but is the estimator core of everything
  above it.

---

## 4. Recommended architectures

### 4.1 Minimum viable design — MVD "anchored hybrid" (Options A+C+zero-field epochs)

**Proposed.** For the user's machine context (a pulsed stellarator with
logged coil currents, e-beam-validated vacuum fields [P013], and
between-shot zero-field access):

- **Hardware:** existing GaN Hall channel (current-spun) + one wound/PCB
  coil on the same axis + co-located temperature sensor + shared,
  time-synchronized DAQ. No new in-vessel actuator.
- **References:** (i) vacuum-shot machine-current anchor (CASE D: all
  four parameters, per anchor epoch; requires ≥2 field levels and a
  ramp+flat-top so dB/dt takes ≥2 values — the CASE I-ramp condition);
  (ii) pre/post-shot zero-field epochs for `b_H`, `b_C` (CASE C2, full
  rank; requires remanent/ambient field controlled or measured —
  assumption flagged, risk RR-24); (iii) an initial bench absolute
  calibration traceable to an NMR-class or equivalent transfer standard
  ([H041], [H042], [H064]).
- **Estimator:** augmented-state Kalman filter with random-walk bias
  states (the C02 direction for integrator drift; structure per stage-20
  CASE1 row of `02_ESTIMATOR_REQUIREMENTS.csv`), plus per-epoch linear
  regressions at anchors, plus the continuous ρ-alarm.
- **What it delivers:** full parameter set re-anchored every vacuum-shot
  epoch; offsets every shot cycle; continuous differential-drift
  detection between anchors. **What it cannot do:** attribute drift
  between anchor epochs, or see common-mode drift between anchors
  (Theorem 1) — accepted at this tier and stated in the uncertainty
  budget (§6.3).

### 4.2 Higher-accuracy design — HA "triangulated self-test hybrid" (H = A+B+C+E, + D at top tier)

**Proposed.** Adds to the MVD:

- **Embedded calibration winding** around/adjacent to the Hall die with a
  traceable current source, spectrally-orthogonal (or toggled) injection,
  and digital lock-in demodulation on **both** channels (§5). Delivers
  continuous relative gain tracking `S_H(t)·G_cal(t)` and
  `K_C(t)·G_cal(t)` — including through quasi-static periods where the
  MVD is blind (CASE F remedy).
- **Repeated-reference-waveform tracking** (Option E, CASE 6 algebra):
  every standard vacuum ramp is regressed against the shot-0 epoch,
  yielding gain-drift ratios with the machine as the (verified-
  reproducibility) excitation source.
- **Top tier only — material-diverse witness channel** (Option D): a
  metallic-Hall (or otherwise mechanism-diverse) die beside the GaN die,
  enabling three-channel voting and differential radiation attribution
  (CASE G + CASE J conditions: measured T, pre-characterized
  coefficients, decorrelated T/D histories). Explicitly contingent on
  replicating [R071]'s single-source null result during the validation
  ladder (risk RR-18).
- **Dosimetry interface (campaign contexts only):** provision for
  co-located activation foils per the validated two-step protocol (C26).
  This is a mounting/geometry provision in the head design, not an HSX
  commitment (§9.4).

### 4.3 Block-level interfaces and measurement equations

**Proposed block diagram (textual):**

```text
[Sensor head — exposed zone]
  B1 GaN Hall die (current-spun bias, 4-wire R_H sense)
  B2 Main pickup coil (air-core; ceramic-insulated MI cable if in-vessel)
  B3 Cal winding (HA only; characterized G_cal; twisted/guarded feed)
  B4 Temperature sensor at die (4-wire)
  B5 (HA top tier) diverse-material Hall die
  B6 (campaign only) activation-foil holder at head
[Cable run] MI or shielded twisted pair; steel-core option per [R049]
[Electronics — remote/shielded zone]
  E1 Hall AFE: spinning-current bias + demod; R_H monitor tap
  E2 Coil AFE: low-drift amp → digitizer (direct) and/or analog
     integrator with characterized (g, m, τ_L)
  E3 Cal source: traceable current reference + waveform DAC + shunt
     readback (I_cal telemetry)
  E4 Shared-clock digitizer (bounds inter-channel skew δt; case 9)
[Software]
  S1 Augmented-state KF (states: B, x_I, b_H, b_C/m, τ_L, [S_H, K_C])
  S2 Lock-in demodulators at f_inj (both channels) → gain products
  S3 Anchor-epoch regressors (vacuum shots; zero-field epochs;
     repeated-waveform ratios)
  S4 Fault bank: innovation χ², ρ-jump, GLR, loss-of-injection,
     triangle-closure residual (§5.5), [voting with B5]
  S5 Ledgered calibration state store (every anchor epoch archived with
     uncertainty; enables post-exposure reprocessing §6.2)
```

**Interfaces (signals, units, requirement class):** `y_H` [V], `y_C` [V],
`y_I` [V], `I_cal` readback [A], `T` [K], `I_m` machine currents [A]
(+ model `G(r)` [T/A]), shot timing/triggers, common clock (skew budget
from case-9 phase term), `R_H` [Ω], all timestamped to one timebase.
Data rates and word lengths are implementation choices bounded by the
simulation plan's parameter schema, not fixed here.

---

## 5. Embedded calibration winding — required analysis

**The stage question: can the winding's field isolate Hall gain and bias
in the presence of an unknown ambient field?**

### 5.1 What injection can and cannot isolate (Derived; CASE E)

With `B_inj(t) = G_cal·I_cal(t)` spectrally orthogonal to ambient
content:

- **Gain: yes, as a product.** Lock-in demodulation of `y_H` at the
  injection frequency estimates `S_H·G_cal` (CASE E, rank 6/7 — both
  gain functions identifiable). Relative gain tracking
  `[S_H·G_cal](t) / [S_H·G_cal](t_0)` is the radiation-monitoring
  quantity of interest and is insensitive to the ambient field entirely.
- **Bias: no — structurally.** The DC null survives every AC injection
  (CASE E): a Hall offset is observationally identical to a static
  ambient shift. Toggled DC injection (`±I_cal,DC`, difference of
  states) measures *gain at the DC operating point* — the difference
  `Δy_H = 2·S_H·G_cal·I_cal,DC` cancels both `b_H` and static ambient —
  but never `b_H` itself. Offset requires zero-field/known-field epochs
  (MVD anchor ii) or an absolute reference. **Any design document
  claiming an embedded winding "calibrates the offset" is wrong**
  (Derived, Theorem 1 β-direction).
- Ambient variation *during* a toggle period leaks into the toggle
  difference; mitigation is fast square-wave toggling with synchronous
  demod, with the main coil as a dB/dt witness to gate/correct toggle
  epochs (Derived).

### 5.2 Frequency plan and lock-in detection (Derived design rules)

- Place `f_inj` in the **overlap band**: above the drift band `ω_d`,
  below the Hall pole, inside the coil's flat response —
  `ω_d < 2π·f_inj < min(a_Hall, ω_C,max)` — and in a measured-quiet
  region of the ambient spectrum. Spectral collision with ambient
  content re-creates the rank deficiency (CASE E-collide: 5/7) — this is
  a hard requirement, not a preference. Machine EMI lines (power
  supplies, spinning-current harmonics) must be surveyed first
  (Hall-sensor EMI susceptibility is documented in adjacent contexts,
  [P021], [P022], C30).
- Coding (PRBS or slow frequency hopping) or on/off toggling makes the
  orthogonality verifiable: the estimator checks that the demodulated
  output tracks the injection schedule (loss-of-injection and
  collision-detection test in fault bank S4).
- Lock-in variance (first-order, matched-filter): for a sine injection
  of amplitude `B_a = G_cal·I_a`,
  `var(Ŝ_H·G_cal) ≈ 2σ_H² / (T_int · I_a²·G_cal²)` — integration time
  `T_int` trades against the drift timescale being tracked
  (quasi-stationarity window, stage-20 assumption 3). Choose `T_int` ≪
  expected drift correlation time; since GaN drift magnitudes are
  Unknown (C14), `T_int` is a *scheduled parameter*, revisited after
  validation rung 5 data exists.
- Coil-side lock-in: the coil sees `d(B_inj)/dt`, amplitude
  `∝ ω_inj·B_a`, so coil-side SNR *improves* with frequency — favoring
  the upper part of the allowed band, jointly optimized against the Hall
  pole margin (case 9: injecting near the pole additionally identifies
  Hall dynamics; CASE H-broad).

### 5.3 Amplitude, heating, EMI (Derived design constraints)

- **Amplitude floor:** `B_a` must give usable lock-in SNR within `T_int`
  (formula above) at the Hall noise floor.
- **Heating ceiling (self-interference):** winding dissipation
  `P_cal = I_rms²·R_cal` raises die temperature by `ΔT_die = R_th·P_cal`,
  which enters the very term (`α_S·ΔT`) the system is trying to
  monitor. Self-consistency condition:
  `|α_S| · R_th · R_cal · I_rms² ≪ δ_S` (target relative-gain
  resolution). This couples winding resistance, thermal design, and
  amplitude; it is a bench-characterizable inequality (Tier 1), and a
  reason the winding cannot simply be driven harder to buy SNR.
- **EMI/coupling:** the injection tone couples into the main coil by
  mutual inductance — this is *used* (§5.5), but also contaminates the
  coil's field measurement at `f_inj`; the demodulator must notch the
  injection line out of the field-estimation path. Injection leads must
  be twisted/guarded so the *cable*, not just the winding, does not
  radiate (RIEMF and pickup discipline as for the main coil, C19).
- Under radiation, the cal circuit itself is exposed: RIEMF adds an
  error current/EMF in the injection loop ([R056] mechanism; Inferred
  transfer — flagged, risk RR-12), and insulation leakage changes the
  delivered `I_cal` unless the readback shunt sits electrically close to
  the winding (design rule: **sense at the winding, not at the source**).

### 5.4 The winding's own reference problem (stage-required; Derived)

`G_cal` is geometry + magnetics. The stage forbids assuming it stays
known, and the evidence supports the caution: **no measurement of
radiation-induced coil-constant/effective-area drift exists for any
coil** (radiation review §4 gap; metrology baseline [R069], [R070]), and
thermal expansion alone changes `G_cal` at the `α_thermal·ΔT` level.
Consequences:

1. Only the **products** `S_H·G_cal`, `K_C·G_cal` are identifiable
   (CASE E). A reference-chain drift is indistinguishable from sensor
   gain drift *within the winding system alone*.
2. The JET RHP record shows the strength and the limit of the same-die
   approach: 11.5 years, SD ≈ 0.07 % sensitivity stability across
   >19,000 pulses including D-T ([H003], [H007], C05) — but a co-located
   same-technology reference cannot by construction detect common-mode
   (shared radiation/thermal) drift of die and winding together (C05
   limitation). Mechanism diversity (geometric constant vs semiconductor
   transport) makes common-mode drift *physically unlikely* but not
   logically excluded (Inferred, stage-20 §5.5).
3. **Resolution in this architecture: triangulation, not trust.** The
   winding is itself referenced against the machine-model anchor at
   every vacuum-shot epoch (CASE D identifies `S_H` and `K_C`
   absolutely; combined with the lock-in products this *solves for
   `G_cal` at each anchor epoch* — Derived). Between anchors, `G_cal`
   drift is bounded by the closure test below, and its residual drift
   rate enters the uncertainty budget explicitly (§6.3) rather than
   being assumed zero.

### 5.5 Triangle-closure consistency test (Derived; added design feature)

The three continuously-available quantities

```text
ρ_HC   = S_H/K_C            (ambient AC cross-regression, CASE A invariant)
π_H    = S_H·G_cal          (Hall-side lock-in)
π_C    = K_C·G_cal          (coil-side lock-in)
```

satisfy the identity `π_H / π_C ≡ ρ_HC` for all t. The **closure
residual** `ε_Δ = π_H/π_C − ρ_HC` is measurable continuously and must be
zero to within noise regardless of drift in any single quantity.
`ε_Δ ≠ 0` indicts the *measurement paths* (demodulator fault, spectral
collision, coil nonlinearity at `f_inj`, injection-line contamination) —
a fault-detection channel that costs nothing extra. Note what it cannot
do: closure holds identically under any {`S_H`, `K_C`, `G_cal`} drift,
so it provides **no drift attribution** — it validates the
instrumentation, not the calibration (consistent with Theorem 1; no
free lunch).

---

## 6. Estimator and compensation logic

### 6.1 Estimator states and structure

**Proposed** (structure per stage-20 estimator-requirements rows;
augmented-bias-state precedent [H015], [H004]):

- **Core filter (always on):** states
  `x = [B, x_I, b_H, b_C (or m), τ_L]`, with `S_H, K_C` held at their
  last anchored values between epochs; random-walk/OU priors band-limited
  below `ω_d`; innovation χ² monitored per channel.
- **Gain-tracking layer (HA):** lock-in outputs `π_H, π_C` as auxiliary
  measurements updating slowly-varying multiplicative states
  `s_H = S_H/S_H^anchor`, `k_C = K_C/K_C^anchor`; the filter treats them
  as direct (noisy) observations of the relative gains, valid under the
  §5.2 orthogonality condition.
- **Anchor-epoch processors (scheduled):** vacuum-shot least squares on
  `[B_ref, 1]` and `[Ḃ_ref, 1]` (CASE D); zero-field offset reads
  (CASE C2); repeated-waveform ratio regression (CASE 6). Each epoch
  writes `{Ŝ_H, K̂_C, b̂_H, b̂_C, Ĝ_cal, cov}` to the calibration ledger
  (S5) with full uncertainty.
- **Fault bank (always on):** ρ-jump alarm; triangle-closure residual;
  innovation χ²; GLR change-point tests on gain states;
  loss-of-injection detector; (top tier) three-channel voting per
  CASE G / confounding test 6. Abrupt-vs-slow signatures are used as a
  *heuristic prior* for failure-vs-drift sorting, never as proof
  (stage-20 confounding row 6).
- **Honesty constraint (binding):** in any regime where stage 20 proves
  non-identifiability (CASE A between anchors, CASE F quasi-static
  without injection), the estimator must **freeze** the corresponding
  states and inflate reported uncertainty, not "converge" on its prior
  (stage-20 §5.3 warning). This is a required behavior, tested in the
  simulation plan (test T-NI).

### 6.2 Four compensation modes (stage-required distinction)

| Mode | Mechanism | Timing | What it corrects | Identifiability basis |
|---|---|---|---|---|
| **Online compensation** | core KF (integrator drift, offsets vs anchors); lock-in gain tracking; ρ-alarm-gated deweighting | continuous | `x_I, m, τ_L, b_C`; relative `S_H, K_C` (HA); field estimate fusion | C02 direction (CASE C2/I); CASE E products; CASE A invariant |
| **Scheduled calibration** | vacuum-shot anchor; zero-field epochs; repeated-waveform ratios; bench recal at maintenance | per shot cycle / run day / vent | absolute `S_H, K_C, b_H, b_C, G_cal`; drift-ratio history | CASE D; CASE C2; CASE 6 |
| **Fault detection** | fault bank S4 (χ², ρ-jump, GLR, closure, loss-of-injection, voting) | continuous | nothing — it *flags*; triggers deweighting, early anchor, or channel exclusion | detection ≠ attribution (confounding 6); attribution only with diversity (CASE G) |
| **Post-exposure correction** | reprocess archived raw data against the calibration ledger: piecewise `Ŝ_H(t)` between anchors interpolated with monotone-in-fluence constraint *only if* rung-5 data supports it; annealing-aware validity windows (C22 hysteresis) | offline, after campaign/exposure | historical field estimates; drift-curve reconstruction `S_H(Φ)` | CASE 6 ratios + anchor epochs; interpolation model is labeled Inferred until rung-5 data exists |

Post-exposure correction is where dosimetry earns its place: fluence from
foils (C26) time-bases the reconstruction; without species-matched
dosimetry the reconstruction cannot claim a dose axis at all (C16).

### 6.3 Uncertainty propagation (Derived budgets)

Every reported field value carries a variance composed of:

1. **Anchor chain:** vacuum-model error `δB_ref/B_ref` maps 1:1 into
   `δS_H/S_H` (CASE D); position error via `∇G·δr`; misalignment enters
   as `S_H·cosθ_m` (inseparable single-axis — budgeted, not estimated);
   current-log accuracy; timing skew into `Ḃ_ref`.
2. **Between-anchor drift:** random-walk growth of frozen states —
   `var(S_H)` grows as `q_S·(t−t_anchor)` with `q_S` set from measured
   drift statistics (bench Tier 1 first, updated by rung-5 data);
   reported, never hidden. This is where Theorem 1's common-mode
   blindness lives in the numbers.
3. **Gain-tracking noise:** lock-in variance (§5.2 formula) plus `G_cal`
   drift-rate allowance (§5.4.3).
4. **Coil-as-reference term (case 2 use):** coil-chain bias `δ(ΔB)`
   enters `δS_H/S_H ≈ −δ(ΔB)/ΔB` multiplicatively; integrator noise
   makes coil-derived `ΔB` a random walk, bounding usable regression
   windows (stage-20 §5.2).
5. **Environmental attribution:** temperature-coefficient uncertainty ×
   ΔT excursion; T–D collinearity penalty when histories correlate
   (CASE J: attribution variance → ∞ as correlation → 1 — reported as a
   conditioning number, not silently regularized).
6. **Dosimetry (campaign):** foil C/E = 1.05 ± 0.13 class uncertainty
   (C26) on the fluence axis; surrogate-to-target flux-gap factor stated
   whenever screening data is extrapolated ([R073], [R074]).

Accuracy claims in this architecture are therefore always of the form
"X % relative to the anchor epoch, growing at the stated rate between
anchors" — no unconditional absolute-accuracy number is claimable, by
Theorem 1 (Derived).

---

## 7. Radiation mechanisms: in-situ measurable vs ex-situ (stage-required)

| Mechanism / quantity | In-situ measurable? | How / why not | Evidence |
|---|---|---|---|
| Relative Hall gain drift `S_H(t)/S_H(t_0)` | **Yes** (HA) | lock-in products; anchor ratios; repeated waveform | CASE E/6; C11 precedent [H059] |
| Absolute `S_H` | **Per-epoch only** | vacuum-shot anchor (machine off-plasma) | CASE D; [P013] |
| Hall offset drift `b_H` | **Per-epoch only** | zero-field epochs; structurally invisible to AC injection | Theorem 1; C07 |
| Hall resistance `R_H` (carrier removal / mobility proxy) | **Yes** | 4-wire bias telemetry; no field reference needed | Derived; mechanism per [R003], [R043] |
| Hall noise spectrum change | **Yes** | quiescent-period PSD monitoring | Derived (monitoring practice) |
| Coil/integrator additive drift (`b_C`, `m`, RIEMF) | **Yes** (given Hall anchor + dB/dt variation) | the C02 hardware-proven direction; zero-dB/dt segments read `b_C` directly | [H004], [H005], C19 |
| Coil gain `K_C` / effective-area drift | **Partially** | `π_C` product + anchor epochs; no in-situ separation of `A_eff` from readout gain | CASE E/D; gap: no dose-to-area data ([R069], [R070] note) |
| Which channel drifted (attribution) | **Only with diversity** | three-channel voting + measured T + decorrelated histories | CASE G/J; C18, C21 |
| Temperature-vs-dose split of a drift | **Conditionally** | measured T + pre-characterized `α_S` + engineered decorrelation | CASE J; C22 hysteresis limit |
| Fluence/spectrum at the head | **Integrating in situ, read ex situ** | activation foils: retrieved and counted after exposure; online per-species spectrometry at the head is not in the evidence base (Unknown) | C26, [R072]–[R076] |
| Mobility vs carrier-density decomposition of a gain drift | **No** | requires van der Pauw / Hall-bar lab measurement | [R003] method |
| Transmutation dopant identification | **No** | materials analysis (post-exposure) | [R025], [R001], C24 |
| Deep-level/trap characterization | **No** | DLTS-class lab work | radiation review §1 |
| Annealing recovery curves | **No** (requires controlled T-history) | furnace/ramp protocols post-exposure | [R024], C22 |
| Insulation resistance / interlaminar integrity | **No** (dedicated test) | megger/mechanical test at maintenance | [R061], [R062], [R068] |
| Readout SET rate | **Yes** (detection) | fault bank catches ms-scale transients; correction is exclusion, not calibration | [R052], C25 |

---

## 8. Cross-sensitivity, common-mode failure, reference degradation

- **Cross-axis response:** single-axis analysis assumed (stage-20 §2.4);
  misalignment inseparable from gain with a single-axis reference —
  budgeted (§6.3.1); bench characterization required (Tier 1);
  vertical-Hall cross-sensitivity evidence [H047].
- **Temperature cross-sensitivity:** first-class state; the J-corr
  failure (T ∝ D → rank 1) is a *scheduling* problem — engineered thermal
  excursions decorrelated from fluence accumulation are part of the
  campaign design, not an afterthought (CASE J-decorr).
- **Common-mode failure classes and their only countermeasures:**
  (i) Hall+coil common gain shift — invisible in-pair (Theorem 1);
  countered only by anchor cadence (C) and mechanism diversity (D);
  (ii) die+winding common shift — invisible to self-test (C05);
  countered by the machine-model anchor;
  (iii) whole-head common environment (T excursion, flux transient) —
  countered by telemetry (T, `R_H`) and post-hoc reprocessing;
  (iv) shared-electronics events (SETs, rail glitches) — countered by
  fault bank + channel-level electrical separation (block design §4.3).
- **Reference degradation:** every reference in this architecture is
  assigned a *degradation observable*: `G_cal` → closure + anchor solve
  (§5.4–5.5); machine-current model → vacuum-shot residuals vs model
  ([P013]-class verification); metallic-Hall witness → its own `R` and
  noise telemetry + ratio consistency (single-source basis flagged,
  C18); zero-field epochs → ambient-field audit (risk RR-24); dosimetry
  → C/E protocol (C26). A reference with no degradation observable is
  not admitted into the estimator (design rule, Derived from stage-20
  §4 feasibility-matrix reading).

---

## 9. Accuracy/cost drivers and budget tiers

No vendor prices are quoted anywhere (none are in the evidence base);
cost classes are order-of-magnitude *labels* (labeled estimate) tied to
`DECISION_FRAMEWORK.md`'s tier structure. Stop/go gates G0–G6 are defined
in the validation plan §10 and summarized here.

| Tier | Content | Dominant accuracy drivers | Dominant cost drivers | Entry gate | Exit (go) gate | Stop rule |
|---|---|---|---|---|---|---|
| **T0 — simulation** | reusable package per validation plan; synthetic fault injection | model fidelity to §2 parameterization; honesty test T-NI | engineering time only | — | **G0:** estimator meets metric targets on identifiable scenarios AND correctly reports non-identifiability on CASE-A/F scenarios | if targets unreachable even with perfect references → redesign before any hardware spend |
| **T1 — bench truth (MVD hardware)** | existing Hall + wound coil + precision current source/Helmholtz + temperature control; traceable transfer standard | reference traceability; temperature-coefficient characterization; noise floors; alignment | bench components; transfer-standard access; time | G0 pass | **G1:** anchored-hybrid calibration repeatable across ≥3 cycles within the T0-predicted uncertainty; `α_S, β_b` characterized | if bench repeatability ≫ prediction and cause not found → architecture assumptions wrong; halt and diagnose |
| **T2 — self-test hybrid (HA hardware)** | + cal winding, traceable current ref, dual lock-in, drift emulation, long-duration soak | `G_cal` characterization; heating ceiling (§5.3); spectral survey quality; emulated-drift recovery accuracy | winding fabrication/characterization; reference electronics; long-run test time | G1 pass | **G2/G3:** emulated gain/offset drifts recovered within CI; closure residual stable over ≥ multi-day soak; drift-attribution logic validated on emulated faults | if injected-reference stability cannot beat the drift resolution target → Option B layer is not earning its complexity; descope to MVD (C-only anchoring) |
| **T3 — environmental qualification (collaborator-led)** | material screening → neutron/gamma qualification with dosimetry, material diversity, pre/post + in-situ protocol per FOCS/foil templates (C20/C26) | species/spectrum match to target environment (C12/C16); dosimetry C/E; sample size; T control during exposure | facility access (never assumed — no facility commitment exists in this plan); collaborator effort; activated-hardware logistics | G3 pass + collaborator agreement | **G4/G5:** screening quantifies `f_S,s` with stated uncertainty; qualification confirms compensation closes the loop at target accuracy | if screening shows drift below the in-situ method's detection floor → in-situ recal is unnecessary (simplify to MVD + scheduled recal: a *good* outcome); if drift is large, non-monotonic, and unattributable → hybrid compensation is falsified for that material; pivot to Option D/F material change |

(Four tiers ≥ the required three; T0 costs no hardware and is the
mandatory first spend.)

### 9.4 HSX-paper decoupling (binding statement)

Tiers T0–T2 and gates G0–G3 involve **no radiation exposure of any
kind** and constitute the complete architecture-validation content
relevant to the user's current first-author HSX trajectory. T3 exists
only as a collaborator-led, later or coauthored work package
(per `MISSION.md` boundary and root scope rule); no output of T0–T2, and
no HSX deliverable, depends on T3 occurring. Radiation results may be
*cited as complementary or outlook* in first-author work, never claimed
experimentally (root `CLAUDE.md` scope rule).

---

## 10. Unresolved engineering risks (summary)

Full register with likelihood/impact/mitigation:
`outputs\03_RADIATION_RISK_REGISTER.csv` (24 rows, RR-01…RR-24). The five
that most threaten the architecture (Derived ranking by
impact × irreducibility):

1. **RR-01/RR-02 — GaN drift magnitude unknown (C14):** every cadence,
   window, and threshold in §5–6 is sized provisionally until rung-5
   screening data exists; the architecture is designed to *measure* its
   way out of this, but cannot be proven sufficient before that data.
2. **RR-13 — common-mode blindness between anchors (Theorem 1):**
   irreducible in-pair; bounded only by anchor cadence and (top tier)
   diversity; the residual is an honest uncertainty term, not a solved
   problem.
3. **RR-12/RR-08 — reference-chain drift under radiation (`G_cal`,
   `A_eff`):** zero direct evidence either way (no dose-to-geometry
   measurements exist); triangulation bounds but does not eliminate it.
4. **RR-18 — witness-channel single-source basis ([R071], C18):** the
   attribution tier rests on an unreplicated null result.
5. **RR-16/RR-17 — planning-level extrapolation traps (C16, C17):** any
   shortcut that sizes the design from proton or single-species data
   risks the documented ~14× class of error; enforced by the
   species-indexing discipline of §2.

---

## 11. Consistency statement

Checked line-by-line against stage 20: every "covers" claim in §3–§7
cites the enabling CASE and inherits its conditions; no claim exceeds the
feasibility matrix (`02_MUTUAL_CALIBRATION_FEASIBILITY.md` §2); the
estimator is required to refuse convergence where stage 20 proves
non-identifiability (§6.1). No statement in this file asserts that any
radiation experiment has been performed by the user or is required for
the user's current first-author work. Simulation is never called
validation; [R050]-class simulation-only sources are not cited as
experimental anywhere in this file.
