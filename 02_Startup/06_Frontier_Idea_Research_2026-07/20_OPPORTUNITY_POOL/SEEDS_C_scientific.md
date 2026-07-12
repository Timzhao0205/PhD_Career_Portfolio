# SEEDS — Batch C (Scientific & Photonic Systems), lanes L05 / L12 / L13

Idea-architect: claude-fable-5 / xhigh. Date: 2026-07-12. 16 seeds (12 minimum; surplus intended
for orchestrator culling). All demand/technical/competitor claims cite accepted ledger IDs from
`10_SOURCE_ATLAS/L05|L12|L13_verified_sources.json`. Founder profile was NOT read before these
seeds were frozen; founder_fit_note sentences were appended afterward in the JSON only.

## C01 — Traceable FLASH/UHDR beam-dose metrology instrument (L05)
- Product: charge-buildup-compensated BCT head + GS/s digitizer + Faraday-cup-traceable calibration, sold as a per-pulse SI-traceable beam-dose meter with self-test injection.
- Buyer: e-beam sterilization operators and FLASH-RT developers (IBA/SteriLab L05-028; CGN Dasheng customers L05-035; clinical physics groups L05-023/024).
- Pain/demand: BCTs demonstrably mis-read at UHDR (L05-023, L05-024) just as ISO 11137-1:2025 (L05-042) tightens sterilization validation amid EtO-replacement capacity build-out (L05-028).
- Mechanism: guard-ring shielded toroid + drift-corrected gated integration + inter-pulse reference-current self-calibration; traceable to primary electrical standards.
- Incumbents miss: Bergoz sells storage-ring catalog components (L05-049), metrology institutes publish but don't productize.
- Experiment ($140k): benchmark vs Faraday cup on rented linac, 1–10^6 Gy/s; pass = <2% charge error where stock BCT fails. Vision: the legal meter of every therapeutic/industrial beam.
- Substitutes: catalog BCTs, radiochromic film, one-off lab rigs. Uncertainty: FLASH-RT commercialization timing; niche TAM until dose-audit expansion.

## C02 — Merchant solid-state accelerator powertrain for industrial e-beam (L05)
- Product: qualified SiC/IGBT Marx cell library configured as 100–300 kV modulators, gun pulsers, and column supplies with published IEC 60060-1:2025 acceptance protocol and ISO 11137-grade documentation.
- Buyer: new e-beam machine builders/contract sterilizers stuck behind the IBA/L3 backlog (L05-028), CGN Dasheng-class OEMs (L05-035), isotope-program integrators (L05-036).
- Pain/demand: duopoly backlogged into 2026–27 on EtO replacement (L05-028); every builder reinvents its powertrain with bespoke acceptance tests (L05-043 gap).
- Mechanism: modular Marx per L05-001/003/004/006 with per-cell gate-timing flat-top correction; one BOM covers pulsed-to-DC.
- Incumbents miss: turnkey vendors won't arm competitors; ScandiNova/Jema (L05-047, L05-030) do one-off science tenders, not industrial product lines.
- Experiment ($180k): 12-cell 120 kV/100 A/20 us stack, ±0.5% flat-top, 500 Hz, fault survival + OEM LOI. Vision: "Advanced Energy of accelerators."
- Uncertainty: backlog claim trade-press-sourced; count of credible new OEM customers unproven.

## C03 — Pulse-agile multi-energy modulator retrofit for cargo-screening linacs (L05)
- Product: drop-in Marx modulator with shot-to-shot stage-count/charge-voltage command: 4/6/9 MeV arbitrary interleave at 400+ Hz, no thyratron consumable.
- Buyer: cargo-screening integrators and customs agencies in a documented upgrade cycle (Varex industrial +25% YoY, >$55M cargo orders, L05-033); CGN NDT builders (L05-035).
- Mechanism: Marx stage modulation + magnetic pulse compression (L05-002, L05-005, L05-015) recovers thyratron-class rise; energy change becomes purely electronic.
- Incumbents miss: Varex monetizes tubes/detectors, modulators are a cost center (L05-033); science modulator vendors ignore the fragmented ports-retrofit fleet (L05-047, L05-050).
- Experiment ($200k): 3-level pulse-agile bench demo into magnetron-equivalent load, <1% settling; then integrator beam test. Vision: software-defined inspection beams at every port.
- Substitutes: OEM PFN/thyratron, ScandiNova K-series, in-house Varex/CPI electronics. Uncertainty: integrator channel access; Varex insourcing.

## C04 — Klystron/gyrotron coupler & window health monitor (L05, sec L13)
- Product: waveguide sensor pod (arc photodiodes + ns reflectometer + acoustic emission) with FPGA precursor classification, <1 us RF-kill, TDR degradation localization.
- Buyer: tube-fleet operators — F4E/ITER 24 gyrotrons (L05-029), PAL ~70 klystrons (L05-037), ESS gallery (L05-030); funding path via DOE ARDAP (L05-031).
- Pain: couplers/windows named the most common VED failure at high CW power, fixes still open research (L05-014); operators absorb unplanned downtime with no cross-vendor diagnostic.
- Incumbents miss: tube OEMs won't instrument warranty failure modes across competitors' tubes (L05-050); labs build one-offs.
- Experiment ($90k): instrument one operating klystron 3 months; capture/classify precursors, beat existing crowbar chain. Vision: predictive-uptime ARR across CPI-scale installed tube base.
- Uncertainty: modest unit count forces service-ARR model; failure-data access needs operator partnerships.

## C05 — Catalog PSM HV supply with <10 J arc energy for gyrotrons/fusion RF (L05, sec L13)
- Product: series-stacked ~1 kV PSM modules synthesizing −55 kV/100 A-class with kHz agility; crowbar-less <10 J arc-energy guarantee (wire-survival tested); published acceptance protocol.
- Buyer: F4E/ITER EC heating (EUR 20M Thales contract for 6 of 24 gyrotrons, L05-029; live tenders L13-030), ESS-class RF galleries (L05-030); DOE flags <50% wall-plug RF chains (L05-039).
- Mechanism: digital voltage synthesis from many isolated modules, module-bypass redundancy, small stored energy per cell bounds arc energy without triggered crowbar (L05-015, L05-002, L05-007).
- Incumbents miss: incumbents profit from engineered-to-order tenders; no catalog SKU with published tests exists (lane pains #4/#5).
- Experiment ($220k): 24-module 24 kV/20 A string, 1 kHz modulation, 25 um wire arc-survival pass. Vision: the merchant "RF wall socket" for commercial fusion heating fleets.
- Uncertainty: lumpy tenders, long quals, strong EU incumbency (EU beachhead; both region flags false).

## C06 — Ruggedized adaptive-optics beam-control LRU for 100 kW-class DE (L12)
- Product: sealed MIL-rated LRU: cooled deformable mirror w/ high-LIDT coating + wavefront sensor + deterministic kHz modal controller + health telemetry.
- Buyer: JLWS primes nLIGHT Defense / LM Aculight ($86M initial, $847M ceiling, L12-031/032), DRDO Surya (L12-043), DARPA POWER teams (L12-047); GAO transition gap (L12-045).
- Pain: no ruggedized merchant middle tier between boutique lab AO (L12-011) and commodity components (lane pain #8).
- Mechanism: astronomy-derived real-time wavefront stabilization (L12-009/010/011) with LIDT-informed optics (L12-019/020), packaged as field-swappable unit.
- Experiment ($230k): closed loop at 2–5 kW CW, >2x Strehl at 1 kHz, 30-min survival, shake-table pass. Vision: fire-control layer of the DE and power-beaming era.
- Uncertainty: prime insourcing at rate production; ITAR; DM survivability at sustained 100 kW flux.

## C07 — Merchant coherent-beam-combining phase-control engine (L12)
- Product: rack-unit LOCSET-class frequency-tagged phase controller: single-photodiode demux, >10 kHz loops on LiNbO3 modulators, piston/tip-tilt hierarchy, group-delay servo for ultrafast arrays.
- Buyer: nLIGHT (L12-033), LM Aculight (L12-031), DARPA MELT/AMPED tile awardees (L12-040/041).
- Pain: TMI caps single-fiber power (L12-016/017/018) so 300–500 kW systems must combine; every OEM re-develops phase control in-house (L12-001/002 still research).
- Incumbents miss: combining is guarded OEM IP, so no merchant offer exists — exactly what tile programs and second-tier integrators need.
- Experiment ($250k): 8-channel, ~500 W, >90% combining efficiency, <lambda/30 RMS residual, <1 s cold-start lock. Vision: the standard combining engine to MW-class arrays and fusion drivers.
- Uncertainty: 100+-channel efficiency unproven publicly; OEM IP posture; defense-only concentration.

## C08 — CPO external-laser-source thermal stabilization module (L12, sec L14)
- Product: micro-channel cold plate + per-bank TEC zones + traffic-feedforward controller holding laser junctions ±0.1 K under 5–25 W/cm2 transients; one qualified interface for 16/32-laser ELS shelves.
- Buyer: Coherent ($4B DCI target, L12-035/036) and Broadcom-class CPO system vendors (L12-022/023).
- Pain: four independent 2024–26 peer-reviewed thermal approaches, no dominant design (L12-021–024); wavelength stability is the gating ELS reliability item.
- Incumbents miss: cooling vendors don't do wavelength-grade control; photonics vendors don't do coolant loops; the interface is contractually orphaned.
- Experiment ($120k): surrogate-load testbed reproducing published CPO power maps; ±0.1 K under 10x transients, <5% overhead. Vision: thermal backbone of optical compute interconnect.
- Uncertainty: CPO ramp timing/architecture; absorption by Coherent/Broadcom; post-Novec coolant plan (ATLAS caution).

## C09 — GaN ps-precision high-current laser-diode driver family (L12, sec L05)
- Product: qualified driver modules: GaN-HEMT stage, <100 pH loop, per-pulse charge metering, DLL timing core <10 ps edge placement; CW pump control to 300 ps seed pulsing on one BOM.
- Buyer: nLIGHT (L12-033), TRUMPF (L12-039), MELT tile integrators (L12-041), IPG-class OEMs (L12-034).
- Pain: precision pulsed diode drive is still a research frontier (L12-025/026/027) — every OEM carries driver R&D risk (lane pain #6).
- Incumbents miss: big OEMs never sell their in-house drivers (L12-051); IC vendors chase low-current lidar volume; the high-current/ps corner is unserved.
- Experiment ($95k): 100 A/2 ns and 20 A/300 ps into real diodes, <15 ps RMS jitter, eval-kit replicated by two OEM labs. Vision: "the driver MCU of photonics."
- Uncertainty: fragmented sockets, modest ASPs, 1–2 yr design-in cycles.

## C10 — In-situ optics damage inspection & lifetime tracking for MJ-class facilities (L12)
- Product: dark-field oblique-illumination scanning head + registered site maps + per-site damage-growth-law fitting against shot fluence records.
- Buyer: NNSA/LLNL EYC (NIF 2.2→2.6 MJ, CD-1, $26M FY2026, L12-042); NNSA fusion recapitalization (L12-046); JLWS-era DE integrators (L12-031).
- Pain: higher fluence accelerates damage initiation/growth; the inspection capability is locked inside LLNL; new IFE/DE entrants can't replicate it.
- Mechanism: Mie-scatter dark-field detection of micron sites on meter-class apertures; LIDT-model-informed thresholds (L12-019/020); wavefront-era registration (L12-011).
- Experiment ($110k): track seeded 5–50 um sites on 30 cm optics over 100 cycles; >95% detection at 10 um blind vs microscopy. Vision: the maintenance ledger of every high-fluence optic.
- Uncertainty: few near-term facility buyers; LLNL tech-transfer competition; DE needs small-aperture variant.

## C11 — Active-safety interlock module for handheld laser welders (L12)
- Product: inline module: contact-gated emission, <10 us back-reflection kill via driver enable, IMU free-swing detection, tamper-evident compliance log.
- Buyer: handheld-welder OEMs + Western importers/insurers (Raycus handheld exports +66% in 2025, L12-038; Han's-class OEMs L12-037).
- Pain: product class exploding under a 2007-dated safety standard (ISO 11553-2, L12-050) — undocumented residual Class-4 risk (lane pain #7).
- Incumbents miss: price-war OEMs won't add cost in a regulatory vacuum; standards bodies move on decade timescales; first mover defines the compliance kit.
- Experiment ($60k): retrofit two 1.5 kW welders; fault-injection campaign, <10 us kill, zero false-kill over 40 h production. Vision: the GFCI of handheld lasers.
- Uncertainty: NO dated regulatory trigger yet (anticipatory — flagged per ATLAS trigger-honesty); clone risk. Confidence: low.

## C12 — WILDCARD: 2-um high-pulse-energy drive-laser module for next-gen EUV R&D (L12)
- Product: Tm-fiber-pumped Ho:YLF/YAG module, 50–100 mJ ns-class at multi-kHz, <1% RMS stability, head+driver packaging.
- Buyer (bridge): Gigaphoton R&D (L12-053), ASML/Cymer supply chain facing architecture-change risk (1,000 W CO2 milestone treadmill, L12-034), national labs (L12-042).
- Evidence: peer-reviewed 5% EUV conversion efficiency from 2-um-driven tin droplets (L12-003) + tin-plasma physics base (L12-006/007/008).
- Incumbents miss: sunk CO2 fleet at Cymer; Gigaphoton follows ASML; no merchant 2-um high-energy module exists. Explicit enthusiasm-zone wildcard per ATLAS Section 6.
- Experiment ($250k): 50 mJ/1 kHz single-stage amp, M2<1.3; loaner head to one national-lab EUV group. Vision: become the Cymer-supplier of the next EUV architecture; interim 2-um processing revenue.
- Uncertainty: single-buyer-chain risk; industrial rep-rate CE/debris unproven; >5 yr timeline. Confidence: low.

## C13 — 4 K FDM readout front-end module (cryo LNA + mux + cal) (L13)
- Product: 4 K module: qualified cryo LNA + frequency-division mux banks (~1 mW/qubit class) + calibration tone injector; one coax carries 8–16 channels to RT RFSoC digitizers.
- Buyer: DOE QIS centers ($625M explicitly includes scaling-chip components, L13-028); qubit builders at the 256→4,096 channel wall (L13-042); Taiwan ITRI/SEEQC manufacturing-line ecosystem (L13-039).
- Pain: cryo I/O density and cooling-power budgets are the acknowledged scaling bottlenecks (L13-042; L13-013/021/023) yet labs build competing point solutions instead of buying products.
- Mechanism: microwave FDM per SQUID/TES playbook (L13-008) + 28nm 1.08 mW/qubit readout ASIC result (L13-023) + few-K-noise cryo LNAs (L13-021, L13-013).
- Incumbents miss: RT-control vendors monetize per-channel racks; cryo-ASIC know-how trapped in academia; fridge vendors sell cooling not electronics.
- Experiment ($190k): 8-channel FDM at 4 K, <1.5 dB SNR penalty, <5 mW heat load, co-run with a QIS-center testbed. Vision: merchant cryo front-end of the 100k-channel era.
- Uncertainty: vendor verticalization; modality-dependent mux choice; opaque government pricing.

## C14 — Supported White Rabbit timing appliance with conformance suite (L13, sec L05)
- Product: WR node/switch with IEEE 1588-2019 HA profile, DDMTD phase detection, OCXO/Rb holdover, asymmetry self-cal, fleet telemetry, LTS contracts, published tender-citable acceptance suite.
- Buyer: ITER-class procurement (L13-030), JT-60SA-class projects (L13-033), RRCAT-class accelerator ops (L13-051), WR-adopter facilities (L13-027).
- Pain: WR is technically mature but its commercial ecosystem only formalized in 2024 — facilities cannot buy decades-long support or conformance guarantees (lane pain #10).
- Incumbents miss: telecom timing giants ignore the sub-ns niche; CERN-spinoff boutiques don't productize support; "support as a product" is unclaimed.
- Experiment ($70k): two nodes over 25 km deployed fiber, <200 ps accuracy for 30 days incl. thermal cycling; conformance suite cited in one tender. Vision: sub-ns time as a utility (quantum networks, fusion plants, arrays).
- Uncertainty: small pure-science TAM; open-hardware community dynamics; incumbent entry.

## C15 — Two-personality direct-RF control instrument: accelerator LLRF + qubit control (L13, sec L05)
- Product: RFSoC-based instrument with qualified LLRF (sub-sampling IQ, L13-002) and qubit (QICK/QubiC-class, L13-001/025) personalities, WR-disciplined multi-crate coherence, published acceptance tests.
- Buyer: DOE QIS centers (L13-028), Taiwan ITRI/SEEQC manufacturing-line ecosystem (L13-039), Japan AIST-class programs, and mid-tier accelerator facilities; Keysight/AIST delivery proves top-end demand (L13-037).
- Pain: same silicon (L13-045), divergent one-off gateware everywhere; DOE had to broker Fermilab–Qblox just to make QICK supportable (L13-032); flagship pricing opaque ($1–3M estimates, L13-046).
- Incumbents miss: Keysight targets flagships; QM/Qblox/QuEL are qubit-only; LLRF is too small for them but adjacent for a two-personality platform (cross-lane standardization echo: L05-009).
- Experiment ($160k): one platform passing qubit benchmarks AND <0.1%/0.1 deg cavity regulation; two paid pilots. Vision: the oscilloscope of coherent control.
- Uncertainty: competing with free + giants; Qblox CRADA may occupy the ground.

## C16 — Cryogenic interconnect qualification station (L13)
- Product: 4 K cryostat insert: 64+-channel microwave switch matrix + TRL cal standards at temperature; S-parameters, crosstalk to −80 dB, thermal conductance, microphonics — hundreds of paths per cooldown; standardized "cryo datasheet" output.
- Buyer: Bluefors (L13-041), Delft Circuits-class cable vendors (L13-042), SEEQC–ITRI line (L13-038), DOE QIS hardware teams (L13-028).
- Pain: 16x I/O scale-up rests on vendor self-claims; every player burns cryostat time on ad hoc qualification; no third-party instrument or standard exists.
- Incumbents miss: fridge/cable vendors can't be neutral metrology authorities; T&M giants ignore the 4 K niche; the market is forming faster than any standard.
- Experiment ($180k): 16-channel insert in a borrowed DR; TRL-calibrated results consistent with models; 64-path single-cooldown qualification; two vendor pilots. Vision: the qualification authority underwriting the 100k-qubit supply chain.
- Uncertainty: dozens of buyers near-term; absorbable as a fridge accessory; standard-setting needs ecosystem buy-in.
