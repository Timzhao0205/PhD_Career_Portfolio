# SEEDS — Batch A (Process Industries): L01 plasma, L06 semicon subsystems, L07 vacuum/ultraclean, L11 electrochemical/precision power

18 seeds (A01–A18), generated evidence-first from the P2-adjudicated atlas. All source IDs are
accepted records in `10_SOURCE_ATLAS/Lxx_verified_sources.json`. Verifier corrections respected:
L07-051's TSMC-JDA/$200M claims are NOT used; L11-055 (rejected) not cited; no electrolyzer-stack,
plasma-gasification, open-market VOC, or seawater-electrolysis plays (per ATLAS Section 6).
Founder profile was not read until after these seeds were frozen; founder_fit_note is a
capability-transfer sentence only (fit capped at 5/100 downstream).

## A01 — Shared-bus multi-channel plasma power rack for "numbering-up" plasma chemistry (L01; sec L11, L06)
- Buyer: plasma-chemistry plant developers — Nitricity (sold out through 2028, L01-031), N2 Applied/GEA (L01-033), NEDO consortium (L01-043).
- Pain: numbering-up multiplies power supplies + matches per cell (L01-014/015/016); only semiconductor-priced single-channel generators exist (L01-040/049/050).
- Product/mechanism: one PFC front end + 400–800 V DC bus; 8–64 hot-swap 1–5 kW resonant channel cards with electronic (frequency-agile) impedance tracking, per-channel arc quench; optional ns-pulse stage (L01-105, L01-112).
- Incumbents miss: AE/MKS/Comet/TRUMPF sell semiconductor-margin single channels; no $/kW industrial rack.
- Experiment: 8-ch 2 kW/ch rack on gliding-arc/DBD array; efficiency, $/kW, arc ride-through — $140k.
- Vision: power backbone of electrified chemical plants. Substitutes: discrete generators, Chinese entrants (L06-042/044), in-house builds.
- Uncertainty: field still pre-industrial (L01-009/028); anchor customers may build in-house. Confidence: medium.

## A02 — Transportable plasma PFAS destruction unit for defense remediation (L01; sec L07)
- Buyer: US DoD (delivered $2.25M plasma PFAS contract, >300 t, L01-036); defense primes (L01-034/035).
- Pain: single supplier (PyroGenesis) with delivered contracts; no site-mobile mid-scale per-tonne option.
- Product/mechanism: containerized 100–500 kW transferred-arc cell; C–F mineralization at 4,000–10,000 K, alkaline quench to CaF2, onboard DRE verification (waste-plasma physics analogue L01-102).
- Incumbents miss: PyroGenesis sells bespoke MW torch projects; SCWO handles liquids only.
- Experiment: 50 kW bench rig on spent AFFF/IX resin, third-party ≥99.99% DRE incl. short-chain — $200k.
- Vision: national mobile destruction fleet; industrial/water-utility residuals. Substitutes: PyroGenesis (L01-034/035/036), SCWO, storage.
- Uncertainty: EPA driver unverified in ledger; economics vs. SCWO/incineration. Confidence: medium.

## A03 — Retrofit ion-energy-distribution synthesizer (tailored-waveform bias generator) (L06; sec L01)
- Buyer: fab process-dev groups (Samsung co-authorship, L06-009), China OEMs (AMEC, L06-048), AE-customer base hitting sub-2nm walls (L06-039).
- Pain: tailored-voltage-waveform ion-energy control is the active frontier (L06-009/010/011/027) with no off-the-shelf retrofit; ALE labs underserved (L01-103/109).
- Product/mechanism: 5+ phase-locked harmonics + DC tail, 1–10 kW, broadband EVC match, sheath-model feedback, integrated arc detection (L06-018).
- Incumbents miss: AE/MKS/Comet productize slowly for top-3 fab platform deals only (L06-039/049).
- Experiment: 2-harmonic + DC-tail on ICP testbed with RFEA; ≥3x IEDF narrowing — $180k.
- Vision: ion-energy control layer for all atomic-scale processing. Substitutes: AE EVOS/Everest (L06-039), Comet Synertia (L06-049), Kyosan (L06-050), Hengyunchang (L06-042).
- Uncertainty: incumbent productization race, export controls on China channel, IP thicket. Confidence: medium.

## A04 — Pressure-based fast-transient MFC (SEMI E17-certified, <100 ms, zero overshoot) (L06; sec L07)
- Buyer: Ichor ($947.7M gas-delivery revenue, L07-049), AMEC/Piotech-class OEMs (L06-048/042), US subfab buildout (L06-033).
- Pain: MFC transient response is standards-codified as a throughput constraint (SEMI E17, L06-035) and still an active control-research problem (L06-026); ALD/ALE cycle time is gas-switch-gated.
- Product/mechanism: laminar-element differential-pressure MEMS sensing (µs-scale) + piezo valve + observer-based MPC; drop-in gas-panel format.
- Incumbents miss: MKS/Horiba/Brooks locked to thermal-sensor architectures (L07-050); nobody competes on a transient spec.
- Experiment: benchtop vs. commercial thermal MFC under SEMI E17; 5x settle improvement, no overshoot — $150k.
- Vision: gas layer for atomic-layer everything + fast reactive dosing. Substitutes: incumbent thermal MFCs (L07-050), plumbing workarounds.
- Uncertainty: 18–24 mo OEM qualification; pain inferred from standard + research, not a stated purchase criterion. Confidence: medium.

## A05 — Low-ripple four-quadrant plasma-control-coil converters for fusion (L01; sec L07, L03, L05)
- Buyer: fusion labs — ASIPP RMP/PF-converter tenders (L01-037/038); ITER procurement bands (L07-041); expansion: private fusion.
- Pain: precision coil supplies are one-off in-house builds/bespoke tenders per machine; no standard product line.
- Product/mechanism: ±1 kA/±1 kV four-quadrant SiC modules, <100 ppm ripple (interleaved phase cancellation per MMC-family topologies, L11-016/017), µs-deterministic control interface, energy recovery.
- Incumbents miss: too low-volume for ABB/Siemens; big-science buys as EPC engineering; AE (L01-040) targets chambers, not coils.
- Experiment: 200 kW module on inductive dummy load to written lab spec — $220k.
- Vision: actuator-power supplier for the private-fusion fleet. Substitutes: in-house builds, bespoke tender winners.
- Uncertainty: lumpy government cycles; CN tenders closed to US startup; fleet mostly future. Confidence: low.

## A06 — Merchant NEG-coating cell + service (second source to SAES) (L07; sec L01, L13)
- Buyer: accelerator/synchrotron programs (IHEP HEPS tenders w/ domestic-only rule, L07-045; ITER chain L07-041/042).
- Pain: distributed-pumping NEG coating has effectively one merchant vendor (SAES IntegraTorr, L07-037); single-point-of-supply risk; uncoated chambers need 250 °C/30 h bakeouts (L07-009).
- Product/mechanism: cylindrical-magnetron TiZrV coating system + coat-to-print service; wall-as-pump physics (L07-001), 180 °C activation.
- Incumbents miss: SAES won't compete with itself; pump OEMs see demand destruction; national programs want second sources.
- Experiment: coat 2 m × 60 mm bore pipe; sticking coefficient, pumping speed, 5 vent/reactivation cycles vs. benchmarks — $120k.
- Vision: bakeout-free getter-lined vacuum for quantum/XHV/gravitational-wave. Substitutes: SAES (L07-037), CERN-licensed self-coating, lumped pumps.
- Uncertainty: lumpy dozens-of-projects TAM; CERN licensing. Confidence: low.

## A07 — Rapid certified hydrogen-degas station for UHV chamber production (L07; sec L13)
- Buyer: UHV chamber fabricators (Lesker-class, L07-036) and accelerator programs (L07-045/041).
- Pain: 250 °C/30 h treatment cuts H2 outgassing >70,000x (L07-009) but is a rigid schedule/energy bottleneck; no certified low-outgassing supply option (Ti costly, L07-008).
- Product/mechanism: induction+radiant vacuum-fire furnace (400–950 °C) optimized for cycle time; ~L²/D(T) diffusion physics; built-in throughput-method outgassing certificate.
- Incumbents miss: furnace vendors don't speak UHV QA; the certificate is the product and nobody sells it.
- Experiment: induction-retrofit furnace, 316L T/t matrix, outgassing + cost model — $90k.
- Vision: "degassed steel as a spec'd commodity." Substitutes: DIY ovens, Ti chambers (L07-008), NEG route (L07-037).
- Uncertainty: WTP untested; demand inferred, no ledgered degas-service purchase. Confidence: low.

## A08 — Quiet-cryostat interface retrofit for dilution refrigerators (L07; sec L13)
- Buyer: superconducting-qubit programs and national-lab DR fleets (research-frontier evidence L07-014–017).
- Pain: pulse-tube vibration couples to qubit decoherence via triboelectric wiring (L07-017); isolation vs. thermal conductance is lab-built today (L07-014); cooling power lags scale-up needs (2 mW@100 mK frontier, L07-016; split-cryostat vibration L07-015).
- Product/mechanism: split mechanical low-pass coupling + annealed-Cu links + jacketed low-triboelectric looms, retrofit to Bluefors/Oxford-class fridges; mW-class still upgrades.
- Incumbents miss: fridge OEMs sell catalog base-temperature specs; every lab reinvents isolation in-house.
- Experiment: module on partner-lab DR; vibration PSD at MXC, added heat load, noise-band suppression — $170k.
- Vision: quiet-cryo backbone for racks of fridges, cryo-EM, optical clocks. Substitutes: lab builds (L07-014/015), OEM options.
- Uncertainty: ATLAS flags DR frontier caution; OEMs can integrate fixes; no ledgered retrofit PO. Confidence: low.

## A09 — Nuclear-qualified vacuum instrumentation & valve packages for fusion (L07; sec L01, L03)
- Buyer: ITER Org (VVPSS instruments/valves awards, €300k–2M each, L07-042/043; awardee precedent MAP Industrial, L07-044); helium supply band (L07-041); ASIPP pattern (L01-037/038).
- Pain: commercial gauges/valves carry no nuclear qualification dossier; every project re-qualifies one-off via EPC hours.
- Product/mechanism: rad-tolerant gauge heads with remoted electronics over MI cable; bellows-sealed all-metal actuators; the qualification dossier is the moat (gauge physics L07-002/003/004; leak methodology L07-032).
- Incumbents miss: INFICON/MKS (L07-053/050) won't maintain nuclear paperwork for a niche.
- Experiment: gamma + thermal + magnetic tolerance campaign on partitioned prototype; draft dossier — $130k.
- Vision: instrumentation supplier of record for private fusion + advanced fission. Substitutes: commercial hardware + per-project qualification.
- Uncertainty: Euro-centric slow tenders; small volumes until fusion construction wave. Confidence: medium.

## A10 — Dopant-tuned Johnsen-Rahbek AlN ESCs + refurb line for SiC/GaN and legacy fabs (L06; sec L01, L07)
- Buyer: China etch/depo OEMs localizing components (<12% RF-component localization, L06-054; AMEC L06-048; Hengyunchang precedent L06-042/043); SiC expansions (Wolfspeed context, L06-041).
- Pain: ESC ceramics remain an active unsolved materials problem (L06-004/005/006/007/014/015); 150/200 mm compound-semi has long leads and no refurb ecosystem.
- Product/mechanism: Y-doped AlN holds volume resistivity in the JR window across temperature (L06-014); dual-zone heaters; PEALD alumina recoat service (L01-108).
- Incumbents miss: NGK/TOTO/Kyocera chase 300 mm leading edge; compound-semi too fragmented for them.
- Experiment: toll-made 150 mm Y:AlN puck; resistivity vs. T, clamp/declamp, residual charge under plasma, uniformity — $250k.
- Vision: electrostatic handling for >500 °C processes, hybrid bonding, panel-level. Substitutes: incumbent/captive ESCs, refurbished OEM chucks.
- Uncertainty: ceramics yield/capex vs. $5M cap; export-control friction on CN channel; no ledgered merchant-ESC PO. Confidence: low.

## A11 — Validated lyophilizer PAT retrofit kit (comparative pressure + TDLAS endpoint) (L07)
- Buyer: sterile-injectable manufacturers with legacy lyophilizers (FDA/CDER-documented deficiency patterns 2015–2023, L07-021).
- Pain: freeze-drying vacuum/process-control deficiencies recur in FDA applications/inspections (L07-021); best-practice CPV (L07-020) exceeds legacy machine instrumentation.
- Product/mechanism: Pirani/capacitance-manometer divergence endpoint + TDLAS vapor mass-flux spool + Part-11 controller producing validation-aligned batch records.
- Incumbents miss: OEMs monetize new machines, not competitor-fleet retrofits; instrument vendors sell parts without dossiers.
- Experiment: instrument pilot lyo; endpoint accuracy vs. gravimetric across 3 formulations + draft validation package — $110k.
- Vision: closed-loop model-based aseptic drying / continuous lyo control layer. Substitutes: OEM upgrades, manual validation practice (L07-020).
- Uncertainty: GMP change-control slows sales; demand evidence is regulatory-findings-based, not a named retrofit buyer. Confidence: low.

## A12 — Modular IGBT active-front-end rectifier retrofit blocks for electrowinning (L11; sec L02)
- Buyer: copper/zinc EW-ER operators (vendor-market evidence L11-045; specialty refiners first). ATLAS names rectifier quality the real L11 niche.
- Pain: SCR installed base wastes up to 13–14% specific energy via ripple/PF (quantified in electrolyzer analogue, L11-019/020); EW current-efficiency research ongoing (L11-026/027); monolithic replacements get deferred for years.
- Product/mechanism: containerized 1 kA IGBT AFE modules paralleled to 30–50 kA, <2% ripple, PF>0.99, bank-by-bank phased retrofit (topologies L11-016/017).
- Incumbents miss: ABB/Dynapower sell 20-year monolithic replacements; mining is under-instrumented so the loss stays invisible.
- Experiment: partner tank-house pilot, IGBT bank vs. SCR bank, kWh/t + current efficiency + harmonics over 60–90 days — $150k.
- Vision: precision-DC layer for all industrial electrochemistry with measured-efficiency guarantees. Substitutes: Advint-class upgrades (L11-045), full replacement, do-nothing.
- Uncertainty: no ledgered named mining buyer; retrofit windows tied to rare shutdowns. Confidence: medium.

## A13 — Warranty-grade stack-side power conditioner + online EIS "stack guardian" (L11; sec L02)
- Buyer: electrolyzer OEMs (Plug L11-046, Nel L11-047, tk nucera L11-048), developers/financiers (DOE hubs L11-032, EU H2Bank L11-039, NEOM L11-052).
- Pain: warranties written before degradation attribution is settled (L11-001/003/004/031); ripple accelerates PEM degradation (L11-021); thyristor base wastes 13–14% (L11-019/020); OEM order books shrinking (L11-047/048) — bankability is the binding constraint.
- Product/mechanism: interleaved active ripple filter + anti-OCV polarization hold + per-string online EIS at full current + finance-grade degradation ledger.
- Incumbents miss: rectifier vendors stop at the DC bus; OEMs can't fund side businesses and financiers need an independent data party. Compliant with ATLAS "no stack plays" rule — this is the power/diagnostics wedge.
- Experiment: 100 kW conditioner on PEM short stack; 1,000 h A/B intermittent campaign quantifying degradation delta — $240k.
- Vision: independent performance-underwriting layer for electrochemical assets; actuarial data moat. Substitutes: MMC/hybrid new-build rectifiers (L11-016/017), OEM BoP (L11-040), offline testing.
- Uncertainty: Western deployment volume itself is shaky; OEM resistance to third-party stack-health data. Confidence: medium.

## A14 — Degradation-aware SOEC power-and-thermal management unit (PTMU) (L11)
- Buyer: SOEC ammonia/e-fuel projects — Japan CfD winners Resonac/Toyota Tsusho (L11-054, L11-037); NEOM-class ammonia (L11-052) as expansion.
- Pain: industrial SOEC needs ≤0.75%/kh degradation (L11-014); degradation-aware operation cuts LCOH 9.5–16% (L11-034) and mode choice matters (L11-015) — but exists only as papers, not product.
- Product/mechanism: precision DC supply w/ potentio-galvanostatic mode control + hotbox thermal balancing + degradation-model MPC enforcing ΔT/voltage limits while following renewables.
- Incumbents miss: SOEC vendors are ceramics companies; rectifier vendors don't model degradation; value lives in the coupling.
- Experiment: HIL rig (stack-emulating impedance + thermal model) hitting ≥9% LCOH-equivalent gain, then 300 h short-stack validation — $200k.
- Vision: control backbone for high-temp electrolysis/reversible SOFC. Substitutes: in-house BoP, PLC+rectifier packages.
- Uncertainty: tiny installed SOEC base; 2030 CfD timing; stack access for validation. Confidence: low.

## A15 — Regenerative SiC formation/grading power modules for gigafactories (L11; sec L02, L06)
- Buyer: cell makers via formation-line integrators (Andritz Schuler 1.5 GW line, Wuxi Lead — L11-043); UHPC-class users (L11-044). ATLAS names formation/cycling equipment a real L11 niche decoupled from H2.
- Pain: formation is the gigafactory energy/floor-space hog; incumbents (Chroma/Hioki, L11-043) sell accuracy, not energy recovery or density.
- Product/mechanism: 5 V/100 A bidirectional SiC channels on shared DC bus with channel-to-channel energy shuttling (>92% round trip), 2x rack density, nA-class UHPC metrology on sampled channels (L11-044 benchmark).
- Incumbents miss: decades-amortized architectures; energy-cost salience is new; redesign cannibalizes their module economics.
- Experiment: 8-channel prototype; >92% round-trip + calibration stability vs. reference cycler — $160k.
- Vision: formation as dispatchable grid asset + inline precision coulometry QC. Substitutes: Chroma/Hioki lines (L11-043), Avrion UHPC (L11-044), Chinese integrators.
- Uncertainty: Chinese price competition; cyclical capex; supplier churn in niche (NOVONIX rebrand note, L11-044). Confidence: medium.

## A16 — High-pressure hydrogen in-situ mechanical test cells ("standard-method-in-a-box") (L11; sec L07)
- Buyer: H2 hub participants/pipeline operators (HyVelocity/MachH2, up to $2.2B, L11-032), steel/OEM materials labs, TIC labs.
- Pain: H2-embrittlement testing lacks settled standards; 2025–26 literature is still building methodology (L11-028/029/030), so operators over-spec steel or stall conversion; every lab custom-builds autoclave rigs.
- Product/mechanism: 200–1,000 bar H2 autoclave with internal SSRT/fracture fixtures (kills seal-friction artifacts), controlled H2 partial pressure and strain rate (the comparability variables per L11-028), leak QA per NASA framework (L07-032).
- Incumbents miss: frame makers leave the environment to customers; custom shops don't productize method compliance + reproducibility data.
- Experiment: 300 bar cell; round-robin SSRT on X52/X70 vs. published data (L11-029) — $180k.
- Vision: materials-qualification infrastructure for H2 transport/storage/aviation + licensable data library. Substitutes: in-house rigs, national-lab services.
- Uncertainty: tens-of-labs instrument volume; standards timing; service labs may absorb demand. Confidence: medium.

## A17 — Fuel-free microwave-plasma PFC abatement with dry fluorine capture (L06; sec L01, L07)
- Buyer: fab facilities teams (Samsung Pyeongtaek-class facility capex, L07-046/047); subfab OEM channels Edwards (L06-033)/Ebara (L07-051). Demand bridge: Ebara's fossil-fuel-free ELF plasma abatement enters mass production 2026 (L07-051) — electrified abatement is validated, fab PFC abatement is NOT the open-air VOC enthusiasm zone.
- Pain: burn-wet abatement needs fuel gas + water and ships fluorine out as wet HF waste; new fabs don't want that infrastructure.
- Product/mechanism: 2.45 GHz atmospheric microwave torch dissociates CF4/NF3/SF6 (>95% DRE) without combustion (scale-up per L01-016; electron-energy control L01-105); dry Ca(OH)2 beds capture F as exchangeable CaF2 cartridges.
- Incumbents miss: Edwards/Ebara monetize fuel/water/consumables architectures; F-recovery cuts their service revenue.
- Experiment: bench torch on dilute CF4/NF3, FTIR DRE + kWh/Nm3 vs. burn-wet + CaF2 capture efficiency — $170k.
- Vision: fab fluorine-loop management under PFAS-era F-gas scrutiny; battery/solar fabs next. Substitutes: Ebara ELF (L07-051), Edwards burn-wet (L06-033), central scrubbers.
- Uncertainty: Ebara head start; long fab quals; unpriced fluorspar credit. Confidence: low.

## A18 — Robotic helium leak-qualification cell for gas-panel/weldment fabricators (L07; sec L06, L11)
- Buyer: Ichor ($947.7M, 76% two customers — audit pressure, L07-049); Edwards Genesee NY plant / US reshored capacity (L06-033).
- Pain: thousands of orbital-weld VCR joints are leak-tested by manual sniffing — operator-dependent, slow, no quantified uncertainty; rigorous accumulation methods exist (NASA framework, L07-032) but aren't productized for factory throughput.
- Product/mechanism: robotic clamshell accumulation fixtures + He mass-spec + per-joint uncertainty budgets and barcode-traceable certificates; 10x operator productivity.
- Incumbents miss: INFICON/Pfeiffer sell detectors, not fixtured automation (L07-053/039); integrators build one-offs without uncertainty math.
- Experiment: single-cell prototype on 500 production joints; cycle time, MDL, uncertainty vs. skilled operator — $95k.
- Vision: automated hermeticity infrastructure (semicon, H2 joints per L11-028, cryo, quantum) + fleet leak-data analytics. Substitutes: manual benches (L07-053), integrator one-offs, batch chamber testing.
- Uncertainty: cyclical fabricator capex (Ichor restructuring, L07-049); clonable by integrators — moat must be certification software + data. Confidence: medium.
