# Stage 10 — Publication Technical Disclosure Map

Run: HSXIP-20260805T071311Z. Scope authority: `IP_SCOPE.md`, `CLAUDE.md`,
`schemas/OUTPUT_GATES.md`. Inputs read in full: `inputs/manuscript/source/regular_lsens/regular_lsens.tex`
(619 lines), `inputs/manuscript/submission.pdf` (9 pages: portal metadata pp.1-3,
manuscript body pp.4-7, graphical abstract p.8, cover letter p.9). This document
is a disclosure/enablement map, not a patentability opinion, not an exhaustive
prior-art search, and not legal advice. It does not evaluate novelty or
non-obviousness under any legal standard (that is Stage 30's job); where the
authors themselves assert novelty, that assertion is recorded as a fact, not
endorsed or evaluated.

## 1. Methodology

**Disclosure-level taxonomy** (applied per `OUTPUT_GATES.md`):

- `explicit` — stated directly in the manuscript body, figure, caption, or
  (for the cover letter/graphical abstract, which are part of the same
  `submission.pdf` controlling artifact per `IP_SCOPE.md`) the submission
  bundle, as implemented/performed/observed.
- `implicit` — reasonably inferable from stated facts but not directly stated;
  the inference chain is given in the `notes` field.
- `future` — explicitly framed by the authors as future work, or a citation to
  work not performed in this paper. Per `CLAUDE.md`, a future-work sentence or
  citation is never recorded as `implemented = yes` or as invented content of
  this manuscript.
- `absent` — not present anywhere in the three controlling artifacts, but
  material to enablement/IP screening; used only for gap-flagging, never as a
  disclosed feature.

**yes/no/partial/unclear convention** used consistently across
`implemented`, `validated`, `authors_claim_novel`, `known_group_work`:

- `implemented`: `yes` = manuscript states the feature was actually built,
  fabricated, installed, or performed; `no` = not done (future/absent items);
  `partial` = only a sub-part was done or it was done generically/off-the-shelf
  without paper-specific enablement detail.
- `validated`: `yes` = the manuscript reports data or an observed result that
  demonstrates the feature functioned as described; `no` = no supporting data
  or observation is shown; `partial` = only qualitative/indirect support is
  shown (e.g., overall device survival across shots, without a direct
  controlled comparison).
- `authors_claim_novel`: `yes` = the authors use explicit novelty/priority
  language ("first," "novel," etc.) about the specific feature/claim in that
  row, quoted verbatim in `notes`; `no` = no such language appears for that
  feature; `unclear` is not used in this map — every instance found was either
  an explicit quoted claim or no claim at all.
- `known_group_work`: `yes` = the manuscript (TeX body or cover letter)
  explicitly attributes the technique, process, geometry, or physical
  understanding to an earlier group publication via citation, named in
  `notes`; `no` = no such attribution appears; `partial` = the general
  category of technique is cited to others' prior art (not the authors' own
  earlier work) or only loosely associated.
- `commercial_use`: a textual flag, not a market analysis — `yes` = the
  manuscript ties the feature to a stated practical/application benefit
  (harsh-environment/in-situ sensing, fusion diagnostics); `no` = no such
  framing for that specific feature; `unclear` = ambiguous/generic framing
  only.

`missing_enablement` records, per row, what a reader/practitioner cannot
reproduce or verify from the three controlling artifacts alone — this is an
enablement-gap flag, not a legal sufficiency determination.

## 2. Section-by-section walkthrough

### §I Introduction (TeX lines 448–453)
Establishes the background and problem (Mirnov-coil integration drift, L449;
GaN thermal tolerance and 2DEG mobility rationale, L451, citing prior thermal
characterization up to 576°C attributed to ref11/Alpert 2020 and general
AlGaN/GaN Hall-sensor art ref7–ref12) and states the paper's contribution: an
AlGaN/GaN Hall sensor "fabricated, packaged for ultra-high-vacuum and
high-temperature operation, and deployed near the plasma edge" of HSX, with a
1 MHz bandwidth readout across 68 shots (L453). HSX itself is described as
"the first stellarator designed and built with a quasi-helically symmetric
magnetic field" (L453) — this "first" is a cited fact about the host facility
(refs 13–14), **not** an authors' novelty claim about the sensor invention;
it is recorded separately from the sensor-specific novelty claims below.

### §II-A Fabrication (TeX line 457, Fig. 1 / lines 458–463)
Maps to feature group 1 (Hall device and fabrication): purchased NTT AAT
heterostructure wafer stack, mesa etch, Ti/Al/Mo/Au ohmic contacts annealed at
850°C/35s (citing ref11), 7 nm Al₂O₃ passivation, vias, Ti/Au bond metal,
5×5 mm die singulation, regular octagonal 200 µm-inscribed-diameter Hall plate
(citing ref10). Rows F01–F09.

### §II-B Packaging (TeX line 465, Fig. 2 / lines 466–471, Fig. 3 caption line 469 for "flange")
Maps to feature group 2 (UHV/GDC module): Al wire bonds to a ceramic LCC
(Spectrum Semiconductor Materials), EPO-TEK 353ND epoxy encapsulation, 150°C/
1-hour vacuum bake "to meet the ultra-high-vacuum (UHV) requirements of the
HSX facility," custom zirconia ceramic holder, stainless-steel standoff,
custom flange for insertion (Fig. 2 caption, L469), and the grounded graphite
shield with its stated purpose ("to reduce the risk of arcing and epoxy
degradation during glow discharge cleaning (GDC) and plasma operations,"
L465). Rows F10–F17.

### §II-C Experimental Setup (TeX lines 478–487, Fig. 3 / lines 472–477, Fig. 4 / lines 488–493)
Maps to feature group 3 (bias and readout): two-terminal voltage bias (0.4 V
biased / 0 V unbiased) supplied by the built-in waveform generator of a
Keysight DSOX1204G oscilloscope, INA849 instrumentation amplifier + two
OPA814 op-amp stages (gain breakdown ×10/×10/×2 per Fig. 3) for a total 200
V/V gain and 1 MHz bandwidth, external electronics connected via vacuum
feedthroughs (L479). This subsection also contains the paper's only in-body
future-work sentence at the readout level: "Absolute calibration of
$V_{\mathrm{off}}$ and quantitative correction for its temperature dependence
remain future work" (L487), and attributes the general fact that $V_{off}$
"may vary with temperature during operation" to ref15 (Dowling 2019 Ph.D.
dissertation, Stanford) — known group work, not new characterization in this
paper. Rows F18–F24, F34.

### §III Results and Discussion (TeX lines 494–504, Fig. 4/Fig. 5)
§III-A Sensor Functionality (L495–496) reports the 68-shot deployment, HSX
operating context (18 motor generators, 48 coils, ~800 ms coil ramp, 50 ms
flat-top, up to 200 kW/28 GHz ECRH), the biased-vs-unbiased comparison
(Fig. 4a, shots 63/65) and plasma-vs-coil-only comparison (Fig. 4b, shots
65/68), and a repeatability claim ("the shape and timing of this transient
repeated reliably under comparable conditions"). §III-B Real-Time Plasma
Energy Tracking (L503–504) reports the diamagnetic-loop temporal comparison
(Fig. 5, shots 21/18/19) with an explicitly stated ~30 ms DAQ timing offset,
and explicitly distinguishes the two diagnostics as measuring "physically
distinct quantities" that are only "expected to be temporally correlated"
(citing ref1), not interchangeable measurements. Rows F25–F32.

### §IV Conclusion (TeX line 506)
Restates the fabrication/packaging/deployment result and lists four explicit
future-work items in one sentence: absolute calibration via in-situ
cross-reference with established HSX diagnostics (citing ref17), extended-
duration deployment to evaluate offset stability, radiation/neutron
irradiation characterization at a dedicated facility, and lower-noise readout
electronics for smaller-amplitude MHD fluctuations. Rows F33, F35–F37.

### Acknowledgment (TeX lines 511–514)
DOE Contract DE-AC02-76SF00515, SLAC FWP 101264, TomKat Center (Stanford),
fabrication at Stanford Nanofabrication Facility (NNCI, NSF ECCS-2026822).
Sponsorship facts only, relevant to Stage 50, not mapped as a technical
feature row.

### Cover letter and graphical abstract (`submission.pdf` pp. 8–9)
Not part of `regular_lsens.tex`, but part of the controlling `submission.pdf`
per `IP_SCOPE.md`. The graphical abstract (p.8) is a visual restatement of
Fig. 2/Fig. 8-style content (HSX cutaway, epoxy-coated sensor, 5 mm die,
custom flange) — no new technical content beyond the body. The cover letter
(p.9) contains the manuscript's only explicit "first"/novelty language about
the sensor itself and its only explicit sensitivity-comparison claim; see §4
below. Rows F49–F51.

## 3. Explicit "novel"/"first" claims — exact quotes and locations

The rendered TeX manuscript body contains **no** "first," "novel," or
"first-of-its-kind" language applied to the sensor, package, or readout
invention itself. The only "first" language in the TeX body (L453) describes
the **host facility**, not the sensor: *"the Helically Symmetric eXperiment
(HSX), the first stellarator designed and built with a quasi-helically
symmetric magnetic field"* — a fact attributed to citations ref13/ref14, i.e.
prior published characterization of HSX by others, not an authors' novelty
assertion about this manuscript's invention. This absence in the manuscript
body is itself recorded as a finding.

All explicit novelty/"first"/comparative-superiority language about the
sensor is confined to the **cover letter** (`submission.pdf` p.9), which is
part of the controlling submission bundle but not part of the peer-reviewed
manuscript body:

1. *"To our knowledge, this is the first GaN-based Hall-effect sensor
   deployed inside a stellarator for in-situ magnetic field monitoring."*
   (`submission.pdf` p.9, cover letter, paragraph 2.) — Row F49.
2. *"The present manuscript reports the first deployment and validation of
   this platform in an operating stellarator and contains no overlap in data
   or text with these earlier studies."* (`submission.pdf` p.9, cover letter,
   paragraph 3, immediately following the citation of the authors' own
   Alpert 2019/2020 papers.) — Row F50. This sentence is simultaneously a
   novelty claim (about the deployment) and a group-work-differentiation
   statement (about the earlier lab papers), so it is flagged
   `authors_claim_novel = yes` and `known_group_work = yes` together.
3. *"Compared with the metal Hall probes developed for ITER and DEMO by
   other groups, the 2DEG-based platform offers substantially higher
   sensitivity while retaining thermal tolerance."* (`submission.pdf` p.9,
   cover letter, paragraph 3.) — Row F51. This is a comparative-superiority
   claim against third-party (not the authors') prior art (ref5 Quercia 2022,
   ref6 Bolshakova 2017); no quantitative sensitivity data supporting
   "substantially higher" appears anywhere in the three controlling
   artifacts.

The manuscript body's strongest self-description language is a feasibility
claim, not a novelty claim: *"these results establish AlGaN/GaN Hall-effect
sensors as a feasible platform for real-time magnetic diagnostics in
fusion-relevant environments"* (L506, Conclusion). Per `CLAUDE.md`, a
feasibility/successful-experimentation statement is not treated here as a
novelty assertion and is not evaluated for patentability.

## 4. Attribution to earlier group work / cited prior art

| Citation | What is attributed | Location |
|---|---|---|
| ref10 (Alpert et al., IEEE Sensors J. 2019) | The octagonal Hall-plate geometry and 200 µm inscribed diameter | TeX L457; cover letter p.9 ("effect of device geometry on sensitivity and offset") |
| ref11 (Alpert et al., Rev. Sci. Instrum. 2020) | The 850°C/35s Ti/Al/Mo/Au ohmic-contact anneal recipe; prior thermal characterization to 576°C | TeX L451, L457; cover letter p.9 ("stable current-scaled sensitivity up to 576°C") |
| ref15 (Dowling, Stanford Ph.D. dissertation 2019) | The general behavior that $V_{off}$ is bias-independent but temperature-dependent | TeX L487 |
| ref16 (Schmitt et al., Nucl. Fusion 2013) | The HSX diamagnetic-loop diagnostic used as the comparison instrument | TeX L504 |
| ref17 (Chlechowitz et al., Nucl. Fusion 2015) | The "established HSX magnetic diagnostics" that future absolute-calibration cross-reference will use | TeX L506 |
| ref5 (Quercia et al., Nucl. Fusion 2022), ref6 (Bolshakova et al., Nucl. Fusion 2017) | ITER/DEMO metal Hall probes, used as the comparison basis for the cover-letter sensitivity claim | Cover letter p.9; TeX L449/L575–L578 bibliography |
| ref7–ref9, ref12 | General AlGaN/GaN HEMT, 2DEG-formation physics, and high-temperature AlGaN/GaN Hall-sensor art | TeX L451 |
| ref1, ref2, ref3, ref4 | General magnetic-diagnostics and Mirnov-coil integration-drift background | TeX L449 |
| ref13, ref14 | HSX facility design/construction, including the "first quasi-helically symmetric stellarator" fact | TeX L453 |

This table shows that the Hall-plate geometry and the ohmic-contact anneal
recipe — two of the more specific fabrication choices in §II-A — are each
explicitly traced by the authors to their own earlier published work, not
newly developed for this manuscript. No such citation exists in the
manuscript for the UHV/GDC packaging choices (LCC, epoxy, bake parameters,
zirconia holder, standoff, flange, graphite shield) — none of those five
elements is attributed to any reference in the bibliography.

## 5. Implemented-and-validated vs implemented-but-not-validated vs future-only

**Implemented and validated with in-manuscript data** (rows F01–F09, F18–F24
device/readout elements as used in the deployment; F25–F30, F32 deployment
results): the fabricated device, its integration into the readout chain, and
its 68-shot in-vessel operation are all supported by Fig. 4/Fig. 5 waveform
data and the accompanying comparative narrative.

**Implemented but only partially/indirectly validated**: the grounded
graphite shield (F16) — its installation is explicit, its stated purpose is
explicit, but no comparative data with/without the shield, no arcing
incident log, and no epoxy-degradation measurement is presented; the device's
mere 68-shot survival is the only (indirect) evidence offered. The GDC/plasma
exposure itself (F17) is not explicitly described as tested with data — it is
inferred only from the shield's stated protective purpose (implicit).

**Future-only** (rows F33–F37): absolute $V_{off}$/field calibration,
temperature-dependent offset correction, extended-duration deployment,
radiation/neutron characterization, and lower-noise readout electronics. Per
`CLAUDE.md` and `IP_SCOPE.md`, these are recorded with `implemented = no`,
`validated = no`, and `disclosure_level = future` — they are prior-art/
future-work context, not disclosed inventions of this manuscript.

## 6. Largest enablement / missing-evidence gaps

These map directly to the "Questions that materially affect the strongest
candidate" list in `IP_SCOPE.md` (rows F38–F48):

1. **Graphite shield conception and specification (F40, F41, F42)** — no
   drawings, dimensions, aperture layout, clearance, current path, or
   grounding-route detail is given anywhere in the three artifacts; the shield
   is described only as "a grounded graphite shield ... installed over the
   packaged sensor module" (L465). This is the single largest gap for
   evaluating the UHV/GDC module as a candidate, since `IP_SCOPE.md` flags
   shield conception/ownership as an open OTL question.
2. **No documented failure mode or without-shield comparison (F42)** — the
   stated purpose (arcing/epoxy-degradation reduction) is asserted, not
   demonstrated by a controlled comparison or failure-mode narrative.
3. **No UHV acceptance criterion for the bake (F43)** — "150°C for 1 hour to
   meet the ultra-high-vacuum (UHV) requirements of the HSX facility" (L465)
   states a process but not the pressure, outgassing rate, RGA, or leak-test
   criterion that "meeting UHV requirements" means; no acceptance data is
   reported.
4. **No absolute calibration data (F38, F47)** — the manuscript explicitly
   states this is future work (L487, L506); no B-field-to-volts sensitivity
   value, no Tesla-referenced measurement, is reported anywhere in this
   paper.
5. **No temperature-characterization data specific to this manuscript (F39)**
   — the 576°C thermal-stability fact is attributed to prior published work
   (ref11), not measured in this paper; no in-vessel temperature log is
   reported.
6. **No quantitative noise/SNR figures (F45)** and **no tabulated raw data**
   (F48) — all quantitative results are presented only as time-series plots
   (Fig. 4, Fig. 5) with axis-scale values (e.g., 0–0.4 V, 0–60 J); no numeric
   noise floor, SNR, or sensitivity coefficient is stated in text.
7. **No explicit inventorship/conception statement (F44)** and **no GDC
   cycle-count or exposure-log data (F46)** — both are simply absent from the
   text; `IP_SCOPE.md` flags inventorship attribution and UW-Madison
   contribution as open questions this document cannot resolve.

## 7. Scope discipline confirmation

No excluded concept from `IP_SCOPE.md` (three-axis/vector probes, Hall-coil
hybrids, radiation-compensation/current-spinning/self-calibration
architectures, TCAD/simulation, startup concepts, future PhD plans, or
unpublished readout inventions) appears anywhere in the CSV as an
`implemented` or `validated` feature. Where a future-work sentence gestures
toward radiation characterization or a lower-noise readout, it is recorded
strictly under `disclosure_level = future` with `implemented = no`,
`validated = no` (rows F36, F37), consistent with `CLAUDE.md`'s hard rule
that a future-work sentence is never converted into a manuscript invention.

## 8. Files produced

- `outputs/10_PUBLICATION_TECH.md` (this file)
- `outputs/10_DISCLOSURE_MAP.csv` (51 rows, exact schema from
  `schemas/OUTPUT_GATES.md` §10)
