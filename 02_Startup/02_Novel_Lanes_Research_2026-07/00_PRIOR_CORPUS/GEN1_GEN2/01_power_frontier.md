# Worker Output 01 — Power / Energy / Grid / AI Data-Center Infrastructure Frontier

**Worker prefix:** PWR
**Domain:** Power / energy / grid / AI data-center infrastructure
**Date:** 2026-06-28
**Scope discipline:** Engine-layer subsystems and platforms that make a new high-end power system possible. Not dashboards, not monitoring-only, not commodity procurement.

---

## 1. Domain Thesis

**The electrical layer between the medium-voltage grid and the chip is being rebuilt for the first time in a century, and the company that owns the "power core" of the AI factory owns the chokepoint.**

Three forces converge:

1. **The AI factory broke the legacy power chain.** Racks are moving from ~50–130 kW to **1 MW and beyond**, and the industry has converged on **800 VDC** distribution because 54 VDC at 1 MW requires ~200 kg of copper busbar per rack and ~200,000 kg per gigawatt campus (NVIDIA/Schneider, company claims; triangulated by IEEE Spectrum). The legacy chain — MV transformer → 480 VAC → double-conversion UPS → PSU rectifiers — has five conversion stages and 12–15% loss. The boundary shift is from *facility AC + many conversion stages* to **a single solid-state MV-to-800VDC power core** with microsecond protection, integrated transient buffering, and grid-forming behavior. This is the "engine layer."

2. **Gigawatt loads are now an unplanned grid actor.** Synchronized GPU training produces second-to-millisecond power steps; **PNNL/DOE/NERC have documented sustained grid oscillations originating from data centers** (e.g., measured oscillation modes; NASPI "Measurement Adequacy" report). Diesel and gas turbines cannot react at millisecond timescales. The fix is not software dashboards — it is **fast power-electronic buffering, grid-forming hardware, and active damping that change control, not just observe it.** The IEA projects data-center electricity roughly doubling to ~945 TWh by 2030, with the US and China driving ~80% of growth; FERC's December 2025 PJM order shows interconnection itself is now the binding constraint (median ~5-year queue).

3. **At gigawatt campus scale, extreme-systems physics becomes economic.** Superconducting MVDC busways, cryogenic power electronics, superconducting fault-current limiters, and high-frequency medium-voltage magnetics move from lab curiosities to cost-justified subsystems when a single campus draws 1–5 GW and copper/loss/footprint dominate. Peer-reviewed work (Applied Energy, Energy, Superconductor Science and Technology) now shows superconducting delivery cutting transmission loss to ~1.7% of conventional AC for representative cases.

**Where the defensible engines are:** (a) the MV-to-800VDC solid-state power core and its sub-engines — medium-frequency magnetics, MV gate-drive/stack control, microsecond DC breakers, high-temp DC-link/buffer modules; (b) the grid-edge buffer/grid-forming hardware that hides AI load volatility; (c) the extreme-environment frontier (superconducting/cryogenic) that becomes the only way to densify a GW campus. China runs this race in parallel with a state-backed MV-DC standard push (Delta/Alibaba "Panama" + a domestic 800 VDC white paper), which creates both a China-first lane and an export-risk lane.

Bet on the **engine**, not the dashboard.

---

## 2. Candidate Ideas (PWR)

> Capex bands: **Low** = <$5M to credible prototype; **Med** = $5–25M; **High** = $25–100M; **Very High** = >$100M (pilot line / field demo).

### PWR-01 — AI-Factory MV-to-800VDC Solid-State Power Core ("Power Cube")
- **One-sentence product:** A single-/two-stage solid-state power core that converts medium-voltage AC (4.16–13.8 kV) directly to regulated 800 VDC at 1–5 MW per skid, replacing the transformer + double-conversion UPS + rectifier chain.
- **System boundary shift:** Collapses 5 conversion stages into 1–2 inside one footprint; the data hall sees clean 800 VDC from the MV grid with grid-forming behavior built in.
- **Extreme metric:** Target >98.5% end-to-end efficiency at 2–5 MW with ~3–5× power density vs. legacy MV-transformer + UPS room; sub-millisecond MV ride-through.
- **First high-end customer:** Hyperscaler / neocloud building 800 VDC racks (NVIDIA Kyber / Vera Rubin-class halls).
- **Buyer title:** VP/Head of Data Center Energy & Power Engineering (or Director, Critical Facilities).
- **Pain:** Legacy AC chain wastes 12–15% of incoming power, consumes enormous copper, and cannot deliver 1 MW racks; power-room footprint and interconnect timeline cap how much compute fits per megawatt.
- **Current workaround:** Stack discrete MV transformer + line-frequency UPS + 54V/415V rectifiers; bolt on sidecars for 800 VDC.
- **Why current solution fails:** Multiple isolated conversion stages compound loss and footprint, lack fast fault control, and cannot natively buffer GPU transients or present grid-forming impedance.
- **Hardware stack:** SiC MV half-bridge stacks, medium-frequency transformer (10–20 kHz), 800 VDC output stage, integrated DC bus, liquid cooling, solid-state input/output protection.
- **Software/control stack:** Real-time modular multilevel control, active impedance/grid-forming controller, transient feed-forward from rack telemetry, digital-twin health/derating.
- **Prototype path 2026–2028:** 2026 250 kW–1 MW single-skid lab demo into 800 VDC load bank; 2027 2 MW field pilot at a colo/neocloud hall; 2028 5 MW multi-skid line for a GW campus.
- **China wedge:** Aligns with the domestic 800 VDC / "Panama-class" MV-DC standard push; SiC and magnetics supply chain domesticating fast.
- **US wedge:** Hyperscaler 800 VDC roadmaps (NVIDIA ecosystem ~2027) and interconnect pressure favor footprint/loss reduction; pairs with behind-the-meter generation.
- **Cleanroom dependency:** None in-house; buy SiC die/modules from foundries, wind magnetics in-house, assemble at power-electronics MLO. Outsourcing path clear.
- **Capex band:** High.
- **Regulatory/export risk:** SiC/WBG and grid-control IP face US–China export friction; UL/IEC MV-DC standards still maturing.
- **Competitors:** Delta (Panama), Schneider, ABB, Eaton, Vertiv, Navitas/EPFL (250 kW SST), Hitachi Energy.
- **Defensibility:** Magnetics + MV control co-design, thermal integration, and field-reliability data; standards seat; hard-to-copy control firmware.
- **Kill criteria:** If hyperscalers standardize on incumbent MV-UPS + separate 800V rectifier and refuse single-core integration, or if efficiency/footprint gains <10% in field.
- **Evidence status:** CLEARED_WITH_WEAKNESS (load/efficiency pain from IEA + peer-reviewed SST; 800 VDC architecture is largely company claim, triangulated).
- **Key sources:** IEA Energy & AI; IEEE Industrial Electronics Magazine SST review (Huang); Navitas/EPFL APEC 2026 demo; NVIDIA/Schneider 800 VDC (company).

### PWR-02 — Microsecond 800VDC Solid-State Breaker / e-Fuse
- **One-sentence product:** A bidirectional SiC/GaN solid-state DC breaker and high-density e-fuse module rated for 800–1000 VDC busways that interrupts faults in microseconds with coordinated selectivity.
- **System boundary shift:** Moves protection from millisecond mechanical/AC-side breakers to **microsecond semiconductor interruption** native to a DC busway, enabling safe high-power DC distribution.
- **Extreme metric:** <1–10 µs interruption at 800–1000 VDC, multi-kA fault clearing, with low on-state loss (<0.5%) and selective coordination across nested zones.
- **First high-end customer:** 800 VDC power-shelf/busway OEM and hyperscaler critical-facilities team.
- **Buyer title:** Director of Power Distribution Engineering / Electrical Safety.
- **Pain:** 800 VDC has no natural current zero; an unprotected fault can arc-flash and destroy a busbar before an AC breaker reacts; worker safety and equipment risk block deployment.
- **Current workaround:** Hybrid mechanical breakers, fuses, or AC-side protection — too slow for DC arc energy.
- **Why current solution fails:** Silicon IGBTs cannot interrupt fast enough at this voltage; mechanical breakers and fuses lack selectivity and reset speed.
- **Hardware stack:** SiC JFET/MOSFET or GaN bidirectional switch array, TVS/MOV/active-clamp energy-absorption, current/temperature sensing, gate drive.
- **Software/control stack:** Fault-detection logic (di/dt + threshold), adaptive trip curves, selective coordination protocol, soft-start/soft-turn-off.
- **Prototype path 2026–2028:** 2026 800 VDC/2 kA single-module bench demo; 2027 zone-selective busway demo; 2028 UL/IEC-qualified product into a pilot hall.
- **China wedge:** Domestic SiC JFET/MOSFET supply + AIDC DC standardization create early-adopter pull.
- **US wedge:** 800 VDC safety/standards gap is an explicit deployment blocker; ABB SACE Infinitus shows incumbents validating the category.
- **Cleanroom dependency:** None; die sourced from WBG foundries, module assembly only.
- **Capex band:** Med.
- **Regulatory/export risk:** SiC export controls; UL 489-DC / IEC arc-energy standards still settling.
- **Competitors:** ABB (SACE Infinitus), Infineon, Eaton, Littelfuse, Atom Power.
- **Defensibility:** Energy-absorption + selectivity firmware, thermal packaging, qualification data; standards participation.
- **Kill criteria:** If hyperscalers accept ±400 VDC with conventional protection and 800 VDC DC-side breakers stay a niche, or if on-state loss can't beat 0.5%.
- **Evidence status:** CLEARED (peer-reviewed SiC SSCB results + authoritative protection literature).
- **Key sources:** IEEE APEC self-powered ultra-fast SiC JFET SSCB; IEEE journal SiC SSCB (motor control center); Power Electronics News DC-protection analyses (timing).

### PWR-03 — Rack Transient Buffer / "Power-Smoothing" Energy Interface
- **One-sentence product:** A rack/shelf-level hybrid energy buffer (supercapacitor + film capacitor + fast DC-DC) that absorbs GPU load steps in microseconds-to-seconds so neither the upstream converter nor the grid sees the spike.
- **System boundary shift:** Inserts an **active power-shaping layer between the GPU and the bus**, decoupling compute dynamics from power-delivery dynamics.
- **Extreme metric:** Absorb/inject ≥400 J per GPU (≈28.8 kJ per 72-GPU rack) in microseconds; cut peak current draw ~25%; smooth multi-MW second-scale steps.
- **First high-end customer:** GPU rack / power-shelf OEM (ODM building 800 VDC racks).
- **Buyer title:** Chief Engineer, Rack Power Architecture.
- **Pain:** GPU training causes spiky, synchronized load that stresses PSUs, trips protection, and propagates to the grid as oscillation; utilization is throttled to stay within power envelopes.
- **Current workaround:** Oversized PSUs, firmware power-capping/ramp limits, and software smoothing that sacrifices performance.
- **Why current solution fails:** Software-only smoothing wastes compute; passive caps alone can't store seconds of energy; battery BBUs are too slow for microsecond steps.
- **Hardware stack:** Hybrid supercapacitor bank, high-temp film caps, bidirectional SiC/GaN DC-DC, local bus sensing.
- **Software/control stack:** Predictive feed-forward from GPU power telemetry, droop/virtual-impedance control, state-of-charge management, coordination with upstream UPS.
- **Prototype path 2026–2028:** 2026 single-shelf buffer demo on a synthetic GPU step profile; 2027 full-rack integration with an ODM; 2028 multi-rack hall pilot with grid-side smoothing verification.
- **China wedge:** Domestic supercap (e.g., established cell makers) + AIDC scale; pairs with Panama-class cores.
- **US wedge:** NVIDIA's "Intelligent Power Smoothing" spec institutionalizes the requirement; first-mover on the standardized buffer.
- **Cleanroom dependency:** None; cells/caps procured, module assembly only.
- **Capex band:** Med.
- **Regulatory/export risk:** Low–moderate (energy-storage transport/UL).
- **Competitors:** Capacitech, Panasonic (supercaps), KEMET/TDK, NVIDIA-partner power teams, Vertiv.
- **Defensibility:** Predictive control co-designed with GPU telemetry, thermal/lifetime engineering, OEM design-win lock-in.
- **Kill criteria:** If GPU vendors fully solve smoothing in firmware + on-package caps, eliminating the shelf-level buffer market.
- **Evidence status:** CLEARED (peer-reviewed storage review + DC-link reliability + documented grid-oscillation pain).
- **Key sources:** Wang & Blaabjerg IEEE TIA DC-link reliability; PNNL/DOE/NERC oscillation reports; IEEE Spectrum AI-UPS (timing).

### PWR-04 — Campus Power-Shaping Buffer (Grid-Hiding Hybrid Storage + Grid-Forming Converter)
- **One-sentence product:** A megawatt-scale fast hybrid-storage + grid-forming converter system that sits between an AI campus and the grid and turns the campus's spiky load into a smooth, grid-friendly profile.
- **System boundary shift:** Makes a volatile gigawatt load look like a **constant, dispatchable, grid-forming resource** to the utility — load-shaping as a hardware service.
- **Extreme metric:** Suppress second-to-minute load swings of ±100s of MW; deliver grid-forming inertia/damping at GW campus scale; ramp-rate limiting to utility-set bounds.
- **First high-end customer:** AI data-center developer / utility serving a co-located large load.
- **Buyer title:** Head of Power Procurement & Grid Interconnection (developer) or Director of Transmission Planning (utility).
- **Pain:** Utilities are throttling or delaying interconnection because volatile AI loads threaten frequency/voltage stability and cause measurable oscillations; developers face multi-year queues.
- **Current workaround:** Curtail load, overbuild firm generation, or accept long interconnect timelines; passive ride-through only.
- **Why current solution fails:** Diesel/gas can't follow millisecond-second dynamics; pure-software ramp limits waste compute; standard grid-following BESS doesn't provide grid-forming stabilization.
- **Hardware stack:** MW SiC grid-forming converter, hybrid storage (Li-ion + supercap/flywheel), MV interface, fast switching.
- **Software/control stack:** Grid-forming/virtual-synchronous-machine control, active oscillation damping, ramp-rate governor, utility-facing dispatch API.
- **Prototype path 2026–2028:** 2026 1 MW grid-forming + storage testbed against recorded AI load traces; 2027 10–50 MW pilot at a developer site; 2028 utility-accepted "smooth-load" interconnection product.
- **China wedge:** State grid coordination + west-cluster (东数西算) renewable surplus makes load-shaping strategically aligned.
- **US wedge:** FERC's 2025 PJM co-location/large-load order and DOE/PNNL oscillation findings create explicit regulatory pull for grid-forming load shaping.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Interconnection rules in flux (opportunity + uncertainty); grid-control IP export-sensitive.
- **Competitors:** Tesla Megapack + Autobidder, Fluence, Hitachi Energy (grid-forming), Emerald AI (software), gas/turbine integrators.
- **Defensibility:** Grid-forming control validated against real AI load dynamics + utility certification; pairs with PWR-01/03.
- **Kill criteria:** If FERC/ISOs accept software ramp-limits + firm gas as sufficient and refuse to value grid-forming buffering.
- **Evidence status:** CLEARED (FERC order + DOE/PNNL/NERC oscillation evidence + DOE grid-forming spec).
- **Key sources:** FERC Dec-2025 PJM order; PNNL NASPI oscillation report; DOE OE oscillation article; DOE GFM IBR spec v1; IEA.

### PWR-05 — Behind-the-Meter Grid-Forming Microgrid Controller + Hardware for Islanded AI Campuses
- **One-sentence product:** A grid-forming control hardware + protection platform that lets behind-the-meter gas/SOFC generation + storage island an AI campus and run stably without the utility.
- **System boundary shift:** Turns a data center from a grid-dependent load into a **self-forming microgrid** that can run islanded or grid-parallel, bypassing the interconnect queue.
- **Extreme metric:** Black-start and stabilize a 100–500 MW islanded campus with sub-cycle fault response and seamless grid re-sync.
- **First high-end customer:** Behind-the-meter power developer / neocloud building ahead of grid availability.
- **Buyer title:** VP of Energy / Microgrid Engineering Lead.
- **Pain:** Grid interconnection takes ~5 years; generation must be coordinated, protected, and islanded reliably or the whole campus trips.
- **Current workaround:** Ad-hoc genset paralleling switchgear + utility-style relays not designed for inverter-dominant fast loads.
- **Why current solution fails:** Legacy synchronous-genset controls and grid-following inverters can't stabilize a low-inertia, high-dynamics AI microgrid; protection coordination breaks.
- **Hardware stack:** Grid-forming inverter controllers, fast protection relays, MV paralleling switchgear interface, storage interface.
- **Software/control stack:** Virtual-synchronous-machine + droop control, islanding/anti-islanding, protection coordination, re-sync logic.
- **Prototype path 2026–2028:** 2026 controller + HIL demo of islanded AI load; 2027 multi-MW field microgrid with SOFC/gas + storage; 2028 100 MW+ islanded campus reference.
- **China wedge:** Distributed prime-power + microgrid policy support; domestic inverter supply.
- **US wedge:** Bloom Energy SOFC and gas behind-the-meter deals (AEP/AWS/Brookfield) are scaling fast; controller is the missing stabilization layer.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Air-permit and interconnection rules; grid-control export sensitivity.
- **Competitors:** Caterpillar/Cummins controls, PowerSecure, GE Vernova, Schneider EcoStruxure, startup microgrid controllers.
- **Defensibility:** Grid-forming + protection co-design for inverter-dominant AI loads; certification and field reliability.
- **Kill criteria:** If hyperscalers default to simple grid-parallel gas with utility backup and don't need true islanding/grid-forming.
- **Evidence status:** CLEARED_WITH_WEAKNESS (DOE GFM spec + behind-the-meter scaling via journalism/company; islanding stability peer-reviewed).
- **Key sources:** DOE GFM IBR spec v1; FERC PJM order (BTM generation rules); Utility Dive / company SOFC deals (timing).

### PWR-06 — Medium-Frequency Transformer / High-Frequency Magnetics Engine
- **One-sentence product:** A medium-frequency (5–50 kHz) high-isolation transformer + integrated-cooling magnetics platform engineered to be the core building block inside every MV solid-state transformer / power core.
- **System boundary shift:** Treats the **magnetic element as the design-limiting engine** of the SST and productizes it as a qualified module, not a custom one-off.
- **Extreme metric:** >10 kW/L power density at >99.3% transformer efficiency, partial-discharge-free at MV isolation (e.g., 10–25 kV), with managed hot-spot temperature.
- **First high-end customer:** SST / 800VDC power-core makers (including PWR-01-type entrants) and EV/charging power-electronics OEMs.
- **Buyer title:** Director of Power Magnetics / Power Electronics R&D.
- **Pain:** The MFT dominates SST size, loss, insulation reliability, and cost; in-house magnetics design is slow, partial-discharge failures are common, and there's no qualified merchant supply.
- **Current workaround:** Each SST team designs bespoke transformers with line-frequency-era tools; long iteration, poor yield.
- **Why current solution fails:** Electrical/magnetic/dielectric/thermal limits are coupled; few teams can co-optimize them, and standard cores/insulation don't meet MV-DC reliability.
- **Hardware stack:** Nanocrystalline/amorphous or ferrite cores, litz/foil windings, advanced solid+fluid insulation, integrated liquid/heat-pipe cooling.
- **Software/control stack:** Multiphysics design-optimization toolchain (magnetics + thermal + dielectric) and digital-twin loss/PD model (the moat is the toolchain + qualified library).
- **Prototype path 2026–2028:** 2026 100 kW / 10 kHz qualified MFT module; 2027 MV-isolated 250 kW–1 MW family; 2028 design wins inside ≥2 SST/charging platforms.
- **China wedge:** Dominant nanocrystalline/amorphous ribbon and magnetics manufacturing base; cost + scale.
- **US wedge:** Merchant high-reliability MV magnetics is a gap; sell into the entire SST ecosystem rather than picking a winner.
- **Cleanroom dependency:** None; winding/potting/test facility, not semiconductor cleanroom.
- **Capex band:** Med.
- **Regulatory/export risk:** Low (materials), some dual-use on MV power tech.
- **Competitors:** Hitachi Metals/Proterial (cores), Payton, Vacuumschmelze, in-house teams at ABB/Hitachi Energy.
- **Defensibility:** Multiphysics toolchain + PD-free MV insulation know-how + qualification library; "arms dealer" to all SST makers.
- **Kill criteria:** If incumbents keep magnetics in-house and merchant qualification never closes design wins.
- **Evidence status:** CLEARED (peer-reviewed MFT design-optimization literature in IEEE TPEL).
- **Key sources:** Mogorovic & Dujic, MFT design optimization & experimental verification, IEEE Trans. Power Electronics; OSTI MV insulation design report.

### PWR-07 — Superconducting MVDC Campus Busway (Substation-to-Hall Ultra-Dense Link)
- **One-sentence product:** A cryostat-housed REBCO HTS DC busway that carries 10s of kA at MV across a gigawatt campus from substation to data halls with near-zero resistive loss.
- **System boundary shift:** Replaces tonnes of copper MV/LV busbar and feeders with a **thin, ultra-high-current-density superconducting spine**, removing the copper/loss/footprint ceiling on campus density.
- **Extreme metric:** Engineering current density ~150–300 kA/cm² (20 K) vs. ~1 kA/cm² copper; transmission loss demonstrated at ~1.7% of conventional AC in representative studies; multi-kA single cable.
- **First high-end customer:** GW-scale AI campus developer / hyperscaler campus electrical lead.
- **Buyer title:** Director of Campus Power Infrastructure.
- **Pain:** Distributing 1–5 GW across a campus needs enormous copper and rights-of-way; losses and voltage drop force substations close to halls and waste land/capex.
- **Current workaround:** Many parallel copper feeders + multiple distributed substations.
- **Why current solution fails:** Copper hits ampacity, weight, and loss limits; cannot scale cleanly to multi-GW dense campuses.
- **Hardware stack:** REBCO/HTS tape cable, cryostat, cryocooler/LN2 (or sub-cooled) plant, current leads, terminations, DC converter interfaces.
- **Software/control stack:** Quench detection/protection, cryogenic plant control, fault-coordination with HVDC converters.
- **Prototype path 2026–2028:** 2026 short (10–50 m) MVDC HTS busway loop demo at rated current; 2027 100–200 m substation-to-hall pilot; 2028 campus-spine reference with reliability data.
- **China wedge:** Domestic REBCO tape capacity (Shanghai Superconductor) + deployed 35 kV/1.2 km HVDC HTS cable precedent + GW campus pipeline.
- **US wedge:** GW campuses (Stargate-class) make the copper/land math favor HTS; pairs with HVDC bring-in.
- **Cleanroom dependency:** None in-house; buy HTS tape from merchant suppliers; cable/cryostat assembly is specialized but not semiconductor cleanroom.
- **Capex band:** Very High.
- **Regulatory/export risk:** HTS tape and cryo tech have dual-use/export sensitivity; novel MVDC safety approval.
- **Competitors:** Nexans, Sumitomo, LS Cable, VEIR, SuperNode, Shanghai Superconductor.
- **Defensibility:** Systems integration (cable + cryostat + quench protection + converter coordination) and reliability data; first qualified campus spine.
- **Kill criteria:** If cryo balance-of-plant + reliability never beat distributed copper substations on $/MW-delivered at campus scale.
- **Evidence status:** CLEARED (multiple Q1 peer-reviewed sources + field demos).
- **Key sources:** Superconductor Science & Technology 2026 HTS cable roadmap (DOI 10.1088/1361-6668/ae15c2); Applied Energy 2022 (DOI 10.1016/j.apenergy.2022.118602); Energy 2022 superconducting DC busbar networks (pii S036054422200723X).

### PWR-08 — Cryogenic GaN Power-Electronics Module
- **One-sentence product:** A GaN-based power-converter module engineered and packaged to operate at cryogenic temperature (77 K down toward 20 K) co-located with superconducting machines or cryo-cooled systems.
- **System boundary shift:** Moves power conversion **inside the cold environment**, exploiting GaN's improved on-resistance/switching at cryo to slash loss and co-package with superconducting machines.
- **Extreme metric:** ~5× on-resistance reduction and ~30% lower converter loss at cryo vs. room temperature; supports MW-class drives at high specific power.
- **First high-end customer:** Electrified-aircraft propulsion programs and cryo-cooled superconducting machine builders.
- **Buyer title:** Chief Engineer, Electric Propulsion / Superconducting Machines.
- **Pain:** Superconducting motors/generators need a cold drive electronics layer; warm power electronics force long cryo feedthroughs, heat leak, and weight penalties.
- **Current workaround:** Room-temperature inverters with long leads into the cryostat; large thermal-management mass.
- **Why current solution fails:** SiC degrades at cryo (rising Ron), and warm electronics impose heat-leak and specific-power penalties incompatible with flight/dense systems.
- **Hardware stack:** Cryo-rated GaN HEMTs, cryo-compatible gate drive/passives, low-thermal-leak packaging, integrated cold plate.
- **Software/control stack:** Cryo-characterized device models, temperature-adaptive control, quench/over-temp protection.
- **Prototype path 2026–2028:** 2026 sub-100 kW cryo GaN converter characterized at 77 K; 2027 MW-class cryo inverter brassboard; 2028 integration with a superconducting machine demo.
- **China wedge:** CAS superconducting machine programs + domestic GaN; aviation electrification push.
- **US wedge:** NASA HEMM/cryo-inverter heritage (16 kW/kg motor; 18 kVA/kg cryo inverter) and defense/eVTOL pull.
- **Cleanroom dependency:** None in-house; GaN die procured; cryo packaging/characterization lab required.
- **Capex band:** High.
- **Regulatory/export risk:** Aerospace/defense ITAR/EAR exposure; GaN export controls.
- **Competitors:** NASA-affiliated teams, GE Aerospace, Airbus UpNext, Rolls-Royce, university cryo-power labs.
- **Defensibility:** Cryo device characterization + packaging IP + machine co-design; very few teams worldwide.
- **Kill criteria:** If superconducting machines stall commercially and cryo electronics have no near-term host system.
- **Evidence status:** CLEARED_WITH_WEAKNESS (peer-reviewed cryo-power reviews + NASA authoritative; commercial host systems early).
- **Key sources:** NASA NTRS HEMM / cryo MW inverter; iEnergy/IEEE review of cryogenic power electronics (DOI 10.23919/IEN.2024.0014); IOP cryo device comparison.

### PWR-09 — Superconducting Fault-Current Limiter for Dense Power Nodes
- **One-sentence product:** A REBCO resistive superconducting fault-current limiter that instantly limits fault current at congested MV/DC nodes (data-center substations, shipboard grids) and self-recovers.
- **System boundary shift:** Adds a **passive, near-instant current-limiting element** that lets dense nodes raise short-circuit capacity without ripping out switchgear.
- **Extreme metric:** Sub-cycle (sub-millisecond) fault limitation with ~50 ms ride-through and seconds-scale recovery; transparent (zero loss) in normal operation.
- **First high-end customer:** Navy/shipboard MVDC integrators; secondarily dense data-center substations and utilities.
- **Buyer title:** Director of Shipboard Power Systems / Substation Engineering.
- **Pain:** Adding generation/loads at a node raises fault current beyond switchgear ratings; replacing all breakers is costly and slow.
- **Current workaround:** Series reactors, bus splitting, or wholesale switchgear upgrades — lossy or disruptive.
- **Why current solution fails:** Reactors add steady loss; switchgear replacement is expensive; neither is as fast or transparent as an SFCL.
- **Hardware stack:** REBCO tape coils/modules, cryostat + cryocooler, fault-energy management, recovery control.
- **Software/control stack:** Quench/recovery monitoring, coordination with protection relays.
- **Prototype path 2026–2028:** 2026 lab SFCL module at MV; 2027 shipboard/microgrid demonstrator; 2028 fielded node installation with utility/Navy.
- **China wedge:** Domestic REBCO + state-grid SFCL demonstration history.
- **US wedge:** Navy MVDC electrification and dense-load substations; prior AMSC/Siemens validation.
- **Cleanroom dependency:** None in-house; HTS tape procured.
- **Capex band:** High.
- **Regulatory/export risk:** HTS dual-use; defense procurement.
- **Competitors:** Applied Materials/Faraday, SuperOx, AMSC heritage, Nexans.
- **Defensibility:** Recovery + fault-energy management engineering and qualification; defense relationships.
- **Kill criteria:** If solid-state fault current limiters (SiC) outcompete on cost/footprint without cryogenics.
- **Evidence status:** CLEARED_WITH_WEAKNESS (peer-reviewed SFCL demos exist; mostly demonstration-stage, not yet broad commercial).
- **Key sources:** MDPI Energies SFCL functionality study (verify Q1/Q2); HAL/IEEE ship-grid SFCL demonstrator; EPRI SFCL technology watch.

### PWR-10 — High-Power-Density Flywheel Ride-Through (Sub-Second BBU Replacement)
- **One-sentence product:** A high-power kinetic energy buffer (flywheel) sized for sub-second-to-tens-of-seconds AI load ride-through and grid frequency support, replacing battery backup units for transient duty.
- **System boundary shift:** Splits backup into **a kinetic high-power layer for transients** (millions of cycles, no degradation) and a separate energy layer for long outages.
- **Extreme metric:** <4 s response, instantaneous high-power injection, ~hundreds of kW–MW per unit, with effectively unlimited cycle life vs. battery wear.
- **First high-end customer:** AI data-center critical-facilities team and behind-the-meter microgrid operators.
- **Buyer title:** Director of Critical Power / Energy Storage.
- **Pain:** Battery BBUs degrade under the high-cycle transient duty AI loads impose and are oversized for short ride-through; chemistry safety adds cost.
- **Current workaround:** Oversized Li-ion BBUs cycled hard, or supercaps with limited energy.
- **Why current solution fails:** Batteries wear out and have thermal-runaway risk under heavy cycling; supercaps can't cover tens of seconds.
- **Hardware stack:** Composite/steel rotor, magnetic bearings, vacuum housing, bidirectional motor-generator + SiC drive.
- **Software/control stack:** Grid-forming/frequency-response control, charge/discharge scheduling, bearing/vacuum monitoring.
- **Prototype path 2026–2028:** 2026 single-unit MW transient demo; 2027 rack-row/hall integration; 2028 multi-unit campus frequency-support reference.
- **China wedge:** Domestic flywheel manufacturing scaling for grid frequency regulation.
- **US wedge:** Sandia/DOE flywheel frequency-regulation precedent; AI transient duty is a perfect fit.
- **Cleanroom dependency:** None.
- **Capex band:** Med–High.
- **Regulatory/export risk:** Low.
- **Competitors:** Amber Kinetics, Beacon heritage, Piller (UPS flywheels), Energiestro, Chinese flywheel makers.
- **Defensibility:** Bearing/rotor + grid-forming drive integration and reliability; AI-transient-tuned control.
- **Kill criteria:** If supercap + battery hybrids dominate transient duty at lower $/kW and flywheels stay niche.
- **Evidence status:** CLEARED_WITH_WEAKNESS (DOE/Sandia flywheel reports authoritative; data-center transient fit partly inferred).
- **Key sources:** Sandia flywheel frequency-regulation reports; DOE Beacon grid-scale flywheel report; peer-reviewed flywheel frequency-regulation review (Renewable Energy/Elsevier).

### PWR-11 — Solid-State MV Interconnect Bay (Fast-Interconnect Static Substation)
- **One-sentence product:** A solid-state MV switching/transformer bay (static transformer + solid-state tap/breaker) that gives utilities dynamic power-flow control and fault-current limiting to interconnect large loads faster.
- **System boundary shift:** Replaces the passive substation bay with an **active, controllable solid-state node** that manages flow, voltage, and fault current to free interconnection capacity without new lines.
- **Extreme metric:** Dynamic load balancing + fault-current limiting + voltage regulation in one bay; helps unlock the ~175 GW of transmission headroom IEA cites from grid-optimization.
- **First high-end customer:** Transmission/distribution utility serving large data-center loads.
- **Buyer title:** Director of Transmission/Substation Engineering.
- **Pain:** Interconnect queues run ~5 years; existing substations can't dynamically manage volatile large loads, forcing costly new builds.
- **Current workaround:** Conventional transformers + mechanical tap changers + reactors; new-line buildouts.
- **Why current solution fails:** Passive equipment can't control flow or limit fault current dynamically; upgrades are slow and capital-heavy.
- **Hardware stack:** SiC MV converter, solid-state tap changer, integrated breaker/limiter, MV transformer.
- **Software/control stack:** Power-flow/voltage control, fault-current limiting logic, ISO/utility dispatch interface.
- **Prototype path 2026–2028:** 2026 sub-scale solid-state tap/limiter demo (DOE FITT-style); 2027 distribution-feeder pilot; 2028 utility field bay at a data-center interconnect.
- **China wedge:** State grid flexible-substation programs; domestic SiC.
- **US wedge:** DOE FITT/GRIP funding explicitly targets solid-state transformer/tap-changer tech; FERC pressure to speed interconnection.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Grid-asset certification; SiC export.
- **Competitors:** GE Vernova, Resilient Power Systems, Hitachi Energy, Smart Wires (topology control).
- **Defensibility:** Utility qualification + control IP + DOE-backed demos; long sales cycle is also a moat.
- **Kill criteria:** If utilities reject power-electronic substations as unproven and stick to copper + new lines.
- **Evidence status:** CLEARED (DOE FITT/GRIP awards + FERC interconnection + IEA grid-optimization headroom).
- **Key sources:** DOE OE FITT/GRIP awards (GE Vernova, Resilient Power Systems); FERC Dec-2025 PJM order; IEA Energy & AI grid section.

### PWR-12 — Megawatt Charging Power Core (Multi-MW MCS Depot)
- **One-sentence product:** A solid-state MV-to-DC charging power core delivering 1–3.75 MW per port (MCS, up to 1250 V / 3000 A) for heavy-duty electric truck/equipment depots, reusing the SST + SSCB stack.
- **System boundary shift:** Brings the **AI-factory MV-DC power core to the charging plug**, eliminating the line-frequency transformer + rectifier chain at the depot.
- **Extreme metric:** >95% efficiency at MW-class; 1250 V/3000 A per port; switching-matrix power allocation across multiple ports.
- **First high-end customer:** Fleet/depot operator and charging network for Class-8 trucks.
- **Buyer title:** Director of Fleet Electrification / Charging Infrastructure.
- **Pain:** MCS needs multi-MW per stall with grid-friendly behavior; conventional architectures are bulky, lossy, and stress the local grid.
- **Current workaround:** MV transformer + parallel DC chargers + separate buffering.
- **Why current solution fails:** Multi-stage conversion is inefficient and large; can't smooth peak draw or share power flexibly.
- **Hardware stack:** SiC MV SST front end, isolated DC-DC, switching matrix, liquid-cooled MCS interface, optional buffer storage.
- **Software/control stack:** ISO 15118-20 plug-and-charge, dynamic power allocation, grid-support/peak-shaving control.
- **Prototype path 2026–2028:** 2026 1 MW MCS power-core bench demo; 2027 depot pilot with 2–3 MW ports; 2028 multi-port grid-interactive depot.
- **China wedge:** Largest EV-truck/charging market + domestic SiC + MV-DC standardization.
- **US wedge:** MCS standard finalizing; freight electrification corridors; shares engine with PWR-01.
- **Cleanroom dependency:** None.
- **Capex band:** Med–High.
- **Regulatory/export risk:** Charging standards; SiC export.
- **Competitors:** ABB, Heliox, Kempower, Alpitronic, ChargePoint, Chinese MCS makers.
- **Defensibility:** Shared MV-DC core platform economics + grid-interactive control; reuse of AIDC stack.
- **Kill criteria:** If MCS rollout stalls or buyers prefer commodity AC-input chargers.
- **Evidence status:** CLEARED_WITH_WEAKNESS (DOE/OSTI MCS architecture authoritative; standard still maturing).
- **Key sources:** OSTI MW-scale charging system architecture; MCS/ISO 15118-20 standard documentation; IEEE 802.3 10BASE-T1S (comms).

### PWR-13 — MVDC Electric-Ship Power & Protection System
- **One-sentence product:** An integrated MVDC shipboard power-distribution and ultra-fast DC protection system for all-electric naval and commercial vessels.
- **System boundary shift:** Moves shipboard distribution from AC ring buses to a **fault-managed MVDC integrated power system** with semiconductor protection and multi-mode operation.
- **Extreme metric:** Selective sub-millisecond DC fault clearing across multiple operating modes; high power density for pulsed/propulsion + service loads.
- **First high-end customer:** Naval shipbuilder / Navy power-systems program.
- **Buyer title:** Program Manager, Shipboard Integrated Power Systems.
- **Pain:** Next-gen warships and large electric ships need MVDC for density and pulsed loads, but DC fault protection and multi-converter coordination are unsolved at the needed speed/selectivity.
- **Current workaround:** MVAC distribution + conventional breakers; limited density and pulsed-load support.
- **Why current solution fails:** AC distribution can't meet density/pulsed-power needs; standard breakers too slow for MVDC faults.
- **Hardware stack:** MVDC bus, SiC DC breakers/limiters, converter modules, energy buffers.
- **Software/control stack:** Fault detection/management, mode coordination, power management for failure modes.
- **Prototype path 2026–2028:** 2026 MVDC protection testbed; 2027 shore-based integrated power-system demo; 2028 vessel/Navy demonstrator.
- **China wedge:** PLAN electrification + domestic power electronics (note: primarily a US/allied defense play; China lane is sovereign-only).
- **US wedge:** US Navy MVDC roadmap and electric-ship programs; defense funding.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Heavy ITAR/defense controls.
- **Competitors:** GE Vernova, L3Harris, BAE Systems, Leonardo DRS, ABB Marine.
- **Defensibility:** Defense qualification + DC-protection IP; high barriers to entry.
- **Kill criteria:** If Navy delays MVDC adoption or prime contractors keep it fully in-house.
- **Evidence status:** CLEARED (peer-reviewed MVDC ship power-electronics reviews + Navy design specs).
- **Key sources:** Electric Power Systems Research (Elsevier) all-electric ship MVDC review (pii S0142061517300595); ESPR MVDC design specs/requirements review (pii S0142061518302680); Doerry MVDC architecture papers (authoritative).

### PWR-14 — eVTOL / Electric-Aircraft HV Power-Distribution + Solid-State Protection Unit
- **One-sentence product:** An 800–1000 V high-voltage power-distribution unit with fast solid-state protection and fault isolation for eVTOL and electrified aircraft.
- **System boundary shift:** Replaces relay-based aircraft power distribution with a **lightweight solid-state HV distribution + protection core** designed for fault-tolerant, redundant flight power.
- **Extreme metric:** 800 V class distribution at high specific power (kW/kg), sub-millisecond fault isolation, fail-operational redundancy for flight safety.
- **First high-end customer:** eVTOL / electric-aircraft OEM.
- **Buyer title:** Chief Engineer, Electrical Power Systems.
- **Pain:** Flight power must be light, redundant, and fault-isolating at 800 V where arcing risk rises with altitude; legacy contactors are heavy and slow.
- **Current workaround:** Contactor/relay distribution + fuses; heavy and slow.
- **Why current solution fails:** Mechanical protection is heavy and too slow for HV DC arc faults; can't meet fail-operational + weight targets.
- **Hardware stack:** SiC/GaN solid-state power controllers, HV bus, sensing, lightweight packaging.
- **Software/control stack:** Fault detection/isolation, load management, redundancy/reconfiguration logic, DO-160/DO-254-aligned design.
- **Prototype path 2026–2028:** 2026 800 V SSPC distribution unit bench demo; 2027 iron-bird integration with an OEM; 2028 flight-test hardware.
- **China wedge:** Large eVTOL OEM base (EHang, XPeng AeroHT) + domestic WBG.
- **US wedge:** Joby/Archer/Beta certification pipelines; defense electrification.
- **Cleanroom dependency:** None.
- **Capex band:** Med–High.
- **Regulatory/export risk:** Aviation certification + ITAR/EAR for defense variants.
- **Competitors:** Astronics, Safran, Honeywell, GE Aerospace, startups.
- **Defensibility:** Certified lightweight solid-state protection IP; OEM design-ins are sticky.
- **Kill criteria:** If eVTOL market timelines slip badly or OEMs keep power distribution in-house.
- **Evidence status:** CLEARED_WITH_WEAKNESS (NASA 800 V architecture work authoritative; market timing uncertain).
- **Key sources:** NASA 800 V modular aircraft battery architecture (NTRS); IEEE/AIAA more-electric-aircraft power literature; NASA EAP program reports.

### PWR-15 — LDES Power-Conversion + Balance-of-Plant Skid (100-Hour-Optimized PCS)
- **One-sentence product:** A low-cost bidirectional power-conversion system + balance-of-plant skid purpose-built for 100-hour long-duration storage (iron-air, flow, thermal), where $/kW PCS dominates value not $/kWh.
- **System boundary shift:** Decouples and optimizes the **power layer separately from the energy layer** for ultra-long-duration storage, where conventional 4-hour BESS PCS is wrong-sized and overpriced.
- **Extreme metric:** PCS + BOP cost targeting a fraction of standard BESS $/kW by exploiting low power-to-energy ratios; multi-day dispatch capability.
- **First high-end customer:** LDES project developer / utility integrating iron-air or flow systems.
- **Buyer title:** Director of Storage Project Engineering.
- **Pain:** LDES economics live or die on balance-of-plant and PCS cost; today's PCS/BOP (designed for short-duration BESS) is a major and ill-fit cost driver.
- **Current workaround:** Repurpose standard BESS inverters + ad-hoc BOP; over-spec'd and costly.
- **Why current solution fails:** Short-duration PCS is optimized for high power-to-energy ratios and frequent cycling, not the trickle-power, long-duration LDES profile.
- **Hardware stack:** Right-sized bidirectional inverter, MV interface, thermal/air management for the storage medium, integration skid.
- **Software/control stack:** Multi-day dispatch optimization, grid-forming/ancillary services, plant controller.
- **Prototype path 2026–2028:** 2026 PCS+BOP skid spec'd to an LDES chemistry; 2027 pilot with an LDES developer; 2028 utility-scale reference plant.
- **China wedge:** Massive LDES + renewable-integration mandate; domestic inverter scale.
- **US wedge:** First grid-connected iron-air (Ore Energy 2025) and Form Energy scale-up create pull for purpose-built BOP.
- **Cleanroom dependency:** None.
- **Capex band:** Med–High.
- **Regulatory/export risk:** Grid interconnection; low export risk.
- **Competitors:** SMA, Sungrow, Power Electronics SL, Form Energy (in-house), EPC integrators.
- **Defensibility:** Chemistry-specific BOP optimization + grid-forming control; partner lock-in with LDES makers.
- **Kill criteria:** If LDES OEMs vertically integrate BOP or standard BESS PCS proves "good enough."
- **Evidence status:** CLEARED_WITH_WEAKNESS (peer-reviewed iron-energy nexus + BOP cost-driver evidence; commercial LDES early).
- **Key sources:** iScience (Cell Press) iron-energy nexus (pii S2590332222001026); C&EN LDES review (ACS); grid-connection milestone (journalism, timing).

### PWR-16 — High-Temp DC-Link / Buffer Capacitor + Module for 15-Year AI SLA
- **One-sentence product:** A high-temperature polymer-dielectric DC-link / energy-buffer capacitor and module engineered for 800 VDC power cores to meet 15-year, high-humidity, high-cycle AI-factory reliability.
- **System boundary shift:** Turns the **capacitor from the lifetime-limiting weak link into the reliability backbone** of 800 VDC conversion and buffering.
- **Extreme metric:** >600 V/µm dielectric headroom, ~15+ year service life at data-center humidity/temperature, microsecond transient response for power smoothing.
- **First high-end customer:** 800 VDC power-core / power-shelf OEM (PWR-01/03 ecosystem).
- **Buyer title:** Director of Power Electronics Component Engineering.
- **Pain:** Electrolytic caps wear out in ~6–8 years; existing film caps struggle with the temperature/humidity + transient-smoothing duty of AI factories; capacitor failure dominates converter failure rate.
- **Current workaround:** Over-provision electrolytic/film caps and accept replacement cycles.
- **Why current solution fails:** Electrolytic evaporation/wear-out and humidity sensitivity cause early failure; standard films don't meet the combined thermal/transient/SLA envelope.
- **Hardware stack:** High-temp polymer/nanocomposite film, metallization, self-healing winding, low-ESR module packaging.
- **Software/control stack:** Embedded condition monitoring / remaining-life estimation (changes maintenance scheduling, not just reports).
- **Prototype path 2026–2028:** 2026 dielectric + cap prototype with accelerated-life data; 2027 module qualified into a power-core; 2028 design wins + field reliability data.
- **China wedge:** Dominant film-capacitor manufacturing base; cost + scale.
- **US wedge:** Reliability-critical AI SLAs + advanced-dielectric IP (e.g., high-temp polymer) is a differentiated wedge.
- **Cleanroom dependency:** None (film/metallization line, not semiconductor cleanroom).
- **Capex band:** Med–High.
- **Regulatory/export risk:** Low; some advanced-material IP sensitivity.
- **Competitors:** TDK, KEMET/Yageo, Vishay, PeakNano, Chinese film-cap makers.
- **Defensibility:** Dielectric material + module reliability data + design-ins; hard to second-source once qualified.
- **Kill criteria:** If incumbents close the high-temp film-cap gap first or buffering moves entirely to supercaps.
- **Evidence status:** CLEARED (peer-reviewed DC-link capacitor reliability literature + documented AI buffering requirement).
- **Key sources:** Wang & Blaabjerg IEEE TIA (DOI 10.1109/TIA.2014.2308357) capacitor reliability; film-capacitor lifetime studies; NVIDIA power-smoothing energy spec (company, triangulated).

### PWR-17 — China-First 800VDC AIDC Power Core ("Panama-Class" Localized)
- **One-sentence product:** A fully domestic MV-to-800VDC AI-data-center power core optimized for China's east-west (东数西算) clusters, using domestic SiC, magnetics, and controls.
- **System boundary shift:** Same single-core MV-DC boundary shift as PWR-01, **localized for China's standard, supply chain, and west-cluster renewable surplus** rather than a US clone.
- **Extreme metric:** ~98.5% MV-to-800VDC efficiency at multi-MW per cabinet with prefabricated, hot-swappable modular deployment.
- **First high-end customer:** Chinese hyperscaler (Alibaba Cloud, Tencent, ByteData) building west-cluster AI campuses.
- **Buyer title:** Head of Data Center Power Architecture (China cloud).
- **Pain:** West-cluster campuses need rapid, prefab, high-density power with minimal copper and grid-friendly behavior to absorb renewable variability.
- **Current workaround:** Delta/Alibaba "Panama" MV-DC + domestic HVDC, still maturing toward 800 V.
- **Why current solution fails (gap to fill):** Current Panama/HVDC solutions are early on 800 V, grid-forming behavior, and integrated transient buffering for GPU loads.
- **Hardware stack:** Domestic SiC MV stacks, nanocrystalline magnetics, 800 VDC output, integrated protection + buffer.
- **Software/control stack:** Grid-forming control tuned for renewable west clusters; prefab commissioning tooling.
- **Prototype path 2026–2028:** 2026 cabinet-scale demo aligned to the domestic 800 VDC white paper; 2027 west-cluster campus pilot; 2028 multi-campus rollout.
- **China wedge:** Policy tailwind (东数西算, green-transformation mandates), domestic supply, incumbent standard momentum — a genuine China-first lane, not a clone.
- **US wedge:** Limited directly; IP/control could license to allied markets but export-constrained.
- **Cleanroom dependency:** None; domestic SiC sourcing.
- **Capex band:** High.
- **Regulatory/export risk:** Reverse export risk (US SiC/EDA dependence); favored if fully domestic.
- **Competitors:** Delta, Huawei Digital Power, Envicool, Kehua, SuperX, Sungrow.
- **Defensibility:** Standard alignment + domestic supply + grid-forming control for renewable clusters; policy moat.
- **Kill criteria:** If Huawei Digital Power / Delta capture the standard and lock the cabinet market before entry.
- **Evidence status:** CLEARED_WITH_WEAKNESS (China policy + market authoritative/triangulated; specific products are company claims).
- **Key sources:** China data-center electricity-demand policy (MIIT via CNESA/Wood Mackenzie triangulation); Delta/Alibaba Panama + 800 VDC white paper (company); IEA China data-center growth.

### PWR-18 — Active Wide-Area Oscillation Damper for Data-Center Grids
- **One-sentence product:** A fast power-electronic damping device (PMU-driven) that actively cancels the sub-/super-synchronous oscillations large AI data centers inject into the grid — it acts, not just observes.
- **System boundary shift:** Converts oscillation *monitoring* into **closed-loop active damping hardware** at the point of common coupling.
- **Extreme metric:** Detect-and-damp oscillation modes (e.g., the documented ~14–15 Hz and lower-frequency data-center modes) within cycles; configurable damping across a wide frequency band.
- **First high-end customer:** ISO/utility + large data-center operator at the interconnection point.
- **Buyer title:** Director of Grid Stability / Transmission Operations.
- **Pain:** AI training loads induce sustained, measurable grid oscillations that threaten stability and trigger curtailment/interconnect denial; monitoring alone doesn't fix it.
- **Current workaround:** PMU monitoring + manual mitigation / load curtailment.
- **Why current solution fails:** Monitoring is passive; existing damping (PSS on generators) isn't tuned for inverter-load-driven oscillations at data-center nodes.
- **Hardware stack:** Fast MW converter (often co-located with storage/STATCOM), PMU sensing, MV interface.
- **Software/control stack:** Real-time oscillation detection + wide-area damping control, coordination with grid-forming assets.
- **Prototype path 2026–2028:** 2026 HIL + lab damping demo against recorded data-center oscillation modes; 2027 substation pilot; 2028 ISO-accepted damping product.
- **China wedge:** State grid stability programs + dense AI clusters.
- **US wedge:** PNNL/DOE/NERC have formalized the oscillation problem; FERC interconnection pressure creates demand for an active fix.
- **Cleanroom dependency:** None.
- **Capex band:** Med–High.
- **Regulatory/export risk:** Grid-control export sensitivity; ISO certification.
- **Competitors:** Hitachi Energy (STATCOM/grid-forming), GE Vernova, Mitsubishi, Smart Wires.
- **Defensibility:** Wide-area damping control IP validated on real data-center modes; ISO certification.
- **Kill criteria:** If grid-forming converters (PWR-04) absorb this function and a standalone damper has no market.
- **Evidence status:** CLEARED (DOE/PNNL/NERC oscillation evidence is authoritative; must remain an actuator, not a dashboard).
- **Key sources:** PNNL NASPI "Measurement Adequacy for Monitoring Data Center Oscillations"; DOE OE oscillation article; NERC oscillation monitoring/mitigation TRD.

### PWR-19 — MV Isolated Gate-Driver & Stack-Control Platform for SiC Power Cores
- **One-sentence product:** A high-isolation, high-dv/dt gate-driver + modular stack-control platform (the "nervous system") that makes series-stacked MV SiC reliable inside solid-state transformers and breakers.
- **System boundary shift:** Productizes the **MV series-stack control + isolation layer** that today is the hidden failure point of every MV SiC converter.
- **Extreme metric:** Multi-kV isolation, >100 kV/µs common-mode immunity, sub-nanosecond switching synchronization across series devices, integrated protection.
- **First high-end customer:** SST / SSCB / MV-converter makers (the PWR-01/02/11 ecosystem).
- **Buyer title:** Director of Power Electronics Design.
- **Pain:** Series-stacking SiC at MV is plagued by voltage imbalance, dv/dt-induced faults, and isolation breakdown; teams burn months on gate-drive reliability.
- **Current workaround:** Custom in-house gate drives + isolation, low yield and reliability.
- **Why current solution fails:** Off-the-shelf drivers lack the isolation/timing/protection for MV series stacks; bespoke designs don't scale.
- **Hardware stack:** Reinforced-isolation gate driver, isolated power/signal, active voltage balancing, desat/short-circuit protection, modular controller.
- **Software/control stack:** Synchronization + balancing firmware, fault management, configurable for different stack topologies.
- **Prototype path 2026–2028:** 2026 MV stack gate-drive reference module; 2027 design-ins with ≥2 converter makers; 2028 qualified platform with field data.
- **China wedge:** Domestic SiC ecosystem needs the control layer; sell to all domestic SST makers.
- **US wedge:** Merchant MV stack-control is a real gap; arms-dealer to the SST race.
- **Cleanroom dependency:** None.
- **Capex band:** Low–Med.
- **Regulatory/export risk:** Some MV power-control IP sensitivity.
- **Competitors:** Power Integrations, Infineon (EiceDRIVER), Texas Instruments, Analog Devices, in-house teams.
- **Defensibility:** Isolation + balancing + protection IP and reliability library; component lock-in.
- **Kill criteria:** If chip vendors integrate full MV stack control on-die and eliminate the merchant layer.
- **Evidence status:** CLEARED_WITH_WEAKNESS (MV SiC stacking challenges peer-reviewed; merchant demand inferred from SST literature).
- **Key sources:** IEEE Industrial Electronics Magazine SST review (Huang); IEEE TPEL MV SST/MFT papers; IEEE APEC SiC SSCB papers.

### PWR-20 — Last-Inch 800VDC→Core Vertical Power-Delivery Module
- **One-sentence product:** A high-density power module that converts 800 VDC down toward the GPU/accelerator core voltage with vertical/in-package delivery, minimizing the last-inch losses that dominate at 1 MW racks.
- **System boundary shift:** Moves the final step-down from board-edge to **vertical/under-die delivery**, cutting PDN resistance and copper at the rack's hottest, highest-current point.
- **Extreme metric:** Hundreds of amps at sub-volt core rails with minimized PDN loss; supports 1 MW rack current densities without copper-busbar blow-up.
- **First high-end customer:** Accelerator/board OEM and rack-power architect.
- **Buyer title:** Principal Engineer, Power Delivery Network.
- **Pain:** At 1 MW/rack, last-inch IR losses and copper dominate; lateral board delivery can't supply the current density GPUs now demand.
- **Current workaround:** Lateral multiphase VRMs on the board edge; massive copper planes.
- **Why current solution fails:** Lateral delivery has too much resistance/inductance at these currents; copper/loss explode.
- **Hardware stack:** Vertical power module (integrated magnetics + WBG/Si stages), advanced substrate, co-packaged with accelerator.
- **Software/control stack:** Fast multiphase control, transient response co-tuned with PWR-03 buffering.
- **Prototype path 2026–2028:** 2026 vertical power module demo into a representative load; 2027 board OEM co-design; 2028 integration with an accelerator platform.
- **China wedge:** Domestic packaging + power IC; AIDC scale.
- **US wedge:** Tied to NVIDIA-class roadmaps; advanced packaging partners.
- **Cleanroom dependency:** Moderate — advanced packaging/substrate; outsource to OSAT/packaging partners (no full fab needed).
- **Capex band:** Med–High.
- **Regulatory/export risk:** Advanced-packaging export controls (overlaps semiconductor lane).
- **Competitors:** Infineon, Vicor, Monolithic Power, Empower, Texas Instruments.
- **Defensibility:** Vertical-delivery + integrated-magnetics IP + accelerator co-design.
- **Kill criteria:** If chip vendors fully integrate on-package power delivery, foreclosing the merchant module.
- **Evidence status:** CLEARED_WITH_WEAKNESS (PDN/last-inch loss documented via 800 VDC copper analyses; partly company-claim driven).
- **Key sources:** Schneider/NVIDIA 800 VDC copper/PDN analysis (company, triangulated); IEEE power-delivery literature; high-density-rack technical reports.

### PWR-21 — HTS Cable Cryostat & Cryogenic Balance-of-Plant Subsystem
- **One-sentence product:** A modular cryostat + cryocooling balance-of-plant subsystem (the cold "engine room") that makes superconducting power links and busways deployable and serviceable.
- **System boundary shift:** Productizes the **cryogenic BOP as a standardized subsystem** rather than a bespoke science project, lowering the barrier to all HTS power deployments.
- **Extreme metric:** Low-heat-leak cryostat enabling 20–77 K operation over 100s of meters with high reliability and serviceable cryocoolers; multi-year MTBF target.
- **First high-end customer:** HTS cable/busway integrators (PWR-07/09) and fusion/magnet programs.
- **Buyer title:** Director of Cryogenic Systems.
- **Pain:** Cryo BOP (cryostat, cooling, current leads, reliability) is the cost/risk driver that stalls superconducting power adoption.
- **Current workaround:** Custom cryostats + lab cryocoolers per project; poor serviceability.
- **Why current solution fails:** Bespoke cryo BOP is expensive, unreliable, and not field-serviceable; no merchant standard exists.
- **Hardware stack:** Vacuum-insulated cryostat, redundant cryocoolers / sub-cooled LN2 loop, current leads, terminations, quench protection.
- **Software/control stack:** Cryo plant control, quench detection, reliability/predictive maintenance.
- **Prototype path 2026–2028:** 2026 modular cryostat + cooling skid demo; 2027 integration with an HTS busway pilot; 2028 field reliability dataset.
- **China wedge:** Domestic cryocooler + HTS ecosystem; deployed HTS cable precedent.
- **US wedge:** Fusion + data-center HTS demand; "picks-and-shovels" to the whole HTS sector.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Cryo/HTS dual-use export sensitivity.
- **Competitors:** Cryocooler makers (Sumitomo, Cryomech), Linde/Air Liquide, Nexans (integrated).
- **Defensibility:** Reliability + serviceability engineering + standardized interfaces; enables every HTS player.
- **Kill criteria:** If HTS power adoption stays niche and cryo BOP volume never materializes.
- **Evidence status:** CLEARED_WITH_WEAKNESS (cryo BOP as the limiting factor is well established in peer-reviewed HTS roadmaps; commercial volume early).
- **Key sources:** Superconductor Science & Technology HTS cable roadmap (DOI 10.1088/1361-6668/ae15c2); Applied Energy superconducting delivery; iEnergy cryo-power review.

### PWR-22 — Prime-Power Island Inverter / Paralleling Controller for SOFC + Gas
- **One-sentence product:** A power-conditioning + paralleling inverter and controller that turns large solid-oxide-fuel-cell and gas behind-the-meter fleets into a stable, grid-forming prime-power island for AI campuses.
- **System boundary shift:** Makes SOFC/gas DC output a **dispatchable, grid-forming AC/DC source** that can run a campus independent of the grid, not just trickle power.
- **Extreme metric:** Parallel 10s–100s of MW of SOFC modules with grid-forming stability and seamless transient support for volatile AI loads.
- **First high-end customer:** Behind-the-meter SOFC/gas power developer (e.g., partners deploying 100s of MW).
- **Buyer title:** VP of Power Systems / Generation Engineering.
- **Pain:** SOFC/gas are scaling fast for AI prime power, but conditioning their DC output, paralleling fleets, and providing grid-forming/transient support to spiky AI loads is unsolved at scale.
- **Current workaround:** Standard grid-following inverters + utility backbone for stability.
- **Why current solution fails:** Grid-following inverters can't form a stable island or follow AI transients; SOFC ramp is slow and needs buffering.
- **Hardware stack:** SiC grid-forming inverter, DC bus conditioning, storage/buffer interface, MV paralleling.
- **Software/control stack:** Grid-forming + droop control, fleet paralleling, transient buffering coordination, dispatch.
- **Prototype path 2026–2028:** 2026 inverter + controller demo on an SOFC stack; 2027 multi-MW islanded pilot; 2028 100 MW+ prime-power island.
- **China wedge:** Domestic SOFC + inverter; distributed-energy policy.
- **US wedge:** Bloom/Brookfield/AEP/AWS SOFC deals (1+ GW) need the conditioning + grid-forming layer.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Air-permit/interconnection; grid-control export.
- **Competitors:** Bloom (in-house power electronics), SMA, Power Electronics SL, GE Vernova.
- **Defensibility:** Grid-forming + fleet-paralleling control validated for fuel-cell prime power; pairs with PWR-05.
- **Kill criteria:** If SOFC makers vertically integrate the inverter/controller and refuse merchant supply.
- **Evidence status:** CLEARED_WITH_WEAKNESS (BTM SOFC scale via journalism/company + DOE GFM spec; specific deal numbers are company claims).
- **Key sources:** DOE GFM IBR spec v1; FERC PJM BTM generation order; Utility Dive / company SOFC deals (timing only).

### PWR-23 — Prefab Mobile MV Power-Island Skid (Interconnect-Queue Bypass)
- **One-sentence product:** A factory-built, truckable MV power-island skid (MV-DC core + protection + grid-forming + storage interface) that energizes an AI site in months while the utility interconnection is pending.
- **System boundary shift:** Converts grid-connection from a multi-year civil project into a **deployable, relocatable power product** that lands on site pre-commissioned.
- **Extreme metric:** Energize multi-MW of compute within months vs. ~5-year queue; relocatable and standardized.
- **First high-end customer:** Neocloud / data-center developer racing ahead of grid timelines.
- **Buyer title:** Head of Site Energization / Speed-to-Power.
- **Pain:** Interconnection queues (~5-year median) gate revenue; developers need power now, on terms they control.
- **Current workaround:** Diesel rental fleets + ad-hoc switchgear; dirty, slow to permit, not grid-forming.
- **Why current solution fails:** Rental diesel is emissions/permit-limited and can't form a stable AI microgrid; bespoke builds are slow.
- **Hardware stack:** Containerized MV-DC core (PWR-01), solid-state protection (PWR-02), grid-forming converter, storage + generation interface.
- **Software/control stack:** Plug-and-play commissioning, grid-forming/islanding control, remote ops.
- **Prototype path 2026–2028:** 2026 single-skid integrated demo; 2027 field deployment at a speed-to-power site; 2028 fleet of relocatable skids.
- **China wedge:** Prefab modular data-center culture + fast deployment; domestic supply.
- **US wedge:** FERC/DOE interconnection crisis + behind-the-meter generation rules make speed-to-power the #1 buyer pain.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Air-permit (if paired with gas); interconnection on grid re-sync.
- **Competitors:** VoltaGrid, ProEnergy, Caterpillar, Aggreko, Cummins, gas-turbine integrators.
- **Defensibility:** Integration of PWR-01/02/04 into a deployable product + commissioning speed; standardization.
- **Kill criteria:** If interconnection reform collapses the queue and speed-to-power premium disappears.
- **Evidence status:** CLEARED (FERC order + DOE interconnection authoritative; integrates cleared sub-engines).
- **Key sources:** FERC Dec-2025 PJM co-location order; Utility Dive/White & Case interconnection analyses (timing); DOE interconnection directives.

### PWR-24 — MV Grid-Forming SST for LDES / Renewable Hybrid-Plant Interconnection
- **One-sentence product:** A medium-voltage grid-forming solid-state transformer that interconnects co-located renewables + LDES + (optionally) data-center load as one grid-forming hybrid plant.
- **System boundary shift:** Collapses the separate inverter/transformer/controller chain of a hybrid plant into **one MV grid-forming SST node**, enabling renewables+storage to firmly serve large loads.
- **Extreme metric:** Single MV node providing grid-forming behavior, bidirectional MV-DC interface, and >98% efficiency for a renewables+LDES+load hybrid.
- **First high-end customer:** Renewable + storage IPP / hybrid-plant developer serving data centers.
- **Buyer title:** Director of Hybrid Plant Engineering.
- **Pain:** Hybrid plants need many converters + transformers + controllers to firm renewables for large loads; integration is costly and not grid-forming.
- **Current workaround:** Separate PV/wind inverters + BESS PCS + line-frequency transformers + plant controller.
- **Why current solution fails:** Multi-box integration is lossy, slow, and grid-following; can't firmly serve a volatile AI load behind the meter.
- **Hardware stack:** MV SiC SST, multiport DC interface (PV/wind/storage), grid-forming output, protection.
- **Software/control stack:** Grid-forming control, multiport energy management, hybrid dispatch.
- **Prototype path 2026–2028:** 2026 multiport MV SST demo; 2027 hybrid-plant pilot; 2028 grid-forming hybrid serving a data-center load.
- **China wedge:** West-cluster renewable + LDES mandate; domestic SiC and inverters.
- **US wedge:** Behind-the-meter co-location (FERC) + LDES scale-up; firm-clean-power demand from hyperscalers.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Interconnection; SiC/control export.
- **Competitors:** SMA, Sungrow, Hitachi Energy, GE Vernova, Power Electronics SL.
- **Defensibility:** Multiport grid-forming SST IP + hybrid control; shares engine with PWR-01/06.
- **Kill criteria:** If multi-box hybrids stay cheaper and grid-forming SST integration never pays off.
- **Evidence status:** CLEARED_WITH_WEAKNESS (SST + grid-forming peer-reviewed; hybrid-for-datacenter use partly inferred).
- **Key sources:** IEEE Industrial Electronics Magazine SST review; DOE GFM IBR spec; FERC co-location order; iScience iron-energy nexus.

---

## 3. Source Rows (Evidence Ledger)

> Status legend: CLEARED / CLEARED_WITH_WEAKNESS / HOLD / WATCH / WEAK_SIGNAL_ONLY / KILL. "Type" indicates whether it counts as peer-reviewed academic, authoritative non-article, company claim, or journalism (timing/triangulation only).

| SID | Source | Type | Domain/Quartile note | Supports | Status |
|-----|--------|------|----------------------|----------|--------|
| PWR-S01 | IEA, *Energy and AI* / "Energy demand from AI" (iea.org, 2025) | Authoritative non-article | International agency | Data-center electricity ~doubles to ~945 TWh by 2030; US+China ~80% of growth; ~20% of projects at risk from grid | CLEARED |
| PWR-S02 | FERC order on PJM large-load / co-location interconnection, Dec 18 2025 (ferc.gov) | Authoritative non-article (regulator) | US regulator | Interconnection is binding constraint; BTM generation + co-location rules; load volatility concern | CLEARED |
| PWR-S03 | DOE Office of Electricity — FITT / GRIP solid-state transformer & SiC packaging awards (energy.gov) | Authoritative non-article | US national program | Solid-state transformer / static substation funding (GE Vernova, Resilient Power Systems) | CLEARED |
| PWR-S04 | PNNL / NASPI, "Measurement Adequacy for Monitoring Data Center Oscillations" (pnnl.gov) | Authoritative non-article (national lab) | National lab | Data centers induce sustained measurable grid oscillations | CLEARED |
| PWR-S05 | DOE OE, "Monitoring Oscillations from Large Data Centers" (energy.gov) | Authoritative non-article | US gov | Oscillation problem formalized; AI loads to multi-GW | CLEARED |
| PWR-S06 | NERC, draft "Power System Oscillation Monitoring and Mitigation" TRD (nerc.com) | Authoritative non-article (reliability org) | Standards/reliability | Need for oscillation mitigation, not just monitoring | CLEARED |
| PWR-S07 | NASA NTRS / Glenn — HEMM (16 kW/kg, 99%) & cryo MW inverter (18 kVA/kg) (nasa.gov, ntrs.nasa.gov) | Authoritative non-article (gov lab) | US gov research | Cryo/superconducting machine + cryo power electronics metrics | CLEARED |
| PWR-S08 | DOE/OSTI, "Megawatt Scale Charging System Architecture" (osti.gov) | Authoritative non-article | National lab | MCS architecture, MW-class DC charging | CLEARED |
| PWR-S09 | DOE, "Specifications for Grid-forming Inverter-Based Resources v1" (energy.gov) | Authoritative non-article | US gov spec | Grid-forming requirements definition | CLEARED |
| PWR-S10 | Sandia, flywheel frequency-regulation reports (sandia.gov) | Authoritative non-article (national lab) | National lab | Flywheel fast frequency response, high-cycle duty | CLEARED |
| PWR-S11 | DOE/Beacon, grid-scale flywheel storage plant report (energy.gov) | Authoritative non-article | US gov | Flywheel grid-scale ride-through/frequency support | CLEARED |
| PWR-S12 | *Superconductor Science and Technology*, 2026, 39(2) 023501, DOI 10.1088/1361-6668/ae15c2 | Peer-reviewed (IOP) | Q1/Q2, high impact | HTS cable roadmap; Je ~150–300 kA/cm² at 20 K; field demos (Shanghai 35 kV/1.2 km HVDC) | CLEARED |
| PWR-S13 | *Applied Energy*, 2022, 310:118602, DOI 10.1016/j.apenergy.2022.118602 | Peer-reviewed (Elsevier) | Q1, high impact | Superconducting delivery to 100-MW data center; loss ~1.7% of conventional AC | CLEARED |
| PWR-S14 | *Energy* (Elsevier), 2022, pii S036054422200723X | Peer-reviewed (Elsevier) | Q1, high impact | Superconducting DC busbar networks for 10 MW data center; loss/economics | CLEARED |
| PWR-S15 | Wang & Blaabjerg, *IEEE Trans. Industry Applications*, 2014, 50(5):3569-3578, DOI 10.1109/TIA.2014.2308357 | Peer-reviewed (IEEE) | Q1, high impact | DC-link capacitor reliability dominates converter failure; electrolytic wear-out | CLEARED |
| PWR-S16 | Mogorovic & Dujic, MFT design optimization & experimental verification, *IEEE Trans. Power Electronics* (2018/2019) | Peer-reviewed (IEEE) | Q1, high impact | MFT is the SST design-limiting engine; multiphysics optimization, PD-free MV | CLEARED |
| PWR-S17 | Huang et al., "Medium-Voltage Solid-State Transformer," *IEEE Industrial Electronics Magazine*, 2016 (IEEE doc 7575787) | Peer-reviewed (IEEE) | Q1 | MVSST architecture for smarter/resilient grid | CLEARED |
| PWR-S18 | "A self-powered ultra-fast DC solid state circuit breaker using a normally-on SiC JFET," *IEEE APEC* (doc 7104436) | Peer-reviewed conference (IEEE APEC) | peer_reviewed_conference_no_jif | Sub-µs SiC fault interruption at 400 V | CLEARED |
| PWR-S19 | SiC MOSFET solid-state circuit breaker motor control center, *IEEE journal* (doc 10816147, 2024) | Peer-reviewed (IEEE) | Q1/Q2 | SSCB soft-start/soft-turn-off design at MV | CLEARED |
| PWR-S20 | All-electric ship MVDC power-electronics review, *Electric Power Systems Research* (Elsevier), 2017, pii S0142061517300595 | Peer-reviewed (Elsevier) | Q1/Q2 | MVDC shipboard distribution + DC protection needs | CLEARED |
| PWR-S21 | MVDC shipboard design specs/requirements review, *Electric Power Systems Research*, 2018, pii S0142061518302680 | Peer-reviewed (Elsevier) | Q1/Q2 | MVDC ship design requirements (selectivity/speed) | CLEARED |
| PWR-S22 | Review of cryogenic power electronics, *iEnergy* (IEEE/Tsinghua), 2024, DOI 10.23919/IEN.2024.0014 | Peer-reviewed | Newer journal — verify percentile | GaN improves at cryo; ~30% lower converter loss; SiC degrades at cryo | CLEARED_WITH_WEAKNESS |
| PWR-S23 | Iron-energy nexus for LDES, *iScience* (Cell Press), 2022, pii S2590332222001026 | Peer-reviewed (Cell Press) | Q1 | LDES scaling; BOP/power-layer cost drivers | CLEARED |
| PWR-S24 | SFCL functionality under long-duration faults, *Energies* (MDPI), 2025, 18(19):5302 | Peer-reviewed (MDPI) | Verify Q1/Q2 for category | REBCO SFCL fault-limiting behavior | CLEARED_WITH_WEAKNESS |
| PWR-S25 | China data-center power demand & 800 VDC policy (MIIT) — via CNESA / Wood Mackenzie / IEA triangulation | Authoritative (policy) + triangulation | China policy + agency | China DC demand ~20→40 GW (2024→2030); HVDC/DC push; 东数西算 | CLEARED_WITH_WEAKNESS |
| PWR-S26 | NVIDIA 800 VDC architecture; Schneider "1 MW rack needs 800 VDC"; Delta/Alibaba "Panama" + 800 VDC white paper | Company claim | Company-supported only | 800 VDC direction; copper/loss math; MV-UPS + DC distribution | WATCH (triangulated, not independent proof) |
| PWR-S27 | IEEE Spectrum — "Gigascale AI datacenter power"; "Taming Data Center Power Fluctuation With AI UPS" | Journalism (IEEE Spectrum) | Timing/triangulation only | Millisecond load spikes; diesel/turbine can't follow; UPS buffering | CLEARED_WITH_WEAKNESS (timing) |
| PWR-S28 | Navitas + EPFL 250 kW single-stage SST (3.3 kV AC → 800 VDC), APEC 2026 demo (semiconductor-today) | Company claim + conference demo | Company/timing | Single-stage MV-to-800VDC SST feasibility | WATCH |
| PWR-S29 | OSTI report — "Optimizing Insulation Design for Transformers in MV Power Conversion Systems" | Authoritative non-article (national lab) | National lab | PD-free MV MFT insulation challenge | CLEARED |
| PWR-S30 | Behind-the-meter SOFC/gas deals (Bloom/Brookfield/AEP/AWS) via Utility Dive / company filings | Journalism + company | Timing/triangulation | BTM prime power scaling to >1 GW | CLEARED_WITH_WEAKNESS (timing) |

---

## 4. Rejected Ideas

1. **Generic DCIM / power-monitoring dashboard.** Monitoring-only; doesn't change control or protection. Anti-pattern. **Rejected.**
2. **"AI software to optimize data-center PUE."** Software-only, TAM-claim, no hardware boundary shift; commoditizing fast. **Rejected.**
3. **Commodity Li-ion BESS container for data-center backup.** No defensibility, crowded, not engine-layer. **Rejected.** (Re-scoped into PWR-04/10 where the converter/control is the engine.)
4. **Room-temperature superconductor power cable startup.** No verified, reproducible RT-SC material; treating it as fact is regulatory/physics speculation. **Rejected** (HTS at cryo, PWR-07/21, is the grounded version).
5. **China clone of Bloom Energy SOFC.** "China clone of US company" without a defensible wedge; the defensible wedge is the grid-forming power-conditioning layer (PWR-22), not the stack. **Rejected as framed.**
6. **Wireless / resonant power transfer for data-center racks.** Not credible at MW power density; efficiency/EMI physics fail. **Rejected.**
7. **Green-hydrogen production plant for data centers.** Commodity energy production, not the power-engine layer; balance-of-plant arbitrage, not defensible subsystem. **Rejected.**
8. **Standalone PMU oscillation-monitoring product.** Monitoring-only unless it actuates; only counts if it becomes an active damper (PWR-18). **Rejected as monitoring-only.**

---

## 5. Top 5 From This Worker Lane

Ranked for engine-layer leverage, defensibility, evidence strength, and "makes a new high-end system possible":

1. **PWR-01 — AI-Factory MV-to-800VDC Solid-State Power Core.** The central chokepoint of the AI-factory power rebuild; everyone needs it, few can integrate magnetics+MV control+thermal+protection. Highest strategic leverage.
2. **PWR-06 — Medium-Frequency Transformer / High-Frequency Magnetics Engine.** The single design-limiting sub-engine inside every SST/power core; "arms dealer" to the whole race; strongest peer-reviewed grounding (IEEE TPEL).
3. **PWR-02 — Microsecond 800VDC Solid-State Breaker / e-Fuse.** A hard physics gate (no DC current zero) that blocks 800 VDC deployment; cleared by peer-reviewed SiC SSCB results; clear first buyer.
4. **PWR-03 — Rack Transient Buffer / Power-Smoothing Energy Interface.** Directly attacks the GPU-step → grid-oscillation pain at the source; institutionalized by NVIDIA's power-smoothing spec; strong control-IP moat.
5. **PWR-07 — Superconducting MVDC Campus Busway.** The frontier flagship — when campuses hit multi-GW, HTS is the only way past the copper/loss/footprint ceiling; multiple Q1 peer-reviewed anchors and real field demos.

---

## 6. CSV-Ready Candidate Rows

```csv
candidate_id,candidate_name,one_sentence_product,system_boundary_shift,extreme_metric,first_customer,buyer_title,pain,current_workaround,why_current_fails,hardware_stack,software_control_stack,prototype_path_2026_2028,china_wedge,us_wedge,cleanroom_dependency,capex_band,reg_export_risk,competitors,defensibility,kill_criteria,evidence_status,key_sources
PWR-01,AI-Factory MV-to-800VDC Solid-State Power Core,"Single/two-stage solid-state core converting MV AC to regulated 800VDC at 1-5MW per skid","Collapses 5 conversion stages to 1-2 with grid-forming behavior",">98.5% efficiency; 3-5x density; sub-ms ride-through",Hyperscaler/neocloud 800VDC halls,VP Data Center Energy & Power Engineering,"Legacy AC chain wastes 12-15% and cannot serve 1MW racks","MV transformer + line-freq UPS + rectifiers + 800V sidecar","Multi-stage loss/footprint; no fast fault control or transient buffering","SiC MV stacks; MF transformer; 800VDC stage; liquid cooling; SS protection","MMC control; grid-forming impedance; transient feed-forward; digital twin","2026 1MW skid demo; 2027 2MW field pilot; 2028 5MW line","Aligns to domestic 800VDC standard + SiC/magnetics supply","Hyperscaler 800VDC roadmaps + interconnect pressure",None (buy SiC die; assemble),High,"SiC/grid-control export; MV-DC standards maturing","Delta(Panama);Schneider;ABB;Eaton;Vertiv;Navitas/EPFL","Magnetics+MV control+thermal co-design; field reliability; standards seat","Hyperscalers keep separate MV-UPS+rectifier; field gains <10%",CLEARED_WITH_WEAKNESS,"PWR-S01;PWR-S17;PWR-S26;PWR-S28"
PWR-02,Microsecond 800VDC Solid-State Breaker / e-Fuse,"Bidirectional SiC/GaN DC breaker+e-fuse for 800-1000VDC busways with selectivity","Protection from ms mechanical to us semiconductor interruption","<1-10us interruption at 800-1000VDC; multi-kA; <0.5% loss",800VDC busway OEM / hyperscaler facilities,Director Power Distribution Engineering,"800VDC has no current zero; faults arc-flash before AC breakers react","Hybrid mechanical breakers/fuses/AC-side protection","Si IGBTs too slow; breakers/fuses lack selectivity & reset speed","SiC JFET/MOSFET or GaN array; TVS/MOV/active clamp; sensing; gate drive","di/dt+threshold detection; adaptive trip; selective coordination; soft turn-off","2026 800V/2kA module; 2027 zone-selective busway; 2028 UL/IEC product","Domestic SiC + AIDC DC standardization pull","800VDC safety/standards gap is explicit blocker; ABB validating",None,Med,"SiC export; UL489-DC/IEC arc standards settling","ABB(SACE Infinitus);Infineon;Eaton;Littelfuse;Atom Power","Energy-absorption+selectivity firmware; qualification data","Hyperscalers stay at 400VDC with conventional protection",CLEARED,"PWR-S18;PWR-S19"
PWR-03,Rack Transient Buffer / Power-Smoothing Energy Interface,"Rack hybrid buffer (supercap+film cap+fast DC-DC) absorbing GPU load steps","Active power-shaping layer decoupling compute from power dynamics",">=400J/GPU (~28.8kJ/rack) in us; ~25% peak-current cut",GPU rack/power-shelf OEM,Chief Engineer Rack Power Architecture,"Spiky synchronized GPU load stresses PSUs and propagates grid oscillation","Oversized PSUs; firmware power-capping; software smoothing","Software smoothing wastes compute; caps alone too little energy; BBUs too slow","Hybrid supercap; high-temp film caps; bidirectional SiC/GaN DC-DC; sensing","Predictive feed-forward from GPU telemetry; droop/virtual-impedance; SOC mgmt","2026 shelf demo; 2027 full-rack ODM; 2028 hall pilot w/ grid verification","Domestic supercap + AIDC scale; pairs Panama cores","NVIDIA power-smoothing spec institutionalizes requirement",None,Med,Low-moderate (storage UL/transport),"Capacitech;Panasonic;KEMET/TDK;Vertiv","Predictive control co-designed w/ GPU telemetry; OEM lock-in","GPU vendors solve smoothing in firmware + on-package caps",CLEARED,"PWR-S04;PWR-S15;PWR-S27"
PWR-04,Campus Power-Shaping Buffer (Grid-Hiding GFM + Hybrid Storage),"MW-scale hybrid storage + grid-forming converter making AI campus load smooth to grid","Volatile GW load looks like constant dispatchable grid-forming resource","Suppress +-100s MW second-min swings; GW grid-forming damping",AI DC developer / utility,Head of Power Procurement & Grid Interconnection,"Utilities throttle/delay interconnect due to volatile AI load + oscillations","Curtail load; overbuild firm gen; passive ride-through","Diesel/gas cannot follow ms-s dynamics; software wastes compute; GFL BESS no stabilization","MW SiC GFM converter; hybrid storage (Li-ion+supercap/flywheel); MV interface","GFM/VSM control; active oscillation damping; ramp governor; utility dispatch API","2026 1MW testbed on AI traces; 2027 10-50MW pilot; 2028 utility product","State grid + west-cluster renewable surplus alignment","FERC 2025 PJM order + DOE/PNNL oscillation findings",None,High,"Interconnect rules in flux; grid-control export","Tesla Megapack;Fluence;Hitachi Energy;Emerald AI(sw)","GFM control validated on real AI dynamics + utility certification","FERC/ISO accept software ramp-limits+firm gas as sufficient",CLEARED,"PWR-S02;PWR-S04;PWR-S05;PWR-S09"
PWR-05,Behind-the-Meter Grid-Forming Microgrid Controller+Hardware,"GFM control+protection platform letting BTM gas/SOFC+storage island an AI campus","Data center from grid-dependent load to self-forming microgrid","Black-start/stabilize 100-500MW island; sub-cycle fault; seamless re-sync",BTM power developer / neocloud,VP Energy / Microgrid Engineering Lead,"~5yr interconnect; generation must island reliably or campus trips","Ad-hoc genset paralleling + utility relays","Synchronous-genset controls + GFL inverters cannot stabilize low-inertia AI microgrid","GFM controllers; fast relays; MV paralleling interface; storage interface","VSM+droop; islanding/anti-islanding; protection coordination; re-sync","2026 controller+HIL; 2027 multi-MW field microgrid; 2028 100MW+ island","Distributed prime-power + microgrid policy; domestic inverters","Bloom/gas BTM deals scaling; controller is missing stabilization layer",None,High,"Air-permit/interconnect; grid-control export","Caterpillar/Cummins;PowerSecure;GE Vernova;Schneider","GFM+protection co-design for inverter-dominant AI loads; certification","Hyperscalers default to grid-parallel gas; no islanding needed",CLEARED_WITH_WEAKNESS,"PWR-S02;PWR-S09;PWR-S30"
PWR-06,Medium-Frequency Transformer / HF Magnetics Engine,"MF (5-50kHz) high-isolation transformer+integrated-cooling magnetics module for SST cores","Magnetic element productized as the SST design-limiting engine",">10kW/L at >99.3% transformer eff; PD-free at 10-25kV isolation",SST/800VDC core makers + EV charging OEMs,Director Power Magnetics / Power Electronics R&D,"MFT dominates SST size/loss/insulation/cost; no merchant supply","Bespoke per-team transformers w/ legacy tools","Coupled E/M/dielectric/thermal limits; std cores fail MV-DC reliability","Nanocrystalline/amorphous/ferrite cores; litz/foil; advanced insulation; integrated cooling","Multiphysics design-optimization toolchain; digital-twin loss/PD model","2026 100kW/10kHz module; 2027 MV 250kW-1MW family; 2028 design-ins x2","Dominant nanocrystalline/amorphous ribbon + magnetics base","Merchant high-reliability MV magnetics is a gap; sell to all",None (winding/potting/test),Med,Low (some dual-use),"Proterial/Hitachi Metals;Payton;Vacuumschmelze;in-house","Multiphysics toolchain + PD-free MV insulation + qualified library","Incumbents keep magnetics in-house; no design wins",CLEARED,"PWR-S16;PWR-S17;PWR-S29"
PWR-07,Superconducting MVDC Campus Busway,"REBCO HTS DC busway carrying 10s kA at MV across GW campus near-zero loss","Copper MV/LV busbar replaced by ultra-high-current-density superconducting spine","Je ~150-300 kA/cm2 (20K); loss ~1.7% of AC; multi-kA cable",GW-scale AI campus developer,Director Campus Power Infrastructure,"Distributing 1-5GW needs enormous copper/land; losses force many substations","Many parallel copper feeders + distributed substations","Copper hits ampacity/weight/loss limits; cannot scale to multi-GW dense campus","REBCO tape cable; cryostat; cryocooler/LN2; current leads; terminations","Quench detection/protection; cryo plant control; HVDC fault coordination","2026 10-50m loop; 2027 100-200m substation-to-hall; 2028 campus spine","Domestic REBCO tape + 35kV/1.2km HVDC HTS precedent + GW pipeline","GW campuses make copper/land math favor HTS; pairs with HVDC",None (buy HTS tape),Very High,"HTS/cryo dual-use export; novel MVDC approval","Nexans;Sumitomo;LS Cable;VEIR;SuperNode;Shanghai Superconductor","Systems integration (cable+cryostat+quench+converter) + reliability data","Cryo BOP never beats distributed copper on $/MW-delivered",CLEARED,"PWR-S12;PWR-S13;PWR-S14"
PWR-08,Cryogenic GaN Power-Electronics Module,"GaN converter module engineered to operate at 77K toward 20K co-located with SC machines","Power conversion moves inside the cold environment","~5x Ron reduction; ~30% lower loss at cryo; MW-class drives",Electrified-aircraft propulsion + SC machine builders,Chief Engineer Electric Propulsion / SC Machines,"SC motors need cold drive electronics; warm electronics add heat leak/weight","Room-temp inverters w/ long cryo leads; large thermal mass","SiC degrades at cryo; warm electronics impose heat-leak/specific-power penalty","Cryo-rated GaN HEMTs; cryo gate drive/passives; low-leak packaging; cold plate","Cryo device models; temp-adaptive control; quench/over-temp protection","2026 <100kW cryo GaN at 77K; 2027 MW brassboard; 2028 SC machine demo","CAS SC machine programs + domestic GaN + aviation push","NASA HEMM/cryo-inverter heritage + defense/eVTOL pull",None (GaN die; cryo packaging lab),High,"ITAR/EAR aerospace; GaN export","NASA teams;GE Aerospace;Airbus UpNext;Rolls-Royce","Cryo characterization+packaging IP + machine co-design","SC machines stall commercially; no near-term host",CLEARED_WITH_WEAKNESS,"PWR-S07;PWR-S22"
PWR-09,Superconducting Fault-Current Limiter for Dense Nodes,"REBCO resistive SFCL limiting fault current instantly at congested MV/DC nodes","Passive near-instant current limiter raising node short-circuit capacity","Sub-ms limitation; ~50ms ride-through; seconds recovery; zero normal loss",Navy/shipboard MVDC; dense DC substations; utilities,Director Shipboard Power Systems / Substation Engineering,"Adding gen/load raises fault current beyond switchgear; full upgrade costly","Series reactors; bus splitting; switchgear replacement","Reactors add loss; switchgear swap costly; neither as fast/transparent","REBCO coils/modules; cryostat+cryocooler; fault-energy mgmt; recovery control","Quench/recovery monitoring; relay coordination","2026 lab MV module; 2027 ship/microgrid demo; 2028 fielded node","Domestic REBCO + state-grid SFCL demo history","Navy MVDC + dense substations; AMSC/Siemens prior validation",None (HTS tape procured),High,"HTS dual-use; defense procurement","Faraday/AMSC heritage;SuperOx;Nexans","Recovery+fault-energy mgmt + qualification; defense ties","SiC solid-state FCLs win on cost/footprint w/o cryo",CLEARED_WITH_WEAKNESS,"PWR-S24;PWR-S12;PWR-S20"
PWR-10,High-Power-Density Flywheel Ride-Through,"Kinetic buffer for sub-second to 10s-second AI ride-through + frequency support","Splits backup into kinetic high-power layer vs separate energy layer","<4s response; MW injection; effectively unlimited cycle life",AI DC critical-facilities + BTM microgrids,Director Critical Power / Energy Storage,"Battery BBUs degrade under AI high-cycle transient duty and oversized","Oversized Li-ion BBUs cycled hard; limited supercaps","Batteries wear/thermal-runaway under cycling; supercaps cannot cover 10s s","Composite/steel rotor; magnetic bearings; vacuum housing; bidirectional SiC drive","GFM/frequency-response control; charge scheduling; bearing/vacuum monitoring","2026 1MW unit; 2027 hall integration; 2028 campus frequency reference","Domestic flywheel manufacturing scaling for frequency regulation","Sandia/DOE flywheel precedent; AI transient duty fit",None,Med-High,Low,"Amber Kinetics;Piller;Beacon heritage;Energiestro","Bearing/rotor + GFM drive integration; AI-transient control","Supercap+battery hybrids dominate transient duty cheaper",CLEARED_WITH_WEAKNESS,"PWR-S10;PWR-S11"
PWR-11,Solid-State MV Interconnect Bay,"Solid-state MV bay (static transformer+SS tap/breaker) giving utilities dynamic flow control","Passive substation bay becomes active controllable solid-state node","Dynamic balancing+fault-limiting+voltage reg in one bay; unlock grid headroom",T&D utility serving large DC loads,Director Transmission/Substation Engineering,"~5yr queues; substations cannot dynamically manage volatile large loads","Transformers + mechanical tap changers + reactors; new lines","Passive gear cannot control flow/fault current; upgrades slow/capital-heavy","SiC MV converter; solid-state tap changer; integrated breaker/limiter; transformer","Power-flow/voltage control; fault-current limiting; ISO dispatch interface","2026 SS tap/limiter demo; 2027 feeder pilot; 2028 utility bay at DC interconnect","State grid flexible-substation programs + domestic SiC","DOE FITT/GRIP funds SST/tap-changer; FERC interconnect pressure",None,High,"Grid-asset certification; SiC export","GE Vernova;Resilient Power Systems;Hitachi Energy;Smart Wires","Utility qualification + control IP + DOE-backed demos","Utilities reject power-electronic substations; stick to copper",CLEARED,"PWR-S03;PWR-S02;PWR-S01"
PWR-12,Megawatt Charging Power Core,"Solid-state MV-to-DC charging core delivering 1-3.75MW per port (MCS) for HD EV depots","AI-factory MV-DC core brought to the charging plug",">95% eff at MW; 1250V/3000A per port; switching-matrix allocation",Fleet/depot operator + charging network,Director Fleet Electrification / Charging Infrastructure,"MCS needs multi-MW per stall grid-friendly; conventional bulky/lossy","MV transformer + parallel DC chargers + separate buffering","Multi-stage conversion inefficient/large; cannot smooth/share power","SiC MV SST front end; isolated DC-DC; switching matrix; liquid MCS interface; buffer","ISO 15118-20 plug-charge; dynamic power allocation; peak-shaving","2026 1MW bench; 2027 depot pilot 2-3MW ports; 2028 multi-port grid-interactive","Largest EV-truck/charging market + domestic SiC + MV-DC std","MCS standard finalizing; freight corridors; shares engine w/ PWR-01",None,Med-High,"Charging standards; SiC export","ABB;Heliox;Kempower;Alpitronic;Chinese MCS makers","Shared MV-DC core economics + grid-interactive control","MCS rollout stalls; buyers prefer commodity AC chargers",CLEARED_WITH_WEAKNESS,"PWR-S08"
PWR-13,MVDC Electric-Ship Power & Protection System,"Integrated MVDC shipboard distribution + ultra-fast DC protection for all-electric ships","AC ring bus to fault-managed MVDC integrated power system","Selective sub-ms DC fault clearing across modes; high density for pulsed loads",Naval shipbuilder / Navy power program,Program Manager Shipboard Integrated Power Systems,"Warships need MVDC for density/pulsed loads but DC fault protection unsolved","MVAC distribution + conventional breakers","AC cannot meet density/pulsed needs; std breakers too slow for MVDC faults","MVDC bus; SiC DC breakers/limiters; converter modules; energy buffers","Fault detection/management; mode coordination; failure-mode power mgmt","2026 protection testbed; 2027 shore IPS demo; 2028 vessel demonstrator","PLAN electrification (sovereign-only lane)","US Navy MVDC roadmap; defense funding",None,High,"Heavy ITAR/defense controls","GE Vernova;L3Harris;BAE;Leonardo DRS;ABB Marine","Defense qualification + DC-protection IP","Navy delays MVDC; primes keep in-house",CLEARED,"PWR-S20;PWR-S21"
PWR-14,eVTOL/eAircraft HV Power-Distribution + SS Protection Unit,"800-1000V HV distribution + fast solid-state protection for electrified aircraft","Relay-based aircraft power distribution to lightweight solid-state core","800V class at high kW/kg; sub-ms fault isolation; fail-operational",eVTOL / electric-aircraft OEM,Chief Engineer Electrical Power Systems,"Flight power must be light/redundant/fault-isolating at 800V w/ arcing risk","Contactor/relay distribution + fuses","Mechanical protection heavy/slow for HV DC arcs; misses weight+fail-op","SiC/GaN solid-state power controllers; HV bus; sensing; lightweight packaging","Fault detection/isolation; load mgmt; redundancy logic; DO-160/254 design","2026 800V SSPC unit; 2027 iron-bird w/ OEM; 2028 flight-test HW","Large eVTOL OEM base (EHang/XPeng AeroHT) + domestic WBG","Joby/Archer/Beta certification pipelines; defense",None,Med-High,"Aviation cert + ITAR/EAR defense","Astronics;Safran;Honeywell;GE Aerospace","Certified lightweight solid-state protection IP; sticky design-ins","eVTOL timelines slip; OEMs keep distribution in-house",CLEARED_WITH_WEAKNESS,"PWR-S07"
PWR-15,LDES Power-Conversion + Balance-of-Plant Skid,"Low-cost bidirectional PCS+BOP skid built for 100h LDES where $/kW dominates","Optimizes the power layer separately from the energy layer for ultra-long LDES","PCS+BOP at fraction of BESS $/kW; multi-day dispatch",LDES project developer / utility,Director Storage Project Engineering,"LDES economics live on BOP/PCS cost; today's PCS wrong-sized/overpriced","Repurposed BESS inverters + ad-hoc BOP","Short-duration PCS optimized for high P/E, not trickle long-duration","Right-sized bidirectional inverter; MV interface; thermal/air mgmt; skid","Multi-day dispatch optimization; GFM/ancillary; plant controller","2026 PCS+BOP skid spec; 2027 LDES developer pilot; 2028 utility plant","Massive LDES + renewable mandate; domestic inverter scale","First grid-connected iron-air + Form scale-up create pull",None,Med-High,"Interconnect; low export","SMA;Sungrow;Power Electronics SL;Form(in-house)","Chemistry-specific BOP optimization + GFM control; partner lock-in","LDES OEMs integrate BOP or std PCS good enough",CLEARED_WITH_WEAKNESS,"PWR-S23"
PWR-16,High-Temp DC-Link/Buffer Capacitor+Module for 15yr AI SLA,"High-temp polymer-dielectric DC-link/buffer cap+module for 800VDC cores at 15yr SLA","Capacitor from lifetime-limiting weak link to reliability backbone",">600V/um headroom; ~15+yr life at DC humidity/temp; us transient response",800VDC power-core/power-shelf OEM,Director Power Electronics Component Engineering,"Electrolytics wear out ~6-8yr; films struggle w/ AI temp/humidity+transient duty","Over-provision electrolytic/film caps; replacement cycles","Electrolytic wear-out/humidity; std films miss thermal+transient+SLA envelope","High-temp polymer/nanocomposite film; metallization; self-healing; low-ESR module","Embedded condition monitoring / remaining-life (changes maintenance)","2026 dielectric+cap w/ accel-life; 2027 module qualified; 2028 design-ins+field","Dominant film-cap manufacturing base; cost+scale","Reliability-critical AI SLA + advanced-dielectric IP wedge",None (film/metallization line),Med-High,Low (material IP),"TDK;KEMET/Yageo;Vishay;PeakNano","Dielectric material + module reliability data + design-ins","Incumbents close high-temp film gap; buffering moves to supercaps",CLEARED,"PWR-S15;PWR-S26"
PWR-17,China-First 800VDC AIDC Power Core,"Fully domestic MV-to-800VDC AIDC core optimized for 东数西算 west clusters","Same MV-DC boundary shift localized for China standard/supply/renewables","~98.5% MV-to-800VDC at multi-MW; prefab hot-swap modular",Chinese hyperscaler (Alibaba/Tencent/ByteData),Head of Data Center Power Architecture (China cloud),"West clusters need rapid prefab high-density grid-friendly power","Delta/Alibaba Panama MV-DC + domestic HVDC maturing to 800V","Panama/HVDC early on 800V, grid-forming, integrated buffering","Domestic SiC MV stacks; nanocrystalline magnetics; 800VDC; protection+buffer","GFM control for renewable clusters; prefab commissioning tooling","2026 cabinet demo vs white paper; 2027 west-cluster pilot; 2028 rollout","Policy tailwind (东数西算/green mandate) + domestic supply + std momentum","Limited; license to allied markets but export-constrained",None (domestic SiC),High,"Reverse export risk (US SiC/EDA); favored if domestic","Delta;Huawei Digital Power;Envicool;Kehua;SuperX;Sungrow","Standard alignment + domestic supply + renewable GFM control; policy moat","Huawei/Delta capture standard and lock cabinet market first",CLEARED_WITH_WEAKNESS,"PWR-S25;PWR-S26;PWR-S01"
PWR-18,Active Wide-Area Oscillation Damper for DC Grids,"Fast PMU-driven power-electronic device actively cancelling AI-DC grid oscillations","Oscillation monitoring becomes closed-loop active damping hardware","Detect-and-damp ~14-15Hz and lower DC modes within cycles; wide band",ISO/utility + large DC operator at PCC,Director Grid Stability / Transmission Operations,"AI loads induce sustained measurable oscillations threatening stability","PMU monitoring + manual mitigation / curtailment","Monitoring passive; generator PSS not tuned for inverter-load oscillations","Fast MW converter (w/ storage/STATCOM); PMU sensing; MV interface","Real-time oscillation detect + wide-area damping; GFM coordination","2026 HIL+lab damping on recorded modes; 2027 substation pilot; 2028 ISO product","State grid stability programs + dense AI clusters","PNNL/DOE/NERC formalized problem; FERC pressure for active fix",None,Med-High,"Grid-control export; ISO certification","Hitachi Energy;GE Vernova;Mitsubishi;Smart Wires","Wide-area damping control IP validated on real DC modes; ISO cert","GFM converters (PWR-04) absorb function; no standalone market",CLEARED,"PWR-S04;PWR-S05;PWR-S06"
PWR-19,MV Isolated Gate-Driver & Stack-Control Platform,"High-isolation high-dv/dt gate-driver + modular stack-control for series MV SiC","Productizes the MV series-stack control+isolation layer","Multi-kV isolation; >100kV/us CM immunity; sub-ns sync; integrated protection",SST/SSCB/MV-converter makers,Director Power Electronics Design,"Series-stacking SiC at MV plagued by imbalance/dv-dt faults/isolation breakdown","Custom in-house gate drives + isolation; low yield","Off-the-shelf drivers lack MV isolation/timing/protection; bespoke no scale","Reinforced-isolation driver; isolated power/signal; active balancing; desat protection; controller","Sync+balancing firmware; fault mgmt; topology-configurable","2026 MV stack gate-drive reference; 2027 design-ins x2; 2028 qualified platform","Domestic SiC ecosystem needs control layer; sell to all","Merchant MV stack-control is a real gap; arms dealer",None,Low-Med,Some MV power-control IP sensitivity,"Power Integrations;Infineon;TI;Analog Devices","Isolation+balancing+protection IP + reliability library; lock-in","Chip vendors integrate full MV stack control on-die",CLEARED_WITH_WEAKNESS,"PWR-S17;PWR-S16;PWR-S18"
PWR-20,Last-Inch 800VDC-to-Core Vertical Power Module,"High-density module stepping 800VDC toward GPU core voltage with vertical/in-package delivery","Final step-down from board-edge to vertical under-die delivery","100s A at sub-V rails minimized PDN loss; supports 1MW rack densities",Accelerator/board OEM + rack-power architect,Principal Engineer Power Delivery Network,"At 1MW/rack last-inch IR loss+copper dominate; lateral cannot supply density","Lateral multiphase VRMs at board edge; massive copper planes","Lateral delivery too much R/L at these currents; copper/loss explode","Vertical power module (integrated magnetics+WBG/Si); advanced substrate; co-packaged","Fast multiphase control; transient co-tuned w/ PWR-03","2026 module demo; 2027 board OEM co-design; 2028 accelerator integration","Domestic packaging + power IC; AIDC scale","Tied to NVIDIA-class roadmaps; advanced packaging partners",Moderate (advanced packaging via OSAT),Med-High,"Advanced-packaging export controls","Infineon;Vicor;Monolithic Power;Empower;TI","Vertical-delivery + integrated-magnetics IP + accelerator co-design","Chip vendors fully integrate on-package power delivery",CLEARED_WITH_WEAKNESS,"PWR-S26;PWR-S15"
PWR-21,HTS Cable Cryostat & Cryogenic Balance-of-Plant,"Modular cryostat+cryocooling BOP making HTS power links/busways deployable+serviceable","Cryogenic BOP productized as standardized subsystem","Low-heat-leak 20-77K over 100s m; serviceable cryocoolers; multi-yr MTBF",HTS cable/busway integrators + fusion/magnet programs,Director Cryogenic Systems,"Cryo BOP is the cost/risk driver stalling superconducting power adoption","Custom cryostats + lab cryocoolers per project","Bespoke cryo BOP expensive/unreliable/not field-serviceable; no merchant std","Vacuum cryostat; redundant cryocoolers/subcooled LN2; current leads; quench protection","Cryo plant control; quench detection; predictive maintenance","2026 cryostat+cooling skid; 2027 HTS busway integration; 2028 field reliability","Domestic cryocooler+HTS ecosystem; HTS cable precedent","Fusion + DC HTS demand; picks-and-shovels to HTS sector",None,High,"Cryo/HTS dual-use export","Sumitomo;Cryomech;Linde;Air Liquide;Nexans","Reliability+serviceability engineering + standardized interfaces","HTS power stays niche; cryo BOP volume never materializes",CLEARED_WITH_WEAKNESS,"PWR-S12;PWR-S13;PWR-S22"
PWR-22,Prime-Power Island Inverter/Paralleling Controller for SOFC+Gas,"Power-conditioning+paralleling inverter+controller turning SOFC/gas into GFM prime-power island","SOFC/gas DC output becomes dispatchable grid-forming source","Parallel 10s-100s MW SOFC w/ GFM stability + transient support",BTM SOFC/gas power developer,VP Power Systems / Generation Engineering,"SOFC/gas scaling for AI prime power but conditioning+paralleling+GFM unsolved","Standard grid-following inverters + utility backbone","GFL inverters cannot form stable island/follow AI transients; SOFC ramp slow","SiC GFM inverter; DC bus conditioning; storage/buffer interface; MV paralleling","GFM+droop; fleet paralleling; transient buffering coordination; dispatch","2026 inverter+controller on SOFC stack; 2027 multi-MW island; 2028 100MW+","Domestic SOFC+inverter; distributed-energy policy","Bloom/Brookfield/AEP/AWS SOFC deals (1+GW) need conditioning+GFM",None,High,"Air-permit/interconnect; grid-control export","Bloom(in-house);SMA;Power Electronics SL;GE Vernova","GFM+fleet-paralleling control validated for fuel-cell prime power","SOFC makers vertically integrate inverter/controller",CLEARED_WITH_WEAKNESS,"PWR-S09;PWR-S30;PWR-S02"
PWR-23,Prefab Mobile MV Power-Island Skid,"Factory-built truckable MV power-island skid energizing AI sites in months pre-commissioned","Grid-connection from multi-year project to deployable relocatable product","Energize multi-MW in months vs ~5yr queue; relocatable; standardized",Neocloud / DC developer racing grid timelines,Head of Site Energization / Speed-to-Power,"Interconnect queues (~5yr) gate revenue; need power now on own terms","Diesel rental fleets + ad-hoc switchgear","Rental diesel emissions/permit-limited and not grid-forming; bespoke slow","Containerized MV-DC core; solid-state protection; GFM converter; gen/storage interface","Plug-and-play commissioning; GFM/islanding; remote ops","2026 single-skid demo; 2027 speed-to-power deployment; 2028 relocatable fleet","Prefab modular DC culture + fast deployment + domestic supply","FERC/DOE interconnect crisis + BTM generation rules; #1 buyer pain",None,High,"Air-permit (if gas); interconnect on re-sync","VoltaGrid;ProEnergy;Caterpillar;Aggreko;Cummins","Integration of PWR-01/02/04 into deployable product + commissioning speed","Interconnect reform collapses queue; speed-to-power premium vanishes",CLEARED,"PWR-S02;PWR-S01;PWR-S30"
PWR-24,MV Grid-Forming SST for LDES/Renewable Hybrid Plant,"MV grid-forming SST interconnecting co-located renewables+LDES+load as one GFM hybrid","Hybrid-plant inverter/transformer/controller chain collapsed into one GFM SST node","Single MV node GFM + bidirectional MV-DC + >98% eff",Renewable+storage IPP / hybrid-plant developer,Director Hybrid Plant Engineering,"Hybrid plants need many converters+transformers+controllers; not grid-forming","Separate PV/wind inverters + BESS PCS + transformers + plant controller","Multi-box integration lossy/slow/grid-following; cannot firmly serve volatile load","MV SiC SST; multiport DC interface (PV/wind/storage); GFM output; protection","GFM control; multiport energy mgmt; hybrid dispatch","2026 multiport MV SST; 2027 hybrid pilot; 2028 GFM hybrid serving DC load","West-cluster renewable+LDES mandate; domestic SiC/inverters","BTM co-location (FERC) + LDES scale-up; firm-clean demand",None,High,"Interconnect; SiC/control export","SMA;Sungrow;Hitachi Energy;GE Vernova;Power Electronics SL","Multiport GFM SST IP + hybrid control; shares engine w/ PWR-01/06","Multi-box hybrids stay cheaper; GFM SST never pays off",CLEARED_WITH_WEAKNESS,"PWR-S17;PWR-S09;PWR-S23"
```

---

## 7. CSV-Ready Evidence Ledger Rows

```csv
source_id,worker,source,source_type,impact_or_authority,quartile_or_venue,supports_claim,evidence_status
PWR-S01,PWR,"IEA Energy and AI / Energy demand from AI (iea.org, 2025)",authoritative_non_article,international_agency,NA,"DC electricity ~doubles to ~945 TWh by 2030; US+China ~80% growth; 20% projects at grid risk",CLEARED
PWR-S02,PWR,"FERC order on PJM large-load / co-location interconnection (Dec 18 2025)",authoritative_non_article,us_regulator,NA,"Interconnection binding constraint; BTM generation + co-location rules; load volatility",CLEARED
PWR-S03,PWR,"DOE Office of Electricity FITT/GRIP solid-state transformer & SiC packaging awards",authoritative_non_article,us_national_program,NA,"Solid-state transformer / static substation funding (GE Vernova; Resilient Power Systems)",CLEARED
PWR-S04,PWR,"PNNL/NASPI Measurement Adequacy for Monitoring Data Center Oscillations",authoritative_non_article,national_lab,NA,"Data centers induce sustained measurable grid oscillations",CLEARED
PWR-S05,PWR,"DOE OE Monitoring Oscillations from Large Data Centers",authoritative_non_article,us_gov,NA,"Oscillation problem formalized; AI loads to multi-GW",CLEARED
PWR-S06,PWR,"NERC draft Power System Oscillation Monitoring and Mitigation TRD",authoritative_non_article,reliability_org,NA,"Need active oscillation mitigation not just monitoring",CLEARED
PWR-S07,PWR,"NASA NTRS/Glenn HEMM (16 kW/kg) & cryo MW inverter (18 kVA/kg)",authoritative_non_article,gov_research_lab,NA,"Cryo/superconducting machine + cryo power electronics metrics",CLEARED
PWR-S08,PWR,"DOE/OSTI Megawatt Scale Charging System Architecture",authoritative_non_article,national_lab,NA,"MCS architecture; MW-class DC charging power electronics",CLEARED
PWR-S09,PWR,"DOE Specifications for Grid-forming Inverter-Based Resources v1",authoritative_non_article,us_gov_spec,NA,"Grid-forming requirements definition",CLEARED
PWR-S10,PWR,"Sandia flywheel frequency-regulation reports",authoritative_non_article,national_lab,NA,"Flywheel fast frequency response; high-cycle duty",CLEARED
PWR-S11,PWR,"DOE/Beacon grid-scale flywheel storage plant report",authoritative_non_article,us_gov,NA,"Flywheel grid-scale ride-through/frequency support",CLEARED
PWR-S12,PWR,"Superconductor Science and Technology 2026 39(2) 023501 (DOI 10.1088/1361-6668/ae15c2)",peer_reviewed_academic,high_impact,Q1_Q2_IOP,"HTS cable roadmap; Je 150-300 kA/cm2 at 20K; field demos incl Shanghai 35kV/1.2km HVDC",CLEARED
PWR-S13,PWR,"Applied Energy 2022 310:118602 (DOI 10.1016/j.apenergy.2022.118602)",peer_reviewed_academic,high_impact,Q1_Elsevier,"Superconducting delivery to 100-MW data center; loss ~1.7% of conventional AC",CLEARED
PWR-S14,PWR,"Energy (Elsevier) 2022 pii S036054422200723X",peer_reviewed_academic,high_impact,Q1_Elsevier,"Superconducting DC busbar networks for 10MW data center; loss/economics",CLEARED
PWR-S15,PWR,"Wang & Blaabjerg IEEE Trans Industry Applications 2014 50(5):3569-3578 (DOI 10.1109/TIA.2014.2308357)",peer_reviewed_academic,high_impact,Q1_IEEE,"DC-link capacitor reliability dominates converter failure; electrolytic wear-out",CLEARED
PWR-S16,PWR,"Mogorovic & Dujic MFT design optimization & experimental verification IEEE Trans Power Electronics",peer_reviewed_academic,high_impact,Q1_IEEE,"MFT is SST design-limiting engine; multiphysics optimization; PD-free MV",CLEARED
PWR-S17,PWR,"Huang et al Medium-Voltage Solid-State Transformer IEEE Industrial Electronics Magazine 2016 (doc 7575787)",peer_reviewed_academic,high_impact,Q1_IEEE,"MVSST architecture for smarter/resilient grid",CLEARED
PWR-S18,PWR,"Self-powered ultra-fast DC SSCB normally-on SiC JFET IEEE APEC (doc 7104436)",peer_reviewed_conference,flagship_conference,peer_reviewed_conference_no_jif,"Sub-us SiC fault interruption at 400V",CLEARED
PWR-S19,PWR,"SiC MOSFET solid-state circuit breaker motor control center IEEE journal (doc 10816147, 2024)",peer_reviewed_academic,high_impact,Q1_Q2_IEEE,"SSCB soft-start/soft-turn-off design at MV",CLEARED
PWR-S20,PWR,"All-electric ship MVDC power-electronics review Electric Power Systems Research 2017 pii S0142061517300595",peer_reviewed_academic,moderate_high,Q1_Q2_Elsevier,"MVDC shipboard distribution + DC protection needs",CLEARED
PWR-S21,PWR,"MVDC shipboard design specs/requirements review Electric Power Systems Research 2018 pii S0142061518302680",peer_reviewed_academic,moderate_high,Q1_Q2_Elsevier,"MVDC ship design requirements (selectivity/speed)",CLEARED
PWR-S22,PWR,"Review of cryogenic power electronics iEnergy 2024 (DOI 10.23919/IEN.2024.0014)",peer_reviewed_academic,verify_percentile,newer_journal,"GaN improves at cryo ~30% lower loss; SiC degrades at cryo",CLEARED_WITH_WEAKNESS
PWR-S23,PWR,"Iron-energy nexus for LDES iScience (Cell Press) 2022 pii S2590332222001026",peer_reviewed_academic,high_impact,Q1_CellPress,"LDES scaling; BOP/power-layer cost drivers",CLEARED
PWR-S24,PWR,"SFCL functionality long-duration faults Energies (MDPI) 2025 18(19):5302",peer_reviewed_academic,verify_quartile,MDPI_verify_Q1_Q2,"REBCO SFCL fault-limiting behavior",CLEARED_WITH_WEAKNESS
PWR-S25,PWR,"China DC power demand & 800VDC policy (MIIT) via CNESA/Wood Mackenzie/IEA",authoritative_non_article_plus_triangulation,china_policy_plus_agency,NA,"China DC demand ~20->40GW 2024->2030; HVDC/DC push; 东数西算",CLEARED_WITH_WEAKNESS
PWR-S26,PWR,"NVIDIA 800VDC architecture; Schneider 1MW rack; Delta/Alibaba Panama + 800VDC white paper",company_claim,company_supported_only,NA,"800VDC direction; copper/loss math; MV-UPS + DC distribution",WATCH
PWR-S27,PWR,"IEEE Spectrum Gigascale AI datacenter power; Taming DC Power Fluctuation With AI UPS",journalism,timing_triangulation,IEEE_Spectrum,"ms load spikes; diesel/turbine cannot follow; UPS buffering",CLEARED_WITH_WEAKNESS
PWR-S28,PWR,"Navitas+EPFL 250kW single-stage SST 3.3kV->800VDC APEC 2026 demo",company_claim_plus_conference_demo,company_timing,NA,"Single-stage MV-to-800VDC SST feasibility",WATCH
PWR-S29,PWR,"OSTI Optimizing Insulation Design for Transformers in MV Power Conversion Systems",authoritative_non_article,national_lab,NA,"PD-free MV MFT insulation challenge",CLEARED
PWR-S30,PWR,"BTM SOFC/gas deals (Bloom/Brookfield/AEP/AWS) via Utility Dive / company filings",journalism_plus_company,timing_triangulation,NA,"BTM prime power scaling to >1GW",CLEARED_WITH_WEAKNESS
```

---

### Notes on evidence discipline

- No top-5 candidate rests its core technical or customer-pain claim solely on preprints, company claims, market reports, or weak journalism. Core anchors are peer-reviewed (IEEE TPEL/TIA/IEM, Applied Energy, Energy, Superconductor Sci. & Tech., iScience, Electric Power Systems Research) or authoritative non-article (IEA, FERC, DOE, PNNL, NERC, NASA, Sandia, OSTI).
- 800 VDC architecture direction (NVIDIA/Schneider/Delta) is treated as **company claim, triangulated** — never as independent proof. The underlying *pain* (load growth, copper/loss, grid volatility, interconnection delay) is anchored to IEA/FERC/DOE/PNNL/NERC.
- `verify` flags (PWR-S22, PWR-S24): journal percentile/quartile should be confirmed by the source auditor before either is used as a sole anchor; both currently support secondary candidates only.
- DOIs marked by `pii` (PWR-S14) could not be fully fetched (publisher 403); journal and identifiers are recorded as found in indexing results and should be re-confirmed at final audit rather than treated as verified DOIs.
