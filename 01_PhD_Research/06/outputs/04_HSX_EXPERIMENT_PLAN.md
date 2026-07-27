# 04 — Finished-study experiment plan: bench + HSX campaign (Stage 40)

Prepared by: Claude Code, stage `40_experiment`, requested model Fable 5 /
Extra High. Companion documents:
[`04_MEASUREMENT_REQUIREMENTS.csv`](04_MEASUREMENT_REQUIREMENTS.csv)
(requirement register, IDs `A-##`/`B-##`/`C-##`/`D-##`/`E-##`/`F-##`/`G-01`
referenced throughout),
[`04_DATA_ANALYSIS_PLAN.md`](04_DATA_ANALYSIS_PLAN.md), and
[`04_UNCERTAINTY_AND_STATISTICS_PLAN.md`](04_UNCERTAINTY_AND_STATISTICS_PLAN.md).

Basis: the stage-30 reviewer matrix
([`03_REVIEWER_RESPONSE_MATRIX.csv`](03_REVIEWER_RESPONSE_MATRIX.csv)) and
diagnosis ([`03_MANUSCRIPT_DIAGNOSIS.md`](03_MANUSCRIPT_DIAGNOSIS.md)), the
stage-20 direction decision
([`02_RESEARCH_DIRECTION_DECISION.md`](02_RESEARCH_DIRECTION_DECISION.md),
OPT2 with work packages WP-A/B/C/D and gates G1–G5), the stage-00 baseline
([`00_INPUT_INVENTORY.md`](00_INPUT_INVENTORY.md),
[`00_CLAIM_BASELINE.csv`](00_CLAIM_BASELINE.csv),
[`00_CONFLICT_LEDGER.md`](00_CONFLICT_LEDGER.md)), and direct re-reads this
stage of the parent bench truth:
[`../../02_HSX_Hall_Sensor_Readout/docs/SPECS.md`](../../02_HSX_Hall_Sensor_Readout/docs/SPECS.md),
[`../../02_HSX_Hall_Sensor_Readout/NOTES.md`](../../02_HSX_Hall_Sensor_Readout/NOTES.md),
[`../../02_HSX_Hall_Sensor_Readout/docs/hsx_readout_bringup_and_calibration_plan.md`](../../02_HSX_Hall_Sensor_Readout/docs/hsx_readout_bringup_and_calibration_plan.md)
(cited below as "the 02 plan"), and
[`../../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md`](../../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md)
(cited as "the 03 plan"). Source IDs `S####` resolve in
[`01_SOURCE_LEDGER.csv`](01_SOURCE_LEDGER.csv) with a DOI link on first use.

Epistemic labels: **[SF]** supplied fact, **[EE]** external evidence,
**[INF]** inference, **[REC]** recommendation, **[PX]** proposed
experiment, **[GATE]** unresolved gate. Values with no supplied basis are
marked NOT ESTABLISHED FROM SUPPLIED FILES.

Standing corrections honored (conflicts C1/C6): the manuscript is a
declined 2026 submission with an invitation to resubmit — never "the 2023
published paper"; project 02's "calibrated" language is aspirational — the
only bench result is emulator offset cancellation (C016) with the ~109×
magnitude anomaly open (C017).

---

## 1. Design philosophy: minimum rigorous, fabrication-minimal, two-tier

**Objective [REC]:** convert the existing voltage-domain HSX demonstration
into a defensible magnetic-field instrument study — tesla-denominated
output with a written uncertainty budget, repeatability evidence, a
justified bandwidth figure, and (as upside) an in-machine absolute anchor
— while adding **zero new device topology and zero cleanroom work**
(stage 20 §7; MISSION.md low-cleanroom constraint).

Three design rules govern everything below:

1. **Bench before machine.** Every P0 reviewer item (AE-01, AE-03, AE-04,
   AE-05, R1-01, R2-02) is bench-satisfiable; the AE explicitly conceded
   in-vessel repetition is impractical and asked for bench repetition
   (matrix AE-03). The HSX campaign is upside and RSI material, not a
   single point of failure — stage 20's structural improvement (fallback
   F1 at gate G2).
2. **Nothing is assumed available.** Equipment, dies, feedthroughs, shot
   time, and machine signals enter the plan only through the §2 inventory
   gates. The supplied files establish surprisingly little as physically
   in-hand (see §2) — most of the 02 plan's testbench is *designed*, not
   *built* [SF: shopping list at 02 plan §7.4; C013].
3. **Anomaly first.** The ~109× discrepancy (C017) carries an explicit
   do-not-calibrate instruction in the project's own journal [SF]. Every
   calibration requirement is gated behind B-01. A calibration built on an
   unexplained 109× gain error would be worse than no calibration.

**Two-tier output** (matches the stage-30 route decision A→C):
- **Tier 1 — SENSL resubmission package** (bench + supplied-data
  analyses only): §11.1.
- **Tier 2 — RSI instrument package** (adds campaign anchors, vector
  probe, stability): §11.2.

---

## 2. Pre-campaign inventory and go/no-go gates

### 2.1 What the files establish as physically existing [SF]

| Item | Evidence |
|---|---|
| `hsx_2026_v1` readout board #1, assembled, logic + emulator spin verified | NOTES.md 2026-07-08 entry |
| Pico 2 + mode-1 (spin+scope) firmware, bench-proven | NOTES.md 2026-07-08 |
| Mode-2 (static-bias, Pico-ADC) firmware — **smoke-tested with hardware stubbed only** | NOTES.md 2026-07-08 |
| Emulator plug (680 Ω ring + 2.2 kΩ variant, used 2026-07-08); SPECS specifies a 649 Ω + 33 kΩ parallel design — whether that second plug was built is not established | NOTES.md; SPECS.md |
| Bench scope DSO-X 4022A (used in the 2026-07-08 run) | NOTES.md |
| A current source capable of 20 mA (identity unrecorded) | NOTES.md 2026-07-08 config |
| Analysis scripts `hsx_demod_scope_csv.py`, `spin_verify_nosync.py` | 02 folder inventory |
| The 2025 HSX raw archive (73 scope CSVs, shot log, .dat files, coil logs) — immutable | `../../07_HSX_august2025_results/hsx_20250821/`; 00 inventory Group C |
| Gerber/order package for board copies | `../../02_HSX_Hall_Sensor_Readout/circuit/` |
| One GaN Hall module was packaged and deployed in HSX in Aug 2025 | C001/C007 |

### 2.2 Inventory confirmation gates (close before bench work is scheduled)

Everything below is required by some requirement row and **NOT ESTABLISHED
FROM SUPPLIED FILES** as currently in-hand. Each is a written go/no-go
item [GATE]; none is a purchase/request this mission can execute
(no-external-action rule) — they are the user's checklist.

| Gate | Item | Needed by | Basis of doubt | Unblock action |
|---|---|---|---|---|
| I-1 | DSOX1204G scope/wavegen, bench supply, DMM at the Stanford bench | B-01+, C-01+ | 02 plan §7.4 says "assumes existing" — an assumption, not a record; only the DSO-X 4022A is demonstrated in use | Physical check; note which scope is the campaign unit |
| I-2 | Precision floating ~100 µA source (SMU, or REF200 to be purchased) | C-02, C-04, D-01 | REF200 is on the unpurchased shopping list; SMU access never documented | Confirm SMU or order REF200 (~$8) |
| I-3 | Calibration-bench BOM (~$90): magnet wire, printed former + cradle, 1 Ω 0.1 % shunt, DRV5055A1/TLE493D/MLX90393 breakouts, NdFeB magnets, DSUB plugs | C-01, E-01 | 02 plan §7.4 is a shopping list, not an inventory | Purchase + build (user action) |
| I-4 | Packaged GaN die inventory: where is the deployed 2025 module now, is it functional, and does a spare packaged die exist? | C-02, C-03, C-05, C-07, C-08, D-01/D-02, F-07 | No supplied file records the module's post-campaign location or health; "spare sensor" appears only in a packing list | Physical inventory + resistance map (F-07 protocol) |
| I-5 | Unpackaged dies + LCCs + wedge-bonder access to package ≥2 more modules; gen-2 die status/count | D-01 (WP-B) | Advisor decision 3 (stage 20 §10): gen-2 fabricated/in-fab/not-started is unknown; bonder access undocumented | Advisor answer; assembly-lab booking |
| I-6 | Does the 2023 voltage-bias chain (INA849 + 2×OPA814, G=200) still exist as hardware? | B-04, C-03 preferred | Chain described only in the manuscript; no bench record since | Physical inventory |
| I-7 | 10–20 m harness-type cable + feedthrough-equivalent capacitance for the long-cable rehearsal | B-06 | 02 plan Week 4 item; procurement never recorded | Procure or emulate with discrete C |
| I-8 | Hotplate/oven for 25–100 °C runs | C-07 | Mentioned in the 02 plan; availability never recorded | Lab check |
| I-9 | Borrowed electromagnet + calibrated gaussmeter for a high-field point | E-03 preferred | 02 plan §7.2.4 *infers* access from prior group work — an inference, not a record | Ask the group; if no, rely on F-01 |

### 2.3 UW / HSX gates (the July email — advisor decision 4, stage 20 §10)

All campaign-side items funnel through one advisor-authorized email to
Wayne Goodman / Thomas Gallenberger [SF: the 03 plan already drafted this
ask list; stage 20 added the data-request items]:

| Gate | Ask | Feeds |
|---|---|---|
| U-1 | Do co-located B-dot/Mirnov/pickup-coil records exist for the Aug-2025 shots (9–68)? Channel positions, sampling, access | E-02 → analysis-only 1:1 comparison (R1-02) |
| U-2 | Feedthrough pin count/connector on the intended port | Harness build; F-05 spare-pin question; 3-axis decision |
| U-3 | Mount pose survey feasibility (±1 mm, ±1°) + post-run re-survey | F-02 |
| U-4 | Vacuum-field computation at the probe pose vs coil current, per setting | F-01 |
| U-5 | Coil-only shot allocation (≥2 settings × ≥3 shots) + plasma shot-list scale | F-01, F-03 |
| U-6 | Trigger/clock tie-in or trigger-signal access; DAQ channel options | F-04; 03 plan §2.5 strategy C |
| U-7 | Whether an HSX discharge-magnetics archive exists at scale | WP-D sizing; prices the OPT3 fallback (stage 20 §10) |
| U-8 | Bench basics at HSX (DMM, bench supply) for F-07 health checks | F-07 |
| U-9 | August window confirmation (C018 is a target, not a booking) | Campaign #1 existence (gate G2) |

### 2.4 Go/no-go gate ladder [REC]

| Gate | Test | Pass → | Fail → |
|---|---|---|---|
| **G0 (inventory)** | I-1…I-5 closed; purchases done | Bench phase starts | Work the A-group analyses (§4.0) — they need nothing |
| **G1 (bench truth = stage 20 G1)** | B-01 closes the ~109× anomaly; G known to ±1 % | Calibration unlocked | Board fault isolation sprint; SENSL revision re-scoped around A-group + WP-A + bandwidth derivation while chain is fixed |
| **G-cal** | C-01 (k to ≤2 %) and C-02 (m to ≤2 %, linearity <0.5 %) pass | Tesla-denominated claims and G-01 conversion allowed | No tesla claim anywhere; route decision revisited (matrix AE-01 fallback column) |
| **G-die (WP-B)** | ≥3 packaged dies confirmed (I-4/I-5) | D-01 as designed | Single-device fallback (§7.3) with limitation language |
| **G2 (campaign #1 = stage 20 G2)** | U-9 confirmed; C-02 done pre-ship; F-07 pre-ship map recorded | Campaign per §9–§10 | Fallback F1: Tier-1 package unaffected; anchor moves to next window |

---

## 3. Bench phase 0 — chain verification (before any calibration)

**B-01 — anomaly closure (ΔV gain check)** [PX; inherited as project 02's
own named top priority, not invented here]. Static phases; inject ~1 mV
known differential (1.000 V through 10 kΩ:10 Ω divider) at the sense pair;
toggle; `ΔV_out/ΔV_in = G`. Target 100.3 ± 1 % (02 plan §4 Day 3–4).
Repeat at all 8 states (preferred design). In parallel, re-derive the
expected emulator output from DMM-measured ring resistances via
`o = I·(R14·R23 − R12·R34)/ΣR` — the 2026-07-08 run's 0.686 V vs ~75 V
prediction must resolve into either (a) in-operation gain ≠ 100.3 or
(b) the 2.2 kΩ not electrically unbalancing the bridge as modeled
[SF: NOTES.md names exactly these two survivors]. **Exit criterion:** the
mechanism is named, reproduced, and written to the project 02 journal;
the do-not-calibrate flag is lifted. No calibration work starts before
this [REC — hard rule].

**B-02 — static 8-state survey.** Emulator survey across all 8 mux states
must reproduce SPECS' sign pattern `+ − − + − + + −` with amplitude G·o
predicted from measured resistors. Preferred: cross-check states 2/3/6/7
on the mode-2 Pico-ADC path — this is also mode-2's first hardware
validation (it has only ever run stubbed [SF]), which D-01 and F-07 need.

**Fix the global sign here and freeze it** (§5).

---

## 4. Bench calibration — DC and frequency-dependent

### 4.0 Campaign zero: the supplied-data analyses (run any time, no hardware)

A-01…A-06 ([`04_MEASUREMENT_REQUIREMENTS.csv`](04_MEASUREMENT_REQUIREMENTS.csv);
methods in [`04_DATA_ANALYSIS_PLAN.md`](04_DATA_ANALYSIS_PLAN.md) §3–§5):
shot recount, operational-repeatability statistics, quantified
diamagnetic-loop correlation + measured DAQ offset, bias-scaling check,
in-situ voltage-noise floor, figure regeneration. These six close the
wording-level reviewer items (A5/R-3/R-4/M8) from the immutable 2025
archive alone [SF basis: stage 30 diagnosis §4.1] and are the cheapest
credibility wins in the whole plan. Start them immediately — they are
also the G1-fail hedge.

### 4.1 Field source and traceability (C-01)

Build the Helmholtz pair exactly per SPECS (R = 50 mm, N = 100/coil,
k ≈ 1.8 mT/A, ±2.7 mT at ±1.5 A) [SF: design exists; build does not].
Triangulate k three ways (02 plan §7.2): geometry + 0.1 % shunt
(primary; the pair is a *calculable standard*, uniform to <0.1 % over the
die), AC pickup coil, and commercial reference sensors (E-01). Norm for
traceable Hall-probe calibration with a written budget:
[S0051](https://doi.org/10.5194/jsss-9-391-2020) [EE]. **Acceptance:**
u(k)/k ≤ 2 %, methods consistent within stated uncertainties;
disagreements investigated, never averaged away [REC].

### 4.2 DC calibration, current-bias mode (C-02 — the WP-C core)

Bipolar ≥11-point sweep over ±2.7 mT at 100 µA; fit
`V_demod = m·B + b`; up and down sweeps (hysteresis, C-06 free of
charge); ≥3 full repetitions on separate days with remount (feeds D-02).
Expected m ≈ 0.5–0.6 V/T [SF: SPECS expectation — to be tested, not
assumed]. Targets (02 plan §7.3): **~2 % absolute, <0.5 % linearity**.
Cross-check m against first principles `G·S_I·I·(loading ≈ 0.83)`; a
large gap re-opens B-01. Training/held-out field-point protocol per the
02 plan §7.3 (leakage safeguard — see
[`04_DATA_ANALYSIS_PLAN.md`](04_DATA_ANALYSIS_PLAN.md) §8).

### 4.3 Voltage-bias-mode sensitivity for the retroactive conversion (C-03)

**This row exists because the 2025 data was not taken with the 2026
readout.** The deployed chain was voltage-bias 0.2–0.4 V through
INA849 + 2×OPA814 at G = 200 [SF: manuscript M3/M4; C004]. Converting the
2025 traces to tesla (AE-01/AE-05 → G-01) therefore needs **S_v at the
deployed bias settings for the deployed die** — not the 100 µA
current-bias m. Measure S_v (V/V/T) at 0.2/0.3/0.4 V on the deployed die
(gate I-4), through the actual 2023 chain if it still exists (gate I-6),
else through a documented bench amplifier with the chain-gain-200
assumption stated. Every downstream tesla figure for 2025 data carries
the same-die/same-chain/temperature-transfer assumptions explicitly
(matrix AE-01 note). Fallback if the deployed die is gone: same-wafer
sibling + D-01's die-to-die spread as the transfer uncertainty, clearly
labeled [REC].

### 4.4 Bias-current scaling (C-04)

m at I = 50/100/200/500 µA; confirm m ∝ I; pick the HSX operating point
deliberately (noise-vs-I as the preferred add-on). If only a fixed
source exists, the linearity-in-I assumption is cited to prior GaN
characterization ([S0006](https://doi.org/10.1063/1.5139911),
[S0017](https://doi.org/10.1063/1.2201339)) and flagged as assumed [EE].

### 4.5 Frequency-dependent calibration (B-03/B-04 — closes AE-07/R1-04)

- **Spun chain:** transfer function 10 Hz–3 kHz (electrical injection
  minimum; Helmholtz sine drive preferred once C-01 exists) at
  f_spin = 10/40/100 kHz. Expected −3 dB near 1–2 kHz from demod
  averaging [SF: SPECS]; measure, don't assert. Record **phase lag** —
  required for honest correlation claims against the diamagnetic loop.
- **Static-phase (fast) chain:** electrical sweep to −3 dB; this is the
  fast-transient mode's real bandwidth.
- **The 1 MHz question (C003):** the revision states, for each chain
  generation, a bandwidth **with its evidentiary basis** (measured /
  derived / asserted — asserted is retired). If the 2023 chain no longer
  exists (I-6), a derivation from the component configuration and
  acquisition settings is presented as derived-not-measured [REC].
  B-dot calibration methodology as the class norm:
  [S0076](https://doi.org/10.1063/1.3246785) [EE].

---

## 5. Field-to-voltage transfer function, sign, and orientation

Model chain (single axis) [SF: SPECS/plan; equations restated in
[`04_DATA_ANALYSIS_PLAN.md`](04_DATA_ANALYSIS_PLAN.md) §4]:

- Current-bias 2026: `V_demod = m·B_⊥ + b`, `m = G·L·S_I·I`
  (G gain, L loading ≈ 0.83, S_I ≈ 60 V/A/T, I bias) — every factor
  measured, none trusted from SPECS without the §3–§4 checks.
- Voltage-bias 2023/2025: `V_out = A_v·S_v·V_bias·B_⊥ + A_v·V_off(T)`
  (C023) — S_v from C-03; V_off is why only calibrated-slope and
  AC/transient components convert cleanly (analysis plan §4.2).

**Sign/orientation protocol [REC, from the 02 plan §1 caveat]:**
1. The demod sign rule (`+1 if a0 == a2`) comes from the netlist; the
   **global** sign does not — fix it once with a NdFeB magnet of known
   polarity (I-3 purchase) and freeze it in firmware/analysis.
2. Record which plate normal maps to +B, photograph the die-in-LCC
   orientation, and carry that into the mount drawing.
3. At HSX, the surveyed pose (F-02) + the UW field model's field
   direction at the pose (U-4) close the orientation loop: predicted
   sign of the coil-only response is a pass/fail check on installation
   day (F-01 acceptance includes sign).
4. B_⊥ is the normal component only: the cos-error term (<3° → 0.15 %
   [SF: 02 plan §7.3]) enters the budget; in-plane (planar-Hall) response
   is checked at bench by driving B in-plane (03 plan §3.2 method,
   single-axis version) [PX].

---

## 6. Characterization suite (offset, linearity, hysteresis, temperature, drift, noise, bandwidth, parasitics)

One row each — full designs in the CSV:

| Quantity | Req | Method (minimum) | Key acceptance |
|---|---|---|---|
| Offset (spun residual b + raw plate offset) | C-05 | Zero-field demod with 180° flip pairs; mode-2 raw offset | b with spread; emulator (C016) vs die results **never conflated** |
| Linearity | C-02 | Residuals of the bipolar fit | <0.5 % FS or honestly reported |
| Hysteresis | C-06 | Up-vs-down sweep difference (free from C-02) | <0.5 % FS or quantified into budget |
| Temperature | C-07 | 25–100 °C steps: b(T), m(T); emulator as control (gate I-8) | Coefficients with CI; in-vessel ΔT bound stated (F-05 or assumption) |
| Drift | C-08 | Overnight zero-field log → Allan deviation ([S0168](https://doi.org/10.1109/TIM.2007.908635)) [EE]; parallel mode-2 unspun log shows what spinning buys | Allan knee identified; drift in µT over stated interval |
| Noise | B-05 | Welch PSD, emulator then die; spur inventory of the RS6-2415D DC/DC rails | Floor in V/√Hz and µT/√Hz with ENBW; model-consistency discussed |
| Bandwidth | B-03/B-04 | §4.5 | Measured −3 dB + phase; basis stated per chain |
| Parasitics | B-06 | Glitch/settling vs f_spin; blanking study; long-cable test (I-7); bond/LCC step-response estimate | Settling margin at HSX cable length; AE-08 novelty claimed **only if measured** |

---

## 7. Device/module repeatability (WP-B) — with the honest single-device fallback

### 7.1 Multi-die design (D-01, the AE's own specification)

≥3 packaged dies (the AE's number [SF: decision letter]), same fabrication
lineage, existing iterations only — 2023-generation remainders and/or
gen-2 if fabricated (advisor decision 3; gates I-4/I-5). Per die: mode-2
raw-offset at 100 µA (the incoming-inspection tool the 03 plan §2.1
already designates [SF]) and a ≥5-point Helmholtz sensitivity spot-sweep.
≥3 repeats per die so within-die variance is separable from between-die
variance (variance decomposition in
[`04_UNCERTAINTY_AND_STATISTICS_PLAN.md`](04_UNCERTAINTY_AND_STATISTICS_PLAN.md)
§4). Literature templates: on-chip Hall-cell statistics
[S0218](https://doi.org/10.3390/jsan2010085); the group's own geometry/
offset statistics [S0004](https://doi.org/10.1109/JSEN.2019.2895546);
JET's 18-sensor multi-year stability as the field's bar
[S0068](https://doi.org/10.1088/1741-4326/ac8aad) [EE].

### 7.2 Setup-vs-device separation (D-02)

≥3 full remove-remount-recalibrate cycles on one die (plus a thermal
cycle preferred). Without this, D-01's between-die spread is confounded
with fixture repeatability [INF].

### 7.3 Honest single-device fallback [REC]

If gates I-4/I-5 yield only one packaged die and no packaging path:
1. Report D-02 remount repeatability as **operational** repeatability —
   never as fabrication repeatability.
2. Cite prior-literature die statistics that genuinely cover the claim
   (S0004, S0218) — the AE explicitly allows this route if "shown
   clearly" [SF: decision letter].
3. State the single-module rationale from the team's actual record
   (never invented — matrix AE-03 note).
4. Use the limitations language of
   [`04_UNCERTAINTY_AND_STATISTICS_PLAN.md`](04_UNCERTAINTY_AND_STATISTICS_PLAN.md)
   §6 verbatim-class honesty: n=1 bounds nothing about the die
   population; the claim is about *this instrument*, with population
   statements deferred to literature.

### 7.4 Board/channel repeatability (D-03, P2)

Only when boards 2–3 exist (03 plan Sep gate): emulator + ΔV check per
board, inter-board gain/phase skew. RSI-package scope.

---

## 8. Conventional-reference strategy — bench vs HSX, kept strictly separate

**R1-02's ask ("compare to a conventional field probe") has a bench half
and a machine half; conflating them is how overclaims happen [INF].**

| Layer | What | Feasible where | Status |
|---|---|---|---|
| Bench, calculable standard | Helmholtz geometry + 0.1 % shunt (primary standard) | Stanford bench | Build gated on I-3 |
| Bench, independent physics | AC pickup coil (V = 2πf·N_p·A·B) | Stanford bench | Same build |
| Bench, commercial reference | DRV5055A1 / TLE493D / MLX90393 (±2–5 % class) — E-01 | Stanford bench | Purchase gated (I-3); **no commercial gaussmeter is established as available** — the cheap references are the plan's honest substitute |
| Bench, high-field | Borrowed electromagnet + calibrated gaussmeter (E-03 preferred) | Stanford/borrowed | Gate I-9 — access is an inference in the 02 plan, treat as unconfirmed |
| Machine, computed reference | Coil-only vacuum field from the HSX model at surveyed pose (F-01) | HSX only | Gates U-4/U-5; the [S0143](https://doi.org/10.1063/1.4894209) validation paradigm [EE] |
| Machine, inductive diagnostics | Co-located B-dot/Mirnov/pickup 1:1 comparison (E-02 → F-03); drift-fusion seed for WP-D ([S0118](https://doi.org/10.1088/1741-4326/adb599), [S0122](https://doi.org/10.1016/j.fusengdes.2025.115180)) [EE] | HSX only (2025 records if U-1 says they exist; else campaign) | Gate U-1 — **no bound may be claimed today** [SF: matrix R1-02] |

The 2.7 mT bench ceiling vs ~0.5 T at the probe is a ~185× extrapolation:
E-03/F-01 exist to close it; if neither lands, every HSX-scale tesla
statement carries the extrapolation limitation explicitly [REC].

---

## 9. Coil-only absolute anchor and pose uncertainty (F-01/F-02)

Campaign #1 must-have (the 03 plan's own priority 1 [SF]):
≥2 coil-current settings × ≥3 repeated coil-only shots; compare measured
`(V_demod − b)/m` against UW-computed **B_vac** at the surveyed pose.
Repeats give the anchor a spread, two settings test in-machine scale
linearity where the bench cannot reach. Acceptance: agreement within the
joint budget (bench ~2 % ⊕ pose term ⊕ field-model term — worked
symbolically in
[`04_UNCERTAINTY_AND_STATISTICS_PLAN.md`](04_UNCERTAINTY_AND_STATISTICS_PLAN.md)
§3.4); any discrepancy is investigated, not averaged. Sign check on
installation day per §5.

**Pose (F-02):** fixture CAD + machinist survey to ±1 mm / ±1°
(photogrammetry cross-check preferred; re-survey after the run). The pose
uncertainty enters as `|∇B|·u(pose)` plus the angular cosine term — UW's
field model supplies the local gradient (add to U-4). If no survey is
possible, CAD-nominal pose with widened uncertainty, and the anchor
degrades to consistency-check language [REC].

This section deliberately reuses the 03 plan's §3.3 design [SF] scoped to
the single-axis campaign #1; the vector version is campaign #2 / RSI
scope and is not re-planned here (stage boundary).

---

## 10. Plasma-shot matrix, controls, randomization, metadata, synchronization, failure handling

### 10.1 Shot matrix (campaign #1 request — final counts set by HSX, then logged)

Priority-ordered [REC; counts are the 03-plan-scale ask, not a promise]:

| Priority | Block | Shots (ask) | Purpose |
|---|---|---|---|
| 1 | Coil-only anchor: 2–3 settings × ≥3 | ~6–9 | F-01 (the must-have) |
| 2 | Biased vs unbiased pairs | ≥4 (2 pairs min) | Hall-origin control, 2025 Fig. 4 continuity |
| 3 | One standard discharge class, repeated | ≥3 | Between-shot statistics with n≥3 (uncertainty plan §4) |
| 4 | Long fixed-setting sequence | ~10 | F-06 offset stability b(t) |
| 5 | Taxonomy breadth (late-/failed-breakdown) | ~4 | 2025 class continuity |

If time shrinks: cut from the bottom. **Repetition beats coverage** for
the resubmission [REC].

### 10.2 Controls and randomization — honest version

- Controls: unbiased shots (EMI/charge-artifact null), coil-only shots
  (no-plasma null), and the emulator plug run in situ pre/post campaign
  day (chain-health null) [PX].
- True randomization of machine conditions is not Tim's to control
  (facility scheduling) [INF]. What is controllable and **is** required:
  **interleave** bias settings and biased/unbiased states across the day
  rather than blocking them (breaks time-order/warm-up confounds), and
  record run order so time-trend regression is possible (analysis plan
  §7). Where interleaving is refused by operations, the confound is
  declared, not hidden [REC].

### 10.3 Per-shot metadata (mandatory record — analysis plan §2.2 schema)

Shot number; timestamp; machine configuration + coil-current setpoint;
plasma/coil-only; bias mode/setting; measured bias (R9/R10 drop logged
each block — 02 plan risk register [SF]); f_spin + blanking; scope
config/memory strategy; trigger source + measured offset; ambient/board
temperature if instrumented (F-05, gated); operator notes incl.
anomalies. The 2025 campaign's single-docx manifest is the
counterexample motivating this schema [INF from Group C].

### 10.4 Synchronization (F-04)

Minimum: HSX trigger on a spare scope channel; measure offset + jitter
over ≥5 shots (the 2025 ~30 ms offset was asserted, A-03 measures its
2025 value; F-04 fixes it forward). Preferred: full clock tie-in (03
plan DAQ strategy C, gate U-6). Scope memory strategy A/B/C per 03 plan
§2.5 — decide at the October-equivalent bench gate, record per shot.

### 10.5 Failure handling (F-07)

Resistance map before/after every environment step (ship, bake, GDC,
run) with pre-agreed go/no-go thresholds; mode-2 30-second offset health
check as the scope-free tool; runbook with the EN-pulldown and
ground-bond traps at step 1 [SF: 02 plan risk register]; spares kit per
02 plan Week 4 (spare-module existence is gate I-4 — if none, the
failure branch is measure-and-document, stated in advance). Every
failure/abort event is itself logged data (analysis plan §2.3).

---

## 11. Minimum publishable data packages

### 11.1 Tier 1 — SENSL resubmission (campaign-independent by design)

Per the stage-30 route decision (A→C) and matrix P0 set:

1. A-01…A-06 supplied-data analyses (corrected shot accounting,
   operational-repeatability statistics, quantified correlation + lag,
   bias-scaling, in-situ noise floor, regenerated figures).
2. B-01/B-02 chain verification with the anomaly closed (G1).
3. C-01 + C-02: absolute calibration, m ± u(m), linearity, hysteresis.
4. C-03 + G-01: S_v at deployed settings → **Fig. 5 re-plotted in field
   units with uncertainty bands** (AE-05's explicit acceptance of honest
   uncertainty regions).
5. C-05: residual-offset headline (die, not emulator).
6. B-03/B-04: bandwidth figures with stated basis (1 MHz retired).
7. D-01 (or §7.3 fallback): repeatability statistics + single-module
   rationale.
8. WP-A comparison table (analysis-only; stage 30 §3 spec) — not a
   measurement, listed for package completeness.
9. C-07/C-08 (temperature, drift) strengthen but do not gate Tier 1
   [REC]: include if bench time allows before resubmission.

**Nothing in Tier 1 requires HSX access, new fabrication, or UW data.**

### 11.2 Tier 2 — RSI instrument package (adds machine truth)

Tier 1 plus: F-01/F-02 coil-only absolute anchor at surveyed pose;
F-03 shot matrix with controls; F-04 synchronization; F-06 in-vessel
offset stability; E-02-or-campaign 1:1 conventional-probe comparison
(R1-02's full answer, and WP-D's dataset); C-07/C-08 now mandatory;
D-03 when boards 2–3 exist; the vector-probe content itself remains
project 03 / campaign #2 scope (genre anchors:
[S0143], [S0154](https://doi.org/10.1063/5.0002193),
[S0113](https://doi.org/10.1063/1.4732077)–[S0115](https://doi.org/10.1063/1.5038812),
HSX magnetics context [S0132](https://doi.org/10.1088/0029-5515/55/11/113012)) [EE].

---

## 12. Work/time burden and the low-cleanroom route

### 12.1 Burden [INF — estimates, in bench-days not calendar dates]

Calendar note: the 02 plan's internal dates (Week 1 = Jul 6–12) are
already ~2.5 weeks stale — NOTES.md shows Week-1 items still open as of
2026-07-08 with no later entries [SF]. Burden below is effort, sequenced
by the gate ladder; stage 60 owns the calendar.

| Block | Content | Bench-days (est.) |
|---|---|---|
| A-group analyses | 6 supplied-data analyses + scripts | 4–6 desk-days (parallel to anything) |
| G0 procurement/build | Purchases, Helmholtz wind + former, cradle | 2–3 |
| Phase 0 | B-01, B-02, sign fix | 2–3 |
| Calibration core | C-01 triangulation, C-02, C-03, C-04 | 4–6 |
| Characterization | C-05…C-08, B-03/B-04, B-05, B-06 | 5–7 (one overnight run ×≥1) |
| Repeatability | D-01 (3 dies) + D-02; packaging adds if I-5 requires | 2–4 (+2–3 if packaging needed) |
| Campaign rehearsal | Long-cable, EMI, shot replay, runbook, spares | 2–3 |
| Campaign #1 | Trip + install + shots + health checks | ~5 on-site |
| **Total to Tier 1** | (no campaign needed) | **≈ 19–29 bench/desk-days** (stage-70 corrected sum of block maxima; +2–3 more if I-5 requires packaging) |

Single-operator, serial [INF]. The A-group and the build block
parallelize; nothing else safely does (one board, one operator).

### 12.2 Low-cleanroom implementation route [REC — restates the stage 20 §7 constraint as executed here]

- **Zero cleanroom steps anywhere in this plan.** No new topology, no
  epitaxy, no mask work. Gen-2's enlarged pads are a packaging-driven
  layout change owned outside this plan's scope [SF: stage 20 §7].
- Everything device-adjacent is **assembly-lab**: LCC packaging, wedge
  bonding, EPO-TEK 353ND encapsulation, 150 °C vacuum bake — the proven
  2023 process reused verbatim [SF].
- WP-B consumes **existing** fabrication iterations only; if none exist,
  the §7.3 fallback avoids fabrication entirely.
- The calibration bench is a <$100 buy-and-build (02 plan §7.4) plus
  instruments the lab must simply confirm (gates I-1/I-2/I-8/I-9).
- The heaviest hardware ask in the whole plan is hand-assembling board
  copies — and that is Tier-2/project-03 scope, not Tier-1.

---

## 13. Open gates handed forward

To stage 50/60/70/80 and the user:

1. Advisor decisions 3 and 4 (die supply; UW email authorization) gate
   D-01 and every U-row — the two human unblocks with the longest
   shadows [SF: stage 20 §10].
2. I-4 (where is the deployed module?) is this stage's most consequential
   *new* inventory question: C-03/G-01 — the direct answer to AE-01/AE-05
   for the 2025 dataset — depend on it.
3. U-1 (2025 co-located records) decides whether R1-02 closes by analysis
   or waits for the campaign.
4. C018 (August window) remains a target, not a booking; Tier 1 is
   engineered to survive its slip.
5. The ~109× anomaly (C017) remains open until B-01 closes it; every
   tesla-denominated promise in the route decision is conditional on G1.
6. No neutron/gamma experiment appears anywhere above (mission scope
   rule); radiation stays literature/TCAD outlook
   ([S0002](https://doi.org/10.1109/TMAG.2012.2196986),
   [S0054](https://doi.org/10.1149/2.0251602jss)) [EE].
