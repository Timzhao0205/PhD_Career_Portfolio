# D08 — Instrumentation & Sensing Products (Standalone)

## Landscape

Precision magnetic/current sensing and general-purpose electrical instrumentation splits into
several distinct product families: (1) source-measure units (SMUs) — Keithley/Tektronix and
Keysight dominate, prices from ~$7,900 (Keithley 2450) to ~$22,900 (Keysight B2902B 2-ch)
[D08-15 pricing context via market search, verified via vendor listings]; (2) precision current
sensors/transducers — Hall, TMR, fluxgate, Rogowski, and zero-flux designs from LEM (1-3 ppm
accuracy, few-ppm/K drift) [D08-15] and Danisense (linearity to 1 ppm, 50 A-11 kA) [D08-17], plus
IC-level sensors from Allegro (its ACS37017, released Feb 2026, claims 0.55% sensitivity error
over life/temperature for AI-datacenter and xEV power loops) [D08-14]; (3) quantum-adjacent
magnetometers with classical readout — optically pumped magnetometers (OPMs) from QuSpin
(7-15 fT/√Hz sensitivity, $7,700-$10,000/sensor depending on volume) [D08-16] serving MEG/fMCG
research, and NV-diamond and Rydberg-atom RF sensors moving out of national labs toward
navigation and EW products [D08-02][D08-03]; (4) EMC/EMI test gear — a $4.9B (2026) to $7.1B
(2031, 7.7% CAGR) market dominated by spectrum analyzers and EMI receivers, Asia-Pacific already
40% of revenue and growing fastest [D08-19]. The common thread: buyers pay a large premium for
instruments that get to a hard physical limit (noise floor, bandwidth, drift, SI-traceability)
that off-the-shelf parts cannot reach, and they buy them as capital equipment, not services.

## Pain points & buyers

Power electronics and EV/AI-datacenter engineers need current sensors that are simultaneously
fast (>10 MHz, for GaN/SiC switching edges) and accurate (sub-1% over life and temperature);
today's parts trade one for the other — Allegro's own three-way split into speed (ACS37100,
10 MHz), power density (ACS37200), and accuracy (ACS37017) product lines is a direct admission of
this gap [D08-14]. Neuroscience/psychiatry researchers and hospitals want whole-head OPM-MEG
arrays but a 50+ sensor array still costs "in the range of a SQUID-MEG" system despite
room-temperature operation, and per-sensor movement artifacts remain unsolved [D08-13]. EMC labs
and power-electronics EMI debuggers need field probes that are SI-traceable without a NIST trip;
Rydberg-atom E-field probes promise self-calibration to <1% uncertainty versus antenna standards
but are still lab-grade and expensive [NIST program, D08-03][D08-22]. Battery and grid-storage
manufacturers need SMU-class sourcing/measurement that is cheaper per channel and more precise
than Keithley/Chroma/Arbin gear as formation-test throughput scales with gigafactory buildout
[market search]. HTS/superconducting magnet builders (fusion, MRI/NMR, no-insulation coil makers)
need production-line current and quench-onset instrumentation compatible with cryogenic
environments and non-invasive coupling — a niche the founder's own laser-aligned HTS winding-
machine work touches directly [prior education context, not a citable claim].

## Incumbents & gaps

SMUs: Keithley/Tektronix and Keysight own the general-purpose market; gaps are in ultra-low-noise,
high-channel-count formation testing for next-gen (solid-state, sodium-ion) cells, where Chroma
ATE and Arbin lead but accuracy/noise headroom is being pushed by new chemistries [battery
formation market search]. Current sensors: LEM and Danisense own ppm-accuracy at moderate
bandwidth; Allegro/Infineon own high-volume IC-level Hall/TMR sensing; nobody yet ships a single
product combining >10 MHz bandwidth with <0.1% accuracy at moderate cost — this is a real
whitespace for a 2-5 person team building a TMR- or fluxgate-hybrid module, and recent open
literature shows TMR designs reaching 0.045% accuracy and 10.5 kHz bandwidth in lab prototypes,
i.e., the physics is proven but not yet packaged as a fast+accurate product [D08-23]. OPM
magnetometers: QuSpin is the commercially mature leader with a narrow SKU set (QZFM/QTFM); gaps
exist in triaxial arrays, wearable form factors, and defense/navigation-grade ruggedization — NIST
explicitly flags unresolved diamond-material standardization for the competing NV-center approach
[D08-02]. Rydberg RF probes: Rydberg Technologies is first to a commercial product (RFP
1100/RFMS 1800) but the field is one company deep, DARPA is actively de-risking ruggedization
through the new RoQS program (Phase 1 launched 2025) [D08-05][D08-06], and downstream EMC/defense
buyers have no second source. HTS/cryogenic current sensing: cryogenic current comparators exist
as lab instruments (IEEE literature back to the early 2000s) [D08-11] but no vendor sells a
turnkey, non-invasive quench/current instrument aimed at HTS coil manufacturers as opposed to
national-lab beamlines.

## 2029 inflections

DARPA's RoQS program (Phase 1, 2025-2026) is explicitly funding ruggedization of quantum
magnetometers and RF sensors for fielded platforms, meaning DoD-validated, vibration-tolerant
designs should be reaching TRL 6-7 by 2028-2029 — the window in which non-defense spinouts
(navigation, EMC, medical) typically appear [D08-05][D08-06]. China's 十五五 (15th Five-Year Plan,
2026-2030) names 高端仪器 (high-end instruments) as one of a short list of "must-win" supply-chain
technologies alongside integrated circuits and 工业母机, with the Ministry of Science and
Technology and NSFC both funding quantum precision measurement (NSFC's dedicated program funds
"cultivating" projects at ~$600K/3 yr and "key support" projects at ~$2.8M/4 yr through at least
2026) [D08-04][D08-08]. Beijing's municipal 高端科学仪器创新发展行动计划 (2025-2027) targets 50+
complete instruments and 30+ key components developed locally by 2027 [D08-07] — a direct signal
that China-side instrument buyers (universities, CAS institutes, state labs) will have fresh
procurement budgets and explicit non-Western-sourcing pressure through 2029-2030. On the
current-sensor side, GaN/SiC adoption in EV traction inverters and AI-datacenter power delivery
is the volume driver pulling sensor bandwidth requirements past 10 MHz industry-wide by 2028-2029
[D08-14][D08-19].

## China notes

Chinese magnetic-sensor makers (多维科技/MultiDimension, 美新/MEMSensing, 纳芯微/Novosense,
希磁科技/Sicel, BYD Semiconductor, and others) hold roughly 5-10% of the global magnetic-sensor
chip market despite two decades of MEMS/TMR development, leaving Western/Japanese suppliers
dominant in China's own automotive and grid supply chains [D08-18]. On the quantum-sensing
frontier, a Chinese Academy of Engineering strategy paper is explicit that Western nations
restrict export to China of optically pumped magnetometers above 20 pT sensitivity (versus the US
Geometrics G-824A's 0.3 pT/√Hz benchmark), and that China's own airborne superconducting/quantum
magnetic systems (Jilin University, Shanghai Institute of Microsystem) remain largely lab
prototypes, not fielded, fabricable-at-scale products — a direct, citable domestic-sensor supply
gap [D08-12]. This combination (explicit export restriction + explicit five-year-plan funding +
immature domestic supply) is the strongest China-specific opening in this domain for a
US/China-fluent founder able to legally sell non-restricted-spec instruments into Chinese research
and industrial buyers.

## Opportunity seeds

**1. Fast + accurate isolated current-sensor module for GaN/SiC power test and production.**
Power-electronics and EV/AI-datacenter engineers currently must choose between Allegro's
speed-optimized, power-density-optimized, or accuracy-optimized current-sensor lines because no
single IC-class product hits >10 MHz bandwidth and <0.1% lifetime accuracy together [D08-14].
Buyers are WBG power-module makers, inverter OEMs, and double-pulse-tester integrators who will
pay a premium per channel for a drop-in replacement. A 2-5 person team with GaN/SiC device and
precision-analog expertise can combine a TMR or fluxgate front end with a custom compensation ASIC
faster than large IDMs can re-architect existing product families. China's EV/inverter volume and
the domestic magnetic-sensor gap (5-10% share) make this dual-market from day one [D08-18].

**2. Compact triaxial OPM sensor line for MEG/fMCG and defense-adjacent navigation.**
Neuroscience labs and hospitals want whole-head OPM arrays, but QuSpin is effectively the sole
mature commercial vendor and per-sensor triaxial pricing still adds ~$1,250 to a $7,700-$10,000
base [D08-16], while DARPA is simultaneously funding ruggedized quantum-magnetometer navigation
payloads through RoQS [D08-05]. A small team building a laser/vapor-cell sensor module (directly
leveraging laser-alignment and precision-winding fabrication skill) could target the
underserved triaxial/wearable niche for research buyers first, then migrate the same sensor core
toward GPS-denied navigation as RoQS-funded ruggedization matures by 2028-2029. Second-sourcing a
single-vendor market is a classic small-team wedge; China's own quantum-magnetometer prototypes
remain lab-only, giving a US-fabricated, export-compliant product a path into Chinese university
and industrial buyers [D08-12].

**3. Rugged, self-calibrating Rydberg-atom RF field probe for EMC pre-compliance labs.**
EMC test houses and power-electronics EMI debug teams need SI-traceable field probes without
routine NIST recalibration trips, and Rydberg-atom sensing promises <1% self-calibrated
uncertainty versus conventional antenna standards [D08-03][D08-22], but Rydberg Technologies is
currently the only commercial vendor. A 2-5 person team can target a narrower, cheaper
bench-top probe for the fast-growing Asia-Pacific EMC test-equipment market (40% of a $4.9B 2026
market, 11%+ regional CAGR, driven partly by China's GB/T 18655 vehicle EMC standard) [D08-19]
rather than chasing Rydberg Technologies' broad defense roadmap, entering as ruggedization
research funded by DARPA's RoQS program de-risks the core physics package by 2028-2029 [D08-05].

**4. Non-invasive cryogenic current & quench-onset instrument for HTS coil manufacturers.**
Fusion-magnet, MRI/NMR-magnet, and no-insulation HTS coil makers need production-line
instrumentation to verify current distribution and catch quench onset during winding and
commissioning, but published cryogenic current comparator work is lab/beamline-grade, not a
packaged commercial test instrument for coil manufacturing lines [D08-11]. The buyer is the
magnet/coil manufacturer's test-and-QA function, paying capital-equipment prices per unit, not a
monitoring subscription — keeping this outside diagnostic-service territory. This is the founder's
most direct skill match (laser-aligned HTS winding-machine design experience) and a market too
small and too specialized for incumbent SMU/current-sensor vendors to prioritize, making it
winnable by a tiny, technically deep team; both US fusion/MRI-magnet makers and China's growing
HTS coil industry are addressable customers.

**5. Ultra-low-noise SMU/source-measure instrument line for next-gen battery-cell R&D.**
Battery R&D labs and gigafactories doing formation and characterization testing on solid-state
and sodium-ion chemistries are pushing existing Keithley/Chroma/Arbin SMU-class gear toward its
noise and channel-density limits as the EV battery formation/testing market grows from ~$1.7B
(2024) at ~17%/yr [market search]. A small team building a purpose-built, high-channel-count,
sub-ppm-noise SMU for R&D (not full production-line formation, avoiding head-on collision with
Chroma/Arbin's manufacturing-scale business) can sell direct to battery-chemistry labs at a
premium; China's CATL/BYD-scale battery R&D ecosystem and simultaneous instrument-export
sensitivities make a China-fluent founder unusually well positioned to serve both US and Chinese
battery-lab buyers with a compliant, domestically-buildable instrument.
