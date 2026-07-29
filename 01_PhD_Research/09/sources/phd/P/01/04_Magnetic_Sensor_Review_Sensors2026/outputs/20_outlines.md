# Stage 20 — Candidate outlines for the magnetic-field-sensors review

Target: MDPI *Sensors*, review article, submission before 30 Oct 2026.
All four outlines honor the author's five-part plan (Introduction; Sensor
types + current applications; Future applications; Potential + standards;
Conclusion) with the three middle parts near a third each. They differ only
in how the middle is ORGANIZED. Headings follow MDPI numbered style (up to
three levels, per `00_target_journal_brief.md`). Sensor-family shorthand:
Hall (Si/CMOS + GaN 2DEG), AMR/GMR/TMR (xMR), fluxgate, search-coil, GMI,
SQUID, OPM/SERF, NV-diamond, magnetoelectric (ME), MEMS/Lorentz-force,
fiber-/magneto-optic, NMR/Overhauser. Domains: energy (EN), transportation
(TR), industrial & manufacturing (IN), biomedicine (BM).

No external sources were consulted at this stage (structure design only), so
no new entries were added to `refs_raw/`.

---

## Outline A — Sensor-family-primary (taxonomy backbone)

Section 2 walks the device families one by one — each with principle,
performance envelope, strengths/weaknesses box, maturity, and typical
domains — then closes with a cross-cutting applications subsection and the
master comparison table. This is the structure that maps 1:1 onto
`PROJECT_BRIEF.md` §3–§4.

### 1. Introduction (~7%)
**1.1. Why Magnetic Sensing Matters**
- The ubiquity argument: magnetic fields as a contact-free proxy for
  current, position, motion, material state, and physiology; one measurand,
  four industries (EN/TR/IN/BM).
- The measurement problem as a trade-space: field range vs. resolution vs.
  bandwidth vs. size/power/cost/temperature; why no single family wins.
- *Fig. 1:* field-strength landscape — geomagnetic, biomagnetic (fT–pT),
  industrial/automotive (µT–T) regimes on one log axis, annotated with the
  families that reach each regime.

**1.2. Scope, Method, and Contributions of This Review**
- Vendor-neutral narrative review; commercial + pioneering families;
  current applications in four domains; future methods; standards/TRL for a
  dual technical + business/investor readership.
- What is excluded (single-application deep dives, magnet design,
  full geophysics/space survey) and why.

**1.3. Organization of the Paper**
- One paragraph mapping Sections 2–5; pointer to the comparison table and
  the family × domain matrix as the reader's navigation aids.

### 2. Magnetic-Field Sensor Technologies and Their Current Applications (~31%)
**2.1. Figures of Merit and Taxonomy**
- Definitions used throughout: noise floor (pT/√Hz), dynamic range,
  bandwidth, offset & drift, linearity, power, cost tier, maturity class
  (mass-market / niche / lab-only).
- The commercial-vs-pioneering axis as the section's organizing contrast.
- *Fig.:* taxonomy tree of the families covered in 2.2–2.10.

**2.2. Hall-Effect Sensors**
- Principle; Si CMOS integration; spinning-current offset cancellation;
  wide-bandgap GaN/2DEG variants for temperature/radiation-harsh use.
- Strengths/weaknesses box: linear to large fields, cheap, integrable vs.
  offset/1/f noise, modest sensitivity. Typical domains: TR (position,
  commutation), EN (current), IN (proximity).

**2.3. Magnetoresistive Sensors: AMR, GMR, and TMR**
- Physics ladder AMR → GMR spin-valve → TMR/MTJ; MR ratio, bridge
  configurations, set/reset and flipping.
- Strengths/weaknesses box: sensitivity and low power (TMR) vs. hysteresis,
  saturation, ESD/annealing limits. Typical domains: TR (angle, wheel
  speed), IN (encoders), EN (current), BM (biosensor arrays).

**2.4. Fluxgate Magnetometers**
- Core saturation principle; parallel/orthogonal gate; digital fluxgates.
- Strengths/weaknesses box: nT-class accuracy and stability vs. size,
  power, bandwidth. Typical domains: EN (dc metering, grid), navigation,
  space heritage.

**2.5. Search-Coil / Induction Sensors**
- Faraday-law ac sensing; air-core vs. cored; Rogowski relatives for
  current.
- Strengths/weaknesses box: passive, wideband ac vs. no dc response, size
  scaling. Typical domains: IN (eddy-current NDT), EN (ac current),
  geophysics context.

**2.6. Giant Magnetoimpedance (GMI) Sensors**
- Skin-effect impedance modulation in amorphous wires/ribbons; MHz
  excitation readout.
- Strengths/weaknesses box: high sensitivity at low power vs. nonlinearity,
  fabrication spread, limited vendor base. Typical domains: BM (emerging
  biomagnetics), IN, e-compass.

**2.7. SQUID Magnetometers**
- dc/rf SQUID principle; LTS vs. HTS; cryogenic infrastructure.
- Strengths/weaknesses box: fT-class ultimate sensitivity vs. cryogenics,
  cost, shielded rooms. Typical domains: BM (MEG/MCG gold standard), IN
  (NDE niche), metrology.

**2.8. Optically Pumped Magnetometers (OPM / SERF)**
- Alkali-vapor principle; SERF regime; scalar vs. vector variants;
  wearable-array packaging.
- Strengths/weaknesses box: cryogen-free fT–pT sensitivity vs. bandwidth,
  dynamic range, zero-field operation needs. Typical domains: BM (wearable
  MEG/MCG/fetal), magnetic navigation, surveys.

**2.9. NV-Diamond Magnetometry**
- NV-center ODMR principle; ensembles vs. single centers; vector capability
  and spatial resolution.
- Strengths/weaknesses box: room-temperature quantum sensing, µm-scale
  imaging, wide dynamic range vs. photon-budget sensitivity limits, system
  complexity, TRL. Typical domains: EN (battery/current diagnostics), BM
  (imaging), IN (materials).

**2.10. Other Emerging Families**
- Magnetoelectric composites; MEMS/Lorentz-force resonators; fiber-optic /
  magneto-optic sensors; NMR/Overhauser scalar standards.
- One strengths/weaknesses paragraph each, with maturity and pioneering
  direction; which niches they could unlock (passive sensing, EMI-immune
  links, absolute calibration).

**2.11. Cross-Cutting Comparison and Current Applications in the Four Domains**
- *Table 1 (master):* family × {range, resolution/noise floor, bandwidth,
  temperature behavior, power, cost tier, maturity, representative
  devices/vendors} — sourced numbers only.
- 2.11.1 Energy; 2.11.2 Transportation; 2.11.3 Industrial & Manufacturing;
  2.11.4 Biomedicine — each ~1 page: concrete deployments, which family is
  used and why it fits the domain's constraint set.
- *Table 2:* family × domain deployment matrix (established / emerging /
  unsuited), the paper's single most quotable artifact.

### 3. Future Applications and Methods (~28%)
**3.1. Data-Driven Modeling of Magnetic Sensors**
- Learned calibration and calibration transfer; temperature/aging drift
  compensation; offset and 1/f-noise mitigation; soft/virtual sensing.
- Which families gain most (Hall/xMR offset & drift; OPM/NV readout).

**3.2. Machine-Learning Readout and Control**
- ML denoising and fast state estimation (incl. quantum-sensor readout);
  adaptive biasing; closed-loop compensation; anomaly detection feeding
  predictive maintenance (IN/EN).
- *Fig.:* block diagram — classical readout chain vs. learning-augmented
  chain, annotated with insertion points.

**3.3. Sensor Fusion, Arrays, and Multi-Modality**
- Magnetic + inertial/optical/thermal fusion; gradiometer and dense arrays;
  array signal processing; source localization (BM MEG/MCG, TR navigation,
  IN NDT imaging).

**3.4. Digital Twins Built on Magnetic Sensing**
- Twin of the sensor (calibration state, health) vs. twin of the asset
  (motor, grid, battery, patient-adjacent); design optimization loops.
- Honest maturity assessment: what is demonstrated vs. proposed —
  the review's most conservative-citation zone.

### 4. Commercial Potential and Industry Standards (~28%)
**4.1. Technology Readiness and Market Landscape by Family**
- TRL ladder per family; market segments by domain; labeled market-size
  estimates from cited analyses; IP/patent-activity signals.
- *Fig.:* TRL-vs-market-pull map (families as points).

**4.2. Functional Safety and Automotive Qualification**
- ISO 26262/ASIL for position & current sensors; IEC 61508 parentage;
  ISO/PAS 21448 (SOTIF); ISO/SAE 21434; redundancy/diagnostics, SEooC;
  AEC-Q100 context.

**4.3. Industrial and Energy-Sector Standards**
- IEC 61508 in OT; IEC 62443 security; relevant IEC/IEEE sensor,
  instrument-transformer, and EMC standards for grid/inverter sensing.

**4.4. Medical Device Pathways**
- IEC 60601, ISO 13485, ISO 14971; FDA/CE framing for OPM-MEG, MPI, and
  magnetic biosensor products.

**4.5. Metrology and Traceability**
- NIST/PTB field standards, NMR-based absolute references, uncertainty
  budgets, calibration services — why traceability is a purchase criterion.

**4.6. What a Company or Investor Should De-Risk**
- Checklist synthesis: supply chain (He-3-free, cryogen-free, diamond
  supply), qualification cost, single-vendor exposure, standards gaps for
  pioneering families. Clearly labeled framing vs. sourced fact.

### 5. Conclusion (~6%)
- Synthesis: the trade-space has no universal winner; the frontier is
  systems + intelligence, not raw sensitivity alone.
- Open challenges list (per family and cross-cutting); outlook to 2030.

**Balance:** 1: 7% · 2: 31% · 3: 28% · 4: 28% · 5: 6%.

**Best when...** The author wants the review cited as the reference
taxonomy — readers arrive asking "which sensor should I use?" and Section 2
answers it directly; it also tracks `PROJECT_BRIEF.md` §3–§4 with the least
re-mapping, making Stages 30–40 briefs drop in almost unchanged. Tradeoff:
the four domains get compressed into 2.11, so applications read as a tail
rather than a co-equal story, and domain-specific readers must self-serve
via Table 2.

---

## Outline B — Application-primary (domain backbone)

Section 2 is organized by the four domains; a compact device primer and the
consolidated comparison table come first so each domain section can name
families without re-deriving them. Emphasizes deployments and buyer
context over device physics.

### 1. Introduction (~7%)
**1.1. Magnetic Sensing as Cross-Industry Infrastructure**
- Four domains, one measurand; economic footprint of magnetic sensing in
  EN/TR/IN/BM; why domain constraints (safety, temperature, cost, biology)
  drive device choice more than raw specs.
**1.2. The Measurement Trade-Space**
- Range/resolution/bandwidth/SWaP-C/temperature axes; *Fig. 1:* capability
  landscape (same artwork as A-1.1 figure).
**1.3. Scope, Method, and Organization**
- Review method, inclusion window (~5-year SOTA + classics), roadmap.

### 2. Sensor Technologies in Their Application Domains (~31%)
**2.1. Device Primer and Consolidated Comparison**
- Two-to-three-paragraph capsule per family group (Hall; xMR; fluxgate /
  search-coil / GMI; SQUID / OPM / NV; ME / MEMS / optical / NMR): principle
  in two sentences, envelope, maturity.
- *Table 1 (up front):* the master family comparison table — placed here so
  all domain sections reference it.

**2.2. Energy**
- 2.2.1 Current sensing in power electronics and inverters (Hall, TMR,
  search-coil/Rogowski; isolation and bandwidth drivers).
- 2.2.2 Smart grid and substation monitoring (fluxgate dc metering, optical
  CTs, xMR retrofit sensing).
- 2.2.3 Battery management and EV pack sensing (shunt-vs-magnetic tradeoff,
  Hall/TMR pack current, SoC support; NV battery diagnostics as pioneer).
- 2.2.4 Renewables condition monitoring (wind-turbine drivetrain, MFL in
  cabling). *Fig.:* inverter/BMS sensing points diagram.

**2.3. Transportation**
- 2.3.1 Position, angle, and speed (steering, throttle, ABS wheel speed,
  BLDC/EV commutation — Hall vs. TMR displacement of Hall).
- 2.3.2 Traction-inverter and charging current sensing (Hall, TMR, core vs.
  coreless).
- 2.3.3 Navigation and e-compass; rail and aerospace (AMR/fluxgate,
  magnetic anomaly context). *Fig.:* sensor map of an EV (one vehicle,
  ~15 magnetic sensing points).

**2.4. Industrial and Manufacturing**
- 2.4.1 NDT: eddy-current and MFL pipeline/tank inspection (search-coil,
  GMR arrays, SQUID/NV niche imaging).
- 2.4.2 Motor, bearing, and process condition monitoring; predictive
  maintenance signals.
- 2.4.3 Robotics, encoders, proximity/position, process metrology
  (Hall/xMR encoders; safety-rated position).

**2.5. Biomedicine**
- 2.5.1 MEG and MCG: SQUID installed base vs. wearable OPM arrays; TMR/GMI
  attempts at room-temperature biomagnetics.
- 2.5.2 Magnetic particle imaging and magnetogenetics-adjacent tools.
- 2.5.3 GMR/TMR biosensors and lab-on-chip; catheter/instrument tracking;
  wearables. *Fig.:* biomagnetic amplitude-vs-frequency chart with family
  noise floors overlaid.

**2.6. Cross-Domain Synthesis**
- *Table 2:* domain × requirement × chosen family matrix; recurring
  patterns (isolation, temperature, safety rating) that explain family
  wins across domains.

### 3. Future Applications and Methods (~28%)
**3.1. Data-Driven Calibration and Drift Compensation** — as A-3.1, but each
method tagged with the domain that pulls it (e.g., BMS drift → EN).
**3.2. ML Readout, Control, and Predictive Analytics** — denoising/fast
readout; anomaly detection as the IN/EN bridge; ASIL-relevant ML caveats.
**3.3. Fusion, Arrays, and Multi-Modality** — MEG source localization (BM),
magnetic+inertial navigation (TR), array NDT (IN).
**3.4. Digital Twins per Domain** — grid/motor/battery twins (EN/IN),
vehicle sensor twins (TR), patient/device twins (BM); maturity flags.

### 4. Commercial Potential and Industry Standards (~28%)
Same subsections as A-4.1–4.6, but 4.2–4.4 now inherit context from the
domain sections (each standard cites back to the deployments in 2.2–2.5),
and 4.1's market framing is per-domain first, per-family second.

### 5. Conclusion (~6%)
- Synthesis by domain: where each is on the adoption curve; open
  challenges; outlook.

**Balance:** 1: 7% · 2: 31% · 3: 28% · 4: 28% · 5: 6%.

**Best when...** The author wants maximum pull for applied and
business/investor readers — every stakeholder finds "their" section and the
standards chapter lands naturally because domains are already the frame; it
also pairs perfectly with title #2's explicit four-domain naming. Tradeoff:
device physics gets fragmented (TMR appears in all four domains), forcing
either repetition or heavy cross-referencing, and the taxonomy depth the
brief's §3 demands must be squeezed into primer 2.1 or an appendix-like
table.

---

## Outline C — Capability-envelope-primary (measurement-regime backbone)

Section 2 is organized by what must be measured — four performance regimes —
mapping families and domains onto each. The intellectual frame is the
trade-space itself; the comparison table becomes a capability map.

### 1. Introduction (~7%)
**1.1. One Measurand, Ten Orders of Magnitude**
- fT (brain) to tens of T (magnets): why the field spans regimes no single
  device covers; regime boundaries as the review's organizing principle.
- *Fig. 1 (the paper's signature):* capability map — field range vs.
  bandwidth plane with family envelopes drawn as regions and the four
  regimes of Section 2 shaded.
**1.2. Figures of Merit and How to Read the Map**
- Noise floor, dynamic range, bandwidth, drift; SWaP-C as a third axis;
  maturity encoding on the map.
**1.3. Scope, Method, and Organization**

### 2. Measurement Regimes: Families and Current Applications (~31%)
**2.1. Ultra-Sensitive Weak-Field Sensing (fT–pT)**
- Families: SQUID, OPM/SERF, NV ensembles, ME composites (aspiring).
- Applications: MEG/MCG and fetal biomagnetics (BM), magnetic anomaly and
  survey work, lab metrology.
- Strengths/weaknesses contrast: cryogenic vs. cryogen-free vs.
  room-temperature-quantum routes to the same floor. *Table:* weak-field
  contenders — noise floor, bandwidth, operating constraints, maturity.

**2.2. Precision DC and Vector Field Measurement (nT–µT)**
- Families: fluxgate, AMR, GMI, NMR/Overhauser (absolute reference).
- Applications: navigation/e-compass (TR), space and geomagnetic context,
  grid dc metering (EN), magnetic signature monitoring (IN).
- The accuracy/stability problem (offset, drift, calibration) as this
  regime's defining challenge.

**2.3. Robust Position, Angle, and Proximity Sensing (µT–mT, harsh
environments)**
- Families: Hall (Si + GaN), TMR/GMR encoders.
- Applications: automotive position/angle/speed and commutation (TR),
  robotics and encoders (IN), safety-rated proximity.
- Why "robust beats sensitive" here: temperature, EMC, cost, ASIL.

**2.4. High-Bandwidth Current and Power Sensing (µT–T equivalent, dc–MHz)**
- Families: Hall (core/coreless), TMR, search-coil/Rogowski, fiber-optic
  CTs.
- Applications: inverters and traction (EN/TR), BMS pack current (EN),
  wide-bandgap (SiC/GaN) converter demands on sensor bandwidth.

**2.5. Imaging, Arrays, and Spatially Resolved Sensing**
- Families: NV-diamond microscopy, GMR/TMR biosensor and eddy-current
  arrays, OPM arrays, MPI systems.
- Applications: NDT imaging (IN), lab-on-chip and MPI (BM), battery/current
  mapping (EN).
- Array signal processing as the shared enabler (bridge to Section 3.3).

**2.6. Regime Synthesis**
- *Table 1 (master comparison):* family rows, regime columns — where each
  family is best-in-class, usable, or excluded; domains annotated per cell.

### 3. Future Applications and Methods (~28%)
**3.1. Pushing the Envelope with Data-Driven Modeling** — learned
calibration/drift compensation framed as moving a family's envelope
(cheap Hall toward precision-dc; OPM toward higher bandwidth).
**3.2. ML Readout and Control** — fast quantum-sensor readout (regime 2.1),
adaptive biasing (2.2–2.3), converter-noise-aware current sensing (2.4).
**3.3. Fusion, Arrays, and Source Localization** — the regime-2.5 methods
generalized; multi-modality as envelope-stitching across regimes.
**3.4. Digital Twins of Sensors and Assets** — twin-assisted calibration
transfer as the long-term answer to regime 2.2's stability problem;
asset twins fed by regime 2.4/2.5 data.

### 4. Commercial Potential and Industry Standards (~28%)
**4.1. Maturity and Markets per Regime** — TRL and market pull mapped onto
the capability map (*Fig.: capability map redrawn with TRL shading*);
where investment concentrates (2.3/2.4 mass markets vs. 2.1/2.5 frontier).
**4.2–4.5.** Standards subsections as in A-4.2–4.5 (functional safety;
industrial/energy; medical; metrology) — each introduced by which regime it
governs.
**4.6. De-Risking the Frontier** — what moves a 2.1/2.5 technology into
2.3/2.4-style volume; qualification, supply chain, standards gaps.

### 5. Conclusion (~6%)
- The envelope picture restated: which boundaries are physics, which are
  engineering, which are being moved by ML/fusion; outlook.

**Balance:** 1: 7% · 2: 31% · 3: 28% · 4: 28% · 5: 6%.

**Best when...** The author wants the most intellectually distinctive
review — regime framing is rarer in the magnetic-sensor review literature
than family or application framing, and it gives the paper one signature
reusable figure (the capability map). Tradeoff: it is the hardest to
execute honestly (every envelope boundary needs a sourced number), some
families straddle regimes and get discussed twice, and business readers
must translate regimes back into their domain before Section 4 pays off.

---

## Outline D — Value-chain / TRL-primary (business-forward)

Section 2 climbs the value chain — devices → systems → deployments — with
maturity as the explicit sorting axis throughout; the four domains thread
through as deployment case studies. Standards and markets stop being an
appendix and become the destination the whole paper walks toward.

### 1. Introduction (~7%)
**1.1. From Physical Effect to Product**
- The claim: magnetic sensing value is created at three layers — element,
  system (readout/packaging/compensation), and deployment — and most
  failures of promising devices happen between layers.
- The dual-audience contract stated openly: specs for engineers, readiness
  signals for investors.
**1.2. The Trade-Space and the TRL Lens**
- Range/resolution/bandwidth/SWaP-C axes; TRL and maturity-class
  definitions used throughout. *Fig. 1:* value-chain schematic with the
  four domains as end columns.
**1.3. Scope, Method, and Organization**

### 2. The Magnetic Sensing Value Chain Today (~31%)
**2.1. Device Layer: Families by Maturity Tier**
- 2.1.1 Mass-market: Hall (Si CMOS, spinning-current), AMR/GMR/TMR —
  principle, envelope, strengths/weaknesses, representative vendors.
- 2.1.2 Established niche: fluxgate, search-coil, SQUID, GMI — same
  treatment; why each stays niche (power, cryogenics, fab spread).
- 2.1.3 Pioneering: OPM/SERF, NV-diamond, ME composites, MEMS/Lorentz,
  fiber-/magneto-optic — envelope plus the credible claim each makes.
- *Table 1 (master comparison):* families sorted by maturity tier, with
  range/resolution/bandwidth/cost/maturity/vendor columns.

**2.2. System Layer: From Element to Instrument**
- Readout and compensation: spinning current, chopping, closed-loop flux
  feedback, bridge conditioning, ASIC integration; packaging and
  temperature compensation; self-test/diagnostics as a safety enabler.
- Why the system layer decides commercial winners (TMR vs. Hall example:
  element superiority vs. ecosystem maturity).

**2.3. Deployment Layer: Four Domains as Case Studies**
- 2.3.1 Energy — inverter/BMS/grid deployments and who supplies them.
- 2.3.2 Transportation — position/angle/current at automotive volume;
  qualification as barrier to entry.
- 2.3.3 Industrial & manufacturing — NDT, condition monitoring, encoders;
  fragmented buyers, longer lifecycles.
- 2.3.4 Biomedicine — SQUID incumbency vs. OPM challengers; biosensors;
  the regulatory moat. Each ≤1.5 pages, family-annotated, cited
  deployments only. *Table 2:* domain × family deployment matrix with
  maturity coloring.

### 3. Future Methods as Value-Chain Upgrades (~28%)
**3.1. Device-Layer Upgrades: Data-Driven Modeling** — learned calibration,
drift/offset compensation, soft sensing; framed as raising yield and
cutting calibration cost, not only improving specs.
**3.2. System-Layer Upgrades: ML Readout and Control** — denoising, fast
readout, adaptive biasing, closed-loop compensation; anomaly detection as
a sellable feature (predictive maintenance).
**3.3. Deployment-Layer Upgrades: Fusion, Arrays, Multi-Modality** —
magnetic+inertial/optical/thermal fusion products; gradiometer arrays;
source localization as application enabler (BM/TR/IN).
**3.4. Digital Twins Across the Chain** — sensor twins (calibration state,
health) to asset twins (motor/grid/battery/patient pathway); demonstrated
vs. aspirational, conservatively cited. *Fig.:* value chain redrawn with
ML/twin insertion points from 3.1–3.4.

### 4. Standards, Markets, and Investment Signals (~28%)
**4.1. Standards as Market Gates**
- 4.1.1 Automotive/functional safety: ISO 26262 & ASIL, IEC 61508,
  ISO/PAS 21448, ISO/SAE 21434, SEooC, AEC-Q context.
- 4.1.2 Industrial: IEC 61508, IEC 62443, sensor/EMC/instrument-transformer
  standards.
- 4.1.3 Medical: IEC 60601, ISO 13485, ISO 14971, FDA/CE pathways.
- 4.1.4 Metrology: NIST/PTB traceability, absolute references, uncertainty
  budgets.
**4.2. Market Landscape and TRL per Family**
- Cited market analyses (estimates labeled); TRL ladder per family;
  IP/patent-activity signals. *Fig.:* TRL vs. addressable-market map.
**4.3. Risk Register for Adopters and Investors**
- Supply chain (cryogens, diamond, alkali cells, rare targets),
  qualification cost/time, single-source exposure, standards white space
  for pioneering families; sourced facts explicitly separated from framing.
**4.4. Where Value Accrues Next**
- Synthesis: which layer (device/system/deployment) captures margin per
  domain; the ML/twin methods of Section 3 as the differentiators to watch.

### 5. Conclusion (~6%)
- Restate the three-layer thesis; per-tier outlook (mass-market
  consolidation, niche persistence, pioneering inflection points); open
  challenges.

**Balance:** 1: 7% · 2: 31% · 3: 28% · 4: 28% · 5: 6%.

**Best when...** The business/investor audience is a first-class goal, not
a bolt-on — this is the only structure where the standards/market third
feels inevitable rather than appended, and Section 3's methods gain a "why
fund this" framing. Tradeoff: it is the least conventional shape for a
*Sensors* review, device physics per family is thinner (spread across
maturity tiers), and reviewers expecting a classical taxonomy may push back
on the business voice.

---

## Recommendation

**Pick Outline A, hybridized with B's domain depth in the applications
tail.** Concretely: keep A's family-by-family Section 2 (2.1–2.10, the
strengths/weaknesses boxes, and Table 1), but expand A-2.11 into four full
domain subsections at B-2.2–2.5's level of specificity (named deployments,
one figure for the EV sensor map or biomagnetic amplitude chart), closing
with the family × domain matrix (Table 2). Rationale:

1. **It matches the brief with least friction.** `PROJECT_BRIEF.md` §3
   ("Section 2 backbone" = taxonomy) and §4 ("current use, Section 2 tail")
   literally describe A; Stages 30 (family litreview) and 40 (applications
   litreview) then map one-to-one onto A-2.2–2.10 and A/B-hybrid 2.11,
   minimizing restructuring at integration (Stage 80).
2. **It is the lowest-risk shape for *Sensors*.** Family-primary is the
   canonical review structure the journal's reviewers expect; C's regime
   framing is more original but demands sourced envelope boundaries
   everywhere, which is the highest-hallucination-risk way to organize the
   paper's skeleton.
3. **The business third survives intact.** A's Section 4 already carries
   D's best content (TRL map, de-risking checklist, standards-as-gates);
   adopting D's "standards as market gates" subsection titling inside A-4
   imports D's clarity without its unconventional Section 2.

Second choice: **B**, if the author decides the four domains are the
paper's identity (title #2 chosen) and accepts capsule-level device physics.
Avoid running C or D pure: C for execution risk, D for reviewer-expectation
risk — both are better mined for their signature artifacts (C's capability
map as Fig. 1 in any outline; D's risk register as A-4.6).

### Title pairings (from `outputs/10_titles.md`)
- **Outline A / A+B hybrid:** #2 (four domains named — best overall match),
  #3 (technology-span hook), #13 (commercial-vs-pioneering contrast is A's
  2.1 organizing axis). Stage 10's default pick #2 works unchanged.
- **Outline B:** #2 (exact fit) or #4 (domains + principles/performance).
- **Outline C:** #3 or #15 (device-span titles that a capability map
  naturally illustrates); #9 only with a subtitle.
- **Outline D:** #7 (elements-to-systems — near-literal description of D),
  #8, or #14 (most investor-facing, matching D's voice and risk).
