# Stage 10C -- low-fabrication novelty and methods evidence batch: synthesis

Source: [`evidence/10C_METHODS_SOURCES.csv`](10C_METHODS_SOURCES.csv) (74 rows, `C0001`-`C0074`).
This is the third of three parallel literature lanes (10a/10b/10c) that feed the merged,
deduplicated `outputs/01_SOURCE_LEDGER.csv` at stage `10d_literature_merge`. IDs in this file are
provisional (`C####`) and will be renumbered `S####` at the merge stage per `SOURCE_POLICY.md`.
This stage does not decide PhD direction, manuscript route, or publication strategy (reserved for
stages `20_direction` / `30_manuscript`) and does not rank final directions.

## 1. Search and verification method

**External evidence.** Seven parallel auxiliary-model (Sonnet, general-purpose agent) research
lanes were run in parallel, one per required coverage bullet: (1) calibration matrices,
self-calibration, uncertainty propagation, sensor fusion, system identification, inverse methods,
Bayesian estimation; (2) signal processing for offset/noise/drift separation and transient magnetic
measurement; (3) physics-informed and data-driven reconstruction for plasma magnetic diagnostics;
(4) digital twins, surrogate models, and real-time estimation/control with a concrete measurement
role; (5) multi-axis/vector sensing, arrays, spatial reconstruction, and model-based validation;
(6) reproducibility, device-to-device statistics, metrology, traceability, and instrument
qualification; (7) precedent for application/system novelty over new device topology. Each lane
used `WebSearch` to find candidates and verified every counted paper via the Crossref API
(`api.crossref.org/works/<doi>` or a bibliographic query), a PubMed/PMC record, or a direct
publisher DOI-landing-page fetch -- never a search snippet alone. Combined raw yield across the
seven lanes was 108 candidate rows; each lane also reported dropping additional candidates that
failed independent verification (e.g. an unverifiable IEEE conference paper, a mismatched initial
DOI later corrected via Crossref) rather than guessing.

**This main session then performed three dedup/inclusion passes, in order:**

1. **Within-batch DOI dedup.** Deduplicated all 108 rows by normalized DOI across the seven lanes,
   removing 9 duplicate occurrences (the same paper independently surfaced by more than one lane
   -- e.g. Lao et al. 1985's EFIT paper was found by both the calibration/inverse-methods lane and
   the physics-informed-reconstruction lane; the Quercia et al. 2022 JET Hall-probe paper was found
   by both the metrology/qualification lane and the application-novelty lane). This left 99 unique
   DOIs.
2. **Cross-stage DOI dedup against the already-completed Stage 10A and 10B ledgers.** Because
   several 10C coverage bullets (offset/drift signal processing; fusion-context Hall-probe
   qualification; application-novelty precedent) overlap thematically with Stage 10A's
   spinning-current lane and Stage 10B's fusion-Hall-probe and magnetic-diagnostic-system lanes,
   25 of the 99 unique-to-10C candidates turned out to share an exact DOI with a row already
   verified and counted in `evidence/10A_GAN_WBG_SOURCES.csv` or
   `evidence/10B_FUSION_DIAGNOSTICS_SOURCES.csv`. Unlike Stage 10A/10B's single incidental
   cross-lane overlaps (each flagged but kept in-ledger, since dedup across lanes is formally stage
   `10d`'s job), this batch's overlap was large enough (25 of 99, ~25%) that keeping every
   duplicate would pad this stage's count without adding new coverage and would create needless
   dedup work for stage `10d`. This session therefore proactively excluded these 25 rows from
   `10C_METHODS_SOURCES.csv` rather than deferring the removal, since the source is already
   verified and counted once. This is a deliberate, stricter judgment call for this stage,
   explicitly logged here for the merge stage's benefit; it is consistent with, not a departure
   from, `SOURCE_POLICY.md`'s "deduplicate by normalized DOI first" rule -- it simply performs that
   dedup now instead of leaving it entirely to stage `10d`. The excluded DOIs, with their existing
   ledger IDs, are listed in full in Section 6 below for traceability.
3. No off-topic exclusion was needed this stage (unlike Stage 10A's exclusion of a GMR biosensor
   paper and Stage 10B's exclusion of a CERN accelerator paper): every remaining candidate ties
   concretely to the GaN/HSX magnetic-diagnostic problem or to a coverage bullet the stage prompt
   explicitly asked to be searched broadly (e.g. bullet 7 explicitly requested cross-field
   application-novelty precedent from space, geothermal, and deep-sea instrumentation). One
   borderline case was kept rather than dropped: Amodeo, Arpaia & Buzio 2019 (`C0023`, a CERN
   particle-accelerator drift-correction paper) was excluded by Stage 10B as off-topic for a
   *fusion-diagnostics* lane, but is included here because Stage 10C's coverage bullet is general
   offset/noise/drift signal processing, not fusion-restricted; this distinction is noted directly
   in the row's `notes` field.

This left **74 valid, unique, verified peer-reviewed rows**, exceeding both the 65-source target
and the 55-row floor. No DOI in the ledger was guessed; every row's `doi` field is a bare,
Crossref-registered DOI, and `url` is the corresponding `https://doi.org/...` resolver link.

**Inference (this stage).** As in Stages 10A/10B, most full-text publisher pages (ScienceDirect,
AIP Publishing, some IEEE Xplore records) blocked automated fetches -- a structural access
limitation, not a shortcut. Access-level breakdown: 58 `abstract_metadata`, 12 `full_text`
(mostly open-access MDPI/PMC/arXiv-mirrored papers), 4 `metadata_only` (bibliographic identity
only, abstract not independently retrieved this session -- these rows' `claims_supported` and
`notes` fields are worded to reflect title-level, not content-level, confirmation).

## 2. Method taxonomy

The 74 rows organize into the seven required coverage bullets (provisional ID ranges reflect
search-lane order, not a ranking):

| # | Coverage bullet | IDs | Rows | Representative sources |
|---|---|---|---:|---|
| 1 | Calibration matrices, self-calibration, uncertainty propagation, sensor fusion, system ID, inverse methods, Bayesian estimation | `C0001`-`C0015` | 15 | `C0002`/`C0003` (Bayesian integrated data analysis, incl. a stellarator/W7-AS application), `C0007` (Bayesian inverse-method current tomography), `C0011` (Allan variance) |
| 2 | Signal processing for offset/noise/drift separation and transient measurement | `C0016`-`C0023` | 8 | `C0016` (fusion-context pulsed-field Hall sensing), `C0019` (chopper/CDS/autozero foundational review), `C0022` (Kalman-filter drift-free integration) |
| 3 | Physics-informed / data-driven plasma-magnetic reconstruction | `C0024`-`C0037` | 14 | `C0024` (DNN Grad-Shafranov solver, KSTAR), `C0032` (stellarator-class PINN, W7-X), `C0031` (V3FIT, stellarator-class, validated on CTH) |
| 4 | Digital twins, surrogate models, real-time estimation/control with concrete measurement role | `C0038`-`C0050` | 13 | `C0039` (fusion digital-twin review), `C0046` (RAPTOR, ITER), `C0050` (digital-twin precedent outside fusion) |
| 5 | Multi-axis/vector sensing, arrays, spatial reconstruction, model-based validation | `C0051`-`C0060` | 10 | `C0051` (single-die 3D Hall vector sensing), `C0053` (D-optimality array-placement validation), `C0059` (Cluster multi-point curlometer) |
| 6 | Reproducibility, device-to-device statistics, metrology, traceability, instrument qualification | `C0061`-`C0067` | 7 | `C0061` (device-to-device Hall-cell geometry statistics), `C0062` (magnetic-measurement traceability routes), `C0066` (cross-cutting ICF/MCF diagnostic-qualification review) |
| 7 | Application/system novelty over new device topology | `C0068`-`C0074` | 7 | `C0068` (bismuth Hall sensor named to one tokamak), `C0069` (RSI system-integration precedent, RADCAM), `C0073` (explicit "for the first time" deployment framing, geothermal fiber optic) |

Venue concentration (74 rows, 39 distinct venues): *Sensors* (12), *Nuclear Fusion* (11), *Review
of Scientific Instruments* (6), *IEEE Transactions on Magnetics* (3), *Fusion Engineering and
Design* (3), *Proceedings of the IEEE*, *Plasma Physics and Controlled Fusion*, *IEEE Transactions
on Instrumentation and Measurement*, *IEEE Sensors Journal*, and *Physics of Plasmas* (2 each),
with the remaining 29 venues appearing once. Year range 1960-2026 (9 rows pre-2000, foundational
estimation/instrumentation theory; 44 of 74 rows from 2015-2026, reflecting that most of this
batch's methods -- ML/PINN equilibrium reconstruction, digital twins, modern calibration algorithms
-- are recent). Source type: 70 `journal_article`, 3 `review_article`, 1 `conference_paper`.
Quality tier: 40 `A`, 30 `B`, 4 `C`.

## 3. Feasibility with existing devices/data versus requirements for new experiments

**Achievable using only the existing GaN Hall sensor, its bench/HSX data, and software/analysis
work (no new fabrication, no new HSX campaign):**

- A rigorous **calibration-matrix and Bayesian-uncertainty treatment** of the existing sensor's
  offset/sensitivity/temperature behavior (`C0001`, `C0004`, `C0008`, `C0017`), replacing the
  "V_off unknown" gap the 2023 manuscript's own stated future work flagged.
- A **device-to-device statistics study**, if even 2-3 more dies from the same fabrication run
  (already fabricated, not new cleanroom work) are bench-characterized using the protocol in
  `C0061` -- directly answers the "only one device tested" review criticism using hardware
  that likely already exists in the Senesky lab.
- **Reprocessing existing HSX bias-voltage-domain data** with Allan-variance drift analysis
  (`C0011`), lock-in/synchronous-detection-style post-processing (`C0020`), or a Kalman-filter
  fusion of the Hall signal against the existing diamagnetic-loop signal (`C0003`, `C0022`) --
  pure signal-processing, needs only the raw data already in hand.
- A **formal metrology/traceability writeup** of whatever calibration procedure was actually used
  (`C0062`, `C0064`), even retroactively, using GUM or Monte-Carlo uncertainty propagation
  (`C0063`).

**Requires new bench work but no new device fabrication (existing sensor, new measurement/test):**

- **Linearity/temperature/high-field qualification testing** of the existing sensor across its
  real operating envelope, following the ITER Hall-sensor qualification template (`C0067`) --
  needs bench time and equipment (temperature chamber, calibrated field source), not new dies.
- **A Biot-Savart-model-validated sensor-placement study** (`C0053`, `C0060`) for the *next*
  campaign's probe position, using CAD/field-simulation software against HSX's known coil
  geometry -- computational, but needs the actual HSX vacuum-field model as an input.

**Requires new HSX experiment/campaign (deferred to stage `40_experiment`, not decided here):**

- Any claim benchmarked against a **conventional-probe comparison** (the AEIC's explicit request)
  needs an actual co-located B-dot/Mirnov measurement during a real shot; no source in this batch
  substitutes for that missing HSX-specific data.
- A genuine **multi-axis vector-probe spatial-reconstruction demonstration** (`C0059`, `C0031`)
  needs project 03's 2-3 axis hardware actually built and deployed; this batch supports the
  *methodology* for validating such a probe once it exists, not a way to skip building it.
- A **physics-informed or ML-based HSX-specific equilibrium/field reconstruction** (`C0024`,
  `C0032`, `C0035`) needs a training/validation dataset of HSX discharges with known ground truth
  (e.g. from V3FIT) -- this batch shows the method works elsewhere (KSTAR, W7-X, NSTX-U, MAST,
  DIII-D), but **no source in this batch demonstrates it has been done on HSX specifically**; that
  is new analysis work, not new fabrication, but it is not free -- it needs HSX-specific discharge
  data and a validated forward model to train/constrain against.

## 4. Compute/software burden and data prerequisites

| Method class | Compute burden | Software prerequisite | Data prerequisite |
|---|---|---|---|
| Calibration matrix / Bayesian calibration (`C0001`, `C0004`) | Low (offline least-squares/MCMC on a laptop) | Standard numerical/statistics stack (e.g. Python/MATLAB with a Bayesian-inference library) | Multi-orientation or multi-field-point bench calibration dataset |
| Allan variance / drift characterization (`C0011`) | Low | Any time-series analysis environment | A long, evenly-sampled static/quiet time series from the existing sensor |
| Kalman-filter / EKF sensor fusion (`C0003`, `C0022`, `C0045`, `C0046`) | Low-moderate (real-time-capable on a microcontroller for deployment; trivial offline) | A filtering library or a from-scratch EKF implementation; requires a stated process/measurement model | Time-synchronized data from the Hall sensor and the diagnostic(s) it is fused with (e.g. diamagnetic loop) |
| Inverse-method / regularized reconstruction (`C0007`, `C0009`, `C0010`) | Low-moderate (iterative linear solves) | A regularization/optimization library (Tikhonov, SVD) | A forward model (Biot-Savart or Grad-Shafranov-type) linking sensor readings to the reconstructed quantity |
| PINN / data-driven equilibrium reconstruction (`C0024`, `C0032`, `C0035`, `C0036`) | **High**: the W7-X and KSTAR precedents report multi-day single-GPU training (`C0032`: ~8 days on one V100); real-time inference is fast (sub-ms to ~1 ms) but training is the expensive step | A deep-learning framework (PyTorch/TensorFlow/JAX) and, for physics-informed variants, an autodiff-compatible MHD/Grad-Shafranov formulation | A large discharge database (KSTAR's DNN solver used 1,118 discharges) or a "data-free" formulation (`C0035`) that trades the training-data requirement for a heavier per-instance PDE-residual optimization -- **HSX has no such existing discharge-magnetics database at the scale used by these precedents**, an evidence gap this batch does not close |
| Digital twin / real-time state observer (`C0038`, `C0047`, `C0049`) | Moderate (an EKF/state-observer runtime is lightweight; building and validating the physics model behind it is the real effort) | A dynamic-systems/control-toolbox environment; ideally a real-time-capable target if deployed live | A validated reduced physics model of the plant (plasma or sensor-response dynamics) to observe against |
| Sensor-array placement optimization (`C0053`, `C0054`) | Low-moderate (a D-optimality/particle-swarm search over candidate geometries) | An optimization library plus a field-forward-model (Biot-Savart) | HSX's known coil/vessel geometry as the forward-model input |

**Cross-cutting point:** every method in the "low-moderate" compute rows above is achievable on
existing hardware/data with a laptop and open-source software -- these are the most immediately
actionable novelty paths. The PINN/data-driven-reconstruction row is the one method class in this
batch with a genuine, non-trivial data prerequisite (a discharge database HSX does not yet have at
the scale used by precedent) that stage `40_experiment` would need to address explicitly rather
than assume away.

## 5. Common overclaiming traps

1. **Calling calibration or current-spinning itself "novel."** `C0001` (Renaudin et al.),
   Munter's foundational spinning-current paper (already verified and counted in Stage 10A as
   `A0033`, not re-listed here since it is a cross-stage duplicate -- see Section 6), and `C0019`
   (Enz & Temes 1996) collectively show these are decades-old, thoroughly characterized techniques.
   The novelty has to be in the *specific rigor, the specific fused/estimated quantity, or the
   specific deployment context* -- not the calibration act itself. This directly echoes Reviewer
   2's decline rationale already logged in `outputs/00_CLAIM_BASELINE.csv`.
2. **Presenting a PINN/ML equilibrium-reconstruction result without a stated ground truth.**
   Every credible source in this batch (`C0024`, `C0032`, `C0035`) reports a specific accuracy
   metric (RMSE, R^2, MAPE) against a named reference (VMEC, EFIT, Thomson scattering). A paper
   that reports only "the network reconstructs the field" without quantified error against a
   validated reference would not meet this batch's own established norm.
3. **Treating a single simulation-only "data-free" PINN result (`C0035`) as production-ready.**
   Its own abstract-level claim is that it solves the PDE without a training database, not that it
   matches or exceeds specialized production solvers (DESC/VMEC) in the general case; `C0037`
   (Thun et al. 2026) explicitly frames its own contribution as still catching up to conventional
   solvers' residual floor. A claim that a PINN "replaces" VMEC/EFIT-class tools would overreach
   what this batch's own most recent (2026) source claims for itself.
4. **Calling a system-integration or first-deployment paper a "device advance."** The
   application-novelty precedents in this batch (`C0068`-`C0074`) are explicit that their
   contribution is framed as integration, qualification, or first-in-environment deployment of
   *existing* technology. Retroactively describing such work as a device-physics contribution
   (rather than a system/application contribution) would misstate its own precedent's framing and
   invite exactly the kind of reviewer pushback the 2023 manuscript already received.
5. **Citing a foundational estimation-theory paper (Kalman 1960, `C0014`; Astrom & Eykhoff 1971,
   `C0006`) as if it were itself evidence of GaN-Hall-specific or fusion-specific novelty.** These
   are correctly used only as the *theoretical basis* for a specific, new applied contribution --
   not as substitutes for demonstrating that contribution.
6. **Assuming a method demonstrated on a tokamak (KSTAR, DIII-D, NSTX-U, MAST) transfers to a
   stellarator (HSX) without modification.** Only `C0032` (W7-X), `C0031` (V3FIT/CTH), and
   `C0036` (W7-X ANN topology reconstruction) in this batch are stellarator-class precedents; the
   majority of the ML/PINN equilibrium-reconstruction literature here is tokamak-specific, and
   stellarators' fully 3D (non-axisymmetric) geometry is a substantive, not cosmetic, difference
   that a direct-porting claim would need to address rather than assume.
7. **Treating "abstract_metadata" or "metadata_only" verification as full-text confirmation of a
   quantitative claim.** 62 of this batch's 74 rows are `abstract_metadata` or `metadata_only`
   (Section 1); any later stage citing a specific number from one of those rows should note it
   came from an abstract or bibliographic record, not an independently read full body/methods
   section, per the mission's stated evidentiary-honesty requirement.

## 6. Cross-stage DOI overlaps excluded from this ledger (for stage 10d traceability)

The following 25 DOIs were found independently by a Stage 10C lane but excluded from
`10C_METHODS_SOURCES.csv` because they are exact-DOI duplicates of a row already verified and
counted in Stage 10A's or Stage 10B's ledger (Section 1, dedup pass 2). Listed for stage `10d`'s
audit trail; no further action is needed from that stage beyond confirming these are already
present under their original `A####`/`B####` ID.

| Already-covered topic | DOI | Already in |
|---|---|---|
| Lao et al. 1985, EFIT foundational inverse-reconstruction paper | 10.1088/0029-5515/25/11/007 | 10B |
| Dowling et al. 2019, AlGaN/GaN current-spinning offset paper (same Senesky-group device lineage) | 10.1109/LSENS.2019.2898157 | 10A |
| Munter 1990, foundational spinning-current Hall plate | 10.1016/0924-4247(89)80069-X | 10A |
| Steiner et al. 1998, continuous spinning-current method | 10.1016/S0924-4247(98)00003-X | 10A |
| Bellekom & Sarro 1998, offset reduction across crystal planes | 10.1016/S0924-4247(97)01700-7 | 10A |
| Lee et al. 2020, delta-sigma-ADC Hall readout | 10.3390/s20185285 | 10A |
| Spuig et al. 2015, WEST integrators | 10.1016/j.fusengdes.2015.06.047 | 10B |
| Chen et al. 2023, EAST long-pulse magnetic diagnostics | 10.1088/2058-6272/ace87d | 10B |
| Alpert et al. 2019, AlGaN/GaN Hall geometry (Senesky group) | 10.1109/JSEN.2019.2895546 | 10A |
| Buschel et al. 2024, synthetic Mirnov diagnostic W7-X | 10.1063/5.0190619 | 10B |
| Pons-Villalonga et al. 2025, Mirnov array stellarator TJ-II | 10.1063/5.0244636 | 10B |
| Hole et al. 2009, high-resolution Mirnov array MAST | 10.1063/1.3272713 | 10B |
| Endler et al. 2015, W7-X magnetic-diagnostics engineering design | 10.1016/j.fusengdes.2015.07.020 | 10B |
| Wouters et al. 2016, innovative three-axis Hall sensor | 10.1016/j.sna.2015.11.022 | 10B |
| Strait 2006, DIII-D magnetic diagnostic system | 10.1063/1.2166493 | 10B |
| Paun et al. 2013, comparative study of five Hall devices | 10.3390/s130202093 | 10A |
| Gerken et al. 2020, traceably calibrated scanning Hall probe | 10.5194/jsss-9-391-2020 | 10A |
| Quercia et al. 2022, JET long-term radiation-hard Hall probes | 10.1088/1741-4326/ac8aad | 10A and 10B |
| Entler et al. 2018, ITER high-field Hall-sensor test | 10.1063/1.5038812 | 10B |
| Adaikkan et al. 2022, LTCC sensors for ITER | 10.1016/j.fusengdes.2022.113316 | 10B |
| Shen 2016, EAST calibration/uncertainty analysis | 10.1016/j.fusengdes.2016.02.051 | 10B |
| Ivanek et al. 2025, Hall/coil data fusion via Kalman filtering | 10.1016/j.fusengdes.2025.115180 | 10B |
| Entler et al. 2019, antimony Hall sensors for future reactors | 10.1016/j.fusengdes.2019.01.013 | 10A |
| Entler et al. 2021, ceramic-chromium Hall sensors harsh environment | 10.3390/s21030721 | 10B |
| Kovarik et al. 2006, CASTOR safety-factor Hall probes | 10.1007/s10582-006-0185-4 | 10A and 10B |

(Table has 25 entries. Two of them -- Quercia et al. 2022 and Kovarik et al. 2006 -- are each
already flagged as overlapping *both* 10A and 10B per `evidence/10B_SYNTHESIS.md` section 1, so
their "Already in" column lists both stages rather than one.)

## 7. Direct implications for publishable, low-cleanroom PhD directions

These are inferences from this batch's literature only, not a decision (reserved for stage
`20_direction`):

- The single most literature-dense, low-burden novelty path this batch supports is **a rigorous
  calibration/uncertainty/reproducibility treatment of the existing GaN Hall sensor and its
  existing HSX data** (bullets 1, 2, 6): every needed method (Bayesian calibration, Allan-variance
  drift characterization, GUM/Monte-Carlo uncertainty budgets, device-to-device statistics) has
  multiple mature, directly citable precedents, requires no new fabrication, and directly answers
  the specific gaps (`C0001`-style "V_off unknown", "only one device tested") already logged as
  reviewer concerns.
- **Sensor fusion of the Hall signal with HSX's existing diamagnetic-loop/pickup-coil data** via a
  Kalman-filter or Bayesian-graphical-model architecture (bullets 1, 4) is the second
  most-supported low-burden path, with a stellarator-specific precedent (`C0003`, W7-AS) that is
  unusually close to HSX's own facility class.
- **A physics-informed or data-driven reconstruction demonstration specifically on HSX** (bullet 3)
  is well-precedented in *method* (14 rows, several stellarator-class) but has a real, literature-
  confirmed data-prerequisite gap: this batch found no existing large HSX discharge-magnetics
  database comparable to what the KSTAR/W7-X/NSTX-U precedents trained on. This is a
  higher-payoff, higher-effort direction that stage `40_experiment` should size explicitly rather
  than assume is free.
- **Multi-axis/vector-probe validation methodology** (bullet 5) is directly relevant to project 03
  but its strongest precedents (`C0053`, `C0059`, `C0060`) validate an array *design*, not a
  single sensor -- reinforcing that this novelty path is tied to the vector-probe hardware actually
  being built, not a software-only substitute for it.
- **Application/system-novelty framing** (bullet 7) has strong precedent that "first deployment of
  an established sensor type in a new environment/device" is independently publishable (`C0068`,
  `C0069`, `C0073`), which is directly relevant to evaluating whether the HSX deployment itself,
  rigorously documented, is a sufficient novelty claim on its own -- a question this stage
  surfaces as evidence but explicitly leaves to stage `20_direction` to decide.

## 8. Row count

**74 valid, unique, verified peer-reviewed rows** (`C0001`-`C0074`), all
`peer_review_status = verified_peer_reviewed`, all deduplicated by normalized DOI both within this
stage's own search (9 within-batch duplicates removed) and against the two already-completed
parallel ledgers (25 further rows excluded as exact-DOI duplicates of Stage 10A/10B rows, listed in
full in Section 6) -- verified programmatically: 74 rows, 16 columns, 0 duplicate `source_id`,
0 duplicate `doi`, 0 duplicate normalized title, 100% `peer_review_status = verified_peer_reviewed`,
all `quality_tier`/`access_level`/`source_type` values within the allowed enums, no empty required
fields, zero residual overlap with the `doi` sets of `evidence/10A_GAN_WBG_SOURCES.csv` and
`evidence/10B_FUSION_DIAGNOSTICS_SOURCES.csv`. This exceeds both the stage floor (55) and the stage
target (65).
