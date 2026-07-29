# 04 — Data analysis plan (Stage 40)

Prepared by: Claude Code, stage `40_experiment`, requested model Fable 5 /
Extra High. Companions:
[`04_HSX_EXPERIMENT_PLAN.md`](04_HSX_EXPERIMENT_PLAN.md) (requirement IDs
`A-##`…`G-01` from
[`04_MEASUREMENT_REQUIREMENTS.csv`](04_MEASUREMENT_REQUIREMENTS.csv)) and
[`04_UNCERTAINTY_AND_STATISTICS_PLAN.md`](04_UNCERTAINTY_AND_STATISTICS_PLAN.md)
(symbol definitions and budgets used here). Epistemic labels as in the
experiment plan ([SF]/[EE]/[INF]/[REC]/[PX]/[GATE]).

This plan covers analysis of (i) the immutable 2025 archive, (ii) new
bench data, and (iii) future campaign data. It defines pipelines and
equations; it performs no analysis itself and edits no data.

---

## 1. Raw-data immutability and provenance

1. **Immutable originals.** The supplied archives are already anchored:
   `inputs/07_HSX_august2025_results_original.zip` is the frozen
   original, SHA-256-verified against `INPUT_CHECKSUMS.sha256` [SF:
   [`00_INPUT_INVENTORY.md`](00_INPUT_INVENTORY.md) Group A]. The
   extracted tree `../../07_HSX_august2025_results/` is treated
   read-only by every mission rule and every script below.
2. **Extend the same discipline to new data [REC]:** every bench or
   campaign acquisition lands in a dated `raw/` directory, checksummed
   (SHA-256 manifest) the day of acquisition, and never edited; all
   processing writes to `derived/` keyed by the manifest hash. The 02
   project already has the seed convention
   (`data/2026-07-08_test_spin.csv` + journal entry) [SF].
3. **Provenance chain per derived artifact:** input hashes, script name +
   version (git hash if the repo is versioned; else file hash), parameter
   set (f_spin, blanking fraction, calibration constants with their
   dates), and output hash. A one-line JSON sidecar per artifact
   suffices [REC].
4. **Calibration constants are data:** every m, b, k, S_v, and
   temperature coefficient is stored with value, uncertainty, method,
   date, die/board serial, and the B-01 gate status at the time — so no
   trace can ever be converted with an orphaned constant [REC].
5. **Bench-truth rule** carried from the parent memory: measured values
   are never "corrected" in analysis; discrepancies are flagged and
   traced (e.g., the C017 anomaly workflow) [SF: parent CLAUDE.md rule].

## 2. Metadata, logging, and failure records

### 2.1 Bench session schema
Session date/operator; board serial; die serial + resistance-map ref;
source identity + measured bias (R9/R10 drops); f_spin; blanking; scope
config; ambient temperature; linked raw files. One row per acquisition.

### 2.2 Campaign shot schema (mandatory, experiment plan §10.3)
`shot_id, timestamp, machine_config, coil_setpoints, plasma_or_coilonly,
bias_mode, bias_setting, bias_measured, f_spin, blanking, scope_strategy,
trigger_source, trigger_offset_measured, files[], operator_notes,
anomaly_flag`. The 2025 single-docx manifest is the failure mode this
schema prevents [INF].

### 2.3 Failure/abort records
Aborted shots, railed channels, tripped health checks (F-07) are logged
with the same schema plus a reason code — they are data (attrition
reporting in the uncertainty plan §6), not deletions [REC].

---

## 3. Preprocessing pipelines

### 3.1 The 2025 voltage-domain archive (A-group inputs)
1. Parse `test_note.docx` → shot/classification table (A-01); join to
   `scope_N.csv` by acquisition order; flag unmapped files.
2. Per trace: units check (`second,Volt` two-column format [SF]),
   monotonic-time check, sampling-rate extraction, duplicate/NaN scan.
3. Offset handling: the legacy scripts subtract a fixed
   `amp_offset = 4 mV` [SF: Group C]; the new pipeline re-estimates the
   pre-trigger baseline per trace and reports both, rather than
   inheriting the constant blindly [REC].
4. Segmentation: pre-shot quiet window (noise, A-05), ignition
   transient (A-02), discharge window (A-03/A-04), post-shot.
5. No filtering before feature extraction beyond documented anti-alias
   decimation; any additional filter is named (type, order, cutoff,
   zero-phase application) and identical across compared traces [REC].

### 3.2 Spun-readout bench/campaign data (B/C/D/F-group inputs)
The demod chain is fixed by the verified reference implementation
(`hsx_demod_scope_csv.py`; sync reconstruction + `a0==a2` sign rule +
30 % default blanking + runt rejection) [SF]. Pipeline: sync
reconstruction → phase indexing → blanking → per-phase means → signed
8-phase rolling average → `V_demod(t)`. Parameters (f, blanking) come
from the B-06 study, are frozen before C-02, and are recorded per §1.3.
`spin_verify_nosync.py` is the fallback when sync is missing [SF].

### 3.3 Calibration application and offset removal
- Current-bias: `B̂(t) = (V_demod(t) − b)/m` with (m, b) from C-02 and
  the same-day zero-field b check; b drift between checks enters the
  budget (C-08 term).
- Voltage-bias (2025 retroactive, G-01): see §4.2.

### 3.4 Synchronization
2025 data: diamagnetic-loop `.dat` vs scope time aligned by measured
cross-correlation lag (A-03), reported with its CI — the ~30 ms figure
becomes a measured quantity. Campaign data: trigger-channel offset (F-04)
applied; residual jitter kept as a timing-uncertainty term.

### 3.5 Bandwidth estimation
Transfer-function measurements (B-03/B-04): swept-sine amplitude/phase
ratio with coherence check; −3 dB read from the fitted response (state
the fit family, e.g., single-pole vs measured-shape interpolation — do
not force a model that visibly misfits [REC]). Noise PSDs (A-05/B-05):
Welch, window and segment count stated, ENBW quoted with every floor.

---

## 4. Transfer-function and uncertainty-propagation equations

Full symbolic budget with worked example:
[`04_UNCERTAINTY_AND_STATISTICS_PLAN.md`](04_UNCERTAINTY_AND_STATISTICS_PLAN.md)
§3. Summary here for pipeline implementation.

### 4.1 Current-bias (2026 chain)
`V_demod = m·B_⊥ + b`, `m = G·L·S_I·I` [SF: SPECS model; every factor
measured per experiment plan §3–§4].
Inverse: `B̂ = (V_demod − b)/m`.
First-order combined uncertainty (uncorrelated terms; correlation
handling and Monte-Carlo cross-check in the uncertainty plan §3.5):

```text
u(B̂)^2 = (u(V)/m)^2 + (u(b)/m)^2 + ((V−b)/m^2)^2 · u(m)^2
u(m)/m  = sqrt[ (u(k)/k)^2 + (u(I)/I)^2 + u_fit^2 + u_align^2 + (dm/dT·u(ΔT)/m)^2 ]
```

### 4.2 Voltage-bias (2023 chain, 2025 data — G-01)
`V_out = A_v·S_v·V_bias·B_⊥ + A_v·V_off(T)` (C023 [SF]).
Because V_off was never measured [SF: C005], absolute DC levels do not
convert; **changes** do:
`ΔB̂ = ΔV_out / (A_v·S_v·V_bias)` over windows where V_off(T) is
approximately constant; the V_off drift bound over the window (from C-07
temperature coefficient × bounded ΔT, F-05 fallback) enters as an
additive uncertainty term. Fig. 5-class re-plots therefore show
`B(t) − B(t_ref)` (or equivalently transient amplitude in tesla) with
bands, not absolute field — exactly the honest form AE-05's
"uncertainty regions acceptable" invites [REC]. Additional G-01 terms:
u(S_v) from C-03, u(A_v) (gain-200 basis, gate I-6), die-transfer term
if a sibling die was used (D-01 spread), and the bias-setting term
(nominal 0.2–0.4 V wavegen settings, unlogged actuals [SF: C022]).

### 4.3 Coil-only anchor comparison (F-01)
Per setting: measured `B̂_i` (i = 1…n shots) vs computed `B_vac` at the
surveyed pose. Report `Δ = mean(B̂) − B_vac`, spread of B̂_i, and the
joint uncertainty `u_joint = sqrt(u(B̂)^2 + u(B_vac)^2 + (|∇B|·u_pose)^2
+ u_angle^2)`. Consistency criterion `|Δ| ≤ 2·u_joint` [REC]; failures
trigger investigation (§9 falsification duty), never post-hoc widening.

---

## 5. 1:1 comparison metrics, residuals, confidence intervals, effect sizes

For any co-located comparison (E-02 2025 records if they exist, else
F-03 campaign data) and for the diamagnetic-loop correlation (A-03):

1. **Time-domain residuals** (like-vs-like only): resample both signals
   to a common timebase; compare in the overlapping bandwidth after
   applying the measured transfer functions of *both* instruments
   (B-dot signals integrate; integrator/droop characteristics must come
   from UW channel documentation — a U-1 sub-ask [GATE]). Report
   residual RMS, bias, and residual-vs-amplitude structure.
2. **Bland–Altman-style agreement** for paired per-shot scalar features
   (e.g., transient peak amplitude): mean difference (bias), limits of
   agreement, with CIs.
3. **Correlation + lag** (A-03): normalized cross-correlation r(lag);
   peak r and lag with block-bootstrap CIs (blocks ≥ the signal
   autocorrelation time so the CI is honest [REC]). Never quote r
   without n, bandwidth, and lag convention.
4. **Effect sizes:** for class contrasts (e.g., biased vs unbiased
   amplitude; discharge classes), report the absolute effect in physical
   units with CI, plus a standardized measure (difference / pooled
   between-shot SD) so "clear response" becomes a number [REC].
5. **What is *not* claimed:** no field-magnitude bound from the
   diamagnetic loop (different measurand — R1-02's own point [SF]); no
   1:1 claim of any kind until U-1 or F-03 supplies co-located field
   data [SF: matrix disposition].

## 6. Hall-origin (bias-scaling) analysis — A-04

Regress transient amplitude on nominal V_bias across A-01-classified
comparable shots; slope CI vs proportionality; unbiased shots as the
zero-point null. Confounds declared: bias settings were not randomized
in 2025 and actual bias voltages were not logged [SF: C022] — the
analysis is observational, and its conclusion is worded accordingly
("consistent with Hall scaling") rather than causally [REC].

## 7. Repeated-measures and shot-variability handling

Unit definitions and variance components:
[`04_UNCERTAINTY_AND_STATISTICS_PLAN.md`](04_UNCERTAINTY_AND_STATISTICS_PLAN.md)
§2/§4. Analysis rules:

1. **The shot is the primary statistical unit** for in-machine claims;
   time-samples within a shot are non-independent (autocorrelation) and
   never counted as replicates.
2. Per-shot feature extraction first (amplitude, timing, correlation,
   noise floor), then statistics across shots: median/IQR always
   reported alongside mean/SD (small n, no normality assumption) [REC].
3. Class comparisons: with n≥3 per cell, nonparametric or
   permutation-based contrasts preferred at these sample sizes;
   parametric CIs reported in parallel where reasonable.
4. Time-order regression across the run day (drift/warm-up check) using
   the recorded run order (§2.2).
5. Bench repeated measures mirror this: die = unit for D-01, remount
   cycle = unit for D-02, sweep repetition = unit for C-02 precision.

## 8. Leakage and overfitting safeguards

No ML method is required by any Tier-1 claim [INF]. Safeguards, scaled
to what is actually planned:

1. **Calibration fitting (C-02/C-03):** training/held-out field-point
   split per the 02 plan §7.3 [SF]; held-out points (interleaved, both
   polarities, one elevated-T point) are never used to refit; report
   held-out % error, worst-case and RMS.
2. **Frozen parameters:** f_spin, blanking, filter choices frozen from
   B-06 before calibration data is taken; any re-tuning after seeing
   calibration residuals restarts the acquisition, not the fit [REC].
3. **No post-hoc metric shopping:** the comparison metrics of §5 are
   pre-declared here; additions are labeled exploratory in any
   manuscript [REC].
4. **If/when WP-D estimation work starts (P2/RSI scope):** shot-level
   splits only (never time-sample splits of the same shot across
   train/test); tuning on a validation split, single touch of the test
   split; synthetic-data validation before machine data; baseline
   comparison against the plain integrator and the plain Hall channel —
   precedent norms from the tokamak drift-fusion lineage
   ([S0118](https://doi.org/10.1088/1741-4326/adb599),
   [S0122](https://doi.org/10.1016/j.fusengdes.2025.115180)) [EE].
5. **Selective-reporting guard:** A-01's census defines the shot
   population once; every later analysis states n as
   "x of the N classified shots" with exclusions itemized [REC].

## 9. Figures and tables mapped to claims

Extends the stage-30 revision map
([`03_MANUSCRIPT_DIAGNOSIS.md`](03_MANUSCRIPT_DIAGNOSIS.md) §7) from
"what to change" to "which artifact proves it":

| Artifact | Claim it carries | Data source | Requirement |
|---|---|---|---|
| Table: shot census | Corrected shot-count wording (A5) | 2025 archive | A-01 |
| Fig: transient-statistics distribution | Operational repeatability (R-3 → statistic) | 2025 archive | A-02 |
| Fig/Table: r(lag) + CI, measured DAQ offset | Quantified tracking (R-4) | 2025 archive | A-03 |
| Fig: amplitude vs V_bias | Hall origin (M8) | 2025 archive | A-04 |
| Fig: in-situ V/√Hz PSD | Noise in machine environment (AE-07 part) | 2025 archive | A-05 |
| Fig: calibration line + residuals + held-out errors | Absolute calibration (AE-01/AE-04/R1-01) | bench | C-02 |
| Fig 5 (re-plot): field-unit overlay with bands | AE-05 + R1-05 | 2025 archive × C-03 | G-01 |
| Table: uncertainty budget | Honest tesla claim | bench + budget | uncertainty plan §3 |
| Fig/Table: offset — raw vs spun residual, die | Offset headline (C-05); emulator kept separate | bench | C-05 |
| Fig: transfer function + phase, per chain, basis labeled | Bandwidth (AE-07/R1-04; 1 MHz retired) | bench | B-03/B-04 |
| Table: die-to-die m and offset statistics (or fallback block) | Repeatability (AE-03/R2-02) | bench | D-01/D-02 |
| Table: WP-A comparison (12 dimensions) | Positioning/novelty (AE-02/R2-01) | ledger, re-confirmed | stage 30 §3 |
| Fig: Allan deviation | Drift/long-pulse credibility | bench | C-08 |
| Fig: measured vs computed B_vac per setting | Absolute anchor (RSI centerpiece) | campaign | F-01 |
| Fig: b(t) over shot sequence | In-vessel offset stability vs 2023 V_off | campaign | F-06 |

Rule: **no figure appears in a manuscript without its requirement row
closed and its uncertainty band drawn from the budget** [REC].

## 10. Reproducible scripts and data-release structure

1. **One repository, one entry point per artifact** [REC]: each §9 row
   is produced by a single script (`analysis/aXX_*.py` naming mirroring
   requirement IDs) reading only `raw/` + constants files, writing only
   `derived/` + `figures/`. Existing tools
   (`hsx_demod_scope_csv.py`, `spin_verify_nosync.py`, the legacy `.m`
   scripts as cross-checks) are wrapped, not rewritten, unless a defect
   is found — in which case the defect is logged first [REC].
2. **Environment pinning:** Python version + package lockfile committed;
   MATLAB scripts (if retained for cross-checks) pinned by version note.
3. **Determinism:** any resampling/bootstrap uses a recorded seed.
4. **End-to-end re-run check** before any submission: fresh clone →
   `make all` (or equivalent) reproduces every figure/table byte-stable
   or within documented floating-point tolerance.
5. **Release package** (journal/repository dependent; release itself is
   a user action outside this mission's execution scope): raw immutable
   archives + checksums, constants files with uncertainties, scripts +
   lockfile, per-figure provenance sidecars, shot-census table, README
   mapping artifacts to manuscript claims. The IEEE/AIP sharing-policy
   specifics were verified in stage 30
   ([`03_PUBLICATION_ROUTE_DECISION.md`](03_PUBLICATION_ROUTE_DECISION.md));
   nothing here presumes a particular venue.
6. **What is never released:** any UW-provided machine data without UW
   consent (collaboration norm; also feeds the stage-50 IP screen
   ordering) [REC].
