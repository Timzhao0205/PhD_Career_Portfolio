# 02 — Mutual-calibration feasibility verdict

Stage 20 (`20_observability`). Produced and signed off by Fable 5 (xhigh).
Basis: the derivations and rank tests in
`outputs\02_OBSERVABILITY_AND_IDENTIFIABILITY.md` (cited below as §x) and
the stage-10D evidence base (`outputs\01_SOURCE_LEDGER.csv`,
`outputs\01_EVIDENCE_MAP.csv`). Labels: Observed / Derived / Inferred /
Proposed / Unknown per `CLAUDE.md`.

---

## 1. Plain-language verdict

**"Mutual calibration" of a Hall sensor and an inductive coil is partly
true, direction-dependent, and misleading if stated symmetrically.**

- **Hall → coil: feasible and the only hardware-proven direction.** A
  calibrated Hall channel can estimate and correct the coil chain's
  integrator initial condition, integrator drift, leakage, and — given
  dB/dt variation — the coil gain, and it supplies the DC/low-frequency
  field the coil cannot see. This direction is hardware-proven outside
  fusion (CERN bench, [H004], [H005]) and deployed at system level (ITER
  OVSS, [P003]) — claim C02 (Observed). Derivation: §5.1, CASE C2/I.

- **Coil → Hall: conditionally feasible for GAIN, never for OFFSET.** A
  trusted coil chain measures field *increments*, which lets a regression
  identify Hall sensitivity in situ — but only when the field actually
  moves (sufficient ΔB excitation), only over windows where the Hall
  parameters are quasi-constant, and only as accurately as the coil chain
  itself is known. The coil can never deliver the Hall offset: a constant
  offset is observationally identical to a static field shift the coil
  cannot see. Offset requires zero-field (or known-field) epochs or an
  absolute reference. Derivation: §5.2 (CASE B); the one real-world
  precedent is non-fusion, driven-ramp ([H059], claim C11, Observed).

- **Both drifting simultaneously: not mutually calibratable.** If Hall
  gain/offset and coil gain/integrator drift are all unknown, the pair has
  an exact two-parameter blind spot (proof: §3, Theorem 1): common-mode
  gain drift is indistinguishable from a genuine field change, and Hall
  offset is indistinguishable from a static field. The pair can *detect*
  that the two channels have drifted apart (the gain-ratio alarm) but
  cannot tell *which* channel moved. Redundancy alone does not attribute
  drift — exactly as `MISSION.md` warned. (Derived; consistent with the
  literature absence, claim C03.)

- **Quasi-static operation is the worst case.** With little field
  variation, the coil carries no information at all and nothing can be
  mutually checked (§5.8, CASE F). This is precisely the long-pulse/
  steady-state regime that motivates adding a Hall channel — so the
  hybrid's calibration value there depends entirely on *engineered*
  excitation and references (embedded calibration coil, reference shots,
  zero-field anchors, current-model checks), not on the pair itself.

**One-sentence answer to the mission question:** the coil can help track
radiation-induced *Hall gain* drift only under a trusted coil chain plus
real field excursions, an external absolute anchor is required at least
once, Hall *offset* tracking requires zero-field epochs, and the
symmetric phrase "the sensors calibrate each other" should not be used in
any manuscript or proposal without these conditions attached.

---

## 2. Feasibility matrix

Verdicts: **F** = feasible (structurally identifiable under stated,
realistic conditions), **C** = conditional (identifiable only with the
listed extra reference/excitation), **N** = not feasible (structurally
unidentifiable). Case numbers refer to
`02_OBSERVABILITY_AND_IDENTIFIABILITY.md` §5.

| Target quantity | Pair alone | + zero-field epochs | + machine current & field model (vacuum) | + embedded cal coil (AC, characterized) | + repeated reference shots | + material-diverse Hall + T/dose proxies |
|---|---|---|---|---|---|---|
| Hall gain `S_H` (absolute) | **N** (§3) | N | **F** (case 4) | **C** — product `S_H·G_cal`; needs reference-chain trust (case 5) | **C** — drift ratio vs shot-0 only (case 6) | N (scale null survives, case 7) |
| Hall gain drift tracking (relative) | **C** — only via trusted coil + ΔB excitation (case 2) | C | F | **F** (spectrally orthogonal injection) | **F** (waveform reproducibility) | **C** — differential attribution (case 7) |
| Hall offset `b_H` | **N** (§3, β-null) | **F** (case 1 anchors) | **F** (vacuum B=0 or known B) | **N** (AC injection blind to offset) | C — lump/change only | N |
| Hall dynamics (pole/delay) | **C** — overlap-band excitation + trusted coil (case 9) | C | C | **F** (inject near/above pole) | C | C |
| Hall fault (abrupt) | **C** — detect via ρ-alarm, cannot attribute (§4) | C | F | **F** (self-test toggle) | F | **F** (voting) |
| Coil gain `K_C` (absolute) | **N** (§3) | N | **F** (case 4, needs dB/dt ≠ 0) | **C** (mutual-inductance reference) | **C** (ratio to shot-0) | N |
| Integrator initial condition `x_I(0)` | **C** — needs calibrated Hall (case 1/I) | F | F | C | C | C |
| Integrator drift `m` | **C** — calibrated Hall (case 1/I); confounded with gain under constant dB/dt (CASE I-ramp) | **F** (with dB/dt variation) | F | C | C | C |
| Integrator leak `τ_L` | **C** (case I; needs flat-top + excursion) | F | F | C | C | C |
| Coil LF/DC content | **F** — supplied by calibrated Hall (case 1; the C02 direction) | F | F | C | C | F |
| Coil fault/saturation | **C** — overlap-band residual only (case 9) | C | F | F | F | F |
| "Which channel drifted?" (attribution) | **N** (§5.3) | C (offsets only) | **F** | **C** (not common-mode of die+cal coil, C05) | C | **F** (mechanism diversity; rests on [R071] single source) |
| Temperature vs radiation cause | **N** | N | N | N | N | **C** — measured T + decorrelated histories (CASE J) + species-matched dosimetry (C16/C26) |

**Reading the matrix (Derived):** no column except "machine current +
field model" makes absolute quantities feasible; every in-situ scheme is a
*change-tracking* scheme anchored to an initial absolute calibration. The
architecture question is therefore not "can they calibrate each other" but
"which minimal set of anchors keeps both channels' drift observable."

---

## 3. Required references and minimum excitation (per objective)

Derived from §5; each line lists the *minimum* addition that makes the
objective observable.

1. **Absolute scale (once, and after any suspected common-mode event):**
   vacuum reference field from machine coil currents + validated field
   model (case 4) with ≥2 field levels and a nonzero-dB/dt segment; or an
   NMR/traceable transfer standard on the bench ([H041], [H042], [H064]).
2. **Hall offset:** zero-field (or independently known field) epochs with
   remanent/ambient field controlled or measured; between-shot access
   suffices (case 1, CASE C2).
3. **Hall gain tracking in situ:** either (a) trusted coil chain + field
   excursions with SNR — variance shrinks as `σ_H²/Σ(ΔB−ΔB̄)²` (case 2);
   or (b) embedded calibration coil with spectrally orthogonal (or
   toggled) injection and a stability-budgeted reference chain (case 5);
   or (c) repeated reference waveforms with logged reproducibility
   (case 6).
4. **Coil gain vs integrator drift separation:** waveform containing at
   least two distinct dB/dt values (ramp + flat-top); under a constant
   ramp they are structurally confounded (CASE I-ramp).
5. **Drift attribution (which channel / which cause):** a third,
   mechanism-diverse channel (metallic Hall [R071] and/or the cal coil)
   plus measured temperature with pre-characterized coefficients and a
   dose proxy whose species matches the environment — cross-species
   scaling can err ~14× (Observed, [R042]; claim C16).
6. **Hall dynamics/bandwidth verification:** excitation near/above the
   Hall pole (injected or natural transients); near-DC operation cannot
   verify bandwidth (CASE H-narrow).
7. **Fault coverage during quiescent periods:** none exists from the pair
   (case 8) — scheduled injected self-tests are the only option.

---

## 4. Implications for radiation-induced sensitivity tracking

- **What is genuinely available (Derived):** an in-situ estimate of
  *relative* Hall-gain evolution `S_H(t)/S_H(t_0)` — the quantity a
  radiation-drift monitor actually needs — via case 2/5/6 mechanics,
  provided the anchors and excitation above exist. Combined with
  between-shot zero-field offset checks (case 1) this covers both Hall
  drift parameters the mission cares about.
- **The coil chain is not a free reference under radiation (Inferred from
  observed mechanisms):** RIEMF adds radiation-driven `b_C` errors
  ([R056], claim C19), and readout/integrator electronics have their own
  documented radiation failure modes (claim C25). The very environment
  that makes Hall recalibration necessary degrades the coil-as-reference
  assumption of case 2. Design consequence: budget the coil chain's
  radiation terms explicitly (MI-cable RIEMF, integrator electronics
  siting) before assigning it reference authority, and prefer
  triangulation — coil + embedded cal coil + material-diverse Hall —
  over any single reference.
- **Common-mode blindness is the radiation-specific danger (Derived):** a
  radiation/thermal event that shifts the Hall die and its co-located
  reference together is invisible to same-die self-test (claim C05
  limitation) and, by Theorem 1, a common-mode gain shift of Hall and
  coil is invisible to the pair. Only mechanism diversity (geometric coil
  constant vs semiconductor transport vs metallic Hall) plus an
  occasional absolute anchor (case 4) closes this hole. The metallic-Hall
  reference option currently rests on a single source ([R071], claim C18)
  — a bench/irradiation validation item, not settled evidence.
- **Temperature/dose attribution requires design, not inference (Derived):**
  separability demands measured temperature, pre-characterized
  coefficients, and thermal histories decorrelated from dose (CASE J);
  annealing hysteresis further narrows validity windows ([R024], claim
  C22). Dosimetry must match the actual species/spectrum (claims C16,
  C26).
- **What the literature does and does not support (Observed):** existing
  hybrid work corrects the *coil* chain from a Hall/absolute reference
  (C02) and does **not** demonstrate in-situ identification of
  radiation-induced Hall gain or bias drift in any fusion or radiation
  environment (C06). The single coil-calibrates-Hall precedent is
  non-fusion, unirradiated, driven-ramp ([H059], C11). Nothing in this
  stage's mathematics should be read as claiming the literature already
  validates radiation-aware mutual calibration — it does not, and the
  magnitudes needed to size excitation cadence for the user's GaN devices
  are **Unknown** (no GaN/AlGaN Hall-plate neutron dataset exists, claim
  C14).
- **Fault detection under radiation (Derived):** the gain-ratio alarm
  gives cheap, continuous *detection* of differential drift; attribution
  requires the case-7 voting architecture. During quiescent field
  periods there is zero coverage (case 8) — schedule injected self-tests
  around irradiation exposure windows.

---

## 5. Honest scope statement

This verdict is a structural-identifiability result derived from the
stage's measurement model plus reproducible synthetic rank tests. It is
not an experimental result; no hardware demonstration of the coil→Hall
direction exists in fusion conditions (C06), and the quantitative
radiation drift rates for the user's device family are unknown (C14).
The correct next consumers are stage 30 (compensation architecture:
which anchors to build) and stage 60 (research program: which of the
open identifiability conditions to demonstrate on the bench first).
