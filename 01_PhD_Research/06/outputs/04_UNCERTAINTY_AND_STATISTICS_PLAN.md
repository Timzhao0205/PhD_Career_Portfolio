# 04 — Uncertainty and statistics plan (Stage 40)

Prepared by: Claude Code, stage `40_experiment`, requested model Fable 5 /
Extra High. Companions:
[`04_HSX_EXPERIMENT_PLAN.md`](04_HSX_EXPERIMENT_PLAN.md),
[`04_DATA_ANALYSIS_PLAN.md`](04_DATA_ANALYSIS_PLAN.md), requirement IDs
from [`04_MEASUREMENT_REQUIREMENTS.csv`](04_MEASUREMENT_REQUIREMENTS.csv).
Norms: GUM-style budget with Monte-Carlo cross-check
([S0220](https://doi.org/10.3390/s25051633)), traceable Hall calibration
reporting ([S0051](https://doi.org/10.5194/jsss-9-391-2020)), Allan-based
drift decomposition ([S0168](https://doi.org/10.1109/TIM.2007.908635))
[EE]. Epistemic labels as in the companions.

**Ground rule (stage prompt + mission):** no sample-size number appears
here without its assumptions shown; expected uncertainty magnitudes are
the 02 plan's stated *expectations* [SF], carried as placeholders until
measured — they are inputs to planning, not results.

---

## 1. Notation and measurement models

Current-bias (2026) chain [SF: SPECS/02-plan model]:

```text
V_demod = m·B_⊥ + b            m = G·L·S_I·I
B̂       = (V_demod − b)/m
```

- G: amplifier gain (nominal 100.3; measured by B-01)
- L: loading factor (~0.83; absorbed into end-to-end m by calibration)
- S_I: current-scaled sensitivity (~60 V/A/T expected)
- I: bias current (measured via R9/R10 + shunt)
- b: demodulated residual offset (C-05)
- k: Helmholtz coil constant, B = k·I_coil (C-01)

Voltage-bias (2023 chain, 2025 data) [SF: C023]:

```text
V_out = A_v·S_v·V_bias·B_⊥ + A_v·V_off(T)
ΔB̂    = ΔV_out /(A_v·S_v·V_bias)        (changes only; V_off unknown)
```

All quantities retain units and uncertainties at every step; any value
lacking a measured basis is labeled `assumed` in the budget tables and
NOT ESTABLISHED FROM SUPPLIED FILES where applicable.

---

## 2. Statistical unit definitions (the hierarchy every claim must name)

| Unit | Definition | Claims it carries | Independence caution |
|---|---|---|---|
| Wafer/lot | Fabrication lineage (2023-gen; gen-2 if it exists) | Population statements (literature-supported only at n_die ≤ 5) | Dies share wafer — not independent draws from "GaN sensors" |
| Die (device) | One Hall plate | Fabrication repeatability (D-01, AE-03) | The AE's unit of "fabrication iteration" [SF] |
| Module | Packaged die (LCC + bonds + encapsulation) | Offset, packaging effects, health tracking (F-07) | Die vs packaging effects separable only with ≥2 modules of one die generation [INF] |
| Channel/board | Module + `hsx_2026_v1` copy + source | Calibration constants m, b; D-03 skew | Constants belong to the *pair*, not the die alone |
| Session/remount | One mounting + calibration epoch | Setup repeatability (D-02) | Remount variance confounds die variance if unmeasured |
| Shot | One HSX discharge/coil event | All in-machine statistics (A-02…A-04, F-01, F-03, F-06) | **The primary in-machine unit**; class and time-order recorded |
| Time-sample | One digitized point | Noise/PSD estimates only | Autocorrelated; never counted as replicates for shot-level claims |

Rule [REC]: every quoted statistic names its unit and its n at that
unit ("m = … ± …, n = 3 sweeps on 1 module"; "transient amplitude CV =
…, n = 14 biased plasma shots"). A number without a unit-and-n label
does not enter a manuscript.

---

## 3. Worked symbolic uncertainty budget

### 3.1 Sensitivity (current-bias calibration, C-02)

```text
u(m)/m = sqrt[ (u(k)/k)^2        coil constant (C-01)
             + (u(I_coil)/I_coil)^2   sweep-current measurement (shunt)
             + u_fit^2            regression SE of slope (measured)
             + u_align^2          cos-error, (1−cosθ) for tilt θ
             + (T_c·u(ΔT))^2      sensitivity tempco × temp uncertainty ]
```

Placeholder magnitudes — **02-plan expectations [SF], to be replaced by
measurement**: u(k)/k ≈ 1.5–2 %; u(I)/I ≈ 0.1 % (0.1 % shunt);
u_fit: measured (expected small at ≥11 points, SPECS SNR);
u_align ≈ 0.15 % (θ < 3°); temperature term 0.1–0.5 %.

Worked example with the placeholder set {2 %, 0.1 %, 0.5 % assumed fit,
0.15 %, 0.3 %}:

```text
u(m)/m = sqrt(0.02^2 + 0.001^2 + 0.005^2 + 0.0015^2 + 0.003^2)
       = sqrt(4.00e−4 + 1.0e−6 + 2.5e−5 + 2.3e−6 + 9.0e−6)
       ≈ 0.0209  →  ≈ 2.1 %
```

**Reading [INF]:** the coil constant dominates (92 % of the variance);
nothing else matters until u(k) improves — which is why C-01
triangulation is a P0 and why buying a better shunt is pointless.

### 3.2 Field estimate from a trace (current-bias)

```text
u(B̂)^2 = (u(V)/m)^2 + (u(b)/m)^2 + ((V−b)/m^2)^2·u(m)^2
```

- u(V): noise + digitizer quantization over the analysis bandwidth
  (B-05/A-05; the 8-bit-scope quantization that limited the C016
  emulator residual to ≤5 mV is the cautionary precedent [SF])
- u(b): zero-field residual spread + drift allocation between checks
  (C-05, C-08 Allan interval)
- relative m term scales with signal size: dominant at HSX field levels
  (V−b ≈ 0.25–0.3 V expected [SF: SPECS]); u(b)/m dominates near zero.

### 3.3 Retroactive 2025 conversion (voltage-bias, G-01)

```text
u(ΔB̂)/ΔB̂ = sqrt[ (u(S_v)/S_v)^2          C-03 calibration
               + (u(A_v)/A_v)^2          gain-200 basis (gate I-6)
               + (u(V_bias)/V_bias)^2    nominal, unlogged setting [SF: C022]
               + u_transfer^2            sibling-die term if same die unavailable (from D-01 spread)
               + u_Voff_drift^2          V_off(T) stability over the analysis window (C-07 × ΔT bound)
               + (u(ΔV)/ΔV)^2 ]          trace noise/quantization
```

No placeholder total is quoted: u_transfer and u_Voff_drift have **no
supplied basis at all** today and are exactly what C-03/C-07/D-01 exist
to measure. The budget's honesty feature: if the deployed die is lost
(gate I-4), u_transfer is bounded by measured die-to-die spread — and if
that spread is large, the conversion bands get visibly wide, which is
the truthful outcome AE-05 explicitly tolerates [SF: decision letter].

### 3.4 Coil-only anchor comparison (F-01)

```text
u_joint^2 = u(B̂)^2 + u(B_vac,model)^2 + (|∇B|·u_pose)^2 + (B·sinθ̄·u_θ)^2
```

u(B_vac,model) and |∇B| at the pose must come from UW (asks U-4/U-3) —
they are [GATE] inputs, not assumptions this plan invents. Consistency
test: |mean(B̂) − B_vac| ≤ 2·u_joint, with the shot-to-shot spread of B̂
reported separately as the repeatability of the anchor.

### 3.5 Method

First-order GUM propagation as above for reporting; Monte-Carlo
propagation ([S0220]) as the cross-check whenever a term is
non-Gaussian (quantization, bounded systematics like alignment) or the
model is nonlinear (matrix calibration later, project 03 scope);
correlated terms (e.g., k and I_coil both using the same DMM) handled by
either measuring with independent instruments or propagating the
covariance — the choice recorded per constant [REC].

---

## 4. Replication logic — how much repetition is enough, and why

**Principle:** replicate where the variance of interest lives (§2), and
report the information content of small n honestly rather than
pretending significance. Formulas first, numbers only as conditional
illustrations.

### 4.1 Precision of an SD from n replicates
Relative standard uncertainty of a sample SD (normal approximation):

```text
u(s)/s ≈ 1/sqrt(2(n−1))     n=3 → 50 %   n=5 → 35 %   n=10 → 24 %
```

**Consequence for D-01 [INF]:** n=3 dies (the AE's own number [SF])
estimates die-to-die spread to only ~±50 % relative — sufficient to
*bound* variability and to catch an outlier die, insufficient for a
population claim. The manuscript therefore reports the D-01 spread as a
bound with n stated, and population statements lean on literature
([S0218](https://doi.org/10.3390/jsan2010085),
[S0004](https://doi.org/10.1109/JSEN.2019.2895546)) [REC].

### 4.2 Precision of a mean
CI half-width = `t_{n−1,0.975}·s/√n`: n=3 → 2.48·s; n=5 → 1.24·s;
n=10 → 0.72·s. Used to size C-02 sweep repetitions: the target
"u_fit ≤ 0.5 %" is checked against the achieved s across ≥3 sweeps, and
repetitions are added until the CI half-width of m meets the target —
an adaptive rule, not a fixed magic n [REC].

### 4.3 Sensitivity (minimum detectable difference) for shot contrasts
Two-condition comparison with n shots/cell and between-shot SD s
(α = 0.05, power 0.8, two-sample z-approximation):

```text
detectable Δ ≈ 2.8·s·sqrt(2/n)
```

Conditional illustration (assumption clearly labeled): **if** the A-02
analysis finds between-shot amplitude CV ≈ 10 % — a value with no
supplied basis today; it is measured by A-02 — then n=3/cell detects
only Δ ≈ 23 % effects; n=6 detects ≈ 16 %. **Consequence [REC]:** the
F-03 matrix asks for ≥3/cell as the floor that makes an SD estimable at
all (2 degrees of freedom), prioritizes repeats of one class over
taxonomy breadth, and defers exact power statements until A-02 supplies
s from the 2025 archive — that is the power-analysis input this plan
refuses to invent.

### 4.4 Where each replicate count in the CSV comes from
- ≥3 dies (D-01): the decision letter's own request [SF] + §4.1 bound
  logic.
- ≥3 repeats within die/remount (D-01/D-02): minimum df for a
  within-unit SD; separates within- from between-unit variance in the
  simplest two-level decomposition.
- ≥11 field points (C-02): the 02 plan's sweep design [SF]; also gives
  ≥9 residual df for the linearity claim.
- ≥3 shots per anchor setting (F-01): SD of the anchor estimable; two
  settings test scale linearity with the minimum that can reveal a
  slope error [INF].
- ≥5 shots for trigger-offset statistics (F-04): jitter SD to ~±35 %
  relative (§4.1), adequate for a timing term that must merely be ≪ the
  claimed lags [INF].
- Census analyses (A-01…A-05): n is fixed by the archive, not chosen;
  reported, never padded.

### 4.5 Variance decomposition
Two-level model for D-01/D-02 (die i, repeat j):
`y_ij = µ + d_i + ε_ij`, Var(d) = between-die, Var(ε) = within
(remount + measurement). Report both components (ANOVA/REML point
estimates with the §4.1 caveat at these n); D-02's remount-only data
identifies Var(ε) so D-01's between-die component is not inflated by
fixturing [INF]. The same structure reads onto shots (class i, shot j)
for F-03.

---

## 5. Sensitivity analysis of the budget and the plan

1. **One-at-a-time doubling:** double each §3.1/§3.3 term and recompute
   u_total — ranks the terms; with the placeholder set, only u(k)
   materially moves the total (doubling it moves u(m)/m from 2.1 % to
   ≈4.0 %; doubling any other term moves it by <0.2 pp) [INF].
2. **Threshold questions asked in advance [REC]:**
   - If C-01 triangulation disagrees beyond stated uncertainties →
     stop, find the error; do not widen u(k) to cover disagreement.
   - If measured noise ≫ the 25–30 µT expectation → revisit bias point
     (C-04) and EMI (B-06) before quoting a floor.
   - If D-01 spread is so large that u_transfer swamps the G-01 budget →
     the sibling-die conversion is *not* published as tesla; fall back
     to the bounds-only language (CSV G-01 fallback).
   - If the F-01 anchor misses 2·u_joint → treat as a finding
     (installation, pose, model, or physics), not a nuisance; the
     stage-20 falsifiability register applies [SF].
3. **Monte-Carlo consistency:** report both GUM and MC intervals for the
   headline numbers; discrepancy >20 % of the interval width triggers a
   model review ([S0220] practice) [REC].
4. **Assumption ledger:** every `assumed` entry in the budget tables
   carries its planned replacement measurement (requirement ID) — the
   budget is finished only when no load-bearing term is `assumed`.

---

## 6. Limitations language when ideal replication is impossible

Pre-drafted, honest formulations [REC] — to be adapted, never silently
dropped:

1. **Single-device case (D-01 fallback):** "Repeatability data are
   reported for the single packaged module available in this study
   (remount repeatability, n = … cycles); they characterize this
   instrument, not die-to-die fabrication variability. Fabrication-
   iteration statistics from comparable AlGaN/GaN Hall processes are
   summarized from the literature [S0004, S0218]; extending them to
   this device family is an assumption we state rather than test. The
   single-module deployment reflects …" (team-record reason — a [GATE]
   input; never invented).
2. **Shot-count and non-randomized conditions:** "Shot conditions
   followed facility scheduling; bias states were interleaved but not
   randomized. Reported contrasts are observational, with run order
   recorded and time-order trends checked."
3. **Field-range extrapolation (E-03 unmet):** "Bench calibration spans
   ±2.7 mT; in-machine fields at the probe are ~0.5 T. Linearity beyond
   the bench range rests on [the F-01 anchor / literature 2DEG
   linearity], and the calibration uncertainty quoted at HSX fields
   includes this extrapolation term explicitly."
4. **Sibling-die conversion (I-4 fail):** "The 2025 traces were
   converted using a same-wafer sibling die calibrated in the deployed
   bias configuration; the die-transfer term in the budget uses the
   measured die-to-die spread (n = …) and dominates the stated
   uncertainty."
5. **Temperature unknown in 2025 (F-05 fallback):** "Sensor temperature
   during the 2025 shots was not instrumented; the conversion assumes
   |ΔT| ≤ … (worst case, stated), contributing … to the band."
6. **Anchor unavailable (campaign slip):** "No in-machine absolute
   cross-check was available for this dataset; absolute-field statements
   derive from bench traceability alone, with the machine anchor
   identified as planned validation."

Each statement pairs a claim boundary with the measurement that would
remove it — the reviewer-facing form of this plan's gate structure
[INF]. JET's multi-year 18-sensor stability record
([S0068](https://doi.org/10.1088/1741-4326/ac8aad)) remains the field's
bar and is cited as context, never implied as met [EE].
