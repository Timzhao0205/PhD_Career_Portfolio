# Radiation literature — final review (stage 10D)

Source IDs cite `outputs\01_SOURCE_LEDGER.csv`; claim IDs cite
`outputs\01_EVIDENCE_MAP.csv`. Labels: **Observed / Derived / Inferred /
Proposed / Unknown** per `CLAUDE.md`. Radiation species, spectrum, fluence,
dose, temperature, bias, and annealing state are never merged across sources;
where a number could not be independently read it is flagged, not asserted.

## 1. Mechanism framework (Derived framing)

Three physically distinct damage classes recur and must be kept separate:

1. **Displacement damage** (neutron/proton/electron/heavy-ion): Frenkel
   pairs, clusters, carrier removal, mobility loss, deep traps in the
   semiconductor bulk [R035, R040, R022, R026, R027].
2. **Ionization/TID** (gamma, X-ray, low-LET): trapped charge in oxides,
   insulators, packaging, and analog electronics [R024, R044, R045, R047].
3. **Transmutation** (thermal-neutron capture): permanent element conversion
   — Ga→Ge in GaN [R025]; In/Sb capture products in InSb [R001] (C24).

## 2. Direct Hall-device evidence, material × species (Observed)

- **InSb** (the material fielded at JET/ITER): sensitivity drops under a
  *thermal-inclusive fission* spectrum at ~1e16 n/cm² yet is stable under a
  *purely fast* spectrum at comparable fluence — attributed by the authors to
  transmutation, not displacement (R001, R002) (C12). At 6.6–7.0e17 fast
  n/cm² (~200 °C), thin-film InSb mobility fell 75–90 % (avg 83 %, 9
  samples), carrier-density direction doping-dependent (R003, full text)
  (C13). Consequence (Derived): an integrated-fluence number without spectral
  shape is not a sufficient predictor of InSb Hall drift.
- **GaAs**: conductivity and Hall mobility fall over 1e13–3e15 n/cm² with an
  n/p-inversion signature at the top of that range (R043); Co-60 gamma shows
  a low-dose stabilizing / high-dose degrading split near (8–10)e3 Gy (R009,
  R010); gamma/beta comparison ranks Si/Ge as more tolerant than InSb/GaAs
  via displacement-threshold arguments (R008).
- **Si/SOI**: direct evidence is bulk/detector-grade characterization (R007,
  R020, R021, R040), not packaged sensors; the FD-SOI Hall "radiation
  effects" paper is **TCAD simulation only** (R044 — seed-list error
  documented; simulated TID *raised* sensitivity +29 %) and must never be
  cited as experiment.
- **GaN/AlGaN** (the user's device family): **no bare GaN/AlGaN Hall-plate
  neutron irradiation exists in the peer-reviewed literature — any
  spectrum** (C14, Unknown/gap). The closest direct devices are AlGaN/GaN
  *micro-Hall sensors under protons*: only slightly affected at ~1e13 p/cm²,
  degrading toward 1e16, with **partial** anneal recovery and a cryogenic
  sensitivity-enhancement anomaly (R012–R016; quantitative details
  secondary-sourced). Enabling HEMT/2DEG data quantifies the mechanism: 2 MeV
  protons at 6e14 cm⁻² cut mobility 28.9 % and 2DEG density 12.1 % (R022,
  abstract-confirmed) (C15).
- **Metallic Hall (Cu on ceramic)**: no measurable sensitivity change to
  ~1e18 n/cm², flat 100–250 °C (R071, single source) (C18).
- **Packaged Hall ICs**: TID tolerance 40–100 krad(Si) class, SEE-hard to
  LET 67.7 MeV·cm²/mg in one part, TID-induced errors partly anneal-
  recoverable (R011, R018, R019).

## 3. Cross-species and combined-field warnings (Observed; counterevidence)

1. **NIEL scaling fails across species within one material family:** Co-60
   gamma lifetime damage in InAs/InAsSb is ~14× the proton-scaled prediction
   — proton cascade defects self-anneal; gamma's isolated Frenkel pairs do
   not (R042) (C16). Any proton-test-based projection of gamma (or neutron)
   response for a III-V Hall die is unsafe without a mechanism argument.
2. **Mixed fields are non-additive with structure-dependent sign:** 14 MeV
   neutron + Co-60 gamma in GaN HEMTs gives sub-additive leakage but
   super-additive threshold shift in the cascode structure (R028); mixed
   neutron+gamma in a bipolar OP07 is synergistic (R046) (C17). Single-
   species Hall data cannot be summed to predict a fusion mixed field.
3. **Long-fluence asymptote (Inferred, falsifiable):** heavily proton-
   irradiated InAs/InSb converge to material-specific limiting Fermi levels
   (R037, R038; theory R036) — suggesting bounded rather than divergent
   parameter drift. Proton-only; unconfirmed under neutrons, and C16 warns
   against silent transfer (C23).

## 4. Measurement chain (kept separate from sensor-die physics)

- **Electronics** (C25): bipolar op-amp offset/bias degradation with mixed-
  field synergy (R046); ELDRS-type dose-rate/temperature sensitivity (R047);
  millisecond-scale single-event transients from op-amp bias/startup
  circuitry (R052) — a transient corruption mode distinct from slow TID
  drift; COTS ADC TID/SEU evaluation methodology (R051); the only 1-MGy-class
  rad-hard instrumentation amplifier found is **simulation-only** (R050).
  Current-sense-amplifier TID work exists but content is unverified (R055).
- **Coil chain** (C19): RIEMF in mineral-insulated cable is established by a
  five-paper cluster (R056–R060; theory R059 vs experiment R060 kept
  distinct), with a secondary-sourced ITER target of ≪1 µV non-inductive
  voltage for 3000-s pulses; a separate radiation+thermal-gradient
  core-to-sheath asymmetry is *uncorrelated* with core-to-core RIEMF (R048),
  and copper-core activation (⁶⁶Cu beta decay) is a named, avoidable
  mechanism — steel core sidesteps it (R049). Insulation: matched
  cryogenic organic-vs-ceramic pair (Kapton R061 vs alumina R062); FRP
  interlaminar shear at 4 K (R068). JET's in-vessel Mirnov coils suffered
  real "severe faults" under combined radiation+EM stress driving a Ti→Cu
  redesign (R066) — causal shares not disaggregated. ITER CER effective-area
  calibration is documented (~0.1 mrad axis rig, R069, R070) but **no
  radiation-induced effective-area drift measurement exists** for any coil.
- **Fiber-optic (coil-adjacent alternative)** (C20): the JET FOCS is the
  single strongest real-fusion-field dataset in the ledger — operated through
  DTE2 (~8.5e20 D-T neutrons; ~1.5e12 n/cm²/s peak at the sensor), Verdet
  constant ±4 % shot-to-shot, a possible ~0.7 % campaign drift at low
  statistical confidence, no disqualifying degradation, continuously
  cross-validated against the CER Rogowski (R063 full text; pre-campaign
  baseline H031; gamma-only Verdet study R064; in-pulse fiber attenuation
  R065).
- **Integrator/timing**: quartz-oscillator frequency shift is the only
  verified source (R067, space context) — the thinnest sub-topic in the
  ledger (gap).

## 5. Dosimetry and qualification practice (Observed, C26)

Activation-foil dosimetry is mature and validated: VERDI benchmarked at the
14 MeV FNG reference field (C/E = 1.05 ± 0.13, R076), then validated
in-machine at JET D-D to 8 % (R075); protocol formalized as reference-field
calibration → in-machine validation (R072); TU Dresden's ITER-TBM
foil-activation program explicitly quantifies the surrogate-facility gap —
its test flux sits 3–5 orders of magnitude below full-power ITER-TBM flux
(R073, R074). KSTAR runs a routine activation system (R078). **Derived:** any
Hall irradiation campaign inherits a ready-made dosimetry protocol; the
surrogate-to-target flux gap and the spectral-shape sensitivity (C12) must
both be stated in its design.

## 6. Calibration implications for the state model

Against `y_H = S_H B + b_H + n_H`, `y_C = K_C dB/dt + b_C + n_C`:

- **Modelable now:** TID two-regime (reversible low-dose vs persistent
  oxide-trapping) offset/threshold behavior for GaN-family electronics
  (R024, R033) (C22); RIEMF as an additive coil-chain term of established
  existence but unquantified dose curve (C19); the bounded-asymptote
  hypothesis for III-V parameters (C23, Inferred only).
- **Monitorable now:** fluence/spectrum via activation foils (C26);
  temperature as a first-class state (tracked explicitly in R003, R022,
  R037, R038, R071).
- **Calibratable in principle, undemonstrated in practice:**
  **no source in either lane demonstrates in-situ, during-irradiation
  recalibration of Hall sensitivity against a material-diverse reference,
  for any Hall material (C21, Unknown).** The fielded JET solution (H003/
  H007) is same-die self-test — vulnerable, by construction, to common-mode
  radiation/thermal drift of die and reference together.
- **Required statement (Derived, C06):** the existence of Hall+coil (and
  Hall→coil) drift-correction architectures does **not** prove that
  radiation-induced Hall sensitivity drift can be calibrated in situ. The
  demonstrated direction of correction is coil-drift-from-Hall-reference;
  the radiation problem needs the opposite direction (or an independent
  reference), whose observability is unproven (hybrid review §3–4).
- **Candidate architecture elements the evidence supports (Inferred/
  Proposed):** a metallic-Hall witness channel (R071's null result — single
  source, needs replication), an embedded known-field injection winding
  (H038/H007 lineage), activation-foil dosimetry co-located with the sensor
  (C26), and explicit temperature telemetry. These are design inputs for
  stage 30, not conclusions.

## 7. Gaps (Unknown; carried to stages 30/60/70)

1. Bare GaN/AlGaN Hall-plate neutron response — none exists (C14).
2. 14 MeV D-T direct Hall data — none; FOCS is the only in-machine D-T
   dataset and is not a Hall device (C20).
3. Combined neutron+gamma+temperature Hall dataset — none; non-additivity
   demonstrated only in HEMTs/op-amps (C17).
4. In-situ material-diverse Hall recalibration — unreported (C21).
5. Dose-to-RIEMF and dose-to-effective-area curves — unquantified (C19).
6. Integrator/timing-chain radiation data — single space-context source
   (R067).
7. Metallic-Hall tolerance — single source, one envelope (R071).
