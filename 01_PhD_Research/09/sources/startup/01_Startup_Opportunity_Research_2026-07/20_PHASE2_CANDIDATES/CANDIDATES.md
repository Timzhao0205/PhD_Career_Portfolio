# PHASE 2 — CANDIDATE IDEAS (C01–C40)

Synthesized from the ten Phase-1 domain briefs (`10_PHASE1_LANDSCAPE/`). Citations `[S###]` refer
to `90_BIBLIOGRAPHY/sources.json` (each entry's `alt_ids` maps back to the per-domain ledgers).

**Diversity-rule compliance (checked at generation):**
- Standalone products/systems: 29/40 = 72.5% (≥50% required ✓)
- Test/measurement/diagnostic instruments: 11/40 = 27.5% (C21–C25, C30–C34, C40) (≤33% required ✓)
- Outside PhD thesis lane (GaN Hall sensing / fusion magnetic diagnostics): 37/40 = 92.5%
  (in-lane-adjacent: C30 magnetic current sensing, C31 magnetometry, C33 quench/current sensing) (≥50% required ✓)
- Every candidate names a high-end beachhead + expansion path, and both China and US entry angles.

Category tags: `[S]` standalone product/system · `[T]` test/measurement/diagnostic instrument.

---

## C01 — MW-class ruggedized SiC power-electronics building blocks (PEBBs) for marine, off-highway & defense integrators [S]

**Concept.** A catalog family of qualified, >100 W/in³ SiC power-stage building blocks (inverter/rectifier/DC-DC bricks, 50–500 kW each, stackable to multi-MW) sold to system integrators in niches the SST/charging gold-rush ignores: marine electrification, mining/off-road vehicles, mobile/backup MW power, directed-energy test infrastructure.
**Extreme edge.** Power density and ruggedization (shock/vibration/salt/thermal cycling) at levels catalog industrial drives don't reach; integrators buy a qualified power stage instead of an 18-month in-house design.
**Beachhead.** US Navy/ONR PEBB procurement and defense primes [S007]; dozens of marine-propulsion integrators; ASP $50–150K per building block.
**Expansion.** Off-road OEMs → mobile MW charging → microgrid converters.
**Frontier vision.** The "Vicor of megawatt electrification" — every niche MW system built from its bricks.
**HW/SW split.** HW power stage + gate-drive/protection firmware, digital control, fleet-config software.
**TRL/feasibility.** SiC modules, gate drivers, controllers all purchasable; v1 in 12–18 months. WBG device supply eases by 2029 [S001].
**Cleanroom dependence.** None (buys dies/modules).
**China angle.** Marine/inland-waterway electrification supply chains; local SiC substrate cost advantage [S017].
**US angle.** ONR/DoD PEBB programs and marine integrators; aviation-adjacent spec credibility [S007][S022].
**Founder fit.** Power electronics × harsh-environment packaging × embedded control — core capability graph.
**Sources.** [S007][S001][S022][S014]

## C02 — High-temperature WBG power-module packaging platform (licensable packaging + premium module line) [S]

**Concept.** Packaging/interconnect technology (sintered attach, high-Tg encapsulation, double-side cooling) that lets GaN/SiC modules run hotter and longer without derating — sold as a licensable platform plus a boutique line of extreme-temperature modules.
**Extreme edge.** Every WBG segment independently fights heat-flux/hot-spot limits that force derating or larger die, eroding WBG's density advantage [S015]; a packaging fix is a 10x-lifetime claim defensible with physics.
**Beachhead.** Custom-converter builders (defense, aviation-adjacent, downhole) who can't get >200°C-capable modules from catalog vendors; ASP $5–30K/module, license deals $100K+.
**Expansion.** Automotive/industrial module makers license the platform; converges with C27 (downhole) and C26 (space).
**Frontier vision.** The packaging standard for post-silicon power electronics.
**HW/SW split.** HW-dominant; SW = reliability modeling & digital-twin lifetime prediction tooling.
**TRL/feasibility.** Packaging lines are lab-scale equipment (vacuum reflow, sinter press), not a cleanroom; 18 months to qualified samples.
**Cleanroom dependence.** Low (buys bare dies; assembly is back-end).
**China angle.** License to Chinese module makers scaling SiC output [S017][S020].
**US angle.** DoD/NASA-adjacent qualification programs; IEEE ITRW roadmap names packaging the bottleneck [S130].
**Founder fit.** Direct: harsh-environment packaging + WBG device characterization are his PhD core.
**Sources.** [S015][S130][S001]

## C03 — Compact MW-class inverters for hybrid-electric marine & off-highway vehicles [S]

**Concept.** A full inverter/converter product (not just bricks) for hybrid-electric workboats, ferries, tugs, and mining/construction equipment: aviation-class kW/kg without the FAA gate.
**Extreme edge.** Aviation programs prove 19–20 kW/kg and ~99% efficiency is physically reachable [S022]; marine/off-highway buyers today get industrial drives at a fraction of that density. Bringing aviation-class density to an uncertified segment is the 10x.
**Beachhead.** Marine propulsion integrators and heavy-equipment OEMs electrifying under IMO/emissions pressure; hundreds of yards/OEMs globally; ASP $100–400K/system.
**Expansion.** Serial-hybrid gensets, port equipment, eventually certified aviation supply once volume exists.
**Frontier vision.** Electrified heavy transport powered by extreme-density conversion.
**HW/SW split.** HW inverter + control/monitoring software, remote fleet management.
**TRL/feasibility.** SiC modules at acceptable TRL; marine class-society certification (DNV/ABS) is months, not years. V1 by 2030 realistic.
**Cleanroom dependence.** None.
**China angle.** China's shipbuilding dominance + inland-waterway electrification push; founder's network for yard partnerships [S022].
**US angle.** Jones-Act fleet repowering, defense adjacent (USV power trains).
**Founder fit.** High-power-density power electronics (Rivas-group collaboration) directly on point.
**Sources.** [S022][S018][S021]

## C04 — Second-generation megawatt-charging (MCS) power modules for charger integrators [S]

**Concept.** High-density SiC power modules (350–500 kW bricks, liquid-cooled) sold to charging-network hardware integrators for the 2029 second-generation MCS replacement cycle — a component supplier, not a charging network.
**Extreme edge.** Beat incumbent module cost-per-kW and density once 8-inch SiC substrates reach cost parity (~2028) [S017]; first-gen 2026 MCS hardware will need denser, cheaper successors [S003].
**Beachhead.** Charger integrators (Alpitronic-class, plus second-tier) buying power stages; ASP $20–60K/module, thousands of units by 2030.
**Expansion.** Fleet-depot storage-buffered chargers; port/mine charging; overlaps C01 bricks.
**Frontier vision.** The power stage inside every MW charging point outside the BYD/Huawei walled gardens.
**HW/SW split.** HW module + charging-session control firmware, ISO 15118/MCS protocol stack.
**TRL/feasibility.** Straightforward integration play by 2029; standards (IEC TS 63379) already published [S003].
**Cleanroom dependence.** None.
**China angle.** Hard head-on (BYD/Huawei in-house [S004]); sell to second-tier Chinese integrators or export-focused OEMs.
**US angle.** MCS corridor buildout for heavy trucking, federal freight-electrification programs [S018].
**Founder fit.** Good power-electronics fit; weaker uniqueness vs. C01/C03.
**Sources.** [S018][S001][S003][S004]

## C05 — Compact pulsed-power & capacitor-discharge modules for directed-energy and industrial pulsed loads [S]

**Concept.** SWaP-optimized pulsed-power modules (capacitor banks + WBG switching + charging converters) for directed-energy test benches, EM launchers, pulsed lasers, and industrial pulse applications (magnetizers, EM forming).
**Extreme edge.** GaN/SiC switching plus engineered thermal/electromechanical capacitor management extends pulse-repetition life where legacy systems fail [S023]; Epirus's $250M DoD funding shows willingness to pay for compact pulsed power [S014].
**Beachhead.** DoD labs/primes (AFRL, ONR) and national-lab test infrastructure; ASP $80–500K/system; tens of buyers, deep budgets [S007].
**Expansion.** Fusion magnet pulse supplies (C10 adjacency), industrial EM processing, medical pulsed fields.
**Frontier vision.** Pulsed power as a compact catalog product rather than a facility.
**HW/SW split.** HW banks/switching + trigger-timing FPGA firmware, safety interlocks, waveform software.
**TRL/feasibility.** Component-integration play; ITAR-aware but sellable by 2029–2030.
**Cleanroom dependence.** None.
**China angle.** Effectively closed for defense use; industrial pulse-processing equipment only — plan US-first.
**US angle.** Strong: active ONR/AFRL funding pipelines [S007][S014].
**Founder fit.** Power electronics + instrumentation; less use of HTS/China assets.
**Sources.** [S023][S007][S014]

## C06 — Solid-state DC arc-fault & ground-fault protection modules for 800 VDC data centers [S]

**Concept.** Certifiable, field-replaceable solid-state DC breaker/protection modules (arc-fault detection integrated with sub-ms WBG interruption) for 800 VDC racks and busways.
**Extreme edge.** DC arcs don't self-extinguish; codes and products lag the 800 VDC rollout in both the US and China [S025][S040]. Sub-millisecond solid-state clearing at 800 V/kA class is a hard, physics-defensible spec no incumbent ships as a rack-level product [S223].
**Beachhead.** Hyperscaler/colo facility-electrical and EHS teams qualifying 800 VDC deployments from 2027 [S211]; ASP $5–25K/module at rack scale — thousands of units per campus.
**Expansion.** DC microgrids, marine/EV DC systems, solid-state switchgear line.
**Frontier vision.** The protection layer of the DC-electrified world.
**HW/SW split.** HW breaker + detection algorithms (the moat: arc-signature discrimination firmware), fleet analytics.
**TRL/feasibility.** SiC devices, current sensing, DSP all buyable; UL/IEC certification is the long pole — start 2027-class standards engagement early [S045].
**Cleanroom dependence.** None.
**China angle.** China's DC code still in draft = standards-shaping opportunity with ByteDance-class buyers [S040].
**US angle.** OCP qualification path; ERCOT-driven power-electronics scrutiny [S041].
**Founder fit.** WBG devices + precision sensing + firmware — strong; protection is a product, not a diagnostic.
**Sources.** [S223][S211][S045][S025][S040]

## C07 — High-cycle blind-mate 800 V busbar/connector system for AI racks [S]

**Concept.** Full-voltage-rated, high-current, high-mating-cycle blind-mate connectors and busway for monopolar 800 VDC racks.
**Extreme edge.** Contact reliability — low-mΩ rise under thermal cycling at 800 V/kA — is a materials/mechanical problem won by out-testing incumbents [S025].
**Beachhead.** One neocloud/colo rack OEM qualification; per-connector ASP at extreme volume; Amphenol's 33% AI-datacom share shows the prize [S035].
**Expansion.** OCP contribution → hyperscaler qualification → EV/industrial DC connectors.
**Frontier vision.** The contact physics standard for DC power delivery.
**HW/SW split.** HW-dominant; SW = qualification/test automation and per-connector traceability data.
**TRL/feasibility.** Buildable now; qualification cycles 12–18 months.
**Cleanroom dependence.** None.
**China angle.** Crowded (中航光电 etc. [S036]); position as US/EU-qualified alternative with China manufacturing.
**US angle.** Second-source pressure against Amphenol concentration [S035].
**Founder fit.** Moderate — electromechanical + test rigor, but little use of his rare-skill stack; flag for score-down on fit.
**Sources.** [S045][S211][S035]

## C08 — Rack-level hybrid supercapacitor + Li-ion transient power buffer for GPU clusters [S]

**Concept.** A drop-in "power shock absorber" module smoothing 30–70% sub-second GPU load swings so campuses can right-size transformers, gensets, and grid interconnects.
**Extreme edge.** Sub-millisecond response with engineered energy/cycle-life density; NVIDIA's own Kyber spec reserves ~65 J/GPU of storage, validating the architecture need [S033]; grid operators now mandate ride-through (ERCOT NOGRR282: sags to 0.20 p.u.) [S041].
**Beachhead.** Colo/neocloud operators without NVIDIA's in-house solution + UPS OEMs seeking a white-label module; ASP $15–60K/rack.
**Expansion.** Utility-facing ramp-rate compliance products; SMES upgrade path (C17); China 智算中心 buildout [S214].
**Frontier vision.** The buffering layer between bursty AI compute and slow grids.
**HW/SW split.** Power stage + supercap/Li-ion management, predictive load-following firmware (tight SW moat).
**TRL/feasibility.** All components COTS; control is the differentiator; v1 in 12 months.
**Cleanroom dependence.** None.
**China angle.** Active domestic suppliers — enter via licensing or a US-first record [S036].
**US angle.** ERCOT/NERC compliance pull from 2027–2028 [S041][S212].
**Founder fit.** Power electronics + control + embedded — strong.
**Sources.** [S212][S041][S214][S033][S037]

## C09 — Sub-1 MW transformerless MV-to-800 VDC power blocks for colo/edge retrofit [S]

**Concept.** Compact SiC medium-voltage-to-800 VDC conversion blocks (100 kW–1 MW) for smaller colos, enterprise AI clusters, and retrofits — the tier below the 5 MW+ SST startups' targets.
**Extreme edge.** Transformer lead times of 2–4 years and 45–95% price increases [S029] make a compact, fast-delivery MV block a capacity-unlock, not a cost play; higher distribution voltage cuts conversion losses ~5% end-to-end [S225][S227].
**Beachhead.** Colo operators and enterprise AI builders (hundreds of sites/yr) stuck in transformer queues; ASP $150–500K/block.
**Expansion.** Microgrid interface (C38 adjacency), industrial DC parks.
**Frontier vision.** Power rooms replaced by cabinets.
**HW/SW split.** MV power stage + insulation/protection + grid-interface control software.
**TRL/feasibility.** MV SiC (3.3–10 kV) devices maturing; hardest candidate technically in the D02 set; 24 months to certified v1. Well-funded competitors may down-scope into this tier — watch Heron/DG Matrix [S030].
**Cleanroom dependence.** None.
**China angle.** Parallel 800 V rollout, ByteDance bidding [S031 via D02]; domestic giants likely to own it — US-first.
**US angle.** Strong: transformer crisis is acute [S029][S042].
**Founder fit.** High-power-density conversion — strong; MV insulation experience must be built.
**Sources.** [S225][S227][S211][S029][S042]

## C10 — Precision GaN/SiC magnet & scientific power converter line (fusion, accelerators, research) [S]

**Concept.** A modern, WBG-native line of precision magnet power supplies and scientific converters (ppm-stability, fast-response, kA-class) sold to fusion pilot plants, accelerator facilities, and university/national labs — replacing decades-old thyristor custom-quote shops.
**Extreme edge.** Incumbents (OCEM-class) ship 5 ppm thyristor/IGBT converters as multi-year custom projects [S059]; a GaN/SiC-native catalog product with 10x volumetric density and weeks-not-years lead time is a structural leap. Magnets are 28–40% of tokamak capex — power hardware rides that budget line [S054].
**Beachhead.** DOE Milestone awardees hitting PDRs 2027–2029 [S058] + CAS institutes tendering >¥1.3B per batch [S052]; ASP $100K–$2M/system.
**Expansion.** Proton-therapy and synchrotron magnets (C35 adjacency), industrial electromagnets, quantum-lab supplies.
**Frontier vision.** The power-conversion vendor to big science and fusion's industrial phase.
**HW/SW split.** Converter HW + precision digital regulation, sequencing, facility-integration software.
**TRL/feasibility.** Bench-provable without a reactor partner; v1 18 months.
**Cleanroom dependence.** None.
**China angle.** Direct: CAS/Spark-1 procurement pipeline, founder-readable tenders [S052][S070].
**US angle.** DOE milestone procurement wave peaks exactly at launch [S058].
**Founder fit.** Power electronics + instrumentation + big-science credibility (stellarator deployment) — excellent.
**Sources.** [S058][S054][S070][S059][S052]

## C11 — Fast solid-state HTS quench-protection switch & dump modules [S]

**Concept.** Safety-critical solid-state protection hardware for HTS magnets: sub-millisecond kA-class dump switches, energy-extraction resistorless schemes, and drive electronics — sold as a qualified subsystem to every magnet integrator.
**Extreme edge.** REBCO's slow normal-zone propagation plus GJ-scale stored energy makes protection the unsolved hardware problem of HTS magnets [S054][S066]; sub-ms high-current solid-state switching is a defensible physics claim, and SFCL history shows the category needs a product-grade entrant [S085].
**Beachhead.** HTS magnet builders (CFS-class, TE Magnetics, 联创超导, MRI/motor integrators) — every magnet needs one; ASP $50–500K/system.
**Expansion.** Fusion → compact MRI, HTS motors, SMES; converges with C10's customer base.
**Frontier vision.** The safety layer that makes HTS magnets bankable.
**HW/SW split.** Power switching HW + quench-detection-to-trip firmware and magnet-protection modeling software.
**TRL/feasibility.** Prototype-able on a bench without building magnets; 18–24 months to a qualified module.
**Cleanroom dependence.** None.
**China angle.** Sell into China's magnet-supplier boom (联创光电's ¥1.8B+ orders) [S051].
**US angle.** CFS-ecosystem and DOE-milestone magnet programs [S054][S058].
**Founder fit.** WBG switching + superconductivity domain knowledge — a rare intersection; protection hardware, not diagnostics.
**Sources.** [S066][S054][S065][S085]

## C12 — Automated no-insulation HTS coil winding & jointing machines (capital equipment) [S]

**Concept.** Laser-aligned, tension/turn-uniformity-controlled automated winding and joint-fabrication machines for NI/MI HTS coils, sold as capital equipment to magnet manufacturers scaling from prototype to production.
**Extreme edge.** Every named magnet builder winds semi-manually with in-house rigs; no third-party turnkey NI-winding equipment vendor exists [S089]; winding uniformity and joints are named failure points [S054][S091]. The founder has already built exactly this machine once.
**Beachhead.** Magnet manufacturers commissioning new lines (US fusion entrants, 联创超导-class, national labs); machine ASP $300K–$1.5M; 10x REBCO demand growth drives line capex [S080].
**Expansion.** Specialty motor/rotor coils, MRI magnet lines, winding-process software licensing; pairs with C13 (joints) and C33 (QC instrument) as a product family.
**Frontier vision.** "The ASML of coil manufacturing" — owning the machine layer of the HTS century.
**HW/SW split.** Precision electromechanical HW + motion control, machine vision, process-recipe software (deep SW content).
**TRL/feasibility.** Highest-TRL personal asset: a working prior build; 12–18 months to commercial v1.
**Cleanroom dependence.** None.
**China angle.** Direct sales into China's magnet-fab capex wave [S051]; equipment (not magnets) sidesteps most IP walls.
**US angle.** US entrants scaling to pilot-plant volumes; NASEM calls for doubling HTS industrial base [S054].
**Founder fit.** The single most direct capability match in the portfolio (undergrad machine + automation + HTS).
**Sources.** [S089][S086][S102][S054][S051][S080]

## C13 — HTS current leads & low-resistance joint/splice modules [S]

**Concept.** Qualified low-resistance joint/splice modules, terminations, and vapor-cooled/HTS current leads sold as components to magnet integrators.
**Extreme edge.** Splices are "the weakest point" of HTS coils [S054]; nΩ-class reproducible joints at production yield is a physics + process claim a specialist team can own [S091].
**Beachhead.** Magnet builders and national labs buying qualified joints/leads rather than developing in-house; ASP $5–50K/part, recurring.
**Expansion.** Full termination assemblies, cryogenic feedthroughs; natural bundle with C12 machines.
**Frontier vision.** Standardized interconnect for the superconducting economy.
**HW/SW split.** HW component + process-control/traceability software; thinner SW content (flag).
**TRL/feasibility.** Bench-provable; 12 months to qualified samples.
**Cleanroom dependence.** None (precision joining lab).
**China angle.** Component sales into Chinese magnet supply chain [S051].
**US angle.** Fusion + MRI + research magnet base [S054].
**Founder fit.** Superconductivity + precision process — strong, though narrower standalone business.
**Sources.** [S091][S054][S086]

## C14 — Compact conduction-cooled cryostats & QC test dewars for HTS coil manufacturers [S]

**Concept.** Standardized bench-scale conduction-cooled cryostats and coil-qualification dewars (fast-turnaround, laser-aligned fixturing, integrated current leads) for magnet fabs, universities, and QC lines.
**Extreme edge.** Big cryo vendors serve industrial/semiconductor scale, not the fast-cycle coil-test niche; low heat-leak + fast thermal cycling + integrated fixturing is a real engineering edge [S076].
**Beachhead.** Magnet manufacturers and university/national-lab programs qualifying coils before shipment; ASP $80–300K.
**Expansion.** Turnkey test cells bundling C33 instrumentation; OEM cryostats for C15 magnet modules.
**Frontier vision.** The standard cold test bench of the HTS industry.
**HW/SW split.** Vacuum/cryo HW + thermal control, data-acquisition and test-sequencing software.
**TRL/feasibility.** Cryocoolers purchasable; 12–18 months to v1; cryocooler supply tightness is a sourcing risk [S093].
**Cleanroom dependence.** None.
**China angle.** Sell to Chinese coil fabs; local cryocooler sourcing hedge [S051].
**US angle.** Fusion/MRI magnet QC demand [S054].
**Founder fit.** Harsh-environment packaging (UHV, cryo) + instrumentation — good.
**Sources.** [S076][S054][S093][S075]

## C15 — Turnkey cryocooler-integrated compact HTS magnet modules for OEM instrument builders [S]

**Concept.** A standardized, quench-safe, cryogen-free HTS magnet platform (one bore/field class, e.g. 1.5–3 T benchtop) sold as a subsystem to NMR/benchtop-MRI/metrology OEMs who lack magnet engineering.
**Extreme edge.** Ultra-compact HTS magnets are proven in prototypes (1.5 T, <400 mm bore, single cryocooler) but blocked by manufacturing failure modes (epoxy cracking under thermal cycling) no vendor has solved at production scale [S076][S199] — a winding/packaging problem, which is precisely the founder's asset.
**Beachhead.** Benchtop-NMR and emerging point-of-care/low-field imaging OEMs (instrument prices $30–150K; magnet subsystem ASP $30–80K) [S074].
**Expansion.** Compact accelerator/beamline magnets, industrial NMR engines, veterinary imaging; feeds C37 gradient-amp bundling.
**Frontier vision.** HTS magnets as a catalog component, not a project.
**HW/SW split.** Magnet+cryo HW + field-control/quench-management firmware and homogeneity-mapping software.
**TRL/feasibility.** REBCO cost falling on fusion demand [S080]; 24 months to OEM-qualified platform.
**Cleanroom dependence.** None.
**China angle.** Sell magnets to Chinese instrument makers currently importing; 十五五 names superconducting materials a priority [S078].
**US angle.** Domestic-supply demand as AMSC-class players focus on grid [S083].
**Founder fit.** NI-HTS winding + packaging + electronics — excellent.
**Sources.** [S076][S074][S078][S083]

## C16 — HTS induction heaters for non-ferrous metals processing [S]

**Concept.** Cryocooler-integrated HTS DC-induction billet heaters (rotating billet in a static superconducting field) for aluminum/copper extrusion and forging shops.
**Extreme edge.** Resistive induction heating of non-ferrous billets is ~50% efficient; HTS DC induction demonstrated ~2x efficiency and ~25% productivity gains at a commercial extruder [S079] — a clean, physics-backed 2x-on-energy claim with six-to-seven-figure ROI per machine.
**Beachhead.** Mid-size extrusion/forging shops (thousands globally) replacing end-of-life heaters; ASP $500K–$1.5M.
**Expansion.** Steel/titanium preheating, industrial magnet systems; China's extrusion industry.
**Frontier vision.** Superconductivity quietly decarbonizing hot metal forming.
**HW/SW split.** Magnet+cryo+drive HW + process-control/scheduling software.
**TRL/feasibility.** Category proven (Zenergy, Supercoil) then stalled on 1G-era economics; 2029 REBCO costs re-open it [S080]. 24 months to first unit.
**Cleanroom dependence.** None.
**China angle.** Large extrusion base + state energy-efficiency mandates [S078].
**US angle.** Reshored fabrication + industrial-electrification incentives.
**Founder fit.** HTS coils + power electronics + automation — strong.
**Sources.** [S079][S078][S094][S080]

## C17 — Compact SMES modules for sub-second power-quality ride-through [S]

**Concept.** Standardized sub-MJ superconducting magnetic energy storage units (cryocooler-integrated) for data-center and industrial sub-cycle ride-through — sold where supercaps/batteries can't meet cycle life or response.
**Extreme edge.** Sub-100 ms (down to ms) response, >95% efficiency, effectively unlimited cycle life [S092]; targets the same transient problem as C08 with a physics-differentiated (and dearer) tool.
**Beachhead.** Semiconductor fabs / AI campuses with chronic sag exposure; ASP $300K–$1M/unit.
**Expansion.** Grid ancillary microservices, pulsed-load industrial buyers.
**Frontier vision.** Superconducting buffers stabilizing the electronic grid.
**HW/SW split.** Magnet/cryo/converter HW + power-quality event response firmware.
**TRL/feasibility.** Chronically stalled category [S081]; must beat supercaps on lifetime economics — genuine risk that C08 wins commercially. 24–30 months.
**Cleanroom dependence.** None.
**China angle.** Grid-modernization pilots; state appetite for superconducting demos [S078].
**US angle.** Data-center power quality (ERCOT-driven) [S041].
**Founder fit.** HTS + power electronics — direct; market risk is the question, not capability.
**Sources.** [S092][S212][S088][S081]

## C18 — HTS magnetic-Czochralski retrofit magnets for crystal growers outside China [S]

**Concept.** Retrofit HTS magnet modules (with cryo and field control) for magnetic-field-applied Czochralski silicon growth, sold to Western/Japanese/Korean furnace OEMs and wafer producers.
**Extreme edge.** Superconducting MCZ suppresses melt convection for better crystal yield; 联创超导 proved the category with RMB-billions in orders and 1,600-unit/yr planned capacity — but serves China only [S082]. Outside China there is no equivalent supplier.
**Beachhead.** Furnace OEMs and 300 mm wafer/PV ingot producers in US/EU/JP/KR; ASP $300K–$800K/furnace.
**Expansion.** Other field-assisted processing (directional solidification, EM stirring).
**Frontier vision.** Field-engineered materials manufacturing.
**HW/SW split.** Magnet HW + field-profile control software tuned to growth recipes.
**TRL/feasibility.** Category-proven physics; 24 months to retrofit-qualified unit; requires furnace-OEM co-development.
**Cleanroom dependence.** None (the buyer owns the fab).
**China angle.** Inverted: compete with 联创 for non-China share; possibly source tape from China early [S082][S051].
**US angle.** Semiconductor reshoring + supply-chain de-risking from Chinese equipment [S070].
**Founder fit.** HTS magnets + automation; semiconductor-market knowledge from PhD context.
**Sources.** [S082][S078][S070][S051]

## C19 — Compact isostatic-press densification cells for solid-state battery pilot lines [S]

**Concept.** Precision warm-isostatic-press formation cells (pressure/temperature-profile control, single-cell to small-batch) for solid-state battery pilot lines.
**Extreme edge.** SSB solid-solid interfaces need ~600 MPa-class densification with tight control; incumbent Chinese lines target gigafactory scale, leaving pilot-scale (the 2027–2030 phase every SSB program must pass through) unserved [S097][S118].
**Beachhead.** SSB startups and OEM pilot lines (dozens in US/EU/JP/CN) running 10²–10⁴ cells/month; ASP $200–800K.
**Expansion.** Production-scale presses, sodium/silicon chemistry formation (C20 adjacency).
**Frontier vision.** The process-equipment layer of post-Li-ion batteries.
**HW/SW split.** Hydraulic/thermal HW + closed-loop process control and recipe/traceability software.
**TRL/feasibility.** Industrial components; 18 months to v1. Chinese equipment majors will follow — speed is the moat [S097].
**Cleanroom dependence.** None (dry room at customer).
**China angle.** RMB 500B-by-2030 SSB equipment framing; sell to Chinese pilot lines early [S097].
**US angle.** FEOC rules push US lines toward non-Chinese equipment from 2027 [S106][S107].
**Founder fit.** Precision electromechanical + control; battery domain must be learned (flag).
**Sources.** [S106][S107][S097][S118]

## C20 — Energy-recycling pilot-scale formation/EOL systems for emerging battery chemistries [S]

**Concept.** High-accuracy, energy-recycling formation and end-of-line systems sized for sodium-ion/silicon-anode/SSB pilot production (hundreds of channels, not gigafactory scale).
**Extreme edge.** Commodity formation racks publish no accuracy specs and waste energy [S112]; >90% energy recycling with precision per-channel source/measure is a quantifiable edge incumbents reserve for their largest customers [S105].
**Beachhead.** Emerging-chemistry cell makers and national-lab pilot lines; ASP $150–600K/system; Unico's entry proves sub-Tier-1 demand [S096].
**Expansion.** Grading/EOL automation, chemistry-specific formation recipes as licensed IP.
**Frontier vision.** Formation as a precision instrument, not a power-waster.
**HW/SW split.** Power-converter HW + per-channel measurement + recipe/analytics software (high SW content).
**TRL/feasibility.** Core is precision bidirectional converters — founder home turf; 12–18 months.
**Cleanroom dependence.** None.
**China angle.** Sodium-ion is a state priority; compete on precision vs. 先导/杭可 scale [S097].
**US angle.** FEOC-driven non-Chinese-equipment preference [S107][S106].
**Founder fit.** Power electronics + instrumentation + software — strong.
**Sources.** [S096][S107][S105][S112][S106]

## C21 — Compact wafer-level burn-in & stress-test cells for WBG power devices [T]

**Concept.** Benchtop-to-cell-scale wafer/die-level burn-in systems (high current, high temperature, HTRB/dynamic stress) for GaN/SiC device makers and module builders who can't justify Aehr-class multi-million-dollar platforms.
**Extreme edge.** High-parallelism thermally-managed kV/hundreds-of-amps stress at 1/10th the entry price; incumbents chase the largest AI-processor accounts [S101][S122], leaving specialty power devices thinly served.
**Beachhead.** GaN power-IC startups and second-tier SiC fabs (US, EU, China) needing automotive credibility; ASP $300K–$1M.
**Expansion.** Module-level burn-in, test services, JEDEC-compliance bundles (C23 family).
**Frontier vision.** Reliability screening as accessible infrastructure for the WBG buildout.
**HW/SW split.** Thermal/contact HW + test-plan sequencing, data analytics, yield-learning software.
**TRL/feasibility.** 18 months to v1; JEDEC JEP203/204 (June 2026) creates the compliance pull [S135][S139].
**Cleanroom dependence.** Low (interfaces to wafers; doesn't process them).
**China angle.** Packaging/test equipment localization ~5–14% — strong import-substitution pull [S124][S125].
**US angle.** University/DoE labs and fabs lacking affordable rigs [S133].
**Founder fit.** GaN/SiC characterization is literally his PhD daily work.
**Sources.** [S135][S139][S101][S122][S124]

## C22 — Automated partial-discharge/insulation EOL qualification rigs for HV power-electronics manufacturing [T]

**Concept.** In-line automated hipot/PD/insulation qualification systems tuned to compact SiC/GaN HV assemblies (EV chargers, converters, motor drives) for 100% end-of-line screening — explicitly production test, not grid-asset condition monitoring (Magnefy conflict avoided).
**Extreme edge.** Fast-switching, high-dV/dt compact assemblies stress insulation in ways utility-transformer PD gear isn't built for [S104]; fast automated sequencing is a direct throughput lever.
**Beachhead.** Power-electronics module/drive manufacturers; ASP $100–400K/line.
**Expansion.** Design-validation labs; insulation-lifetime data services.
**HW/SW split.** HV instrumentation HW + PD signal processing/classification software.
**TRL/feasibility.** 12–18 months; standards exist (IEC 60747 family) [S142].
**Cleanroom dependence.** None.
**China angle.** Sell to Chinese drive/charger makers; 华乘 focuses on grid, not EOL [S110].
**US angle.** Reshored power-electronics manufacturing lines.
**Founder fit.** Precision instrumentation + HV — good; category is crowded-adjacent (flag).
**Sources.** [S142][S015][S104][S110]

## C23 — JEDEC-compliant automated WBG characterization appliance (DPT + dynamic-Ron + short-circuit ruggedness) [T]

**Concept.** A purpose-built, sub-$150K automated bench appliance producing JEP203/204-compliant SiC/GaN datasheet and qualification data (double-pulse, dynamic RDS(on), HTRB, short-circuit withstand) with clean sweep/export software.
**Extreme edge.** Today this capability is patched together from scopes and one-off rigs; a national Catapult center had to build shared DPT capacity because no product exists [S127]. New JEDEC guidelines (June 2026) standardize methods the industry lacks equipment for [S135][S128].
**Beachhead.** Mid-tier device makers, university/DoE/DoD labs; hundreds of buyers; ASP $80–150K.
**Expansion.** Wafer-level versions (C21 family), compliance-data services, China fab labs.
**HW/SW split.** Precision pulsed HW + measurement automation and reporting software (SW-heavy).
**TRL/feasibility.** Fastest-to-revenue candidate: 9–12 months to sellable v1.
**Cleanroom dependence.** None.
**China angle.** SiC/GaN fab buildout + low equipment localization [S125][S131].
**US angle.** Sandia/NASA-documented capability gap in labs [S133][S143].
**Founder fit.** He runs these exact measurements today; deep credibility with the buyer.
**Sources.** [S135][S128][S127][S139][S142][S133]

## C24 — High-voltage SiC/GaN probe cards & wafer test interface hardware [T]

**Concept.** Arc-resistant, field-replaceable kV-class probe cards and test interfaces for WBG wafer-level test.
**Extreme edge.** kV-class probing with clean switching parasitics is a niche the big probe-card vendors underserve [S126]; China has near-total import dependence on test-interface hardware [S124].
**Beachhead.** WBG IDMs/OSATs qualifying wafer lots; consumable-like recurring ASP $10–50K/card.
**Expansion.** Full test cells (with C21/C23), RF probe niches.
**HW/SW split.** HW-dominant precision electromechanical; SW = test-interface configurators (thin — flag).
**TRL/feasibility.** 12 months; qualification cycles with each customer.
**Cleanroom dependence.** Low.
**China angle.** Strong import-substitution demand [S124][S125].
**US angle.** Custom short-run automotive-grade cards.
**Founder fit.** Moderate; precision fixturing yes, but thinner software and smaller frontier story.
**Sources.** [S139][S135][S126][S124]

## C25 — Standalone die-to-wafer overlay/void inspection stations for mid-tier OSATs [T]

**Concept.** A single-purpose optical/IR overlay + void metrology station for die-to-wafer hybrid bonding at mid-tier OSATs priced below EVG/KLA flagship tools.
**Extreme edge.** Sub-µm-pitch bonding needs dense overlay sampling; EVG's newest tool (2,800 points/wafer in 4 min) is priced for HVM leaders [S121]; the mid-volume tier still undersamples and eats yield loss [S136][S137].
**Beachhead.** OSAT process-engineering teams (chiplet/HBM overflow capacity); ASP $500K–$1.5M.
**Expansion.** Void/bond-quality metrology; NIST flags predictive bond metrology as open [S132].
**HW/SW split.** Optics/stage HW + image processing and metrology software (SW-heavy).
**TRL/feasibility.** Hardest optical-engineering lift in the T-group; 24 months. Adjacent to, not inside, founder's core (flag).
**Cleanroom dependence.** Medium (tool operates in customer cleanroom; development needs class control).
**China angle.** OSAT localization push [S124][S125].
**US angle.** CHIPS-funded advanced-packaging buildout [S132].
**Founder fit.** Weakest fit of the T-group — optics-centric; kept for diversity and market size.
**Sources.** [S121][S136][S137][S138][S132]

## C26 — Radiation-characterized SiC/GaN power modules for satellite constellation buses [S]

**Concept.** A power-module family (one voltage class, e.g. 100 V/300 V bus) with radiation performance as a designed-in, documented headline spec — published proton/heavy-ion data as the differentiator — sold to constellation primes.
**Extreme edge.** SiC radiation response varies from <1% to 15% breakdown-voltage shift purely by edge-termination design [S161] — device-physics depth is the moat; no incumbent sells WBG space power with radiation data as the spec sheet's first page [S145].
**Beachhead.** SDA-ecosystem primes and smallsat integrators burned by the propulsion/parts crunch [S151][S152]; ASP $20–100K/module.
**Expansion.** Full PCDUs (C29), lunar/fission-surface-power converters [S156].
**Frontier vision.** Power electronics for the electrified solar system.
**HW/SW split.** HW modules + telemetry/derating-management firmware.
**TRL/feasibility.** COTS-plus screening flows are established [S145][S160]; radiation campaigns are buyable beam time, not a fab; 18–24 months.
**Cleanroom dependence.** Low (buys dies).
**China angle.** Qianfan/Guowang's non-integrated supply chain wants suppliers [S162] — but export controls force a fully separate entity; treat as optional parallel track.
**US angle.** Strong: DoD lending + rad-hard supply subsidies signal structural shortage [S152][S154].
**Founder fit.** WBG device physics + harsh-environment packaging + instrumentation — excellent.
**Sources.** [S161][S145][S154][S153][S162][S160]

## C27 — 300°C-native power-conditioning modules for geothermal/downhole tools [S]

**Concept.** Power-conditioning and drive modules built from WBG devices and high-temperature packaging that natively survive 250–300°C+ downhole, replacing vacuum-flask workarounds around 175°C silicon.
**Extreme edge.** EGS wells target >375°C while today's tools spec 225°C [S158][S159]; native high-temperature electronics removes the constraint instead of insulating around it [S147]. GaN's high-temperature physics is the founder's PhD substrate.
**Beachhead.** MWD/LWD tool builders and EGS developers (Fervo-class, FORGE ecosystem) [S155]; ASP $30–150K/module; deep per-well budgets.
**Expansion.** Oil/gas retrofit, well-integrity robotics, aero-engine-adjacent high-temp power.
**Frontier vision.** Electronics that work where the energy is.
**HW/SW split.** HW module + downhole telemetry/health firmware.
**TRL/feasibility.** High-temp passives/packaging are the hard part; 24 months to qualified module; US/EU market almost exclusively.
**Cleanroom dependence.** Low.
**China angle.** Weak (no comparable EGS program found) — US-first by structure [S159].
**US angle.** DOE EGS push + enhanced-geothermal venture wave [S158][S155].
**Founder fit.** Harsh-environment packaging + WBG + instrumentation — direct.
**Sources.** [S147][S158][S159][S155]

## C28 — Fast-turn COTS-plus radiation-tolerant DC-DC converter family for smallsats [S]

**Concept.** One isolated DC-DC converter family (100–1500 W band) qualified via COTS-plus screening, competing on guaranteed lead time and a non-China supply chain.
**Extreme edge.** The pain is qualification lead time and lot-to-lot risk, not physics [S152]; "weeks not quarters" delivery with published screening data is the 10x in a market where primes redesign around unreliable suppliers [S151].
**Beachhead.** Constellation primes and DoD-adjacent integrators; ASP $10–60K; SDA batch economics ($9–17M/satellite) leave room [S153].
**Expansion.** PCDU line (C29), rad-characterized WBG modules (C26).
**HW/SW split.** HW converters + screening automation and traceability software.
**TRL/feasibility.** Fastest space entry: 12 months to first quals via MIL-PRF flows [S160].
**Cleanroom dependence.** None.
**China angle.** Separate-entity question as C26; default US-first.
**US angle.** Structural shortage documented by DoD lending programs [S152][S154].
**Founder fit.** Power electronics + disciplined test — strong; less unique than C26 (screening is process, not physics).
**Sources.** [S160][S154][S152][S151]

## C29 — Smallsat PPU/PCDU product line for constellation-scale manufacturing [S]

**Concept.** Power-processing units (for electric propulsion) and power-conditioning/distribution units designed for rate manufacturing — the mass-production cost curve legacy space primes never built.
**Extreme edge.** SDA's buildout hit an actual thruster/PPU shortage ("~100 thrusters a month" needed) [S151]; incumbents ship bespoke units at prime prices [S144]; design-for-rate + WBG density is the wedge.
**Beachhead.** Smallsat primes and propulsion startups needing PPUs at volume; ASP $50–250K.
**Expansion.** Full electrical power systems; orbital power/data-center periphery [S148][S149].
**Frontier vision.** The power backbone of megaconstellations.
**HW/SW split.** HW + power-management, MPPT, fault-protection flight software (rich SW).
**TRL/feasibility.** 24 months to flight-qualified v1 — longest space cycle here; anchor-customer strategy required.
**Cleanroom dependence.** Low.
**China angle.** Qianfan needs ~2x Starlink's cadence via a non-integrated supply chain [S162] — a real China-entity opportunity with hard export-control walls; assess in Phase 5.
**US angle.** SDA tranche cadence + commercial constellations [S153][S151].
**Founder fit.** Power electronics + embedded + manufacturing automation — strong.
**Sources.** [S153][S162][S144][S151]

## C30 — Fast + accurate isolated current-sensor modules for WBG power systems [T]

**Concept.** A current-sensing module line combining >10 MHz bandwidth with <0.1% lifetime accuracy (TMR/fluxgate hybrid front end + compensation electronics) for WBG power test, EV inverters, and AI-datacenter power loops.
**Extreme edge.** The incumbent leader ships three separate product lines because speed, density, and accuracy can't be had together [S178]; published TMR physics shows the combination is reachable but unproductized [S187].
**Beachhead.** WBG module makers, DPT-rig integrators (C23 synergy), inverter OEMs; ASP $200–2K/channel at volume.
**Expansion.** Metrology-grade transducers (LEM/Danisense tier) [S179][S181]; datacenter rail monitoring as a component.
**HW/SW split.** Sensor HW + compensation/calibration algorithms (SW-rich for a component).
**TRL/feasibility.** 12–18 months; possible ASIC later (buys foundry, no cleanroom ownership).
**Cleanroom dependence.** Low.
**China angle.** Domestic magnetic-sensor share only 5–10% — import-substitution demand [S182].
**US angle.** EV/AI power-delivery volume [S178].
**Founder fit.** Magnetic sensing + precision analog — in-lane-adjacent (counts toward PhD-lane cap); genuinely strong fit.
**Sources.** [S187][S165][S178][S182]

## C31 — Triaxial OPM magnetometer product line (MEG research → GPS-denied navigation) [T]

**Concept.** Compact triaxial optically-pumped magnetometer modules for MEG/fMCG research arrays first, migrating the sensor core toward defense-adjacent navigation as ruggedization matures.
**Extreme edge.** fT/√Hz-class sensitivity at room temperature; the mature commercial market is effectively one vendor (QuSpin) with a narrow SKU set [S180]; whole-head arrays still cost SQUID-system money [S177].
**Beachhead.** Neuroscience/biomagnetism labs (hundreds worldwide); ASP $8–12K/sensor, $500K+/array.
**Expansion.** GPS-denied navigation (DARPA RoQS de-risks ruggedization to TRL 6-7 by 2028-29 [S169][S170]); cardiac screening.
**HW/SW split.** Photonics/vapor-cell HW + closed-loop control and array-processing software.
**TRL/feasibility.** Physics mature; manufacturing yield is the moat; 24 months. Laser-alignment fabrication skill applies directly.
**Cleanroom dependence.** Low-medium (vapor cells purchasable).
**China angle.** Western OPMs above 20 pT sensitivity are export-restricted to China [S176] — export-compliant lower-spec variants only; complex compliance surface (Phase 5).
**US angle.** Research + defense funding pull [S169].
**Founder fit.** Precision optomechanical fabrication + magnetometry — in-lane (magnetic sensing); counts toward cap.
**Sources.** [S177][S180][S169][S170][S176][S166]

## C32 — Self-calibrating Rydberg-atom RF field probes for EMC labs [T]

**Concept.** A benchtop SI-traceable Rydberg-atom E-field probe for EMC pre-compliance and calibration labs — atomic self-calibration replacing periodic NIST-trip antenna calibration.
**Extreme edge.** <1% self-calibrated uncertainty vs. antenna standards [S186][S167]; exactly one commercial vendor exists worldwide [S185]; second-sourcing a one-vendor frontier market.
**Beachhead.** EMC test houses and RF calibration labs (Asia-Pacific = 40% of a $4.9B market [S183]); ASP $50–150K.
**Expansion.** Spectrum monitoring, defense EW test.
**HW/SW split.** Laser/vapor-cell HW + spectroscopy control and traceability software.
**TRL/feasibility.** Hardest physics package in the T-group; DARPA RoQS ruggedization matures 2028–29 [S169]; 24–30 months. Atomic-physics hiring needed (flag).
**Cleanroom dependence.** Low.
**China angle.** 高端仪器 is a named 十五五 must-win — Chinese labs will buy compliant instruments [S171][S168].
**US angle.** NIST-adjacent credibility path [S167].
**Founder fit.** Instrumentation + lasers yes; atomic physics is new — moderate.
**Sources.** [S186][S167][S169][S185][S183][S174]

## C33 — Cryogenic current-distribution & quench-onset QC instruments for HTS coil production [T]

**Concept.** A production-line instrument (non-invasive Hall-array/CCC-based) that verifies current distribution and catches quench precursors in NI-HTS coils during winding QC and commissioning — sold as capital equipment to coil manufacturers.
**Extreme edge.** Published methods (current-distribution monitoring, cryogenic current comparators) are lab/beamline-grade [S175][S066]; nobody packages them as a factory instrument. NI coils' screening currents make QC genuinely hard — a physics-rich niche.
**Beachhead.** HTS coil/magnet manufacturers ramping lines (same buyers as C12); ASP $100–300K.
**Expansion.** Bundle with C12 winding machines and C14 cryostats into turnkey coil production cells.
**HW/SW split.** Sensor-array HW + inversion algorithms and QC software (SW-rich).
**TRL/feasibility.** 18 months; direct extension of his stellarator Hall-sensing work — in-lane (counts toward cap).
**Cleanroom dependence.** None.
**China angle.** Chinese coil fabs scaling fastest [S051].
**US angle.** Fusion magnet QC demand [S054].
**Founder fit.** The most literal PhD-skill transfer in the list; capped as diagnostic-category.
**Sources.** [S175][S066][S054][S051]

## C34 — Ultra-low-noise high-channel-count SMU line for battery & materials R&D [T]

**Concept.** Purpose-built, high-channel-density, sub-µV/pA-noise source-measure instruments for next-gen battery-cell R&D and materials labs — below Keithley/Keysight prices per channel, above their noise performance.
**Extreme edge.** New chemistries push formation/characterization gear to its noise floor; general-purpose SMUs are $8–23K/channel [S173]; a 10x channel-density-per-dollar claim with better noise is quantifiable.
**Beachhead.** Battery-chemistry R&D labs (gigafactory R&D centers, universities); ASP $50–200K/system.
**Expansion.** Formation-adjacent (C20 synergy), semiconductor parametric test.
**HW/SW split.** Precision analog HW + measurement orchestration/analytics (SW-heavy).
**TRL/feasibility.** 12 months to v1 — among the fastest.
**Cleanroom dependence.** None.
**China angle.** CATL/BYD-scale R&D + instrument import-substitution [S171].
**US angle.** National-lab and startup battery R&D.
**Founder fit.** Precision analog instrumentation — direct.
**Sources.** [S173][S096][S095]

## C35 — Modular solid-state RF amplifier cassettes for compact particle-therapy accelerators [S]

**Concept.** GaN-on-SiC solid-state RF/LLRF amplifier cassettes (1–5 kW VHF modules, N+1 combinable to 100+ kW) replacing tubes in compact proton/carbon-ion cyclotrons — field-swappable to kill clinical downtime.
**Extreme edge.** Tube supply chains are shrinking; solid-state gives graceful degradation and 68–71% published efficiency at 83 MHz [S192][S193][S209]; downtime is the metric hospitals pay for.
**Beachhead.** Cyclotron OEMs and national labs building compact systems; China alone allocated 41+8 proton/heavy-ion units under national planning [S204][S194]; ASP $30–100K/cassette, $1M+/system.
**Expansion.** Synchrotron/linac RF, industrial accelerators, fusion ICRH (C10 customer overlap).
**Frontier vision.** Solid-state RF power as the enabling layer of accessible particle therapy.
**HW/SW split.** RF HW + LLRF control (FPGA-heavy), health-management software.
**TRL/feasibility.** Published building blocks exist; 18–24 months to OEM-qualified cassette; no clinical regulatory burden (OEM subsystem).
**Cleanroom dependence.** None (buys GaN transistors).
**China angle.** Five domestic proton-system developers + state demand pipeline; 国产化 exclusion risk noted [S203][S204].
**US angle.** IBA/Mevion-class OEM second-sourcing.
**Founder fit.** RF power + FPGA + instrumentation — strong.
**Sources.** [S192][S193][S209][S194][S204][S203]

## C36 — GaN-native modular RF/microwave generator platform for ablation-device OEMs [S]

**Concept.** A licensable GaN RF/microwave energy engine (300 kHz–2.45 GHz variants) with fast closed-loop impedance/temperature control, sold as an OEM subsystem to interventional-ablation device makers.
**Extreme edge.** Legacy generators carry magnetron-era size/heat/coarse control; GaN solid-state enables fine, fast energy delivery in a fraction of the volume [S202][S208].
**Beachhead.** Mid-tier interventional-oncology OEMs and Chinese ablation makers inside a $4.3B→$10.4B market [S190]; ASP $15–50K/engine + licenses.
**Expansion.** Electrosurgery, pulsed-field ablation (cardiac), aesthetic RF.
**HW/SW split.** RF HW + treatment-control firmware; regulatory burden sits with the integrating OEM.
**TRL/feasibility.** 18 months to OEM reference design.
**Cleanroom dependence.** None.
**China angle.** Fast-growing domestic ablation market; founder network for OEM design-ins [S190].
**US angle.** OEM subsystem sales to device majors.
**Founder fit.** GaN + RF + control — strong; medical-market knowledge to build (flag).
**Sources.** [S202][S208][S190][S191]

## C37 — Precision gradient-amplifier modules for low-field/portable MRI [S]

**Concept.** A three-axis precision gradient-driver module (high-fidelity current control, low drift) priced for the low-field/portable/academic MRI segment that clinical-grade OEM amps ignore.
**Extreme edge.** The incumbent (Prodrive) sells only into large-volume clinical OEM programs [S210]; academics resort to $1,200 audio-amp hacks [S198] — a price-umbrella gap between hack and clinical-grade.
**Beachhead.** Portable/low-field MRI startups, Halbach-array labs, veterinary imaging OEMs; ASP $15–60K.
**Expansion.** RF amplifier + spectrometer electronics bundle; pairs naturally with C15 magnets for a compact-MRI subsystem stack.
**HW/SW split.** Power/precision-analog HW + pulse-sequence interface software.
**TRL/feasibility.** Well-documented physics; 12 months to v1 — fast. FDA 510(k) burden sits with system integrators [S200][S201].
**Cleanroom dependence.** None.
**China angle.** Chinese low-field MRI integrators buy components today [S195].
**US angle.** Portable-MRI startup ecosystem.
**Founder fit.** Precision analog + power — direct.
**Sources.** [S198][S210][S201][S200][S195]

## C38 — Grid-forming power-conversion systems for behind-the-meter compute-campus microgrids [S]

**Concept.** A purpose-built grid-forming (GFM) PCS product line for behind-the-meter AI-campus microgrids: black-start, fault ride-through, certified compliance — built GFM-native rather than retrofitted firmware.
**Extreme edge.** GFM mandates (NERC guidance; China's >30% GFM quota for new Northwest projects) are arriving faster than incumbents certify products [S220][S221]; interconnection queues of 3–7 years make BTM power a capacity unlock [S214].
**Beachhead.** BTM microgrid integrators and data-center developers; ASP $200K–$1M/PCS; a compliance-certification moat.
**Expansion.** Fuel-cell/electrolyzer interfaces (C39), utility GFM retrofits, island grids.
**Frontier vision.** The inverter that replaces the synchronous machine.
**HW/SW split.** SiC power stage + GFM control algorithms (deep SW moat: virtual inertia, protection coordination).
**TRL/feasibility.** 24 months to certified v1; incumbent giants (Sungrow, SMA, GE Vernova) are the risk — niche-first essential [S222].
**Cleanroom dependence.** None.
**China angle.** NDRC/NEA mandate creates compliance demand; crowded domestic PCS field — differentiate on GFM-native control [S220][S222].
**US angle.** ERCOT/NERC compliance cycle 2027–2029 [S221][S212].
**Founder fit.** Power electronics + control theory + software — strong.
**Sources.** [S220][S221][S222][S214][S212]

## C39 — High-efficiency power-source modules for off-grid, fluctuating-renewable electrolyzers [S]

**Concept.** SiC-based rectifier/power-source modules optimized for off-grid wind/solar-direct hydrogen plants — wide-input-range, fast dynamic response, high efficiency where thyristor rectifiers can't follow renewable fluctuation.
**Extreme edge.** China's market shows a 4–6x price gap between crude thyristor and precise IGBT sources [S219]; post-subsidy economics (45V sunsets Jan 2028 [S216]) make kWh/kg efficiency the buying criterion; published work confirms power-quality gains at 20 MW scale [S224].
**Beachhead.** Green-hydrogen EPCs building off-grid projects; ASP $100–500K/module set.
**Expansion.** Fuel-cell power conditioning, DC-coupled solar-storage-hydrogen parks.
**HW/SW split.** Power HW + plant-level power-management software.
**TRL/feasibility.** 18 months; DOE $250/kW system targets squeeze power-electronics cost share [S213].
**Cleanroom dependence.** None.
**China angle.** 制氢电源 named a new blue-ocean domestically; founder-readable market [S219].
**US angle.** Post-45V efficiency-driven projects; export-oriented H2 [S216][S215].
**Founder fit.** Power conversion — direct; hydrogen domain to learn.
**Sources.** [S219][S224][S213][S216][S215]

## C40 — Automated grading & sorting systems for second-life EV battery repurposing [T]

**Concept.** Fast automated multi-channel grading/sorting benches (SOH/DCIR/BMS interrogation, robotic handling) sold as capital equipment to battery repurposing plants.
**Extreme edge.** Grading is the certified-throughput bottleneck: China's mandatory 梯次利用 certification (2023) and UL 1974 both require per-pack assessment that is manual and slow today [S218]; fast parallel electrochemical characterization is an instrumentation problem.
**Beachhead.** Repurposing facilities (B2U/Smartville-class in the US, certified Chinese plants); ASP $200–800K/line [S231][S232].
**Expansion.** EOL automotive test, insurance-grade battery certification data.
**HW/SW split.** Test HW + grading algorithms/database software (SW-rich).
**TRL/feasibility.** 12–18 months; volume wave arrives 2028–2031 as first mass-EV cohorts retire [S226].
**Cleanroom dependence.** None.
**China angle.** Largest retirement volume + mandatory certification = strongest first market [S218].
**US angle.** UL 1974 facility growth [S231].
**Founder fit.** Instrumentation + automation + software — good; battery domain to learn.
**Sources.** [S218][S226][S231][S232]

---

*End of candidate list (40 candidates). Scoring in `30_PHASE3_SCORING/`.*
