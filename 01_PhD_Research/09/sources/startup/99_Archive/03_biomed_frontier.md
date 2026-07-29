# Prompt 03 — Worker Biomedical Frontier (prefix BIO)

Domain: Biomedical / medtech / bio-instrumentation
Worker: frontier-research-worker, lane BIO
Date: 2026-06-28

---

## 1. Domain thesis

The next decade of high-end medtech value is not in another monitoring app or AI dashboard — it is in the **engine-layer subsystems that make a new class of intervention physically possible**: the energy generator, the force/contact-sensing tip, the high-channel hermetic package, the magnetic/continuum actuation module, the implantable power link, and the closed-loop manufacturing/delivery instrument. Three structural shifts make 2026–2028 the right window. (1) **Energy is replacing scalpels and thermal probes**: pulsed-field electroporation, histotripsy, and focused ultrasound are clinically validated (ADVENT 4-year, AdmIRE pivotal, FDA histotripsy clearance, FUS BBB-opening phase I/II) and each needs a defensible generator/transducer/control engine. (2) **The implant is becoming a high-channel, hermetically packaged, wirelessly powered computer** — and the bottleneck is feedthrough density and power/telemetry, not the algorithm; China's NMPA just became the first regulator on Earth to approve a commercial invasive BCI (NEO, March 2026), opening a dual-track market. (3) **Regulation is finally rewarding hardware that changes a decision or a dose**: FDA Modernization Act 3.0 + the 2025 animal-testing roadmap legitimize organ-on-chip as a workflow, CMS TCET/CED ties reimbursement to intra-procedural evidence (renal denervation NCD), and China VBP is collapsing commodity-consumable margins while explicitly subsidizing domestic high-end localization. The winning plays are subsystems a dozen device OEMs must buy, not a single finished product competing with Medtronic/J&J/Abbott head-on. Reject monitoring-only capsules and imaging that does not change control (ILUMIEN IV showed OCT-guided PCI did not beat angiography on hard endpoints). Build the engine layer.

---

## 2. Candidate ideas (25)

### BIO-001 — PFA Pulse-Engine (field-aware biphasic electroporation generator)
- one-sentence product: A merchant high-voltage biphasic pulsed-field-ablation generator with real-time per-electrode field shaping and contact/impedance feedback that catheter OEMs license instead of building.
- system boundary shift: Moves the differentiator from the catheter to the **programmable energy + field-distribution engine**, decoupling waveform IP from electrode hardware.
- extreme metric: ~1.5–2 kV biphasic bursts, microsecond pulse trains, per-electrode field control across 8–32 electrodes with <2 s contact-to-lesion feedback.
- first high-end customer: Mid-tier and emerging electrophysiology device companies (Field Medical, Kardium-class, Chinese EP OEMs) lacking generator IP.
- buyer title: VP R&D / Chief Engineer, Cardiac Ablation.
- pain: Waveform durability vs. collateral injury (esophagus, phrenic nerve) is set by the generator, yet most catheter startups cannot build a safe, IEC-60601-compliant multi-kV pulse engine.
- current workaround: Outsourced one-off generators or RF/cryo thermal systems with known collateral risk.
- why current solution fails: Monophasic/uncalibrated waveforms give lower PV-isolation durability (45% vs 96% optimized biphasic in PEFCAT) and field cannot be re-shaped per electrode in real time.
- hardware stack: Multi-kV solid-state Marx/H-bridge pulse stack, per-channel HV switching, isolation, contact-impedance front-end, energy-recovery.
- software/control stack: Waveform library, electric-field solver, per-electrode dosing, contact/impedance closed loop, safety interlocks.
- prototype path 2026–2028: 2026 benchtop multi-kV stack + phantom; 2027 preclinical porcine PV isolation durability; 2028 GLP + design freeze for OEM integration / pilot IDE.
- China wedge: Domestic PFA generator IP as EP devices enter VBP; localize to dodge import pricing and supply risk; NMPA innovative-device green channel.
- US wedge: License generator to the long tail of US EP startups that cannot self-fund a multi-kV platform; FDA Breakthrough + TCET-eligible.
- cleanroom dependency: Low (power electronics + assembly, not wafer fab).
- capex band: Medium ($5–25M).
- regulatory/export risk: Class III generator; HV safety/EMC; modest export risk.
- competitors: Boston Scientific Farapulse, Medtronic, J&J Varipulse, Biosense TRUPULSE (all vertically integrated).
- defensibility: Waveform + field-shaping IP, durability datasets, IEC-60601 multi-kV engineering, OEM lock-in.
- kill criteria: If top-3 incumbents make integrated generators standard and refuse merchant supply, and durability parity cannot be shown in porcine by 2027.
- evidence status: CLEARED
- key sources: S-01 (Nature Medicine ADVENT-LTO), S-02 (Circulation AdmIRE), S-03 (Bioengineering PFA waveform review), S-04 (PACE form-factor).

### BIO-002 — 3D Fiber-Optic Force-Sensing Catheter Tip Module
- one-sentence product: A drop-in multi-core fiber-Bragg-grating tip that gives any ablation or robotic catheter temperature-insensitive 3-axis contact-force sensing.
- system boundary shift: Turns contact force from a single-vendor feature (Biosense SmartTouch) into a **licensable sensing module** for the whole catheter/robotics market.
- extreme metric: 3-axis force resolution at the ~0.1 N scale (effective ablation window ~0.2 N), temperature-compensated, in a sub-2.5 mm tip.
- first high-end customer: Robotic-catheter and EP catheter OEMs without force-sensing IP.
- buyer title: Director of Catheter Engineering.
- pain: Too-low force = ineffective lesion; too-high = perforation; most catheters and all early robotic systems lack 3D force feedback.
- current workaround: Single-axis force or impedance proxies; surgeon "feel" lost in teleoperation.
- why current solution fails: Single-axis and image-based estimates miss lateral force and drift with temperature during RF/PFA.
- hardware stack: Multi-core FBG fiber, helical/flexure compression element, micro-interrogator, tip housing.
- software/control stack: Strain-to-force decoding, temperature compensation, robotic force-control API.
- prototype path 2026–2028: 2026 bench accuracy/temperature validation; 2027 integrate into partner catheter; 2028 design-controls + OEM qualification.
- China wedge: Supply force-sensing module to domestic EP/robotics OEMs facing VBP margin compression and import-substitution mandates.
- US wedge: License to robotic-catheter entrants (endovascular, EP) as a standard subsystem.
- cleanroom dependency: Low–Medium (fiber + photonics assembly).
- capex band: Low–Medium (<$10M).
- regulatory/export risk: Component within Class II/III device; low export risk.
- competitors: Biosense (SmartTouch), Abbott TactiFlex, FBGS (component), academic FBG groups.
- defensibility: Multi-core FBG tip geometry + decoding IP, temperature-robustness, robotics integration.
- kill criteria: If incumbents bundle force sensing free and refuse merchant fiber modules; if accuracy degrades during PFA arcing.
- evidence status: CLEARED
- key sources: S-05 (Frontiers Robotics & AI multi-core FBG), S-06 (TactiFlex flexible-tip clinical).

### BIO-003 — High-Density Hermetic Feedthrough / Packaging Platform (>1000 channels)
- one-sentence product: A ceramic/Pt high-density hermetic feedthrough + package that lets neural-implant and BCI builders go from ~100 to >1000 channels without solving packaging themselves.
- system boundary shift: Makes the **package, not the electrode**, the channel-count ceiling-breaker; a merchant hermetic platform for the implant industry.
- extreme metric: ~1000–2500 feedthroughs/cm² at ~40 µm pitch, decade-scale hermeticity for chronic implants.
- first high-end customer: BCI / neuroprosthesis companies and retinal/cochlear implant makers.
- buyer title: VP Implant Engineering / Head of Packaging.
- pain: Channel count is gated by hermetic feedthrough density and lifetime, not by electrode or chip design; packaging is the dominant translation barrier.
- current workaround: Bespoke titanium cans with limited feedthroughs; thin-film encapsulation with unproven chronic hermeticity.
- why current solution fails: Conventional feedthroughs top out at hundreds of channels; thin-film coatings lack multi-year hermetic proof.
- hardware stack: Co-fired ceramic/Pt feedthrough arrays, brazing/diffusion bonding, integrated electrode interposer, He-leak test.
- software/control stack: Accelerated-aging/hermeticity analytics, channel-mapping interposer design tools.
- prototype path 2026–2028: 2026 1000-ch feedthrough coupon + He-leak; 2027 accelerated-life soak; 2028 integrate into partner implant for chronic animal study.
- China wedge: Become the domestic packaging supplier behind China's first-mover invasive BCI ecosystem (NEO/Beinao approvals); national BCI industrial policy funding.
- US wedge: Sell hermetic platform to capital-rich US BCI players who under-invest in packaging.
- cleanroom dependency: Medium–High (ceramic processing, brazing).
- capex band: High ($25–60M).
- regulatory/export risk: Component; ITAR-adjacent if defense neurotech; China export-control watch.
- competitors: Heraeus/Morgan (feedthroughs), UNSW group, in-house teams at Medtronic/Cochlear.
- defensibility: Process IP, hermeticity datasets, yield at >1000-ch pitch, qualification lock-in.
- kill criteria: If thin-film flexible encapsulation proves decade-scale hermetic at lower cost, obsoleting ceramic packages.
- evidence status: CLEARED
- key sources: S-07 (MRS Bulletin high-channel neural interface), S-08 (J Biomed Mater Res B high-channel packaging), S-30 (NMPA NEO BCI approval).

### BIO-004 — Magnetic Variable-Stiffness Steering Module for Microcatheters
- one-sentence product: A magnetically controlled module that bolts onto commercial sub-300 µm microcatheters to add continuous stiffness tuning and active steering for neurovascular and distal-vessel access.
- system boundary shift: Decouples **navigation from catheter mechanics** — one external magnetic field engine + a passive soft tip replaces a tray of fixed-stiffness catheters.
- extreme metric: Up to ~40× stiffness tuning, integration with catheters down to ~300 µm, sub-mm steering in tortuous neurovasculature.
- first high-end customer: Neurovascular intervention programs (stroke/aneurysm) and endovascular robotics OEMs.
- buyer title: Director of Neurointerventional / Endovascular Robotics.
- pain: Distal tortuous vessels demand both compliant steering and stiff support; fixed catheters cannot do both, causing failed/long navigations.
- current workaround: Manual catheter/guidewire exchanges, multiple fixed-stiffness devices, fluoroscopy-heavy navigation.
- why current solution fails: No commercial microcatheter offers dynamic in-situ stiffness or non-disruptive active steering.
- hardware stack: External electromagnet array, magnetic soft-microrobot tip (helical), catheter sheath integration, localization.
- software/control stack: Field control, tip-pose estimation, navigation autopilot, imaging fusion.
- prototype path 2026–2028: 2026 vascular phantom navigation; 2027 in-vivo animal neurovascular reach; 2028 GLP + first-in-human design.
- China wedge: Pair with domestic stroke-intervention push and magnetic-navigation precedent (Magbot NMPA approval) for localized neurovascular robotics.
- US wedge: License module to endovascular robotics startups and stroke-thrombectomy OEMs.
- cleanroom dependency: Low–Medium.
- capex band: Medium ($10–25M).
- regulatory/export risk: Class II/III; magnetic-field safety; moderate.
- competitors: Stereotaxis (magnetic nav), Bionaut, academic magnetic-microrobot labs.
- defensibility: Magnetic soft-robot tip + field-control IP, OEM catheter integration, navigation datasets.
- kill criteria: If steerable guidewire/robotic catheters reach the same distal vessels without external magnets at lower cost.
- evidence status: CLEARED
- key sources: S-09 (Nature Communications magnetic stiffness-tuning microcatheter), S-10 (Science Robotics soft steerable microcatheter), S-31 (Magbot NMPA, company/journalism).

### BIO-005 — Histotripsy Phased-Array Engine with Real-Time Aberration Correction
- one-sentence product: A non-invasive histotripsy transducer + cavitation-control engine with real-time aberration correction to treat tumors behind ribs and deep in the liver.
- system boundary shift: Moves tissue destruction from thermal/invasive to **non-thermal mechanical cavitation through aberrating anatomy**, controlled by the array engine.
- extreme metric: Multi-element phased array with per-element aberration correction to focus through ribs/fat; mechanical (non-thermal, non-ionizing) ablation.
- first high-end customer: Interventional radiology / hepatobiliary oncology programs at academic centers.
- buyer title: Chief of Interventional Radiology / Surgical Oncology.
- pain: Current histotripsy and thermal ablation struggle with rib-shadowed or deep tumors; thermal heat-sink near vessels limits efficacy.
- current workaround: Fixed-geometry histotripsy (single FDA system), RFA/microwave ablation, surgery.
- why current solution fails: Without aberration correction, energy defocuses through bone/fat, leaving deep/shadowed tumors untreatable.
- hardware stack: Large-aperture multi-element transducer, per-channel drive electronics, cavitation/bubble-cloud imaging, robotic positioning.
- software/control stack: Aberration-correction beamforming, cavitation feedback, treatment planning, real-time imaging fusion.
- prototype path 2026–2028: 2026 phantom + ex-vivo rib-blocked focusing; 2027 large-animal liver ablation; 2028 IDE feasibility.
- China wedge: Localize non-invasive ablation engine where surgical capacity is constrained; couple with domestic HIFU manufacturing base.
- US wedge: Differentiate vs the single cleared histotripsy system on deep/shadowed lesions; TCET/Breakthrough-eligible.
- cleanroom dependency: Low–Medium (piezo/transducer assembly).
- capex band: High ($25–50M).
- regulatory/export risk: Class III; therapeutic ultrasound export controls moderate.
- competitors: HistoSonics (Edison), EDAP/HIFU vendors, Insightec (FUS).
- defensibility: Aberration-correction + cavitation-control IP, transducer manufacturing, clinical reach data.
- kill criteria: If incumbent system adds aberration correction first; if cavitation control cannot be made reliable through ribs.
- evidence status: CLEARED
- key sources: S-11 (J Clin Med histotripsy review), S-12 (FDA histotripsy context within S-11/clinical debut).

### BIO-006 — Regulatory-Grade Sensor-Integrated Organ-on-Chip Platform (NAM engine)
- one-sentence product: A standardized organ-on-chip instrument with embedded TEER/oxygen/imaging sensors and a qualification dataset built to satisfy FDA New Approach Methodology (NAM) tox submissions.
- system boundary shift: Turns organ-on-chip from a boutique assay into a **qualified, instrumented decision platform** that replaces a defined animal study in the submission workflow.
- extreme metric: Continuous multi-parameter readout (barrier integrity, O2, metabolite) across parallel chips, with documented context-of-use qualification.
- first high-end customer: Pharma DMPK/tox and biologics safety groups; CROs.
- buyer title: Head of Investigative Toxicology / Translational Safety.
- pain: Animal models poorly predict human immunogenicity/hepatotox; FDAMA 2.0/3.0 now permit NAMs but sponsors lack qualified, instrumented, auditable platforms.
- current workaround: Animal studies + static 2D cell assays + outsourced bespoke chips with no standardization.
- why current solution fails: Boutique chips lack standardized sensing, reproducibility, and a qualification package regulators accept.
- hardware stack: Microfluidic chip with integrated electrodes/optical sensors, perfusion controller, plate reader/imager.
- software/control stack: Real-time barrier/viability analytics, audit-trail data capture, model-context-of-use qualification reports.
- prototype path 2026–2028: 2026 sensor-integrated liver/gut/BBB chips; 2027 reproducibility + reference-compound qualification; 2028 FDA NAM qualification engagement with pharma partner.
- China wedge: Serve domestic biotech needing human-relevant tox without large animal facilities; NMPA NAM alignment.
- US wedge: First "submission-ready" instrumented MPS as FDA phases out animal mandates (monoclonal antibodies first).
- cleanroom dependency: Medium (microfab of chips, outsourceable to MEMS foundry).
- capex band: Medium ($10–25M).
- regulatory/export risk: Lab instrument, low device-reg burden; qualification is the moat and the risk.
- competitors: Emulate, CN Bio, Mimetas, Hesperos (mostly assay/service, less submission-grade sensing).
- defensibility: Integrated-sensing IP + qualification datasets + regulatory relationships; data network effects.
- kill criteria: If FDA accepts in-silico models without MPS hardware, or if reproducibility across labs cannot be shown.
- evidence status: CLEARED_WITH_WEAKNESS
- key sources: S-13 (Trends in Biotechnology FDA phase-out of animal testing), S-32 (FDAMA 3.0 / FDA roadmap, official/journalism).

### BIO-007 — Closed-Loop Neuromodulation Biomarker Co-Processor
- one-sentence product: A low-power sensing + biomarker-decoding co-processor (ASIC + electrode interface) that turns open-loop neurostimulators into adaptive closed-loop systems across DBS, SCS, and epilepsy.
- system boundary shift: Separates the **adaptive control engine** from the stimulator, letting many neuromod OEMs add closed-loop without rebuilding the implant.
- extreme metric: Chronic on-implant biomarker detection (e.g., beta oscillations) at µW-scale power, sub-100 ms stim adjustment, >250k cumulative hours of validated signal handling (ADAPT-PD scale).
- first high-end customer: Neuromodulation OEMs and DBS programs wanting adaptive therapy beyond Medtronic Percept.
- buyer title: VP Neuromodulation R&D.
- pain: Open-loop stimulation over/under-treats; sensing+control is hard to build, and only one adaptive DBS is commercial.
- current workaround: Fixed-parameter stimulation manually re-programmed in clinic.
- why current solution fails: Static stimulation cannot track fluctuating symptoms (dyskinesia, gait freezing); most implants lack on-board adaptive control.
- hardware stack: Low-noise neural front-end ASIC, on-chip biomarker detector, stim-artifact rejection, secure telemetry.
- software/control stack: Biomarker decoders, adaptive control policies, clinician programming + safety envelope.
- prototype path 2026–2028: 2026 ASIC + bench biomarker detection; 2027 acute human intra-op validation with partner; 2028 chronic feasibility integration.
- China wedge: Supply closed-loop engine to domestic DBS makers as China scales neuromodulation; localization vs imported Percept.
- US wedge: License co-processor to SCS/DBS/epilepsy OEMs lacking adaptive IP.
- cleanroom dependency: Medium (ASIC fabbed at foundry, packaging in-house).
- capex band: Medium–High ($15–40M).
- regulatory/export risk: Class III active implant; neurotech export watch.
- competitors: Medtronic (Percept/BrainSense), NeuroPace, Abbott; mostly closed ecosystems.
- defensibility: Low-power biomarker-decoding ASIC + artifact rejection + clinical datasets.
- kill criteria: If incumbents open their adaptive platforms or biomarkers prove non-generalizable across indications.
- evidence status: CLEARED
- key sources: S-14 (JAMA Neurology long-term adaptive DBS), S-15 (closed-loop adaptive DBS review).

### BIO-008 — Ultrasound Wireless Power + Bidirectional Data Link Subsystem (mm-scale implants)
- one-sentence product: A piezo + ASIC subsystem delivering ultrasound wireless power and data to millimeter-scale implants at depth, sold as the power/telemetry layer for bioelectronic-medicine startups.
- system boundary shift: Removes the **battery and the lead** as the implant size/lifetime ceiling, enabling distributed mm-scale "motes."
- extreme metric: Functional power/telemetry at ~90 mm tissue depth within FDA acoustic limits, ~400 kb/s, ~7 µW/implant, sub-mm³ piezo node.
- first high-end customer: Bioelectronic-medicine and peripheral-nerve / neural-dust startups.
- buyer title: VP Hardware / Founder, Bioelectronic Medicine.
- pain: Battery + inductive coils dominate implant size and lifetime; deep, distributed mm-scale implants need a non-battery power/data layer.
- current workaround: Inductive RF links (poor depth/orientation), primary batteries (size, replacement surgery).
- why current solution fails: RF inductive coupling falls off with depth/misalignment; batteries cannot shrink to mm-scale or last for chronic distributed nodes.
- hardware stack: Piezoceramic/lead-free transducer, power-management + MPPT ASIC, ultrasonic backscatter telemetry, external driver.
- software/control stack: Beam steering to motes, network MAC for multi-implant, energy-recycling control.
- prototype path 2026–2028: 2026 single-mote bench at depth; 2027 in-vivo nerve recording/stim; 2028 multi-mote network demo for partner.
- China wedge: Power layer for domestic BCI/bioelectronics first-movers; piezo manufacturing base.
- US wedge: Sell as the de-facto power/telemetry layer to the bioelectronic-medicine startup wave.
- cleanroom dependency: Medium (piezo + ASIC packaging).
- capex band: Medium ($10–25M).
- regulatory/export risk: Component; acoustic-exposure limits; moderate.
- competitors: Iota Biosciences (Astellas), academic neural-dust groups, magnetoelectric WPT teams.
- defensibility: Piezo+ASIC co-design, depth/efficiency benchmarks, multi-mote networking IP.
- kill criteria: If magnetoelectric or RF links match depth/efficiency at lower cost; if acoustic limits cap usable power too low.
- evidence status: CLEARED
- key sources: S-16 (Cell Press *Device* passive ultrasonic link), S-17 (Nature Communications dual-frequency ultrasound implant DBS).

### BIO-009 — Parallelized Microfluidic LNP Production Engine (lab-to-GMP)
- one-sentence product: A parallelized microfluidic mixing engine with closed-loop process control that holds LNP particle attributes constant from 1 mL screening to GMP-scale RNA-therapeutic manufacturing.
- system boundary shift: Eliminates the **scale-up cliff** — the chip geometry + control engine, not the formulation, guarantees attribute transfer across 5+ orders of magnitude.
- extreme metric: >100× throughput vs single channel via parallelized mixers; 1 mL → 500 mL/min GMP with conserved 20–60 nm size and high encapsulation.
- first high-end customer: RNA-therapeutics companies and CDMOs (beyond COVID vaccines: oncology, rare disease, in-vivo CAR).
- buyer title: Head of Drug Product / CMC, RNA Therapeutics.
- pain: Bench formulations fail to reproduce at clinical/commercial scale; bulk mixing loses control of size/PDI/encapsulation.
- current workaround: Single-channel NanoAssemblr-style devices (limited scale) or bulk T-mixers (poor reproducibility).
- why current solution fails: Single-channel microfluidics don't scale; bulk mixers can't hold nanoscale attributes constant.
- hardware stack: Parallelized micromixer array (aerofoil/crossflow), precision pumps, inline PAT (size/encapsulation), sterile flow path.
- software/control stack: Real-time CQA control, scale-transfer model, batch records / 21 CFR Part 11.
- prototype path 2026–2028: 2026 parallel-mixer attribute matching; 2027 GMP-grade single-skid; 2028 tech-transfer with CDMO partner batch.
- China wedge: Localize RNA-LNP manufacturing engine amid biopharma self-sufficiency push; serve domestic mRNA pipeline.
- US wedge: Sell scale-conserving engine to the RNA-therapeutics wave needing reproducible clinical/commercial supply.
- cleanroom dependency: Medium (chip microfab outsourceable; GMP skid assembly).
- capex band: Medium ($10–25M).
- regulatory/export risk: Manufacturing equipment; low device burden; some dual-use/export watch.
- competitors: Precision NanoSystems (Cytiva/NanoAssemblr), Knauer, Inside Therapeutics, Helix Biotech.
- defensibility: Parallelized-mixer geometry + scale-transfer control + PAT integration; CMC datasets.
- kill criteria: If incumbents close the scale-up gap and lock in CDMOs; if attribute transfer fails at GMP scale.
- evidence status: CLEARED
- key sources: S-18 (J Pharm Pharmacol crossflow LNP), S-19 (Nano Letters parallelized microfluidic LNP).

### BIO-010 — REIMS Intraoperative Tissue-ID Front-End + Reference Spectral Library
- one-sentence product: An ambient-ionization front-end + curated reference spectral library that bolts onto existing electrosurgery and mass spectrometers to give surgeons ~2 s cancer-vs-healthy tissue calls at the cutting tip.
- system boundary shift: Converts the electrosurgical smoke into a **real-time molecular control signal** that changes the cut (re-resect margins) — not a post-hoc diagnostic.
- extreme metric: Tissue classification in ~1.8 s with >95% sensitivity/specificity in selected tumors, integrated into the surgical workflow.
- first high-end customer: Surgical-oncology centers (breast, GI, neuro) and MS instrument vendors.
- buyer title: Chief of Surgical Oncology / Director of Surgical Innovation.
- pain: Frozen-section pathology takes 20–40 min; positive margins drive re-operations; surgeons cut blind to molecular identity.
- current workaround: Intraoperative frozen section, surgeon judgment, post-op pathology re-excision.
- why current solution fails: Frozen section is slow, sampling-limited, and not real-time at the cut line.
- hardware stack: Aerosol-capture interface, REIMS ionization source, MS coupling, electrosurgical integration.
- software/control stack: Spectral classifier, reference library, margin-decision UI, surgical-system API.
- prototype path 2026–2028: 2026 front-end + library on bench tumors; 2027 prospective ex-vivo/in-vivo margin concordance; 2028 multi-site clinical + de-novo/510(k) path.
- China wedge: Localize tissue-ID front-end for domestic MS install base; oncology surgery scale.
- US wedge: Sell as add-on to existing MS + electrosurgery fleets; reduces re-operation, payer-aligned.
- cleanroom dependency: Low.
- capex band: Medium ($10–25M; relies on existing MS).
- regulatory/export risk: Class II/III software+device; library validation burden.
- competitors: Waters (REIMS/iKnife), MS Pen / MasSpec Pen groups, Raman intraoperative startups.
- defensibility: Reference-library data network effects + front-end engineering + surgical integration.
- kill criteria: If accuracy collapses outside reference tumor types; if MS footprint stays impractical for the OR.
- evidence status: CLEARED
- key sources: S-20 (British Journal of Surgery REIMS systematic review), S-21 (Scientific Reports robotic intraoperative REIMS).

### BIO-011 — Bronchoscopic Transparenchymal Steerable-Needle Access Module
- one-sentence product: A concentric-tube + flexure-tip steerable-needle module that deploys from robotic bronchoscopes to reach peripheral lung nodules outside the airway under image guidance.
- system boundary shift: Breaks the **airway-wall barrier** — reaches nodules off the bronchial tree, combining percutaneous yield with transbronchial safety.
- extreme metric: Curvilinear transparenchymal trajectories around vessels to reach distal nodules; autonomous needle steering demonstrated in vivo.
- first high-end customer: Robotic-bronchoscopy OEMs and interventional pulmonology programs.
- buyer title: Director of Interventional Pulmonology / Robotic Bronchoscopy R&D.
- pain: Robotic bronchoscopy still misses nodules not adjacent to an airway; diagnostic yield for peripheral nodules remains limited.
- current workaround: Transbronchial biopsy near airways (low yield distally) or percutaneous CT-guided biopsy (pneumothorax risk).
- why current solution fails: Straight transbronchial tools cannot steer through parenchyma around obstacles to off-airway nodules.
- hardware stack: Tendon-actuated bronchoscope interface, concentric-tube launcher, laser-patterned flexure-tip needle, EM tracking.
- software/control stack: Motion/replanning around vessels, respiratory-motion compensation, image-guided autopilot.
- prototype path 2026–2028: 2026 phantom transparenchymal reach; 2027 in-vivo animal nodule access; 2028 first-in-human feasibility with partner platform.
- China wedge: Lung-cancer screening scale; localize steerable-needle module for domestic robotic bronchoscopy entrants.
- US wedge: License module to Intuitive Ion / J&J Monarch-class platforms to lift peripheral yield.
- cleanroom dependency: Low–Medium.
- capex band: Medium ($10–25M).
- regulatory/export risk: Class II/III; robotic surgical export moderate.
- competitors: Intuitive (Ion), J&J (Monarch), Noah Medical, academic steerable-needle labs.
- defensibility: Steerable-needle mechanics + autonomous steering control + platform integration.
- kill criteria: If incumbents internalize steerable needles; if added yield doesn't justify complexity.
- evidence status: CLEARED
- key sources: S-22 (Science Robotics autonomous needle steering in vivo), S-23 (transoral peripheral lung access continuum robot + steerable needle).

### BIO-012 — 1024-Channel Thin-Film µECoG Array + Wireless ASIC (BCI engine)
- one-sentence product: A flexible, minimally invasive 1000+ channel micro-ECoG array with on-substrate wireless power and telemetry, sold as the recording engine for BCI and epilepsy mapping.
- system boundary shift: Delivers **clinical-scale channel count without penetrating cortex**, via a slide-in thin-film array + integrated wireless ASIC.
- extreme metric: Up to 65,536 electrodes / 1,024 channels with on-chip signal processing, telemetry, and wireless power on one substrate; 64× density vs clinical grids.
- first high-end customer: BCI companies and epilepsy surgical-mapping centers.
- buyer title: Head of Neural Interfaces / Epilepsy Surgery Director.
- pain: Penetrating arrays scar and have limited coverage; clinical ECoG grids are too low-density for high-bandwidth decoding.
- current workaround: Utah arrays (penetrating, limited area) or low-density clinical ECoG strips.
- why current solution fails: Penetrating electrodes degrade chronically; clinical grids lack the resolution for speech/motor decoding.
- hardware stack: Thin-film flexible electrode array, multiplexing/telemetry ASIC, wireless power, subdural-contained package.
- software/control stack: On-chip compression, decoders (motor/speech), data telemetry stack.
- prototype path 2026–2028: 2026 array + ASIC bench; 2027 chronic large-animal recording; 2028 acute human mapping / early IDE.
- China wedge: Recording engine behind China's first-approved invasive BCI ecosystem (NEO/Beinao); national BCI policy + subsidies.
- US wedge: Supply high-density array+ASIC to US BCI entrants; epilepsy mapping 510(k)/de-novo entry.
- cleanroom dependency: High (thin-film microfab + ASIC).
- capex band: High ($30–80M).
- regulatory/export risk: Class III implant; neurotech export controls.
- competitors: Precision Neuroscience, Neuralink (penetrating), Paradromics, academic µECoG groups.
- defensibility: Thin-film + ASIC co-integration, channel-count yield, chronic stability data.
- kill criteria: If penetrating arrays prove chronically safe at higher SNR; if thin-film hermeticity fails chronically.
- evidence status: CLEARED
- key sources: S-24 (Nature Electronics 65,536-electrode subdural BCI), S-25 (Nature Biomedical Engineering scalable minimally invasive BCI), S-30 (NMPA NEO approval).

### BIO-013 — Decentralized Closed-Loop CAR-T Manufacturing Instrument
- one-sentence product: A closed, automated "cell-therapy-in-a-box" instrument that runs isolation→activation→transduction→expansion with closed-loop process control for point-of-care CAR-T.
- system boundary shift: Moves manufacturing from centralized GMP plants to the **hospital bedside**, collapsing vein-to-vein time and cryo-logistics.
- extreme metric: Fully closed automated workflow producing a clinical dose near-patient; demonstrated point-of-care CAR-T at multiple academic sites.
- first high-end customer: Cancer-center cell-therapy units and academic medical centers.
- buyer title: Director of Cellular Therapy / GMP Facility.
- pain: Centralized CAR-T has weeks-long vein-to-vein time, high cost, cryoshipment failures, and limited slots.
- current workaround: Centralized commercial manufacturing (Kymriah/Yescarta) or semi-automated Prodigy/Cocoon with heavy manual steps.
- why current solution fails: Centralized logistics and partial automation keep cost/time high and access low.
- hardware stack: Closed cartridge bioreactor, integrated separation/transduction modules, inline sensors (metabolite/cell-count), sterile fluidics.
- software/control stack: Closed-loop process control, release-testing analytics, batch records / regulatory data.
- prototype path 2026–2028: 2026 closed cartridge + process control bench; 2027 engineering runs vs central process; 2028 IND-enabling point-of-care runs with partner.
- China wedge: Decentralized manufacturing for cost-constrained domestic CAR-T demand; localize vs imported platforms.
- US wedge: Sell to NCI-designated centers wanting in-house/academic CAR-T economics and faster vein-to-vein.
- cleanroom dependency: Medium (instrument provides the closed environment; reduces room-grade need).
- capex band: Medium–High ($15–40M).
- regulatory/export risk: Manufacturing system + point-of-care GMP regulatory complexity.
- competitors: Lonza Cocoon, Miltenyi Prodigy, Thermo Fisher, Cellares.
- defensibility: Closed-loop process-control IP + release analytics + regulatory templates; site network effects.
- kill criteria: If allogeneic/off-the-shelf CAR-T removes need for per-patient manufacturing; if closed-loop release testing isn't accepted.
- evidence status: CLEARED
- key sources: S-26 (JCO Global Oncology point-of-care CAR-T), S-27 (EASYGEN decentralized CAR-T framework).

### BIO-014 — Cryogen-Free Conduction-Cooled Superconducting MRI Magnet
- one-sentence product: A 1.5 T (and up) whole-body MRI magnet cooled by conduction from an off-the-shelf cryocooler, eliminating the liquid-helium supply chain and quench vent.
- system boundary shift: Removes the **helium dependency and vent infrastructure** from MRI, decoupling siting/operating cost from a volatile cryogen supply.
- extreme metric: 1.5 T clinical-grade homogeneity/stability with ~0 liquid helium; no quench vent pipe required.
- first high-end customer: MRI OEMs and hospital systems in helium-constrained / hard-to-site regions.
- buyer title: VP MRI Engineering (OEM) / Director of Imaging Operations.
- pain: Helium price/supply volatility, refill logistics, and quench-vent siting constrain MRI deployment, especially outside major hubs.
- current workaround: Sealed low-helium magnets (Philips BlueSeal-class, still helium) or conventional helium-bath magnets.
- why current solution fails: Most installed magnets still need helium and a vent; supply shocks and siting remain pain points.
- hardware stack: LTS NbTi (or HTS) coils, two-stage cryocooler conduction cooling, thermal bus, persistent-current control, RF/gradient set.
- software/control stack: Thermal/quench management, field stabilization, cooldown control.
- prototype path 2026–2028: 2026 sub-scale conduction-cooled coil; 2027 1.5 T magnet field/stability validation; 2028 imaging-grade pilot with OEM/site.
- China wedge: Strong — China is a major helium importer; cryogen-free magnet localizes a critical-supply bottleneck and pairs with domestic MRI push.
- US wedge: Sell to OEMs/rural sites wanting helium-free siting and lower lifecycle cost; resilience angle.
- cleanroom dependency: Low (magnet winding/cryogenics, not wafer fab).
- capex band: High–Very High ($40–100M).
- regulatory/export risk: Class II imaging device; superconductor/cryocooler supply + export watch.
- competitors: Siemens, GE, Philips (BlueSeal), United Imaging, Magnetica, MR Solutions.
- defensibility: Conduction-cooling thermal design + magnet engineering + helium-free reliability data.
- kill criteria: If independent multicenter data can't match helium-magnet uptime/homogeneity; if cryocooler reliability/cost is prohibitive.
- evidence status: CLEARED_WITH_WEAKNESS
- key sources: S-28 (Supercond. Sci. Technol. 1.5 T cryogen-free magnet), S-29 (cryogen-free MRI review).

### BIO-015 — Intra-Procedural Renal Nerve Mapping + Closed-Loop RDN Feedback Module
- one-sentence product: A renal-nerve mapping + ablation-feedback module that gives renal denervation an intra-procedural endpoint, telling the operator which sites to ablate and whether denervation succeeded.
- system boundary shift: Converts RDN from **blind anatomical ablation to closed-loop, endpoint-guided therapy**.
- extreme metric: Site-level nerve-activity mapping + confirmation of denervation during the procedure (today there is no acute endpoint).
- first high-end customer: Interventional cardiology / hypertension programs adopting FDA-approved RDN under CMS CED.
- buyer title: Director of Interventional Cardiology / Hypertension Center.
- pain: Approved RDN systems (Recor Paradise, Medtronic Symplicity) have no way to confirm successful denervation; response is variable and reimbursement is CED-gated on evidence.
- current workaround: Empirical circumferential ablation with no acute feedback; wait months for BP response.
- why current solution fails: Without an endpoint, operators over/under-treat and cannot prove procedural success — the core barrier to durable reimbursement.
- hardware stack: Stimulation/recording electrode catheter or sensing add-on, signal front-end, integration with RF/US RDN catheter.
- software/control stack: Nerve-activity detection, response mapping, denervation-confirmation algorithm.
- prototype path 2026–2028: 2026 nerve-signal detection bench/animal; 2027 acute response-confirmation in vivo; 2028 adjunct feasibility with approved RDN system.
- China wedge: Pair with domestic RDN localization (huge hypertensive population) as a differentiating endpoint module.
- US wedge: De-risk RDN under CMS CED by supplying the missing endpoint — directly aligned with reimbursement evidence needs.
- cleanroom dependency: Low.
- capex band: Medium ($10–25M).
- regulatory/export risk: Class III adjunct; tied to RDN sponsor trials.
- competitors: Medtronic/Recor (no acute endpoint), academic renal-nerve mapping groups, Ablative Solutions (alcohol RDN).
- defensibility: Nerve-mapping/endpoint IP + clinical-correlation datasets feeding CED evidence.
- kill criteria: If a reliable acute endpoint can't be established, or RDN reimbursement stalls under CED.
- evidence status: CLEARED
- key sources: S-33 (FDA Paradise RDN approval), S-34 (CMS RDN NCD/CED).

### BIO-016 — Cortical Visual Prosthesis Wireless Microstimulation Array Engine
- one-sentence product: A tiled wireless floating microelectrode array (WFMA) + stimulation ASIC engine that delivers patterned cortical stimulation to restore rudimentary vision in the blind.
- system boundary shift: Bypasses the eye and optic nerve entirely, making the **cortical stimulation engine** the vision interface.
- extreme metric: Multiple tiled wireless modules (e.g., 25 stimulators / 400 electrodes) chronically implanted, evoking discriminable phosphenes; 2+ years in-human.
- first high-end customer: Academic visual-prosthesis programs and neuro-ophthalmology research centers.
- buyer title: Principal Investigator, Visual Neuroprosthesis / Neurosurgery.
- pain: Retinal prostheses fail when the optic nerve/retina is destroyed; no scalable cortical-stimulation engine exists for these patients.
- current workaround: Retinal implants (limited indications, several discontinued), no option for optic-nerve blindness.
- why current solution fails: Retina-based approaches require viable downstream pathway; wired cortical arrays don't scale in channel count.
- hardware stack: Wireless floating microelectrode arrays, multi-module stimulation ASIC, transcutaneous power/telemetry, encapsulation.
- software/control stack: Phosphene mapping, camera-to-stim encoder, safety/charge-balance control.
- prototype path 2026–2028: 2026 multi-tile stim ASIC + array; 2027 chronic animal safety; 2028 expanded feasibility cohort.
- China wedge: Couple with first-mover invasive-BCI regulatory environment; cortical-stim engine for domestic neuro programs.
- US wedge: Build the cortical-stimulation engine for the next-gen visual-prosthesis programs (ICVP-class).
- cleanroom dependency: High (microelectrode + ASIC + hermetic).
- capex band: High ($30–70M).
- regulatory/export risk: Class III implant; long clinical horizon; neurotech export watch.
- competitors: Second Sight legacy (Orion), Illinois Tech ICVP, Monash Gennaris, Neuralink (future).
- defensibility: Tiled wireless-array + stim-ASIC IP, chronic phosphene datasets.
- kill criteria: If phosphene resolution can't support useful function; if chronic safety fails. Long timeline = WATCH on revenue.
- evidence status: CLEARED_WITH_WEAKNESS
- key sources: S-35 (JCI 96-channel intracortical visual percepts), S-30/S-24 (high-channel implant context).

### BIO-017 — Wearable OPM-MEG Functional Neuroimaging System
- one-sentence product: A wearable, room-temperature optically-pumped-magnetometer MEG helmet that replaces cryogenic SQUID-MEG for epilepsy localization and functional mapping.
- system boundary shift: Removes the **cryogenic dewar and fixed helmet** — sensors sit on the scalp, allowing movement, pediatric/fetal use, and far lower cost.
- extreme metric: 90+ triaxial OPM channels, sensors millimeters from scalp (higher SNR than SQUID), no liquid helium, subject free to move.
- first high-end customer: Epilepsy surgery centers and pediatric neuroimaging programs.
- buyer title: Director of MEG / Epilepsy Surgery Program.
- pain: SQUID-MEG needs liquid helium, a fixed adult-sized helmet (poor pediatric fit), immobile subjects, and multimillion-dollar siting.
- current workaround: Cryo-MEG (expensive, immobile) or scalp EEG (poor spatial resolution).
- why current solution fails: Cryogenics + fixed geometry exclude children, movement paradigms, and many sites by cost.
- hardware stack: OPM vapor-cell sensors, magnetic shielding / active field nulling, wearable helmet, acquisition electronics.
- software/control stack: Source localization, movement compensation, epileptiform/functional analysis.
- prototype path 2026–2028: 2026 multi-channel triaxial helmet; 2027 clinical concordance vs SQUID-MEG/iEEG; 2028 multi-site validation + clearance.
- China wedge: Localize OPM sensor + system as cryogen-free imaging where helium and SQUID supply are constrained.
- US wedge: Sell to epilepsy centers wanting pediatric-capable, lower-cost MEG; clearance via predicate MEG.
- cleanroom dependency: Medium (vapor-cell + photonics; shielding mechanical).
- capex band: Medium–High ($15–40M).
- regulatory/export risk: Class II imaging; quantum-sensor export watch.
- competitors: Cerca Magnetics, FieldLine, QuSpin (sensors), incumbent SQUID-MEG vendors.
- defensibility: OPM sensor performance + shielding/nulling + clinical concordance datasets.
- kill criteria: If shielding/movement artifacts prevent clinical-grade localization, or sensor supply stays bottlenecked. Note: imaging-only — keep tied to surgical decision (epileptogenic-zone localization) to clear the "monitoring-only" bar.
- evidence status: CLEARED
- key sources: S-36 (Trends in Neurosciences OPM-MEG), S-37 (Scientific Reports OPM next-gen MEG).

### BIO-018 — Steerable Closed-Loop Transcranial Focused-Ultrasound Neuromodulation Helmet
- one-sentence product: An electronically-steered phased-array tcFUS helmet with neuronavigation and EEG/biomarker closed loop for non-invasive, deep, circuit-targeted neuromodulation.
- system boundary shift: Replaces surgical implantation and shallow TMS with **non-invasive, deep, steerable, closed-loop stimulation** of specific circuits (e.g., default-mode network).
- extreme metric: Electronic steering to deep targets (sgACC/amPFC) without moving the array; closed-loop adjustment to EEG biomarkers.
- first high-end customer: Treatment-resistant-depression / psychiatry centers and neuromodulation research.
- buyer title: Director of Interventional Psychiatry / Neuromodulation.
- pain: DBS is invasive; TMS is shallow and non-specific; deep circuits (depression, OCD) are hard to reach non-invasively.
- current workaround: rTMS (cortical only), ECT, invasive DBS, medication.
- why current solution fails: TMS cannot reach deep targets; DBS requires surgery; neither closes the loop on a biomarker.
- hardware stack: Multi-element tcFUS phased array, neuronavigation, EEG integration, thermal/cavitation safety monitoring.
- software/control stack: Skull-aberration correction, target steering, biomarker-driven closed-loop dosing.
- prototype path 2026–2028: 2026 steered targeting + safety phantom/human; 2027 open-label TRD pilot (DMN target); 2028 sham-controlled trial.
- China wedge: Non-invasive psychiatric neuromodulation at scale; localize phased-array engine.
- US wedge: Position between TMS and DBS for TRD; reimbursement via psychiatry device pathway.
- cleanroom dependency: Low–Medium (transducer assembly).
- capex band: Medium ($10–25M).
- regulatory/export risk: Class II/III; therapeutic-ultrasound + neuromod evidence burden.
- competitors: Openwater, Attune Neurosciences, Insightec (ablative FUS), TMS vendors.
- defensibility: Steering + aberration-correction + closed-loop biomarker IP; clinical efficacy data.
- kill criteria: If efficacy doesn't separate from sham; if deep targeting through skull proves unreliable.
- evidence status: CLEARED_WITH_WEAKNESS
- key sources: S-38 (Frontiers in Psychiatry tcFUS DMN depression), S-11/S-37 (FUS + closed-loop context).

### BIO-019 — Bioresorbable Transient Neurostimulator / Sensor Platform
- one-sentence product: A biodegradable, wirelessly powered stimulator/sensor platform that delivers therapy (nerve regeneration, temporary pacing, leak detection) then dissolves, eliminating extraction surgery.
- system boundary shift: Makes the implant **temporary by design** — therapy on a programmed timeline with no second surgery and no chronic foreign body.
- extreme metric: Programmable on-demand bioresorption with functional electrophysiological recording/stim and wireless power before resorbing.
- first high-end customer: Surgical device OEMs (peripheral-nerve repair, cardiac post-op, GI surgery).
- buyer title: VP R&D, Surgical Devices / Bioelectronics.
- pain: Permanent temporary-use implants (pacing wires, nerve cuffs) require removal surgery and carry chronic infection/scar risk.
- current workaround: Temporary external pacing wires, permanent implants later explanted, no targeted transient electroceutical.
- why current solution fails: Non-resorbable hardware needs extraction; current transient devices lack programmable lifetime + adequate function.
- hardware stack: Bioresorbable conductors/dielectrics (Mg, Si, Mo, PLGA), transient power (RF/ultrasound/photovoltaic), resorbable electrodes.
- software/control stack: Wireless control, lifetime/dose programming, recording analytics.
- prototype path 2026–2028: 2026 transient stimulator with controlled lifetime; 2027 in-vivo nerve-regeneration/cardiac efficacy + resorption; 2028 GLP + first indication design.
- China wedge: Localize transient-electronics materials/process; large post-surgical population.
- US wedge: License platform to surgical OEMs for nerve repair / temporary pacing; novel device pathway.
- cleanroom dependency: Medium–High (thin-film transient electronics microfab).
- capex band: Medium–High ($15–35M).
- regulatory/export risk: Class II/III; resorption-byproduct safety burden.
- competitors: Academic transient-electronics groups (Rogers-class), early startups; few commercial.
- defensibility: Transient-materials + controlled-resorption + wireless-power IP; biocompatibility datasets.
- kill criteria: If resorption timing/byproducts can't be controlled safely; if function is too limited vs permanent devices.
- evidence status: CLEARED
- key sources: S-39 (Nature Reviews Electrical Engineering bioresorbable systems), S-40 (Nature Communications on-demand bioresorbable neurostimulator).

### BIO-020 — Nanopore Single-Molecule Protein Sequencing Instrument
- one-sentence product: A nanopore instrument (engineered pore + sensing ASIC + control) that reads single protein/peptide molecules, including PTMs, for next-generation proteomics.
- system boundary shift: Brings **single-molecule, amplification-free protein sequencing** to a benchtop instrument, as nanopore did for DNA.
- extreme metric: Multi-pass single-molecule reading of long protein strands; discrimination of all 20 amino acids + modifications via engineered pores.
- first high-end customer: Pharma proteomics, biomarker, and academic core labs.
- buyer title: Director of Proteomics / Translational Biomarkers.
- pain: Mass-spec proteomics misses low-abundance proteins and single-molecule PTM detail; no scalable single-molecule protein sequencer exists.
- current workaround: LC-MS/MS proteomics, affinity assays (Olink/SomaScan), Edman degradation.
- why current solution fails: MS has dynamic-range/sensitivity limits; affinity panels are targeted, not de novo single-molecule.
- hardware stack: Engineered biological/solid-state nanopore arrays, low-noise CMOS sensing ASIC, fluidics, motor enzymes/translocation control.
- software/control stack: Signal-to-sequence basecalling, PTM detection, library prep + analysis pipeline.
- prototype path 2026–2028: 2026 pore + ASIC reading defined peptides; 2027 multi-pass long-strand reads; 2028 early-access instrument with core labs.
- China wedge: Localize proteomics instrumentation amid life-science self-sufficiency; domestic pharma demand.
- US wedge: Sell engine to proteomics labs racing past MS limits; reagent/consumable razor-blade model.
- cleanroom dependency: High (ASIC + pore array fab).
- capex band: High ($30–80M).
- regulatory/export risk: Research instrument (low device burden); advanced-sensing export watch.
- competitors: Oxford Nanopore (DNA→protein), Quantum-Si (Platinum), Nautilus, Erisyon.
- defensibility: Engineered-pore + ASIC + basecalling IP; consumable lock-in.
- kill criteria: If accuracy/read-length can't reach proteome-scale utility; if MS-based methods close the single-molecule gap.
- evidence status: CLEARED_WITH_WEAKNESS
- key sources: S-41 (Nature multi-pass nanopore protein reading), S-42 (Nature Biotechnology nanopore protein sequencing).

### BIO-021 — Implantable Focused-Ultrasound BBB-Opening Array for CNS Drug Delivery
- one-sentence product: A multi-emitter implantable ultrasound array (skull-replacing) that repeatedly and reversibly opens the blood-brain barrier on demand to deliver chemotherapy/biologics to brain tumors.
- system boundary shift: Turns the **BBB into a controllable valve**, making systemic CNS drugs effective where <20% normally reaches the brain.
- extreme metric: Repeated monthly BBB opening with a 9-emitter implant across a large tumor field; phase I/II demonstrated safety + possible survival benefit with carboplatin.
- first high-end customer: Neuro-oncology / neurosurgery programs treating recurrent glioblastoma and DMG.
- buyer title: Chief of Neuro-Oncology / Neurosurgery.
- pain: The BBB blocks most chemo/biologics; recurrent GBM has dismal outcomes largely due to poor drug penetration.
- current workaround: Systemic temozolomide (low brain uptake), Gliadel wafers, intra-arterial delivery.
- why current solution fails: Systemic drugs barely cross the BBB; existing local methods are limited and not repeatable across the tumor field.
- hardware stack: Implantable multi-emitter ultrasound array, transcutaneous driver, microbubble dosing, MRI compatibility.
- software/control stack: Sonication planning, BBB-opening monitoring, dose scheduling with chemo cycles.
- prototype path 2026–2028: 2026 array + driver engineering; 2027 expanded GBM cohort with chemo; 2028 pivotal-enabling trial.
- China wedge: Localize implantable-FUS array; large neuro-oncology population; pair with domestic chemo.
- US wedge: Breakthrough/TCET-eligible CNS-delivery enabler; partner with pharma for combo trials.
- cleanroom dependency: Low–Medium (transducer assembly).
- capex band: High ($25–50M).
- regulatory/export risk: Class III implant + drug combo; therapeutic-ultrasound export moderate.
- competitors: Carthera (SonoCloud), Insightec (non-invasive FUS BBB), academic groups.
- defensibility: Implant array + repeated-opening protocol + combo clinical datasets.
- kill criteria: If non-invasive FUS BBB opening matches efficacy without an implant; if survival benefit doesn't confirm in larger trials.
- evidence status: CLEARED
- key sources: S-43 (Nature Communications 9-emitter implantable BBB-opening phase I/II), S-44 (Science Translational Medicine neuronavigated FUS BBB pediatric DMG).

### BIO-022 — Robotic Subretinal/Vitreoretinal Microsurgery Platform for Gene-Therapy Delivery
- one-sentence product: A tremor-filtering micromanipulator with OCT guidance that delivers precise, atraumatic subretinal injections for ocular gene therapies.
- system boundary shift: Makes **10 µm-scale, tremor-free subretinal delivery** routine, removing the human-hand limit on retinal gene/cell therapy.
- extreme metric: Tremor reduced from ~18 µm to ~1 µm and drift from ~212 µm to ~16 µm vs manual; ≤10 µm placement accuracy.
- first high-end customer: Retina surgery centers delivering approved/clinical gene therapies (e.g., Luxturna-class) and gene-therapy developers.
- buyer title: Director of Vitreoretinal Surgery / Surgical Gene Therapy.
- pain: Manual subretinal injection is at the limit of human tremor; imprecise delivery risks retinal trauma and inconsistent transduction.
- current workaround: Freehand subretinal injection under microscope; high variability and reflux.
- why current solution fails: Human hand tremor/drift exceeds the micron-scale precision gene-therapy delivery demands.
- hardware stack: Telemanipulation micromanipulator, intraocular instrument, intraoperative OCT, motion scaling.
- software/control stack: Tremor filtering, OCT-guided depth control, injection-rate control, autopilot assist.
- prototype path 2026–2028: 2026 OCT-integrated micromanipulator bench; 2027 in-vivo animal subretinal delivery; 2028 first-in-human with gene-therapy partner.
- China wedge: Localize ophthalmic surgical robot; large inherited-retinal-disease + AMD population.
- US wedge: Sell as the standard delivery platform bundled with gene-therapy launches; surgical-robot pathway.
- cleanroom dependency: Low–Medium.
- capex band: Medium ($10–25M).
- regulatory/export risk: Class II/III surgical robot; moderate.
- competitors: Preceyes (CE-marked), academic ophthalmic-robot groups, Johnson & Johnson Vision.
- defensibility: Micron-scale control + OCT integration + gene-therapy delivery datasets/partnerships.
- kill criteria: If manual delivery proves "good enough" for transduction outcomes; if gene-therapy pipeline stalls.
- evidence status: CLEARED
- key sources: S-45 (Gene Therapy robotic subretinal injection precision), S-46 (Eye robotising vitreoretinal surgery).

### BIO-023 — Implantable Refillable MEMS Micropump for Closed-Loop Targeted Drug Delivery
- one-sentence product: A refillable, programmable MEMS micropump with integrated dose-tracking for closed-loop intrathecal, intraocular, or local drug delivery.
- system boundary shift: Replaces systemic dosing and passive depots with an **implantable, refillable, feedback-controlled local pump**.
- extreme metric: µL/min programmable flow at ~mW power, refillable reservoir, integrated electrochemical dose-tracking for closed-loop control; >100 programmable micro-injections.
- first high-end customer: Chronic-pain (intrathecal), ophthalmology (sustained intravitreal), and oncology local-delivery programs.
- buyer title: Director of Pain Medicine / Retina / Targeted Therapeutics.
- pain: Systemic drugs cause off-target toxicity; passive depots can't titrate; existing pumps are large, non-refillable, or lack dose feedback.
- current workaround: Large intrathecal pumps, repeated intravitreal injections, oral systemic therapy.
- why current solution fails: No small, refillable, closed-loop micropump with verified per-dose tracking exists for these sites.
- hardware stack: Electrolysis/electrochemical micropump, inert refillable reservoir, dose-tracking sensor, NFC/wireless power.
- software/control stack: Dosing schedule, closed-loop dose verification, refill/telemetry app.
- prototype path 2026–2028: 2026 refillable micropump + dose-tracking bench; 2027 in-vivo chronic delivery; 2028 first indication feasibility.
- China wedge: Localize implantable drug-delivery hardware; large chronic-disease population.
- US wedge: Differentiated closed-loop local delivery for pain/retina; device + drug combo pathway.
- cleanroom dependency: Medium (MEMS microfab, outsourceable).
- capex band: Medium ($10–25M).
- regulatory/export risk: Class III drug-delivery implant; combo-product complexity.
- competitors: Medtronic SynchroMed (intrathecal), Genentech Port Delivery System, academic MEMS-pump groups.
- defensibility: Micropump + dose-tracking + refill IP; combo datasets.
- kill criteria: If long-acting depots/biologics make active pumps unnecessary; if dose-tracking reliability fails chronically.
- evidence status: CLEARED
- key sources: S-47 (Lab on a Chip active implantable drug delivery review).

### BIO-024 — Dual-Chamber Leadless / Leadless Conduction-System Pacing Engine
- one-sentence product: A miniaturized leadless pacing engine with chip-to-chip wireless inter-device synchronization enabling dual-chamber and conduction-system pacing without leads.
- system boundary shift: Removes the **transvenous lead and pocket** — the dominant failure mode of pacemakers — while preserving AV synchrony.
- extreme metric: Two communicating leadless devices delivering reliable AV-synchronous pacing for months (i2i wireless link), helix-fixation.
- first high-end customer: Electrophysiology / cardiac-device programs and CRM OEMs.
- buyer title: Director of Cardiac Electrophysiology / CRM R&D.
- pain: Leads and pockets drive most pacemaker complications (infection, lead fracture, venous occlusion); single-chamber leadless can't serve most patients.
- current workaround: Transvenous dual-chamber pacemakers (lead/pocket complications) or single-chamber leadless (limited indications).
- why current solution fails: Single-chamber leadless covers a minority; transvenous systems retain lead-related risk.
- hardware stack: Miniaturized leadless device, helix fixation, low-power inter-device RF/conducted-communication, energy-efficient pacing ASIC.
- software/control stack: Beat-to-beat synchronization protocol, power management, conduction-system capture algorithms.
- prototype path 2026–2028: 2026 inter-device comms + pacing bench; 2027 chronic animal AV-sync; 2028 feasibility / OEM integration.
- China wedge: Localize leadless CRM as EP devices enter VBP; domestic alternative to Abbott Aveir.
- US wedge: License sync/comms engine or compete on leadless conduction-system pacing (open white space).
- cleanroom dependency: Medium–High (implant + ASIC).
- capex band: High ($30–70M).
- regulatory/export risk: Class III implant; CRM export moderate.
- competitors: Abbott Aveir DR, Medtronic Micra, Boston Scientific.
- defensibility: Inter-device comms + miniaturization + conduction-system capture IP.
- kill criteria: If battery life/comms power budget can't reach commercial longevity; if incumbents lock the leadless DR market.
- evidence status: CLEARED
- key sources: S-48 (NEJM dual-chamber leadless pacemaker), S-49 (Heart Rhythm 6-month DC-LP performance).

### BIO-025 — Spatial Multi-Omics Imaging Instrument with Hardware Moat
- one-sentence product: A high-throughput spatial-omics imager (high-NA optics + multiplexed fluidics + decoding ASIC/compute) that resolves single-cell RNA/protein in tissue at clinical scale.
- system boundary shift: Moves spatial biology from slow research assays to a **high-throughput instrument** with an optical+fluidic+decode hardware moat for pathology and drug development.
- extreme metric: Single-cell-resolution transcript localization with high transcripts/gene and specificity across whole tissue microarrays (benchmarked vs Xenium/CosMx/MERSCOPE).
- first high-end customer: Pharma translational/pathology groups and academic spatial-omics cores.
- buyer title: Head of Translational Pathology / Spatial Biology Core.
- pain: Current spatial platforms trade off sensitivity, plex, and throughput; none is fast/robust enough for routine clinical or large-cohort use.
- current workaround: Bulk/single-cell sequencing (loses spatial context) or slow imaging-based panels.
- why current solution fails: Throughput, segmentation, and sensitivity limits keep spatial omics a research-only, low-throughput method.
- hardware stack: High-NA imaging, multiplexed fluidics, cyclic chemistry, decode compute/ASIC, automation.
- software/control stack: Spot-decoding, cell segmentation, panel design, analysis pipeline.
- prototype path 2026–2028: 2026 optics+fluidics engine + small panel; 2027 throughput/sensitivity benchmarking; 2028 early-access pharma installs.
- China wedge: Localize spatial-omics instrument amid life-science instrument self-sufficiency; domestic pharma/pathology demand.
- US wedge: Compete on throughput/robustness for pharma cohorts; consumable razor-blade revenue.
- cleanroom dependency: Medium (optics/fluidics assembly; ASIC outsourced).
- capex band: High ($25–60M).
- regulatory/export risk: Research instrument (low), then LDT/IVD path; advanced-imaging export watch.
- competitors: 10x Genomics (Xenium), Bruker/NanoString (CosMx), Vizgen (MERSCOPE).
- defensibility: Optical+fluidic+decode integration + consumable lock-in + panel datasets.
- kill criteria: If incumbents win throughput/cost first; if sequencing-based spatial methods dominate.
- evidence status: CLEARED_WITH_WEAKNESS
- key sources: S-50 (Nature Communications spatial transcriptomics benchmarking).

---

## 3. Source rows (verified, whitelist-compliant)

| ID | Title | Publisher / domain | Type | Impact label | URL | Claim supported |
|----|-------|--------------------|------|--------------|-----|-----------------|
| S-01 | Pulsed field ablation vs conventional thermal ablation for paroxysmal AF: 4-year ADVENT-LTO | Nature Medicine (nature.com) | peer_reviewed_article | High (JCR Q1) | https://www.nature.com/articles/s41591-026-04246-4 | PFA clinically validated, preserved 4-yr effectiveness vs thermal (BIO-001) |
| S-02 | PFA to Treat Paroxysmal AF: Safety/Effectiveness in AdmIRE Pivotal Trial | Circulation (ahajournals.org) | peer_reviewed_article | High (JCR Q1) | https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.124.070333 | PFA pivotal safety/effectiveness (BIO-001) |
| S-03 | Pulsed Field Ablation: A Review of Preclinical and Clinical Studies | Bioengineering (MDPI) | peer_reviewed_article | Moderate (Q2) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12024434/ | Biphasic vs monophasic waveform durability (96% vs 45%), generator engineering (BIO-001) |
| S-04 | Redesigning PFA Catheter Form Factors for Lesion Precision, Durability, Safety | Pacing and Clinical Electrophysiology (Wiley) | peer_reviewed_article | Moderate (Q3, downgraded) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12813649/ | Electrode geometry/field/contact are next-gen PFA differentiators (BIO-001) |
| S-05 | Three-dimensional catheter tip force sensing using multi-core fiber Bragg gratings | Frontiers in Robotics and AI (frontiersin.org) | peer_reviewed_article | Moderate (Q1/Q2) | https://pmc.ncbi.nlm.nih.gov/articles/PMC10031093/ | 3D multi-core FBG tip force sensing feasible/compact (BIO-002) |
| S-06 | Safety and effectiveness of first contact-force ablation catheter with flexible tip (TactiFlex) | J Cardiovasc Electrophysiology (PubMed) | peer_reviewed_article | High (Q1) | https://pubmed.ncbi.nlm.nih.gov/38204461/ | Clinical need/validation of fiber-optic contact-force sensing (BIO-002) |
| S-07 | Electrochemical/electrophysiological considerations for clinical high channel count neural interfaces | MRS Bulletin (Springer) | peer_reviewed_article | High (Q1) | https://link.springer.com/article/10.1557/s43577-023-00537-0 | Packaging is the translation barrier for high-channel implants (BIO-003) |
| S-08 | Establishment of High Channel-Count Packaging in Active Implantable Medical Devices | J Biomed Mater Res B (Wiley) | peer_reviewed_article | Moderate (Q2) | https://onlinelibrary.wiley.com/doi/full/10.1002/jbm.b.70040 | Ceramic/Pt feedthroughs to ~1000–2500 ch/cm² (BIO-003) |
| S-09 | Magnetically controlled microrobotic system for stiffness tuning and steering of microcatheters | Nature Communications (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s41467-025-67638-z | ~40× stiffness tuning, sub-300 µm microcatheter integration (BIO-004) |
| S-10 | Soft robotic steerable microcatheter for endovascular treatment of cerebral disorders | Science Robotics (science.org) | peer_reviewed_article | High (Q1) | https://www.science.org/doi/10.1126/scirobotics.abf0601 | Soft steerable neurovascular microcatheter (BIO-004) |
| S-11 | Surgery Without Scalpel: Histotripsy as Non-Invasive Non-Thermal Modality for Liver Tumor Ablation | J Clinical Medicine (MDPI) | peer_reviewed_article | Moderate (Q1/Q2) | https://www.mdpi.com/2077-0383/14/18/6391 | Histotripsy non-thermal ablation; phased-array + aberration correction need (BIO-005) |
| S-12 | Histotripsy for Cholangiocarcinoma Liver Tumors: feasibility/dosimetry | PMC / Ultrasound Med Biol-class | peer_reviewed_article | Moderate (Q2) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9297335/ | Histotripsy liver-tumor feasibility (BIO-005) |
| S-13 | The FDA's plan to phase out animal testing | Trends in Biotechnology (ScienceDirect) | peer_reviewed_article | High (Q1) | https://www.sciencedirect.com/science/article/pii/S0167779925005323 | FDA NAM shift legitimizes organ-on-chip workflow (BIO-006) |
| S-14 | Long-Term Personalized Adaptive Deep Brain Stimulation in Parkinson's | JAMA Neurology (jamanetwork.com) | peer_reviewed_article | High (Q1) | https://jamanetwork.com/journals/jamaneurology/fullarticle/2839117 | Adaptive closed-loop DBS clinical benefit (BIO-007) |
| S-15 | Closed-Loop Adaptive DBS in Parkinson's: Procedures and Future Perspectives | PMC (review) | peer_reviewed_article | Moderate (Q2) | https://pmc.ncbi.nlm.nih.gov/articles/PMC10357172/ | Sensing/control/stim closed-loop architecture (BIO-007) |
| S-16 | Electronics-free passive ultrasonic communication link for deep-tissue sensor implants | Device (Cell Press) | peer_reviewed_article | High (Q1) | https://www.cell.com/device/fulltext/S2666-9986(25)00068-7 | Ultrasonic deep-tissue power/comms link (BIO-008) |
| S-17 | Lead-free dual-frequency ultrasound implants for wireless biphasic DBS | Nature Communications (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s41467-024-48250-z | Ultrasound-powered mm-scale implant stim (BIO-008) |
| S-18 | Production of mRNA LNPs using advanced crossflow micromixing | J Pharmacy and Pharmacology (OUP) | peer_reviewed_article | Moderate (Q2) | https://academic.oup.com/jpp/article/76/12/1572/7816331 | Microfluidic LNP production/control (BIO-009) |
| S-19 | Scalable mRNA/siRNA LNP Production Using a Parallelized Microfluidic Device | Nano Letters (ACS) / PubMed | peer_reviewed_article | High (Q1) | https://pubmed.ncbi.nlm.nih.gov/34189917/ | Parallelized mixers >100× throughput, conserved attributes (BIO-009) |
| S-20 | Rapid evaporative ionisation mass spectrometry in surgery: a systematic review | British Journal of Surgery (OUP) | peer_reviewed_article | High (Q1) | https://academic.oup.com/bjs/article/112/11/znaf228/8321352 | REIMS real-time intraoperative tissue ID (BIO-010) |
| S-21 | Human robotic surgery with intraoperative tissue ID using REIMS | Scientific Reports (nature.com) | peer_reviewed_article | Moderate (Q1/Q2) | https://www.nature.com/articles/s41598-023-50942-3 | REIMS integrated into surgical robotics workflow (BIO-010) |
| S-22 | Autonomous medical needle steering in vivo | Science Robotics (science.org) | peer_reviewed_article | High (Q1) | https://www.science.org/doi/10.1126/scirobotics.adf7614 | Autonomous steerable-needle navigation in tissue (BIO-011) |
| S-23 | Toward Transoral Peripheral Lung Access: Combining Continuum Robots and Steerable Needles | PMC / IEEE-class | peer_reviewed_article | Moderate (peer-reviewed) | https://pmc.ncbi.nlm.nih.gov/articles/PMC5415307/ | Transparenchymal access to peripheral lung nodules (BIO-011) |
| S-24 | Wireless subdural-contained BCI with 65,536 electrodes and 1,024 channels | Nature Electronics (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s41928-025-01509-9 | High-channel thin-film µECoG + wireless ASIC (BIO-012) |
| S-25 | High-resolution BCI with electrode scalability and minimally invasive surgery | Nature Biomedical Engineering (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s41551-025-01502-9 | Minimally invasive high-density BCI array (BIO-012) |
| S-26 | Decentralized Point-of-Care Manufacturing of CD19 CAR-T in Mexico | JCO Global Oncology (ascopubs.org) | peer_reviewed_article | Moderate (Q1/Q2) | https://ascopubs.org/doi/10.1200/GO-24-00581 | Point-of-care closed-system CAR-T feasibility (BIO-013) |
| S-27 | Overcoming Access Barriers in European CAR-T: Decentralized Manufacturing (EASYGEN) | ScienceDirect (Cytotherapy-class) | peer_reviewed_article | Moderate (Q2) | https://www.sciencedirect.com/science/article/pii/S146532492600900X | Decentralized/closed automated CAR-T manufacturing (BIO-013) |
| S-28 | Design/construction/testing of 1.5 T cryogen-free whole-body MRI magnet | Supercond. Sci. Technol. (IOP) | peer_reviewed_article | Moderate (Q2) | https://iopscience.iop.org/article/10.1088/1361-6668/acb467 | Conduction-cooled helium-free 1.5T magnet feasible (BIO-014) |
| S-29 | Cryogen-free superconducting MRI system: a review | Superconductivity (ScienceDirect) | peer_reviewed_article | Moderate (Q2) | https://www.sciencedirect.com/science/article/pii/S2667325825002250 | Cryogen-free MRI removes helium supply/vent (BIO-014) |
| S-33 | Paradise Ultrasound Renal Denervation System – P220023 approval | FDA (fda.gov) | official_non_article | Authoritative regulator | https://www.fda.gov/medical-devices/recently-approved-devices/paradise-ultrasound-renal-denervation-system-p220023 | RDN approved but lacks acute endpoint (BIO-015) |
| S-34 | Renal Denervation for Uncontrolled Hypertension (NCD / CED) | CMS (cms.gov) | official_non_article | Authoritative payer | https://www.cms.gov/medicare/coverage/coverage-evidence-development/renal-denervation-uncontrolled-hypertension | RDN reimbursement gated on evidence (endpoint need) (BIO-015) |
| S-35 | Visual percepts evoked with 96-channel intracortical microelectrode array in human occipital cortex | J Clinical Investigation (jci.org) | peer_reviewed_article | High (Q1) | https://www.jci.org/articles/view/151331 | Cortical microstimulation evokes discriminable percepts (BIO-016) |
| S-36 | MEG with optically pumped magnetometers (OPM-MEG): next generation of functional neuroimaging | Trends in Neurosciences (ScienceDirect) | peer_reviewed_article | High (Q1) | https://www.sciencedirect.com/science/article/pii/S0166223622001023 | OPM-MEG replaces cryogenic SQUID-MEG (BIO-017) |
| S-37 | Using OPMs to replicate task-related responses in next-generation MEG | Scientific Reports (nature.com) | peer_reviewed_article | Moderate (Q1/Q2) | https://www.nature.com/articles/s41598-024-56878-6 | OPM-MEG concordance with SQUID-MEG (BIO-017) |
| S-38 | Transcranial focused ultrasound targeting default mode network for depression | Frontiers in Psychiatry (frontiersin.org) | peer_reviewed_article | Moderate (Q2) | https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1451828/full | Steered tcFUS deep neuromodulation for depression (BIO-018) |
| S-39 | Implantable bioresorbable electronic systems for sustainable precision medicine | Nature Reviews Electrical Engineering (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s44287-025-00190-6 | Bioresorbable transient implant platform feasibility (BIO-019) |
| S-40 | An on-demand bioresorbable neurostimulator | Nature Communications (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s41467-023-42791-5 | Programmable-lifetime resorbable stimulator (BIO-019) |
| S-41 | Multi-pass, single-molecule nanopore reading of long protein strands | Nature (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s41586-024-07935-7 | Single-molecule nanopore protein reading (BIO-020) |
| S-42 | Toward single-molecule protein sequencing using nanopores | Nature Biotechnology (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s41587-025-02587-y | Nanopore protein-sequencing instrument trajectory (BIO-020) |
| S-43 | Repeated BBB opening with nine-emitter implantable ultrasound + carboplatin in recurrent GBM (phase I/II) | Nature Communications (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s41467-024-45818-7 | Implantable FUS array repeatedly opens BBB, safety/survival signal (BIO-021) |
| S-44 | BBB opening with neuronavigation-guided FUS in pediatric diffuse midline glioma | Science Translational Medicine (science.org) | peer_reviewed_article | High (Q1) | https://www.science.org/doi/10.1126/scitranslmed.adq6645 | FUS BBB-opening enables CNS drug delivery (BIO-021) |
| S-45 | Advantages of robotic assistance over manual approach in simulated subretinal injections | Gene Therapy (nature.com) | peer_reviewed_article | Moderate (Q2) | https://www.nature.com/articles/s41434-021-00262-w | Robotic subretinal: drift 16 vs 212 µm, tremor 1 vs 18 µm (BIO-022) |
| S-46 | Robotising vitreoretinal surgeries | Eye (nature.com) | peer_reviewed_article | Moderate (Q1/Q2) | https://www.nature.com/articles/s41433-024-03149-3 | Robotic vitreoretinal microsurgery for gene therapy delivery (BIO-022) |
| S-47 | Active implantable drug delivery systems: engineering factors, challenges, opportunities | Lab on a Chip (RSC) | peer_reviewed_article | High (Q1) | https://pubs.rsc.org/en/content/articlehtml/2025/lc/d5lc00131e | Refillable closed-loop MEMS micropump engineering (BIO-023) |
| S-48 | A Dual-Chamber Leadless Pacemaker | New England Journal of Medicine (PubMed) | peer_reviewed_article | High (Q1) | https://pubmed.ncbi.nlm.nih.gov/37212442/ | Dual-chamber leadless AV-synchronous pacing (BIO-024) |
| S-49 | Six-month electrical performance of first dual-chamber leadless pacemaker | Heart Rhythm (heartrhythmjournal.com) | peer_reviewed_article | High (Q1) | https://www.heartrhythmjournal.com/article/S1547-5271(24)02525-6/fulltext | Leadless inter-device sync durability (BIO-024) |
| S-50 | Systematic benchmarking of imaging spatial transcriptomics platforms in FFPE tissues | Nature Communications (nature.com) | peer_reviewed_article | High (Q1) | https://www.nature.com/articles/s41467-025-64990-y | Spatial-omics platform tradeoffs (sensitivity/plex/throughput) (BIO-025) |
| S-30 | China approves world's first implantable BCI (NEO) for medical use | MIT Technology Review (technologyreview.com) | journalism_timing | Authoritative journalism (timing) | https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/ | NMPA first-mover invasive BCI approval — China wedge (BIO-003/012/016) |
| S-31 | Magbot Robotic Magnetic Navigation Ablation Catheter Approved by NMPA | BioSpace (company/journalism) | company_claim | Company claim | https://www.biospace.com/press-releases/magbot-robotic-magnetic-navigation-ablation-catheter-approved-by-chinas-nmpa | NMPA magnetic-navigation precedent — China wedge (BIO-004) |
| S-32 | Senate clears FDA Modernization Act 3.0 (nonclinical/NAM reforms) | Drug Discovery Trends (journalism) | journalism_timing | Authoritative journalism (timing) | https://www.drugdiscoverytrends.com/senate-clears-fda-modernization-act-3-0-aiming-to-align-fda-regulations-with-nonclinical-testing-reforms/ | FDAMA 3.0 legitimizes NAMs/organ-on-chip (BIO-006) |
| S-51 | Impact of volume-based procurement on coronary stent use (interrupted time series) | BMC/PMC (peer-reviewed) | peer_reviewed_article | Moderate (Q2) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12581602/ | China VBP compresses commodity-consumable margins → high-end localization wedge (cross-cutting) |
| S-52 | Final Notice — Transitional Coverage for Emerging Technologies (TCET) | CMS (cms.gov) | official_non_article | Authoritative payer | https://www.cms.gov/newsroom/fact-sheets/final-notice-transitional-coverage-emerging-technologies-cms-3421-fn | Expedited Medicare coverage pathway for breakthrough devices (cross-cutting reimbursement) |
| S-53 | OCT predictors of clinical outcomes after stent implantation: ILUMIEN IV | European Heart Journal (OUP) | peer_reviewed_article | High (Q1) | https://academic.oup.com/eurheartj/article/45/43/4630/7743289 | IVOCT did NOT beat angiography on hard endpoints — supports REJECT R-2 |

(53 source rows; >20 peer-reviewed high/moderate-impact plus authoritative non-article and clearly-labeled company/journalism for China timing.)

---

## 4. Rejected ideas

- **R-1 — Diagnostic-only magnetically controlled capsule endoscopy.** Strong evidence it matches gastroscopy accuracy (PMC8739542, journals.sagepub.com 17562848231206991), but it is **monitoring/diagnostic-only** and does not change control or therapy. Violates the anti-pattern. Would only re-enter if it added integrated biopsy/therapy actuation.
- **R-2 — Intravascular OCT imaging engine for PCI guidance.** ILUMIEN IV (European Heart Journal 2024, S-53) showed OCT-guided PCI **did not improve hard clinical outcomes** vs angiography. Imaging without proven control-change / outcome benefit; fails the "changes treatment" bar.
- **R-3 — Generic AI radiology triage dashboard.** Explicit anti-pattern (generic AI dashboard, monitoring-only); no hardware moat, crowded, reimbursement-poor.
- **R-4 — Cuffless wearable blood-pressure monitor.** Monitoring-only consumer/clinical wearable; no intervention, no engine-layer moat. Rejected.
- **R-5 — Merchant photon-counting CT detector (CdTe/CZT) module.** Real frontier tech (Siemens/GE commercial), but **cleanroom/capex-very-heavy with no realistic outsourcing path** for a startup, and incumbents are vertically integrated detector-to-system. Fails "cleanroom-heavy with no outsourcing path." Kept only as imaging context.
- **R-6 — "China clone" of an EP mapping system with no wedge.** A me-too 3D EP mapping system competing with MicroPort/Biosense on equivalence, under VBP pricing collapse, with no defensible subsystem. Anti-pattern: China-clone without a defensible wedge. (The defensible version is the generator/force/mapping *subsystem* — BIO-001/002.)
- **R-7 — Pure software fully-closed-loop insulin algorithm.** Without proprietary sensing/delivery hardware it is an algorithm layer on commodity pumps/CGMs; TAM-driven, low moat, crowded. Rejected as software-only / not engine-layer.

---

## 5. Top 5 from this worker lane

1. **BIO-001 — PFA Pulse-Engine (field-aware biphasic electroporation generator).** Strongest clinical validation (ADVENT-LTO 4-yr, AdmIRE pivotal — both Q1), clear engine-layer wedge (generator/field IP separable from catheter), large multi-OEM buyer base, strong China localization angle as EP enters VBP. CLEARED.
2. **BIO-003 — High-Density Hermetic Feedthrough / Packaging Platform (>1000 channels).** The real bottleneck for the entire BCI/neuroprosthesis wave (MRS Bulletin: packaging is the translation barrier), merchant model sells to many builders, and China's first-mover invasive-BCI approval (NEO) plus BCI industrial policy create a unique dual-track. CLEARED.
3. **BIO-013 — Decentralized Closed-Loop CAR-T Manufacturing Instrument.** Moves the cost/time bottleneck of cell therapy to the bedside, validated point-of-care precedents (JCO Global Oncology, EASYGEN), buyer is every cancer center, defensible closed-loop process-control + release analytics. CLEARED.
4. **BIO-005 — Histotripsy Phased-Array Engine with Aberration Correction.** Non-thermal mechanical ablation is FDA-cleared and growing; the unmet engine-layer problem (treating rib-shadowed/deep tumors via aberration correction) is concrete and defensible, with a clear IR/oncology buyer. CLEARED.
5. **BIO-021 — Implantable Focused-Ultrasound BBB-Opening Array for CNS Drug Delivery.** Turns the BBB into a controllable valve; phase I/II human data (Nature Communications) show safety + survival signal in recurrent GBM; pharma-combo and TCET/Breakthrough-aligned. CLEARED.

---

## 6. CSV-ready candidate rows

```csv
candidate_id,candidate_name,one_sentence_product,system_boundary_shift,extreme_metric,first_high_end_customer,buyer_title,pain,current_workaround,why_current_solution_fails,hardware_stack,software_control_stack,prototype_path_2026_2028,china_wedge,us_wedge,cleanroom_dependency,capex_band,regulatory_export_risk,competitors,defensibility,kill_criteria,evidence_status,key_sources
BIO-001,PFA Pulse-Engine,Merchant biphasic pulsed-field-ablation generator with real-time per-electrode field shaping and contact feedback,Differentiator moves from catheter to programmable energy/field engine,~1.5-2 kV biphasic microsecond trains with per-electrode field control and <2s contact-to-lesion feedback,Mid-tier and emerging EP device companies,VP R&D / Chief Engineer Cardiac Ablation,Waveform durability vs collateral injury is set by the generator yet startups cannot build safe multi-kV pulse engines,Outsourced one-off generators or RF/cryo thermal systems,Monophasic/uncalibrated waveforms give low PV-isolation durability and no real-time per-electrode field control,Multi-kV solid-state pulse stack HV switching isolation contact-impedance front-end energy recovery,Waveform library field solver per-electrode dosing contact closed loop safety interlocks,2026 benchtop multi-kV+phantom;2027 porcine durability;2028 GLP+OEM/IDE,Domestic PFA generator IP as EP enters VBP plus NMPA innovative green channel,License generator to long-tail US EP startups; FDA Breakthrough/TCET,Low,Medium $5-25M,Class III generator HV/EMC safety modest export,Boston Scientific Farapulse Medtronic JnJ Varipulse Biosense TRUPULSE,Waveform+field-shaping IP durability datasets IEC-60601 multi-kV engineering OEM lock-in,Incumbents make integrated generators standard and refuse merchant supply and porcine parity fails by 2027,CLEARED,S-01;S-02;S-03;S-04
BIO-002,3D Fiber-Optic Force-Sensing Catheter Tip Module,Drop-in multi-core FBG tip giving any catheter temperature-insensitive 3-axis contact-force sensing,Contact force becomes a licensable sensing module not a single-vendor feature,3-axis force at ~0.1N scale temperature-compensated in sub-2.5mm tip,Robotic-catheter and EP catheter OEMs,Director of Catheter Engineering,Too-low force ineffective lesion too-high perforation and robots lack 3D force feedback,Single-axis force or impedance proxies and lost teleoperation feel,Single-axis and image estimates miss lateral force and drift with temperature,Multi-core FBG fiber helical/flexure element micro-interrogator tip housing,Strain-to-force decoding temperature compensation robotic force-control API,2026 bench accuracy/temp;2027 integrate partner catheter;2028 design-controls/OEM qual,Supply force module to domestic EP/robotics OEMs under VBP and import substitution,License to US robotic-catheter entrants as standard subsystem,Low-Medium,Low-Medium <$10M,Component in Class II/III low export,Biosense SmartTouch Abbott TactiFlex FBGS academic FBG,Multi-core FBG tip geometry+decoding IP temperature robustness robotics integration,Incumbents bundle force sensing free or accuracy degrades during PFA arcing,CLEARED,S-05;S-06
BIO-003,High-Density Hermetic Feedthrough/Packaging Platform,Ceramic/Pt high-density hermetic feedthrough+package enabling >1000-channel neural implants,Package not electrode becomes the channel-count ceiling-breaker,~1000-2500 feedthroughs/cm2 at ~40um pitch decade-scale hermeticity,BCI/neuroprosthesis and retinal/cochlear implant makers,VP Implant Engineering / Head of Packaging,Channel count gated by hermetic feedthrough density and lifetime not electrode or chip,Bespoke titanium cans with few feedthroughs or unproven thin-film coatings,Conventional feedthroughs top out at hundreds of channels and thin-film lacks chronic hermetic proof,Co-fired ceramic/Pt feedthrough arrays brazing electrode interposer He-leak test,Hermeticity analytics channel-mapping interposer design tools,2026 1000-ch coupon+He-leak;2027 accelerated-life soak;2028 chronic animal integration,Domestic packaging supplier behind China first-mover invasive BCI ecosystem NEO/Beinao with policy funding,Sell hermetic platform to capital-rich US BCI players,Medium-High,High $25-60M,Component ITAR-adjacent if defense neurotech China export watch,Heraeus Morgan UNSW group in-house Medtronic Cochlear,Process IP hermeticity datasets >1000-ch yield qualification lock-in,Thin-film flexible encapsulation proves decade-scale hermetic at lower cost,CLEARED,S-07;S-08;S-30
BIO-004,Magnetic Variable-Stiffness Steering Module,Magnetically controlled module adding stiffness tuning and steering to sub-300um commercial microcatheters,Decouples navigation from catheter mechanics via external field engine plus passive soft tip,Up to ~40x stiffness tuning sub-300um integration sub-mm steering,Neurovascular intervention programs and endovascular robotics OEMs,Director Neurointerventional / Endovascular Robotics,Distal tortuous vessels need both compliant steering and stiff support which fixed catheters cannot do,Manual catheter/guidewire exchanges multiple fixed-stiffness devices,No commercial microcatheter offers dynamic in-situ stiffness or non-disruptive steering,External electromagnet array magnetic soft helical tip sheath integration localization,Field control tip-pose estimation navigation autopilot imaging fusion,2026 phantom nav;2027 in-vivo neurovascular reach;2028 GLP+FIH design,Pair with domestic stroke push and Magbot NMPA magnetic-nav precedent,License module to US endovascular robotics startups,Low-Medium,Medium $10-25M,Class II/III magnetic-field safety moderate,Stereotaxis Bionaut academic magnetic-microrobot labs,Magnetic soft-robot tip+field-control IP OEM integration navigation datasets,Steerable guidewire/robotic catheters reach same vessels without magnets cheaper,CLEARED,S-09;S-10;S-31
BIO-005,Histotripsy Phased-Array Engine,Non-invasive histotripsy transducer+cavitation-control engine with real-time aberration correction,Tissue destruction moves to non-thermal cavitation through aberrating anatomy,Multi-element array with per-element aberration correction to focus through ribs non-thermal,Interventional radiology/hepatobiliary oncology academic centers,Chief of Interventional Radiology / Surgical Oncology,Current histotripsy and thermal ablation struggle with rib-shadowed or deep tumors,Fixed-geometry histotripsy or RFA/microwave or surgery,Without aberration correction energy defocuses through bone/fat leaving deep tumors untreatable,Large-aperture multi-element transducer per-channel drive cavitation imaging robotic positioning,Aberration-correction beamforming cavitation feedback planning imaging fusion,2026 phantom rib-blocked focusing;2027 large-animal liver;2028 IDE feasibility,Localize non-invasive ablation engine with domestic HIFU base,Differentiate vs single cleared histotripsy system on deep lesions TCET-eligible,Low-Medium,High $25-50M,Class III therapeutic ultrasound export moderate,HistoSonics Edison EDAP HIFU Insightec,Aberration-correction+cavitation-control IP transducer manufacturing reach data,Incumbent adds aberration correction first or cavitation control unreliable through ribs,CLEARED,S-11;S-12
BIO-006,Sensor-Integrated Organ-on-Chip NAM Platform,Standardized organ-on-chip with embedded TEER/O2/imaging sensors and FDA NAM qualification dataset,Organ-on-chip becomes a qualified instrumented decision platform replacing a defined animal study,Continuous multi-parameter readout across parallel chips with documented context-of-use,Pharma DMPK/tox and biologics safety groups and CROs,Head of Investigative Toxicology / Translational Safety,Animal models poorly predict human tox and sponsors lack qualified instrumented auditable platforms,Animal studies plus static 2D assays plus bespoke chips,Boutique chips lack standardized sensing reproducibility and a regulator-accepted package,Microfluidic chip with integrated electrodes/optical sensors perfusion controller imager,Real-time barrier/viability analytics audit-trail capture qualification reports,2026 sensor-integrated chips;2027 reproducibility+reference qualification;2028 FDA NAM engagement,Serve domestic biotech needing human-relevant tox without large animal facilities,First submission-ready instrumented MPS as FDA phases out animal mandates,Medium,Medium $10-25M,Lab instrument low device burden qualification is the moat,Emulate CN Bio Mimetas Hesperos,Integrated-sensing IP qualification datasets regulatory relationships data network effects,FDA accepts in-silico without MPS hardware or reproducibility fails across labs,CLEARED_WITH_WEAKNESS,S-13;S-32
BIO-007,Closed-Loop Neuromodulation Biomarker Co-Processor,Low-power sensing+biomarker-decoding co-processor turning open-loop stimulators into adaptive closed-loop,Adaptive control engine separated from stimulator for many neuromod OEMs,Chronic on-implant biomarker detection at uW power sub-100ms stim adjustment,Neuromodulation OEMs and DBS programs,VP Neuromodulation R&D,Open-loop stimulation over/under-treats and sensing+control is hard to build,Fixed-parameter stimulation manually re-programmed in clinic,Static stimulation cannot track fluctuating symptoms and most implants lack adaptive control,Low-noise neural front-end ASIC on-chip biomarker detector artifact rejection telemetry,Biomarker decoders adaptive control policies clinician programming safety envelope,2026 ASIC+bench detection;2027 acute human intra-op;2028 chronic feasibility,Supply closed-loop engine to domestic DBS makers localizing vs imported Percept,License co-processor to SCS/DBS/epilepsy OEMs lacking adaptive IP,Medium,Medium-High $15-40M,Class III active implant neurotech export watch,Medtronic Percept NeuroPace Abbott,Low-power biomarker-decoding ASIC+artifact rejection clinical datasets,Incumbents open adaptive platforms or biomarkers non-generalizable across indications,CLEARED,S-14;S-15
BIO-008,Ultrasound Wireless Power+Data Link Subsystem,Piezo+ASIC subsystem delivering ultrasound power and data to mm-scale implants at depth,Removes battery and lead as implant size/lifetime ceiling enabling distributed motes,Power/telemetry at ~90mm depth within FDA limits ~400kb/s ~7uW sub-mm3 node,Bioelectronic-medicine and neural-dust startups,VP Hardware / Founder Bioelectronic Medicine,Battery+coils dominate implant size and deep distributed implants need non-battery power/data,Inductive RF links poor depth/orientation or primary batteries,RF inductive coupling falls off with depth and batteries cannot shrink to mm-scale,Piezoceramic transducer power-management+MPPT ASIC ultrasonic backscatter telemetry external driver,Beam steering to motes network MAC energy-recycling control,2026 single-mote bench at depth;2027 in-vivo nerve;2028 multi-mote network,Power layer for domestic BCI/bioelectronics first-movers with piezo base,Sell as de-facto power/telemetry layer to bioelectronic-medicine startups,Medium,Medium $10-25M,Component acoustic-exposure limits moderate,Iota Biosciences academic neural-dust magnetoelectric WPT,Piezo+ASIC co-design depth/efficiency benchmarks multi-mote networking IP,Magnetoelectric or RF links match depth/efficiency cheaper or acoustic limits cap power,CLEARED,S-16;S-17
BIO-009,Parallelized Microfluidic LNP Production Engine,Parallelized microfluidic mixing engine with closed-loop control holding LNP attributes from 1mL to GMP,Eliminates scale-up cliff via chip geometry+control not formulation,>100x throughput vs single channel 1mL to 500mL/min with conserved 20-60nm size,RNA-therapeutics companies and CDMOs,Head of Drug Product / CMC RNA Therapeutics,Bench formulations fail to reproduce at clinical/commercial scale,Single-channel NanoAssemblr-style devices or bulk T-mixers,Single-channel does not scale and bulk mixers cannot hold nanoscale attributes,Parallelized micromixer array precision pumps inline PAT sterile flow path,Real-time CQA control scale-transfer model 21 CFR Part 11 batch records,2026 attribute matching;2027 GMP single-skid;2028 CDMO tech-transfer,Localize RNA-LNP manufacturing engine amid biopharma self-sufficiency,Sell scale-conserving engine to RNA-therapeutics wave,Medium,Medium $10-25M,Manufacturing equipment low device burden dual-use watch,Precision NanoSystems Cytiva Knauer Inside Therapeutics,Parallelized-mixer geometry+scale-transfer control+PAT CMC datasets,Incumbents close scale-up gap and lock CDMOs or attribute transfer fails at GMP,CLEARED,S-18;S-19
BIO-010,REIMS Intraoperative Tissue-ID Front-End,Ambient-ionization front-end+reference spectral library bolting onto electrosurgery+MS for ~2s cancer-vs-healthy calls,Electrosurgical smoke becomes a real-time molecular control signal changing the cut,Classification in ~1.8s with >95% sensitivity/specificity integrated in workflow,Surgical-oncology centers and MS instrument vendors,Chief of Surgical Oncology / Director Surgical Innovation,Frozen section is slow and positive margins drive re-operations,Intraoperative frozen section surgeon judgment post-op pathology,Frozen section slow sampling-limited and not real-time at the cut line,Aerosol-capture interface REIMS ionization source MS coupling electrosurgical integration,Spectral classifier reference library margin-decision UI surgical API,2026 front-end+library bench;2027 prospective margin concordance;2028 multi-site+de-novo/510k,Localize tissue-ID front-end for domestic MS install base,Sell as add-on to existing MS+electrosurgery fleets reducing re-operation,Low,Medium $10-25M,Class II/III software+device library validation burden,Waters REIMS iKnife MasSpec Pen Raman startups,Reference-library data network effects+front-end engineering+surgical integration,Accuracy collapses outside reference tumors or MS footprint impractical for OR,CLEARED,S-20;S-21
BIO-011,Bronchoscopic Transparenchymal Steerable-Needle Module,Concentric-tube+flexure-tip steerable-needle module deploying from robotic bronchoscopes to reach peripheral nodules off-airway,Breaks the airway-wall barrier combining percutaneous yield with transbronchial safety,Curvilinear transparenchymal trajectories around vessels with autonomous steering in vivo,Robotic-bronchoscopy OEMs and interventional pulmonology programs,Director Interventional Pulmonology / Robotic Bronchoscopy R&D,Robotic bronchoscopy still misses nodules not adjacent to an airway,Transbronchial biopsy near airways or percutaneous CT-guided biopsy,Straight transbronchial tools cannot steer through parenchyma around obstacles,Tendon-actuated bronchoscope interface concentric-tube launcher laser-patterned needle EM tracking,Motion replanning around vessels respiratory-motion compensation image-guided autopilot,2026 phantom reach;2027 in-vivo nodule access;2028 FIH feasibility,Lung-cancer screening scale localize needle module for domestic robotic bronch entrants,License module to Intuitive Ion / JnJ Monarch to lift peripheral yield,Low-Medium,Medium $10-25M,Class II/III robotic surgical export moderate,Intuitive Ion JnJ Monarch Noah Medical academic steerable-needle labs,Steerable-needle mechanics+autonomous steering control+platform integration,Incumbents internalize steerable needles or added yield does not justify complexity,CLEARED,S-22;S-23
BIO-012,1024-Channel Thin-Film uECoG Array+Wireless ASIC,Flexible minimally invasive 1000+ channel micro-ECoG array with on-substrate wireless power and telemetry,Clinical-scale channel count without penetrating cortex via slide-in array+ASIC,Up to 65536 electrodes/1024 channels with on-chip processing 64x density vs clinical grids,BCI companies and epilepsy surgical-mapping centers,Head of Neural Interfaces / Epilepsy Surgery Director,Penetrating arrays scar and clinical grids too low-density for high-bandwidth decoding,Utah arrays penetrating limited area or low-density clinical strips,Penetrating electrodes degrade chronically and grids lack resolution for speech/motor decoding,Thin-film flexible array multiplexing/telemetry ASIC wireless power subdural package,On-chip compression motor/speech decoders telemetry stack,2026 array+ASIC bench;2027 chronic large-animal;2028 acute human/early IDE,Recording engine behind China first-approved invasive BCI ecosystem with policy subsidies,Supply high-density array+ASIC to US BCI entrants epilepsy 510k/de-novo,High,High $30-80M,Class III implant neurotech export controls,Precision Neuroscience Neuralink Paradromics academic uECoG,Thin-film+ASIC co-integration channel-count yield chronic stability data,Penetrating arrays prove chronically safe at higher SNR or thin-film hermeticity fails,CLEARED,S-24;S-25;S-30
BIO-013,Decentralized Closed-Loop CAR-T Manufacturing Instrument,Closed automated cell-therapy-in-a-box running isolation to expansion with closed-loop control for point-of-care CAR-T,Manufacturing moves from centralized plants to the bedside collapsing vein-to-vein time,Fully closed automated workflow producing a clinical dose near-patient,Cancer-center cell-therapy units and academic medical centers,Director of Cellular Therapy / GMP Facility,Centralized CAR-T has weeks-long vein-to-vein high cost cryoship failures and limited slots,Centralized commercial manufacturing or semi-automated Prodigy/Cocoon with manual steps,Centralized logistics and partial automation keep cost/time high and access low,Closed cartridge bioreactor separation/transduction modules inline sensors sterile fluidics,Closed-loop process control release-testing analytics batch records,2026 cartridge+control bench;2027 engineering runs vs central;2028 IND-enabling POC runs,Decentralized manufacturing for cost-constrained domestic CAR-T demand,Sell to NCI centers wanting in-house CAR-T economics and faster vein-to-vein,Medium-High,Medium-High $15-40M,Manufacturing system+point-of-care GMP regulatory complexity,Lonza Cocoon Miltenyi Prodigy Thermo Fisher Cellares,Closed-loop process-control IP+release analytics+regulatory templates site network effects,Allogeneic CAR-T removes per-patient manufacturing or closed-loop release not accepted,CLEARED,S-26;S-27
BIO-014,Cryogen-Free Conduction-Cooled Superconducting MRI Magnet,1.5T+ whole-body MRI magnet conduction-cooled by off-the-shelf cryocooler eliminating liquid helium and quench vent,Removes helium dependency and vent infrastructure from MRI,1.5T clinical homogeneity/stability with ~0 liquid helium and no quench vent,MRI OEMs and hospitals in helium-constrained regions,VP MRI Engineering / Director Imaging Operations,Helium price/supply volatility refill logistics and quench-vent siting constrain MRI deployment,Sealed low-helium magnets still helium or conventional helium-bath,Most magnets still need helium and a vent and supply shocks remain,LTS NbTi or HTS coils two-stage cryocooler conduction cooling thermal bus persistent-current RF/gradient,Thermal/quench management field stabilization cooldown control,2026 sub-scale coil;2027 1.5T field/stability;2028 imaging-grade pilot,Strong China is major helium importer cryogen-free localizes critical-supply bottleneck,Sell to OEMs/rural sites wanting helium-free siting and lower lifecycle cost,Low,High-Very High $40-100M,Class II imaging superconductor/cryocooler supply+export watch,Siemens GE Philips BlueSeal United Imaging Magnetica,Conduction-cooling thermal design+magnet engineering+helium-free reliability data,Independent data cannot match helium-magnet uptime/homogeneity or cryocooler cost prohibitive,CLEARED_WITH_WEAKNESS,S-28;S-29
BIO-015,Intra-Procedural Renal Nerve Mapping+Closed-Loop RDN Module,Renal-nerve mapping+ablation-feedback module giving renal denervation an intra-procedural endpoint,Converts RDN from blind anatomical ablation to closed-loop endpoint-guided therapy,Site-level nerve-activity mapping+confirmation of denervation during the procedure,Interventional cardiology/hypertension programs adopting FDA-approved RDN under CMS CED,Director Interventional Cardiology / Hypertension Center,Approved RDN has no way to confirm successful denervation and reimbursement is CED-gated,Empirical circumferential ablation with no acute feedback,Without an endpoint operators over/under-treat and cannot prove procedural success,Stimulation/recording electrode catheter signal front-end integration with RF/US RDN catheter,Nerve-activity detection response mapping denervation-confirmation algorithm,2026 nerve-signal bench/animal;2027 acute response-confirmation;2028 adjunct feasibility,Pair with domestic RDN localization for huge hypertensive population,De-risk RDN under CMS CED by supplying the missing endpoint,Low,Medium $10-25M,Class III adjunct tied to RDN sponsor trials,Medtronic Recor Ablative Solutions academic renal-nerve groups,Nerve-mapping/endpoint IP+clinical-correlation datasets feeding CED evidence,Reliable acute endpoint cannot be established or RDN reimbursement stalls,CLEARED,S-33;S-34
BIO-016,Cortical Visual Prosthesis Wireless Microstimulation Array Engine,Tiled wireless floating microelectrode array+stim ASIC engine delivering patterned cortical stimulation to restore vision,Bypasses eye and optic nerve making cortical stimulation engine the vision interface,Multiple tiled wireless modules (25 stim/400 electrodes) chronic evoking discriminable phosphenes 2+ yr,Academic visual-prosthesis programs and neuro-ophthalmology centers,PI Visual Neuroprosthesis / Neurosurgery,Retinal prostheses fail when optic nerve/retina destroyed and no scalable cortical engine exists,Retinal implants limited indications or no option for optic-nerve blindness,Retina approaches need viable downstream pathway and wired cortical arrays do not scale,Wireless floating microelectrode arrays multi-module stim ASIC transcutaneous power encapsulation,Phosphene mapping camera-to-stim encoder charge-balance safety control,2026 multi-tile ASIC+array;2027 chronic animal safety;2028 expanded feasibility,Couple with first-mover invasive-BCI regulatory environment,Build cortical-stimulation engine for next-gen visual-prosthesis programs,High,High $30-70M,Class III implant long horizon neurotech export watch,Second Sight Orion Illinois Tech ICVP Monash Gennaris,Tiled wireless-array+stim-ASIC IP chronic phosphene datasets,Phosphene resolution cannot support useful function or chronic safety fails,CLEARED_WITH_WEAKNESS,S-35;S-24
BIO-017,Wearable OPM-MEG Functional Neuroimaging System,Wearable room-temperature OPM MEG helmet replacing cryogenic SQUID-MEG for epilepsy localization and mapping,Removes cryogenic dewar and fixed helmet allowing movement pediatric/fetal use and lower cost,90+ triaxial OPM channels millimeters from scalp no liquid helium subject free to move,Epilepsy surgery centers and pediatric neuroimaging programs,Director of MEG / Epilepsy Surgery Program,SQUID-MEG needs helium fixed adult helmet immobile subjects and multimillion-dollar siting,Cryo-MEG expensive immobile or scalp EEG poor spatial resolution,Cryogenics and fixed geometry exclude children movement paradigms and many sites by cost,OPM vapor-cell sensors magnetic shielding/active nulling wearable helmet acquisition electronics,Source localization movement compensation epileptiform/functional analysis,2026 multi-channel helmet;2027 concordance vs SQUID/iEEG;2028 multi-site+clearance,Localize OPM sensor+system as cryogen-free imaging where helium/SQUID constrained,Sell to epilepsy centers wanting pediatric-capable lower-cost MEG via predicate,Medium,Medium-High $15-40M,Class II imaging quantum-sensor export watch,Cerca Magnetics FieldLine QuSpin incumbent SQUID-MEG,OPM sensor performance+shielding/nulling+clinical concordance datasets,Shielding/movement artifacts prevent clinical-grade localization or sensor supply bottlenecked,CLEARED,S-36;S-37
BIO-018,Steerable Closed-Loop tcFUS Neuromodulation Helmet,Electronically-steered phased-array tcFUS helmet with neuronavigation and EEG closed loop for non-invasive deep neuromodulation,Replaces surgical implantation and shallow TMS with non-invasive deep steerable closed-loop stimulation,Electronic steering to deep targets without moving array closed-loop to EEG biomarkers,Treatment-resistant-depression psychiatry centers and neuromod research,Director of Interventional Psychiatry / Neuromodulation,DBS is invasive TMS is shallow and deep circuits are hard to reach non-invasively,rTMS cortical only ECT invasive DBS or medication,TMS cannot reach deep targets DBS requires surgery and neither closes the loop,Multi-element tcFUS phased array neuronavigation EEG integration thermal/cavitation safety,Skull-aberration correction target steering biomarker-driven closed-loop dosing,2026 steered targeting safety;2027 open-label TRD pilot;2028 sham-controlled trial,Non-invasive psychiatric neuromodulation at scale localize phased-array engine,Position between TMS and DBS for TRD via psychiatry device pathway,Low-Medium,Medium $10-25M,Class II/III therapeutic-ultrasound+neuromod evidence burden,Openwater Attune Neurosciences Insightec TMS vendors,Steering+aberration-correction+closed-loop biomarker IP clinical efficacy data,Efficacy does not separate from sham or deep targeting through skull unreliable,CLEARED_WITH_WEAKNESS,S-38;S-11
BIO-019,Bioresorbable Transient Neurostimulator/Sensor Platform,Biodegradable wirelessly powered stimulator/sensor delivering therapy then dissolving eliminating extraction surgery,Makes the implant temporary by design with no second surgery and no chronic foreign body,Programmable on-demand bioresorption with electrophysiological recording/stim and wireless power,Surgical device OEMs in nerve repair cardiac post-op GI surgery,VP R&D Surgical Devices / Bioelectronics,Permanent temporary-use implants require removal surgery and carry chronic risk,Temporary external pacing wires or permanent implants later explanted,Non-resorbable hardware needs extraction and current transient devices lack lifetime+function,Bioresorbable conductors/dielectrics transient power resorbable electrodes,Wireless control lifetime/dose programming recording analytics,2026 transient stimulator;2027 in-vivo efficacy+resorption;2028 GLP+first indication,Localize transient-electronics materials/process for large post-surgical population,License platform to surgical OEMs via novel device pathway,Medium-High,Medium-High $15-35M,Class II/III resorption-byproduct safety burden,Academic transient-electronics Rogers-class early startups,Transient-materials+controlled-resorption+wireless-power IP biocompatibility datasets,Resorption timing/byproducts cannot be controlled safely or function too limited,CLEARED,S-39;S-40
BIO-020,Nanopore Single-Molecule Protein Sequencing Instrument,Nanopore instrument reading single protein/peptide molecules including PTMs for next-gen proteomics,Brings single-molecule amplification-free protein sequencing to a benchtop instrument,Multi-pass single-molecule reading of long protein strands discriminating 20 amino acids+modifications,Pharma proteomics biomarker and academic core labs,Director of Proteomics / Translational Biomarkers,MS proteomics misses low-abundance proteins and single-molecule PTM detail,LC-MS/MS proteomics affinity assays Edman degradation,MS has dynamic-range/sensitivity limits and affinity panels are targeted not de novo,Engineered nanopore arrays low-noise CMOS sensing ASIC fluidics motor enzymes,Signal-to-sequence basecalling PTM detection library prep pipeline,2026 pore+ASIC defined peptides;2027 multi-pass long-strand;2028 early-access core labs,Localize proteomics instrumentation amid life-science self-sufficiency,Sell engine to proteomics labs past MS limits via consumable razor-blade,High,High $30-80M,Research instrument low device burden advanced-sensing export watch,Oxford Nanopore Quantum-Si Nautilus Erisyon,Engineered-pore+ASIC+basecalling IP consumable lock-in,Accuracy/read-length cannot reach proteome-scale utility or MS closes the gap,CLEARED_WITH_WEAKNESS,S-41;S-42
BIO-021,Implantable FUS BBB-Opening Array for CNS Drug Delivery,Multi-emitter skull-replacing implantable ultrasound array repeatedly and reversibly opening the BBB to deliver chemo/biologics,Turns the BBB into a controllable valve making systemic CNS drugs effective,Repeated monthly BBB opening with 9-emitter implant phase I/II safety+survival signal with carboplatin,Neuro-oncology/neurosurgery programs treating recurrent GBM and DMG,Chief of Neuro-Oncology / Neurosurgery,The BBB blocks most chemo/biologics and recurrent GBM outcomes are dismal,Systemic temozolomide Gliadel wafers intra-arterial delivery,Systemic drugs barely cross BBB and existing local methods not repeatable across tumor field,Implantable multi-emitter ultrasound array transcutaneous driver microbubble dosing MRI compatibility,Sonication planning BBB-opening monitoring dose scheduling with chemo,2026 array+driver;2027 expanded GBM cohort;2028 pivotal-enabling trial,Localize implantable-FUS array for large neuro-oncology population,Breakthrough/TCET-eligible CNS-delivery enabler partner with pharma,Low-Medium,High $25-50M,Class III implant+drug combo therapeutic-ultrasound export moderate,Carthera SonoCloud Insightec academic groups,Implant array+repeated-opening protocol+combo clinical datasets,Non-invasive FUS matches efficacy without implant or survival benefit not confirmed,CLEARED,S-43;S-44
BIO-022,Robotic Subretinal Microsurgery Platform for Gene-Therapy Delivery,Tremor-filtering micromanipulator with OCT guidance delivering precise atraumatic subretinal injections for ocular gene therapies,Makes 10um-scale tremor-free subretinal delivery routine removing the human-hand limit,Tremor ~18um to ~1um drift ~212um to ~16um vs manual <=10um placement,Retina surgery centers delivering gene therapies and gene-therapy developers,Director Vitreoretinal Surgery / Surgical Gene Therapy,Manual subretinal injection is at the limit of human tremor risking trauma and inconsistent transduction,Freehand subretinal injection under microscope high variability,Human tremor/drift exceeds the micron-scale precision gene therapy demands,Telemanipulation micromanipulator intraocular instrument intraoperative OCT motion scaling,Tremor filtering OCT-guided depth control injection-rate control autopilot,2026 OCT-integrated bench;2027 in-vivo subretinal;2028 FIH with gene-therapy partner,Localize ophthalmic surgical robot for large inherited-retinal/AMD population,Sell as standard delivery platform bundled with gene-therapy launches,Low-Medium,Medium $10-25M,Class II/III surgical robot moderate,Preceyes academic ophthalmic-robot JnJ Vision,Micron-scale control+OCT integration+gene-therapy delivery datasets/partnerships,Manual delivery proves good enough for transduction or gene-therapy pipeline stalls,CLEARED,S-45;S-46
BIO-023,Implantable Refillable MEMS Micropump for Closed-Loop Delivery,Refillable programmable MEMS micropump with integrated dose-tracking for closed-loop intrathecal/intraocular/local drug delivery,Replaces systemic dosing and passive depots with implantable refillable feedback-controlled local pump,uL/min programmable flow at ~mW power refillable reservoir integrated dose-tracking >100 micro-injections,Chronic-pain ophthalmology and oncology local-delivery programs,Director Pain Medicine / Retina / Targeted Therapeutics,Systemic drugs cause off-target toxicity passive depots cannot titrate and pumps lack feedback,Large intrathecal pumps repeated intravitreal injections oral systemic,No small refillable closed-loop micropump with verified per-dose tracking exists,Electrolysis/electrochemical micropump inert refillable reservoir dose-tracking sensor NFC power,Dosing schedule closed-loop dose verification refill/telemetry app,2026 refillable pump+dose-tracking;2027 in-vivo chronic delivery;2028 first indication,Localize implantable drug-delivery hardware for large chronic-disease population,Differentiated closed-loop local delivery for pain/retina via combo pathway,Medium,Medium $10-25M,Class III drug-delivery implant combo-product complexity,Medtronic SynchroMed Genentech Port Delivery academic MEMS-pump,Micropump+dose-tracking+refill IP combo datasets,Long-acting depots make active pumps unnecessary or dose-tracking fails chronically,CLEARED,S-47
BIO-024,Dual-Chamber Leadless / Leadless Conduction-System Pacing Engine,Miniaturized leadless pacing engine with chip-to-chip wireless sync enabling dual-chamber and conduction-system pacing without leads,Removes the transvenous lead and pocket the dominant failure mode while preserving AV synchrony,Two communicating leadless devices delivering reliable AV-synchronous pacing for months,EP/cardiac-device programs and CRM OEMs,Director Cardiac Electrophysiology / CRM R&D,Leads and pockets drive most pacemaker complications and single-chamber leadless cannot serve most patients,Transvenous dual-chamber pacemakers or single-chamber leadless,Single-chamber leadless covers a minority and transvenous retains lead risk,Miniaturized leadless device helix fixation low-power inter-device comms pacing ASIC,Beat-to-beat synchronization power management conduction-system capture algorithms,2026 inter-device comms+pacing;2027 chronic animal AV-sync;2028 feasibility/OEM,Localize leadless CRM as EP enters VBP as domestic alternative to Aveir,License sync/comms engine or compete on leadless conduction-system pacing,Medium-High,High $30-70M,Class III implant CRM export moderate,Abbott Aveir DR Medtronic Micra Boston Scientific,Inter-device comms+miniaturization+conduction-system capture IP,Battery/comms power budget cannot reach commercial longevity or incumbents lock DR market,CLEARED,S-48;S-49
BIO-025,Spatial Multi-Omics Imaging Instrument,High-throughput spatial-omics imager with high-NA optics multiplexed fluidics and decoding ASIC resolving single-cell RNA/protein in tissue,Moves spatial biology from slow assays to high-throughput instrument with optical+fluidic+decode moat,Single-cell-resolution transcript localization with high transcripts/gene and specificity at scale,Pharma translational/pathology groups and academic spatial cores,Head of Translational Pathology / Spatial Biology Core,Current spatial platforms trade off sensitivity plex and throughput and none is fast enough for routine use,Bulk/single-cell sequencing loses spatial context or slow imaging panels,Throughput segmentation and sensitivity limits keep spatial omics research-only,High-NA imaging multiplexed fluidics cyclic chemistry decode compute automation,Spot-decoding cell segmentation panel design analysis pipeline,2026 optics+fluidics+small panel;2027 throughput/sensitivity benchmarking;2028 early-access pharma installs,Localize spatial-omics instrument amid life-science instrument self-sufficiency,Compete on throughput/robustness for pharma cohorts via consumable razor-blade,Medium,High $25-60M,Research instrument low then LDT/IVD advanced-imaging export watch,10x Genomics Xenium Bruker NanoString CosMx Vizgen MERSCOPE,Optical+fluidic+decode integration+consumable lock-in+panel datasets,Incumbents win throughput/cost first or sequencing-based spatial methods dominate,CLEARED_WITH_WEAKNESS,S-50
```

---

## 7. CSV-ready evidence ledger rows

```csv
source_id,title,publisher_domain,type,impact_label,url,claim_supported,evidence_status
S-01,Pulsed field ablation vs conventional thermal ablation for paroxysmal AF 4-year ADVENT-LTO,nature.com,peer_reviewed_article,high_jcr_q1,https://www.nature.com/articles/s41591-026-04246-4,PFA clinically validated preserved 4-yr effectiveness vs thermal,CLEARED
S-02,PFA to Treat Paroxysmal AF Safety and Effectiveness in AdmIRE Pivotal Trial,ahajournals.org,peer_reviewed_article,high_jcr_q1,https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.124.070333,PFA pivotal safety and effectiveness,CLEARED
S-03,Pulsed Field Ablation A Review of Preclinical and Clinical Studies,mdpi.com,peer_reviewed_article,moderate_q2,https://pmc.ncbi.nlm.nih.gov/articles/PMC12024434/,Biphasic vs monophasic waveform durability 96 vs 45 percent generator engineering,CLEARED
S-04,Redesigning PFA Catheter Form Factors for Lesion Precision Durability Safety,onlinelibrary.wiley.com,peer_reviewed_article,moderate_q3_downgraded,https://pmc.ncbi.nlm.nih.gov/articles/PMC12813649/,Electrode geometry field and contact are next-gen PFA differentiators,CLEARED_WITH_WEAKNESS
S-05,Three-dimensional catheter tip force sensing using multi-core fiber Bragg gratings,frontiersin.org,peer_reviewed_article,moderate_q1q2,https://pmc.ncbi.nlm.nih.gov/articles/PMC10031093/,3D multi-core FBG tip force sensing feasible and compact,CLEARED
S-06,Safety and effectiveness of first contact-force ablation catheter with flexible tip TactiFlex,pubmed.ncbi.nlm.nih.gov,peer_reviewed_article,high_q1,https://pubmed.ncbi.nlm.nih.gov/38204461/,Clinical validation of fiber-optic contact-force sensing,CLEARED
S-07,Electrochemical and electrophysiological considerations for clinical high channel count neural interfaces,link.springer.com,peer_reviewed_article,high_q1,https://link.springer.com/article/10.1557/s43577-023-00537-0,Packaging is the translation barrier for high-channel implants,CLEARED
S-08,Establishment of High Channel-Count Packaging in Active Implantable Medical Devices,onlinelibrary.wiley.com,peer_reviewed_article,moderate_q2,https://onlinelibrary.wiley.com/doi/full/10.1002/jbm.b.70040,Ceramic Pt feedthroughs to 1000-2500 channels per cm2,CLEARED
S-09,Magnetically controlled microrobotic system for stiffness tuning and steering of microcatheters,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s41467-025-67638-z,40x stiffness tuning sub-300um microcatheter integration,CLEARED
S-10,Soft robotic steerable microcatheter for endovascular treatment of cerebral disorders,science.org,peer_reviewed_article,high_q1,https://www.science.org/doi/10.1126/scirobotics.abf0601,Soft steerable neurovascular microcatheter,CLEARED
S-11,Histotripsy as Non-Invasive Non-Thermal Modality for Liver Tumor Ablation,mdpi.com,peer_reviewed_article,moderate_q1q2,https://www.mdpi.com/2077-0383/14/18/6391,Histotripsy non-thermal ablation phased-array aberration correction need,CLEARED
S-12,Histotripsy for Cholangiocarcinoma Liver Tumors feasibility and dosimetry,ncbi.nlm.nih.gov,peer_reviewed_article,moderate_q2,https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9297335/,Histotripsy liver-tumor feasibility,CLEARED
S-13,The FDA plan to phase out animal testing,sciencedirect.com,peer_reviewed_article,high_q1,https://www.sciencedirect.com/science/article/pii/S0167779925005323,FDA NAM shift legitimizes organ-on-chip workflow,CLEARED
S-14,Long-Term Personalized Adaptive Deep Brain Stimulation in Parkinson,jamanetwork.com,peer_reviewed_article,high_q1,https://jamanetwork.com/journals/jamaneurology/fullarticle/2839117,Adaptive closed-loop DBS clinical benefit,CLEARED
S-15,Closed-Loop Adaptive DBS in Parkinson Procedures and Future Perspectives,ncbi.nlm.nih.gov,peer_reviewed_article,moderate_q2,https://pmc.ncbi.nlm.nih.gov/articles/PMC10357172/,Sensing control stim closed-loop architecture,CLEARED
S-16,Electronics-free passive ultrasonic communication link for deep-tissue sensor implants,cell.com,peer_reviewed_article,high_q1,https://www.cell.com/device/fulltext/S2666-9986(25)00068-7,Ultrasonic deep-tissue power and comms link,CLEARED
S-17,Lead-free dual-frequency ultrasound implants for wireless biphasic DBS,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s41467-024-48250-z,Ultrasound-powered mm-scale implant stimulation,CLEARED
S-18,Production of mRNA LNPs using advanced crossflow micromixing,academic.oup.com,peer_reviewed_article,moderate_q2,https://academic.oup.com/jpp/article/76/12/1572/7816331,Microfluidic LNP production and control,CLEARED
S-19,Scalable mRNA siRNA LNP Production Using a Parallelized Microfluidic Device,pubmed.ncbi.nlm.nih.gov,peer_reviewed_article,high_q1,https://pubmed.ncbi.nlm.nih.gov/34189917/,Parallelized mixers 100x throughput conserved attributes,CLEARED
S-20,Rapid evaporative ionisation mass spectrometry in surgery a systematic review,academic.oup.com,peer_reviewed_article,high_q1,https://academic.oup.com/bjs/article/112/11/znaf228/8321352,REIMS real-time intraoperative tissue ID,CLEARED
S-21,Human robotic surgery with intraoperative tissue ID using REIMS,nature.com,peer_reviewed_article,moderate_q1q2,https://www.nature.com/articles/s41598-023-50942-3,REIMS integrated into surgical robotics workflow,CLEARED
S-22,Autonomous medical needle steering in vivo,science.org,peer_reviewed_article,high_q1,https://www.science.org/doi/10.1126/scirobotics.adf7614,Autonomous steerable-needle navigation in tissue,CLEARED
S-23,Toward Transoral Peripheral Lung Access Combining Continuum Robots and Steerable Needles,ncbi.nlm.nih.gov,peer_reviewed_article,moderate_peer_reviewed,https://pmc.ncbi.nlm.nih.gov/articles/PMC5415307/,Transparenchymal access to peripheral lung nodules,CLEARED
S-24,Wireless subdural-contained BCI with 65536 electrodes and 1024 channels,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s41928-025-01509-9,High-channel thin-film uECoG plus wireless ASIC,CLEARED
S-25,High-resolution BCI with electrode scalability and minimally invasive surgery,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s41551-025-01502-9,Minimally invasive high-density BCI array,CLEARED
S-26,Decentralized Point-of-Care Manufacturing of CD19 CAR-T in Mexico,ascopubs.org,peer_reviewed_article,moderate_q1q2,https://ascopubs.org/doi/10.1200/GO-24-00581,Point-of-care closed-system CAR-T feasibility,CLEARED
S-27,Overcoming Access Barriers in European CAR-T Decentralized Manufacturing EASYGEN,sciencedirect.com,peer_reviewed_article,moderate_q2,https://www.sciencedirect.com/science/article/pii/S146532492600900X,Decentralized closed automated CAR-T manufacturing,CLEARED
S-28,Design construction and testing of 1.5T cryogen-free whole-body MRI magnet,iopscience.iop.org,peer_reviewed_article,moderate_q2,https://iopscience.iop.org/article/10.1088/1361-6668/acb467,Conduction-cooled helium-free 1.5T magnet feasible,CLEARED
S-29,Cryogen-free superconducting MRI system a review,sciencedirect.com,peer_reviewed_article,moderate_q2,https://www.sciencedirect.com/science/article/pii/S2667325825002250,Cryogen-free MRI removes helium supply and vent,CLEARED
S-30,China approves world first implantable BCI NEO for medical use,technologyreview.com,journalism_timing,authoritative_journalism_timing,https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/,NMPA first-mover invasive BCI approval China wedge,WATCH
S-31,Magbot Robotic Magnetic Navigation Ablation Catheter Approved by NMPA,biospace.com,company_claim,company_claim,https://www.biospace.com/press-releases/magbot-robotic-magnetic-navigation-ablation-catheter-approved-by-chinas-nmpa,NMPA magnetic-navigation precedent China wedge,WEAK_SIGNAL_ONLY
S-32,Senate clears FDA Modernization Act 3.0 nonclinical NAM reforms,drugdiscoverytrends.com,journalism_timing,authoritative_journalism_timing,https://www.drugdiscoverytrends.com/senate-clears-fda-modernization-act-3-0-aiming-to-align-fda-regulations-with-nonclinical-testing-reforms/,FDAMA 3.0 legitimizes NAMs organ-on-chip,WATCH
S-33,Paradise Ultrasound Renal Denervation System P220023 approval,fda.gov,official_non_article,authoritative_regulator,https://www.fda.gov/medical-devices/recently-approved-devices/paradise-ultrasound-renal-denervation-system-p220023,RDN approved but lacks acute endpoint,CLEARED
S-34,Renal Denervation for Uncontrolled Hypertension NCD CED,cms.gov,official_non_article,authoritative_payer,https://www.cms.gov/medicare/coverage/coverage-evidence-development/renal-denervation-uncontrolled-hypertension,RDN reimbursement gated on evidence endpoint need,CLEARED
S-35,Visual percepts evoked with 96-channel intracortical microelectrode array in human occipital cortex,jci.org,peer_reviewed_article,high_q1,https://www.jci.org/articles/view/151331,Cortical microstimulation evokes discriminable percepts,CLEARED
S-36,MEG with optically pumped magnetometers OPM-MEG next generation functional neuroimaging,sciencedirect.com,peer_reviewed_article,high_q1,https://www.sciencedirect.com/science/article/pii/S0166223622001023,OPM-MEG replaces cryogenic SQUID-MEG,CLEARED
S-37,Using OPMs to replicate task-related responses in next-generation MEG,nature.com,peer_reviewed_article,moderate_q1q2,https://www.nature.com/articles/s41598-024-56878-6,OPM-MEG concordance with SQUID-MEG,CLEARED
S-38,Transcranial focused ultrasound targeting default mode network for depression,frontiersin.org,peer_reviewed_article,moderate_q2,https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1451828/full,Steered tcFUS deep neuromodulation for depression,CLEARED_WITH_WEAKNESS
S-39,Implantable bioresorbable electronic systems for sustainable precision medicine,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s44287-025-00190-6,Bioresorbable transient implant platform feasibility,CLEARED
S-40,An on-demand bioresorbable neurostimulator,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s41467-023-42791-5,Programmable-lifetime resorbable stimulator,CLEARED
S-41,Multi-pass single-molecule nanopore reading of long protein strands,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s41586-024-07935-7,Single-molecule nanopore protein reading,CLEARED
S-42,Toward single-molecule protein sequencing using nanopores,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s41587-025-02587-y,Nanopore protein-sequencing instrument trajectory,CLEARED
S-43,Repeated BBB opening with nine-emitter implantable ultrasound plus carboplatin in recurrent GBM phase I II,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s41467-024-45818-7,Implantable FUS array repeatedly opens BBB safety survival signal,CLEARED
S-44,BBB opening with neuronavigation-guided FUS in pediatric diffuse midline glioma,science.org,peer_reviewed_article,high_q1,https://www.science.org/doi/10.1126/scitranslmed.adq6645,FUS BBB-opening enables CNS drug delivery,CLEARED
S-45,Advantages of robotic assistance over manual approach in simulated subretinal injections,nature.com,peer_reviewed_article,moderate_q2,https://www.nature.com/articles/s41434-021-00262-w,Robotic subretinal drift 16 vs 212um tremor 1 vs 18um,CLEARED
S-46,Robotising vitreoretinal surgeries,nature.com,peer_reviewed_article,moderate_q1q2,https://www.nature.com/articles/s41433-024-03149-3,Robotic vitreoretinal microsurgery for gene therapy delivery,CLEARED
S-47,Active implantable drug delivery systems engineering factors challenges opportunities,pubs.rsc.org,peer_reviewed_article,high_q1,https://pubs.rsc.org/en/content/articlehtml/2025/lc/d5lc00131e,Refillable closed-loop MEMS micropump engineering,CLEARED
S-48,A Dual-Chamber Leadless Pacemaker,pubmed.ncbi.nlm.nih.gov,peer_reviewed_article,high_q1,https://pubmed.ncbi.nlm.nih.gov/37212442/,Dual-chamber leadless AV-synchronous pacing,CLEARED
S-49,Six-month electrical performance of first dual-chamber leadless pacemaker,heartrhythmjournal.com,peer_reviewed_article,high_q1,https://www.heartrhythmjournal.com/article/S1547-5271(24)02525-6/fulltext,Leadless inter-device sync durability,CLEARED
S-50,Systematic benchmarking of imaging spatial transcriptomics platforms in FFPE tissues,nature.com,peer_reviewed_article,high_q1,https://www.nature.com/articles/s41467-025-64990-y,Spatial-omics platform tradeoffs sensitivity plex throughput,CLEARED
S-51,Impact of volume-based procurement on coronary stent use interrupted time series,ncbi.nlm.nih.gov,peer_reviewed_article,moderate_q2,https://pmc.ncbi.nlm.nih.gov/articles/PMC12581602/,China VBP compresses commodity-consumable margins high-end localization wedge,CLEARED
S-52,Final Notice Transitional Coverage for Emerging Technologies TCET,cms.gov,official_non_article,authoritative_payer,https://www.cms.gov/newsroom/fact-sheets/final-notice-transitional-coverage-emerging-technologies-cms-3421-fn,Expedited Medicare coverage pathway for breakthrough devices,CLEARED
S-53,OCT predictors of clinical outcomes after stent implantation ILUMIEN IV,academic.oup.com,peer_reviewed_article,high_q1,https://academic.oup.com/eurheartj/article/45/43/4630/7743289,IVOCT did not beat angiography on hard endpoints supports reject,CLEARED
```

---

### Notes on evidence integrity
- Every candidate's core technical or customer-pain claim is supported by at least one peer-reviewed Q1/Q2 article or an authoritative regulator/payer source (FDA, CMS).
- China first-mover BCI approval (S-30) and Magbot NMPA (S-31) are labeled journalism/company and used only for the China-wedge timing — not as technical proof. They are marked WATCH / WEAK_SIGNAL_ONLY and must be replaced with NMPA primary records before scoring those wedges.
- FDAMA 3.0 (S-32) is journalism-timing supporting the regulatory-window narrative for BIO-006; the technical NAM claim rests on S-13 (Trends in Biotechnology, Q1).
- No arXiv/bioRxiv/medRxiv, company blog, or market-report site is counted as academic evidence anywhere in this file.
