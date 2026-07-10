# DELIVERABLE — Paper plan & state of the literature review

**Paper:** magnetic-field sensors review → MDPI *Sensors* (ISSN 1424-8220), submit before **30 Oct 2026**.
**Purpose of this document:** the single file to open to (a) finalize the title and outline this week, and (b) see exactly where the literature review stands — what is solid, what is thin, what is missing, and which patch runs to fire next.
**How to read citations here:** `[key]` = an entry in `outputs/reference_registry.csv` (122 unique references, DOI-verified per `outputs/70_bibliography_report.md`). Stage-80 note: this stage synthesizes prior outputs only; **no new sources were retrieved**, so no `refs_raw/80.jsonl` entries were created — every key below already exists in the registry.
**Detail lives in:** `10_titles.md` (all 15 titles), `20_outlines.md` (all 4 outlines), `30_litreview_sensor_types.md`, `40_litreview_applications.md`, `50_litreview_future_methods.md`, `60_standards_and_business.md`, `70_bibliography_report.md`, `00_target_journal_brief.md`.

---

## 1. Recommended title

> **"A Review of Magnetic-Field Sensing Technologies and Their Applications in Energy, Transportation, Industry, and Biomedicine"** (Stage 10, #2)

**Justification.** It states exactly what the paper is and names all four domains, which maximizes database discoverability across each domain's literature and matches MDPI's descriptive-title norm. It cannot be accused of over- or under-claiming — the ML/digital-twin third and the standards third are contents, not promises, so neither reviewer expectations nor scope are distorted. It also pairs naturally with the recommended A+B-hybrid outline below (the domains named in the title are literal subsection headings). If the future-methods third deserves title billing, append the subtitle variant: *"…: From Established Devices to Machine Learning and Digital Twins."*

**Shortlist of alternates** (full annotations in `10_titles.md`):

| # | Title | Pick it if… |
|---|---|---|
| 7 | From Sensing Elements to Deployed Systems: Magnetic-Field Sensor Technologies, Industry Standards, and Commercial Readiness | the standards/TRL/investor angle should be the visible differentiator from existing sensor reviews |
| 6 | Magnetic-Field Sensors in the Age of Machine Learning and Digital Twins: A Review of Devices, Applications, and Emerging Methods | targeting an AI-in-sensing Special Issue; strongest click-through hook |
| 3 | Magnetic Sensors from Hall Effect to Quantum Magnetometry: Technologies, Applications, and Outlook | the established→pioneering technology span should headline |
| 13 | Commercial and Pioneering Magnetic-Field Sensors: A Comparative Review of Performance, Applications, and Maturity | the commercial-vs-pioneering contrast (the paper's actual organizing axis) should headline |

---

## 2. Recommended outline

**Outline A (sensor-family-primary) hybridized with Outline B's domain depth in the applications tail** — Stage 20's recommendation, adopted unchanged. Why it wins:

1. **Least friction with the brief and the evidence.** `PROJECT_BRIEF.md` §3 ("Section 2 backbone" = taxonomy) and §4 ("current use, Section 2 tail") literally describe A; the Stage 30 and 40 briefs drop into it one-to-one with no restructuring.
2. **Lowest-risk shape for *Sensors*.** Family-primary is the canonical review structure the journal's reviewers expect; Outline C's regime framing is more original but requires a sourced envelope boundary everywhere — the highest-hallucination-risk skeleton.
3. **The business third survives intact**, importing Outline D's best artifacts (standards-as-market-gates titling, the risk register as §4.6) without D's unconventional Section 2.

**Hybridization applied:** A-2.11 is expanded into four full domain subsections at Outline B's level of specificity (named deployments, incumbent-vs-challenger per domain, one domain figure), closing with the family × domain matrix. Also mined from the other outlines: C's capability map as Fig. 1, D's risk register as 4.6.

### The outline in full

**1. Introduction (~7%)**
- 1.1 Why Magnetic Sensing Matters — one measurand, four industries; the trade-space (range vs. resolution vs. bandwidth vs. SWaP-C vs. temperature); why no single family wins. *Fig. 1:* capability map — field range vs. bandwidth with family envelopes (fT biomagnetics → multi-T industrial), sourced numbers only.
- 1.2 Scope, Method, and Contributions — vendor-neutral narrative review; commercial + pioneering families; four domains; future methods; standards/TRL for a dual technical + business/investor readership; exclusions (magnet design, full geophysics/space survey, single-application deep dives).
- 1.3 Organization of the Paper — roadmap; pointers to Table 1 (master comparison) and Table 2 (family × domain matrix) as navigation aids.

**2. Magnetic-Field Sensor Technologies and Their Current Applications (~31%)**
- 2.1 Figures of Merit and Taxonomy — noise floor (pT/√Hz), dynamic range, bandwidth, offset & drift, linearity, power, cost tier, maturity class; commercial-vs-pioneering as the organizing contrast. *Fig.:* taxonomy tree.
- 2.2 Hall-Effect Sensors — Si CMOS, spinning-current offset cancellation, GaN/2DEG harsh-environment variants; strengths/weaknesses box.
- 2.3 Magnetoresistive Sensors: AMR, GMR, and TMR — physics ladder, MR ratios, bridges, set/reset; strengths/weaknesses box.
- 2.4 Fluxgate Magnetometers — parallel/orthogonal/FM-OFG; strengths/weaknesses box.
- 2.5 Search-Coil / Induction Sensors — incl. Rogowski relatives; strengths/weaknesses box.
- 2.6 Giant Magnetoimpedance (GMI) Sensors — strengths/weaknesses box.
- 2.7 SQUID Magnetometers — dc/rf, LTS/HTS, cryogenic infrastructure; strengths/weaknesses box.
- 2.8 Optically Pumped Magnetometers (OPM / SERF) — scalar vs. zero-field; wearable arrays; strengths/weaknesses box.
- 2.9 NV-Diamond Magnetometry — ODMR, ensembles vs. single centers, vector capability; strengths/weaknesses box.
- 2.10 Other Emerging Families — magnetoelectric composites; MEMS/Lorentz-force; fiber-optic/magneto-optic; NMR/Overhauser/CPT (positioned as the field's calibration/traceability anchors → bridge to 4.5).
- 2.11 Cross-Cutting Comparison and Current Applications in the Four Domains
  - *Table 1 (master):* family × {range, resolution/noise floor, bandwidth, temperature, power, cost tier, maturity, representative devices} — sourced numbers only (skeleton exists in Stage 30).
  - 2.11.1 Energy — inverter/traction current, BMS, smart grid/OCS, renewables CM (Stage 40 §A depth).
  - 2.11.2 Transportation — position/angle/speed, traction current, e-compass, aerospace/space (Stage 40 §B depth). *Fig.:* EV sensor map (~15 magnetic sensing points on one vehicle).
  - 2.11.3 Industrial & Manufacturing — MFL/eddy-current NDT, stray-flux condition monitoring, encoders/robotics (Stage 40 §C depth).
  - 2.11.4 Biomedicine — MEG/MCG, biosensors/lab-on-chip, MPI, instrument tracking (Stage 40 §D depth). *Fig. (alternate):* biomagnetic amplitude-vs-frequency chart with family noise floors overlaid.
  - *Table 2:* family × domain deployment matrix (established / emerging / unsuited) — the paper's most quotable artifact (skeleton exists in Stage 40 §E).

**3. Future Applications and Methods (~28%)**
- 3.1 Data-Driven Modeling of Magnetic Sensors — learned calibration & calibration transfer; temperature/aging drift compensation; offset & 1/f mitigation; soft/virtual sensing & inverse modeling; which families gain most.
- 3.2 Machine-Learning Readout and Control — ML/Bayesian quantum-sensor readout (NV flagship); DL denoising for classical sensors; adaptive biasing & closed-loop compensation (honest: demonstrated closed loop is model-based, not learned); anomaly detection / predictive maintenance. *Fig.:* classical vs. learning-augmented readout chain with insertion points.
- 3.3 Sensor Fusion, Arrays, and Multi-Modality — magnetic + inertial; magnetic-field SLAM; MagNav; gradiometers & array signal processing (tSSS); source localization as fusion.
- 3.4 Digital Twins Built on Magnetic Sensing — model-vs-twin criterion; machine twins (demonstrated) vs. sensor twins (outlook); the review's most conservative-citation zone.

**4. Commercial Potential and Industry Standards (~28%)**
- 4.1 Technology Readiness and Market Landscape by Family — TRL ladder (labeled as the authors' assessment); market ranges with attribution; M&A/IP signals. *Fig.:* TRL-vs-market-pull map.
- 4.2 Functional Safety and Automotive Qualification ("standards as market gates" voice) — ISO 26262/ASIL, SEooC, redundancy/diagnostics; IEC 61508 parentage; ISO 21448 SOTIF; ISO/SAE 21434; emerging ISO/PAS 8800 & ISO/IEC TR 5469 (the ML-qualification frontier); CISPR 25 / ISO 11452 EMC.
- 4.3 Industrial and Energy-Sector Standards — IEC 61508, IEC 62443, EMC/instrument-transformer context.
- 4.4 Medical Device Pathways — IEC 60601-1, ISO 13485, ISO 14971, FDA 510(k)/CE framing with the Ricoh MEG clearance as the concrete exemplar.
- 4.5 Metrology and Traceability — NIST/PTB references, NMR-based absolute standards, uncertainty budgets; what happens when a learned model enters the chain.
- 4.6 What a Company or Investor Should De-Risk — the seven-question diligence checklist (Stage 60 §B.4), sourced facts explicitly separated from framing.

**5. Conclusion (~6%)** — the trade-space has no universal winner; the frontier is systems + computation, not raw sensitivity alone; open challenges per family and cross-cutting; outlook to 2030.

**Balance check:** 1: 7% · 2: 31% · 3: 28% · 4: 28% · 5: 6% — honors the author's "three roughly equal middle thirds."

---

## 3. Section-by-section annotated brief

The scaffold to write from. Each entry: what the retrieved literature actually supports, with registry keys inline. Honesty flags carried from the stage briefs are preserved — do not silently upgrade them while drafting.

### Section 1 — Introduction
The framing literature is strong and classic: the technology-vs-field-range map goes back to Lenz [Lenz1990review; Lenz2006magsensors], updated by the cross-family surveys [Ripka2010advancesIEEE; Tumanski2013modern; MagSensorsReview2021ERX] and the biomedical sensitivity comparison [Murzin2020biomedsensors]. The trade-space argument (no single family covers fT→tens-of-T across bandwidth, SWaP-C, and temperature) is directly supportable from those surveys plus the family-level anchors in Section 2. Fig. 1 (capability map) can be populated honestly from Stage 30's comparison table — but only its sourced cells; several bandwidth cells are still "n/r" (see gap matrix), so draw envelopes only where a number exists. The author's own AlGaN/GaN-in-HSX example may be mentioned in §1.2 as a harsh-environment motivation **only after the self-citation is inserted manually** — the 2023 *IEEE Sensors Letters* record was [UNVERIFIED] this run and must not be reconstructed (Stage 30 integrity note). Scope statement and exclusions are decided (Stage 20 A-1.2); the method paragraph should state the ~5-year state-of-the-art window plus classics, per `PROJECT_BRIEF.md` §7.

### Section 2 — Sensor technologies + current applications
**Maturity: the strongest section.** All 15 planned families are covered with principle, envelope, strengths/weaknesses, maturity, and pioneering directions (Stage 30), each anchored to at least one authoritative source: Hall [Popovic2004hallbook; Munter1990spinning; Crescentini2022hallcurrent; Alpert2020gan2deg], xMR [Jogschies2015mrindustrial; Freitas2016spintronic; Zhou2022TMRchapter; Zheng2019mrroadmap; Egelhoff2009picoteslaMTJ; TMRsubpT2025APL], fluxgate [Ripka2003fluxgateadv; Fluxgate2021Sensors; Dressler2021orthofluxgate], search-coil [Tumanski2007inductioncoil; Roux2008themisSCM; Coillot2010dualband], GMI [Phan2008gmiprogress; Dolabdjian2016gmichapter; Uchiyama2020picoteslaMI], SQUID [Fagaly2006squidRSI; Clarke2018squidfocus], OPM [Kominis2003subfemtotesla; Shah2007microfabvapor; Tierney2019OPM; Boto2018wearableMEG; Kitching2018chipscaleatomic], NV [Barry2020NVdiamond; NVsub10pT2024prapplied], ME [Bichurin2021MEreview; Li2017nemsME; Nan2013selfbiasME], MEMS Lorentz [HerreraMay2009memsresonant], fiber-optic [Rostami2023fbgreview; Silva2012opticalcurrent], Overhauser/CPT [Ge2016overhauser; Kitching2018chipscaleatomic].
The applications tail is equally well anchored per domain (Stage 40): energy current sensing [Crescentini2022hallcurrent; Khawaja2017overheadlines; Chen2024contactlessOHL; Xu2025TMRsmartgrid; Silva2012opticalcurrent], transportation [Treutler2001automotive; Miles2016fluxgateCubeSat], industrial NDT/CM [Rifai2016GMReddyreview; Bailey2017eddyCUI; Mazaheri2022strayflux], biomedical [Hamalainen1993meg-adjacent via §3; Brisinda2023clinicalMCG; Iwata2024bedsideMCG; Brickwedde2024OPMMEG; Pedersen2022OPMepilepsy; Wang2024magbiosensorPOCT; Wu2019MPIneuro; He2025EMtracking].
**Weak spots to respect while drafting:** (i) several Table 1 cells are still "n/r" — notably Hall noise floor in T/√Hz, AMR/GMR detectivity spectra, SERF bandwidth — fill only from the cited full texts, never from memory; (ii) ~8 numbers carry "(confidence: med)" flags (abstract-level retrieval) listed in Stage 30's gap list — re-verify each before it appears in prose; (iii) vendor numbers (TMR current-sensor 10 MHz/50 ns [AllegroTMRcurrentVendor], angle ±0.6° [MDTangleVendor], encoder 23-bit [MDTencoderVendor], GEM Overhauser specs [GEMOverhauserVendor]) stay `[VENDOR]`-tagged in the text. The strongest narrative thread to carry forward: **TMR is the common challenger in all four domains** (Stage 40 §F.1) — it links Section 2 to Sections 3–4.

### Section 3 — Future applications and methods
**Maturity: good, and honest — the labeling discipline is the section's asset.** Every thread has at least one peer-reviewed anchor: learned calibration [Kok2016magcal; Shetty2026AMRcalibNN; Karniadakis2021piml], soft sensing/inversion [Kadlec2009softsensor; Khawaja2017overheadlines; Chen2024contactlessOHL; Hamalainen1993meg], ML quantum readout [Santagati2019fieldlearning; Zhang2024dnnNVreadout; Homrighausen2023edgeNV; Jauch2026mlquantmag — cite for existence only], DL denoising [Sakib2022mcgedgeDL], closed-loop nulling [Holmes2018biplanarnulling], stray-flux ML diagnostics [Louzada2025strayfluxML; Mazaheri2022strayflux], fusion/SLAM [KokSolin2018magslam; Viset2022ekfmagslam; Taulu2006tsss], digital twins [Wright2020modeltwin; Glaessgen2012dtparadigm; Tao2019dtindustry; Rasheed2020dtenablers; Falekas2021dtmachines; EnergiesDT2025faultdiag].
**The section's load-bearing honesty (keep verbatim in spirit):** hardware still owns offset/1/f (no learned method replaces spinning/chopping at the front end); demonstrated closed-loop compensation is model-based, not learned; "ML-adaptive biasing" is an outlook sentence, not a capability; sensor-level digital twins are aspirational (machine-level twins are the demonstrated case); learned *aging* compensation has **no peer-reviewed anchor at all**. Everything tagged **(assessment)** in Stage 50 — including all TRL reads — must be presented as the authors' judgment in the prose. MagNav rests on a non-peer-reviewed AIAA paper [Gnadt2022magnavcal] plus preprints; quote no accuracy number without a journal-grade source.

### Section 4 — Commercial potential and industry standards
**Maturity: good; the fact/framing boundary is built in — preserve it.** The standards backbone is fully cited to issuing bodies: ISO 26262 [ISO26262], IEC 61508 [IEC61508], ISO 21448 [ISO21448SOTIF], ISO/SAE 21434 [ISOSAE21434], ISO/PAS 8800 [ISOPAS8800], ISO/IEC TR 5469 [ISOIECTR5469], IEC 62443 [IEC62443], CISPR 25/ISO 11452 [CISPR25; ISO11452], IEC 60601-1 [IEC60601], ISO 13485/14971 [ISO13485; ISO14971], with the metrology anchor peer-reviewed [Lenicek2022calibstd] plus PTB's BMSR-2 reference facility [PTBmetrology]. The standards table (Stage 60) converts directly into the manuscript's Section 4 table. Market content is grey-literature by nature and is handled correctly as attributed ranges: USD 3.03 B (2024) → 4.39 B (2030) per [GrandView2025magmarket] vs. higher figures elsewhere — report the spread, never average; TMR-growth and M&A signals from [Allegro2023crocus; TDK2016micronas] `[press]`; FDA-clearance exemplar [RicohMEG2024clearance] `[press]`. The TRL ladder and the seven-question risk register are **(assessment)** and must say so. The section's thesis — qualification + traceability are the two commercial gates, and both strain when a learned model enters the sensing chain — ties Sections 3 and 4 together and is the paper's most distinctive claim; its standards-side evidence ([ISOPAS8800; ISOIECTR5469; Salay2018ISO26262ML `[PREPRINT]`; Wright2020modeltwin]) is current as of this run but **must be re-checked near submission** (both AI-safety documents are 2024-vintage and moving).

### Section 5 — Conclusion
Synthesis only; no new sources needed. Three closing moves are already earned by the material: (1) the trade-space has no universal winner — the comparison table is the proof; (2) the frontier is computation + systems (TMR's cross-domain rise, cryogen-free biomagnetics, the computed sensor) rather than raw sensitivity; (3) the open-challenges list falls out of Stage 50's cross-cutting problems (data scarcity/benchmarks, distribution shift, trust/qualification, metrological standardization of the computed sensor) — each already sourced or explicitly assessment-labeled.

---

## 4. Coverage / gap matrix

Legend: **Done** = citable at submission grade · **Thin** = anchored but needs a number re-verified, a full-text extraction, or one more source · **Missing** = no usable anchor retrieved yet. Columns: principle covered / performance envelope sourced / current applications sourced / future-methods angle sourced / standards-business touched.

| Family | Principle | Performance | Current apps | Future angle | Standards/TRL | The specific gap |
|---|---|---|---|---|---|---|
| Hall (Si CMOS) | Done | **Thin** | Done | Done | Done | Noise floor in T/√Hz n/r — extract from [Crescentini2022hallcurrent] full text; 45 µT/600 kHz figure is med-confidence [JEET2019lownoisehall] |
| Hall (GaN/2DEG) | Done | **Thin** | **Thin** | **Thin** | Done | No noise-floor/bandwidth numbers; author self-citation [UNVERIFIED — insert manually]; spinning-current-on-GaN rests on an arXiv preprint (find VoR) |
| AMR | Done | **Thin** | Done | Done | Done | Detectivity spectra qualitative only — extract pT–nT/√Hz tables from [Zheng2019mrroadmap] full text |
| GMR (spin-valve) | Done | **Thin** | Done | Done | Done | Same [Zheng2019mrroadmap] extraction; field-range/bandwidth cells n/r |
| TMR / MTJ | Done | Done | Done | Done | Done | Strongest row; only the 97 pT/√Hz @10 Hz hybrid figure is med-confidence — re-verify or lean on [Egelhoff2009picoteslaMTJ; TMRsubpT2025APL] |
| Fluxgate | Done | **Thin** | Done | **Thin** | Done | FM-OFG 0.3–0.75 pT/√Hz attribution is med-confidence — pin to [Dressler2021orthofluxgate] full text; no ML/data-driven fluxgate thread found |
| Search-coil | Done | Done | Done | Done | **Thin** | Instrument-transformer/EMC standards named only generically — cite the specific IEC part at drafting |
| GMI | Done | **Thin** | Done | **Missing** | **Thin** | MEMS-GMI numbers med-confidence, DOI unverified; no ML-for-GMI literature retrieved; narrow supplier base noted but unsourced beyond [Phan2008gmiprogress] |
| SQUID | Done | Done | Done | Done | Done | MCG amplitude context figures (50–100 pT) med-confidence — restate from [Clarke2018squidfocus] full text |
| OPM / SERF | Done | **Thin** | Done | Done | Done | SERF bandwidth & dynamic-range numbers n/r — extract from [Tierney2019OPM] full text |
| NV-diamond | Done | Done | **Thin** | Done | **Thin** | Current-sensing application rests on a preprint [NVcurrentPPM2023] — find VoR or soften; no qualification-pathway discussion beyond supply-chain note |
| Magnetoelectric | Done | **Thin** | **Thin** | **Missing** | **Missing** | 6 pT/√Hz figure med-confidence; lab-only (no vendor found — re-check at drafting); no future-methods or standards angle |
| MEMS Lorentz | Done | **Thin** | **Thin** | **Missing** | **Missing** | Resolution figures med-confidence; no volume product; no ML/standards thread — acceptable if kept short (Stage 20 gives it one paragraph) |
| Fiber-optic / magneto-optic | Done | **Thin** | Done | **Missing** | **Thin** | Noise floors in tesla units n/r (family specified in pm/mT); IEC 61850-9-2 digital-substation context named but the standard itself not in the registry |
| Proton / Overhauser / CPT | Done | **Thin** | Done | **Missing** | Done | Performance numbers are `[VENDOR]`-only [GEMOverhauserVendor] — a peer-reviewed spec source would upgrade; "future angle" is by design (they are the traceability anchors) |

**Cross-cutting reading of the matrix:** the taxonomy's principle and applications columns are essentially done; the systematic weakness is **performance-number verification** (one full-text extraction pass over sources already in the registry closes most Thin cells) and the **future/standards columns of the minor families** (GMI, ME, MEMS, fiber-optic, Overhauser) — the latter are acceptable to leave thin given their planned one-paragraph treatment, but say so deliberately rather than by omission.

### Top ~10 highest-value sources still worth adding

1. **The author's own 2023 *IEEE Sensors Letters* AlGaN/GaN-in-HSX paper** — [UNVERIFIED] this run; the author holds the citation and must insert it manually (Stage 30 rule: nobody else reconstructs it). Blocks the §1.2 motivation example and the GaN pioneering paragraph.
2. **Version of record for NV current sensing** (arXiv:2304.07998, 46 ppm / 0–1000 A) — Stage 70 confirmed no VoR as of this run; search again near drafting, else soften to "demonstrated in preprint literature."
3. **Version of record for spinning-current offset cancellation on AlGaN/GaN** (arXiv:1812.00363) — needed for the GaN future-directions paragraph.
4. **A peer-reviewed ISO 26262 + ML safety analysis** to replace or back the [Salay2018ISO26262ML] preprint — the ML-qualification thesis currently leans on grey literature at exactly its most-quoted point.
5. **A journal-grade MagNav accuracy source** — every navigation-accuracy figure currently traces to a non-peer-reviewed AIAA paper [Gnadt2022magnavcal] and preprints.
6. **A peer-reviewed learned-aging-compensation paper for magnetometers** — Stage 50 found none; if a fresh search still finds none, the paper states it as an open gap (which is itself a contribution).
7. **A peer-reviewed magnetic-sensor digital-twin demonstration** — none retrieved; same treatment as (6).
8. **A peer-reviewed analysis of stray-field-robust / redundant ASIL sensor architectures** — Section 4.2's device-architecture claim currently rests on a vendor exemplar [TDK2016micronas].
9. **[Jauch2026mlquantmag] full text** — Crossref-verified but unread (publisher 403); currently citable only for existence.
10. **IEC 61850-9-2** (digital-substation interface) as a registry entry — named in Stage 40 §A.3 but never captured; plus the four missing standards webstore URLs (IEC 60601-1, ISO 13485, CISPR 25, ISO 11452) from Stage 60.

### Claims currently resting on preprints / grey literature that need a peer-reviewed anchor (or explicit softening)

| Claim | Current source | Action |
|---|---|---|
| NV current sensing: 0–1000 A, ~46 ppm, galvanically isolated | [NVcurrentPPM2023] `[PREPRINT]` | Find VoR (item 2) or present as preprint-stage with tag |
| ISO 26262's assurance model breaks for learned components | [Salay2018ISO26262ML] `[PREPRINT]` | Find peer-reviewed successor (item 4); ISO/PAS 8800's existence [ISOPAS8800] partially carries the point |
| MagNav accuracy "tens of meters" | [Gnadt2022magnavcal] (non-PR conference) + [PGTLNet2024preprint] | Quote no number until a journal source exists (item 5) |
| Magnetometer-array odometry/SLAM-with-calibration | [SLCAMma2026preprint] | Cite only as "emerging direction" atop peer-reviewed SLAM anchors [KokSolin2018magslam; Viset2022ekfmagslam], or drop |
| Market size / CAGR / Hall share / TMR 30% CAGR | [GrandView2025magmarket; MRFRautomotivemarket] `[market-report]`, [Allegro2023crocus] `[press]` | No peer-reviewed substitute exists — keep as attributed, ranged estimates (already the Stage 60 discipline) |
| Traction-inverter "Hall ~48.5% share in 2025" | `[MARKET]`, unpinned | Replace with qualitative "Hall dominant, TMR fastest-growing" unless a primary source appears (Stage 40 gap 1) |
| Vendor device specs (TMR 10 MHz/50 ns; ±0.6° angle; 23-bit encoder; GMR ">50× Hall"; Overhauser 0.2 nT) | `[VENDOR]` datasheets/pages | Keep, tagged `[VENDOR]` — legitimate for commercial device facts, never as peer-reviewed evidence |

---

## 5. Journal-fit checklist (vs. `00_target_journal_brief.md`)

| Requirement | Status |
|---|---|
| Article type: narrative review acceptable; no PRISMA demanded | ✅ Satisfied by design |
| Structure: numbered headings ≤3 levels, Introduction→Conclusions | ✅ Recommended outline complies (deepest level is 2.11.4 / 4.1-style x.y.z) |
| Abstract: single paragraph, ~200–250 words, self-contained | ⬜ **Not yet drafted** — write at manuscript stage; state problem/scope/method/findings/implication in one block |
| Keywords: 3–5 immediately after abstract | ⬜ **Not yet chosen** — suggested set: *magnetic sensors; Hall effect; magnetoresistance; machine learning; digital twin* (5) |
| In-text citations: bracketed numerals before punctuation, e.g. [4], [1–3] | ✅ Convention locked in all stage briefs; Stage 70/80 registry → numbered conversion at assembly |
| Reference list: MDPI/ACS style; ISO 4 abbreviations; one-word titles (*Sensors*) NOT abbreviated; DOI wherever it resolves | ◐ `references.bib` + registry exist, DOIs verified; **10 entries have blank author fields** (listed in Stage 70) and [Tumanski2013modern] has no DOI (confirmed none exists) — fill authors from DOI landing pages before submission |
| Standards cited as corporate-author references | ✅ Format defined in journal brief §4 and used in the registry |
| Figures: legend before figure; color free. Tables embedded with numbers/titles | ⬜ **No figures/tables produced yet** — planned: Fig. 1 capability map, taxonomy tree, EV sensor map or biomagnetic chart, readout-chain diagram, TRL-vs-market map; Table 1 master comparison (skeleton in Stage 30), Table 2 family×domain matrix (skeleton in Stage 40), standards table (near-final in Stage 60) |
| Back matter: Author Contributions → Funding → Acknowledgments → Conflicts of Interest → Abbreviations → References (no IRB/data-availability needed) | ⬜ **Not yet drafted** — mechanical; do at assembly |
| **AI-disclosure line in Acknowledgments** (tool, version, purpose) — mandatory given this workflow | ⬜ **Must not be forgotten** — template wording is in the journal brief §7 |
| Length: no cap, "concise and comprehensive" | ✅ Long review acceptable |
| Word template (.dot) for submission | ⬜ Convert from Markdown at final assembly (out of scope for this run) |
| APC ~CHF 2600 (2026 schedule); ~17.8 days to first decision | ✅ Noted; re-verify APC at submission |
| Timeline vs. 30 Oct 2026 | ✅ No blocker — journal turnaround is fast relative to target; manuscript drafting is the critical path |

**Summary:** everything structural is decided and compliant; nothing that requires the journal has been violated. The open items are all manuscript-assembly work (abstract, keywords, figures/tables, back matter, AI disclosure, Word conversion) plus the bibliography's blank-author cleanup.

---

## 6. Suggested next patches (ordered by value)

1. **`.\run.ps1 -OnlyStage 30 -Force`** — with the prompt pointed at the Stage 30 gap list: full-text extraction of the med-confidence and n/r numbers (Zheng2019 detectivity spectra, Crescentini Hall noise/bandwidth, Tierney SERF bandwidth/dynamic range, Dressler FM-OFG attribution, Clarke MCG amplitudes, Bichurin ME figure, HerreraMay MEMS figures, Rostami FBG figure). This single pass converts most **Thin** performance cells to **Done** using sources already in the registry.
2. **`.\run.ps1 -OnlyStage 50 -Force`** — version-of-record hunt: NV current sensing (arXiv:2304.07998), GaN spinning-current (arXiv:1812.00363), a peer-reviewed ISO26262+ML analysis, a journal-grade MagNav accuracy source, learned-aging compensation (confirm gap), sensor-twin demonstration (confirm gap), and the [Jauch2026mlquantmag] full text.
3. **`.\run.ps1 -OnlyStage 70 -Force`** — bibliography hygiene: fill the 10 blank author lists from DOI landing pages, resolve the four missing standards URLs (IEC 60601-1, ISO 13485, CISPR 25, ISO 11452), add IEC 61850-9-2 as a registry entry, and re-check ISO/PAS 8800 / ISO/IEC TR 5469 status.
4. **Manual (author, 5 minutes):** insert the 2023 *IEEE Sensors Letters* self-citation into the registry and Stage 30 §1.2 — nobody else can do this safely.
5. **Optional, pre-submission (October 2026):** re-run Stage 00 to refresh APC, Special-Issue list, and the AI-authorship policy; and re-check the market figures' vintage in Stage 60 — grey-literature market numbers age fast.

---

*End of deliverable pack. Detailed evidence: `30_…`/`40_…`/`50_…`/`60_…`; bibliography state: `70_bibliography_report.md` + `reference_registry.csv` (122 refs, ~80 peer-reviewed journal, ~20% grey/preprint, all flagged).*
