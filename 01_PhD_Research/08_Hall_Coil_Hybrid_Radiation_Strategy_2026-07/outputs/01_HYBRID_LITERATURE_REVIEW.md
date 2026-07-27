# Hybrid Hall+coil literature — final review (stage 10D)

Source IDs cite `outputs\01_SOURCE_LEDGER.csv`. Claim labels follow
`CLAUDE.md`: **Observed** (stated in an inspected source), **Derived**
(calculated/synthesized from documented inputs), **Inferred** (interpretation
with stated assumptions), **Proposed** (future work), **Unknown** (evidence
insufficient). Claim IDs (C01…) cite `outputs\01_EVIDENCE_MAP.csv`.

Measurement model used throughout (per `DECISION_FRAMEWORK.md`):

```text
y_H(t) = S_H(t) B(t) + b_H(t) + n_H(t)      (Hall channel)
y_C(t) = K_C(t) dB(t)/dt + b_C(t) + n_C(t)  (coil channel)
```

## 1. Direct prior art (Observed; C01)

The Hall(DC)+coil(AC) hybrid architecture is not a new idea. Verified direct
prior art spans 26 years and four domains:

| Year | ID | System | What is combined |
|---|---|---|---|
| 1999 | H055 | HOKA current probe (power electronics) | Hall DC channel + air-coil di/dt channel, summed |
| 2002 | H038 | Hall array + on-chip reference actuator | Embedded calibration winding injects known field for Hall self-calibration |
| 2007 | H006 (*uncertain*) | Fusion concept paper | Reported sensing+actuation self-test transducer; full text unobtainable — no strong claim may rest on this row |
| 2008 | H056 | Space AC/DC magnetometer | Hall element physically inside a search-coil core (single head) |
| 2012 | H007 | JET RHP (operational) | Hall probe + embedded microsolenoid that is both self-calibration actuator and pickup coil |
| 2013 | H040 | HBT-EP "artificial plasma" | Driven in-situ calibration coils calibrate 216 Mirnov coils + Rogowski |
| 2018 | H008 | FAT-CM FRC | Hall covers low-f band, coil covers high-f band |
| 2018 | H059 | Feather-M2 HTS dipole (CERN) | Cryogenic Hall sensors **cross-calibrated in situ by induction coils** (abstract read and confirmed at 10D) |
| 2022 | H003 | JET RHP 11.5-year record | Observed: same-die self-calibration stability; **Proposed only**: Luenberger–Kalman Hall+coil hybrid probe |
| 2022 | H004 | CERN accelerator bench | Kalman filter: coil-integrated field state, Hall or magnet-current measurement update |
| 2022 | H045 | Composite current sensor | TMR (not Hall) + Rogowski crossover design |
| 2025 | H001 | KSTAR-adjacent, synthetic data | Kalman filter jointly estimates field + coil-integrator bias with Hall DC anchor |
| 2025 | H002 | Tokamak (validation basis unconfirmed) | Kalman fusion of broadband coil + narrowband Hall |

**Derived:** fusion-specific instances concentrate in 2022–2025 within two
overlapping author clusters (CERN/Arpaia: H004, H005, H028; JET/Prague/KAERI:
H001, H002, H003, H007, H011). Any manuscript claiming "Hall+coil hybrid for
fusion diagnostics" as its contribution must distinguish itself from these
specific papers by source ID (C36).

## 2. What has been demonstrated (Observed/Derived)

**Hardware-validated, decision-grade:**

- Coil/integrator additive drift `b_C` corrected by a non-integrating
  reference — CERN bench: 59.9–120 ppm/s → 0.02–0.08 ppm/s with a Hall or
  magnet-current update (H004, full text); ~3 orders of magnitude with an NMR
  reference (H005, full text). Deployed at system level in ITER's OVSS, where
  a bismuth-Hall DC channel corrects inductive-sensor drift (P003,
  metadata-verified) (C02).
- Hall sensitivity `S_H` *stability verification* by same-die known-field
  injection — JET RHP microsolenoids preserved InSb sensitivity to
  SD ≈ 0.07 % over 11.5 years / >19,000 pulses including D-T (H003, H007)
  (C05).
- Hall offset `b_H` suppression by spinning-current/chopping (H034, H036,
  H037) — with a proven **residual offset floor** that survives current
  spinning (H035): offset is reduced, never eliminated (C07).
- In-situ known-field calibration of *inductive* sensors at machine scale
  (H040) and of Hall arrays at chip scale (H038, quantitative figures
  snippet-flagged) (C08).
- The **reverse direction — coil calibrates Hall in situ** — exists in exactly
  one abstract-confirmed non-fusion case: Feather-M2's cryogenic Hall sensors
  cross-calibrated against induction-coil sensors during driven magnet ramps
  (H059) (C11). The excitation there is engineered and known (a driven ramp);
  nothing comparable exists in a fusion device.

**Simulation-only or unconfirmed (must not be cited as demonstrated):**

- H001: joint field+coil-bias Kalman estimation demonstrated on synthetic
  data only (its own abstract says so).
- H002: validation basis (real vs. synthetic) could not be confirmed after
  repeated attempts (publisher blocked); Unknown.
- H003's hybrid Luenberger–Kalman probe: Proposed in the paper, not built.

**Derived — validation-strength inversion (C09):** the papers architecturally
closest to this mission's proposal are the weakest-validated; the strongest
hardware validations (H004, H005) are non-fusion and never touch `S_H`.

## 3. What remains unproven (Derived/Unknown)

1. **Joint identifiability.** No verified source jointly estimates
   `{B, S_H, b_H, K_C, b_C}` from a Hall+coil pair with a stated
   observability/identifiability condition. The strongest proof found (H021:
   necessary-and-sufficient rank condition for state + per-sensor bias +
   common unknown input) explicitly **excludes an unknown sensor-gain term**,
   and its validation is simulation-only. Foundational bias-observer theory
   (H015, H016, H017) likewise treats additive terms, not multiplicative gain
   (C03). Extending the rank condition to carry `S_H` and `K_C` is an open,
   non-trivial problem — a candidate for genuine novelty.
2. **Excitation conditions.** The closest analyzed analogs (GPS/INS: H018,
   H019; magnetometer-bias geometry: H020) prove bias/state observability is
   conditional on persistent excitation and can degenerate. **Inferred:** a
   Hall+coil pair should be presumed *not* mutually self-calibrating during
   quiescent/DC operation; an engineered excitation (injected known field per
   H038/H040/H007, or a known field ramp as in H059) is likely required, and
   the specific condition for this sensor pair has never been derived (C04).
3. **Crossover design.** No source establishes the Hall↔coil crossover-
   frequency design rule or its error propagation; the nearest instance is
   TMR+Rogowski (H045). Unknown.
4. **Timing/phase misalignment** between a Hall and a coil channel: only
   generic delay-fusion theory exists (H053). Unknown.
5. **Bidirectional mutual correction in a fusion environment**: no source,
   hardware or simulation, demonstrates coil-derived identification of Hall
   gain/bias drift in any plasma machine (C06; see §4).
6. **Counter-signal (Observed, C10):** in superconducting-magnet quench
   detection, Hall-array (H060) and coil quench-antenna (H061) lines remain
   deliberately parallel and unfused — even well-resourced communities have
   not treated Hall+coil fusion as an easy default.

## 4. Required distinction: drift correction is not radiation calibration

**This must be stated explicitly (Derived, C06): existing Hall+coil drift
correction does not automatically prove in-situ Hall radiation-sensitivity
calibration.** Every fusion-context hybrid instance found (H001, H002, P003;
plus the non-fusion H004/H005) operates in one direction only — the Hall (or
NMR/current) channel supplies an absolute reference that corrects the
*coil/integrator* chain's additive drift `b_C` — and every one of them
*assumes* `S_H` is known or stable. None demonstrates the coil channel
identifying radiation-induced drift in `S_H` or `b_H`. The one confirmed
coil-calibrates-Hall case (H059) is non-fusion, radiation-free, and relies on
a driven, known excitation. The only fusion in-situ Hall-recalibration
architecture that exists (H003/H007) is a *same-die, same-technology*
self-test: it cannot, by construction, detect a correlated failure that
shifts the Hall die and its co-located reference microsolenoid together —
precisely the failure class a radiation environment threatens. Whether a coil
channel *can* in principle carry enough information to separate `S_H(t)`
drift from field change is exactly the unresolved identifiability question of
§3.1–3.2, not a settled capability.

## 5. Novelty constraints (Derived, C36; sequencing Proposed, C37)

Not novel (direct prior art exists): the Hall+coil architecture itself (§1);
Kalman-type fusion of the pair for fusion diagnostics (H001, H002, H003);
coil-drift correction from an absolute reference (H004, H005, P003);
accelerator-domain Hall+coil+NMR combination (P052, P057 — see the
applications review).

Credible remaining gaps, each bounded by this mission's documented search:
(a) a joint gain+bias+state identifiability analysis for the Hall+coil pair;
(b) hardware-validated *bidirectional* mutual correction in a real plasma
and/or radiation environment; (c) in-situ radiation-aware Hall recalibration
against a *material-diverse* reference (radiation review, C18/C21); (d) the
stellarator-mapping application niche (applications review, C32).

**Proposed (requires user/advisor scope decision):** keep "Hall-first,
hybridize-second" as engineering sequence, but stake the contribution on gaps
(a)–(d), not on the architecture. A dedicated prior-art sweep should precede
any publication claim on each gap.
