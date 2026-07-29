# 05 — Candidate protectable concepts (Stage 50 pre-publication screen)

> **RESEARCH SCREEN — NOT LEGAL ADVICE**
> **NO PATENTABILITY CONCLUSION**
> **NO FREEDOM-TO-OPERATE CONCLUSION**
>
> This document is an evidence-organization screen prepared to support a
> future conversation with the advisor, Stanford OTL, and registered patent
> counsel. It does not state that any concept is patentable, does not state
> who owns anything, does not decide inventorship, and does not clear any
> product or publication against third-party rights. Only registered patent
> counsel can do those things. Nothing here is a recommendation to file.

**Basis.** Only concepts grounded in the supplied work are screened, per the
stage prompt and MISSION.md item 7: the declined manuscript
([`../../01_Publications/submitted/regular_lsens/regular_lsens.tex`](../../01_Publications/submitted/regular_lsens/regular_lsens.tex)),
the 2025 HSX raw data (`../inputs/07_HSX_august2025_results_original.zip`),
project 02 readout work
([`../../02_HSX_Hall_Sensor_Readout/docs/SPECS.md`](../../02_HSX_Hall_Sensor_Readout/docs/SPECS.md),
[`../../02_HSX_Hall_Sensor_Readout/CLAUDE.md`](../../02_HSX_Hall_Sensor_Readout/CLAUDE.md)),
project 03 vector-probe planning
([`../../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md`](../../03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md)),
the stage 40 analysis methods
([`04_HSX_EXPERIMENT_PLAN.md`](04_HSX_EXPERIMENT_PLAN.md),
[`04_DATA_ANALYSIS_PLAN.md`](04_DATA_ANALYSIS_PLAN.md)), and the stage 20
recommended direction
([`02_RESEARCH_DIRECTION_DECISION.md`](02_RESEARCH_DIRECTION_DECISION.md)).
Prior art references `PA-*` resolve to
[`05_PRIOR_ART_LEDGER.csv`](05_PRIOR_ART_LEDGER.csv); `S####` references
resolve to [`01_SOURCE_LEDGER.csv`](01_SOURCE_LEDGER.csv). Epistemic labels
follow the mission convention: *Supplied fact*, *External evidence*,
*Inference*, *Recommendation*, *Unresolved gate*.

**Standing context from stage 20 §9 (Supplied mission finding):** the
prior-art density around every concept below is high — spinning-current art
since 1990 (PA-N01), the advisor group's own GaN Hall publications
(PA-N03–PA-N05, PA-N08), and a mature fusion Hall lineage (PA-N09–PA-N18)
— so any protectable scope, if counsel finds one at all, is expected to be
**thin and combination-specific, not platform-level**. This screen is
consistent with that expectation.

---

## 0. Summary rank (evidence maturity × urgency for professional review)

| Rank | Concept | Maturity of supporting evidence | Why this urgency |
|---|---|---|---|
| 1 | CC-2 current-spun GaN in-vessel readout chain | Demonstrated on emulator (≥130× suppression; ~109× anomaly open); real-die spin pending | Fully disclosed in any revised manuscript or arXiv post — the stage 30 route makes that the next publication act |
| 2 | CC-1 in-vessel packaging/deployment stack | Reduced to practice (68 shots survived, Aug 2025) | Already fully described in the declined manuscript text that route A→C would resubmit |
| 3 | CC-5 coil-only computed-vacuum-field calibration anchor | Method fully specified; not yet executed (campaign #1 pending) | P1/P3 papers and the July UW email would disclose the method |
| 4 | CC-3 orthogonal-LCC ceramic-cube vector probe | Planning stage; no hardware built | The July UW email (feedthrough/harness asks) starts third-party disclosure; RSI paper ~Mar 2027 |
| 5 | CC-4 hybrid Hall+inductive drift-corrected architecture | Concept only; no algorithm implemented | Freshly dense 2025 prior art (PA-N19/N20) means scope is narrowest; review before WP-D publication |
| 6 | CC-6 retroactive tesla-conversion of archived uncalibrated data | Method defined in stage 40 outputs only; not executed | Lowest maturity; also raises an AI-assisted-contribution question counsel must see |

Urgency driver (Supplied fact): the advisor requires an IP screen **before**
any arXiv posting (`../inputs/ORIGINAL_REQUEST.txt`), and stage 30's route
decision holds all arXiv action behind this stage. Every concept below is
substantially disclosed by the P1 revision package; whatever review is going
to happen must happen before that manuscript or any preprint becomes public.

---

## 1. CC-1 — In-vessel UHV packaging and deployment stack for a 2DEG GaN Hall sensor

**Technical feature combination (concrete, from supplied files):** an
AlGaN/GaN 2DEG Hall die (existing octagonal topology, 200 µm inscribed
diameter) wire-bonded with aluminum wire to a ceramic leadless chip carrier;
die and bonds encapsulated with EPO-TEK 353ND epoxy; vacuum-baked at 150 °C
for 1 h for UHV compatibility; mounted on a custom zirconia ceramic holder on
a stainless standoff; covered by a **grounded graphite shield** specifically
to survive glow-discharge cleaning and reduce arcing/epoxy degradation;
operated in-vessel near the plasma edge through vacuum feedthroughs
(manuscript §II.B, Fig. 2). Validation protocol bundled with it: biased vs
unbiased shots and plasma vs coil-only shots to isolate the Hall response
from pickup/charging artifacts (manuscript §II.C, Fig. 4).

**Documentary basis / likely contributors (no inventorship decision):** the
manuscript (authors Zhao, Goodman, Gallenberger, Cox, Geiger, Senesky)
describes the stack; HSX-side mounting and GDC constraints involve the
UW-Madison co-authors; packaging lineage is the group's published LCC process.
Who conceived which feature is **not determined here** — counsel question.

**Closest prior art and overlap:** ceramic-packaged fusion Hall sensors
(PA-N17); the complete engineered ITER steady-state Hall system incl.
packaging/qualification (PA-N15); in-vessel Hall deployments since CASTOR
(PA-N12, PA-N13); GaN-2DEG-Hall-for-harsh-environment patent art (PA-P03,
abandoned but published). Each element of the stack (LCC, epoxy encapsulation,
vacuum bake, ceramic holder, grounded shields) is individually conventional.

**Potential technical distinctions (conditional):** *if* no reference
combines a wide-bandgap 2DEG Hall die with this specific UHV/GDC-survivable
packaging sequence for in-vessel plasma-facing service, a narrow combination
claim *might* be arguable; the graphite GDC shield over an epoxy-encapsulated
active magnetic sensor is the most specific single feature found nowhere in
the screened art. This is an absence observation from a bounded search, not a
novelty conclusion.

**Enablement/data status:** strongest of all concepts — built, deployed,
survived 68 shots (Supplied fact, manuscript §III.A; raw data in
`../inputs/07_HSX_august2025_results_original.zip`).

**Risks:** *Claim-scope:* a claim narrow enough to clear PA-N15/PA-N17 may be
trivially design-aroundable (different epoxy, different shield material).
*Design-around:* high — the stack is an assembly of catalog parts.
*Publication:* the declined manuscript already describes the stack completely;
resubmission or arXiv makes it prior art against any later filing outside
grace-period windows (see checklist §5). Also note the deployment itself
occurred Aug 2025 at a collaborator facility — whether that constitutes a
public use/disclosure event is a **counsel question, not answered here**
(Unresolved gate).

---

## 2. CC-2 — Current-spun, chopper-stabilized external readout chain for an in-vessel GaN Hall sensor

**Technical feature combination (concrete, from project 02 files):** external
floating ~100 µA current bias entering through a sense-resistor loop (R9/R10,
DC even while spinning because the chopper is downstream); an 8-state
spinning sequence `state=(a2<<2)|(a1<<1)|a0` in which the a1 pairs cancel
plate offset, a0 pairs cancel amplifier offset, and the a2 chopper reversal
removes second-order residuals; demodulation sign rule `+1 if a0==a2 else −1`
with 30 % per-phase blanking; AD8429 instrumentation amplifier (G≈100.3);
40 kHz phase rate → ~1–2 kHz demodulated bandwidth with **raw v_meas
captured in parallel for fast transients**; demonstrated ≥130× offset
suppression on a resistor-ring emulator (SPECS.md; project 02 CLAUDE.md;
journal 2026-07-08). The ~109× magnitude anomaly (C017) is open (Supplied
fact — flagged, not papered over).

**Documentary basis / likely contributors:** project 02 repository (design,
firmware, phase algebra, bench results) — maintained by Tim; the die and its
offset physics come from the group's published lineage (PA-N03–PA-N05,
PA-N08). Contribution boundaries are a counsel/advisor question.

**Closest prior art and overlap:** the heaviest overlap of any concept.
Spinning current itself: PA-N01 (1990), limits PA-N02, randomized/advanced
variants and a dense **active Infineon patent family** (PA-P01, plus
US9110121B2/US8154281B2 noted therein); spinning applied to the *same GaN
2DEG plate family by the same research group* in 2019 (PA-N03 — the single
most damaging reference); dual-path precision+fast readout claimed by TI
(PA-P10); GaN-2DEG-high-temp Hall claims (PA-P03).

**Potential technical distinctions (conditional):** *if* anything survives
PA-N03 and the Infineon/TI families, it would be at system level only — e.g.
the specific combination {external discrete mux network + floating
current-loop bias with downstream chopper + in-vessel sensor at the end of a
long harness + raw-plus-demodulated dual capture for shot transients} as a
*fusion-diagnostic readout method*. Stage 20 §9's thin-claims expectation
applies with full force here.

**Enablement/data status:** emulator-demonstrated; real-die spinning and
absolute calibration not yet performed (C016/C017; stage 40 B-01/C-01 gates).
A method claim's enablement basis improves materially once the bench
calibration package (WP-C) exists.

**Risks:** *Claim-scope:* extreme prior-art density; any granted scope likely
so narrow that trivial phase-table or amplifier substitutions escape it.
*Design-around:* high for the same reason. *Publication:* SPECS-level detail
(phase table, sign rule, blanking) would likely appear in P1's methods
section; once published it is unclaimable art. **Freedom-to-operate note
(question, not conclusion):** active third-party patents (PA-P01, PA-P02,
PA-P10) exist in this space; whether a research deployment or any future
commercial readout infringes anything is strictly a counsel question.

---

## 3. CC-3 — Orthogonal-face ceramic-cube vector probe of LCC-packaged GaN dies with synchronized external spinning

**Technical feature combination (concrete, from project 03 plan):** 2–3
AlGaN/GaN dies, each in its own LCC using the proven CC-1 process, mounted on
mutually orthogonal faces of a machinable-ceramic cube; per-axis replicated
readout boards; **one clock source fanning shared a0/a1/a2/EN lines to all
boards so all axes spin in phase (zero inter-axis phase skew by
construction) with one sync line timestamping all demods**; per-board
floating 100 µA bias (sources deliberately not shared so spinning muxes
don't fight); 12-conductor harness through a vacuum feedthrough; 3×3 matrix
calibration v = M·B + b via indexed-orientation Helmholtz sweeps with
misalignment extracted by polar decomposition (plan §§2.2–2.3, 3.2).

**Documentary basis / likely contributors:** project 03 plan (authored in
Tim's repo); cube packaging leverages the group's LCC process; harness and
feedthrough specifics depend on UW input (open item #1). No inventorship
determined.

**Closest prior art and overlap:** Infineon's interleaved multi-channel
X/Y/Z spinning patent (PA-P02 — closest patent art; active to 2038);
monolithic 3-axis sensors (PA-P08, PA-P09); integrated 3-axis Hall
teslameters and precision probes (PA-N24, Senis/Popovic lineage with a large
patent estate); mixed-technology multi-axis modules (PA-P11); fusion Hall
arrays (PA-N13). Discrete orthogonal mounting of packaged sensors is itself
a known assembly approach (noted in PA-P08's background).

**Potential technical distinctions (conditional):** *if* the art contains no
{orthogonal-face cube of individually packaged WBG Hall dies + phase-locked
simultaneous (not interleaved/multiplexed) spinning across independent
analog channels + in-vessel UHV service} combination, a narrow
system/apparatus claim *might* be arguable. The simultaneous-phase-locked vs
interleaved-multiplexed contrast with PA-P02 is the most specific potential
distinction; whether it is patentably significant is for counsel.

**Enablement/data status:** prophetic — no cube, no second/third board, no
gen-2 die inspection yet (project 03 timeline puts builds in Sep 2026).
Advisor decision #3 (die supply) gates it. Weakest enablement of the
hardware concepts.

**Risks:** *Claim-scope:* must thread between PA-P02 and the Senis estate.
*Design-around:* moderate (2-axis variants, different sync schemes).
*Publication:* the July UW email (feedthrough pin count, harness, mount
survey) begins disclosing design specifics to a third-party institution —
whether an inter-institutional confidentiality framework exists is an
**Unresolved gate** for the checklist; the RSI paper (~Mar 2027) would
disclose everything.

---

## 4. CC-4 — Hybrid Hall + inductive drift-corrected measurement architecture for stellarator magnetics (WP-D)

**Technical feature combination (as far as supplied files support):** fusing
the absolute, low-bandwidth, drift-free spun-Hall channel with HSX's
existing fast inductive channels (pickup/B-dot, Mirnov) via a Kalman-type
estimator carrying a drift state, to produce a drift-corrected wide-band
field estimate on a stellarator; quantified Hall-vs-inductive
complementarity on HSX data (user's original interest in
`../inputs/ORIGINAL_REQUEST.txt`; stage 20 WP-D; stage 40
04_DATA_ANALYSIS_PLAN.md pipelines). No estimator has been implemented yet
(Supplied fact: nothing in project 02/03 or the archive implements fusion).

**Documentary basis / likely contributors:** the direction is the user's
stated original research interest (Supplied fact); its elaboration into
WP-D work packages is mission-stage output. **Note for counsel:** portions
of the concrete plan text were produced by AI planning tools; the
contribution question this raises for inventorship is flagged, not resolved,
here (see checklist §4).

**Closest prior art and overlap:** the densest *fresh* NPL field of any
concept — KSTAR Kalman coil+Hall drift estimation (PA-N19, 2025), COMPASS
lineage coil+Hall Kalman fusion (PA-N20, 2025), CERN-lineage drift-free
Kalman integration (PA-N21) and feed-forward correction (PA-N22); JET's own
proposed hybrid Hall+coil probe (PA-N10, 2022); architecture-level hybrid
drift-corrected in-vessel measurement patented by DOE in 1995 (PA-P04,
expired) and Hall+coil circuits from 1991 (PA-P05, expired).

**Potential technical distinctions (conditional):** *if* any scope exists,
it is limited to implementation specifics (e.g. estimator structure tied to
the spun-Hall demod timing, or stellarator/QHS-specific formulation);
"Kalman fusion of Hall and coil for fusion magnetics" as such is 2025
journal art. Stage 20 §11 already tracks PA-N19-class art as a
falsifiability condition for the *scientific* first — the *patent* first is
even harder.

**Enablement/data status:** lowest of the hardware-adjacent concepts — no
implementation, and the co-located B-dot data question (U-1) is open.

**Risks:** *Claim-scope:* minimal viable scope given 2025 art.
*Design-around:* trivial (alternative estimators). *Publication:* the P2
paper is the disclosure event; nothing needs deciding before WP-D produces
results, but counsel review before P2 submission is the natural gate.

---

## 5. CC-5 — In-situ absolute calibration anchor from coil-only shots and the computed vacuum field at a surveyed pose

**Technical feature combination (concrete, from project 03 §3.3 and stage 40
plans):** use the machine's own confinement coils, in dedicated coil-only
(no-plasma) shots at multiple field settings, as the calibration reference:
compute the vacuum field vector at the probe's surveyed pose (position +
orientation, ±1 mm / ±0.5–1°) from coil currents and geometry; compare
against the bench-calibrated, matrix-corrected probe output M⁻¹(v−b)
component-by-component; propagate a traceable uncertainty chain (Helmholtz
geometry + 0.1 % shunt on the bench side; pose survey + coil-current
uncertainty on the machine side; stage 40 04_UNCERTAINTY_AND_STATISTICS_PLAN.md).

**Documentary basis / likely contributors:** project 03 plan §3.3 (the
"RSI centerpiece"); stage 40 anchors (E-01..E-03, F-01); the pose survey and
vacuum-field computation require UW collaborators (their computation, their
machine) — a joint-contribution fact pattern counsel must examine.

**Closest prior art and overlap:** CTH's GaAs Hall array validated against
Biot–Savart computed vacuum fields (PA-N18 — the method's published
paradigm); reference-field in-situ calibration patents using dedicated
calibration coils (PA-P06 active, PA-P07 expired); traceable Hall
calibration metrology (PA-N23); V3FIT/HSX reconstruction context (S0132).

**Potential technical distinctions (conditional):** the generic method is
published (PA-N18). *If* anything is arguable, it is the narrow procedural
combination {facility-coil-as-reference + surveyed-pose vector anchor +
matrix-calibrated multi-axis probe + stated traceability chain} as a
calibration-transfer *method*; PA-P06/PA-P07 use dedicated embedded coils,
not the facility's own confinement set. Conditional and thin.

**Enablement/data status:** method fully specified; zero executions (needs
campaign #1 or any coil-only session; G0/G-cal gates). Prophetic until
August 2026.

**Risks:** *Claim-scope:* PA-N18 forecloses breadth. *Design-around:*
moderate. *Publication:* the method appears in the P1/P3 papers and in the
July UW email's asks (survey + vacuum-field computation) — same third-party
disclosure question as CC-3.

---

## 6. CC-6 — Retroactive absolute-unit conversion of archived uncalibrated voltage-bias data

**Technical feature combination (from stage 40 outputs):** recover
tesla-unit *changes* from the 2025 archive (voltage-bias, G=200 chain,
unknown V_off) by (a) performing a voltage-bias-mode S_v calibration (C-03)
of the **same physical deployed die** post-campaign, (b) applying a
changes-only conversion ΔB = ΔV_out/(A_v·S_v·V_bias) that never claims
absolute levels through the unknown offset, and (c) carrying a G-01
uncertainty budget with named unmeasured terms (04_DATA_ANALYSIS_PLAN.md;
04_MEASUREMENT_REQUIREMENTS.csv rows C-03/G-01).

**Documentary basis / likely contributors:** this method exists only in
stage 40 mission outputs elaborating the AE's Fig.-5-in-field-units request;
the underlying data and chain facts are Tim's. **The AI-assisted origin of
the method text is a material fact for any inventorship analysis and is
flagged for counsel** (see checklist §4). US practice requires natural-person
inventors; how AI-assisted conception is treated is an evolving legal
question this screen does not answer.

**Closest prior art and overlap:** retrospective calibration/sensitivity
transfer is standard metrology practice (PA-N23 lineage); the changes-only
trick is algebra on the published transfer function (manuscript Eq. 1–2).
No specific patent art was sought for "retroactive sensor-archive
calibration" beyond the CC-5 searches — a bounded-search statement, not an
absence claim.

**Potential technical distinctions (conditional):** likely none of
protectable weight; screened for completeness because it is a concrete
method in the supplied+generated corpus. I-4 (deployed-module whereabouts,
NOT ESTABLISHED FROM SUPPLIED FILES) gates even its execution.

**Enablement/data status:** unexecuted; blocked by I-4.

**Risks:** publication of the method in P1 is the natural course; holding it
back has research cost and near-zero plausible IP upside. Lowest priority
for counsel time.

---

## 7. Cross-cutting observations for the counsel conversation

1. **The group's own 2019 publications are the controlling prior art** for
   CC-2 (PA-N03 especially, plus its public arXiv version and PA-N08). Any
   argument for remaining scope must start from what those references do
   *not* teach: the in-vessel fusion system context.
2. **No Stanford/Senesky-group patent on GaN Hall sensing was found** in the
   bounded searches run for this stage (inventor- and topic-keyed searches;
   see WORKLOG 2026-07-25). This is an absence finding from a limited
   search, not a clearance: OTL's internal docket may contain undisclosed or
   unpublished filings — ask OTL directly (checklist §3).
3. **Every concept's disclosure event is the same manuscript.** The P1
   revision (or any arXiv posting) discloses CC-1, CC-2, CC-5, and CC-6
   nearly completely, and the July UW email starts disclosing CC-3/CC-5
   specifics to a third party. The screen therefore front-loads urgency on
   what P1 contains, not on what is technically strongest.
4. **Expired patents matter in the other direction:** PA-P04, PA-P05, PA-P07
   are in the public domain — they are simultaneously prior art *against*
   new claims and evidence that the broad architecture ideas are free for
   anyone (including competitors) to use.
5. **Sponsor rights:** the manuscript acknowledges DOE contract
   DE-AC02-76SF00515 / SLAC FWP 101264, TomKat Center support, and NSF-supported
   NNCI fabrication (ECCS-2026822) (Supplied fact, manuscript
   Acknowledgment). Government-funding obligations (e.g. Bayh-Dole election
   and disclosure duties) and their effect on ownership/licensing are
   **questions for OTL and counsel**, listed in the checklist — no
   conclusion is stated here.

*End of screen. This document intentionally reaches no patentability,
ownership, or freedom-to-operate conclusion.*
