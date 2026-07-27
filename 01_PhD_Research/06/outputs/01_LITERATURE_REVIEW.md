# 01 — Integrated literature review (Stage 10D)

**Basis:** the 231-source verified ledger
[`outputs/01_SOURCE_LEDGER.csv`](01_SOURCE_LEDGER.csv) (S0001–S0231), merged
and deduplicated from the three Stage 10A/10B/10C lanes and re-verified at
this stage (32 DOIs, ~14% of the ledger, independently re-checked against
Crossref by this session with a 32/32 match rate). Citations below use
`[S####]` with a stable `https://doi.org/...` link on first use. Supplied
project facts cite the source file, not a ledger ID, per `SOURCE_POLICY.md`.

**Epistemic labels used throughout:** *Supplied fact* (from the mission's
input files), *External evidence* (peer-reviewed ledger sources), *Inference*
(this session's reasoning from evidence), *Recommendation* (proposed action
for a later stage to accept or reject), *Gap* (not established by any
supplied file or ledger source). This stage does **not** make the
continue/adjust/change direction decision; that is stage `20_direction`.

**Access-level caveat (applies to every numeric claim below):** 75 of 231
rows are `metadata_only` and 133 are `abstract_metadata`; only 23 are
`full_text`. Numbers quoted from non-`full_text` rows come from abstracts or
publisher records, not an independently read methods section, and are marked
in the ledger row's own `access_level`. See
[`01_SOURCE_COVERAGE.md`](01_SOURCE_COVERAGE.md) §7.

---

## 1. The question this review serves

*Supplied fact.* Tim's submitted IEEE Sensors Letters manuscript
(`SENSL-26-07-RL-1061`, submitted 2-Jul-2026) reported an AlGaN/GaN
Hall-effect sensor deployed in-vessel in HSX across 68 plasma shots,
voltage-biased and uncalibrated (V_off unknown), demonstrating real-time
plasma tracking by temporal correlation with HSX's diamagnetic loop
(`../01_Publications/submitted/regular_lsens/regular_lsens.tex`). It was
declined on 23-Jul-2026 with an invitation to revise and resubmit
(`inputs/Decision_Letter_IEEE_2026-07-23.pdf`). The Associate Editor's
primary concern was novelty; the requested items were a GaN-sensor
performance comparison table, repeatability statistics across fabrication
iterations, bench-top calibration at minimum, and field-unit (not voltage)
presentation of the key figure. Reviewer 1 called the device "novel and
unique to my knowledge" and worth publishing with added calibration or a
conventional-probe comparison; Reviewer 2 judged novelty insufficient,
citing prior GaN Hall-device literature (Stage 00 claim baseline
C005–C011). The mission questions this review must inform are: is the
underlying direction publishable and strategically strong (MISSION.md Q2);
which low-fabrication novelty paths does the literature support (Q3); what
does the literature imply about the reviewer criticisms and venue routes
(Q4–Q5); and which experiment/analysis gaps must close (Q6).

---

## 2. What the GaN/WBG Hall-sensor literature establishes (mission Q1, Q2, Q4)

### 2.1 GaN Hall sensing is an established device-physics field — but a small one, centered on the advisor's own lineage

*External evidence.* AlGaN/GaN 2DEG Hall sensors have a 20-year
characterization literature: high-temperature operation to 400–576 °C with
current-scaled sensitivities of roughly 55–95 V/A/T
([S0001](https://doi.org/10.1088/1742-6596/352/1/012009),
[S0006](https://doi.org/10.1063/1.5139911),
[S0016](https://doi.org/10.1088/1361-6501/ac12fe),
[S0017](https://doi.org/10.1063/1.2201339)), proton-irradiation tolerance at
the device level ([S0002](https://doi.org/10.1109/TMAG.2012.2196986)),
geometry-driven sensitivity/offset trade-offs
([S0004](https://doi.org/10.1109/JSEN.2019.2895546)), micro-tesla residual
offset via four-phase current spinning
([S0005](https://doi.org/10.1109/LSENS.2019.2898157)), and, most recently,
dual-channel AlN/GaN devices for −193 to 407 °C
([S0012](https://doi.org/10.1063/5.0305414)) and a first three-terminal
GaN current-sensing Hall device
([S0010](https://doi.org/10.1109/ACCESS.2025.3539435)). Four of the
central rows — [S0004], [S0005], [S0006], [S0012] — are co-authored by
D. G. Senesky, Tim's own advisor.

*Inference.* Two consequences follow. First, Reviewer 2's objection that
GaN Hall-device characterization is not new is **well supported**: geometry,
offset, spinning-current cancellation, and temperature behavior are already
published for this exact material system, several times from the same lab.
Second, the field is small enough that the *deployment context* — not the
device — is where unclaimed territory lies (§3.3). A revision that implies
device-level novelty would be contradicted by the advisor group's own
published record; a revision that cites that record and claims the
application is the contribution would be aligned with it.

### 2.2 GaN's honest competitive position among Hall materials

*External evidence.* GaN is **not** the most sensitive Hall material:
GaAs-based 2DEG platforms reach ~500–4300 V/A/T and nanotesla-class
detection ([S0009](https://doi.org/10.1109/ises54909.2022.00071),
[S0014](https://doi.org/10.1109/JSEN.2014.2368074)), and InAs/AlSb 2DEGs
achieve ~570 V/A/T with 0.25 µT/√Hz noise floors
([S0011](https://doi.org/10.1109/JSEN.2024.3507799)). GaN's defensible
advantages are (a) temperature stability of the current-scaled sensitivity
(~10–13% variation from room temperature to 576 °C, versus GaAs degrading
~40% over a narrower range) ([S0006], [S0009]), (b) low temperature
cross-sensitivity (103 ppm/°C to 300 °C, [S0017]; <745 ppm/K, [S0016]),
and (c) membership in the wide-bandgap harsh-environment device family with
its own radiation-physics literature
([S0054](https://doi.org/10.1149/2.0251602jss),
[S0055](https://doi.org/10.1039/C2TC00039C),
[S0058](https://doi.org/10.3390/ma17051147),
[S0060](https://doi.org/10.1038/s41928-026-01570-y),
[S0062](https://doi.org/10.1109/JSEN.2009.2026996)). No published review
provides a unified GaN-vs-Si-vs-GaAs-vs-InSb comparison table across
sensitivity/offset/noise/temperature — the closest general review
([S0065](https://doi.org/10.1088/2631-8695/ac0838)) has no GaN row.

*Inference.* The AEIC's requested comparison table cannot be lifted from any
single source; it must be assembled from the ledger rows above. That is
work the literature has left undone — a small but real contribution a
revision could legitimately claim. The table should sell temperature-stable
current-scaled sensitivity and harsh-environment headroom, not raw
sensitivity, or it will lose on its own numbers.

### 2.3 Offset and calibration: the technique shelf is deep, and none of it is novel per se

*External evidence.* Spinning-current offset cancellation dates to 1990
([S0033](https://doi.org/10.1016/0924-4247%2889%2980069-X),
[S0034](https://doi.org/10.1016/0924-4247%2891%2987081-D)) with mature variants
(continuous spinning [S0035](https://doi.org/10.1016/S0924-4247%2898%2900003-X);
dynamic quadrature cancellation
[S0038](https://doi.org/10.1109/4.585275); randomized spinning preserving
2 MS/s bandwidth [S0039](https://doi.org/10.3390/s22166069); CMOS
microsystems [S0037](https://doi.org/10.1109/4.982421)), known theoretical
residual-offset limits (~100 nT from plate nonlinearity,
[S0041](https://doi.org/10.1109/ICSENS.2004.1426372); analytical modeling
and eighth-phase suppression
[S0174](https://doi.org/10.1109/JSEN.2020.2997292)), known
mechanical-stress/packaging offset mechanisms
([S0022](https://doi.org/10.1063/1.115110),
[S0023](https://doi.org/10.1109/jsen.2007.907039),
[S0042](https://doi.org/10.1109/84.809062),
[S0050](https://doi.org/10.1109/JSEN.2013.2264805)), and canonical
chopper/autozero/lock-in theory
([S0176](https://doi.org/10.1109/5.542410),
[S0177](https://doi.org/10.1119/1.17629)). Traceable Hall-probe calibration
methodology with a written uncertainty budget exists as a template
([S0051](https://doi.org/10.5194/jsss-9-391-2020)), as do
metrology-institute traceability routes
([S0219](https://doi.org/10.21014/actaimeko.v13i4.1762)) and formal
GUM/Monte-Carlo uncertainty evaluation
([S0220](https://doi.org/10.3390/s25051633)).

*Inference.* Project 02's current-spinning readout closes a *gap in Tim's
own device's characterization*, not a gap in the field. As a novelty claim,
"we calibrated a Hall sensor with current spinning" is refuted by this
shelf; as an enabling step for an in-stellarator absolute measurement, it is
exactly what the fusion literature says is required (§3.2). The framing
difference is decisive, and Reviewer 2's decline rationale is the
literature's own verdict on the wrong framing.

---

## 3. What the fusion magnetic-diagnostics literature establishes (mission Q1, Q2, Q6)

### 3.1 The incumbent diagnostics and their one structural weakness

*External evidence.* Inductive sensing — Mirnov/pickup coils, flux loops,
diamagnetic loops, Rogowski coils — is the backbone of magnetic diagnosis on
every major device ([S0071](https://doi.org/10.1007/BF01788387),
[S0093](https://doi.org/10.1063/1.2166493),
[S0108](https://doi.org/10.13182/fst08-a1674),
[S0131](https://doi.org/10.1016/j.fusengdes.2015.07.020)). Its structural
weakness is that it measures dB/dt and must be integrated: every long-pulse
machine has published dedicated engineering to fight integrator drift —
W7-X ([S0099](https://doi.org/10.1063/1.2220073),
[S0100](https://doi.org/10.1063/1.2957933)), KSTAR
([S0105](https://doi.org/10.1063/1.1789620),
[S0106](https://doi.org/10.1063/1.3519303)), EAST
([S0098](https://doi.org/10.1063/1.3131627),
[S0103](https://doi.org/10.1016/j.fusengdes.2014.02.019),
[S0104](https://doi.org/10.1016/j.fusengdes.2021.112255) — <8 mV drift per
1000 s bench, compensated operation to a 1284 s discharge), HL-2A
([S0107](https://doi.org/10.1063/1.4940027)), WEST
([S0084](https://doi.org/10.1016/j.fusengdes.2015.06.047)). Diamagnetic
loops carry their own error terms (wall/eddy currents distorting transients
by >10% in fast events, [S0091](https://doi.org/10.1016/j.fusengdes.2018.11.001);
compensation-coil engineering,
[S0086](https://doi.org/10.1088/1741-4326/aacab0),
[S0092](https://doi.org/10.1063/1.1614856),
[S0096](https://doi.org/10.1063/1.4816842)). Radiation adds
cable-level spurious EMFs (RITES) as a recognized reactor-era drift
mechanism ([S0109](https://doi.org/10.1016/j.jnucmat.2004.04.252),
[S0157](https://doi.org/10.1016/j.fusengdes.2022.113122)).

### 3.2 Direct (Hall) sensing in fusion devices: a real, mature, entirely non-GaN lineage

*External evidence.* Hall probes are an established fusion answer to the
DC/steady-state gap: CASTOR used in-vessel Hall probes for safety-factor
measurement in 2006 ([S0070](https://doi.org/10.1007/s10582-006-0185-4))
and an 8-sensor in-vessel array in 2008
([S0117](https://doi.org/10.1063/1.2971209)); EAST measured toroidal field
with in-vessel Hall probes
([S0069](https://doi.org/10.1016/j.fusengdes.2008.07.045)); JET has run
InSb Hall probes for 11+ years and >19,000 pulses with ±0.07% calibration
stability ([S0068](https://doi.org/10.1088/1741-4326/ac8aad) — found
independently by all three search lanes, the most load-bearing precedent in
this ledger); ITER's steady-state magnetic diagnostic is a 60-unit
*bismuth* Hall-sensor array with a completed final design and high-field
qualification ([S0113](https://doi.org/10.1063/1.4732077),
[S0114](https://doi.org/10.1063/1.5038871),
[S0115](https://doi.org/10.1063/1.5038812),
[S0149](https://doi.org/10.1016/j.fusengdes.2017.03.043),
[S0120](https://doi.org/10.1016/j.fusengdes.2017.05.142)); the
DEMO-oriented material path runs through antimony and chromium with
quantified neutron-fluence tolerance
([S0112](https://doi.org/10.1088/1361-6587/ae6c59) — 2.3% sensitivity shift
at 1.4×10²⁰ cm⁻² fast-neutron fluence;
[S0119](https://doi.org/10.1016/j.fusengdes.2023.113476),
[S0153](https://doi.org/10.3390/s21030721),
[S0067](https://doi.org/10.1016/j.fusengdes.2019.01.013)), plus metal
(gold-film) sensors tolerant to 10²⁴ n/m²
([S0066](https://doi.org/10.1088/1741-4326/aa7867)). The field's own
architecture answer to combining bandwidth and DC accuracy is hybrid
coil+Hall sensor fusion via Kalman filtering, demonstrated at KSTAR
([S0118](https://doi.org/10.1088/1741-4326/adb599)) and in the
COMPASS-U/JET lineage ([S0122](https://doi.org/10.1016/j.fusengdes.2025.115180)).

The closest methodological precedent to Tim's project is the Compact
Toroidal Hybrid: a 16-element **GaAs** Hall-sensor array measuring internal
poloidal field in a non-axisymmetric device, calibrated in-situ and
validated against Biot-Savart vacuum-field predictions for use in 3D
equilibrium reconstruction ([S0143](https://doi.org/10.1063/1.4894209)).
A Hall sensor has also captured pulsed fields in an FRC merging experiment
([S0173](https://doi.org/10.1063/1.5039356)).

*External evidence (absence finding).* Across all three lanes — the
GaN-focused lane, the fusion-diagnostics lane, and the methods lane — **no
peer-reviewed paper was found reporting a GaN or AlGaN Hall sensor deployed
inside any tokamak or stellarator.** The forward-looking DEMO
materials-outlook review considers bismuth, antimony, and graphene — not GaN
([S0121](https://doi.org/10.1016/j.fusengdes.2019.03.201)).

*Inference.* This is an absence-of-evidence result from a bounded search,
not proof of global priority; but it was reached independently three times
with different query families, which is as strong as a literature search can
make it. The novelty claim the evidence supports is narrow and specific:
*first GaN/AlGaN (wide-bandgap semiconductor 2DEG) Hall sensor operated
in-vessel in a magnetic-confinement device, and first Hall sensor of any
kind in a quasi-helically symmetric stellarator.* The claim it does **not**
support is "first Hall-effect magnetic diagnostic in fusion" — that is
20 years old and institutionally mature at ITER scale. Reviewer 1's
"novel and unique" and Reviewer 2's "not novel" are therefore *both*
literature-consistent, at different claim granularities; the manuscript's
survival depends on pinning its claim at the granularity the evidence
supports.

### 3.3 What a GaN entrant must answer

*Inference from §2–§3 evidence.* Against this lineage, a GaN deployment
paper must answer "why GaN, when InSb/bismuth/antimony are already
qualified?" The literature-supported answers are: temperature-stable
sensitivity far beyond InSb's ~150 °C class limit
([S0006], [S0012], [S0153] notes semiconductor limit;
[S0117] qualified only below 150 °C), WBG radiation-physics headroom
([S0054], [S0002]), and CMOS/HEMT-technology integration potential
([S0010], [S0060]). None of these is yet demonstrated *as a fusion
qualification result* for GaN — that is precisely the outlook argument, and
it must be labeled as outlook, not achievement (the mission scope forbids
claiming radiation results experimentally; Tim's radiation content is
limited to the co-authored TCAD simulation paper).

---

## 4. Stellarator/HSX-specific context (mission Q1, Q4, Q6)

*External evidence.* Quasi-helical symmetry was proposed computationally in
1988 ([S0123](https://doi.org/10.1016/0375-9601%2888%2990080-1)), shown to be
realizable only approximately
([S0124](https://doi.org/10.1063/1.859916)), and reviewed by Boozer
([S0125](https://doi.org/10.1088/0741-3335/37/11a/007)). The HSX design
paper calls the device "unique," not "first"
([S0126](https://doi.org/10.13182/fst95-a11947086),
[S0127](https://doi.org/10.1109/27.763074)). The citable modern wording is
Garcia et al. 2025: "HSX is the first and only stellarator experiment
optimized for quasi-helical symmetry"
([S0128](https://doi.org/10.1088/1361-6587/adb179)).

HSX's existing magnetic suite is documented in one central paper: a 10-turn
in-vessel diamagnetic loop, Rogowski coils, and pickup-coil belts feeding
V3FIT 3D equilibrium reconstruction, where an optimized 80-coil set reduced
the space of acceptable reconstructed equilibria roughly 7-fold
([S0132](https://doi.org/10.1088/0029-5515/55/11/113012)). V3FIT itself is
validated stellarator-class reconstruction machinery
([S0188](https://doi.org/10.1088/0029-5515/49/7/075031),
[S0142](https://doi.org/10.1063/1.4938031)). The stellarator field's
validation gold standard is W7-X's electron-beam flux-surface mapping,
confirming field topology to 1:100,000
([S0137](https://doi.org/10.1038/ncomms13493),
[S0138](https://doi.org/10.1088/0029-5515/56/10/106005),
[S0139](https://doi.org/10.1088/0741-3335/58/6/064003)), with W7-X's
125-coil in-vessel Mirnov system and stellarator Mirnov-array synthetic
diagnostics defining the array-based state of the art
([S0075](https://doi.org/10.1088/1361-6587/abc395),
[S0073](https://doi.org/10.1063/5.0190619),
[S0074](https://doi.org/10.1063/5.0244636)). A 2025 permanent-magnet
stellarator reduced resonant error fields to ~3×10⁻⁶ of the toroidal field
([S0145](https://doi.org/10.1088/1361-6587/ae1870)).

*Inference.* (a) The manuscript's "first quasi-helically symmetric
stellarator" phrasing should be corrected to match [S0128]'s exact wording —
an easily checked overclaim otherwise, and [S0124] shows exact QHS is
impossible in principle. (b) No HSX-specific Hall-sensor, calibration,
uncertainty, or conventional-probe-comparison literature exists: the HSX
literature gap and the GaN literature gap coincide at exactly Tim's project.
(c) The stellarator community's own validation norm — measurement vs.
computed vacuum field — is the same paradigm the CTH GaAs Hall precedent
[S0143] used, giving stage `40_experiment` a directly citable template.

---

## 5. Low-fabrication novelty paths (mission Q3)

*External evidence, organized by method class; each is established elsewhere
and unapplied on HSX.*

1. **Formal calibration and uncertainty treatment of the existing sensor.**
   Multi-parameter calibration matrices and self-calibration without
   external references ([S0158](https://doi.org/10.1155/2010/967245),
   [S0165](https://doi.org/10.1109/TAES.2011.5751259),
   [S0197](https://doi.org/10.2514/1.6278),
   [S0199](https://doi.org/10.3390/s21165288)); Bayesian calibration
   separating model discrepancy from noise
   ([S0161](https://doi.org/10.1111/1467-9868.00294)); Allan-variance noise/
   drift decomposition ([S0168](https://doi.org/10.1109/TIM.2007.908635));
   GUM/Monte-Carlo budgets ([S0220]); traceability routes ([S0219],
   [S0051]). Fusion-side counterparts: ITER's own OVSS calibration campaign
   (4 mT 2σ target, calibration contributing ~2.5 mT, "at the limit of
   technical feasibility",
   [S0148](https://doi.org/10.1016/j.fusengdes.2021.112398)) and EAST's
   itemized magnetics uncertainty budget
   ([S0152](https://doi.org/10.1016/j.fusengdes.2016.02.051)).
2. **Sensor fusion with HSX's existing diagnostics.** Bayesian integrated
   data analysis, with a stellarator (W7-AS) application that fuses a
   diamagnetic-loop-type signal
   ([S0159](https://doi.org/10.1063/1.1787607),
   [S0160](https://doi.org/10.1063/1.1789611)); Kalman/EKF architectures for
   magnetics ([S0171](https://doi.org/10.1115/1.3662552),
   [S0202](https://doi.org/10.1088/0741-3335/55/10/105003),
   [S0206](https://doi.org/10.1016/j.fusengdes.2025.115363)); and the
   fusion-native coil+Hall drift-fusion precedents ([S0118], [S0122],
   [S0179](https://doi.org/10.3390/s22010182),
   [S0180](https://doi.org/10.3390/s19245455)).
3. **Inverse methods and reconstruction.** Regularized magnetic inversion
   with principled regularization-parameter selection
   ([S0164](https://doi.org/10.1088/0741-3335/50/8/085002),
   [S0166](https://doi.org/10.1109/TMAG.2012.2192287),
   [S0167](https://doi.org/10.1155/2018/7452863)); Bayesian equilibrium
   inference ([S0190](https://doi.org/10.1063/1.3677362)).
4. **ML/physics-informed reconstruction.** Magnetics-only deep equilibrium
   solvers at KSTAR ([S0181](https://doi.org/10.1088/1741-4326/ab555f),
   [S0191](https://doi.org/10.1038/s41598-023-42991-5)), NN surrogates at
   NSTX-U/DIII-D ([S0182](https://doi.org/10.1088/1741-4326/ac77e6),
   [S0195](https://doi.org/10.1088/1741-4326/ad142f),
   [S0198](https://doi.org/10.1017/s0022377825100962)), stellarator-class
   PINN/ANN precedents at W7-X
   ([S0189](https://doi.org/10.1088/1741-4326/acc852),
   [S0193](https://doi.org/10.1088/1741-4326/aab22d),
   [S0194](https://doi.org/10.1088/1741-4326/ae2937),
   [S0192](https://doi.org/10.1063/5.0188634)), RL magnetic control
   ([S0187](https://doi.org/10.1038/s41586-021-04301-9),
   [S0205](https://doi.org/10.1088/1741-4326/ae34c6)), and early NN
   precedents ([S0183](https://doi.org/10.1103/PhysRevLett.75.3594),
   [S0185](https://doi.org/10.1088/0029-5515/34/10/i05),
   [S0186](https://doi.org/10.1162/neco.1995.7.1.206)) against the
   classical rt-EFIT baseline
   ([S0184](https://doi.org/10.1088/0029-5515/38/7/308),
   [S0135](https://doi.org/10.1088/0029-5515/25/11/007),
   [S0136](https://doi.org/10.1088/0029-5515/30/6/006)). **Data
   prerequisite gap:** the KSTAR solver trained on 1,118 discharges
   ([S0181]); no comparable HSX discharge-magnetics database was found —
   stage `40_experiment` must size this rather than assume it.
5. **Vector/array methodology for project 03.** Single-point 3D vector
   Hall sensing ([S0208](https://doi.org/10.1038/s43246-021-00206-2)),
   3-axis integration with offset cancellation
   ([S0032](https://doi.org/10.1038/s41378-025-00876-9),
   [S0027](https://doi.org/10.1016/j.sna.2015.11.022),
   [S0209](https://doi.org/10.3390/s24051659)), model-based array-placement
   optimization (D-optimality)
   ([S0210](https://doi.org/10.1109/TMAG.2009.2027899),
   [S0211](https://doi.org/10.3390/s16060754),
   [S0212](https://doi.org/10.1002/hbm.25586)), multi-point gradient/
   curlometer methods ([S0216](https://doi.org/10.5194/angeo-19-1207-2001),
   [S0213](https://doi.org/10.1109/JSEN.2009.2035711)), Hall-array field
   mapping ([S0214](https://doi.org/10.3390/s24123773),
   [S0215](https://doi.org/10.3390/mi12030299)), and array error analysis
   against a Biot-Savart model
   ([S0217](https://doi.org/10.3390/s18020578)).
6. **Rigor/reproducibility framing.** Device-to-device statistics
   ([S0218](https://doi.org/10.3390/jsan2010085)), the sensor-field
   reproducibility agenda ([S0221](https://doi.org/10.1149/2754-2726/ad9936)),
   qualification-as-contribution precedent in fusion instrumentation
   ([S0222](https://doi.org/10.1063/1.2972024),
   [S0223](https://doi.org/10.1063/5.0218498),
   [S0224](https://doi.org/10.1088/1748-0221/12/07/c07007)).
7. **Application-novelty precedent.** Peer-reviewed venues accept "first
   deployment/qualification of an established sensor in a new
   environment" as the whole contribution: RADCAM's system-integration RSI
   paper ([S0226](https://doi.org/10.1063/5.0095907)), first-flight
   qualification of an AMR magnetometer
   ([S0227](https://doi.org/10.1007/s11214-025-01170-w),
   [S0228](https://doi.org/10.5194/gi-11-375-2022),
   [S0229](https://doi.org/10.3390/s19081850)), explicit "for the first
   time" harsh-environment deployments
   ([S0230](https://doi.org/10.1186/s40517-021-00204-0),
   [S0231](https://doi.org/10.3390/s21123979)), and a bismuth Hall-sensor
   paper titled to one named tokamak
   ([S0225](https://doi.org/10.1016/j.fusengdes.2023.114115)). Digital-twin
   reviews identify sensor-integrated component-level twins as an open gap
   in fusion ([S0196](https://doi.org/10.1109/ACCESS.2025.3561920),
   [S0203](https://doi.org/10.1088/1741-4326/add16e),
   [S0207](https://doi.org/10.1016/j.asoc.2026.115267)).

*Inference.* Paths 1, 2, and 6 need no new fabrication and no new HSX
campaign beyond data already in hand or bench work on existing dies; they
directly answer the decline letter's specific requests (calibration,
repeatability, comparison table). Paths 3–5 are campaign- or
hardware-coupled. Path 7 establishes that the deployment-novelty framing
itself is publishable **if** rigorously documented — which is the standard
the manuscript was judged against and missed (§6).

---

## 6. The field's validation norms versus the manuscript's current state (mission Q4, Q6)

*External evidence — what published fusion-instrumentation work reports:*
itemized uncertainty budgets ([S0152], [S0094](https://doi.org/10.1088/1741-4326/aa86fd));
calibration against an independent standard or model ([S0143], [S0137],
[S0148], [S0115]); accuracy versus a stated requirement ([S0148]: 4 mT 2σ;
[S0144](https://doi.org/10.1088/0029-5515/53/4/043009): ~1 mm position
control); environmental qualification as a program ([S0112], [S0114],
[S0153]); and multi-year/multi-pulse stability ([S0068]: ±0.07% over
19,000 pulses). Bandwidth claims are derived and characterized, not
asserted ([S0076](https://doi.org/10.1063/1.3246785): 10 kHz–50 MHz B-dot
characterization; [S0178](https://doi.org/10.3390/s20102929): 200 kHz
in-vessel digital-integration chain).

*Supplied fact.* The manuscript reports one uncalibrated module, V_off
unknown, a 200 V/V gain chain, an asserted (reviewer-questioned) 1 MHz
bandwidth, and temporal correlation with the diamagnetic loop as its
validation (claim baseline C001–C005; conflict ledger C6 records that
project 02's "calibrated" language is aspirational — bench emulator only,
with an unresolved ~109× magnitude anomaly).

*Inference.* Every element of the decline letter maps onto a published,
citable norm; nothing the reviewers asked for is exotic or
disproportionate. Conversely, the manuscript's demonstrated content
(in-vessel survival, real-time shot-resolved response, correlation with an
independent diagnostic) matches what first-deployment papers in other
fields successfully publish ([S0227], [S0230]) — *when* accompanied by
calibration/uncertainty documentation. The gap is rigor-of-reporting plus
absolute calibration, not concept validity. **Gap register for stage
`40_experiment`:** absolute calibration + V_off (norm: [S0148], [S0051]);
repeatability across dies (norm: [S0218], [S0068]); uncertainty budget
(norm: [S0152], [S0220]); bandwidth derivation (norm: [S0076]);
conventional-probe comparison (norm: [S0143]; AEIC request); field-unit
presentation (trivial once calibration exists); vector-probe placement
justification for project 03 (norm: [S0210], [S0132]).

---

## 7. Venue-route evidence (mission Q5 — evidence only, decision deferred)

*External evidence.* Review of Scientific Instruments is the single most
frequent venue in this ledger (29/231 rows) and routinely publishes exactly
this genre: stellarator in-vessel probe design/characterization
([S0154](https://doi.org/10.1063/5.0002193)), Hall-probe deployments in
confinement devices ([S0143], [S0173]), magnetic-diagnostic systems and
integrators ([S0093], [S0106]), and system-integration-as-contribution
([S0226]). The advisor group has a prior RSI sensor paper
([S0006]). Fusion Engineering and Design and Nuclear Fusion carry the
Hall-sensor qualification lineage ([S0148], [S0068], [S0112]); IEEE
Sensors Letters carries the group's own short-format GaN device letters
([S0005]).

*Inference (not a decision).* The literature shows the project's natural
center of gravity — in-vessel deployment + calibration + validation against
a computed field — is the RSI/FED/NF genre, while the *device-letter* genre
(Sensors Letters) rewards device novelty, which is the axis Reviewer 2
attacked. This is evidence about venue fit, not a recommendation on the
revise-vs-arXiv+RSI route; that comparison, including timing and the
decline letter's resubmission invitation, belongs to stages `20_direction`
and `30_manuscript`. Note on arXiv: preprints are excluded from this
ledger by policy and nothing here evaluates preprint strategy.

---

## 8. Conflicts, disagreements, and unresolved gaps

1. **Reviewer disagreement is real and literature-grounded** (§3.2):
   Reviewer 1's novelty judgment holds at the
   application/material-in-context granularity; Reviewer 2's holds at the
   device-technique granularity. Not a contradiction in the evidence — a
   fork in claim framing.
2. **Publication-status conflict (Stage 00 C1/C2)** stands: the
   parent-project "2023, published" framing is contradicted by the supplied
   2026 submission/decline records. Nothing found in this stage's
   literature search (no DOI, no published record of the manuscript)
   changes that; the manuscript is treated throughout as unpublished.
3. **Metadata disagreements resolved at merge:** Czech-diacritic author
   renderings (Ďuran → "Duran"; Crossref's own "Boshakova"/"Curan"/"Ceran"
   variants) were resolved against Crossref records for S0070, S0120,
   S0121, S0122; volume/issue enrichments applied to S0095, S0112, S0122,
   S0205; the same-DOI duplicate pairs A0068/B0041 and A0070/B0054 were
   merged into S0068 and S0070. Full audit trail in
   [`01_SOURCE_COVERAGE.md`](01_SOURCE_COVERAGE.md) §3.
4. **Open evidence gaps carried forward** (none closable by more
   searching): no GaN Hall sensor in any confinement device (novelty
   anchor; absence finding); no GaN-specific fusion
   radiation/vacuum/thermal qualification; no HSX Hall-sensor/calibration/
   probe-comparison literature; no quantified spatial-coverage benefit for
   a 2–3 axis HSX probe versus existing pickup belts (nearest precedent:
   [S0132]'s 7× ambiguity reduction from 80 added coils); no HSX
   discharge-magnetics database at ML-training scale; no published
   quantitative "success bar" for a first-generation academic Hall sensor
   in a stellarator (nearest bars are ITER/JET-grade: [S0148], [S0068]).
5. **What is NOT ESTABLISHED FROM SUPPLIED FILES:** any calibration
   coefficient, V_off value, or absolute-field result for Tim's sensor
   (project 02's bench anomaly is unresolved); the exact-figure
   reproduction of the manuscript's shots (Stage 00 checked file presence
   only); any HSX August-2026 campaign schedule commitment.

---

## 9. Summary against the mission questions

| Mission question | What this review establishes | Status |
|---|---|---|
| Q1 (150+ paper review) | 231 verified peer-reviewed sources across all seven required categories | Done at this stage |
| Q2 (direction publishable/strong?) | Novelty is real but only at a specific claim granularity (first GaN/WBG Hall in-vessel in a confinement device; first Hall sensor in a QHS stellarator); the enabling-rigor gaps are exactly the field's published norms | Evidence assembled; **decision deferred to `20_direction`** |
| Q3 (low-cleanroom novelty) | Seven method classes with mature precedent; calibration/uncertainty, sensor fusion, and reproducibility paths need no new fabrication | Evidence assembled |
| Q4 (manuscript/reviews) | Every reviewer request maps to a citable published norm; both reviewers' novelty positions are literature-consistent at different granularities; "first QHS stellarator" wording needs correction to match [S0128] | Evidence assembled for `30_manuscript` |
| Q5 (venue route) | Genre analysis: deployment+calibration+validation work lives in RSI/FED/NF; device letters reward the axis that was attacked | Evidence only; decision deferred |
| Q6 (next experiment) | Gap register with per-gap published norms (§6) | Feeds `40_experiment` |
| Q7 (IP screen) | Dense non-GaN fusion Hall prior art ([S0066]–[S0070], [S0112]–[S0122]) and decades-old spinning-current art ([S0033]–[S0043](https://doi.org/10.1109/ICASIC.2007.4415661)) bound any claim scope | Feeds `50_patent`; no legal conclusion here |
| Q8 (24-month plan) | Data prerequisites and campaign-coupled vs. uncoupled paths (§5) | Feeds `60_timeline` |
