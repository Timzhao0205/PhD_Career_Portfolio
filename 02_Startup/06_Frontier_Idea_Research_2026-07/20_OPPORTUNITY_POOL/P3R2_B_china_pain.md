# P3R2 Batch B — China-pain seeds (round 2, authoritative)

Generated 2026-07-13 by idea-architect (Fable 5 / xhigh) from the repaired atlas only. 22 seeds,
15 distinct primary lanes. Every cited ID was checked against the canonical ledger
(`90_BIBLIOGRAPHY/sources.json`): accepted=true and origin-eligible (post-P2A all accepted records
are `verified_non_india_origin`; none of the 42 excluded IDs are cited). Candidate IDs found
rejected during this batch's eligibility check and therefore NOT cited anywhere: L01-013, L03-053,
L05-038, L06-040, L07-007, L08-016, L11-055, L13-043, L14-041, L14-042, L15-044.
Atlas negative findings respected: no electrolyzer-stack play (L11 overcapacity), no two-phase
play without a PFAS-free fluid plan, no reliance on the unverified "100% liquid-cooling mandate"
(L14-036 primary text) or the unverified L13 "100% localization" claim, no commoditized
high-power fiber-laser play (L12-037 price war). Foreign-founder China-access risk is flagged per
seed. Prior SEEDS_A–D were not read or reused.


> **Adjudication applied 2026-07-13:** the independent elegance/novelty verdicts (`P3R2_ELEGANCE_ADJUDICATION.md`) have been applied to every seed below - PROMOTE/FIX_APPLIED/MERGED/REJECT annotations appear at the end of each seed section and in the batch JSON (`elegance_verdict` fields). See `P3R2_FIX_APPLICATION_LOG.md`.

---

## P3R2-B-01 — Negative-pressure two-phase cold-plate loop (PFAS-free) for >2 kW/chip Chinese AI racks

- **Product:** Rack-level subatmospheric water/low-GWP two-phase loop: microchannel evaporator plates + vacuum-condenser CDU; saturation temperature set by vacuum setpoint; seal failures leak air IN (vacuum-decay detected), never coolant onto boards. T/CIEP 0263-2025-compatible interfaces.
- **Buyer + pain evidence:** Envicool-class CDU vendors (L14-043), Alibaba-class HVDC operators (L02-048/049), operators under GB 40879 PUE caps (L14-035) and the 2026 AI-energy action plan's high-efficiency-cooling line (L14-036 — primary text contains no 100% mandate); chip heat flux to 800–1,000 W/cm2 (L14-010, L14-044).
- **Technical mechanism:** Latent-heat extraction at negative gauge pressure; two-phase superiority literature L14-001/002/003/029; microchannel design base L14-006/009; ITRI low-pressure 2.4 kW/chip proof-of-physics (L14-053).
- **Why incumbents miss it:** Chinese incumbents are optimizing single-phase cold plates to hyperscaler specs (L14-043); two-phase architectures are documented as non-converged, and the PFAS fluid path most vendors assumed is dead — water-based negative pressure sidesteps both.
- **Decisive experiment + budget:** 2027-Q2, $250k: 1–2 kW test-die comparison vs best single-phase plate; win = ≥30% lower thermal resistance at equal pump power + demonstrated inward-leak fail-safe.
- **TRL:** 4.
- **2026–2029 plan:** Lab loop testbed and ITRI-class replication; 2–3 core patents; joint evaluations with one CN thermal vendor + one TW/JP ODM lab; 20–50 kW rack demonstrator (HK/Shenzhen partner lab); GB 40879 compliance-economics discovery with 10+ operators. No operating company assumed.
- **2030–2034 trigger (named):** GB 40879 revised PUE ≤1.25/≤1.2 enforcement (L14-035) across the East-Data-West-Computing (东数西算) hub-node buildout (L02-049) in the 15th FYP.
- **2030 competition:** Envicool + 7-vendor Deschutes cohort (L14-043), ITRI-fed Taiwan ODM lines (L14-053), at least one Chinese two-phase startup.
- **Window/timing risk:** Chinese incumbents may productize two-phase in-house pre-2030; access only via licensing/JV or ODM design-in (HK entity).
- **Kill date:** 2034-06-30 absent a ≥100 kW paid pilot.
- **Big vision:** Default leak-safe two-phase architecture for Asian AI infrastructure; extension to WBG power modules, EV fast-charge cabinets, aerospace converters.
- **Nearest substitutes:** Optimized single-phase cold plates; immersion tanks (fluid-supply-constrained).
- **Key uncertainty:** Whether operators price leak-safety highly enough to accept vacuum-system complexity.
- **[Adjudication 2026-07-13 - PROMOTE]:** Best China-primary seed and only mechanism-level original in thermal family (negative-pressure leak-safe two-phase, PFAS-free by design); correctly rejects the debunked 100%-liquid-mandate claim; access via licensing/ODM honestly planned. 2026-07-13: no content imported. C-04 (FIX) adopts B-01's negative-pressure architecture as its primary variant for the US+CN dual play; B-01 remains the CN-primary canonical with the licensing/ODM access route. Cluster duplicate C-04 is retained as a separate FIX seed per adjudication.

## P3R2-B-02 — Liquid-cooling qualification and reliability test platform (T/CIEP 0263-2025-aligned)

- **Product:** 50–250 kW CDU thermohydraulic test carts with transient GPU-load emulation, cold-plate metrology cells, coolant corrosion/clog rigs, automated reporting against T/CIEP 0263-2025 clauses.
- **Buyer + pain evidence:** Chinese CDU/cold-plate vendors and operators doing acceptance tests; documented spec chaos (GB200 TDP/flow contradictions, L14-044), Deschutes 3°C-approach/80 PSI spec (L14-043), new Chinese liquid-cooling specification T/CIEP 0263-2025 (L14-039), GB 40879 caps (L14-035).
- **Technical mechanism:** Traceable calorimetry + scripted transient load profiles; corrosion/biofouling accelerated protocols (technical base L14-006/009/010/028/029).
- **Why incumbents miss it:** Test-equipment majors chase battery/semi test; thermal vendors self-certify (conflict of interest); the standard is 2025-vintage so no bench ecosystem exists yet.
- **Decisive experiment + budget:** 2027-Q1, $400k: published instrumented round-robin of three commercial cold plates vs datasheets; win = findings cited/adopted by ≥1 Chinese vendor or lab.
- **TRL:** 6.
- **2026–2029 plan:** Reference bench in a university/third-party lab; round-robin publication; test-method proposals into the CIEP ecosystem; paid pilot testing-as-research for 2–3 vendors; productized cart design.
- **2030–2034 trigger (named):** T/CIEP 0263-2025 + GB 40879 written into hub-node procurement acceptance terms during the 15th-FYP datacenter buildout (L14-039, L14-035, L02-049).
- **2030 competition:** Chroma ATE-class extension (L11-043), ITRI (L14-053), vendor in-house labs.
- **Window/timing risk:** Certification politics favor domestic labs — sell benches to those labs; moderate access risk.
- **Kill date:** 2034-12-31 absent a bench sale + standards citation.
- **Big vision:** The JEDEC-bench of liquid-cooled computing in Asia; expand to two-phase, immersion, vehicle and power-module cooling qualification.
- **Nearest substitutes:** In-house vendor labs; one-off university test contracts.
- **Key uncertainty:** Whether acceptance testing consolidates into state-affiliated cert labs that build their own benches.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-C-05]:** Import T/CIEP clause-scripted reporting and sell-to-domestic-certification-labs channel into C-05. Record retained as audit trail; not independently promotable.

## P3R2-B-03 — 800 VDC rack-inlet protection/hot-swap module for Chinese HVDC datacenters

- **Product:** 30–100 kW inlet brick: solid-state pre-charge/inrush limiting, active bus-oscillation damping (synthesized virtual impedance), hot-swap sequencing, insulation/ground-fault monitoring, capacitor-health telemetry.
- **Buyer + pain evidence:** Delta China/Zhongheng lineage (L02-048), Autrans (Alibaba + 东数西算 parks, L02-049), Innoscience-ecosystem integrators (L02-050); unresolved 800V grounding/hot-plug/oscillation pain documented in Chinese engineering coverage (L02-054); DC-link capacitor failure physics (L02-010).
- **Technical mechanism:** GaN/SiC series stage emulating programmable damping impedance + sequenced pre-charge; device ecosystem L02-046/051; architecture L02-043/044.
- **Why incumbents miss it:** Huawei/Delta solve it internally for their own racks; chip vendors sell devices, not integration bricks; second-tier integrators and colos have no qualified merchant module.
- **Decisive experiment + budget:** 2027-Q3, $300k: arc-free hot-swap + oscillation suppression at 800 V/10 kW, <5% overshoot under full load.
- **TRL:** 3.
- **2026–2029 plan:** Stability models + 10 kW lab prototype; patents; OCP-profile interop testing; joint test reports with two Chinese PSU vendors; 50 kW pilot brick with a Shenzhen/HK integrator lab.
- **2030–2034 trigger (named):** Alibaba-class HVDC extension across 东数西算 hub parks in the 15th FYP (L02-048/049) + 800V refresh tracking NVIDIA/OCP-spec localization (L02-043/044/050).
- **2030 competition:** Huawei/Delta in-house, Autrans feature creep, Innoscience-partner reference designs.
- **Window/timing risk:** Fast domestic substitution; possible Chinese fork of the 800V spec under GPU export controls; ODM design-in via HK entity mandatory.
- **Kill date:** 2033-12-31 absent an integrator design-win.
- **Big vision:** The "DC utility interface" brick for every 800–1500 VDC rack and MW charging inlet worldwide.
- **Nearest substitutes:** Discrete pre-charge circuits + separate IMD devices engineered ad hoc per project.
- **Key uncertainty:** Whether the module niche stays merchant or gets absorbed into PSU shelves.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-01]:** Standalone CN-first dominated by Huawei/Delta in-house. Import virtual-impedance damping + capacitor telemetry into C-01. Record retained as audit trail.

## P3R2-B-04 — Modular solid-state DC protection stack (SSCB + arc-fault) for Chinese DC parks and industrial DC

- **Product:** 800–1500 V / 100 A–2 kA SiC SSCB modules (microsecond interruption, energy-absorbing branch), multi-physics DC arc-fault units (HF signature + traveling wave), park-level selectivity controller. Sold as bricks to integrators.
- **Buyer + pain evidence:** Datacenter power integrators (L02-048/049) with documented DC protection pain (L02-054); industrial DC yards in the electrolyzer tender ecosystem (L11-051); Chinese DC-protection procurement scale evidenced by State Grid tenders (XJ Electric RMB1.275bn round, L08-034); breaker non-convergence 2023–2025 (L08-001/003/004/017); arc-fault still open research (L08-019/020/021).
- **Technical mechanism:** SiC static switch + varistor/absorber branch; detection fusing HF arc signatures with traveling-wave discrimination for selectivity without zero-crossings.
- **Why incumbents miss it:** Grid giants build project-engineered HVDC valves, not merchant LV/MV bricks; rack vendors stop at the shelf; the mid-layer (park/industrial DC) is orphaned.
- **Decisive experiment + budget:** 2027-Q4, $450k: 800 V/500 A interruption <100 µs with adjacent-branch ride-through; 1,000-cycle zero-nuisance-trip demonstration.
- **TRL:** 4.
- **2026–2029 plan:** Topology study + 500 A prototype; DC fault-injection testbed; joint fault-signature data collection with Chinese integrator labs; witnessed short-circuit tests; discovery with 10+ integrators/EPCs.
- **2030–2034 trigger (named):** 800VDC hub-park rollouts (L02-049/054) + State Grid's recurring UHV/DC control-and-protection tender cadence into the 15th FYP (L08-034); global datacenter-electrification macro (L08-033).
- **2030 competition:** XJ Electric-class grid protection houses (L08-034), Huawei/Delta rack-side, CAS-spinoff SSCB startups.
- **Window/timing risk:** CCC/GB certification needs a local partner; grid layer inaccessible until 2032+; foreign founder sells modules via integrators/HK.
- **Kill date:** 2034-06-30 absent certification unit + integrator PO.
- **Big vision:** The protection-component layer of the DC-electrified industrial world, up to meshed MVDC.
- **Nearest substitutes:** Fuses + AC-side breakers with derating; point-to-point architectures that avoid DC breakers entirely.
- **Key uncertainty:** How fast Chinese DC parks standardize protection requirements into procurable specs.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-01]:** Blend of C-01 and A-02; CCC/GB certification + JV requirements erase foreign-entrant margin by 2030. Record retained as audit trail.

## P3R2-B-05 — Tailored-voltage-waveform RF bias + fast matching subsystem for Chinese etch/deposition OEMs

- **Product:** Arbitrary-waveform bias generator (multi-harmonic sheath shaping for ion-energy-distribution control) + frequency-agile solid-state match with sub-ms retune and pulse-synchronous metrology.
- **Buyer + pain evidence:** AMEC (etch RMB7.28bn +54.7% 2024, L06-048), NAURA/Piotech/ACM (L06-042/043, L01-044), SMIC/YMTC end-pull (L06-043); RF components <12% localized in 2024 (L06-054) vs tool-level 21–35% (L06-051/052, contradiction preserved); domestic RF base fragile (Hengyunchang customer concentration 45–63%, L06-042/043; Injet L06-044).
- **Technical mechanism:** TVW biasing research cluster L06-009/010/011/027; multifrequency matching demonstration L01-012.
- **Why incumbents miss it:** AE/MKS/Comet ship the current-generation platforms (L06-039, L01-049/050) and serve Chinese OEMs at arm's length under export-control pressure; domestic entrants are cloning conventional generators, not waveform control.
- **Decisive experiment + budget:** 2027-Q2, $350k: 3-harmonic synthesized bias narrows measured IED width ≥2x vs single-frequency at equal power on a lab CCP reactor.
- **TRL:** 4.
- **2026–2029 plan:** Waveform prototype + IED replication; export-control counsel FIRST; university joint experiments; match-speed benchmarks vs incumbents; OEM dev-chamber demo under joint-research agreement; lawful non-US-origin BOM qualification.
- **2030–2034 trigger (named):** AMEC/NAURA/Piotech supplier-localization programs under the 15th-FYP self-sufficiency push (Hengyunchang/Injet substitution wave, L06-042/043/044; component gap L06-054).
- **2030 competition:** Matured Hengyunchang/Injet, AE/MKS/Comet waveform features, CAS spinoffs.
- **Window/timing risk:** SEVERE export-control/access risk for advanced-node exposure; mitigate via legacy/compound-semi/panel tools first. Vertical integration risk (Piotech owns Hengyunchang stake).
- **Kill date:** 2033-12-31 if lawful channel blocked or no OEM JDA.
- **Big vision:** Waveform-defined plasma power displacing the duopoly's next-generation sockets across Asia.
- **Nearest substitutes:** Conventional dual-frequency bias + slow mechanical matches; incumbent premium generators.
- **Key uncertainty:** Export-control perimeter for a US-affiliated founder; must be resolved before any China commitment.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-A-10]:** Self-declared severe export-control risk on the core channel is the thesis, not a footnote; CN opportunity survives only as A-10's partitioned >=28nm line. Record retained as audit trail.

## P3R2-B-06 — Electrostatic-chuck power/control subsystem (clamp supply + JR leakage compensation + multi-zone thermal control)

- **Product:** ±kV programmable clamp supply with real-time leakage-current-based clamp-force estimation, arc-safe fast declamp with charge neutralization, 10+ zone heater drive electronics — the electronic half of a domestic ESC stack.
- **Buyer + pain evidence:** AMEC/NAURA/Piotech (L06-048, L06-042/043); Chinese ceramics developers active in ESC design space (L06-004); component-localization gap (L06-054). ESC physics unsolved: breakdown (L06-005), JR dynamics (L06-006), AlN resistivity (L06-014), thermal uniformity (L06-007/015).
- **Technical mechanism:** JR contact-current model inversion for force observation; sequenced neutralization declamp; mK-class multi-zone control.
- **Why incumbents miss it:** US/JP ESC vendors sell integrated chuck+electronics; Chinese ceramics entrants lack the electronics half; nobody merchants the control stack alone.
- **Decisive experiment + budget:** 2027-Q3, $220k: clamp-force estimate within ±10% of load-cell truth across temperature/aging; <100 ms safe declamp.
- **TRL:** 4.
- **2026–2029 plan:** JR physics testbed on commercial pucks; force-observer publication + patents; declamp wafer-displacement characterization; joint evaluation with one ceramics maker + one OEM dev chamber.
- **2030–2034 trigger (named):** Same 15th-FYP OEM localization wave (L06-042/044/054) extended to ESC subsystems as HAR etch tightens clamp/thermal specs (L06-048).
- **2030 competition:** Incumbent integrated ESC vendors; AE/MKS bundling clamp supplies (L06-039).
- **Window/timing risk:** ESC-specific China demand is inferential (no named tender) — P4 must verify; export-control caution lighter than B-05 (mature-node/panel first).
- **Kill date:** 2033-12-31 absent ceramics/OEM co-development.
- **Big vision:** Standard electronics layer for all electrostatic handling — semicon, panel, e-beam, reticle chucks, vacuum robotics.
- **Nearest substitutes:** Imported integrated ESC assemblies; in-house OEM electronics.
- **Key uncertainty:** Whether Chinese ceramics makers partner or hire the capability in-house.
- **[FIX applied 2026-07-13]:** product scoped to mature-node/panel tools; demand explicitly labeled inferential pending a named ESC-localization program/tender or ceramics-maker LOI (P4 gate); AE/MKS bundling-foreclosure check added.

## P3R2-B-07 — Thermal-shock-tolerant PCHE recuperators for China's sCO2 waste-heat retrofit wave

- **Product:** Diffusion-bonded PCHE recuperator family with graded channels + compliant headers rated for >20 °C/min transients, creep-qualified alloys, cycling warranties, embedded health monitoring.
- **Buyer + pain evidence:** CNNC/NPIC (30 MW commercial "Chaotan One", L04-048/051), CAS-IET (rapid-cycling PCHE named open problem, L04-029; programs L04-106/109), SMDERI (L04-102); retrofit market anchor ~RMB100bn/~300 units is single-source state media (L04-051 — flagged).
- **Technical mechanism:** Strain-graded channel geometry moves transient thermal strain off bond planes; materials qualification per documented sCO2 challenges (L04-113); valve/transient context (L04-111).
- **Why incumbents miss it:** Global PCHE incumbents sell steady-state-rated cores without China channels; Chinese institutes prototype in-house but don't productize cycling-rated merchant supply.
- **Decisive experiment + budget:** 2027-Q4, $500k: coupon-scale core survives 1,000 shock cycles (200→550 °C at ≥20 °C/min) with <5% effectiveness loss, CT-verified bond integrity.
- **TRL:** 4.
- **2026–2029 plan:** Bonding trials + shock rig; sub-scale 100 kW-class core + cycling life model; publication; joint test with a CN institute program; HK/JV manufacturing structure design.
- **2030–2034 trigger (named):** Follow-on procurement unlocked by CNNC's Xinjiang molten-salt+sCO2 project's national "first-set major technical equipment" designation (construction H1-2026 → 2028, L04-051) and Chaotan One replication across steel-sintering WHR (L04-048/051).
- **2030 competition:** CAS-IET/CNNC in-house fabrication; 1–2 Chinese HX entrants via national programs.
- **Window/timing risk:** JV/localization required for CNNC-adjacent sales; market size rests on one state-media figure — P4 must triangulate.
- **Kill date:** 2034-06-30 absent CN integrator PO or JV agreement.
- **Big vision:** The qualified compact-HX vendor of the advanced-cycle era (sCO2, CSP, nuclear BOP, fusion-adjacent).
- **Nearest substitutes:** Shell-and-tube WHR (bulky, lower effectiveness); institute-built one-off PCHEs.
- **Key uncertainty:** True size/pace of the sintering retrofit pipeline beyond the flagship units.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-08]:** Import graded-channel/compliant-header mechanism and CNNC first-set logic; RMB100bn TAM stays single-source-flagged. Record retained as audit trail.

## P3R2-B-08 — sCO2 turbomachinery seals and gas-foil bearings for Chinese compressor/turbine programs

- **Product:** Dense-CO2 dry-gas/EHD-compliant shaft seal cartridges + coated gas-foil bearing cartridges (27,000+ rpm class) with seal-health telemetry, drop-in for institute-led OEM machines.
- **Buyer + pain evidence:** CNNC/NPIC units (L04-048/051); SMDERI 100–150 kW compressors (L04-102); CAS-IET MWe program (L04-106) and turbine cooling work (L04-109); seals/bearings are catalogued sCO2 challenges (L04-113); EHD sCO2 seal still research-grade (L04-101).
- **Technical mechanism:** Film-riding groove geometry + elastohydrodynamic compliance handling dense-CO2 phase-margin excursions; engineered foil coatings for start-stop life.
- **Why incumbents miss it:** Oil-and-gas seal majors retrofit hydrocarbon designs; no merchant dense-CO2-specific cartridge line exists; institutes hand-build.
- **Decisive experiment + budget:** 2028-Q1, $600k: <0.5% leakage at representative dense-CO2 conditions over 500 h; 100 start-stop foil-bearing cycles at 30 krpm.
- **TRL:** 3.
- **2026–2029 plan:** Static/dynamic seal rig; EHD replication; spin-rig validation; publication + patents; institute co-test via research collaboration; JV supply pre-negotiation.
- **2030–2034 trigger (named):** Post-"first-set" follow-on units (Xinjiang 2028 completion, L04-051) and sintering-WHR fleet growth (L04-048) turning institute programs into component buyers.
- **2030 competition:** Institute in-house; adapted legacy dry-gas seals.
- **Window/timing risk:** Very narrow initial SAM; JV-only access; optional/extra seed by design.
- **Kill date:** 2033-12-31 absent institute co-test agreement.
- **Big vision:** The SKF-of-dense-fluids: cartridges for sCO2, supercritical H2, cryo turbopumps.
- **Nearest substitutes:** Labyrinth seals with high leakage penalties; oil bearings with contamination risk.
- **Key uncertainty:** Fleet size sensitivity — component economics only work if unit count scales past demonstrations.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-19]:** Self-labeled optional; narrow SAM, JV-only access. C-19 carries the concept. Record retained as audit trail.

## P3R2-B-09 — Standardized solid-state pulsed-power modulator platform for China's accelerator buildout

- **Product:** 50–150 kV / 100 A-class IGBT-Marx modulator family built from one qualified 3 kV brick with per-stage droop correction, fiber-synchronized gating, standard control API; klystron/magnetron/e-gun variants.
- **Buyer + pain evidence:** CGN Dasheng (RMB340M new contracts H1-2025, +21%, L05-035); China Isotope & Radiation cyclotron tender for three medical-isotope centers (L05-036); IHEP/CEPC RF as high-end channel (L05-012/013). Fragmentation pain: ≥5 non-interoperable modulator/SSPA designs documented (L05-003–009); coupler reliability failure mode (L05-014).
- **Technical mechanism:** Series-stacked solid-state Marx with active droop compensation — displacing PFN/thyratron chains, standardized rather than per-project.
- **Why incumbents miss it:** ScandiNova/Jema (L05-047/030) sell premium custom units project-by-project; Chinese institutes hand-build; nobody productizes a brick logistics model.
- **Decisive experiment + budget:** 2027-Q3, $400k: 10-stage stack, 30 kV/50 A, 1 ms flat-top <1% droop, 10^6 pulses, single-stage fault ride-through.
- **TRL:** 5.
- **2026–2029 plan:** Brick qualification; 100 kV prototype on dummy klystron load; 10^7-pulse reliability run; patents; Asian lab co-test; discovery with Chinese integrators; IEC HV pre-certification.
- **2030–2034 trigger (named):** CGN Dasheng fleet buildout/replacement (L05-035), China Isotope medical-isotope center program (L05-036), CEPC decision window in the 15th FYP (IHEP high-efficiency klystron program 78.5%→80.5%, L05-012/013 — approval uncertainty flagged).
- **2030 competition:** ScandiNova, Jema, CGN/CAEP in-house, likely CAS-spinoff.
- **Window/timing risk:** Nuclear-SOE procurement closed to foreigners — enter via medical/NDT integrators + JV licensing; dual-use export review required.
- **Kill date:** 2034-06-30 absent CN purchase/license + lab co-test.
- **Big vision:** The standardized brick family powering sterilization, NDT, cargo scanning, medical linacs, collider RF.
- **Nearest substitutes:** Legacy PFN/thyratron modulators; per-project custom solid-state builds.
- **Key uncertainty:** Whether Chinese integrators accept a merchant platform vs subsidized in-house builds.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-09]:** Nuclear-SOE access foreign-hostile. Import 3kV brick + droop-correction detail and CIRC tender evidence into C-09 CN chapter. Record retained as audit trail.

## P3R2-B-10 — HTS conductor/coil QC instrumentation: reel-to-reel Ic mapping + quench detection

- **Product:** (1) Reel-to-reel critical-current/defect mapper producing per-meter conductor passports (transport-current + Hall-array scanning, in-line strain screening); (2) multi-modal quench-detection/protection racks (voltage taps + fast fiber/acoustic, µs discrimination).
- **Buyer + pain evidence:** Shanghai Superconductor (State Grid Shanghai 35 kV commercial cable builder/operator, L03-041/052), WST (ITER strand, L03-031), ASIPP (35.1 T record, L03-029/037; CFETR design L03-024). Pain: strain/delamination/screening-current degradation (L03-018/020/021); tape supply concentrated in <10 vendors with allocation risk (L03-019).
- **Technical mechanism:** Continuous cryogenic Ic scanning correlated to defect libraries; quench discrimination fusing electrical + acoustic/fiber channels against documented HTS quench-energy physics (L03-018).
- **Why incumbents miss it:** Tape makers build minimal in-house rigs; instrument majors ignore the niche; magnet programs treat QC as bespoke acceptance testing.
- **Decisive experiment + budget:** 2027-Q2, $300k: ≥90% seeded-defect detection, <5% false positives at ≥10 m/min on commercial REBCO at 77 K, benchmarked vs destructive sampling.
- **TRL:** 5.
- **2026–2029 plan:** Benchtop scanner + multi-vendor tape validation; quench testbed on small coils; patents; pilot passporting with one tape maker (HK/Shanghai research collaboration); fusion-QA requirements engagement.
- **2030–2034 trigger (named):** CFETR/BEST magnet procurement decision in the 15th-FYP window (L03-024 — undated, flagged), ASIPP high-field expansion (L03-029/037), State Grid HTS cable follow-ons post-Shanghai (L03-041, single-installation caveat).
- **2030 competition:** In-house rigs; EU/JP instrument boutiques; Chinese institute builds.
- **Window/timing risk:** Best foreign-founder access profile in this batch (instrumentation, low control sensitivity); CFETR timing slip is the demand risk.
- **Kill date:** 2034-12-31 absent tape-maker install or fusion-program order.
- **Big vision:** Metrology-and-protection layer of the global HTS industry; in-service cable monitoring next.
- **Nearest substitutes:** Destructive sampling + witness coils; vendor self-certification.
- **Key uncertainty:** Whether Chinese tape makers buy neutral QC or keep it proprietary.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-D-02]:** Bundles two canonicals (tape QC->D-02, quench->D-01). Import conductor-passport framing and CN buyer set into D-02. Record retained as audit trail.

## P3R2-B-11 — kW-class 4–20 K cryoplant skids for mid-scale Chinese HTS/accelerator programs

- **Product:** Standardized turbo-Brayton/pulse-tube hybrid skids, 100 W–1 kW at 10–20 K, N+1 redundancy, automated cooldown, remote monitoring — industrial-chiller productization of cryogenics.
- **Buyer + pain evidence:** ASIPP facilities (L03-029/037), HTS cable cooling stations (L03-041), IHEP-class programs (procurement style, L07-045). Gap: catalog coolers are mW–W class (PT205 10 mW@2.5 K, L03-050) vs bespoke kW plants (JT-60SA ~9.5 kW context, L03-025/026).
- **Technical mechanism:** Mid-scale cycle optimization + redundancy/controls engineering; the product is standardization and availability, not new thermodynamics.
- **Why incumbents miss it:** Cryoplant majors sell engineered projects; cooler makers sell catalog units; the middle is unserved.
- **Decisive experiment + budget:** 2028-Q2, $700k: 50 W@20 K demonstrator, ≥95% availability over 1,000 h unattended, cost model ±20%.
- **TRL:** 4.
- **2026–2029 plan:** Architecture/vendor mapping; sub-scale demonstrator; reliability controller; cost-per-watt publication; partner-lab field trial; JV/licensing talks with Chinese cryo makers.
- **2030–2034 trigger (named):** CFETR/BEST-era facility buildout (L03-024, undated — flagged) + State Grid HTS replication (L03-041).
- **2030 competition:** Global majors (bespoke), scaling Chinese cryocooler firms, institute in-house plants — atlas competitor data thin (L03-050 only); P4 must map Chinese cryo industry before promotion.
- **Window/timing risk:** Capital-intensive; China-only big-science rules force JV; domestic closure risk pre-2030. Optional/extra seed.
- **Kill date:** 2033-12-31 if P4 finds domestic skid products shipping or no trial partner.
- **Big vision:** Cryogenics-as-a-utility for the superconducting economy.
- **Nearest substitutes:** Arrays of catalog cryocoolers; bespoke helium plants.
- **Key uncertainty:** Chinese domestic cryo capability trajectory (unmapped in atlas).
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-12]:** Atlas competitive intel on Chinese cryo industry admittedly absent; mapping task moves to C-12 FIX. Record retained as audit trail.

## P3R2-B-12 — NEG-coating and low-outgassing surface-engineering line for Chinese UHV fabricators

- **Product:** Licensed production cell: TiZrV NEG sputter-coating line for beampipes/chambers + vacuum-firing/bakeout optimization + witness-sample outgassing metrology and QA protocol.
- **Buyer + pain evidence:** China-registered chamber manufacturers who alone may bid IHEP/HEPS-class tenders (China-only rule, L07-045); bakeout burden 250 °C/30 h for >70,000x H2 reduction (L07-009, physics L07-008); NEG commercially near-single-vendor globally (SAES, L07-037; foundational L07-001).
- **Technical mechanism:** Getter-film distributed pumping after low-temperature activation replaces lumped pumps; process know-how (uniformity in long narrow pipes) is the moat.
- **Why incumbents miss it:** SAES exports coated parts but doesn't enable Chinese domestic fabricators; institutes coat in-house at lab scale only.
- **Decisive experiment + budget:** 2027-Q3, $350k: 2 m narrow-bore pipe coated to spec pumping speed, ≥20 activation cycles without loss, verified on in-house outgassing bench.
- **TRL:** 5.
- **2026–2029 plan:** Coating replication + metrology bench; real-geometry pilots; fixture patents; license negotiation with 1–2 Chinese fabricators (HK IP entity + domestic licensee to fit tender rules); IHEP vacuum-group requirements discovery.
- **2030–2034 trigger (named):** Post-HEPS light-source/FEL pipeline and — if approved in the 15th FYP — CEPC vacuum procurement (IHEP RF investment evidences program, L05-012/013; approval uncertainty flagged); domestic-bid rule funnels demand to licensees (L07-045).
- **2030 competition:** SAES export sales; IHEP in-house coating; possible CAS spinoff.
- **Window/timing risk:** Lumpy, approval-dependent demand; IP-leakage risk in licensing (mitigate via consumables/QA lock-ins).
- **Kill date:** 2034-12-31 absent a license deal and any new large CN accelerator approval.
- **Big vision:** Surface-engineering layer of the vacuum world; maintenance-free compact UHV for portable quantum instruments.
- **Nearest substitutes:** Lumped ion/Ti-sublimation pumping; longer bakeouts.
- **Key uncertainty:** CEPC/next-light-source approval timing.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-A-05]:** License-into-China model = IP leakage in a process-know-how business; CEPC-dependent lumpy demand; licensee accumulates the asset. Record retained as audit trail.

## P3R2-B-13 — Low-ripple rectification and power-quality retrofits for Chinese green-H2 plants and electrowinning

- **Product:** MW-scale IGBT active-front-end + interleaved DC skids, <1% current ripple, degradation-aware current scheduling for renewable-coupled operation, harmonic compliance, per-stack ripple analytics. Same core for electrowinning tank houses.
- **Buyer + pain evidence:** Sinopec (Kuqa documented below-nameplate operation, L11-049), China Energy Construction (125-set tender, L11-051), LONGi/Peric/Sungrow channels (L11-050/051); ripple penalty up to ~14% specific energy (L11-016–021); intermittency-driven degradation (L11-001/003/004/031); shunt-current scale-up physics (L11-012/013); EW analog (L11-045, L11-026/027). Stack overcapacity ~2x demand (L11-035, L11-051) — this seed deliberately sells power quality, NOT stacks.
- **Technical mechanism:** Active rectification + interleaving kills low-order ripple; scheduler maps renewable variability into stack-safe current trajectories using documented stressor physics.
- **Why incumbents miss it:** Thyristor six-pulse is entrenched capex-optimized practice; stack OEMs bundle cheap BOP; nobody sells efficiency retrofits against the installed base.
- **Decisive experiment + budget:** 2027-Q2, $450k: short-stack testbed shows ≥8% specific-energy gain + quantified degradation-rate reduction vs 6-pulse baseline over 1,000 h of emulated wind/solar.
- **TRL:** 5.
- **2026–2029 plan:** HIL ripple-degradation correlation; publication + scheduling patents; 100 kW AFE prototype with measured deltas; EPC/EW-operator retrofit-economics discovery; containerized 1 MW pilot design; OEM/EPC channel pre-agreement.
- **2030–2034 trigger (named):** Continuing Sinopec/China Energy Construction electrolyzer tender cadence in the Xinjiang/Inner-Mongolia renewable-hydrogen bases (L11-049/050/051) through the 15th FYP, plus retrofit demand from documented utilization shortfalls (L11-049). 15th-FYP hydrogen targets to be re-verified in P4 (2026 baseline).
- **2030 competition:** Sungrow is the decisive threat (power-electronics giant already in tenders, L11-051); rectifier incumbents; OEM in-house BOP (Nel/thyssenkrupp contraction context L11-047/048).
- **Window/timing risk:** Brutal Chinese power-electronics cost curve; SOE entry via EPC partners only; EW China buyer evidence not yet named (P4 item).
- **Kill date:** 2033-06-30 if Sungrow ships equivalent ripple specs first or no EPC partnership.
- **Big vision:** The precision-DC layer of world electrochemical industry — H2, EW, chlor-alkali, e-fuels.
- **Nearest substitutes:** 12-pulse thyristor + filters; oversizing stacks to hide losses.
- **Key uncertainty:** Whether efficiency-per-yuan wins tenders while capex-per-watt still dominates buying criteria.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-07]:** Sungrow as buyer-and-giant-competitor kills CN-primary standalone. Import Kuqa retrofit evidence + degradation-weighted scheduling into C-07. Record retained as audit trail.

## P3R2-B-14 — Dual-standard MW charging/swap interface converters (GB swap ↔ IEC TS 63379 MCS)

- **Product:** Bidirectional 1–3.75 MW SiC converter family with swappable "interface personalities": GB/T swap-station DC profile on one side, IEC TS 63379 MCS (1,250 V/3,000 A class) on the other, with certified protocol/interlock stacks.
- **Buyer + pain evidence:** XCMG (240t BEV exports to Fortescue, phased 2028–2030, L10-028), SPIC Qiyuan (swap-tech export, Oyu Tolgoi, L10-031), swap-standard ecosystem (excavator swap standard L10-046; CCS battery-ship rules L10-045; Jining 6006 swap vessel L10-040). Pain: documented non-recognition between Chinese swap standards and CharIN/IEC MCS (L10-050 vs L10-045/046), forcing bespoke interfaces per export project (trolley-compatible trucks L10-052 add a third architecture).
- **Technical mechanism:** Modular SiC DC-DC bricks + protocol arbitration layer handling both standards' safety interlocks; certification engineering is the moat.
- **Why incumbents miss it:** OEM power teams solve one project at a time; Western charger vendors implement MCS only; CATL ecosystem implements swap only.
- **Decisive experiment + budget:** 2028-Q1, $500k: 250 kW dual-personality converter passes scripted conformance for both standards on a battery emulator incl. cross-standard fault interlocks.
- **TRL:** 4.
- **2026–2029 plan:** Standards deep-dive + reference protocol implementation; interlock-arbitration patents; 250 kW brick; interop test methodology publication; OEM export-program field-data partnership (HK entity); pre-certification plan.
- **2030–2034 trigger (named):** XCMG–Fortescue deliveries 2028–2030 and follow-on Western bids (L10-028); SPIC swap exports post-Oyu-Tolgoi trial (ends 2026, L10-031); domestic SOE tender cadence (China Gold 60-truck class L10-034; Baogang L10-035).
- **2030 competition:** XCMG in-house, CATL swap ecosystem (L10-031/040), MCS-only Western vendors.
- **Window/timing risk:** If Western mines reject swap outright, dual-standard need collapses to MCS-only; monitor Fortescue/Rio architecture choices (L10-028/031). Foreign founder advantaged on IEC-side certification.
- **Kill date:** 2034-06-30 absent OEM co-development, or earlier if one standard wins outright by 2032.
- **Big vision:** The interoperability layer of global heavy-fleet electrification, incl. port cranes and e-vessel shore/swap stations.
- **Nearest substitutes:** Per-project bespoke interface engineering; carrying dual charging hardware on vehicles.
- **Key uncertainty:** Survival horizon of the two-ecosystem split.
- **[FIX applied 2026-07-13]:** 2028 named-export-program procurement-evidence gate added; fold-in path to A-21 pre-agreed; demand reclassified as contingent standards-arbitrage option, not base demand.

## P3R2-B-15 — Industrial plasma power-and-matching platform for Chinese non-semi plasma equipment

- **Product:** 1–30 kW pulsed-DC and RF supplies with integrated fast matching, sub-µs arc detection/energy diversion, recipe-level digital control and fleet telemetry, for coating/cleaning/treatment tool builders.
- **Buyer + pain evidence:** PCB plasma-cleaning tenders (Wuxi Shennan Circuit, L01-114); institutional PECVD demand (AVIC Xi'an FACRI award, L01-039 — signal, not target); Chinese plasma-tool ecosystem growth (L01-044). Imports define the mid-market envelope (Comet 13–60 MHz/0.6–6 kW, L01-050; TRUMPF efficiency claims, L01-049; AE platform ramp, L01-040); frontier matching still research-grade (L01-012).
- **Technical mechanism:** Fast solid-state matching + arc-energy diversion topology; telemetry for uptime service economics.
- **Why incumbents miss it:** Duopoly premium lines overshoot mid-market price points; local low-end units lack pulsing/arc management; semi-focused domestic entrants ignore non-semi tools.
- **Decisive experiment + budget:** 2027-Q1, $200k: <1 µs arc detection/diversion over 10,000 induced arcs with zero target damage; reflected power <2% across 3:1 load swing.
- **TRL:** 5.
- **2026–2029 plan:** 5 kW pulsed-DC prototype + arc bench; RF variant + matching module; reliability runs; patents; field beta on one Chinese PCB/coating line via equipment-maker collaboration; China manufacturing-license BOM.
- **2030–2034 trigger (named):** PCB/advanced-packaging equipment upgrade cycle evidenced by recurring MOFCOM plasma tenders (L01-114, L01-039) and the AI-server PCB wave (Han's PCB equipment +50% in 2025, L12-037) running through 2030–2034.
- **2030 competition:** AE/MKS/Comet/TRUMPF imports (L01-040/049/050); Hengyunchang/Injet moving down-market (L06-042/044); local low-end.
- **Window/timing risk:** Price-war exposure if differentiation fails; sell to OEMs/toolmakers, not fabs; moderate access.
- **Kill date:** 2033-12-31 absent OEM design-win or on margin collapse.
- **Big vision:** Power-and-control brain of industrial plasma across Asia; waveform control feeding future plasma chemistry.
- **Nearest substitutes:** Imported premium generators; bare-bones domestic supplies.
- **Key uncertainty:** Mid-market margin durability against domestic cost curves.
- **[Adjudication 2026-07-13 - REJECT]:** Mid-market China plasma power = features-per-yuan commodity fight by 2030; Hengyunchang/Injet down-market motion; arc-quench IP insufficient moat. Record retained as audit trail.

## P3R2-B-16 — Deterministic timing and fast-interlock platform for Chinese big-science facilities

- **Product:** White-Rabbit-grade switches/nodes (sub-ns sync over km fiber), deterministic fast-interlock I/O crates (µs machine protection, formal-verified logic), configuration/monitoring software, long-term support contracts, China-compatible open-hardware licensing.
- **Buyer + pain evidence:** IHEP facilities (domestic procurement style, L07-045), ASIPP (ITER magnet-feeder integrator, L13-035), industrial accelerator fleets (CGN Dasheng, L05-035). Pain: I&C integration burden documented at ITER scale (L13-030); WR ecosystem only formalized 2024 (L13-026/027) — no productized supported platform for the Chinese pipeline.
- **Technical mechanism:** IEEE 1588-2019/White Rabbit sub-ns extension + deterministic interlock fabric.
- **Why incumbents miss it:** EU WR vendors are small and Europe-focused; Chinese institutes self-build without product support layers; US vendors face export-control friction (L13-031) — an opening for a carefully scoped non-quantum offering.
- **Decisive experiment + budget:** 2027-Q4, $250k: 10-node network <100 ps skew over 5 km fiber for 30 days; interlock crate <10 µs verified trip latency over 1,000 injected faults.
- **TRL:** 5.
- **2026–2029 plan:** Build on open WR designs + upstream contributions; benchtop sync demo; formal-verified interlock crate; reliability publication; requirements engagement with an Asian facility control group; pilot at a university accelerator; China license/manufacture structure.
- **2030–2034 trigger (named):** CFETR/BEST-era fusion I&C procurement (ASIPP role, L13-035; decision undated — flagged, L03-024) + next-round CAS light-source/collider controls (procurement style L07-045); CGN-class industrial synchronization demand (L05-035).
- **2030 competition:** EU WR vendors, strong institute in-house groups (ISSCC/VLSI-level Chinese circuit capability, L13-022/023).
- **Window/timing risk:** Export-control scoping is the gating uncertainty (strictly non-quantum, counsel required, L13-031); China-only procurement forces licensing; institute self-supply culture.
- **Kill date:** 2033-12-31 if export scoping fails or no facility pilot.
- **Big vision:** The nervous system of every large machine — accelerators, fusion plants, observatories, distributed pulsed-power fleets.
- **Nearest substitutes:** Institute-built timing systems; generic PTP gear (insufficient determinism).
- **Key uncertainty:** Legal perimeter for a US-affiliated founder selling facility electronics into CAS institutes.
- **[Adjudication 2026-07-13 - REJECT]:** Open hardware = born-commodity; support/integration is consulting-shaped; Chinese institutes self-supply; China-only procurement + quantum export scoping unresolved. Record retained as audit trail.

## P3R2-B-17 — 225–300 °C downhole electronics module for Chinese deep-well and geothermal drilling

- **Product:** Hermetic downhole module: 225 °C SOI controller + SiC power stage + precision sensor front-end, optional sorption/evaporative cooling cartridge for 250–300 °C zones, delivered with full qualification data packs.
- **Buyer + pain evidence:** Chinese downhole-tool OEMs/oilfield institutes (HT drilling gaps diagnosed by China University of Petroleum, L15-021); XJTU SiC sensor programs needing qualified readout/power (L15-006/007). Supply shock: CISSOID CHT obsolete/last-time-buy with no successor (L15-043); no platform above ~250 °C (SOI ~300 °C L15-004; NASA SiC 500 °C lab-proven L15-009; DARPA still funding 800 °C basics 2026, L15-026); thermal and radiation hardness don't transfer (L15-013, L15-020).
- **Technical mechanism:** Hybrid strategy bridging the documented native-HT vs active-cooling split (L15-023/024): qualified 225 °C native electronics + plug-in cooling for excursions.
- **Why incumbents miss it:** Western HT-IC suppliers are exiting or defense-captive; Chinese institutes research devices but no merchant qualified-module vendor exists.
- **Decisive experiment + budget:** 2027-Q4, $550k: 1,000 h at 225 °C + 200 thermal cycles, <5% drift, zero failures; cooling cartridge holds ≤225 °C internal in a 275 °C oven for 8 h.
- **TRL:** 4.
- **2026–2029 plan:** Component screening + soak/cycling testbed; CHT-fallout gap analysis publication; module prototype; sorption cartridge demo; MIL-STD-883-class qualification; tool-OEM discovery via HK channel; supply-agreement drafts.
- **2030–2034 trigger (named, weakest in batch — flagged):** Chinese deep gas (Sichuan/Tarim archetype) and hot-dry-rock geothermal programs implied by the L15-021 research push; the atlas contains NO named Chinese HT-electronics procurement (documented transparency asymmetry). Global corroboration: superhot-geothermal trajectory (ARPA-E SUPERHOT >375 °C, L15-029). P4 must find a named CN program or this seed dies.
- **2030 competition:** TI HT catalog parts (partial coverage), surviving CISSOID lines under new ownership, CAS in-house hybrids (L15-013/020).
- **Window/timing risk:** Inferential China demand; SOE access via tool-OEM channel; dual-use review. High upside, low confidence.
- **Kill date:** 2033-06-30 if 2027–2028 discovery cannot produce two Chinese tool-OEM LOIs.
- **Big vision:** The Honeywell-successor hot-electronics platform; path to 500 °C SiC-native modules (L15-009 physics).
- **Nearest substitutes:** Derated 175–200 °C automotive parts + heat shielding; mud-pulse-limited dumb tools.
- **Key uncertainty:** Existence and size of a named Chinese buyer program.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-A-14]:** Atlas contains no named Chinese HT-electronics procurement (self-flagged); China-primary company on inferential demand fails the demand rule; revisit from A-14 if evidence appears. Record retained as audit trail.

## P3R2-B-18 — Flywheel transient power stabilization modules for Chinese AI datacenter parks

- **Product:** Containerized high-cycle flywheel + SiC bidirectional converter: seconds-scale MW buffering, sub-cycle ride-through, generator-start bridging, DC-coupled to 800 V park buses; unlimited cycling, 20-year life, no battery fire-code burden.
- **Buyer + pain evidence:** Chinese hub-park operators/integrators (Alibaba HVDC lineage L02-048/049; 800 V integration pain L02-054) under PUE policy (L14-035). Demand bridge (per atlas enthusiasm-zone rule): named Western proof — Piller SHIELDX flywheels selected for a 400 MW off-grid AI datacenter plant, shipments from Dec-2025 (L16-052).
- **Technical mechanism:** Kinetic buffering of GPU load swings; converter control doubling as bus damping (synergy with B-03); capacitor-fleet stress relief (L02-010).
- **Why incumbents miss it:** Chinese UPS majors are battery-centric; BESS default thinking ignores cycle-life economics of second-scale swings.
- **Decisive experiment + budget:** 2028-Q2, $600k: 100 kW module, 0–100% load step <2 ms, 100,000 accelerated cycles without fade.
- **TRL:** 5.
- **2026–2029 plan:** GPU-park transient modeling; converter-flywheel co-simulation; CN flywheel manufacturing partner mapping; 100 kW prototype with purchased rotor + custom converter; DC-coupling patents; co-demonstration proposal with one Chinese integrator.
- **2030–2034 trigger (named):** 东数西算 hub expansion (L02-049) + 800VDC park rollouts (L02-048/054) in the 15th FYP, replicating the Piller 400 MW AI-plant architecture (L16-052).
- **2030 competition:** Piller (L16-052), Chinese UPS majors adding flywheels, BESS as default substitute.
- **Window/timing risk:** No named Chinese flywheel-datacenter buyer yet (flagged); BESS price collapse narrows niche; integrator design-in required.
- **Kill date:** 2033-12-31 absent a Chinese park pilot commitment or if BESS wins the transient niche.
- **Big vision:** Kinetic power quality as standard AI-infrastructure equipment; microgrid inertia and pulsed industrial loads next.
- **Nearest substitutes:** Supercap banks; oversized BESS; diesel-rotary UPS.
- **Key uncertainty:** Chinese operators' willingness to adopt non-battery buffering.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-D-19]:** CN demand bridge admitted absent; Piller precedent is Western. D-19 carries the concept. Record retained as audit trail.

## P3R2-B-19 — Precision pulsed laser-driver and timing modules for Chinese ultrafast/micromachining OEMs

- **Product:** GaN sub-ns pump/seed driver modules with programmable pulse shaping, ps-jitter trigger/timing distribution, burst-mode energy control — qualified drop-ins for ultrafast, UV-drilling and precision-marking platforms.
- **Buyer + pain evidence:** Han's Laser (high-power ASP collapse: segment revenue −6.6% on +30.5% units, 2025; PCB/IT equipment +50% on AI-server demand — L12-037), Raycus (up-market pivot + export growth, L12-038), Maxphotonics/top-3 cluster (L12-054, 2021-vintage share data flagged). Driver electronics are documented open research: GaN high-peak drivers (L12-027), modulation-shape control (L12-025), sub-ns digital drivers (L12-026).
- **Technical mechanism:** GaN fast-edge current stages + closed-loop pulse-shape linearization + ps timing distribution.
- **Why incumbents miss it:** Price-war OEMs underinvest in electronics NRE; analog-semi vendors sell generic parts; EU boutiques are low-volume/high-price.
- **Decisive experiment + budget:** 2027-Q2, $180k: programmable 0.5–5 ns pulses at ≥50 A peak, <20 ps RMS jitter, closed-loop shape control on a test diode array.
- **TRL:** 4.
- **2026–2029 plan:** Driver prototype at published state-of-art; jitter bench; shaping firmware + patents; 10^12-pulse reliability data; design-in eval with one Chinese ultrafast OEM via HK component channel.
- **2030–2034 trigger (named):** China's AI-server advanced-PCB/substrate drilling capacity expansion (demand driver documented at Han's, L12-037) pulling UV/ultrafast tools and their drivers through 2030–2034; Raycus ultrafast line expansion (L12-038).
- **2030 competition:** OEM in-house teams, generic analog-semi drivers, EU boutiques; incumbent context (IPG price-war disclosure, L12-034).
- **Window/timing risk:** Insourcing pressure; moderate access (component design-in); firmware-heavy IP defensible.
- **Kill date:** 2033-12-31 absent OEM design-win.
- **Big vision:** The driver-and-timing layer of global photonic tools — PCB drilling to LiDAR test to bio-imaging.
- **Nearest substitutes:** In-house driver boards; repurposed generic pulser ICs.
- **Key uncertainty:** ASP defensibility once a design win scales in China.
- **[Adjudication 2026-07-13 - REJECT, duplicate of P3R2-C-13]:** Import price-war-driven up-market OEM pivot logic as C-13's CN demand chapter. Record retained as audit trail.

## P3R2-B-20 — Ultrasonic weld generator with inline physics-based quality monitoring for EV battery lines (optional)

- **Product:** Adaptive ultrasonic generator (frequency/amplitude under load) + inline weld-quality classification from electrical-impedance and acoustic signatures with closed-loop correction.
- **Buyer + pain evidence:** CATL/BYD lines via integrators — the two took >50% of Jiaocheng Ultrasonic's comparable 2021 equipment purchases; Jiaocheng est. 20–30% share (L16-028; 2021 vintage explicitly flagged).
- **Technical mechanism:** Physics-model-based signature classification (not generic ML) tied to weld-formation dynamics; closed-loop parameter correction.
- **Why incumbents miss it:** Incumbent monitoring is threshold-based; quality escapes surface at pack level where scrap is costly.
- **Decisive experiment + budget:** 2027-Q3, $250k: ≥95% pull-strength-category prediction across 5,000 instrumented Cu/Al welds, beating fixed-parameter scrap baselines.
- **TRL:** 4.
- **2026–2029 plan:** Lab weld cell + destructive-test correlation; closed-loop prototype; patents; one integrator-line pilot; explicit go/no-go vs incumbent feature parity.
- **2030–2034 trigger (named, weak — flagged):** CATL/BYD equipment replacement cycles (L16-028); next-gen (solid-state) line timing NOT evidenced in atlas — fresh P4 evidence required before promotion.
- **2030 competition:** Jiaocheng and Chinese peers, global ultrasonic majors, incumbent in-house features. High discard probability.
- **Window/timing risk:** Hardest access profile in batch: entrenched domestic suppliers + 2-buyer concentration.
- **Kill date:** 2032-12-31 if 2027 lab results show no monitoring advantage.
- **Big vision:** Acoustic process-control platform: wire bonding, busbars, solid-state stack joining, ultrasonic AM QA.
- **Nearest substitutes:** Incumbent weld monitors; post-process resistance/pull sampling.
- **Key uncertainty:** Whether any monitoring edge survives incumbent replication.
- **[Adjudication 2026-07-13 - REJECT]:** Self-labeled weakest/discardable; 2021-vintage data; entrenched domestic incumbents with >50% buyer concentration. Record retained as audit trail.

## P3R2-B-21 — Plasma-chamber arc/ESC-discharge detection and wafer-protection interlock module (optional; merge candidate with B-05/B-06)

- **Product:** Generator-agnostic arc-event module: RF reflected-power + optical-emission + ESC leakage-transient fusion detection, µs interlock, event forensics logging.
- **Buyer + pain evidence:** AMEC/NAURA/Piotech localizing RF stacks (L06-048, L06-042/043, gap L06-054); open literature thin vs patents (single confirmed method paper, L06-018; ESC discharge physics L06-005/006) — incumbent detection ships bundled in AE/MKS units (L06-039).
- **Technical mechanism:** Multi-physics sensor fusion with µs latency and forensic event capture.
- **Why incumbents miss it:** Detection is a bundled feature, never a neutral, generator-agnostic layer for domestic RF stacks.
- **Decisive experiment + budget:** 2027-Q3, $200k: ≥99% seeded micro-arc detection, <10 µs latency, <0.1% false trips over 72 h plasma-on.
- **TRL:** 4.
- **2026–2029 plan:** Arc-injection testbed + dataset; FPGA prototype; freedom-to-operate analysis (patent-dense field — gating); OEM dev-chamber eval.
- **2030–2034 trigger (named):** Attach-rate to every domestically shipped RF generator under the 15th-FYP OEM localization wave (L06-048/054).
- **2030 competition:** AE/MKS bundled features (L06-039), Hengyunchang basic detection (L06-042).
- **Window/timing risk:** FTO risk primary; small ASP — likely bundled with B-05/B-06 at longlist stage; B-05-class export caution.
- **Kill date:** 2033-06-30 if FTO blocked or no OEM eval.
- **Big vision:** Chamber-event intelligence: arc prevention, chuck-life prediction, drift detection.
- **Nearest substitutes:** Bundled generator features; periodic chamber inspection.
- **Key uncertainty:** Patent thicket navigability.
- **[Adjudication 2026-07-13 - MERGED INTO P3R2-A-10]:** Real gap, small ASP, patent thicket - merge candidate by its own admission. 2026-07-13 FIX applied via merge: folded into P3R2-A-10 as its arc/ESC-discharge event-detection and forensics layer (mature-node scope); FTO analysis before any further investment is A-10's precondition for this layer (patent-dense field). Record retained as audit trail. Record retained as audit trail; not independently promotable.

## P3R2-B-22 — DC-link capacitor and converter health prognostics module for Chinese converter fleets

- **Product:** Embedded/retrofit sensing: excitation-free in-situ ESR/capacitance tracking (synchronous demodulation of native switching ripple), hotspot estimation, physics-of-failure RUL models, fleet reporting. Hardware + models, not analytics consulting.
- **Buyer + pain evidence:** Chinese rack/UPS/HVDC power vendors (Delta China L02-048, Autrans L02-049; grid-chain expansion via XJ Electric-scale channel, L08-034); capacitors are a leading converter failure mechanism with density-compressed margins (L02-010); mission-critical 800 V fleets multiplying (L02-054, L02-043).
- **Technical mechanism:** No injected signals — demodulate existing ripple against thermal state; electrolyte-loss/film self-healing statistical RUL.
- **Why incumbents miss it:** Vendor telemetry stops at voltage/temperature; test majors sell bench instruments, not embedded fleet prognostics.
- **Decisive experiment + budget:** 2027-Q1, $150k: ESR tracking within 5% of LCR ground truth across 2,000 h accelerated aging of 20 caps in a live 10 kW converter, correct end-of-life rank ordering.
- **TRL:** 4.
- **2026–2029 plan:** Accelerated-aging lab; tracking validation; module prototype in live converter; RUL calibration; patents; fleet pilot with one Chinese PSU vendor (HK design-in).
- **2030–2034 trigger (named):** 东数西算-era HVDC/800 V fleets installed 2026–2029 reaching capacitor mid-life in 2030–2034 (L02-048/049/054); operators already buy on maintenance economics (NVIDIA 70%-maintenance-reduction framing, L02-043).
- **2030 competition:** Vendor in-house telemetry, test-equipment majors, academic spinoffs.
- **Window/timing risk:** Feature-not-product risk — hedge by serving third-party maintenance operators; moderate access.
- **Kill date:** 2033-12-31 absent vendor design-win.
- **Big vision:** Reliability nervous system for the world's converter fleets; extend to die-attach degradation tracking.
- **Nearest substitutes:** Scheduled replacement; bench ESR spot checks; simple temperature alarms.
- **Key uncertainty:** Willingness of vendors to pay for third-party prognostics vs building basic versions in-house.

---

Batch summary: 22 seeds; primary lanes L01, L02(x2), L03(x2), L04(x2), L05, L06(x3), L07, L08, L10, L11, L12, L13, L14(x2), L15, L16(x2) = 15 distinct lanes. Seeds B-08, B-11, B-15, B-17, B-18, B-20, B-21 are deliberate extras with explicit weak points so the orchestrator can discard; B-21 is a merge candidate into B-05/B-06.

EE/CE transfer note (generic, appended after seed freeze): every seed in this batch reduces to a small number of transferable electrical/computer-engineering competencies — precision power conversion and gate-drive design, fast protection and fault discrimination, deterministic timing/control electronics, physics-based sensing/metrology, and reliability qualification — so capability built for any one seed materially de-risks the others.
- **[FIX applied 2026-07-13]:** retrofit SKU + cross-vendor failure-database moat made explicit; 2028 named design-win LOI gate added; US secondary market kept active to avoid CN-access dependence.

