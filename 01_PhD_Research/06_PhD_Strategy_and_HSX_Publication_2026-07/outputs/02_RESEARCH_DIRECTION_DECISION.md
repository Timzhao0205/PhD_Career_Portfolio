# 02 — Research-direction decision (Stage 20)

**Basis:** the validated Stage 10D evidence package
([`01_SOURCE_LEDGER.csv`](01_SOURCE_LEDGER.csv), 231 verified peer-reviewed
sources S0001–S0231; [`01_LITERATURE_REVIEW.md`](01_LITERATURE_REVIEW.md);
[`01_EVIDENCE_MAP.csv`](01_EVIDENCE_MAP.csv)), the Stage 00 baselines
([`00_CLAIM_BASELINE.csv`](00_CLAIM_BASELINE.csv) claims C001–C025;
[`00_CONFLICT_LEDGER.md`](00_CONFLICT_LEDGER.md) conflicts C1–C6), the
supplied decision letter
([`../inputs/Decision_Letter_IEEE_2026-07-23.pdf`](../inputs/Decision_Letter_IEEE_2026-07-23.pdf)),
and direct re-reads of the parent bench truth
([`../../02_HSX_Hall_Sensor_Readout/NOTES.md`](../../02_HSX_Hall_Sensor_Readout/NOTES.md))
and the vector-probe plan
([`../../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md`](../../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md)).
Citations use `[S####]` with a `https://doi.org/...` link on first use.
Supplied project facts cite the file, not a ledger ID. Epistemic labels:
*Supplied fact*, *External evidence*, *Inference*, *Recommendation*,
*Proposed experiment*, *Unresolved gate*.

**Standing corrections this decision honors:** the manuscript is
**unpublished** — submitted 2-Jul-2026, declined 23-Jul-2026 with an
invitation to revise and resubmit (conflict C1; claims C011/C012). The
parent memory's "2023, published" framing is unsupported and is not relied
on anywhere below. Project 02's "calibrated" language is **aspirational**
(conflict C6): the demonstrated result is ≥130× offset cancellation on a
resistor-ring emulator with an open ~109× magnitude anomaly (claims
C016/C017). Tim currently has, per supplied evidence, **zero accepted
first-author publications** — which materially shapes the risk posture of
this decision.

---

## 1. Executive verdict

**CONTINUE the GaN Hall magnetic-diagnostics direction, with a substantial
adjustment in where the novelty is claimed and how the output portfolio is
structured. Decision class: ADJUST (option OPT2). Do not change direction.**

Three findings force each part of that verdict:

1. **The direction is publishable — at a specific claim granularity.**
   Across three independent literature lanes, no peer-reviewed GaN/AlGaN
   Hall sensor was found deployed inside any tokamak or stellarator, and no
   Hall sensor of any kind was found in a quasi-helically symmetric
   stellarator (absence finding; bounded search). Meanwhile, Hall sensing is
   the fusion field's own chosen answer to the integrator-drift problem —
   JET's InSb probes ran 11+ years at ±0.07% stability
   [S0068](https://doi.org/10.1088/1741-4326/ac8aad), and ITER's
   steady-state magnetic diagnostic is a 60-unit bismuth Hall array
   [S0113](https://doi.org/10.1063/1.4732077),
   [S0114](https://doi.org/10.1063/1.5038871). The concept is validated by
   the field; the specific material-plus-facility combination is unclaimed.

2. **Continuing *as currently framed* would fail again.** Reviewer 2's
   novelty objection is the literature's own verdict on device-granularity
   claims: GaN Hall device physics, spinning-current offset cancellation,
   and temperature behavior are already published — largely by the
   advisor's own group [S0004](https://doi.org/10.1109/JSEN.2019.2895546),
   [S0005](https://doi.org/10.1109/LSENS.2019.2898157),
   [S0006](https://doi.org/10.1063/1.5139911),
   [S0012](https://doi.org/10.1063/5.0305414), and spinning-current dates
   to 1990 [S0033](https://doi.org/10.1016/0924-4247%2889%2980069-X). The
   adjustment is to *cite that record as prior art and claim the
   application, the finished calibrated measurement, and the measurement
   architecture* — the granularity at which Reviewer 1 ("novel and unique")
   and the first-deployment publication precedent class
   [S0226](https://doi.org/10.1063/5.0095907),
   [S0227](https://doi.org/10.1007/s11214-025-01170-w),
   [S0230](https://doi.org/10.1186/s40517-021-00204-0) operate.

3. **A genuine change of direction is dominated.** The best-supported
   change option (software-only stellarator-magnetics methods, §3.3) scores
   below both continuation variants: it abandons the single asset no
   competitor has (a survived, shot-resolved in-vessel GaN deployment,
   claims C001/C002), sits poorly with the advisor group's device
   identity, and depends on an HSX training-scale database whose existence
   is NOT ESTABLISHED FROM SUPPLIED FILES. It is retained as the named
   fallback (§8), not the plan.

The adjusted continuation (OPT2) keeps the **finished, absolutely
calibrated sensing output as the non-negotiable centerpiece** — exactly
what the decline letter demands (claim C010) — and layers on
campaign-uncoupled, software-heavy work packages (comparison table,
multi-die repeatability, formal uncertainty budget, hybrid Hall+inductive
drift fusion) so that no single paper depends on both HSX campaigns
happening on schedule. It is also, verbatim, the user's own original
research interest: GaN Hall diagnostics *"with or without conventional
coils sensors, together, to resolve the drift problem"*
([`../inputs/ORIGINAL_REQUEST.txt`](../inputs/ORIGINAL_REQUEST.txt)) — the
original interest was never device novelty; the first manuscript simply
claimed the wrong axis.

---

## 2. Scoring method: scale, weights, calculations, uncertainty, sensitivity

### 2.1 Scale and beneficial-direction convention

Every criterion is scored **1–5, where 5 is always better for Tim**. For
the two burden columns and the risk column this means the scale is
inverted relative to the raw quantity: `cleanroom_burden = 5` means
*lowest* cleanroom burden, `experimental_burden = 5` means *lightest*
experimental load, `schedule_risk = 5` means *lowest* schedule risk. This
is the beneficial-direction convention required by the stage prompt, and
the CSV cells in [`02_DIRECTION_SCORECARD.csv`](02_DIRECTION_SCORECARD.csv)
follow it.

### 2.2 Weights (baseline W_A) and their rationale

Weights are anchored to MISSION.md's fixed preferences (≈2-year
graduation, low cleanroom, novelty in application/software, startup 2029/30
preparation) — not chosen to favor a predetermined winner.

| Criterion | Weight | Rationale |
|---|---:|---|
| 24_month_publishability | 0.20 | Graduation in ~2 years with currently zero accepted first-author papers makes this the binding constraint |
| novelty_strength | 0.15 | The decline was a novelty decline; the next submission cannot lose on this axis again |
| evidence_strength | 0.10 | How much of the option already stands on demonstrated results (claims C001–C023) |
| cleanroom_burden (5=low) | 0.10 | Explicit user constraint |
| experimental_burden (5=low) | 0.08 | Time-cost of bench/campaign work against the 24-month clock |
| software_simulation_leverage | 0.10 | Explicit user preference for novelty via software/simulation |
| advisor_group_fit | 0.12 | The thesis must be defensible in the Senesky group; misfit is a structural risk |
| startup_optionality | 0.07 | Real but subordinate to graduating |
| schedule_risk (5=low) | 0.08 | Exposure to events Tim does not control (HSX schedule, die supply) |
| **Sum** | **1.00** | |

### 2.3 Scores and calculations

Weighted score = Σ (weight × score). Per-cell justifications are in
§3–§5; the arithmetic:

| Criterion (weight) | OPT1 | OPT2 | OPT3 | OPT4 |
|---|---:|---:|---:|---:|
| 24_month_publishability (0.20) | 4 | 5 | 3 | 2 |
| novelty_strength (0.15) | 3 | 4 | 3 | 3 |
| evidence_strength (0.10) | 4 | 4 | 2 | 3 |
| cleanroom_burden (0.10) | 3 | 4 | 5 | 1 |
| experimental_burden (0.08) | 2 | 3 | 5 | 2 |
| software_simulation_leverage (0.10) | 3 | 5 | 5 | 2 |
| advisor_group_fit (0.12) | 5 | 4 | 2 | 5 |
| startup_optionality (0.07) | 4 | 5 | 3 | 3 |
| schedule_risk (0.08) | 2 | 4 | 3 | 2 |
| **Weighted score** | **3.45** | **4.29** | **3.34** | **2.58** |
| **Rank** | 2 | **1** | 3 | 4 |

Worked example (OPT2): 0.20·5 + 0.15·4 + 0.10·4 + 0.10·4 + 0.08·3 +
0.10·5 + 0.12·4 + 0.07·5 + 0.08·4 = 1.00 + 0.60 + 0.40 + 0.40 + 0.24 +
0.50 + 0.48 + 0.35 + 0.32 = **4.29**.

### 2.4 Uncertainty

Cell scores are ordinal expert judgments grounded in cited evidence, with
a realistic uncertainty of ±1 point per cell. Propagating ±1 independent
per-cell uncertainty through the weights gives a 1σ weighted-score
uncertainty of √(Σwᵢ²) ≈ **±0.35**, and ≈ ±0.50 for the *difference*
between two options. Consequences:

- **OPT2's margin over OPT1 (0.84) is robust** (~1.7× the difference
  uncertainty). The #1 rank is stable.
- **The OPT1-vs-OPT3 gap (0.11) is a statistical tie.** The ordering of
  ranks 2 and 3 should not be treated as meaningful; what is meaningful is
  that both trail OPT2 by ≥0.8.
- OPT4's last place is robust (gap ≥ 0.76 to every other option).

### 2.5 Sensitivity to plausible weight changes

Two deliberately adversarial re-weightings:

**W_B — advisor-device-centric** (advisor_group_fit 0.30, publishability
0.15, novelty 0.15, evidence 0.10, schedule 0.10, cleanroom 0.05,
experimental 0.05, software 0.05, startup 0.05): OPT1 = 3.75, **OPT2 =
4.20**, OPT3 = 2.90, OPT4 = 3.15. OPT2 stays #1 even when the weighting is
tilted toward the axis where OPT1/OPT4 are strongest; OPT4 climbs to #3
but never becomes competitive.

**W_C — graduation-speed-maximal** (publishability 0.30, schedule 0.15,
cleanroom 0.10, experimental 0.10, novelty 0.10, evidence 0.10, software
0.05, advisor 0.05, startup 0.05): OPT1 = 3.30, **OPT2 = 4.30**, OPT3 =
3.35, OPT4 = 2.30. OPT2 stays #1; OPT3 and OPT1 swap within the noise
band — consistent with §2.4's tie finding and with OPT3's role as the
schedule-driven fallback.

**Conclusion:** the OPT2 recommendation survives every plausible
re-weighting tried; only the #2/#3 ordering is weight-sensitive. For OPT2
to lose #1 under the baseline weights, its publishability and novelty
scores would both have to fall by ~2 points each — the falsifiers that
would cause exactly that are named in §11.

---

## 3. The options and the strongest defensible thesis for each

### 3.1 OPT1 — Strengthened continuation (finished calibrated instrument, projects 02+03 as planned)

**Thesis:** *"The first absolutely calibrated multi-axis GaN Hall-effect
probe operated inside a stellarator, with in-vessel spinning-current
offset suppression and vector output validated against the computed
vacuum field"* — project 03's own thesis statement (claim C020), executed
as written on the Aug/Nov 2026 campaign schedule.

**Why it is defensible:** it follows the exact validation paradigm the
field already accepts — CTH's GaAs Hall array validated against
Biot–Savart vacuum-field predictions in a non-axisymmetric device
[S0143](https://doi.org/10.1063/1.4894209) — and lands in the genre (RSI
deployment+calibration+validation) where the ledger shows this work lives
([S0154](https://doi.org/10.1063/5.0002193), [S0226], and RSI as the
ledger's most frequent venue, 29/231 rows).

**Why it is not the adopted framing:** every headline output is
campaign-coupled. The Nov 2026 machine time is, in project 03's own words,
"the immovable object"; bond yield on cube faces is its own top risk; and
the single-axis calibration that everything downstream assumes is still
blocked by the open ~109× anomaly (C017). Scored honestly, its
experimental burden (2) and schedule risk (2) are the worst of the three
viable options. Decision: **fold into OPT2** — everything in OPT1 survives
as OPT2's hardware spine; what changes is that the thesis and the paper
portfolio no longer stand or fall with the campaign calendar.

### 3.2 OPT2 — Adjusted continuation (calibrated output + system/software novelty layer) — ADOPTED

**Thesis:** *"Absolutely calibrated GaN Hall-effect magnetic sensing in
the HSX stellarator, and a drift-corrected hybrid measurement architecture
that fuses direct (Hall) and inductive (pickup-coil) sensing — upgrading
the 2025 uncalibrated single-axis demonstration into a traceable,
uncertainty-quantified, vector-capable diagnostic and quantifying what
direct sensing adds to a stellarator's existing magnetics."*

Concretely, OPT2 = OPT1's hardware spine plus four campaign-uncoupled work
packages, each answering a specific decline-letter item and each carrying
its own citable methodological precedent:

| Work package | Answers | Precedent / template | Campaign-dependent? |
|---|---|---|---|
| WP-A: GaN-vs-competitor comparison table | AEIC request (C010) | Assemblable from ledger rows; no published review contains it — [S0065](https://doi.org/10.1088/2631-8695/ac0838) has no GaN row | No |
| WP-B: multi-die repeatability statistics (bench) | AEIC "only one module was tested" (C007/C010) | On-chip Hall-cell statistics [S0218](https://doi.org/10.3390/jsan2010085); JET's 18-sensor stability bar [S0068] | No |
| WP-C: absolute bench calibration + GUM/MC uncertainty budget | Reviewer 1 key point; AEIC minimum (C009/C010) | Traceable Hall calibration with written budget [S0051](https://doi.org/10.5194/jsss-9-391-2020); GUM/Monte-Carlo [S0220](https://doi.org/10.3390/s25051633); Allan-variance drift decomposition [S0168](https://doi.org/10.1109/TIM.2007.908635) | No |
| WP-D: hybrid Hall+inductive drift-corrected fusion on HSX data | The direction's core physics case | Kalman coil+Hall fusion at KSTAR [S0118](https://doi.org/10.1088/1741-4326/adb599); COMPASS-U/JET lineage [S0122](https://doi.org/10.1016/j.fusengdes.2025.115180); non-fusion hybrid precedents [S0179](https://doi.org/10.3390/s22010182), [S0180](https://doi.org/10.3390/s19245455) | Partly (needs co-located coil data; existing 2025 data may partially serve) |

**Why this wins:** it is the only option that (a) closes every
decline-letter item, (b) puts claimed novelty at the granularity the
literature will defend (first GaN/WBG Hall in-vessel; first Hall of any
kind in a QHS stellarator; first quantified Hall-vs-inductive
complementarity study on a stellarator), (c) shifts a large fraction of
thesis work into software/analysis where the user wants it and where slip
risk is lowest, and (d) preserves every OPT1 deliverable as upside rather
than as a single point of failure.

### 3.3 OPT3 — Genuine change of direction: software-only stellarator-magnetics methods

**Thesis (strongest honest version):** *"Physics-informed
machine-learning reconstruction of stellarator magnetic equilibria from
sparse magnetics, developed and benchmarked on HSX"* — riding the
established method lineage: magnetics-only deep equilibrium solvers at
KSTAR [S0181](https://doi.org/10.1088/1741-4326/ab555f), stellarator-class
PINN/NN precedents at W7-X
[S0189](https://doi.org/10.1088/1741-4326/acc852),
[S0193](https://doi.org/10.1088/1741-4326/aab22d),
[S0194](https://doi.org/10.1088/1741-4326/ae2937),
[S0192](https://doi.org/10.1063/5.0188634), and the V3FIT reconstruction
context HSX already uses
[S0132](https://doi.org/10.1088/0029-5515/55/11/113012). Digital-twin
reviews name sensor-integrated component-level twins as an open fusion gap
[S0196](https://doi.org/10.1109/ACCESS.2025.3561920),
[S0203](https://doi.org/10.1088/1741-4326/add16e).

**Why it loses now:** (a) the KSTAR-class precedent trained on 1,118
discharges [S0181]; no comparable HSX discharge-magnetics database was
found, and its existence is NOT ESTABLISHED FROM SUPPLIED FILES — the
option's first months would be spent discovering whether it is feasible at
all; (b) advisor-group fit is the weakest of any option — the Senesky
group's identity and co-authorship record are WBG devices
([S0004]–[S0012]), not plasma-physics ML, so both supervision depth and
committee framing become risks; (c) it abandons the demonstrated in-vessel
asset and restarts reputation-building from zero with ~24 months left; (d)
its novelty is "first application of an established method to HSX" — real
but incremental in a crowded ML-fusion field. Decision: **hold as
fallback** — it is the named landing zone if the hardware premises fail
(§8, §11), and OPT2's WP-D deliberately builds the data pipelines and
UW relationships that would make the landing survivable.

### 3.4 OPT4 — Device-novelty escalation (considered and rejected)

The remaining pole of the option space: answer Reviewer 2 head-on with new
device topologies (three-terminal current-sensing GaN
[S0010](https://doi.org/10.1109/ACCESS.2025.3539435), AlN/GaN extreme-range
devices [S0012]) and a formal fusion-qualification program toward the
ITER/JET bar ([S0114], [S0068]). Rejected because: it maximizes cleanroom
burden against an explicit user constraint; qualification programs are
multi-year at institutional scale (ITER's OVSS campaign sat "at the limit
of technical feasibility" [S0148](https://doi.org/10.1016/j.fusengdes.2021.112398));
its device-letter genre is exactly where the novelty attack succeeded; and
the mission scope forbids the radiation experiments such a program would
eventually demand. It is scored to show the boundary was examined, not as
a live candidate.

---

## 4. What is demonstrated, what requires analysis, what requires new experiment

**Already demonstrated (supplied facts, with claim IDs):**

- In-vessel deployment and survival of a packaged AlGaN/GaN Hall sensor in
  HSX across the Aug-2025 campaign, with shot-resolved transient response
  (C001, C002; raw data in `../../07_HSX_august2025_results/`).
- Temporal correlation of sensor output with the diamagnetic loop
  (manuscript Figs. 4–5; C001–C005).
- Readout chain: 200 V/V gain (C004); the 1 MHz bandwidth figure is
  asserted, reviewer-questioned, and has no derivation (C003).
- Four-phase spinning-current offset cancellation ≥130× — **on a
  resistor-ring emulator only** (C016), with the ~109× magnitude anomaly
  open (C017). No calibration coefficient, V_off value, or absolute-field
  result exists for the real sensor (C005, C013, conflict C6).

**Requires analysis only (no new hardware, no campaign):**

- WP-A comparison table — assembled from ledger rows ([S0006],
  [S0009](https://doi.org/10.1109/ises54909.2022.00071),
  [S0011](https://doi.org/10.1109/JSEN.2024.3507799),
  [S0014](https://doi.org/10.1109/JSEN.2014.2368074),
  [S0016](https://doi.org/10.1088/1361-6501/ac12fe),
  [S0017](https://doi.org/10.1063/1.2201339); metadata-only rows
  re-confirmed against primary PDFs first, per the Stage 10D gate).
- Bandwidth derivation for the existing chain (C003) — analysis plus at
  most a bench frequency sweep; norm: [S0076](https://doi.org/10.1063/1.3246785).
- Re-analysis of the 68-shot 2025 dataset in field units *once* WP-C
  yields a calibration (Fig. 5 conversion the AEIC requested).
- WP-D algorithm development against synthetic/emulator data and any
  already-recorded HSX coil signals (availability of co-located records is
  an Unresolved gate — UW ask, §10).

**Requires new experiment (bench, no campaign):**

- Resolution of the ~109× anomaly (ΔV gain check — already project 02's
  named top priority; a Proposed experiment inherited, not invented here).
- WP-C: Helmholtz calibration of the real GaN die; temperature
  coefficient; overnight drift; Allan-variance characterization.
- WP-B: raw-offset and sensitivity statistics across ≥3 packaged dies
  (project 02's static-bias mode is the ready tool; die count is an
  advisor question, §10).

**Requires HSX campaign (upside, not single-point-of-failure):**

- In-situ absolute anchor vs computed vacuum field (coil-only shots) —
  the [S0143] paradigm; campaign #1 (Aug 2026) target.
- Co-located Hall vs B-dot/pickup comparison (Reviewer 1's alternative
  ask, C009) and WP-D's in-vessel validation.
- Vector-probe deployment and component-resolved dynamics (campaign #2) —
  the OPT1/RSI centerpiece, per
  [`../../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md`](../../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md).

---

## 5. Novelty versus prior art

**The defensible claims (each bounded by named prior art):**

1. *First GaN/AlGaN (WBG 2DEG) Hall sensor operated in-vessel in any
   magnetic-confinement device* — absence finding, three independent
   lanes; bounded by the mature non-GaN fusion Hall lineage: CASTOR
   [S0070](https://doi.org/10.1007/s10582-006-0185-4),
   [S0117](https://doi.org/10.1063/1.2971209), EAST
   [S0069](https://doi.org/10.1016/j.fusengdes.2008.07.045), JET InSb
   [S0068], ITER bismuth [S0113]–[S0115](https://doi.org/10.1063/1.5038812),
   DEMO-oriented Sb/Cr [S0112](https://doi.org/10.1088/1361-6587/ae6c59),
   [S0153](https://doi.org/10.3390/s21030721), gold-film
   [S0066](https://doi.org/10.1088/1741-4326/aa7867). The claim "first
   fusion Hall diagnostic" is **false** and must never appear.
2. *First Hall sensor of any kind in a quasi-helically symmetric
   stellarator* — HSX facility wording must match
   [S0128](https://doi.org/10.1088/1361-6587/adb179) exactly ("first and
   only stellarator experiment optimized for quasi-helical symmetry");
   exact QHS is impossible in principle
   [S0124](https://doi.org/10.1063/1.859916).
3. *The why-GaN argument as outlook, not achievement:* temperature-stable
   current-scaled sensitivity beyond the ~150 °C class limit of InSb
   ([S0006], [S0012] vs [S0117], [S0153]) and WBG radiation-physics
   headroom ([S0002](https://doi.org/10.1109/TMAG.2012.2196986),
   [S0054](https://doi.org/10.1149/2.0251602jss)) — cited as
   complementary/outlook only; radiation is the co-authored TCAD paper's
   territory and appears in Tim's first-author work as at most a sentence.
4. *Architecture-granularity novelty (OPT2's addition):* a quantified
   direct-vs-inductive complementarity study and drift-corrected fusion on
   a stellarator — the fusion precedents are tokamak-side ([S0118],
   [S0122]); no stellarator counterpart was found; no HSX Hall-sensor,
   calibration, or probe-comparison literature exists at all
   ([S0132] is the nearest HSX magnetics anchor).
5. *What is expressly not novel and must be cited as prior art:*
   spinning-current and offset physics ([S0033],
   [S0039](https://doi.org/10.3390/s22166069),
   [S0041](https://doi.org/10.1109/ICSENS.2004.1426372)); GaN Hall device
   characterization ([S0004]–[S0017], the advisor lineage); Hall-array
   validation against a field model ([S0143],
   [S0217](https://doi.org/10.3390/s18020578)).

**Epistemic status:** claims 1–2 rest on an absence finding from a bounded
231-source search reached independently by three lanes. That is as strong
as literature search can make it, and it is still not proof of priority —
the reversal condition is in §11.

---

## 6. Minimum viable paper sequence within 24 months (Aug 2026 → Jul 2028)

*Recommendation; venue-route arithmetic (revise-SENSL vs arXiv+RSI, and
the IP-screen-before-preprint gate) belongs to stages 30 and 50 and is not
decided here.*

- **P1 (months 0–7): the finished-calibration sensor paper.** The 2025
  deployment re-presented with WP-A/B/C closed: comparison table,
  multi-die bench repeatability, absolute calibration with uncertainty
  budget, bandwidth derivation, Fig. 5 in field units. This is precisely
  the decline letter's list (C010) executed to the field's published norms
  ([S0051], [S0218], [S0220], [S0076]) — and it is campaign-independent:
  it survives even if the August campaign slips. Every month P1 slips, the
  zero-accepted-papers risk compounds; P1 is the schedule's anchor.
- **P2 (months 6–18): the architecture/methods paper.** WP-D: hybrid
  Hall+inductive drift-corrected estimation on HSX data, benchmarked
  against the tokamak precedents [S0118]/[S0122], plus the co-located
  comparison if campaign #1 delivered it. Software-heavy; degrades
  gracefully (synthetic + bench + 2025 data floor).
- **P3 (months 12–24): the RSI vector-probe instrument paper** per
  project 03's plan (C019/C020) — campaign-#2-coupled, genre-anchored
  ([S0143], [S0154], [S0226]), the thesis capstone. If campaign #2 slips
  past ~Feb 2027, P3 descopes to the single-axis in-situ anchor plus
  bench-validated vector module (§8).
- Parallel, not first-author-gating: the co-authored TCAD radiation paper
  (C024).

**Minimum viable outcome: P1 + one of {P2, P3} accepted = 2 first-author
papers; target: all three.** A defensible two-paper floor exists entirely
on bench + already-collected data — that is the structural improvement
OPT2 buys over OPT1.

---

## 7. Cleanroom/fabrication plan (existing topologies only)

*Recommendation, honoring the low-cleanroom constraint:*

- **No new device topology anywhere in the plan.** The die is the
  established AlGaN/GaN Hall cross from the group lineage ([S0004]–[S0006]);
  gen-2 differs only in bond-pad size — a packaging-driven layout change,
  not a device innovation (project 03 §2.1: first-order sensitivity
  unchanged).
- Whether gen-2 dies are already fabricated, in-fab, or not started is
  NOT ESTABLISHED FROM SUPPLIED FILES — advisor question #4 (§10). If no
  gen-2 supply exists, WP-B falls back to remaining 2023-generation dies;
  only the cube's vertical-face bond yield loses its mitigation.
- Everything else is assembly-lab, not cleanroom: LCC packaging, wedge
  bonding, EPO-TEK encapsulation, vacuum bake, ceramic cube machining
  (outsourced quote), three hand-assembled copies of the existing
  `hsx_2026_v1` board.
- Explicitly out: new epitaxy, new mask sets beyond the pad change, any
  OPT4-style topology work, any radiation-exposure experiments (mission
  scope; scope statement fixed in project 03).

---

## 8. Stop/pivot gates and the campaign-slip fallback

| Gate | Window | Test | Pass → | Fail → |
|---|---|---|---|---|
| G1: bench-truth gate | now → Sep 2026 | ~109× anomaly (C017) resolved by the ΔV gain check; real-die Helmholtz calibration underway | WP-C proceeds; P1 drafting starts | Readout redesign decision sprint; P1 recast around WP-A/B + bandwidth + field-unit bounds while the chain is fixed |
| G2: campaign #1 | Aug 2026 (slip ⇒ next HSX window) | Single-axis in-vessel operation + coil-only anchor shots obtained | P2/P3 gain their in-situ anchors | **Fallback F1:** P1 unaffected (bench-only by design); in-situ anchor moves to the next window; WP-D proceeds on 2025 + synthetic data |
| G3: vector hardware | Sep–Oct 2026 | ≥3 working channels; cube bond yield; feedthrough pins ≥12 | 3-axis build | 2-axis module (project 03's own honest fallback) — still a publishable vector instrument |
| G4: campaign #2 | Nov 2026 (slip ⇒ ~Feb 2027 limit for P3-as-planned) | Vector probe operated in-vessel; anchor + dynamics + stability shot list | P3 as planned | **Fallback F2:** P3 descopes to single-axis anchored instrument + bench-validated vector module; P2 becomes the second campaign-independent paper |
| G5: direction gate | ~Jul 2027 (month 12) | ≥1 first-author paper accepted or in revision **and** real-die absolute calibration achieved | Continue OPT2 to completion | **Pivot to OPT3** using the data pipelines and UW relationship built by WP-D; thesis reframes around measurement-architecture + reconstruction methods |

The G5 fallback is why OPT3 is scored and held rather than discarded: the
pivot lands on infrastructure OPT2 builds anyway, so its cost is bounded.

---

## 9. Implications for post-PhD startup preparation

*Recommendation only — this is research-strategy framing, not investment,
legal, or immigration advice.*

- OPT2 is the option that graduates Tim with a **complete
  system-competence stack** — device handling, packaged-sensor
  qualification, precision analog readout, calibration/traceability
  methodology, and estimation software — which is the skill shape of an
  instrumentation company founder, and it does so without betting the PhD
  on any single market thesis.
- The durable, ownable assets it produces are the calibration
  infrastructure, firmware, demod/fusion codebase, and qualification
  datasets; harsh-environment magnetometry demand outside fusion
  (industrial, space-adjacent per the AMR flight-qualification lineage
  [S0227]) is documented in the ledger, but evaluating markets is out of
  scope here.
- Sequencing constraint the user's advisor already imposed (supplied
  fact): the IP screen precedes any arXiv posting. Stage 50 owns that
  screen; §5's prior-art density ([S0033]-class offset art, [S0066]–[S0122]
  fusion Hall art) already bounds any protectable scope as narrow —
  plan for thin, specific claims, not platform claims.
- International-student status is treated per MISSION.md as a scheduling
  and career constraint (favoring the on-schedule two-paper floor and
  transferable system skills), with no immigration-specific guidance
  offered here.

---

## 10. Exact advisor decisions needed next

1. **Approve the novelty re-centering** (OPT2): the group's own device
   papers ([S0004]–[S0006], [S0012]) are cited as prior art; the claimed
   contribution becomes the finished calibrated application + measurement
   architecture. This is the decision Reviewer 2's report forces either
   way.
2. **Approve WP-D (hybrid Hall+inductive fusion) as thesis scope**,
   including the UW co-authorship shape for the plasma-side content.
3. **Gen-2 die status and count:** are larger-pad dies fabricated/in-fab?
   How many packaged dies can WP-B have for repeatability statistics
   (≥3 needed)?
4. **Authorize the July UW email** (project 03's own list, now
   direction-critical): feedthrough pin count, mount-pose survey,
   vacuum-field computation at the probe pose, shot-list request — plus
   OPT2's addition: **access to co-located pickup-coil/B-dot records**
   for WP-D and confirmation of whether any HSX discharge-magnetics
   archive exists at scale (this simultaneously prices the OPT3 fallback).
5. **Venue-route preference input for stage 30** (revise SENSL-26-07-RL-1061
   under its resubmission invitation vs arXiv+RSI) — decision itself is
   stage 30's, with the stage-50 IP screen gating any preprint.
6. **Confirm the two-year graduation target and committee framing** for a
   device+system+methods thesis, so G5's month-12 gate has an agreed
   meaning.
7. **Correct the parent-project record** (C1): the "2023, published"
   framing in the parent memory files should be fixed by the user — this
   mission cannot write there, and any CV/website/committee document
   repeating it would be contradicted by the supplied IEEE records.

---

## 11. Falsifiability: what would reverse this recommendation

The ADJUST/OPT2 verdict is falsifiable. Named reversal conditions:

1. **Novelty anchor collapse:** discovery of a peer-reviewed GaN/AlGaN
   Hall deployment in any confinement device predating Tim's. Effect:
   claims 1–2 of §5 die; P1 reframes as qualification/architecture work
   (the [S0225](https://doi.org/10.1016/j.fusengdes.2023.114115)/[S0226]
   genre still publishes that), and the OPT2-vs-OPT3 margin shrinks to
   inside the uncertainty band — re-run this scorecard.
2. **Device-viability failure:** the real GaN die cannot be absolutely
   calibrated to a stable coefficient (e.g., the anomaly traces to the
   die/packaging, or drift/temperature instability exceeds any honest
   budget) by G5. Effect: the "finished calibrated output" premise fails;
   OPT2's publishability score drops ~2 points; pivot to OPT3 per G5.
3. **Access failure:** HSX access is lost entirely (both campaigns and
   data access). Effect: in-vessel premise fails; OPT3 (on whatever HSX
   archive exists, or public-device data) becomes the rational thesis.
4. **Fit failure:** the advisor declines WP-D/system scope (decision #2).
   Effect: revert to OPT1 as scored (rank 2, viable but
   schedule-concentrated) — a legitimate advisor call, and the scorecard
   already prices it.
5. **Precedent surprise on WP-D:** a stellarator Hall+coil fusion study
   surfaces in the literature. Effect: WP-D loses "first," retains
   HSX-specific value; P2 reframes as comparative/validation work; OPT2
   remains ahead on the remaining margin but the novelty score is re-run.

None of these has occurred on current evidence; each names the observation
that would change the verdict, which is what makes the verdict a decision
rather than a preference.

---

## 12. What this stage deliberately did not decide

- The manuscript/venue route (revise vs arXiv+RSI) and reviewer-response
  strategy → stage `30_manuscript` (which must also align the facility
  claim to [S0128]'s exact wording).
- The experiment/statistics design details, shot budgets, and the sizing
  of any HSX data archive → stage `40_experiment`.
- The IP/prior-art screen → stage `50_patent`.
- Month-by-month scheduling → stage `60_timeline` (P1–P3 windows above
  are direction-level constraints, not the timeline).
