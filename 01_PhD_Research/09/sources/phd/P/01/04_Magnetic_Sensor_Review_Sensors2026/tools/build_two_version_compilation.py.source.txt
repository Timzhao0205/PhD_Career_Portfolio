from __future__ import annotations

import csv
from collections import defaultdict
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "Magnetic_Sensor_Review_Two_Version_Compilation.docx"
REGISTRY = ROOT / "outputs" / "reference_registry.csv"

BLUE = "2E74B5"
DARK_BLUE = "1F4D78"
INK = "0B2545"
MUTED = "5D6875"
LIGHT_BLUE = "E8EEF5"
LIGHT_GRAY = "F2F4F7"
CALLOUT = "F4F6F9"
WHITE = "FFFFFF"
BLACK = "000000"
GOLD = "7A5A00"
RED = "9B1C1C"


OUTLINE_OPTIONS = [
    ("A. Sensor-family primary", "Technology taxonomy is the backbone; applications follow as a cross-cutting tail.", "Best fit with the project brief and conventional Sensors review expectations."),
    ("B. Application primary", "Energy, transportation, industry, and biomedicine are the backbone; device physics is condensed into a primer.", "Best for domain readers, but risks repetition and thinner device physics."),
    ("C. Capability-envelope primary", "Measurement regimes and performance envelopes organize the story.", "Most distinctive conceptually, but every boundary needs defensible quantitative evidence."),
    ("D. Value-chain / TRL primary", "Devices, systems, deployments, standards, and investment gates form a commercialization narrative.", "Strongest business voice, but least conventional for a technical sensor review."),
]

RECOMMENDED_OUTLINE = [
    ("1. Introduction (~7%)", [
        "1.1 Why magnetic sensing matters: one measurand, four industries, and the range-resolution-bandwidth-SWaP-C-temperature trade space.",
        "1.2 Scope, method, and contributions: vendor-neutral narrative review; recent state of the art plus foundational sources; explicit exclusions.",
        "1.3 Paper roadmap, with a capability map and two comparison tables as navigation aids.",
    ]),
    ("2. Technologies and current applications (~31%)", [
        "2.1 Figures of merit and commercial-versus-pioneering taxonomy.",
        "2.2 Hall sensors; 2.3 AMR/GMR/TMR; 2.4 fluxgate; 2.5 search-coil; 2.6 GMI; 2.7 SQUID; 2.8 OPM/SERF; 2.9 NV diamond; 2.10 other emerging families.",
        "2.11 Cross-family comparison plus full subsections for energy, transportation, industrial/manufacturing, and biomedical deployments.",
        "Table 1: sourced performance comparison. Table 2: family-by-domain deployment matrix.",
    ]),
    ("3. Future applications and methods (~28%)", [
        "3.1 Learned calibration, drift compensation, offset/noise mitigation, and virtual sensing.",
        "3.2 ML-assisted readout/control, denoising, adaptive compensation, and predictive maintenance.",
        "3.3 Sensor fusion, arrays, magnetic-inertial systems, MagNav, and source localization.",
        "3.4 Digital twins: demonstrated machine-level twins versus aspirational sensor-level twins.",
    ]),
    ("4. Potential and standards (~28%)", [
        "4.1 TRL and attributed market landscape; 4.2 automotive functional safety and qualification.",
        "4.3 Industrial/energy standards; 4.4 medical pathways; 4.5 metrology and traceability.",
        "4.6 Seven-question company/investor de-risking checklist.",
    ]),
    ("5. Conclusion (~6%)", [
        "No universal winner; system design and computation increasingly determine usable performance; close with evidence-backed open challenges and an outlook to 2030.",
    ]),
]


TECHNICAL = [
    ("Section 1", "Why magnetic sensing matters", "Magnetic sensing turns current, position, motion, material state, and physiological activity into contactless measurements. The literature supports a capability landscape spanning biomagnetic fT-pT signals through industrial multi-tesla fields, but the useful comparison is multidimensional: resolution, bandwidth, dynamic range, drift, size, power, cost, and temperature must be considered together.", "This establishes the review's core thesis: no family is globally superior, so device choice is an application-specific trade.", "Lenz1990review; Lenz2006magsensors; Ripka2010advancesIEEE; Tumanski2013modern; MagSensorsReview2021ERX; Murzin2020biomedsensors"),
    ("Section 1", "Scope and review method", "Use a vendor-neutral narrative review with a recent-state-of-the-art window supplemented by classics for physical principles. Separate peer-reviewed evidence, standards, vendor device specifications, market estimates, and author assessments; every quantitative envelope or non-obvious claim should remain traceable to the registry.", "This protects the paper from overclaiming and makes the dual technical/business audience credible.", "PROJECT_BRIEF; 00_target_journal_brief; 70_bibliography_report"),
    ("Section 1", "Signature synthesis artifacts", "Build Fig. 1 as a sourced field-range-versus-bandwidth capability map. Use Table 1 for performance and maturity and Table 2 for family-by-domain fit; leave cells unreported when the underlying literature has not yet supplied a verified value.", "The paper becomes useful as a selection reference, while visible evidence gaps are safer than invented precision.", "Lenz2006magsensors; Zheng2019mrroadmap; Stage30 comparison table; Stage40 domain matrix"),

    ("Section 2", "Hall effect: silicon CMOS and spinning-current readout", "Hall plates provide true dc response, very wide dynamic range, low cost, and straightforward CMOS integration. Their limiting issues are low raw sensitivity, offset, 1/f noise, stress drift, and the bandwidth/ripple trade introduced by spinning-current or chopping; integrated current sensors are strongest in high-field, position, and power applications.", "Hall remains the volume baseline against which newer families must justify sensitivity, integration, reliability, or cost advantages.", "Popovic2004hallbook; Munter1990spinning; Crescentini2022hallcurrent; JEET2019lownoisehall; SiHall3axis2025msn"),
    ("Section 2", "Hall effect: GaN/2DEG harsh-environment variants", "AlGaN/GaN and InAlN/GaN 2DEG Hall devices extend Hall physics to extreme temperatures. Alpert et al. report operation through 576 C and comparatively stable current-scaled sensitivity, but offset treatment, external readout, supplier depth, and system qualification remain barriers; the author's 2023 IEEE Sensors Letters self-citation still needs manual insertion.", "This is a credible pioneering route for aerospace, rotating machinery, well logging, and fusion environments where silicon electronics cannot survive locally.", "Alpert2020gan2deg; GaNHEMThall2012jpcs; author self-citation [manual insertion required]"),
    ("Section 2", "Magnetoresistive ladder: AMR, GMR, and TMR", "AMR is mature and inexpensive but offers the smallest MR signal and may need set/reset recovery. GMR provides larger response and proven automotive/biosensor use but retains hysteresis, saturation, blocking-temperature, and low-frequency-noise concerns. TMR/MTJ offers the largest transfer signal, low power, and potentially pT-class detectivity, yet barrier uniformity, 1/f noise, hysteresis, ESD, and field-range engineering remain central.", "The AMR-GMR-TMR progression explains why TMR is the most important cross-domain challenger to Hall while older xMR families remain commercially durable.", "Jogschies2015mrindustrial; Freitas2016spintronic; Zheng2019mrroadmap; Zhou2022TMRchapter; Egelhoff2009picoteslaMTJ; TMRsubpT2025APL; Spintronic2024npj"),
    ("Section 2", "Fluxgate magnetometers", "Fluxgates use driven ferromagnetic cores and harmonic detection to measure weak dc fields with high accuracy and stability. They occupy the precision nT-pT niche between mass-market xMR/Hall and quantum instruments; excitation power, size, heading error, offset drift, and core-related noise limit miniaturization.", "Fluxgate is the established reference for navigation, space, geophysics, and precision dc metering when cryogenics or atomic instrumentation is impractical.", "Ripka2003fluxgateadv; Fluxgate2021Sensors; Dressler2021orthofluxgate; Miles2016fluxgateCubeSat"),
    ("Section 2", "Search-coil and induction sensors", "Search coils measure dB/dt and therefore excel at ac fields, transient capture, geophysics, eddy-current inspection, and wideband power sensing; they cannot measure static fields without motion or modulation. Sensitivity, coil size, turns, core losses, resonance, and amplifier noise set the bandwidth-size trade.", "They remain indispensable because passive, robust ac measurement can outperform more complex dc-capable sensors in the right frequency regime.", "Tumanski2007inductioncoil; Roux2008themisSCM; Coillot2010dualband"),
    ("Section 2", "Giant magnetoimpedance (GMI)", "GMI uses the field dependence of high-frequency impedance in soft magnetic wires or films. It can deliver high sensitivity and compact form factors, including picotesla laboratory demonstrations, but drive-frequency electronics, nonlinear response, temperature dependence, fabrication repeatability, and a narrow commercial ecosystem constrain broad adoption.", "GMI is a technically promising bridge between conventional electronics and weak-field sensing, but its commercialization evidence is thinner than its sensitivity literature.", "Phan2008gmiprogress; Dolabdjian2016gmichapter; Uchiyama2020picoteslaMI"),
    ("Section 2", "SQUID magnetometers", "SQUIDs convert magnetic flux into a superconducting interference signal and remain the benchmark for ultra-low noise and broad weak-field performance. Their limitations are cryogenics, shielding, system cost, maintenance, and deployment complexity, though high-Tc and cryogen-free system improvements reduce some burdens.", "SQUID defines the incumbent performance ceiling in biomagnetism and metrology, so every room-temperature challenger should be compared against the full system, not only the sensing element.", "Fagaly2006squidRSI; Clarke2018squidfocus"),
    ("Section 2", "Optically pumped magnetometers (OPM/SERF)", "OPMs infer field from optically interrogated atomic spin dynamics. SERF devices achieve sub-fT-class sensitivity under near-zero-field conditions and have enabled wearable MEG/MCG arrays; dynamic range, bandwidth, crosstalk, heating, field control, and calibration of many channels remain system-level constraints.", "OPMs are the strongest cryogen-free challenger to SQUID in biomagnetism because they permit closer, movable, and potentially more accessible measurements.", "Kominis2003subfemtotesla; Shah2007microfabvapor; Tierney2019OPM; Boto2018wearableMEG; Kitching2018chipscaleatomic; Brickwedde2024OPMMEG; Pedersen2022OPMepilepsy"),
    ("Section 2", "NV-diamond magnetometry", "Nitrogen-vacancy centers provide room-temperature quantum sensing with optical readout, vector capability, and spatial resolution from nanoscale probes to ensembles. Sensitivity depends strongly on spin coherence, photon collection, readout architecture, diamond quality, and microwave/optical overhead; current-sensing deployment evidence is still partly preprint-stage.", "NV sensing is distinctive where spatially resolved, non-invasive, or harsh-environment quantum measurement matters more than near-term commodity cost.", "Barry2020NVdiamond; NVsub10pT2024prapplied; Santagati2019fieldlearning; Zhang2024dnnNVreadout; NVcurrentPPM2023 [preprint]"),
    ("Section 2", "Other emerging and reference families", "Magnetoelectric composites seek passive or low-power pT-class sensing but remain dominated by resonance, vibration, packaging, and reproducibility challenges. MEMS Lorentz-force devices offer CMOS-compatible resonant transduction but face vacuum/Q-factor and bias-current tradeoffs. Fiber/magneto-optic sensors provide isolation and immunity for power systems, while proton/Overhauser/CPT instruments are especially valuable as absolute or traceability references.", "These families should be treated concisely and honestly: they broaden the design space, but their evidence and maturity differ sharply.", "Bichurin2021MEreview; Li2017nemsME; Nan2013selfbiasME; HerreraMay2009memsresonant; Rostami2023fbgreview; Silva2012opticalcurrent; Ge2016overhauser; Kitching2018chipscaleatomic"),

    ("Section 2", "Energy applications", "Hall and TMR dominate isolated dc and traction-inverter current sensing; search-coil/Rogowski and optical approaches add bandwidth or insulation advantages. Fluxgate supports precision dc metering, while distributed magnetic measurements enable overhead-line monitoring, battery-current estimation, and condition monitoring. Claimed market shares should remain qualitative unless tied to a primary, current source.", "Energy systems reward galvanic isolation, bandwidth, low drift, and fault tolerance, making current sensing a major battleground between Hall incumbency and TMR performance.", "Crescentini2022hallcurrent; Khawaja2017overheadlines; Chen2024contactlessOHL; Xu2025TMRsmartgrid; Silva2012opticalcurrent"),
    ("Section 2", "Transportation applications", "Automotive magnetic sensors support position, angle, speed, wheel sensing, motor commutation, traction-current measurement, and navigation. Hall and xMR win through integration and qualification; fluxgate retains precision navigation/space niches. The key technical frame is not maximum sensitivity but operation across temperature, EMC, stray fields, air gaps, redundancy, and functional-safety diagnostics.", "Transportation is the highest-volume proof that packaging, diagnostics, and qualification can matter more than the sensing effect itself.", "Treutler2001automotive; Miles2016fluxgateCubeSat; ISO26262; CISPR25; ISO11452"),
    ("Section 2", "Industrial and manufacturing applications", "Magnetic flux leakage, eddy-current testing, GMR arrays, motor stray-flux monitoring, encoders, robotics, and proximity sensing convert field patterns into defect, condition, or motion information. Array design, inverse models, calibration, and environmental robustness determine whether laboratory sensitivity becomes actionable maintenance evidence.", "This domain is the natural bridge to machine learning because repeatable magnetic signatures can support non-destructive inspection and predictive maintenance.", "Rifai2016GMReddyreview; Bailey2017eddyCUI; Mazaheri2022strayflux; Louzada2025strayfluxML"),
    ("Section 2", "Biomedical applications", "SQUID and OPM support MEG/MCG, with OPM enabling wearable and bedside geometries. GMR/TMR biosensors detect magnetic labels in lab-on-chip formats; MPI images tracer response; magnetic tracking localizes instruments. Clinical usefulness depends on shielding, calibration, source localization, biocompatibility, workflow, and regulatory evidence, not sensor sensitivity alone.", "Biomedicine shows how a sensor becomes a medical system only after the inverse problem, patient interface, and regulatory pathway are solved together.", "Brisinda2023clinicalMCG; Iwata2024bedsideMCG; Brickwedde2024OPMMEG; Pedersen2022OPMepilepsy; Wang2024magbiosensorPOCT; Wu2019MPIneuro; He2025EMtracking"),

    ("Section 3", "Learned calibration and data-driven models", "Machine learning can learn cross-axis, temperature, installation, and environmental corrections and can support calibration transfer or inverse reconstruction. It should augment, not replace, physical calibration and front-end offset/noise suppression; distribution shift and traceability must be quantified.", "The highest-value near-term use of learning is often turning an imperfect, inexpensive sensor into a stable system rather than improving the sensing material itself.", "Kok2016magcal; Shetty2026AMRcalibNN; Karniadakis2021piml; Kadlec2009softsensor"),
    ("Section 3", "ML-assisted readout, control, and diagnostics", "Bayesian and neural methods can accelerate quantum readout, denoise classical signals, and classify machine faults. Demonstrated magnetic closed-loop nulling is presently model-based rather than learned, so adaptive biasing should remain an outlook claim; learned aging compensation lacks a peer-reviewed anchor.", "This distinction keeps the section forward-looking without presenting prototypes or adjacent methods as production-ready capabilities.", "Santagati2019fieldlearning; Zhang2024dnnNVreadout; Homrighausen2023edgeNV; Sakib2022mcgedgeDL; Holmes2018biplanarnulling; Louzada2025strayfluxML"),
    ("Section 3", "Fusion, arrays, and multi-modality", "Magnetic-inertial fusion, magnetic-field SLAM, gradiometry, dense arrays, tSSS, and source localization exploit spatial structure that a single sensor cannot observe. Performance depends on map stability, array calibration, synchronization, interference rejection, and an explicit inverse model.", "The field's frontier is increasingly a coordinated sensing system that combines modest elements into information unavailable from any single channel.", "KokSolin2018magslam; Viset2022ekfmagslam; Taulu2006tsss; Hamalainen1993meg"),
    ("Section 3", "Digital twins", "A digital twin must remain linked to a physical asset and update with operational data; a static simulation is not enough. Machine-level twins using magnetic condition signals are demonstrated, but a traceable sensor-level twin that owns calibration state, uncertainty, drift, and health remains largely aspirational.", "Using a strict definition prevents the paper from inflating ordinary modeling into a trend claim and identifies a genuine research gap.", "Glaessgen2012dtparadigm; Wright2020modeltwin; Tao2019dtindustry; Rasheed2020dtenablers; Falekas2021dtmachines; EnergiesDT2025faultdiag"),

    ("Section 4", "Technology readiness and market landscape", "Mass-market Hall and xMR, established-niche fluxgate/search-coil/SQUID, and pioneering OPM/NV/ME/MEMS occupy different readiness and market-pull positions. TRL ratings are author assessments; market sizes are attributed grey-literature ranges and must not be averaged into false precision. TMR acquisitions and product launches are useful competitive signals, not scientific validation.", "This lets technical performance, manufacturing maturity, and commercial evidence be compared without mixing fundamentally different source types.", "GrandView2025magmarket [market]; Allegro2023crocus [press]; TDK2016micronas [press]; Stage60 TRL assessment"),
    ("Section 4", "Automotive functional safety and qualification", "ISO 26262 structures hazard analysis, ASIL development, diagnostics, and safety cases; IEC 61508 is the broader parent framework. SOTIF, cybersecurity, AI-safety guidance, and EMC standards expand the gate from component reliability to intended-function limitations, connected systems, learned components, and electromagnetic robustness.", "Qualification is a market gate: a sensitive element without redundancy, diagnostics, traceable development, and EMC robustness is not an automotive product.", "ISO26262; IEC61508; ISO21448SOTIF; ISOSAE21434; ISOPAS8800; ISOIECTR5469; CISPR25; ISO11452"),
    ("Section 4", "Industrial and energy standards", "IEC 61508 governs functional-safety lifecycle concepts and IEC 62443 addresses industrial-control cybersecurity. Instrument-transformer, digital-substation, and EMC requirements must be tied to the exact deployment; IEC 61850-9-2 is named in the existing brief but still needs a registry entry.", "Industrial adoption depends on interoperable, secure, certifiable systems, so standards mapping should follow the application rather than the sensor family alone.", "IEC61508; IEC62443; IEC 61850-9-2 [registry entry needed]"),
    ("Section 4", "Medical device pathways", "IEC 60601-1, ISO 13485, and ISO 14971 frame electrical safety, quality management, and risk management. Regulatory pathways such as FDA 510(k) or CE marking require a defined clinical use, system-level verification, and risk controls; the Ricoh MEG clearance is an illustrative commercial precedent, not a general approval shortcut.", "Medical translation is governed by the whole measurement workflow and intended use, not by sensor performance in isolation.", "IEC60601; ISO13485; ISO14971; RicohMEG2024clearance [press]"),
    ("Section 4", "Metrology and traceability", "Traceability requires calibration against recognized field references, an uncertainty budget, controlled environmental conditions, and documented transfer through the measurement chain. NMR/Overhauser methods and PTB/NIST facilities provide anchors; learned corrections introduce model version, training-domain, and change-control questions into that chain.", "A computed sensor can only become trusted infrastructure if its algorithmic contribution is calibrated, versioned, and included in uncertainty and conformity evidence.", "Lenicek2022calibstd; PTBmetrology; Ge2016overhauser; ISOIECTR5469"),
    ("Section 4", "Company and investor de-risking", "The existing seven-question diligence frame should test: real application pull; reproducible performance under operating conditions; manufacturability/yield; calibration burden; qualification pathway; supply-chain concentration; and whether computation improves value without creating unbounded assurance risk. Each conclusion should be labeled as sourced fact or author assessment.", "This converts the review from a technology catalogue into a practical decision tool while preserving scholarly boundaries.", "Stage60 risk register; ISO26262; ISO13485; Lenicek2022calibstd; GrandView2025magmarket [market]"),

    ("Section 5", "Synthesis and outlook", "The evidence supports three closing claims: no sensor wins across the full trade space; system architecture and computation increasingly determine usable performance; and the major open problems are benchmark data, distribution shift, long-term drift, array calibration, metrological treatment of learned models, and qualification of computed sensing chains. Outlook statements should distinguish demonstrated products, emerging prototypes, and research hypotheses.", "This gives the conclusion a defensible message instead of a generic forecast.", "Stage30-60 synthesis; Karniadakis2021piml; Wright2020modeltwin; ISOIECTR5469"),
]


PLAIN = [
    ("Section 1", "The big picture", "Magnetic sensors let us measure electricity, movement, machinery, and even body signals without touching the source. Different jobs demand very different levels of sensitivity, speed, temperature tolerance, cost, and size.", "There is no single best sensor. The review matters because it helps readers choose the right compromise for a real job.", "Lenz1990review; Lenz2006magsensors; Murzin2020biomedsensors"),
    ("Section 1", "How to keep the review trustworthy", "Use recent research for the frontier and classic papers for fundamentals. Clearly label peer-reviewed results, standards, company specifications, market estimates, and the authors' own judgments.", "Readers can see what is proven, what is commercially claimed, and what is still a forecast.", "PROJECT_BRIEF; 70_bibliography_report"),
    ("Section 1", "The two maps readers need", "One chart should show where each sensor works best. One table should compare performance and maturity, and another should show which industries actually use each family.", "These become the paper's practical shortcut for engineers, managers, and investors.", "Stage30 comparison table; Stage40 domain matrix"),

    ("Section 2", "Hall sensors", "Hall sensors are cheap, rugged, easy to put on a chip, and good for measuring strong fields, position, and electrical current. They are less sensitive than many alternatives and need electronics to cancel offset and drift. GaN versions can work at temperatures where silicon fails, but they are not yet a broad catalog product.", "Hall is the incumbent technology: alternatives must beat it on a benefit customers will pay for.", "Popovic2004hallbook; Crescentini2022hallcurrent; Alpert2020gan2deg"),
    ("Section 2", "AMR, GMR, and TMR", "These sensors change resistance when a magnetic field changes the direction of magnetization. AMR is mature and simple, GMR produces a larger signal, and TMR can be much more sensitive and power-efficient. All must manage hysteresis, saturation, temperature, and low-frequency noise.", "TMR is the clearest challenger to Hall across cars, power electronics, industry, and biosensing.", "Jogschies2015mrindustrial; Freitas2016spintronic; Zheng2019mrroadmap; Zhou2022TMRchapter"),
    ("Section 2", "Fluxgate", "Fluxgates repeatedly drive a magnetic core and detect how an outside field changes its response. They measure weak, steady fields accurately, but are larger and consume more power than chip-scale sensors.", "They are a proven choice when accuracy and stability matter more than minimum size or cost.", "Ripka2003fluxgateadv; Fluxgate2021Sensors"),
    ("Section 2", "Search-coil", "A search coil detects changing magnetic fields. It is passive, robust, and fast, but it cannot directly measure a field that is perfectly still.", "For ac power, transient events, and inspection, a simple coil can be the best tool.", "Tumanski2007inductioncoil; Roux2008themisSCM"),
    ("Section 2", "GMI", "GMI devices can be very sensitive by measuring how a soft magnetic material's high-frequency electrical impedance changes with field. They need specialized drive electronics and have less commercial depth than Hall or xMR.", "The science is promising, but the product ecosystem still needs proof.", "Phan2008gmiprogress; Uchiyama2020picoteslaMI"),
    ("Section 2", "SQUID", "SQUID systems are among the most sensitive magnetic instruments available. They require superconducting operation, cooling, shielding, and expensive system support.", "They set the benchmark for weak-field measurement, but their total system burden creates room for room-temperature alternatives.", "Fagaly2006squidRSI; Clarke2018squidfocus"),
    ("Section 2", "OPM/SERF", "OPMs use atoms and light to measure magnetic fields. They can reach extraordinary sensitivity without cryogenic cooling and can be placed close to a moving person, but they need careful field control, heating, calibration, and multi-sensor coordination.", "They could make brain and heart magnetic imaging more wearable and accessible.", "Kominis2003subfemtotesla; Boto2018wearableMEG; Tierney2019OPM"),
    ("Section 2", "NV diamond", "Special defects in diamond behave like tiny quantum compasses that can be read with light. They work at room temperature and can map fields at very small scales, but the optics, microwaves, diamond quality, and manufacturing cost remain demanding.", "NV sensors open measurements that combine high spatial resolution with quantum sensitivity.", "Barry2020NVdiamond; NVsub10pT2024prapplied"),
    ("Section 2", "Other emerging and reference sensors", "Magnetoelectric and MEMS devices aim for small, low-power sensing; fiber-optic sensors offer electrical isolation; proton, Overhauser, and atomic resonance instruments provide highly stable references. Their maturity ranges from laboratory research to specialized instruments.", "They should be included, but not presented as equally ready for mass adoption.", "Bichurin2021MEreview; HerreraMay2009memsresonant; Rostami2023fbgreview; Ge2016overhauser"),

    ("Section 2", "Energy", "Magnetic sensors measure current in inverters, batteries, power lines, and charging systems without placing a resistor directly in the high-power path. Hall is common; TMR, coils, fluxgate, and optical methods win where sensitivity, speed, accuracy, or insulation matters more.", "Better current sensing improves efficiency, protects equipment, and supports safer electrification.", "Crescentini2022hallcurrent; Khawaja2017overheadlines; Xu2025TMRsmartgrid"),
    ("Section 2", "Transportation", "Cars and other vehicles use magnetic sensors for position, speed, steering, motor control, current measurement, and navigation. The winning device must survive heat, vibration, interference, stray fields, and safety checks for years.", "This is a huge market, but qualification and reliability are the real barriers to entry.", "Treutler2001automotive; ISO26262; CISPR25"),
    ("Section 2", "Industry and manufacturing", "Sensors can find cracks or corrosion, watch motors and bearings, and measure robotic motion by reading magnetic patterns. A useful system must turn those patterns into a reliable maintenance or control decision.", "This is where sensor arrays and machine learning can create clear operational value.", "Rifai2016GMReddyreview; Bailey2017eddyCUI; Mazaheri2022strayflux"),
    ("Section 2", "Biomedicine", "Very sensitive instruments can measure the magnetic fields of the brain and heart. Other magnetic systems detect biological labels, image tracers, or track tools inside the body.", "The opportunity is large, but clinical workflow, shielding, algorithms, safety, and regulation matter as much as the sensor.", "Brickwedde2024OPMMEG; Brisinda2023clinicalMCG; Wang2024magbiosensorPOCT; Wu2019MPIneuro"),

    ("Section 3", "Learning better calibration", "Software can learn how temperature, installation, nearby materials, and cross-axis errors distort a sensor. It can correct those patterns, but only inside conditions that were adequately represented and tested.", "This may make inexpensive sensors behave like better systems, reducing calibration cost and drift.", "Kok2016magcal; Shetty2026AMRcalibNN; Karniadakis2021piml"),
    ("Section 3", "Faster readout and smarter diagnostics", "Machine learning can speed quantum measurements, clean noisy signals, and recognize machine-fault patterns. Claims about self-adjusting magnetic control and aging correction are still early and should be labeled as outlook.", "The near-term value is decision-quality information, not magical removal of hardware limitations.", "Santagati2019fieldlearning; Zhang2024dnnNVreadout; Sakib2022mcgedgeDL; Louzada2025strayfluxML"),
    ("Section 3", "Fusion and arrays", "Several sensors can work together with inertial, optical, or thermal data to locate sources and reject interference. The challenge is keeping every channel synchronized and calibrated while solving the right mathematical inverse problem.", "A coordinated system can reveal information that one very sensitive sensor cannot.", "KokSolin2018magslam; Viset2022ekfmagslam; Taulu2006tsss"),
    ("Section 3", "Digital twins", "A real digital twin stays connected to a physical machine or sensor and updates as the physical system changes. Machine twins that use magnetic condition data exist; complete sensor twins that track calibration and uncertainty are mostly a research goal.", "This is an important opportunity, but the paper should not call every simulation a twin.", "Wright2020modeltwin; Tao2019dtindustry; Falekas2021dtmachines"),

    ("Section 4", "Readiness and markets", "Hall and xMR are mass-market; fluxgate, search-coil, and SQUID serve established niches; OPM, NV, magnetoelectric, and many MEMS concepts are earlier or more specialized. Market reports disagree, so their numbers must be attributed rather than combined.", "Investors should distinguish impressive sensitivity from repeatable manufacturing and customer adoption.", "GrandView2025magmarket [market]; Stage60 TRL assessment"),
    ("Section 4", "Automotive rules", "Automotive standards require companies to analyze hazards, design diagnostics and redundancy, control development, resist electromagnetic interference, and increasingly address cybersecurity and AI behavior.", "Meeting these rules is often harder and more expensive than making a promising sensor sample.", "ISO26262; ISO21448SOTIF; ISOSAE21434; ISOPAS8800; CISPR25"),
    ("Section 4", "Industrial and energy rules", "Industrial safety and cybersecurity standards govern the complete system, including how measurements are communicated and protected. The exact standard depends on whether the sensor is used in a machine, grid asset, safety loop, or digital substation.", "Standards determine whether a device can be integrated into critical infrastructure.", "IEC61508; IEC62443; IEC 61850-9-2 [to add]"),
    ("Section 4", "Medical rules", "Medical products need electrical safety, quality management, risk management, evidence for their intended use, and regulatory clearance. A laboratory magnetometer does not become a medical device automatically.", "Commercial success depends on the full clinical system and regulatory pathway.", "IEC60601; ISO13485; ISO14971; RicohMEG2024clearance [press]"),
    ("Section 4", "Calibration and trust", "A trusted measurement must be linked to recognized references and have a documented uncertainty. When software changes the result, its training conditions and version also become part of the measurement chain.", "Without traceability, a more accurate-looking number may still be unusable for certification or safety decisions.", "Lenicek2022calibstd; PTBmetrology; Ge2016overhauser"),
    ("Section 4", "Questions for a company or investor", "Ask whether customers truly need the capability, whether performance survives real conditions, whether manufacturing is repeatable, how expensive calibration is, what qualification is required, where the supply chain is fragile, and whether software adds controllable value.", "These questions expose the difference between a good paper, a good prototype, and a good business.", "Stage60 risk register"),

    ("Section 5", "The takeaway", "No technology wins everywhere. The strongest future products will combine a suitable sensing element with packaging, calibration, arrays, algorithms, standards, and a clear use case.", "The review's most important message is that usable systems—not headline sensitivity alone—create scientific and commercial impact.", "Stage30-60 synthesis"),
]


GAPS = [
    ("Hall (Si)", "Thin", "Verify spectral noise floor and bandwidth from the full-text current-sensor review."),
    ("GaN/2DEG Hall", "Thin", "Add author's verified 2023 citation; find version of record for spinning-current work."),
    ("AMR/GMR", "Thin", "Extract detectivity spectra and field-range/bandwidth values from the MR roadmap."),
    ("TMR", "Strong", "Re-check abstract-level 97 pT/sqrt(Hz) figure; use stronger primary anchors where possible."),
    ("Fluxgate", "Thin", "Verify FM-OFG noise values and attribution from full text."),
    ("Search-coil", "Strong", "Add the exact application-specific instrument-transformer/EMC standards during drafting."),
    ("GMI", "Thin", "Confirm MEMS-GMI numbers and add future-methods or supplier evidence if available."),
    ("SQUID", "Strong", "Re-check MCG amplitude context before quoting exact numbers."),
    ("OPM/SERF", "Thin", "Extract bandwidth and dynamic-range values from full text."),
    ("NV diamond", "Thin", "Find version of record for current sensing or clearly label it preprint-stage."),
    ("Magnetoelectric", "Thin", "Verify sensitivity figure; future-methods and standards coverage remains missing."),
    ("MEMS Lorentz", "Thin", "Verify performance figures; keep maturity claims conservative."),
    ("Fiber/magneto-optic", "Thin", "Translate performance to magnetic units where defensible; add IEC 61850-9-2."),
    ("Overhauser/CPT", "Thin", "Replace vendor-only performance specifications with peer-reviewed sources if possible."),
    ("Future methods", "Thin", "Search for peer-reviewed learned-aging compensation, sensor-level twins, MagNav accuracy, and ISO 26262+ML analysis."),
]


def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_margins(cell, top=80, start=120, bottom=80, end=120):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")


def set_repeat_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = OxmlElement("w:tblHeader")
    tbl_header.set(qn("w:val"), "true")
    tr_pr.append(tbl_header)


def set_table_geometry(table, widths_dxa, indent=120):
    total = sum(widths_dxa)
    table.autofit = False
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    tbl_pr = table._tbl.tblPr
    tbl_w = tbl_pr.find(qn("w:tblW"))
    if tbl_w is None:
        tbl_w = OxmlElement("w:tblW")
        tbl_pr.append(tbl_w)
    tbl_w.set(qn("w:w"), str(total))
    tbl_w.set(qn("w:type"), "dxa")
    tbl_ind = tbl_pr.find(qn("w:tblInd"))
    if tbl_ind is None:
        tbl_ind = OxmlElement("w:tblInd")
        tbl_pr.append(tbl_ind)
    tbl_ind.set(qn("w:w"), str(indent))
    tbl_ind.set(qn("w:type"), "dxa")
    grid = table._tbl.tblGrid
    for child in list(grid):
        grid.remove(child)
    for width in widths_dxa:
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(width))
        grid.append(col)
    for row in table.rows:
        for idx, cell in enumerate(row.cells):
            width = widths_dxa[idx]
            tc_pr = cell._tc.get_or_add_tcPr()
            tc_w = tc_pr.find(qn("w:tcW"))
            if tc_w is None:
                tc_w = OxmlElement("w:tcW")
                tc_pr.append(tc_w)
            tc_w.set(qn("w:w"), str(width))
            tc_w.set(qn("w:type"), "dxa")
            set_cell_margins(cell)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def set_run_font(run, name="Calibri", size=None, color=None, bold=None, italic=None):
    run.font.name = name
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.rFonts
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    rfonts.set(qn("w:ascii"), name)
    rfonts.set(qn("w:hAnsi"), name)
    if size is not None:
        run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = RGBColor.from_string(color)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


def style_paragraph(p, before=0, after=6, line=1.25, keep=False):
    fmt = p.paragraph_format
    fmt.space_before = Pt(before)
    fmt.space_after = Pt(after)
    fmt.line_spacing = line
    fmt.keep_together = keep


def add_numbering(doc, kind="bullet"):
    numbering = doc.part.numbering_part.element
    ids = [int(x.get(qn("w:abstractNumId"))) for x in numbering.findall(qn("w:abstractNum"))]
    abstract_id = max(ids, default=-1) + 1
    num_ids = [int(x.get(qn("w:numId"))) for x in numbering.findall(qn("w:num"))]
    num_id = max(num_ids, default=0) + 1
    abstract = OxmlElement("w:abstractNum")
    abstract.set(qn("w:abstractNumId"), str(abstract_id))
    multi = OxmlElement("w:multiLevelType")
    multi.set(qn("w:val"), "singleLevel")
    abstract.append(multi)
    lvl = OxmlElement("w:lvl")
    lvl.set(qn("w:ilvl"), "0")
    start = OxmlElement("w:start")
    start.set(qn("w:val"), "1")
    lvl.append(start)
    num_fmt = OxmlElement("w:numFmt")
    num_fmt.set(qn("w:val"), "bullet" if kind == "bullet" else "decimal")
    lvl.append(num_fmt)
    lvl_text = OxmlElement("w:lvlText")
    lvl_text.set(qn("w:val"), "•" if kind == "bullet" else "%1.")
    lvl.append(lvl_text)
    jc = OxmlElement("w:lvlJc")
    jc.set(qn("w:val"), "left")
    lvl.append(jc)
    ppr = OxmlElement("w:pPr")
    tabs = OxmlElement("w:tabs")
    tab = OxmlElement("w:tab")
    tab.set(qn("w:val"), "num")
    tab.set(qn("w:pos"), "540")
    tabs.append(tab)
    ppr.append(tabs)
    ind = OxmlElement("w:ind")
    ind.set(qn("w:left"), "540")
    ind.set(qn("w:hanging"), "270")
    ppr.append(ind)
    lvl.append(ppr)
    abstract.append(lvl)
    numbering.append(abstract)
    num = OxmlElement("w:num")
    num.set(qn("w:numId"), str(num_id))
    abs_id = OxmlElement("w:abstractNumId")
    abs_id.set(qn("w:val"), str(abstract_id))
    num.append(abs_id)
    numbering.append(num)
    return num_id


def apply_num(p, num_id):
    ppr = p._p.get_or_add_pPr()
    num_pr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), "0")
    num = OxmlElement("w:numId")
    num.set(qn("w:val"), str(num_id))
    num_pr.append(ilvl)
    num_pr.append(num)
    ppr.append(num_pr)


def add_bullet(doc, text, bullet_id, level=0):
    p = doc.add_paragraph(style="Normal")
    apply_num(p, bullet_id)
    p.paragraph_format.left_indent = Inches(0.375)
    p.paragraph_format.first_line_indent = Inches(-0.188)
    style_paragraph(p, after=4, line=1.25)
    p.add_run(text)
    return p


def add_label_paragraph(doc, label, text, label_color=INK, after=4):
    p = doc.add_paragraph(style="Normal")
    style_paragraph(p, after=after, line=1.25, keep=True)
    r = p.add_run(label + " ")
    set_run_font(r, color=label_color, bold=True)
    p.add_run(text)
    return p


def add_evidence_line(doc, keys):
    p = doc.add_paragraph(style="Evidence")
    style_paragraph(p, after=8, line=1.15, keep=True)
    r = p.add_run("Key literature: ")
    set_run_font(r, size=9.5, color=MUTED, bold=True)
    r = p.add_run(keys)
    set_run_font(r, size=9.5, color=MUTED)
    return p


def configure_styles(doc):
    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor.from_string(BLACK)
    normal._element.rPr.rFonts.set(qn("w:ascii"), "Calibri")
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Calibri")
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.25
    for name, size, color, before, after in [
        ("Heading 1", 16, BLUE, 18, 10),
        ("Heading 2", 13, BLUE, 14, 7),
        ("Heading 3", 12, DARK_BLUE, 10, 5),
    ]:
        s = styles[name]
        s.font.name = "Calibri"
        s.font.size = Pt(size)
        s.font.bold = True
        s.font.color.rgb = RGBColor.from_string(color)
        s._element.rPr.rFonts.set(qn("w:ascii"), "Calibri")
        s._element.rPr.rFonts.set(qn("w:hAnsi"), "Calibri")
        s.paragraph_format.space_before = Pt(before)
        s.paragraph_format.space_after = Pt(after)
        s.paragraph_format.line_spacing = 1.0
        s.paragraph_format.keep_with_next = True
    if "Evidence" not in [s.name for s in styles]:
        s = styles.add_style("Evidence", 1)
        s.base_style = normal
    evidence = styles["Evidence"]
    evidence.font.name = "Calibri"
    evidence.font.size = Pt(9.5)
    evidence.font.color.rgb = RGBColor.from_string(MUTED)
    evidence.font.italic = True


def configure_section(section):
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1)
    section.right_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.header_distance = Inches(0.492)
    section.footer_distance = Inches(0.492)


def add_page_field(p):
    p.add_run("Page ")
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    p._p.append(fld)


def add_header_footer(section):
    header = section.header
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    style_paragraph(p, after=0, line=1.0)
    r = p.add_run("MAGNETIC-FIELD SENSORS REVIEW  |  EVIDENCE COMPILATION")
    set_run_font(r, size=8.5, color=MUTED, bold=True)
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    style_paragraph(p, after=0, line=1.0)
    set_run_font(p.add_run("Prepared 14 July 2026  |  "), size=8.5, color=MUTED)
    add_page_field(p)
    for run in p.runs:
        set_run_font(run, size=8.5, color=MUTED)


def add_cover(doc):
    p = doc.add_paragraph()
    style_paragraph(p, after=0)
    p.add_run("\n\n\n")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_paragraph(p, after=18)
    r = p.add_run("REVIEW-PAPER EVIDENCE COMPILATION")
    set_run_font(r, size=11, color=GOLD, bold=True)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_paragraph(p, after=10)
    r = p.add_run("Magnetic-Field Sensors")
    set_run_font(r, size=30, color=INK, bold=True)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_paragraph(p, after=6)
    r = p.add_run("Outline, literature map, and critical-point summaries")
    set_run_font(r, size=15, color=DARK_BLUE)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_paragraph(p, after=36)
    r = p.add_run("Two aligned versions: technical synthesis + plain-language importance guide")
    set_run_font(r, size=11, color=MUTED, italic=True)
    table = doc.add_table(rows=3, cols=2)
    data = [
        ("Target", "MDPI Sensors review; submission target before 30 October 2026"),
        ("Evidence base", "122 deduplicated references; 80 peer-reviewed journal articles; standards, vendor, preprint, and market sources explicitly flagged"),
        ("Recommended structure", "Sensor-family backbone with full energy, transportation, industrial, and biomedical application sections"),
    ]
    for i, (label, value) in enumerate(data):
        table.cell(i, 0).text = label
        table.cell(i, 1).text = value
        set_cell_shading(table.cell(i, 0), LIGHT_BLUE)
        for run in table.cell(i, 0).paragraphs[0].runs:
            set_run_font(run, color=INK, bold=True)
    set_table_geometry(table, [1800, 7560])
    p = doc.add_paragraph()
    style_paragraph(p, before=28, after=0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Prepared from the processed outputs in this project folder")
    set_run_font(r, size=9.5, color=MUTED)
    doc.add_page_break()


def add_callout(doc, label, text, fill=CALLOUT):
    table = doc.add_table(rows=1, cols=1)
    set_table_geometry(table, [9360])
    set_cell_shading(table.cell(0, 0), fill)
    p = table.cell(0, 0).paragraphs[0]
    style_paragraph(p, after=0, line=1.2)
    r = p.add_run(label + " ")
    set_run_font(r, color=INK, bold=True)
    p.add_run(text)
    return table


def add_reader_guide(doc, bullet_id):
    doc.add_heading("How to use this compilation", level=1)
    add_callout(doc, "Recommended paper architecture.", "Use Outline A as the backbone and expand the application tail using Outline B. Retain Outline C's capability map and Outline D's risk register as signature artifacts.")
    doc.add_heading("What the two versions contain", level=2)
    add_bullet(doc, "Version 1 is a technical evidence synthesis. Each critical point states the supported claim, its role in the paper, and the key citation keys.", bullet_id)
    add_bullet(doc, "Version 2 follows the same paper structure in plain language and explicitly states why each point matters.", bullet_id)
    add_bullet(doc, "Appendix A lists all 122 registered sources, grouped by the paper section where they are used. Source status remains visible.", bullet_id)
    add_bullet(doc, "Appendix B records the evidence gaps and drafting priorities so uncertain values are not silently upgraded.", bullet_id)
    doc.add_heading("Evidence rules carried forward", level=2)
    add_bullet(doc, "Use citation keys during drafting; convert to numbered MDPI citations at manuscript assembly.", bullet_id)
    add_bullet(doc, "Keep vendor specifications tagged as vendor evidence and market figures attributed as estimates.", bullet_id)
    add_bullet(doc, "Treat TRL ratings, risk judgments, and future-readiness claims as author assessments.", bullet_id)
    add_bullet(doc, "Do not fill unreported performance cells from memory; verify them from full text or leave them explicitly unreported.", bullet_id)
    doc.add_heading("Candidate outline families", level=2)
    table = doc.add_table(rows=1, cols=3)
    hdr = table.rows[0]
    for i, text in enumerate(("Outline", "Organizing logic", "Best use / tradeoff")):
        hdr.cells[i].text = text
        set_cell_shading(hdr.cells[i], BLUE)
        for run in hdr.cells[i].paragraphs[0].runs:
            set_run_font(run, size=9.5, color=WHITE, bold=True)
    set_repeat_header(hdr)
    for name, logic, use in OUTLINE_OPTIONS:
        cells = table.add_row().cells
        for cell, value in zip(cells, (name, logic, use)):
            cell.text = value
            for p in cell.paragraphs:
                style_paragraph(p, after=0, line=1.1)
                for run in p.runs:
                    set_run_font(run, size=9.2)
    set_table_geometry(table, [1900, 3400, 4060])
    doc.add_heading("Recommended outline in full", level=2)
    for heading, items in RECOMMENDED_OUTLINE:
        doc.add_heading(heading, level=3)
        for item in items:
            add_bullet(doc, item, bullet_id)


def add_version(doc, title, subtitle, items, plain=False):
    doc.add_page_break()
    p = doc.add_paragraph()
    style_paragraph(p, after=6)
    r = p.add_run(title)
    set_run_font(r, size=22, color=INK, bold=True)
    p = doc.add_paragraph()
    style_paragraph(p, after=14)
    r = p.add_run(subtitle)
    set_run_font(r, size=11.5, color=MUTED, italic=True)
    current = None
    for section, topic, summary, importance, refs in items:
        if section != current:
            doc.add_heading(section, level=1)
            current = section
        doc.add_heading(topic, level=2)
        if plain:
            add_label_paragraph(doc, "In plain language:", summary)
            add_label_paragraph(doc, "Why it matters:", importance, label_color=GOLD)
        else:
            add_label_paragraph(doc, "Evidence synthesis:", summary)
            add_label_paragraph(doc, "Critical significance:", importance, label_color=GOLD)
        add_evidence_line(doc, refs)


def add_gaps(doc):
    doc.add_page_break()
    doc.add_heading("Appendix B. Evidence gaps and drafting priorities", level=1)
    add_callout(doc, "Main reading.", "The taxonomy's principles and applications are substantially covered. The systematic weakness is verification of quantitative performance cells and the future/standards treatment of minor families.", LIGHT_BLUE)
    table = doc.add_table(rows=1, cols=3)
    for i, text in enumerate(("Topic", "Status", "Action before drafting exact claims")):
        table.rows[0].cells[i].text = text
        set_cell_shading(table.rows[0].cells[i], BLUE)
        for run in table.rows[0].cells[i].paragraphs[0].runs:
            set_run_font(run, size=9.2, color=WHITE, bold=True)
    set_repeat_header(table.rows[0])
    for topic, status, action in GAPS:
        cells = table.add_row().cells
        for cell, value in zip(cells, (topic, status, action)):
            cell.text = value
            for p in cell.paragraphs:
                style_paragraph(p, after=0, line=1.08)
                for run in p.runs:
                    set_run_font(run, size=8.8)
        if status == "Strong":
            set_cell_shading(cells[1], "E7F2EA")
        else:
            set_cell_shading(cells[1], "FFF4D6")
    set_table_geometry(table, [1900, 900, 6560])
    doc.add_heading("Highest-value next actions", level=2)
    actions = [
        "Perform one full-text extraction pass for Hall, AMR/GMR, fluxgate, OPM/SERF, magnetoelectric, MEMS, and fiber-optic performance values already anchored in the registry.",
        "Search for versions of record for NV current sensing and GaN spinning-current work; otherwise keep them explicitly preprint-stage.",
        "Add the author's verified 2023 IEEE Sensors Letters citation manually; do not reconstruct it from memory.",
        "Find peer-reviewed anchors for learned aging compensation, a magnetic-sensor digital twin, MagNav accuracy, and ML assurance under ISO 26262—or present the absence as a research gap.",
        "Complete bibliography hygiene: missing author fields, missing standards URLs, and an IEC 61850-9-2 registry entry.",
        "Before October 2026 submission, refresh MDPI APC/policy information, AI-authorship disclosure guidance, market estimates, and the status of 2024 AI-safety documents.",
    ]
    for a in actions:
        add_bullet(doc, a, BULLET_ID)


def status_label(row):
    status = row["status"]
    if status == "peer-reviewed journal":
        return "Journal"
    if status == "standard":
        return "Standard"
    if status == "preprint":
        return "Preprint"
    if status == "vendor-grey":
        return "Vendor"
    if status == "market-report-grey":
        return "Market"
    if "conference" in status:
        return "Conference"
    if "book" in status:
        return "Book"
    return status


def add_registry(doc):
    doc.add_page_break()
    doc.add_heading("Appendix A. Complete literature inventory", level=1)
    p = doc.add_paragraph()
    style_paragraph(p, after=10)
    p.add_run("All 122 entries in ")
    r = p.add_run("reference_registry.csv")
    r.italic = True
    p.add_run(" are included below. DOI and source-status information is preserved so each version of the summary can be traced to the same evidence base.")
    with REGISTRY.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    groups = defaultdict(list)
    for row in rows:
        groups[row["sections_used"] or "unassigned"].append(row)
    order = ["intro", "sensors", "applications", "applications; standards/business", "future", "standards", "unassigned"]
    names = {
        "intro": "Introduction and cross-family framing",
        "sensors": "Sensor families and operating principles",
        "applications": "Current application domains",
        "applications; standards/business": "Applications plus business/standards",
        "future": "Future methods, fusion, and digital twins",
        "standards": "Standards, metrology, markets, and business",
        "unassigned": "Unassigned",
    }
    for group in order:
        if not groups.get(group):
            continue
        doc.add_heading(names[group], level=2)
        table = doc.add_table(rows=1, cols=5)
        headers = ("Key", "Year", "Type", "Title / venue", "DOI or evidence note")
        for i, text in enumerate(headers):
            table.rows[0].cells[i].text = text
            set_cell_shading(table.rows[0].cells[i], BLUE)
            for run in table.rows[0].cells[i].paragraphs[0].runs:
                set_run_font(run, size=8.2, color=WHITE, bold=True)
        set_repeat_header(table.rows[0])
        for row in sorted(groups[group], key=lambda x: (x["year"], x["key"])):
            typ = status_label(row)
            title_venue = row["title"] + (f" — {row['venue']}" if row["venue"] else "")
            note = row["doi"] or ("No DOI; " + typ.lower())
            cells = table.add_row().cells
            for cell, value in zip(cells, (row["key"], row["year"], typ, title_venue, note)):
                cell.text = value
                for p in cell.paragraphs:
                    style_paragraph(p, after=0, line=1.02)
                    for run in p.runs:
                        set_run_font(run, size=7.8)
            if typ in ("Preprint", "Vendor", "Market"):
                set_cell_shading(cells[2], "FFF4D6")
            elif typ == "Standard":
                set_cell_shading(cells[2], LIGHT_BLUE)
        set_table_geometry(table, [1600, 600, 1100, 4060, 2000])
        p = doc.add_paragraph()
        style_paragraph(p, after=4)


def add_source_note(doc):
    doc.add_heading("Source files consolidated", level=2)
    files = [
        "PROJECT_BRIEF.md and 00_target_journal_brief.md",
        "10_titles.md and 20_outlines.md",
        "30_litreview_sensor_types.md",
        "40_litreview_applications.md",
        "50_litreview_future_methods.md",
        "60_standards_and_business.md",
        "70_bibliography_report.md, reference_registry.csv, and references.bib",
        "00_DELIVERABLE_paper_plan.md and PATCH_NOTES.md",
    ]
    for f in files:
        add_bullet(doc, f, BULLET_ID)


def build():
    global BULLET_ID
    doc = Document()
    configure_styles(doc)
    for section in doc.sections:
        configure_section(section)
        add_header_footer(section)
    BULLET_ID = add_numbering(doc, "bullet")
    add_cover(doc)
    add_reader_guide(doc, BULLET_ID)
    add_version(doc, "Version 1 — Technical evidence synthesis", "A concise, citation-keyed writing scaffold for the manuscript.", TECHNICAL, plain=False)
    add_version(doc, "Version 2 — Plain-language importance guide", "The same paper logic explained for non-specialist, business, and investor readers.", PLAIN, plain=True)
    add_registry(doc)
    add_gaps(doc)
    add_source_note(doc)
    props = doc.core_properties
    props.title = "Magnetic-Field Sensors Review: Two-Version Evidence Compilation"
    props.subject = "Technical and plain-language summaries with complete literature inventory"
    props.author = "Research compilation"
    props.keywords = "magnetic sensors; Hall effect; magnetoresistance; OPM; standards; literature review"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
