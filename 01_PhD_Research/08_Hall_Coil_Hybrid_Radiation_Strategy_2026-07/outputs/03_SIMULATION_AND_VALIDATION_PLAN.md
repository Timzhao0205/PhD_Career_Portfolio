# 03 — Simulation and validation plan

Stage 30 (`30_radiation_compensation`). Produced and signed off by Fable 5
(xhigh). Source/claim IDs cite `outputs\01_SOURCE_LEDGER.csv` /
`outputs\01_EVIDENCE_MAP.csv`; stage-20 CASE references cite
`outputs\02_OBSERVABILITY_AND_IDENTIFIABILITY.md`. Architecture context:
`outputs\03_RADIATION_COMPENSATION_ARCHITECTURE.md` (cited as ARCH §x).
Labels: **Observed / Derived / Inferred / Proposed / Unknown**.

---

## 1. Purpose and evidence-class boundary (binding)

This plan specifies (a) a simulation package precise enough for a later
implementer to build **without inventing any scientific model content**,
and (b) the staged experimental ladder that can falsify the ARCH concept
at the lowest possible cost.

**Three evidence classes are never mixed (per `CLAUDE.md` and
`SOURCE_POLICY.md`):**

| Class | What it can establish | What it can never establish |
|---|---|---|
| **Simulated** (rungs 1) | estimator correctness, structural identifiability behavior, fault-logic coverage, uncertainty-propagation correctness | any device physics; any drift magnitude; any claim of "validation" of the concept against reality |
| **Bench** (rungs 2–4) | non-radiation identifiability conditions in hardware; noise floors; temperature coefficients; reference traceability; emulated-drift recovery | radiation response of anything |
| **Radiation** (rungs 5–6, collaborator-led) | species/spectrum-specific drift magnitudes `f_S,s`, `f_b,s`; compensation closure under real damage | nothing about species/spectra not actually used (C16: cross-species scaling can err ~14×; C17: mixed fields non-additive) |

Simulation results are always reported as "synthetic"; the phrase
"experimental validation" is reserved for rungs 2+ hardware results.
Rungs 5–7 are outside the user's current first-author HSX scope
(ARCH §9.4; `00_CONFLICT_LEDGER.md` C6).

---

## 2. State-space specification

**Proposed** (implements ARCH §2 exactly; a coder implements these
equations verbatim — no scientific choices are left open, only numerical
ones).

### 2.1 Continuous-time truth model

States `x`, inputs `u`, outputs `y`:

```text
Field:        B(t)                          [T]   (scenario-defined input trajectory)
Injection:    B_inj(t) = G_cal(t)·I_cal(t)  [T]   (u: I_cal; state: G_cal)
Integrator:   dx_I/dt = −x_I/τ_L + g·d(B+B_inj)/dt + m(t)

Hall gain:    S_H(t) = S_H0·[1 + α_S·ΔT(t) + f_S(Φ(t)) + h_S(a(t))] · (1 + w_S(t))
Hall offset:  b_H(t) = b_H0 + β_b·ΔT(t) + f_b(Φ(t)) + h_b(a(t)) + w_b(t)
Coil gain:    K_C(t) = K_C0·[1 + α_K·ΔT(t) + f_K(Φ(t))] · (1 + w_K(t))
Coil offset:  b_C(t) = b_C0 + β_c·ΔT(t) + r_RIEMF·φ̇(t) + w_c(t)
Cal transfer: G_cal(t) = G_cal0·[1 + α_G·ΔT(t) + f_G(Φ(t))] · (1 + w_G(t))
Drift rate:   m(t)   = m0 + w_m(t)
Annealing:    da/dt  = −a/τ_a(T) + κ(T)·dΦ_ann/dt        (hysteresis state; see 2.4)

Outputs:
  y_H = S_H·(B + B_inj) + b_H + n_H                      [V]
  y_C = K_C·(h_C ∗ d(B+B_inj)/dt) + b_C + n_C            [V]  (direct mode)
  y_I = x_I + n_I                                        [V]  (integrated mode)
  y_T = T + n_T                                          [K]
  y_R = R_H(t) + n_R                                     [Ω]  (R_H = R_H0·[1 + γ_R·ΔT + f_R(Φ)])
  y_D = Φ(t_read) · (1 + n_D)                            (fluence, read only at retrieval epochs — foils, C26)
```

`h_C` is a first-order low-pass with pole `ω_C` plus pure delay `δt_C`;
the Hall channel optionally gets pole `a_H` and delay `δt_H` (case-9
scenarios). All `w_•(t)` are independent random walks or OU processes
with intensities `q_•` (config); all `n_•` are white Gaussian with
variances `σ_•²` (config). Species indexing: `Φ` is a **vector** over
species s; every `f_•` takes the vector and applies per-species curves —
the package must refuse a scalar-fluence config when more than one
species is nonzero (enforces C16/C17 discipline programmatically).

### 2.2 Radiation response functions `f_•(Φ)` — placeholder policy (binding)

**No GaN/AlGaN Hall-plate neutron response exists (C14).** The package
therefore ships with *labeled placeholder families*, never presented as
device predictions:

- `f = 0` (null case);
- linear `f = c₁·Φ_s`;
- saturating `f = c_sat·(1 − exp(−Φ_s/Φ_0))` — the bounded-asymptote
  *hypothesis* (Inferred, C23, proton-only basis [R036]–[R038]);
- piecewise/two-regime (TID-like, C22 basis [R024]);
- user-supplied tabulated curve (the rung-5 output slot).

Config files must carry a `basis` field per curve:
`{placeholder | literature:<source_id> | measured:<dataset_id>}`. Any
figure or report generated from `placeholder` curves must carry a
"synthetic placeholder — no device basis" watermark string. (Derived
requirement from the C14 gap; prevents the simulation from silently
becoming fake device evidence.)

### 2.3 Discretization and estimator-side model

Truth model integrated at `dt_sim`; measurements sampled at `dt_H`,
`dt_C` (allowing inter-channel skew `δt` injection). The estimator (ARCH
§6.1) uses the *same equations* with states
`[B, x_I, b_H, b_C|m, τ_L, s_H, k_C]` and treats anchors/lock-in outputs
as scheduled measurements. Estimator-model mismatch scenarios (S9) use a
deliberately reduced estimator model against the full truth model.

### 2.4 Annealing/hysteresis state

`a(t)` accumulates during exposure and relaxes with
temperature-dependent `τ_a(T)`; recovery fraction capped (`h_S` recovers
only a configurable share, transmutation share non-recoverable —
structure per C22/C24 evidence; all rate constants are placeholders per
§2.2 policy). Purpose: reproduce the CASE J window-validity problem so
the estimator's windowed attribution logic can be tested — not to
predict any real device.

---

## 3. Parameter schema

**Proposed** config schema (one namespace per block; YAML/JSON; all
fields required, units in-name):

```text
hall:      S_H0_V_per_T, b_H0_V, R_H0_ohm, alpha_S_per_K, beta_b_V_per_K,
           gamma_R_per_K, sigma_H_V, q_S, q_b, pole_a_H_rad_s|null,
           delay_s, f_S{basis,type,params[per species]}, f_b{...}, f_R{...},
           anneal{tau_a_s(T)_params, kappa_params, recoverable_fraction}
coil:      K_C0_Vs_per_T, b_C0_V, alpha_K_per_K, beta_c_V_per_K,
           sigma_C_V, q_K, q_c, pole_w_C_rad_s, delay_s,
           riemf_r_V_per_flux_rate|0, f_K{...}
integ:     g, m0_V_per_s, tau_L_s, x_I0_V, sigma_I_V, q_m
calwind:   G_cal0_T_per_A, alpha_G_per_K, q_G, f_G{...},
           R_cal_ohm, R_th_K_per_W        (heating model, ARCH §5.3)
inject:    waveform{sine|toggle|prbs|off}, f_inj_Hz, I_amp_A, T_int_s,
           schedule
env:       T_profile, Phi_profiles[per species], dose_rate_profiles,
           correlation_controls (for CASE J scenarios)
refs:      machine_anchor{schedule, dB_levels_T[>=2], dBdt_values[>=2],
           ref_error_rel, position_error, timing_skew_s},
           zero_field{schedule, ambient_residual_T},
           bench_absolute{uncertainty_rel},
           dosimetry{CoverE_mean=1.05, CoverE_sd=0.13 basis C26, read_epochs}
sim:       dt_sim_s, dt_H_s, dt_C_s, skew_s, duration_s, seed, solver
estimator: variant{MVD|HA|HA+witness}, q_priors, freeze_policy,
           fault_thresholds
```

Defaults ship as `placeholder` basis; nothing in the schema encodes a
claimed GaN number. Bench-measured values (rung 2+) enter as
`measured:<dataset_id>` with the dataset archived beside the config.

---

## 4. Scenario matrix

Each scenario states its stage-20 anchor so expected estimator behavior
is pre-registered (Derived from stage 20, not tuned after the fact):

| ID | Scenario | Truth setup | Pre-registered expected behavior |
|---|---|---|---|
| S1 | Unreferenced pair, everything drifting | no anchors, no injection | CASE A: estimator must freeze gains/offsets, report ρ only; honesty test T-NI applies |
| S2 | Vacuum-shot anchoring cycle | machine anchor per schedule, ≥2 levels + ramp/flat-top | CASE D: all four parameters recovered within CRLB-class bounds at each epoch |
| S3 | Quasi-static flat-top, no injection | dB/dt ≈ 0 window | CASE F: uncertainty growth exactly as budgeted; no spurious convergence |
| S4 | Quasi-static + injection ON | S3 + spectrally clean tone | CASE E: gain products tracked through flat-top; b_H untouched (stays frozen) |
| S5 | Spectral collision | ambient line at/near f_inj | CASE E-collide: collision detector fires; gain tracking deweighted, not corrupted |
| S6 | Radiation drift ramp, T decorrelated | f_S ramp (placeholder curve), independent T excursions | CASE J-decorr: attribution splits kT vs kD within CI |
| S7 | Radiation drift ramp, T ∝ Φ | correlated histories | CASE J-corr: attribution reports conditioning failure (no silent split) |
| S8 | Common-mode gain event | S_H and K_C shifted together between anchors | Theorem 1: NO in-pair alarm expected; next anchor epoch must catch and re-anchor; report flags the blind interval |
| S9 | Model mismatch | truth has pole/delay/nonlinearity absent from estimator model | residual/χ² flags; no false drift attribution (confounding 6 heuristic only) |
| S10 | Annealing window | exposure stop → recovery with T history | windowed attribution validity enforced (C22-driven logic) |
| S11 | Integrator-only stress | m, τ_L drift, constant-ramp segments | CASE I vs I-ramp: g·r+m confound reproduced and resolved only when dB/dt varies |
| S12 | Long-duration soak (synthetic twin of rung 4) | slow drifts everywhere, realistic anchor cadence | end-to-end uncertainty budget matches ensemble truth-error statistics |

## 5. Fault-injection catalog

Injectable at configurable onset/magnitude/shape (step, ramp, sag,
burst):

F1 Hall gain step/ramp; F2 Hall offset step/ramp; F3 coil gain
step/ramp; F4 integrator drift-rate step; F5 integrator leak change;
F6 common-mode Hall+coil gain shift (Theorem-1 probe); F7 cal-chain
drift `G_cal` (reference degradation, ARCH §5.4); F8 loss/partial loss
of injection current; F9 RIEMF ramp on `b_C` (flux-rate-correlated);
F10 SET-like ms transients on either channel ([R052] class); F11
saturation/clipping of coil readout (case 9); F12 timing-skew step;
F13 zero-field-epoch contamination (ambient residual ≠ 0, RR-24);
F14 witness-channel failure (top tier: voting must not be fooled).

Every fault has a pre-registered expected detector response
(which alarm, max latency class, and what must NOT fire — false-
attribution guards). Coverage matrix (fault × detector) is a shipped
test artifact.

---

## 6. Reference datasets

1. **Synthetic truth sets:** generated by the package itself with pinned
   seeds/configs (one per scenario S1–S12); archived as
   `datasets\synthetic\<scenario>_<config_hash>`.
2. **Bench datasets (rungs 2–4 outputs):** schema-defined slots
   (`measured:<dataset_id>`) — raw channel streams + reference logs +
   environment telemetry + calibration-ledger entries. None exist yet;
   the package must run fully without them (Unknown until rung 2).
3. **Machine waveform templates:** field/current waveform *shapes* may
   be drawn from the folder-07 HSX shot archive (coil-current logs) as
   scenario inputs, clearly labeled as waveform templates — never as
   sensor-truth data (the 07 folder is read-only context; no value from
   it becomes a claimed measurement of this architecture).
4. **No fabricated data:** the package contains no dataset presented as
   a device measurement; placeholder-basis outputs carry the §2.2
   watermark. (Binding.)

---

## 7. Metrics

| ID | Metric | Definition | Used at |
|---|---|---|---|
| M1 | Field accuracy | RMSE and max-error of `B̂` vs truth, absolute and relative-to-anchor | S2–S12, G0/G1 |
| M2 | Parameter recovery | bias and variance of each parameter estimate vs truth; ratio to CRLB from the stage-20 FIM machinery | S2, S4, S6, S11 |
| M3 | Coverage honesty | fraction of time truth lies inside reported 1σ/2σ intervals (target: nominal within stated tolerance) — the headline honesty metric | all scenarios |
| M4 | Detection performance | per-fault detection latency and missed-detection rate at fixed false-alarm budget (ARL-style) | F1–F14 |
| M5 | Attribution accuracy | confusion matrix over {Hall gain, Hall offset, coil gain, integrator, reference-chain, common-mode/none} | S6–S9, F-catalog |
| M6 | Non-identifiability honesty (T-NI) | in S1/S3/S8 blind intervals: estimator must NOT reduce reported variance below the open-loop growth curve; any "convergence" in a proven-unidentifiable direction = FAIL | S1, S3, S8 |
| M7 | Closure residual behavior | ε_Δ (ARCH §5.5) null under drift, non-null under path faults F7/F8/F11 | S4–S5, F7/F8/F11 |
| M8 | Budget fidelity | end-to-end reported uncertainty vs ensemble truth error over ≥100-seed Monte Carlo | S12, G0 |

## 8. Test suite

- **Unit:** each model equation vs closed-form solutions (integrator
  response, lock-in output for known tone, annealing relaxation);
  schema validation (species-vector enforcement; basis-field
  enforcement).
- **Regression:** reproduce stage-20 rank results by running
  `tools\observability_rank_tests.py` (kept reusable at stage 20)
  against the package's Jacobians — CASE A/B/C1/C2/D/D-flat/E/
  E-collide/F/G/H/I/I-ramp/J must match rank-for-rank. This binds the
  package to the proven structure (no silent model drift).
- **Acceptance:** scenario matrix S1–S12 with pre-registered behaviors;
  fault coverage matrix; M3/M6 honesty gates. A run report is generated
  per config hash.
- **Estimator-abuse tests:** deliberately mis-specified priors must not
  produce confident wrong answers in unidentifiable directions (extends
  T-NI).

## 9. Reproducibility

Pinned dependencies; single-command run per scenario; every artifact
tagged with `config_hash` + seed; deterministic solvers (fixed-step for
truth model); all randomness via one seeded generator; CI-style script
that re-runs unit+regression suites; outputs include the exact config
copy. No wall-clock or machine-dependent values enter results.

---

## 10. Staged experimental ladder (rungs, gates, stop rules)

Rung numbering follows the stage prompt; gates G0–G5 are the tier gates
of ARCH §9. Calibration standards are named generically where the
evidence base contains no specific instrument (no vendor items are
invented); sample sizes are given only where a defensible basis exists,
otherwise stated as TBD-at-gate with the determining quantity named.

**Rung 1 — Simulation / synthetic fault injection (T0; gate G0).**
Deliverables: §4–§8 complete, all pre-registered behaviors met.
Acceptance: M1/M2 within CRLB-class factors on identifiable scenarios;
M3 coverage nominal ±stated tolerance; M6 zero violations; fault matrix
coverage complete. Stop rule: targets unreachable with *perfect*
references → architecture redesign, no hardware spend.

**Rung 2 — Benchtop static/dynamic field + temperature (T1; gate G1).**
Setup: existing Hall device + wound/PCB coil + precision current
source/Helmholtz-class field generation + controlled temperature +
traceable transfer standard ([H041], [H042], [H064] class chain).
Protocol: full anchored-hybrid calibration (CASE D bench analog: ≥2
field levels, ramp+flat-top waveforms; zero-field offset reads);
temperature coefficients `α_S, β_b, α_K` mapped over the operating
range; noise floors and `R_H` telemetry baselined.
Repeatability: ≥3 full calibration cycles per condition (Proposed;
separates cycle repeatability from drift); acceptance: cycle-to-cycle
scatter consistent with the rung-1 predicted uncertainty (M8 logic on
real data). Stop rule: unexplained excess scatter → halt, diagnose
before adding hardware.

**Rung 3 — Controlled offset/gain emulation (T2 entry; gate G2).**
Method: electrically emulate drifts (bias-network trims, series/shunt
perturbations, integrator-offset injection) so *known* parameter changes
challenge the estimator on real hardware — no radiation involved.
Acceptance: emulated steps/ramps of gain and offset recovered within
reported CI (M2/M5 on hardware); collision detector validated by
deliberately placing an interfering tone (S5 analog). Stop rule: if the
HA layer (winding + lock-in) cannot resolve emulated drifts smaller
than the drift resolution target set at G1, the winding layer is
descoped (ARCH §9 T2 stop rule).

**Rung 4 — Long-duration drift test (T2; gate G3).**
Multi-day-to-multi-week powered soak with periodic scheduled anchors,
continuous lock-in tracking, thermal excursions decorrelated by design
(CASE J-decorr rehearsal). Acceptance: closure residual (M7) stable;
between-anchor uncertainty growth matches budget; every alarm traceable
to a logged cause. Sample size: TBD at G2 (determined by rung-3 variance
estimates); duration: set by the drift-band definition (must span ≥
several `1/ω_d` periods of the slowest modeled drift).

**Rung 5 — Material/device radiation screening (T3; gate G4;
collaborator-led).** Purpose: measure `f_S,s`, `f_b,s`, `f_R,s` for the
actual device family — the C14 gap. Design constraints from evidence:
species/spectrum must match the claim target (C12: spectral shape
changed the InSb outcome qualitatively; C16: no cross-species
substitution); dosimetry per the validated foil protocol
(reference-field calibration → in-situ foils; C/E = 1.05 ± 0.13 class,
C26); temperature logged throughout ([R003], [R071] practice); bias
state recorded (`SOURCE_POLICY.md`); pre/post van der Pauw
decomposition (mobility vs carrier density, [R003] method); control
(unirradiated) devices held back. Sample size: ≥5 irradiated + ≥3
control devices per material/condition (Proposed; scale consistent with
the 9-sample InSb campaign [R003] — defensible as a minimum for a mean
drift curve with outlier rejection, not for population statistics).
Acceptance: drift curves with stated uncertainty enter the package as
`measured:` curves. Stop rules (either direction is decisive):
drift below in-situ detection floor → in-situ recal unnecessary,
simplify architecture (good outcome); drift large/non-monotonic/
unattributable → hybrid compensation falsified for that material;
pivot per ARCH §9 T3 stop rule.

**Rung 6 — Collaborator-led neutron/gamma qualification (T3; gate G5).**
Only if G4 passes. Full head (Hall + coil + winding + witness +
dosimetry) under representative exposure with in-situ anchors per the
FOCS qualification template (the only in-machine D-T radiation-effects
dataset in the ledger, C20: continuous cross-validation against an
independent reference, pre/post baselines). Acceptance: in-situ
compensation closes to the target accuracy against the independent
reference; every §7 in-situ claim of the ARCH table demonstrated or
amended. No facility, schedule, or access is assumed to exist —
this rung is a specification for a future collaboration agreement.

**Rung 7 — Relevant-machine demonstration.** MVD (non-radiation content)
can demonstrate on a stellarator/tokamak vacuum+plasma cycle
independently of rungs 5–6 — anchoring, offset epochs, integrator
correction, and ρ-alarm need no radiation environment. Full HA radiation
demonstration only after rung 6. Sequencing decisions belong to stage 60.

**Uncertainty budgets at every rung:** the ARCH §6.3 budget table is the
mandatory reporting format from rung 2 onward (reference chain,
between-anchor growth, tracking noise, environmental attribution,
dosimetry where applicable).

---

## 11. Interfaces for the later reusable package

**Proposed module boundary (implements, never re-derives, the science):**

```text
model/      truth-model integrator (§2 equations, config-driven)
schema/     config schema + validators (§3; species/basis enforcement)
estimator/  KF core, lock-in, anchor processors, fault bank (ARCH §6.1)
faults/     injection catalog (§5)
scenarios/  S1–S12 definitions + pre-registered expectations (§4)
metrics/    M1–M8 (§7)
report/     run reports, watermarking (§2.2), budget tables (ARCH §6.3)
tests/      unit / regression (rank-test binding, §8) / acceptance
```

The scientific content an implementer must NOT change without a new
stage-20-class review: the measurement equations (§2.1), the
identifiability-derived freeze policy (ARCH §6.1), the species-vector
discipline (§2.1/§2.2), and the pre-registered scenario expectations
(§4). Everything else (solvers, languages, tooling) is free.

## 12. Limitations

1. Every radiation-response curve in the package is a labeled
   placeholder until rung 5 (C14); the simulation can validate *logic*,
   never device survivability.
2. The plan's attribution tier depends on the unreplicated [R071] null
   result (C18) — rung 5 must include the witness material.
3. Dose-to-RIEMF and dose-to-`G_cal`/`A_eff` curves do not exist in the
   literature (C19; radiation review §4) — rung 6 is the first place
   they could be measured; until then they are budget allowances.
4. Integrator/timing radiation behavior rests on one space-context
   source ([R067]) — treated as unknown, not modeled.
5. Rungs 5–7 assume no specific facility, price, or schedule; none is
   claimed to exist.
