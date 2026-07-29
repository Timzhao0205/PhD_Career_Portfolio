# Worker 05 — Extreme / Cryogenic / Superconducting / High-Field / Harsh Environments

Worker prefix: **EXT**
Domain: Extreme / cryogenic / superconducting / high-field / harsh environments
Date: 2026-06-28
Author: EXTREME FRONTIER worker (fresh from-scratch research)

---

## 1. Domain thesis

The frontier in extreme systems is being defined by three near-simultaneous demand shocks:

1. **The HTS fusion magnet buildout.** Private fusion (Commonwealth Fusion, Tokamak Energy, Type One, Thea, Proxima) and state programs (ITER, China's EAST/BEST/CFETR) have moved REBCO high-temperature-superconductor magnets from physics to manufacturing. REBCO tape capacity grew >400% from 2020–2025 and a single Chinese supplier (Shanghai Superconductor) is scaling from 2,000 to 4,000 km/yr. The magnet itself is now a *systems integration* problem: quench detection in HTS is fundamentally harder than in LTS (slow normal-zone propagation, tiny voltages buried in tokamak EM noise), joints/splices are a known yield bottleneck, no-insulation coils trade self-protection for charging delay and screening-current stress, and the cold-powering / cryoplant / current-lead chain is the dominant heat-load budget. Each of these is an "engine-layer" subsystem that every magnet builder needs but few can build well.

2. **Harsh-environment electronics hitting a temperature/radiation wall.** Superhot geothermal (350–450 °C), advanced fission in-core (>500 °C, >10^15 n/cm^2), fusion in-vessel diagnostics (10^13 n/cm^2/s), hypersonic thermal-protection skins, and space all need active electronics and sensors where silicon CMOS quits at ~175–225 °C. SiC and wide-bandgap nitrides are the materials answer, but the gap is *qualified, packaged, system-ready modules* — not bare die.

3. **The cryogenic stack as a supply-chain chokepoint.** Quantum computing (cryo-CMOS control, dilution refrigeration), fusion (75 kW @ 4.5 K cryoplants), and superconducting power all compete for the same scarce helium, cryocoolers, current leads, and cryogenic power electronics. The winners will productize the subsystems that turn a one-off physics rig into a manufacturable cold platform.

**Where the defensible companies are:** not in dashboards or "monitoring," but in the *protection-and-control loop and the qualified hardware module* that makes a frontier magnet, reactor, drill, or vehicle survivable. The recurring pattern is: a physical sensing/actuation modality (fiber optics, Hall sensors, SiC detectors, EM pumps, flux pumps) + a real-time control/discrimination algorithm + a qualification/test capability that incumbents lack. China is genuinely competitive-to-leading in REBCO tape, fusion magnets, and high-field labs (CHMFL Hefei, ASIPP), which means US-first candidates must lean on export-controlled / allied-supply-chain wedges, while China-first candidates have a real domestic pull market.

---

## 2. Candidate ideas (24)

Capex bands: **Low** <$2M to first prototype; **Mid** $2–10M; **High** $10–50M; **Very High** >$50M.

---

### EXT-01 — Distributed fiber-optic quench detection + protection unit for HTS magnets
- **One-sentence product:** A co-wound Rayleigh/OFDR optical-fiber interrogator plus quench-discrimination firmware that detects and localizes normal zones in HTS magnets milliseconds before a voltage signal appears, and fires the protection circuit.
- **System boundary shift:** Moves quench detection from lumped voltage taps (overwhelmed by EM noise and slow HTS propagation) to distributed, EM-immune optical sensing that triggers active protection — a detection-to-actuation loop, not monitoring.
- **Extreme metric:** Sub-second normal-zone detection at <1 cm spatial resolution inside tokamak-level EM noise at 4–20 K and tens of kA.
- **First high-end customer:** Compact-fusion magnet developers (Commonwealth Fusion Systems, Tokamak Energy, Type One Energy).
- **Buyer title:** Head of Magnet Engineering / Quench Protection Lead.
- **Pain:** A single undetected HTS quench can destroy a multi-million-dollar coil; voltage-based detection is too slow/noisy for HTS.
- **Current workaround:** Co-wound voltage taps + multi-stage inductive-voltage compensation (e.g., EAST two-stage method); manual margins.
- **Why current solution fails:** HTS normal-zone propagation is slow (cm/s), the quench voltage is tiny and buried in induced/ramp voltage; pure voltage detection misses early quenches.
- **Hardware stack:** Polyimide-coated optical fiber co-wound in pancakes; OFDR/Rayleigh interrogator; cryo-compatible feedthroughs; FPGA trigger to dump resistor / heaters.
- **Software/control stack:** Real-time backscatter inversion, temperature/strain discrimination, ML normal-zone classifier, latency-bounded trip logic.
- **Prototype path 2026–2028:** 2026 single-pancake bench at 77 K; 2027 sub-scale REBCO coil at 4.2 K in a magnet builder's facility; 2028 integration on a customer test coil with closed-loop dump.
- **China wedge:** ASIPP / next-generation fusion magnet program already publishing fiber-optic quench studies — strong domestic pull; localize interrogator + fiber.
- **US wedge:** Sell qualification + integration to private fusion primes; allied optical-interrogator supply (Luna/OFDR class) under export control.
- **Cleanroom dependency:** None (no semiconductor fab); optics assembly only.
- **Capex band:** Mid.
- **Regulatory/export risk:** Moderate — fusion magnet tech may touch export controls; dual-use.
- **Competitors:** In-house teams at CFS/MIT PSFC; interrogator vendors (Luna); academic groups.
- **Defensibility:** Calibration datasets across REBCO geometries + trip-latency IP + qualification track record.
- **Kill criteria:** If voltage+compensation methods reach adequate latency at scale, or if interrogator cost/channel can't beat voltage taps by 2028.
- **Evidence status:** CLEARED.
- **Key sources:** IOP SUST Rayleigh quench (S01), IOP SUST VIPER/SULTAN (S02), IOP SUST China next-gen fusion magnet fiber (S03), IOP Nuclear Fusion IntelliMIK (S04).

---

### EXT-02 — Qualified low-resistance HTS joint manufacturing system ("joint-as-a-component")
- **One-sentence product:** Automated soldered/bridge-lap joint tooling plus per-joint 4 K/77 K resistance and mechanical qualification, sold as qualified joint cartridges and as an in-house joint line.
- **System boundary shift:** Turns the magnet joint from a hand-made artisan step into a specified, traceable, qualified component with a resistance/strength data sheet.
- **Extreme metric:** Reproducible joint resistance in the 1–50 nΩ range at 4 K with documented mechanical strength and field tolerance to >12 T.
- **First high-end customer:** Fusion magnet integrators and accelerator/high-field magnet labs.
- **Buyer title:** Magnet Manufacturing Lead / Conductor Engineering Manager.
- **Pain:** Demountable and large magnets need many reproducible low-resistance joints; variability drives heat load and quench risk; joints are a yield/throughput bottleneck.
- **Current workaround:** Manual soldered lap joints, sampled testing, accept/reject by experience.
- **Why current solution fails:** Solder layer + REBCO/Ag interface resistivity dominate and vary; no productized, statistically-qualified joint exists.
- **Hardware stack:** Alignment/lamination press, controlled solder reflow, integrated 4-point cryo resistance probe, peel/tensile rig.
- **Software/control stack:** Process-recipe control, SPC database, per-joint digital passport.
- **Prototype path 2026–2028:** 2026 bench joint + 77 K QA; 2027 4 K resistance qualification line; 2028 pilot supply of qualified joints to a magnet builder.
- **China wedge:** Co-locate with Shanghai Superconductor / ASIPP magnet lines; domestic CICC programs.
- **US wedge:** Allied joint supply for CFS/Type One; reduce reliance on hand labor.
- **Cleanroom dependency:** None.
- **Capex band:** Mid.
- **Regulatory/export risk:** Moderate (fusion dual-use).
- **Competitors:** ACT/Advanced Conductor, in-house magnet shops, CORC (Advanced Conductor Technologies).
- **Defensibility:** Recipe IP + qualification dataset + tooling.
- **Kill criteria:** If magnet architectures move to jointless winding or if joint variability proves immaterial at scale.
- **Evidence status:** CLEARED.
- **Key sources:** IOP SUST soldered demountable joints (S05), ScienceDirect REBCO stacked-cable low-resistance joint (S06).

---

### EXT-03 — In-line REBCO tape critical-current / defect QC inspection platform
- **One-sentence product:** A high-throughput reel-to-reel contactless critical-current-mapping and defect-classification tool that grades and cuts REBCO tape faster and at higher resolution than today's 77 K self-field scanners.
- **System boundary shift:** Moves tape QC from end-of-line 77 K spot checks to high-resolution, in-line Ic/defect mapping tied to magnet-relevant in-field performance.
- **Extreme metric:** ~1 mm-resolution Ic profiling over >100 m tape with predictive in-field (high-B) performance correlation.
- **First high-end customer:** REBCO tape manufacturers and fusion magnet winders.
- **Buyer title:** VP Manufacturing / Quality Director.
- **Pain:** Intrinsic Ic non-uniformity and slitting defects are the largest source of magnet performance uncertainty; bad meters of tape sterilize whole coils.
- **Current workaround:** TapeStar-class 77 K self-field scanners (low resolution, self-field only).
- **Why current solution fails:** Self-field 77 K Ic poorly predicts in-field high-temperature magnet performance; transverse Jc variability matters for screening-current stress.
- **Hardware stack:** Reel-to-reel transport, Hall-array / inductive excitation heads, optional in-field cryo module, XRD/optical defect channel.
- **Software/control stack:** Electromagnetic inversion for Ic distribution, ML defect classifier, cut-plan optimizer, digital tape passport.
- **Prototype path 2026–2028:** 2026 contactless 77 K mapping head; 2027 in-field correlation module; 2028 in-line pilot at a tape vendor.
- **China wedge:** Sell into Shanghai Superconductor / Shanghai Creative scaling lines (domestic, large volume).
- **US wedge:** Allied tape QC for MetOx/Faraday/SuperPower scale-up; tie to magnet builder acceptance specs.
- **Cleanroom dependency:** None.
- **Capex band:** Mid.
- **Regulatory/export risk:** Low–moderate.
- **Competitors:** THEVA/Bruker TapeStar, in-house metrology.
- **Defensibility:** Inversion algorithms + in-field correlation dataset + vendor integration.
- **Kill criteria:** If tape Ic uniformity improves enough that defect mapping is commoditized.
- **Evidence status:** CLEARED.
- **Key sources:** IOP SUST reduced-Ic current/heat transfer (S07), Nature Sci Rep transverse Jc variability vs screening-current stress (S08), Princeton in-field Ic testing challenges (S07 supporting).

---

### EXT-04 — HTS magnet charging + active quench-protection control platform
- **One-sentence product:** A high-stability magnet power supply plus model-based controller (and optional HTS flux-pump charger) that drives no-insulation / low-resistance HTS magnets while actively compensating charging delay and triggering protection.
- **System boundary shift:** Unifies power supply, charging-delay compensation, screening-current management, and quench protection into one closed-loop control platform rather than separate boxes.
- **Extreme metric:** <0.1 ppm short-term current ripple / 10 ppm/4 h stability with active feedback ramp control of NI coils.
- **First high-end customer:** High-field NI/LR magnet developers, fusion magnet test programs.
- **Buyer title:** Magnet Controls Engineer / Power Systems Lead.
- **Pain:** NI/metal-insulation coils are self-protecting but have long charging delays and nonlinear field response; chargers and protection are bespoke.
- **Current workaround:** Lab-built linear+switching supplies + manual PI tuning; separate quench detection.
- **Why current solution fails:** Charging delay and screening-current stress are coil-specific and poorly controlled; ripple drives AC loss and instability.
- **Hardware stack:** Pre-regulated switching + linear final stage; flux-pump option; current/field sensing; dump circuit.
- **Software/control stack:** Coil electromagnetic model, charging-delay observer, ramp-rate optimizer, integrated trip logic.
- **Prototype path 2026–2028:** 2026 supply + PI feedback on sub-scale NI coil; 2027 flux-pump variant; 2028 integration with EXT-01/EXT-19.
- **China wedge:** CHMFL (Hefei) 45 T-class hybrid magnet supply expertise; domestic high-field labs.
- **US wedge:** Sell to NHMFL-adjacent users, fusion primes; allied controller.
- **Cleanroom dependency:** None.
- **Capex band:** Mid.
- **Regulatory/export risk:** Moderate.
- **Competitors:** Cryomagtech, American Magnetics, Magna-Power (hardware-only).
- **Defensibility:** Control IP + coil-model library; bundled detection.
- **Kill criteria:** If insulated coils dominate and charging-delay control becomes unnecessary.
- **Evidence status:** CLEARED.
- **Key sources:** Cryogenics 45 T CHMFL outsert power supply (S12), Cryogenics flux-pump charger (S13), Cryogenics NI charging-delay elimination (S10), NI feedback-control patent (company claim, supporting).

---

### EXT-05 — Cryogen-free conduction-cooled HTS current-lead modules
- **One-sentence product:** Productized binary (copper + HTS) conduction-cooled current-lead modules with integrated thermometry, optimized to minimize cryocooler power per ampere for cryogen-free magnets.
- **System boundary shift:** Replaces helium-vapor-cooled brass leads and lab-built assemblies with a specified, drop-in cryogen-free lead module.
- **Extreme metric:** Minimized refrigerator power per kA via optimized HTS current density and joint temperature; near-zero standing helium use.
- **First high-end customer:** Cryogen-free HTS magnet builders (research, medical, industrial), fusion test stands.
- **Buyer title:** Cryogenic Systems Engineer.
- **Pain:** Current leads are one of the dominant heat loads; helium-vapor cooling is supply-constrained and operationally costly.
- **Current workaround:** Vapor-cooled brass leads or custom HTS leads designed per project.
- **Why current solution fails:** Helium dependence; per-project redesign; no optimized off-the-shelf module.
- **Hardware stack:** Copper upper stage, HTS (REBCO/Bi-2223) lower stage, thermal intercepts, integrated sensors.
- **Software/control stack:** Thermal model + lead-protection/over-temp logic.
- **Prototype path 2026–2028:** 2026 single lead at rated current on cryocooler; 2027 modular family (100–2000 A); 2028 customer integration.
- **China wedge:** Pair with domestic cryocoolers and SST tape; fast localization.
- **US wedge:** Allied cryogen-free supply as helium tightens.
- **Cleanroom dependency:** None.
- **Capex band:** Low–Mid.
- **Regulatory/export risk:** Low–moderate.
- **Competitors:** American Magnetics, HTS-110/Scientific Magnetics, in-house.
- **Defensibility:** Optimization + qualification + integrated protection.
- **Kill criteria:** Commodity pricing collapses margins; helium supply eases.
- **Evidence status:** CLEARED.
- **Key sources:** Cryogenics conduction-cooled HTS current leads for wiggler (S14), Cryogenics cryocooled HTS magnet temperature optimization (S09), MIT PSFC current-lead optimization report (supporting).

---

### EXT-06 — SiC superhot-geothermal downhole electronics & telemetry module (>300 °C)
- **One-sentence product:** A SiC-based downhole sensing-and-telemetry module (pressure, temperature, attitude, gamma, vibration) rated for continuous operation at 300–450 °C in superhot geothermal and HT oil & gas wells.
- **System boundary shift:** Pushes active downhole electronics past the ~175 °C silicon wall into the supercritical regime, enabling MWD/LWD where none exists today.
- **Extreme metric:** Continuous active operation at ≥300 °C (target 400 °C) at >20,000 psi.
- **First high-end customer:** Superhot/EGS geothermal drillers (Quaise, Mazama, Fervo deep wells), HT oil & gas service companies.
- **Buyer title:** Drilling Technology Director / Downhole Tools Lead.
- **Pain:** At ≥400 °C steel weakens, elastomers fail, and electronics fry; current downhole sensors top out ~150–175 °C, so deep wells are drilled blind.
- **Current workaround:** Flask/Dewar-cooled silicon tools (short dwell), mud-pulse telemetry, or no downhole electronics at all.
- **Why current solution fails:** Active cooling and elastomer-sealed mud pulsers degrade fast; silicon CMOS cannot survive supercritical temperatures.
- **Hardware stack:** SiC/AlGaN sensors and power devices, high-temp packaging/interconnect, ceramic substrates, SiC-based telemetry.
- **Software/control stack:** High-temp drift compensation, fault-tolerant data link, edge inference for tool-face/vibration.
- **Prototype path 2026–2028:** 2026 SiC sensor + amp at 300 °C bench; 2027 packaged module in HT oven/test well; 2028 field trial in an EGS well.
- **China wedge:** China deep-drilling and SiC programs; CGS/CNPC HT well demand.
- **US wedge:** DOE/NREL geothermal HT-electronics ecosystem; allied SiC supply (export-controlled).
- **Cleanroom dependency:** Yes for SiC die — but outsource to SiC foundry; company focuses on packaging/integration (outsourcing path exists).
- **Capex band:** Mid–High.
- **Regulatory/export risk:** Moderate (SiC/wide-bandgap export sensitivity).
- **Competitors:** Schlumberger/SLB, Baker Hughes HT tools, NREL/Sandia programs.
- **Defensibility:** High-temp packaging + qualification + drift-compensation IP.
- **Kill criteria:** If superhot geothermal stalls and HT oil & gas demand alone can't support, or if SiC packaging reliability fails at 400 °C.
- **Evidence status:** CLEARED.
- **Key sources:** DOE EERE HT tools & sensors + NREL HT electronics (S16), Int. Comm. Heat & Mass Transfer downhole thermal-management review (S17), Stanford Geothermal Workshop superhot drilling gap (S18 supporting).

---

### EXT-07 — Cryogenic SiC/GaN power module + gate-driver subsystem (20–77 K)
- **One-sentence product:** A characterized, packaged GaN/SiC power module with a cryo-rated gate driver designed to operate at 20–77 K inside the cold space of superconducting machines and cryo-electric powertrains.
- **System boundary shift:** Moves power conversion *inside* the cryostat (eliminating warm/cold feedthrough losses) with devices selected and packaged for cryogenic operation.
- **Extreme metric:** MW-class conversion with GaN dynamic on-resistance reduced multi-fold at cryogenic temperature vs 300 K.
- **First high-end customer:** Cryo-electric aircraft propulsion and superconducting-machine developers; cryo-cooled data-center power R&D.
- **Buyer title:** Power Electronics Lead / Chief Engineer (Propulsion).
- **Pain:** Warm power electronics force lossy current leads across the cold boundary; standard modules aren't characterized or packaged for cryogenic reliability.
- **Current workaround:** Room-temperature inverters + high-current cryogenic feedthroughs.
- **Why current solution fails:** Feedthrough heat load and copper losses dominate; device behavior (threshold, dynamic Rds-on, gate drive) shifts at cryo and is uncharacterized.
- **Hardware stack:** GaN HEMT / SiC MOSFET modules, cryo-tolerant gate driver, low-CTE packaging, cryo capacitors.
- **Software/control stack:** Cryo device models, temperature-adaptive gate control, protection.
- **Prototype path 2026–2028:** 2026 device cryo characterization; 2027 kW gate-driver+module at 77 K; 2028 sub-MW demo at 20–77 K with a machine partner.
- **China wedge:** Domestic GaN/SiC + superconducting machine programs; localize packaging.
- **US wedge:** DOE/national-lab cryo power-electronics base; allied wide-bandgap supply.
- **Cleanroom dependency:** Outsourced die; packaging/test in-house.
- **Capex band:** Mid.
- **Regulatory/export risk:** Moderate–high (GaN/SiC + propulsion dual-use).
- **Competitors:** GE Aerospace, Airbus UpNext, university labs, module makers (Wolfspeed/Infineon at 300 K only).
- **Defensibility:** Cryo characterization library + packaging + gate-drive IP.
- **Kill criteria:** If cryo-electric propulsion timelines slip past investment horizon and no superconducting-machine pull remains.
- **Evidence status:** CLEARED.
- **Key sources:** OSTI SiC/GaN cryogenic devices national-lab report (S19), Cardiff/peer-reviewed GaN cryo power electronics for SC motors (S20 supporting).

---

### EXT-08 — Liquid-metal MHD flow-control + electromagnetic-pump skid for fusion PFC/blanket
- **One-sentence product:** An electromagnetic-pump + MHD flow-control skid with insulating channel inserts and flow/level/corrosion diagnostics for liquid-lithium / PbLi plasma-facing components and breeding blankets.
- **System boundary shift:** Turns liquid-metal handling from one-off lab loops into a controllable, instrumented flow subsystem with managed MHD pressure drop.
- **Extreme metric:** Stable flowing-Li film handling ≥10 MW/m² peak heat flux (divertor) with MHD pressure-drop mitigation under multi-tesla fields.
- **First high-end customer:** Liquid-metal divertor/blanket programs (national labs, private fusion exploring LM PFCs).
- **Buyer title:** Blanket/PFC Systems Lead.
- **Pain:** MHD drag from transverse fields imposes huge pumping power; corrosion of structural steel; no productized flow-control subsystem.
- **Current workaround:** Bespoke university/lab MHD loops (e.g., UCLA PbLi facility); mechanical pumps unsuited to liquid metal in field.
- **Why current solution fails:** Without electrical insulation/flow-channel inserts and active control, MHD pressure drop and corrosion are unmanaged.
- **Hardware stack:** Annular/EM induction pump, SiC/alumina-coated flow-channel inserts, level/flow/corrosion sensors, heated piping.
- **Software/control stack:** MHD flow model, closed-loop flow/temperature control, corrosion-product tracking.
- **Prototype path 2026–2028:** 2026 small EM pump loop; 2027 insulating-insert flow test in field; 2028 divertor-relevant film demo.
- **China wedge:** ASIPP liquid-metal divertor work; domestic loop fabrication.
- **US wedge:** LLNL/UCLA FNSF liquid-metal first-wall heritage; allied subsystem supply.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Moderate–high (fusion + lithium/PbLi).
- **Competitors:** National-lab in-house, KIT/EU blanket programs.
- **Defensibility:** Insert + control IP; corrosion datasets.
- **Kill criteria:** If solid PFCs (tungsten) remain dominant and liquid-metal PFCs stay research-only past 2030.
- **Evidence status:** CLEARED_WITH_WEAKNESS (frontier-stage; pull market still mostly programmatic).
- **Key sources:** Nuclear Materials & Energy LM PFC review (S26), IOP Nuclear Fusion fast-flow Li divertor (S27), Fusion Eng. & Design UCLA MHD PbLi facility (S28).

---

### EXT-09 — Neutron-tolerant steady-state magnetic sensor module with drift-free observer
- **One-sentence product:** A radiation-hard antimony-Hall + inductive-coil hybrid magnetic field sensor module with a Luenberger/Kalman observer that delivers drift-free field measurement over long-pulse / steady-state fusion discharges.
- **System boundary shift:** Replaces drift-prone integrated pickup coils with a hybrid sensor + observer that survives neutron flux and transmutation for steady-state control.
- **Extreme metric:** Drift-free field measurement for 1,000 s+ pulses at neutron flux ~10^13 cm^-2 s^-1.
- **First high-end customer:** Long-pulse tokamaks (ITER, China EAST/BEST, private long-pulse devices).
- **Buyer title:** Diagnostics & Control Lead.
- **Pain:** Inductive sensors drift over long pulses; radiation causes thermal stress and transmutation; without reliable B-field, plasma control is impossible.
- **Current workaround:** Integrated pickup coils + drift correction; experimental Hall probes.
- **Why current solution fails:** Integrator drift accumulates; standard Hall sensors degrade under neutron flux; no qualified steady-state sensor.
- **Hardware stack:** Sb Hall sensor with W–Ti diffusion barrier, inductive coil, rad-hard packaging, cabling.
- **Software/control stack:** Hybrid-sensor observer (Kalman/Luenberger), in-situ recalibration, drift estimation.
- **Prototype path 2026–2028:** 2026 hybrid probe bench; 2027 irradiation campaign; 2028 install on a long-pulse device.
- **China wedge:** EAST 1,000 s+ pulse program needs exactly this; domestic fab.
- **US wedge:** ITER/DEMO and private long-pulse; allied diagnostic supply.
- **Cleanroom dependency:** Hall die outsourced; module integration in-house.
- **Capex band:** Mid.
- **Regulatory/export risk:** Moderate (fusion diagnostics).
- **Competitors:** ITER diagnostic teams, IPP/CEA labs.
- **Defensibility:** Sensor packaging + observer IP + irradiation qualification.
- **Kill criteria:** If pickup-coil drift correction proves adequate for DEMO-class pulses.
- **Evidence status:** CLEARED.
- **Key sources:** IOP Nuclear Fusion rad-hard Hall + hybrid sensor (S29), Fusion Eng. & Design Sb Hall steady-state diagnostic (S30), Fusion Eng. & Design ITER magnetics set (S31 supporting).

---

### EXT-10 — SiC in-core neutron-flux detector + electronics for advanced fission reactors
- **One-sentence product:** A SiC PIN/Schottky neutron-flux detector with high-temperature readout electronics for in-core and near-core monitoring of HTGRs, microreactors, and molten-salt reactors operating >500 °C.
- **System boundary shift:** Brings solid-state neutron sensing in-core at temperatures that destroy conventional fission chambers and silicon electronics.
- **Extreme metric:** Operation >500 °C (counting demonstrated above 700 °C) and integrated neutron fluence >6×10^15 n/cm².
- **First high-end customer:** Advanced reactor developers (X-energy, Kairos Power, Radiant, Westinghouse eVinci, USNC).
- **Buyer title:** Instrumentation & Controls Lead / Reactor Engineering Manager.
- **Pain:** Gen-IV reactors run hot; existing flux monitors and cabling can't sit in-core; licensing demands qualified instrumentation.
- **Current workaround:** Ex-core fission chambers, self-powered neutron detectors with slow response.
- **Why current solution fails:** Out-of-core placement loses spatial/temporal resolution; conventional detectors degrade at high T and fluence.
- **Hardware stack:** SiC PIN/Schottky diode + 6LiF converter, high-temp ceramic packaging, SiC/HT readout ASIC, mineral-insulated cable.
- **Software/control stack:** Pulse-height discrimination, gamma rejection, neutron-flux reconstruction.
- **Prototype path 2026–2028:** 2026 SiC detector + HT readout bench; 2027 research-reactor irradiation (e.g., university TRIGA); 2028 in-core demo with a reactor developer.
- **China wedge:** China HTGR (Shidaowan) and microreactor programs; domestic SiC.
- **US wedge:** DOE NRIC/INL gateway; advanced-reactor licensing pull; allied SiC.
- **Cleanroom dependency:** SiC die outsourced; packaging/qualification in-house.
- **Capex band:** Mid–High.
- **Regulatory/export risk:** High (nuclear instrumentation, NRC qualification, export).
- **Competitors:** Centronic/Mirion fission chambers, national-lab programs.
- **Defensibility:** Qualification dossier + HT packaging + readout IP.
- **Kill criteria:** If self-powered detectors satisfy advanced-reactor I&C licensing cheaply.
- **Evidence status:** CLEARED.
- **Key sources:** Nature Sci Rep SiC P-N detectors under neutron irradiation at RA-6 (S21), Nucl. Instr. Meth. A SiC near-core high-flux monitoring (S22), EPJ Web of Conf. SiC reactor monitoring (supporting).

---

### EXT-11 — Embedded TPS health-monitoring sensor network for hypersonic vehicles
- **One-sentence product:** A network of subsurface high-temperature (passive RFID/wireless and wired) sensors plus a thermal-inversion engine that reconstructs surface temperature and detects thermal-protection-system damage in real time, feeding flight/thermal control.
- **System boundary shift:** Turns the TPS from a passive, inspected-after-flight skin into an instrumented, self-reporting structure that informs control and reuse decisions.
- **Extreme metric:** Subsurface sensing under skins seeing >1,500–2,000 °C surface, with real-time temperature reconstruction.
- **First high-end customer:** Hypersonic vehicle developers and reusable high-speed platforms (Hermeus, Castelion, Stratolaunch, prime contractors).
- **Buyer title:** Chief Engineer / Thermal Protection Systems Lead.
- **Pain:** TPS failure is catastrophic; current sensors top out ~225 °C; reusable vehicles need post-flight integrity data fast.
- **Current workaround:** Sparse thermocouples, post-flight inspection, conservative margins.
- **Why current solution fails:** CMOS sensors fail at high T; surface temperature can't be directly measured; no embedded health-monitoring network.
- **Hardware stack:** Subsurface high-temp sensors (RFID SensorTag-class, C/C-SiC resistance sensing), wireless interrogation, rad/heat-tolerant electronics in cooler zones.
- **Software/control stack:** Full-time-domain temperature-inversion algorithm, damage detection, sensor-fusion to vehicle health management.
- **Prototype path 2026–2028:** 2026 subsurface sensor + inversion bench (arc-jet coupon); 2027 instrumented leading-edge in arc-jet; 2028 flight-test integration.
- **China wedge:** Strong domestic hypersonics program; dual-use sensitivity high.
- **US wedge:** DoD hypersonics demand explicitly calling for extreme-temperature sensors; allied-only supply.
- **Cleanroom dependency:** Minimal (sensor assembly).
- **Capex band:** Mid (arc-jet access dominates cost).
- **Regulatory/export risk:** High (ITAR/hypersonics).
- **Competitors:** NASA/SRI heritage, prime in-house, academic SHM groups.
- **Defensibility:** Inversion algorithms + high-temp sensor integration + flight qualification.
- **Kill criteria:** If primes keep TPS health monitoring fully in-house, or arc-jet/flight access is unattainable.
- **Evidence status:** CLEARED.
- **Key sources:** NASA NTRS wireless subsurface TPS microsensors (S23), Acta Astronautica large-area TPS review (S24), Sensors (MDPI) full-time-domain temperature inversion (S25).

---

### EXT-12 — Point-of-use helium recovery + reliquefaction skid for fusion/quantum labs
- **One-sentence product:** A compact closed-loop helium recovery + reliquefaction skid that captures boil-off from magnets, cryostats, and dilution refrigerators and returns liquid helium on-site.
- **System boundary shift:** Converts helium from a consumed commodity to a recirculated working fluid at the facility level, decoupling operations from the volatile helium market.
- **Extreme metric:** High recovery fraction of 4 K boil-off with reliquefaction at lab scale, near-zero net helium loss.
- **First high-end customer:** Quantum computing companies, fusion magnet test stands, university/national-lab cryo facilities.
- **Buyer title:** Cryogenic Facilities Manager / Lab Operations Director.
- **Pain:** Helium-4 supply is unstable (geopolitics, declining natural-gas-tied production), prices spike, and shortages halt experiments.
- **Current workaround:** Buy liquid helium, vent boil-off, or large central liquefiers (capex-heavy).
- **Why current solution fails:** Venting wastes scarce helium; central liquefiers are oversized and costly for distributed users.
- **Hardware stack:** Recovery bag/compressor, purifier, GM/pulse-tube cold head, dewar, instrumentation.
- **Software/control stack:** Boil-off prediction, recovery optimization, remote facility telemetry.
- **Prototype path 2026–2028:** 2026 recovery+purify loop; 2027 integrated reliquefaction skid; 2028 deployment at a multi-cryostat customer.
- **China wedge:** China helium import dependence is acute — strong domestic pull; localize cold heads.
- **US wedge:** Allied cryocooler supply; sell to quantum/fusion scaling labs.
- **Cleanroom dependency:** None.
- **Capex band:** Mid.
- **Regulatory/export risk:** Low–moderate.
- **Competitors:** Quantum Design ATL, Bluefors, SHI/Sumitomo, Linde/Air Liquide (large scale).
- **Defensibility:** Skid integration + recovery-control software + service model.
- **Kill criteria:** If helium prices stabilize cheaply or cryogen-free systems eliminate liquid helium entirely.
- **Evidence status:** CLEARED_WITH_WEAKNESS (pain well documented; product is integration of known components).
- **Key sources:** Nature Sci Rep cryogenic cooling material / helium-supply motivation (S33), ITER cryoplant scale (S32 supporting), Lake Shore/SHI pulse-tube vs GM (company, triangulation).

---

### EXT-13 — HTS conductor & joint test-and-qualification platform (SULTAN-class)
- **One-sentence product:** A variable-temperature, high-field, high-current cable/joint test rig with integrated fiber-optic and electrical diagnostics, offered as a product and as qualification-as-a-service for fusion conductors.
- **System boundary shift:** Democratizes the scarce, world-limited high-fidelity HTS conductor test capability (today essentially SULTAN) into a deployable platform.
- **Extreme metric:** High-current (tens of kA), multi-tesla, 4–20 K cyclic testing of full-scale HTS cables with quench instrumentation.
- **First high-end customer:** Fusion magnet developers and conductor suppliers needing acceptance qualification.
- **Buyer title:** Conductor Qualification Lead / Magnet Program Director.
- **Pain:** Global HTS cable test capacity is a bottleneck; queues at SULTAN delay magnet programs.
- **Current workaround:** Wait for SULTAN (PSI) slots; small in-house coil tests.
- **Why current solution fails:** Single-facility dependence; insufficient throughput for the magnet boom.
- **Hardware stack:** Background-field magnet, high-current supply (links EXT-04), variable-temp cryostat, fiber-optic + voltage diagnostics, cyclic loading.
- **Software/control stack:** Automated test sequencing, quench/degradation analytics, conductor performance database.
- **Prototype path 2026–2028:** 2026 sub-scale rig; 2027 high-current cable test; 2028 commercial qualification service.
- **China wedge:** ASIPP/CHMFL test infrastructure; domestic magnet supply chain.
- **US wedge:** Relieve allied magnet builders' dependence on a single European facility.
- **Cleanroom dependency:** None.
- **Capex band:** High–Very High (background magnet + supply).
- **Regulatory/export risk:** Moderate–high (fusion).
- **Competitors:** PSI SULTAN/EDIPO, MIT PSFC test stands.
- **Defensibility:** Capability scarcity + diagnostics + data moat.
- **Kill criteria:** If magnet builders standardize on in-house testing and external qualification demand collapses.
- **Evidence status:** CLEARED.
- **Key sources:** IOP SUST VIPER/SULTAN fiber-optic quench testing (S02), IOP SUST China model-conductor testing (S03), IOP SUST low-Ic conductor analysis (S07).

---

### EXT-14 — MgB2 LH2-cooled MVDC superconducting busway for GW data centers / hydrogen hubs
- **One-sentence product:** A medium-voltage-DC MgB2 superconducting busway cooled by liquid hydrogen that co-distributes bulk electrical power and hydrogen for gigawatt-scale data centers and energy hubs.
- **System boundary shift:** Merges electrical and hydrogen distribution into one cryogenic corridor, removing copper ampacity limits at the campus scale.
- **Extreme metric:** GW-class power at MVDC with MgB2 at ~20 K (LH2), demonstrated kA-class cable and 50 kV DC hold-off.
- **First high-end customer:** Hyperscale data-center developers and hydrogen-hub / e-fuel operators with co-located generation.
- **Buyer title:** Director of Energy Infrastructure / Campus Power Architect.
- **Pain:** GW data centers strain copper busways and substations; siting near generation needs high-density, low-loss transfer.
- **Current workaround:** Massive copper/aluminum busways, multiple HV transformers, separate H2 piping.
- **Why current solution fails:** Copper losses and footprint scale poorly at GW; no integrated power+H2 corridor.
- **Hardware stack:** MgB2 cable, LH2 cryostat/transfer line, current leads (links EXT-05), HVDC terminations, cryo-HV bushings (links EXT-23).
- **Software/control stack:** Cryogenic thermal/fault management, DC protection, leak/quench safety logic.
- **Prototype path 2026–2028:** 2026 short MgB2 MVDC sample test; 2027 ~30 m hybrid line; 2028 campus pilot segment.
- **China wedge:** China MgB2/HTS cable demos and grid programs; domestic LH2 buildout.
- **US wedge:** Data-center power crunch; allied superconductor supply; SCARLET-class learning.
- **Cleanroom dependency:** None.
- **Capex band:** Very High.
- **Regulatory/export risk:** Moderate–high (hydrogen safety, grid interconnection).
- **Competitors:** Nexans/SuperGrid (HTS cables), VEIR, conventional busway makers.
- **Defensibility:** Integrated power+H2 system engineering + safety qualification.
- **Kill criteria:** If LH2 handling/safety proves uneconomic vs HVDC copper, or data-center siting avoids co-location.
- **Evidence status:** CLEARED_WITH_WEAKNESS (technical feasibility shown; deployment economics speculative).
- **Key sources:** IEEE Trans. Applied Superconductivity MgB2 MVDC LH2 cable (S34), Physics Procedia 30 m hybrid LH2/MgB2 line test (S35), SuperGrid/SCARLET (company, triangulation).

---

### EXT-15 — REBCO HTS cabling / CICC manufacturing line
- **One-sentence product:** An automated machine and process line that converts REBCO tape into high-current cables (CORC-class / stacked / cable-in-conduit) with in-line tension, defect, and Ic monitoring for fusion magnets.
- **System boundary shift:** Industrializes the tape-to-cable step that currently limits magnet throughput, with quality designed in.
- **Extreme metric:** Continuous production of multi-kA HTS cable with controlled bending strain and in-line Ic verification.
- **First high-end customer:** Fusion magnet builders and conductor suppliers.
- **Buyer title:** Conductor Manufacturing Director.
- **Pain:** Cabling is slow, strain-sensitive, and largely manual; tape damage during cabling destroys performance.
- **Current workaround:** Semi-manual cabling; CORC/ACT specialized but capacity-limited.
- **Why current solution fails:** Throughput and reproducibility gap vs magnet demand; mechanical loading creates defects.
- **Hardware stack:** Tape-handling/cabling heads, conduit forming, in-line metrology (links EXT-03), tension control.
- **Software/control stack:** Strain/tension control, defect tracking, cable digital passport.
- **Prototype path 2026–2028:** 2026 cabling head + metrology; 2027 multi-kA cable pilot; 2028 line for a magnet builder.
- **China wedge:** SST tape + domestic CICC for EAST/BEST/CFETR; vertical integration.
- **US wedge:** Allied cabling capacity for CFS/Type One; reduce manual labor.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Moderate–high (fusion).
- **Competitors:** Advanced Conductor Technologies (CORC), in-house magnet shops.
- **Defensibility:** Process IP + integrated QC.
- **Kill criteria:** If magnet architectures converge on simple stacked tapes needing no cabling line.
- **Evidence status:** CLEARED.
- **Key sources:** IOP SUST low-Ic conductor analysis (S07), ScienceDirect REBCO stacked-cable joint (S06), Blocks-in-conduit REBCO cable concept (supporting).

---

### EXT-16 — Space-grade radiation-hard GaN power module + SEE-screening service
- **One-sentence product:** A radiation-hardened GaN power module (with SEE-mitigated design and TID/displacement qualification) plus single-event-effect screening service for satellite power and electric propulsion.
- **System boundary shift:** Provides qualified, screened wide-bandgap power for space rather than bare die or silicon, where SEE susceptibility is the unsolved gap.
- **Extreme metric:** GaN operation through GEO radiation environment (demonstrated in multi-year orbit) with SEE-hardened design.
- **First high-end customer:** Satellite-bus and electric-propulsion makers (Apex, Astranis, EP/Hall-thruster suppliers, primes).
- **Buyer title:** Power Systems Lead / Spacecraft Chief Engineer.
- **Pain:** GaN is TID-tolerant but SEE-susceptible to heavy ions; mass-/efficiency-critical buses need qualified wide-bandgap power.
- **Current workaround:** Rad-hard silicon MOSFETs (heavier, less efficient), conservative derating.
- **Why current solution fails:** Silicon limits efficiency/mass; unscreened GaN risks single-event burnout.
- **Hardware stack:** SEE-mitigated GaN module, qualified packaging, screening test interfaces.
- **Software/control stack:** Derating/protection models, SEE rate prediction.
- **Prototype path 2026–2028:** 2026 SEE characterization at accelerator; 2027 hardened module; 2028 flight-qualification lot.
- **China wedge:** Domestic GaN + large LEO constellation demand; export-restricted from US market.
- **US wedge:** NASA NEPP / allied space-grade supply; constellation power demand.
- **Cleanroom dependency:** Die outsourced; module/screening in-house.
- **Capex band:** Mid (heavy-ion beam access dominates).
- **Regulatory/export risk:** High (ITAR/EAR, GaN export controls).
- **Competitors:** Infineon/EPC (commercial GaN), rad-hard Si vendors, in-house prime teams.
- **Defensibility:** SEE-hardening design IP + qualification dataset + screening service.
- **Kill criteria:** If commercial GaN SEE hardness improves to where screening is unnecessary, or rad-hard Si stays good enough.
- **Evidence status:** CLEARED.
- **Key sources:** PMC peer-reviewed 6-year GaN-in-GEO evaluation (S37), Penn State review SEE in SiC/GaN power electronics (S36), Wiley 2024 radiation-damage review (S38).

---

### EXT-17 — Fabless cryo-CMOS multiplexed control/readout subsystem for quantum
- **One-sentence product:** A fabless cryo-CMOS control/readout chiplet + multiplexing subsystem (at the 4 K stage) sold to quantum hardware companies that lack their own custom control ASIC.
- **System boundary shift:** Moves the classical control/readout chain into the cryostat to break the room-temperature wiring bottleneck, as a merchant component rather than an in-house mega-project.
- **Extreme metric:** Per-qubit control/readout dissipation low enough to fit the constrained 4 K cooling budget while multiplexing many channels.
- **First high-end customer:** Spin-qubit, neutral-atom, and small superconducting-qubit companies without in-house cryo-CMOS (e.g., emerging quantum startups).
- **Buyer title:** VP Hardware / Head of Control Systems.
- **Pain:** Coaxial wiring from 300 K doesn't scale past ~hundreds of qubits; only the largest players (IBM/Intel/Google) build their own cryo-CMOS.
- **Current workaround:** Room-temperature AWG/instrument racks + dense cabling.
- **Why current solution fails:** Thermal load and physical wiring limits cap qubit count; bespoke ASICs are out of reach for most.
- **Hardware stack:** Cryo-CMOS controller/readout chiplet, multiplexer, cryo-compatible interconnect, 4 K mounting.
- **Software/control stack:** Pulse compilation, calibration, low-power multiplexing firmware.
- **Prototype path 2026–2028:** 2026 cryo-characterized building blocks; 2027 multiplexed controller at 4 K; 2028 integration with a qubit customer.
- **China wedge:** Domestic quantum programs + foundry; but advanced-node export limits bite.
- **US wedge:** Merchant cryo-control for the long tail of quantum startups; allied foundry.
- **Cleanroom dependency:** Yes (CMOS) — but fabless via foundry (outsourcing path exists).
- **Capex band:** High (tape-outs).
- **Regulatory/export risk:** High (advanced-node + quantum export controls).
- **Competitors:** Intel Horse Ridge, IBM, SemiQon, equipment makers (Qblox/Zurich at 300 K).
- **Defensibility:** Cryo circuit IP + low-power multiplexing + qubit-agnostic interfaces.
- **Kill criteria:** If large players' in-house ASICs and 300 K control suffice for the addressable market, or foundry access is denied.
- **Evidence status:** CLEARED_WITH_WEAKNESS (crowded; strong technical pull, contested market).
- **Key sources:** AIP APL Quantum classical interfaces for cryogenic quantum control (S39), ISSCC/JSSC cryo-CMOS controller literature (supporting), IBM Research cryo-CMOS (company claim).

---

### EXT-18 — High-heat-flux divertor/PFC thermal-qualification test bed
- **One-sentence product:** A high-heat-flux electron-beam/plasma test bed with embedded diagnostics that cyclically qualifies divertor and first-wall components to fusion-relevant heat loads.
- **System boundary shift:** Provides scarce plasma-facing-component qualification capacity as a deployable, instrumented product/service.
- **Extreme metric:** Steady and transient surface heat flux ≥10 MW/m² with cyclic fatigue and in-situ temperature/erosion diagnostics.
- **First high-end customer:** Fusion materials/PFC teams (private fusion + national labs).
- **Buyer title:** PFC/Materials Qualification Lead.
- **Pain:** Few facilities can apply fusion-relevant heat flux; PFC qualification is a bottleneck for DEMO-class designs.
- **Current workaround:** National-lab e-beam facilities (limited slots), HHF labs abroad.
- **Why current solution fails:** Capacity scarcity; limited diagnostics; long queues.
- **Hardware stack:** High-power e-beam/plasma source, actively cooled sample stage, IR/pyrometry, erosion sensors.
- **Software/control stack:** Heat-flux control, fatigue cycling, damage analytics, materials database.
- **Prototype path 2026–2028:** 2026 e-beam HHF cell; 2027 cyclic qualification with diagnostics; 2028 commercial PFC qualification.
- **China wedge:** ASIPP HHF test heritage (EAST divertor); domestic build.
- **US wedge:** Relieve allied PFC qualification bottleneck; tie to private fusion.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Moderate (fusion).
- **Competitors:** Sandia PFCs/IEC HHF facilities, EU labs.
- **Defensibility:** Capability + diagnostics + materials data moat.
- **Kill criteria:** If PFC designs freeze and qualification demand drops, or national labs expand capacity for free.
- **Evidence status:** CLEARED_WITH_WEAKNESS.
- **Key sources:** Nuclear Materials & Energy LM PFC review (S26), IOP Nuclear Fusion fast-flow Li divertor (S27), Acta Astronautica TPS/heat-flux methods (S24 supporting).

---

### EXT-19 — Closed-loop screening-current-stress-aware ramp controller for high-field HTS magnets
- **One-sentence product:** A controller that uses fiber-Bragg strain sensing + an electromagnetic model to manage screening-current-induced stress and field error during HTS magnet ramps, closing the loop on ramp rate (not just monitoring).
- **System boundary shift:** Makes screening-current stress and field distortion an actively controlled variable rather than a static design margin.
- **Extreme metric:** Real-time screening-current stress estimation and ramp-rate control in high-field (≥20 T-class) REBCO coils.
- **First high-end customer:** Ultra-high-field magnet developers (fusion, NMR/MRI, science magnets).
- **Buyer title:** Magnet Controls / Mechanical Integrity Lead.
- **Pain:** Screening currents cause field errors and mechanical stress concentrations that can crack/degrade high-field REBCO coils.
- **Current workaround:** Conservative ramp rates, large mechanical margins, post-hoc shimming.
- **Why current solution fails:** Open-loop margins waste field/cost and don't catch coil-specific stress hot spots.
- **Hardware stack:** Fiber-Bragg strain sensors, field probes, fast power supply interface (links EXT-04).
- **Software/control stack:** Coupled electromagnetic-mechanical model, stress observer, ramp-rate optimizer, alarm-to-control loop.
- **Prototype path 2026–2028:** 2026 strain-instrumented sub-scale coil; 2027 closed-loop ramp control; 2028 high-field integration.
- **China wedge:** CHMFL high-field magnet program (45 T-class); domestic sensing.
- **US wedge:** NHMFL users, fusion primes; allied controller.
- **Cleanroom dependency:** None.
- **Capex band:** Mid.
- **Regulatory/export risk:** Moderate.
- **Competitors:** In-house magnet teams, FBG vendors (sensing only).
- **Defensibility:** Coupled model + control IP + coil datasets.
- **Kill criteria:** If tape transverse-Jc engineering removes screening-current stress as a binding constraint.
- **Evidence status:** CLEARED.
- **Key sources:** AIP J. Applied Physics screening-current EM-force in NI coils (S11), Nature Sci Rep transverse Jc vs screening-current stress (S08), Cryogenics NI charging behavior (S10 supporting).

---

### EXT-20 — Compact high-power 4.5 K helium cryoplant / cold-compressor module for private fusion
- **One-sentence product:** A standardized, factory-built 4.5 K helium refrigeration module (with cold compressors) sized for private-fusion magnet systems, between lab cryocoolers and ITER-scale plants.
- **System boundary shift:** Turns the megawatt-class cryoplant from a bespoke megaproject into a productized, repeatable module for the fusion fleet.
- **Extreme metric:** Multi-kW @ 4.5 K cooling in a containerized, replicable package (ITER's plant is 75 kW @ 4.5 K — the reference point for scale).
- **First high-end customer:** Private fusion companies building pilot plants and magnet test halls.
- **Buyer title:** Cryogenics Systems Director.
- **Pain:** Each fusion magnet program needs large 4.5 K cooling; today's options are tiny cryocoolers or one-off giant plants — nothing in between, and lead times are long.
- **Current workaround:** Air Liquide/Linde custom plants (long lead, high cost) or stacked cryocoolers.
- **Why current solution fails:** Custom plants are slow and expensive; cryocoolers don't reach the needed capacity.
- **Hardware stack:** Helium turbo/cold compressors, heat exchangers, oil-removal, control valves, cold box.
- **Software/control stack:** Plant control, load-following, reliability/predictive maintenance.
- **Prototype path 2026–2028:** 2026 module design + cold-compressor test; 2027 sub-scale plant; 2028 deploy at a fusion test hall.
- **China wedge:** ASIPP cryogenics heritage; domestic plant build; localize compressors.
- **US wedge:** Allied cryoplant supply to private fusion fleet; reduce single-vendor lead times.
- **Cleanroom dependency:** None.
- **Capex band:** Very High.
- **Regulatory/export risk:** Moderate–high (fusion, large rotating machinery).
- **Competitors:** Air Liquide, Linde Kryotechnik, SHI.
- **Defensibility:** Modularization + reliability + service.
- **Kill criteria:** If incumbents productize first, or HTS magnets at 20 K shift cooling away from 4.5 K helium plants.
- **Evidence status:** CLEARED_WITH_WEAKNESS (capability proven at ITER scale; productization/economics unproven).
- **Key sources:** ITER cryogenics 75 kW @ 4.5 K (S32), ScienceDirect ITER cryoplant economics of LHe plants (S32 supporting), Nature Sci Rep helium-supply pressure (S33).

---

### EXT-21 — Rad-hard / high-temperature wireless telemetry & data link for in-vessel fusion and in-containment nuclear
- **One-sentence product:** A radiation- and temperature-tolerant wireless/wired data-link module (SiC/GaN-based) that gets sensor data out of in-vessel fusion and in-containment nuclear locations where standard electronics and cabling fail.
- **System boundary shift:** Extends the sensing edge into zones previously inaccessible to active electronics, enabling control-relevant data from inside the radiation boundary.
- **Extreme metric:** Survives in-vessel neutron flux (~10^13 cm^-2 s^-1) / in-core fluence and high temperature while transmitting reliably.
- **First high-end customer:** Fusion device operators and advanced-reactor developers.
- **Buyer title:** Instrumentation & Controls Lead.
- **Pain:** Cabling and silicon electronics degrade under radiation/heat; running hundreds of leads out of the vessel is impractical.
- **Current workaround:** Long mineral-insulated cable runs, ex-vessel electronics, sparse sensing.
- **Why current solution fails:** Cable count/length and silicon failure limit in-vessel instrumentation density.
- **Hardware stack:** SiC/GaN front-end, rad-hard transceiver, high-temp antenna/feedthrough, links to EXT-09/EXT-10 sensors.
- **Software/control stack:** Robust low-rate protocol, error correction, sensor fusion.
- **Prototype path 2026–2028:** 2026 SiC front-end + link bench; 2027 irradiation/HT test; 2028 in-vessel/in-containment demo.
- **China wedge:** EAST/BEST in-vessel diagnostics demand; domestic SiC.
- **US wedge:** ITER/DEMO + advanced reactors; allied rad-hard supply.
- **Cleanroom dependency:** Die outsourced; module in-house.
- **Capex band:** Mid.
- **Regulatory/export risk:** High (nuclear/fusion, export).
- **Competitors:** National-lab I&C groups, rad-hard electronics vendors.
- **Defensibility:** Rad-hard packaging + protocol IP + qualification.
- **Kill criteria:** If wired mineral-insulated cabling remains adequate and cheaper, or wireless can't meet reliability/licensing.
- **Evidence status:** CLEARED_WITH_WEAKNESS.
- **Key sources:** IOP Nuclear Fusion rad-hard Hall/hybrid sensor (S29), Nucl. Instr. Meth. A SiC near-core (S22), Wiley 2024 radiation-damage review (S38).

---

### EXT-22 — Compact cryocooler-cooled HTS fault-current limiter for dense data-center grid nodes
- **One-sentence product:** A compact, cryocooler-cooled REBCO superconducting fault-current limiter module engineered for data-center campus substations and dense urban grid nodes.
- **System boundary shift:** Brings SFCL from utility-substation one-offs to a packaged module for high-density loads where fault currents are exceeding switchgear ratings.
- **Extreme metric:** Sub-cycle fault-current interruption with REBCO quench-and-recover, cryocooler-cooled (no liquid cryogen).
- **First high-end customer:** Hyperscale data-center power teams and dense urban utilities.
- **Buyer title:** Director of Electrical Infrastructure / Substation Engineering.
- **Pain:** Adding GW of data-center load raises available fault current above existing switchgear ratings; SFCLs are bespoke and bulky.
- **Current workaround:** Splitting buses, series reactors, switchgear upgrades.
- **Why current solution fails:** Reactors add losses; switchgear upgrades are costly/slow; conventional SFCLs are not productized for campuses.
- **Hardware stack:** REBCO fault-limiting elements, cryocooler, vacuum cryostat, MV terminations.
- **Software/control stack:** Fault detection, recovery management, condition monitoring.
- **Prototype path 2026–2028:** 2026 element + cryocooler bench; 2027 MV module; 2028 campus pilot.
- **China wedge:** China grid SFCL deployments + domestic REBCO (SST); strong supply chain.
- **US wedge:** Data-center fault-current crisis; allied superconductor supply.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Moderate.
- **Competitors:** Applied Materials/SuperPower legacy, Nexans, solid-state FCL makers.
- **Defensibility:** Packaging + recovery control + REBCO supply integration.
- **Kill criteria:** If solid-state FCLs or grid reconfiguration win on cost, or REBCO element cost stays too high.
- **Evidence status:** CLEARED_WITH_WEAKNESS (technology real; pain partly evidenced by market data — needs primary-source confirmation of data-center fault-current driver).
- **Key sources:** University at Buffalo record REBCO Jc / SFCL cost trajectory (S40 — verify primary), REBCO capacity expansion for power/fusion (S40 supporting), IEEE TAS HTS applications (S34 supporting).

---

### EXT-23 — Cryogenic high-voltage dielectric qualification & bushing subsystem for superconducting cables
- **One-sentence product:** A cryogenic high-voltage dielectric test capability plus qualified cryo-HV bushings/terminations for superconducting MVDC/HVDC cables and current-lead boxes.
- **System boundary shift:** Treats the cryogenic dielectric/bushing as a qualified subsystem with a data sheet, rather than a project-specific unknown.
- **Extreme metric:** Tens-of-kV DC hold-off across the cold-to-warm boundary at cryogenic temperature (e.g., 50 kV DC demonstrated on MgB2/LH2 leads).
- **First high-end customer:** Superconducting cable developers (EXT-14) and high-current cryogenic power-system builders.
- **Buyer title:** HV/Insulation Systems Engineer.
- **Pain:** Cryogenic HV insulation behavior (partial discharge, breakdown) differs from room temperature and lacks productized, qualified components.
- **Current workaround:** Project-specific bushing designs, ad hoc HV testing.
- **Why current solution fails:** No standardized cryo-HV qualification or off-the-shelf bushings; breakdown physics under-characterized.
- **Hardware stack:** Cryo-HV test cell, PD diagnostics, bushing/termination hardware, current leads (links EXT-05).
- **Software/control stack:** PD analysis, breakdown statistics, insulation database.
- **Prototype path 2026–2028:** 2026 cryo-HV test cell + PD; 2027 qualified bushing; 2028 integrate with a cable demo.
- **China wedge:** China SC cable + grid programs; domestic HV.
- **US wedge:** Allied cable supply chain; data-center MVDC.
- **Cleanroom dependency:** None.
- **Capex band:** Mid.
- **Regulatory/export risk:** Moderate.
- **Competitors:** Cable-maker in-house, HV component vendors.
- **Defensibility:** Cryo-HV dataset + qualified bushing IP.
- **Kill criteria:** If superconducting MVDC/HVDC cable deployment stalls and demand evaporates.
- **Evidence status:** CLEARED_WITH_WEAKNESS.
- **Key sources:** IEEE TAS MgB2 MVDC LH2 (50 kV DC) cable (S34), Physics Procedia LH2/MgB2 line test (S35), Cryogenics current-lead context (S14 supporting).

---

### EXT-24 — Cold-powering feeder & valve-box subsystem for fusion magnet systems
- **One-sentence product:** An integrated cold-powering "feeder" subsystem — HTS current leads, cryogenic valves, instrumentation, and the helium feed/return box — packaged and qualified for fusion magnet systems.
- **System boundary shift:** Bundles the dispersed cold-powering interface (leads + valves + cryo lines + sensors) into one qualified, serviceable module between cryoplant and magnet.
- **Extreme metric:** High-current (tens of kA) powering with minimized 4.5 K heat load and reliable cryogenic valve actuation at the magnet interface.
- **First high-end customer:** Fusion magnet system integrators.
- **Buyer title:** Magnet Systems / Cryogenics Integration Lead.
- **Pain:** The feeder/valve-box interface is complex, leak-prone, and largely bespoke; it gates magnet commissioning.
- **Current workaround:** Custom feeders engineered per project; mix of vendors.
- **Why current solution fails:** Per-project complexity, long lead times, reliability/leak risk at cryo joints and valves.
- **Hardware stack:** HTS current leads (EXT-05), cryogenic valves/actuators, helium feed box, instrumentation, vacuum jacketing.
- **Software/control stack:** Feeder control, leak/thermal monitoring, interlocks.
- **Prototype path 2026–2028:** 2026 lead+valve box bench; 2027 integrated feeder; 2028 magnet-system integration.
- **China wedge:** ASIPP feeder heritage (ITER feeders built in China); strong domestic capability.
- **US wedge:** Allied feeder supply for private fusion; reduce bespoke engineering.
- **Cleanroom dependency:** None.
- **Capex band:** High.
- **Regulatory/export risk:** Moderate–high (fusion).
- **Competitors:** ASIPP, national labs, cryogenic systems integrators.
- **Defensibility:** Integration + qualification + reliability data.
- **Kill criteria:** If magnet builders keep feeders fully in-house and won't buy a module.
- **Evidence status:** CLEARED_WITH_WEAKNESS.
- **Key sources:** ITER cryogenics/feeder system (S32), Cryogenics conduction-cooled current leads (S14), Cryogenics cryocooled magnet optimization (S09 supporting).

---

## 3. Source rows (28)

Quality tiers: **PR-Q1/Q2** = peer-reviewed Q1/Q2 journal or flagship conference; **AUTH** = authoritative non-article (gov / national-lab / international agency / standards); **TRI** = triangulation only (company / market / think tank / new-unranked journal). DOIs/PIIs taken directly from live search results.

| SID | Citation (journal / body) | URL | Tier | Supports candidates | Evidence status |
|-----|---------------------------|-----|------|--------------------|-----------------|
| S01 | Quench detection for HTS magnets: Rayleigh-backscattering interrogated optical fibers — *Superconductor Science and Technology* (IOP, Q1) | https://iopscience.iop.org/article/10.1088/0953-2048/29/3/03LT01 | PR-Q1/Q2 | EXT-01 | CLEARED |
| S02 | Fiber-optic quench detection for large-scale HTS magnets demonstrated on VIPER cable at SULTAN — *Superconductor Science and Technology* (IOP, Q1) | https://iopscience.iop.org/article/10.1088/1361-6668/abdba8 | PR-Q1/Q2 | EXT-01, EXT-13 | CLEARED |
| S03 | Quench detection by fiber-optic sensors for HTS model conductors of China's next-generation fusion magnets — *Superconductor Science and Technology* (IOP, Q1) | https://iopscience.iop.org/article/10.1088/1361-6668/ae6984 | PR-Q1/Q2 | EXT-01, EXT-13 | CLEARED |
| S04 | IntelliMIK: intelligent quench detection method for fusion devices — *Nuclear Fusion* (IOP, Q1, high impact) | https://iopscience.iop.org/article/10.1088/1741-4326/adb0dd | PR-Q1/Q2 | EXT-01 | CLEARED |
| S05 | Soldered joints — an essential component of demountable HTS fusion magnets — *Superconductor Science and Technology* (IOP, Q1) | https://iopscience.iop.org/article/10.1088/0953-2048/29/7/075005 | PR-Q1/Q2 | EXT-02 | CLEARED |
| S06 | A low-resistance joint of REBCO stacked cable for large-scale superconducting magnets — *Superconductivity* (Elsevier) | https://www.sciencedirect.com/science/article/pii/S2772830725000420 | PR-Q1/Q2 (new journal, verify) | EXT-02, EXT-15 | CLEARED_WITH_WEAKNESS |
| S07 | Analysis of current and heat transfer in locations with reduced critical current in coated-conductor tape — *Superconductor Science and Technology* (IOP, Q1) | https://iopscience.iop.org/article/10.1088/1361-6668/ad6484 | PR-Q1/Q2 | EXT-03, EXT-13, EXT-15 | CLEARED |
| S08 | Transverse variability of Jc mitigates screening-current stress in high-field REBCO magnets — *Scientific Reports* (Nature) | https://www.nature.com/articles/s41598-024-81902-0 | PR-Q1/Q2 | EXT-03, EXT-19 | CLEARED |
| S09 | Optimization of operating temperature in cryocooled HTS magnets — *Cryogenics* (Elsevier, Q2) | https://www.sciencedirect.com/science/article/abs/pii/S0011227502001479 | PR-Q1/Q2 | EXT-05, EXT-24 | CLEARED |
| S10 | Charging-delay elimination of solder-impregnated HTS coils with specific excitation current — *Cryogenics* (Elsevier, Q2) | https://www.sciencedirect.com/science/article/abs/pii/S0011227524001000 | PR-Q1/Q2 | EXT-04, EXT-19 | CLEARED |
| S11 | Effect of screening current on electro-magnetic-force of high-field no-insulated coils — *Journal of Applied Physics* (AIP, Q1/Q2) | https://pubs.aip.org/aip/jap/article/137/9/093906 | PR-Q1/Q2 | EXT-19 | CLEARED |
| S12 | Power supply system for 45 T hybrid magnet superconducting outsert at CHMFL — *Cryogenics* (Elsevier, Q2) | https://www.sciencedirect.com/science/article/abs/pii/S0921453423001752 | PR-Q1/Q2 | EXT-04, EXT-19 | CLEARED |
| S13 | HTS transformer-rectifier flux pump for no-insulation magnet — *Cryogenics* (Elsevier, Q2) | https://www.sciencedirect.com/science/article/abs/pii/S0921453418303368 | PR-Q1/Q2 | EXT-04 | CLEARED |
| S14 | Design/experiment of conduction-cooling HTS current leads for wiggler magnets — *Cryogenics* (Elsevier, Q2) | https://www.sciencedirect.com/science/article/abs/pii/S0921453423002241 | PR-Q1/Q2 | EXT-05, EXT-23, EXT-24 | CLEARED |
| S16 | High-Temperature Tools and Sensors, Down-hole Pumps and Drilling — US DOE EERE; NREL HT electronics | https://www.energy.gov/eere/geothermal/high-temperature-tools-and-sensors-down-hole-pumps-and-drilling | AUTH | EXT-06 | CLEARED |
| S17 | Thermal management systems for electronics in deep downhole environment: a review — *Int. Communications in Heat and Mass Transfer* (Elsevier, Q1) | https://www.sciencedirect.com/science/article/abs/pii/S0735193322005723 | PR-Q1/Q2 | EXT-06 | CLEARED |
| S18 | Drilling for Superhot Geothermal Energy: A Technology Gap — Stanford Geothermal Workshop proceedings | https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2025/Pearce.pdf | AUTH (institutional/workshop) | EXT-06 | CLEARED_WITH_WEAKNESS |
| S19 | SiC and GaN Devices With Cryogenic Cooling — US DOE/OSTI national-lab report | https://www.osti.gov/servlets/purl/1817397 | AUTH | EXT-07 | CLEARED |
| S20 | GaN-based cryogenic-temperature power electronics for superconducting motors (cryo-electric aircraft) — peer-reviewed (verify venue) | https://orca.cardiff.ac.uk/id/eprint/161404/1/pdf.pdf | PR-Q1/Q2 (verify) | EXT-07 | CLEARED_WITH_WEAKNESS |
| S21 | SiC P-N detectors under thermal/fast neutron irradiation at RA-6 reactor — *Scientific Reports* (Nature) | https://www.nature.com/articles/s41598-025-32175-8 | PR-Q1/Q2 | EXT-10 | CLEARED |
| S22 | SiC detectors for high-flux neutron monitoring at near-core locations — *Nuclear Instruments and Methods A* (Elsevier, Q2) | https://www.sciencedirect.com/science/article/abs/pii/S0168900219314433 | PR-Q1/Q2 | EXT-10, EXT-21 | CLEARED |
| S23 | Wireless subsurface microsensors for health monitoring of TPS on hypersonic vehicles — NASA NTRS (+ SPIE proc.) | https://ntrs.nasa.gov/citations/20010097314 | AUTH | EXT-11 | CLEARED |
| S24 | Review of large-area thermal-protection structures for hypersonic vehicles — *Acta Astronautica* (Elsevier, Q1) | https://www.sciencedirect.com/science/article/abs/pii/S009457652500205X | PR-Q1/Q2 | EXT-11, EXT-18 | CLEARED |
| S25 | Real-time TPS surface-temperature sensor via full-time-domain inversion — *Sensors* (MDPI, Q1/Q2) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11991591/ | PR-Q1/Q2 | EXT-11 | CLEARED |
| S26 | Recent progress in liquid-metal plasma-facing components for magnetic fusion — *Nuclear Materials and Energy* (Elsevier, Q1/Q2) | https://www.sciencedirect.com/science/article/pii/S2352179124001996 | PR-Q1/Q2 | EXT-08, EXT-18 | CLEARED |
| S27 | Fast-flow liquid-Li divertor for FNSF (coupled plasma + LM MHD/heat-transfer) — *Nuclear Fusion* (IOP, Q1) | https://iopscience.iop.org/article/10.1088/1741-4326/ad3a7b | PR-Q1/Q2 | EXT-08, EXT-18 | CLEARED |
| S28 | Construction and initial operation of MHD PbLi facility at UCLA — *Fusion Engineering and Design* (Elsevier, Q1/Q2) | https://www.sciencedirect.com/science/article/abs/pii/S0920379613003128 | PR-Q1/Q2 | EXT-08 | CLEARED |
| S29 | Long-term operation of radiation-hard Hall probes + path to hybrid magnetic field sensor — *Nuclear Fusion* (IOP, Q1) | https://iopscience.iop.org/article/10.1088/1741-4326/ac8aad | PR-Q1/Q2 | EXT-09, EXT-21 | CLEARED |
| S30 | Steady-state magnetic diagnostic based on antimony Hall sensors for fusion reactors — *Fusion Engineering and Design* (Elsevier, Q1/Q2) | https://www.sciencedirect.com/science/article/abs/pii/S0920379619300183 | PR-Q1/Q2 | EXT-09 | CLEARED |
| S32 | ITER cryoplant: 75 kW @ 4.5 K helium refrigeration — ITER Organization / Fusion for Energy | https://www.iter.org/machine/supporting-systems/cryogenics | AUTH | EXT-12, EXT-20, EXT-24 | CLEARED |
| S33 | Innovative cryogenic cooling material from abundant elements (helium-supply pressure) — *Scientific Reports* (Nature) | https://www.nature.com/articles/s41598-025-29709-5 | PR-Q1/Q2 | EXT-12, EXT-20 | CLEARED |
| S34 | MgB2-based MVDC superconducting power cable in liquid hydrogen — *IEEE Trans. Applied Superconductivity* (Q2) | https://ieeexplore.ieee.org/document/10380545/ | PR-Q1/Q2 | EXT-14, EXT-22, EXT-23 | CLEARED |
| S36 | Review: opportunities in single-event effects in radiation-exposed SiC/GaN power electronics — Penn State (peer-reviewed, verify venue) | https://pure.psu.edu/en/publications/review-opportunities-in-single-event-effects-in-radiation-exposed/ | PR-Q1/Q2 (verify) | EXT-16 | CLEARED_WITH_WEAKNESS |
| S37 | Pioneering evaluation of GaN transistors in geostationary satellites (6-yr Alphasat) — peer-reviewed (PMC-indexed) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9334328/ | PR-Q1/Q2 | EXT-16 | CLEARED |
| S38 | Overview of radiation-damage effects and protection in microelectronics (2024) — *Science and Technology of Nuclear Installations* (Wiley) | https://onlinelibrary.wiley.com/doi/10.1155/2024/3616902 | PR-Q1/Q2 (moderate) | EXT-16, EXT-21 | CLEARED_WITH_WEAKNESS |
| S39 | Classical interfaces for controlling cryogenic quantum computing technologies — *APL Quantum* (AIP) | https://pubs.aip.org/aip/apq/article/2/4/041501/3373674 | PR-Q1/Q2 (newer venue) | EXT-17 | CLEARED_WITH_WEAKNESS |
| S40 | REBCO capacity expansion + record Jc / SFCL cost trajectory (industry triangulation) — superconductor market overview | https://www.globenewswire.com/news-release/2025/01/10/3007450/0/en/Superconductors-Materials-Products-and-Applications-Overview-2024.html | TRI | EXT-22 (also context for EXT-02/03/15) | WEAK_SIGNAL_ONLY |

Additional context sources (triangulation / timing only, not counted as proof):
- Shanghai Superconductor REBCO 2,000→4,000 km/yr capacity — company/industry (CERN indico presentation + SST site) — TRI/company claim.
- China fusion ~$6.5B buildout; EAST/BEST/CFETR — UC IGCC think-tank analysis + Reuters timing — TRI.
- ITER cryoplant commissioning timeline — Fusion for Energy (F4E) — AUTH/timing.
- Quaise/Fervo downhole approaches — company claims + New Atlas/ITIF — company/TRI.

---

## 4. Rejected ideas (7)

1. **Generic cryogenic-asset monitoring dashboard.** Pure monitoring with no control/protection action — violates the monitoring-only anti-pattern. Rejected.
2. **"China clone" of a US REBCO tape maker with no wedge.** Tape manufacturing is already led by Chinese/Japanese players; a me-too tape line has no defensible wedge. Rejected (kept the QC/cabling/joint *engine-layer* tools instead).
3. **Room-temperature superconductor productization.** Claims remain unreplicated; treating it as a near-term product is regulatory/physics speculation treated as fact. Rejected.
4. **Standalone bulk SMES for grid arbitrage.** Energy density and cost make bulk SMES uncompetitive vs batteries; only pulsed/niche cases survive, which is too thin for a flagship. Rejected (fast-pulse niche folded as a watch-item, not a candidate).
5. **General-purpose dilution-refrigerator clone.** Bluefors/Oxford/ICE dominate; a me-too fridge without a differentiated subsystem is conservative procurement, not frontier. Rejected (kept fabless cryo-CMOS and helium-recovery instead).
6. **MRI cryogen-reduction retrofit kit.** Established vendors (GE/Siemens/Philips) and a conservative, regulated, slow-moving market; not boundary-shifting. Rejected.
7. **Fusion "digital twin" software platform.** Software-only, no hardware boundary shift, crowded, and doesn't change a physical control loop on its own. Rejected.

---

## 5. Top 5 from the EXTREME lane

Ranked on: strength of peer-reviewed pain evidence, clear first product + first buyer, engine-layer defensibility, and a real China feasibility story.

1. **EXT-01 — Distributed fiber-optic quench detection + protection for HTS magnets.** Best-evidenced (4 strong IOP/Nature-class sources incl. SULTAN/VIPER and a China next-gen fusion-magnet study), unambiguous detection-to-actuation loop, and every HTS magnet builder needs it. The clearest engine-layer wedge.
2. **EXT-06 — SiC superhot-geothermal downhole electronics module (>300 °C).** Hard physical wall (silicon dies ~175 °C) that blocks a whole industry; DOE/NREL-backed pain; concrete MWD product and named buyers; dual oil & gas + geothermal demand de-risks timing.
3. **EXT-10 — SiC in-core neutron-flux detector + electronics for advanced fission.** Nature/NIM-A-backed, a licensing-driven must-have for Gen-IV/microreactors, clear buyers, defensible via qualification dossier. (Export/NRC risk is the main caveat.)
4. **EXT-03 — In-line REBCO tape Jc/defect QC inspection platform.** Sits at the throat of the entire HTS magnet supply chain; strong IOP/Nature evidence that tape non-uniformity is the dominant performance risk; sells to both Chinese and allied tape scale-ups.
5. **EXT-09 — Neutron-tolerant steady-state magnetic sensor module with drift-free observer.** Steady-state plasma control is impossible without it; strong Nuclear-Fusion/FED evidence; directly pulled by EAST/BEST long-pulse and ITER/DEMO; changes the control loop (not monitoring).

Runners-up: EXT-02 (qualified joints), EXT-05 (cryogen-free current leads), EXT-07 (cryo SiC/GaN modules).

---

## 6. CSV-ready candidate rows

All fields quoted; internal separators use semicolons. Header first.

```csv
candidate_id,candidate_name,one_sentence_product,system_boundary_shift,extreme_metric,first_customer,buyer_title,pain,current_workaround,why_current_fails,hardware_stack,software_control_stack,prototype_path_2026_2028,china_wedge,us_wedge,cleanroom_dependency,capex_band,reg_export_risk,competitors,defensibility,kill_criteria,evidence_status,key_sources
"EXT-01","Distributed fiber-optic quench detection + protection for HTS magnets","Co-wound Rayleigh/OFDR fiber interrogator + firmware that detects/localizes HTS normal zones and fires protection","Lumped voltage taps -> distributed EM-immune optical detection-to-actuation loop","Sub-second normal-zone detection at <1 cm resolution in tokamak EM noise","Commonwealth Fusion; Tokamak Energy; Type One","Head of Magnet Engineering","Undetected HTS quench destroys multi-M$ coil; voltage detection too slow/noisy","Voltage taps + multi-stage inductive-voltage compensation","HTS quench propagation slow; tiny voltage buried in induced/ramp voltage","Polyimide fiber co-wound; OFDR interrogator; cryo feedthroughs; FPGA trip to dump/heaters","Real-time backscatter inversion; temp/strain discrimination; ML classifier; trip logic","2026 77K pancake; 2027 4.2K REBCO coil; 2028 closed-loop dump on customer coil","ASIPP next-gen fusion magnet program already publishing fiber quench studies","Sell qualification+integration to private fusion; allied interrogator supply","None","Mid","Moderate (fusion dual-use)","CFS/MIT in-house; Luna; academic groups","Calibration datasets across REBCO geometries + trip-latency IP + track record","Voltage+compensation reaches adequate latency at scale by 2028","CLEARED","S01;S02;S03;S04"
"EXT-02","Qualified low-resistance HTS joint manufacturing system","Automated soldered/bridge joint tooling + 4K/77K resistance & mechanical qualification sold as qualified joints and as a line","Hand-made artisan joint -> specified traceable qualified component","Reproducible 1-50 nOhm joint at 4K with documented strength to >12 T","Fusion magnet integrators; accelerator/high-field labs","Magnet Manufacturing Lead","Demountable/large magnets need many reproducible low-R joints; yield bottleneck","Manual soldered lap joints; sampled testing","Solder + REBCO/Ag interface resistivity dominate and vary; no qualified joint","Alignment/lamination press; controlled reflow; 4-point cryo probe; tensile rig","Process-recipe control; SPC database; per-joint digital passport","2026 bench joint+77K QA; 2027 4K qualification line; 2028 pilot supply","Co-locate with SST/ASIPP magnet lines; domestic CICC","Allied joint supply for CFS/Type One; cut hand labor","None","Mid","Moderate (fusion)","ACT; in-house shops; CORC","Recipe IP + qualification dataset + tooling","Magnets move to jointless winding or variability immaterial","CLEARED","S05;S06"
"EXT-03","In-line REBCO tape Jc/defect QC inspection platform","High-throughput contactless reel-to-reel Jc-mapping + defect classification that grades/cuts tape","End-of-line 77K spot checks -> high-res in-line Jc/defect mapping tied to in-field performance","~1 mm-resolution Jc over >100 m with in-field (high-B) correlation","REBCO tape makers; fusion magnet winders","VP Manufacturing / Quality Director","Jc non-uniformity & slitting defects are largest magnet performance risk","TapeStar-class 77K self-field scanners","Self-field 77K Jc poorly predicts in-field magnet performance","Reel-to-reel transport; Hall/inductive heads; in-field cryo module; XRD/optical","EM inversion for Jc; ML defect classifier; cut-plan optimizer; tape passport","2026 77K mapping head; 2027 in-field correlation; 2028 in-line pilot at vendor","Sell into SST / Shanghai Creative scaling lines","Allied QC for MetOx/Faraday/SuperPower; acceptance specs","None","Mid","Low-moderate","THEVA/Bruker TapeStar; in-house metrology","Inversion algorithms + in-field correlation dataset + integration","Tape Jc uniformity improves so defect mapping commoditized","CLEARED","S07;S08"
"EXT-04","HTS magnet charging + active quench-protection control platform","High-stability supply + model-based controller (+flux-pump) for NI/LR HTS magnets with active charging/protection","Separate supply/charger/protection -> unified closed-loop control platform","<0.1 ppm ripple / 10 ppm/4h with active NI ramp control","High-field NI/LR magnet developers; fusion test programs","Magnet Controls Engineer","NI coils self-protect but have long charging delay & nonlinear field; bespoke","Lab-built linear+switching supplies; manual PI; separate detection","Charging delay & screening stress coil-specific; ripple drives AC loss","Pre-regulated switching+linear final; flux-pump option; current/field sensing; dump","Coil EM model; charging-delay observer; ramp optimizer; trip logic","2026 supply+PI on NI coil; 2027 flux-pump variant; 2028 integrate EXT-01/EXT-19","CHMFL 45T-class hybrid magnet supply expertise","NHMFL users + fusion primes; allied controller","None","Mid","Moderate","Cryomagtech; American Magnetics; Magna-Power","Control IP + coil-model library + bundled detection","Insulated coils dominate; charging-delay control unneeded","CLEARED","S12;S13;S10"
"EXT-05","Cryogen-free conduction-cooled HTS current-lead modules","Binary copper+HTS conduction-cooled current-lead modules with integrated thermometry","Helium-vapor brass leads / lab-built -> specified drop-in cryogen-free module","Minimized refrigerator power per kA; near-zero standing helium","Cryogen-free HTS magnet builders; fusion test stands","Cryogenic Systems Engineer","Current leads dominate heat load; helium-vapor cooling supply-constrained","Vapor-cooled brass or custom HTS leads per project","Helium dependence; per-project redesign; no optimized module","Cu upper stage; HTS lower stage; thermal intercepts; sensors","Thermal model + lead over-temp protection logic","2026 single lead at rated I; 2027 100-2000A family; 2028 customer integration","Pair with domestic cryocoolers + SST tape; fast localization","Allied cryogen-free supply as helium tightens","None","Low-Mid","Low-moderate","American Magnetics; HTS-110; in-house","Optimization + qualification + integrated protection","Commodity pricing collapses margins; helium eases","CLEARED","S14;S09"
"EXT-06","SiC superhot-geothermal downhole electronics & telemetry module (>300C)","SiC downhole sensing+telemetry module rated for continuous 300-450C deep wells","Active downhole electronics past ~175C silicon wall into supercritical regime","Continuous active operation >=300C (target 400C) at >20000 psi","Superhot/EGS drillers (Quaise; Mazama; Fervo deep); HT oil&gas","Drilling Technology Director","At >=400C steel weakens, elastomers fail, electronics fry; sensors top ~175C","Flask-cooled silicon tools; mud-pulse telemetry; or drill blind","Active cooling & elastomer pulsers degrade; CMOS cannot survive supercritical","SiC/AlGaN sensors+power devices; HT packaging; ceramic substrate; SiC telemetry","HT drift compensation; fault-tolerant link; edge inference","2026 SiC sensor+amp 300C bench; 2027 packaged module in HT oven/well; 2028 EGS field trial","China deep-drilling & SiC programs; CGS/CNPC HT well demand","DOE/NREL HT-electronics ecosystem; allied SiC (export-controlled)","Yes for SiC die but outsource to foundry; focus on packaging","Mid-High","Moderate (SiC export)","SLB; Baker Hughes; NREL/Sandia","HT packaging + qualification + drift-compensation IP","Superhot geothermal stalls & HT O&G alone insufficient; 400C packaging fails","CLEARED","S16;S17;S18"
"EXT-07","Cryogenic SiC/GaN power module + gate-driver subsystem (20-77K)","Characterized packaged GaN/SiC module + cryo-rated gate driver for 20-77K cold space","Warm power electronics -> conversion inside the cryostat; cryo-packaged devices","MW-class conversion with GaN dynamic Rds-on multi-fold lower at cryo vs 300K","Cryo-electric aircraft & superconducting-machine developers; cryo data-center R&D","Power Electronics Lead / Chief Engineer","Warm electronics force lossy current leads across cold boundary; modules uncharacterized","Room-temp inverters + high-current cryogenic feedthroughs","Feedthrough heat & Cu losses dominate; device behavior shifts at cryo","GaN HEMT/SiC MOSFET modules; cryo gate driver; low-CTE packaging; cryo caps","Cryo device models; temp-adaptive gate control; protection","2026 device cryo characterization; 2027 kW driver+module 77K; 2028 sub-MW 20-77K demo","Domestic GaN/SiC + SC machine programs; localize packaging","DOE national-lab cryo base; allied wide-bandgap supply","Outsourced die; packaging/test in-house","Mid","Moderate-high (GaN/SiC + propulsion)","GE Aerospace; Airbus UpNext; module makers (300K only)","Cryo characterization library + packaging + gate-drive IP","Cryo-electric propulsion slips & no SC-machine pull","CLEARED","S19;S20"
"EXT-08","Liquid-metal MHD flow-control + EM-pump skid for fusion PFC/blanket","EM-pump + MHD flow-control skid with insulating inserts and flow/level/corrosion diagnostics for Li/PbLi","One-off lab loops -> controllable instrumented flow subsystem with managed MHD drop","Stable flowing-Li film >=10 MW/m2 peak heat flux with MHD pressure-drop mitigation","Liquid-metal divertor/blanket programs (labs; private fusion)","Blanket/PFC Systems Lead","Transverse-field MHD drag huge pumping power; corrosion; no flow-control product","Bespoke lab MHD loops (UCLA PbLi); mechanical pumps unsuited in field","Without insulation/inserts & control, MHD drop & corrosion unmanaged","Annular/EM induction pump; SiC/alumina-coated inserts; level/flow/corrosion sensors; heated piping","MHD flow model; closed-loop flow/temp control; corrosion tracking","2026 small EM pump loop; 2027 insert flow test in field; 2028 divertor-relevant film demo","ASIPP liquid-metal divertor work; domestic loop fab","LLNL/UCLA FNSF heritage; allied subsystem supply","None","High","Moderate-high (fusion + Li/PbLi)","National-lab in-house; KIT/EU blanket programs","Insert + control IP; corrosion datasets","Solid tungsten PFCs dominate; LM PFCs stay research-only past 2030","CLEARED_WITH_WEAKNESS","S26;S27;S28"
"EXT-09","Neutron-tolerant steady-state magnetic sensor module with drift-free observer","Rad-hard Sb-Hall + inductive-coil hybrid sensor + Kalman observer for drift-free long-pulse B-field","Drift-prone integrated pickup coils -> hybrid sensor + observer surviving neutron flux","Drift-free field for 1000s+ pulses at neutron flux ~1e13 cm-2 s-1","Long-pulse tokamaks (ITER; EAST/BEST; private long-pulse)","Diagnostics & Control Lead","Inductive sensors drift; radiation causes thermal stress & transmutation; no qualified sensor","Integrated pickup coils + drift correction; experimental Hall probes","Integrator drift accumulates; standard Hall degrades under neutrons","Sb Hall (W-Ti barrier); inductive coil; rad-hard packaging; cabling","Hybrid-sensor observer (Kalman/Luenberger); in-situ recalibration","2026 hybrid probe bench; 2027 irradiation campaign; 2028 install on long-pulse device","EAST 1000s+ pulse program needs this; domestic fab","ITER/DEMO + private long-pulse; allied diagnostic supply","Hall die outsourced; module in-house","Mid","Moderate (fusion)","ITER diagnostic teams; IPP/CEA","Sensor packaging + observer IP + irradiation qualification","Pickup-coil drift correction adequate for DEMO pulses","CLEARED","S29;S30"
"EXT-10","SiC in-core neutron-flux detector + electronics for advanced fission reactors","SiC PIN/Schottky neutron detector + HT readout for in-core monitoring of HTGR/microreactor/MSR >500C","Out-of-core fission chambers -> in-core solid-state sensing at high T/fluence","Operation >500C (counting >700C); fluence >6e15 n/cm2","Advanced reactor developers (X-energy; Kairos; Radiant; eVinci; USNC)","I&C Lead / Reactor Engineering Manager","Gen-IV runs hot; flux monitors & cabling cannot sit in-core; licensing needs qualified I&C","Ex-core fission chambers; slow self-powered detectors","Out-of-core loses resolution; conventional detectors degrade at high T/fluence","SiC PIN/Schottky + 6LiF; HT ceramic packaging; SiC/HT readout ASIC; MI cable","Pulse-height discrimination; gamma rejection; flux reconstruction","2026 detector+HT readout bench; 2027 research-reactor irradiation; 2028 in-core demo","China HTGR (Shidaowan) & microreactor programs; domestic SiC","DOE NRIC/INL gateway; licensing pull; allied SiC","SiC die outsourced; packaging/qualification in-house","Mid-High","High (NRC qualification + export)","Centronic/Mirion; national-lab programs","Qualification dossier + HT packaging + readout IP","Self-powered detectors satisfy advanced-reactor I&C cheaply","CLEARED","S21;S22"
"EXT-11","Embedded TPS health-monitoring sensor network for hypersonic vehicles","Subsurface HT sensor network + thermal-inversion engine reconstructing surface temp & detecting TPS damage in real time, feeding control","Passive inspected-after-flight skin -> instrumented self-reporting structure feeding control","Subsurface sensing under >1500-2000C skin with real-time temp reconstruction","Hypersonic & reusable high-speed developers (Hermeus; Castelion; Stratolaunch; primes)","Chief Engineer / TPS Lead","TPS failure catastrophic; sensors top ~225C; reusables need fast integrity data","Sparse thermocouples; post-flight inspection; conservative margins","CMOS fails at high T; surface temp not directly measurable; no embedded network","Subsurface HT sensors (RFID SensorTag; C/C-SiC resistance); wireless interrogation; electronics in cool zones","Full-time-domain temp-inversion; damage detection; fusion to vehicle health mgmt","2026 sensor+inversion arc-jet coupon; 2027 instrumented leading edge in arc-jet; 2028 flight-test integration","Strong domestic hypersonics; dual-use sensitive","DoD hypersonics explicitly needs extreme-T sensors; allied-only","Minimal (sensor assembly)","Mid","High (ITAR/hypersonics)","NASA/SRI heritage; prime in-house; academic SHM","Inversion algorithms + HT sensor integration + flight qualification","Primes keep TPS SHM in-house; no arc-jet/flight access","CLEARED","S23;S24;S25"
"EXT-12","Point-of-use helium recovery + reliquefaction skid for fusion/quantum labs","Compact closed-loop helium recovery + reliquefaction skid returning LHe on-site","Helium as consumed commodity -> recirculated working fluid at facility level","High recovery fraction of 4K boil-off with near-zero net helium loss","Quantum companies; fusion magnet test stands; university/national-lab cryo facilities","Cryogenic Facilities Manager","He-4 supply unstable; price spikes & shortages halt experiments","Buy LHe & vent boil-off; or large central liquefiers","Venting wastes scarce helium; central liquefiers oversized/costly for distributed users","Recovery bag/compressor; purifier; GM/pulse-tube cold head; dewar; instrumentation","Boil-off prediction; recovery optimization; remote telemetry","2026 recovery+purify loop; 2027 integrated skid; 2028 multi-cryostat deployment","China He import dependence acute -> strong pull; localize cold heads","Allied cryocooler supply; sell to quantum/fusion scaling labs","None","Mid","Low-moderate","Quantum Design ATL; Bluefors; SHI; Linde/Air Liquide","Skid integration + recovery-control software + service model","Helium prices stabilize cheap; cryogen-free eliminates LHe","CLEARED_WITH_WEAKNESS","S33;S32"
"EXT-13","HTS conductor & joint test-and-qualification platform (SULTAN-class)","Variable-temp high-field high-current cable/joint test rig + diagnostics, as product and qualification-as-a-service","Single scarce facility (SULTAN) -> deployable conductor qualification platform","Tens-of-kA, multi-T, 4-20K cyclic testing of full-scale HTS cables","Fusion magnet developers & conductor suppliers needing acceptance qualification","Conductor Qualification Lead / Program Director","Global HTS cable test capacity is a bottleneck; queues delay magnet programs","Wait for SULTAN slots; small in-house coil tests","Single-facility dependence; insufficient throughput for magnet boom","Background-field magnet; high-current supply; variable-temp cryostat; fiber+voltage diagnostics; cyclic loading","Automated sequencing; quench/degradation analytics; conductor database","2026 sub-scale rig; 2027 high-current cable test; 2028 commercial qualification service","ASIPP/CHMFL test infrastructure; domestic supply chain","Relieve allied dependence on single European facility","None","High-Very High","Moderate-high (fusion)","PSI SULTAN/EDIPO; MIT PSFC stands","Capability scarcity + diagnostics + data moat","Builders standardize in-house testing; external demand collapses","CLEARED","S02;S03;S07"
"EXT-14","MgB2 LH2-cooled MVDC superconducting busway for GW data centers / H2 hubs","MVDC MgB2 superconducting busway cooled by liquid hydrogen co-distributing power and hydrogen","Separate power + H2 distribution -> single cryogenic corridor beyond copper ampacity","GW-class power at MVDC with MgB2 at ~20K; kA cable & 50 kV DC hold-off shown","Hyperscale data-center developers; hydrogen-hub/e-fuel operators","Director of Energy Infrastructure / Campus Power Architect","GW data centers strain copper busways & substations; siting near generation needs density","Massive copper/Al busways; multiple HV transformers; separate H2 piping","Copper losses/footprint scale poorly at GW; no integrated power+H2 corridor","MgB2 cable; LH2 cryostat/transfer line; current leads; HVDC terminations; cryo-HV bushings","Cryo thermal/fault management; DC protection; leak/quench safety","2026 short MgB2 MVDC sample; 2027 ~30 m hybrid line; 2028 campus pilot segment","China MgB2/HTS cable demos & grid programs; domestic LH2","Data-center power crunch; allied superconductor supply; SCARLET learning","None","Very High","Moderate-high (H2 safety + interconnect)","Nexans/SuperGrid; VEIR; busway makers","Integrated power+H2 system engineering + safety qualification","LH2 handling uneconomic vs HVDC copper; siting avoids co-location","CLEARED_WITH_WEAKNESS","S34;S35"
"EXT-15","REBCO HTS cabling / CICC manufacturing line","Automated machine/line converting REBCO tape into high-current cables with in-line tension/defect/Jc monitoring","Semi-manual cabling -> industrialized tape-to-cable with quality designed in","Continuous multi-kA HTS cable with controlled bending strain + in-line Jc verification","Fusion magnet builders & conductor suppliers","Conductor Manufacturing Director","Cabling slow, strain-sensitive, manual; tape damage destroys performance","Semi-manual cabling; CORC/ACT capacity-limited","Throughput/reproducibility gap vs demand; mechanical loading creates defects","Tape-handling/cabling heads; conduit forming; in-line metrology; tension control","Strain/tension control; defect tracking; cable digital passport","2026 cabling head+metrology; 2027 multi-kA cable pilot; 2028 line for builder","SST tape + domestic CICC for EAST/BEST/CFETR; vertical integration","Allied cabling capacity for CFS/Type One; cut manual labor","None","High","Moderate-high (fusion)","Advanced Conductor Technologies (CORC); in-house shops","Process IP + integrated QC","Architectures converge on simple stacks needing no cabling line","CLEARED","S07;S06"
"EXT-16","Space-grade rad-hard GaN power module + SEE-screening service","Rad-hardened GaN power module (SEE-mitigated, TID/DD-qualified) + heavy-ion SEE screening service for space power/EP","Bare die / silicon -> qualified screened wide-bandgap space power","GaN through GEO radiation (multi-year orbit demonstrated) with SEE hardening","Satellite-bus & electric-propulsion makers (Apex; Astranis; EP suppliers; primes)","Power Systems Lead / Spacecraft Chief Engineer","GaN TID-tolerant but SEE-susceptible to heavy ions; mass/efficiency-critical buses need qualified WBG","Rad-hard silicon MOSFETs (heavier, less efficient); conservative derating","Silicon limits efficiency/mass; unscreened GaN risks single-event burnout","SEE-mitigated GaN module; qualified packaging; screening test interfaces","Derating/protection models; SEE rate prediction","2026 SEE characterization at accelerator; 2027 hardened module; 2028 flight-qual lot","Domestic GaN + large LEO constellation demand; export-restricted from US","NASA NEPP / allied space-grade supply; constellation power demand","Die outsourced; module/screening in-house","Mid","High (ITAR/EAR; GaN export)","Infineon/EPC (commercial GaN); rad-hard Si; prime in-house","SEE-hardening design IP + qualification dataset + screening service","Commercial GaN SEE hardness improves; rad-hard Si stays good enough","CLEARED","S37;S36;S38"
"EXT-17","Fabless cryo-CMOS multiplexed control/readout subsystem for quantum","Fabless cryo-CMOS control/readout chiplet + multiplexing at 4K for quantum firms lacking in-house ASIC","Room-temp wiring bottleneck -> in-cryostat control as merchant component","Per-qubit dissipation low enough for 4K budget while multiplexing many channels","Spin-qubit/neutral-atom/small SC-qubit firms without in-house cryo-CMOS","VP Hardware / Head of Control Systems","Coax wiring from 300K doesn't scale past ~hundreds of qubits; only giants build cryo-CMOS","Room-temp AWG/instrument racks + dense cabling","Thermal load & wiring cap qubit count; bespoke ASICs out of reach","Cryo-CMOS controller/readout chiplet; multiplexer; cryo interconnect; 4K mounting","Pulse compilation; calibration; low-power multiplexing firmware","2026 cryo building blocks; 2027 multiplexed controller at 4K; 2028 qubit-customer integration","Domestic quantum + foundry; advanced-node export limits bite","Merchant cryo-control for long tail of quantum startups; allied foundry","Yes (CMOS) but fabless via foundry","High","High (advanced-node + quantum export)","Intel Horse Ridge; IBM; SemiQon; Qblox/Zurich (300K)","Cryo circuit IP + low-power multiplexing + qubit-agnostic interfaces","Giants' in-house ASICs + 300K control suffice; foundry access denied","CLEARED_WITH_WEAKNESS","S39"
"EXT-18","High-heat-flux divertor/PFC thermal-qualification test bed","High-heat-flux e-beam/plasma test bed + diagnostics that cyclically qualifies divertor/first-wall components","Scarce PFC qualification -> deployable instrumented product/service","Steady & transient heat flux >=10 MW/m2 with cyclic fatigue + in-situ diagnostics","Fusion materials/PFC teams (private fusion + national labs)","PFC/Materials Qualification Lead","Few facilities can apply fusion-relevant heat flux; PFC qualification is a bottleneck","National-lab e-beam (limited slots); HHF labs abroad","Capacity scarcity; limited diagnostics; long queues","High-power e-beam/plasma source; actively cooled stage; IR/pyrometry; erosion sensors","Heat-flux control; fatigue cycling; damage analytics; materials database","2026 e-beam HHF cell; 2027 cyclic qualification; 2028 commercial PFC qualification","ASIPP HHF heritage (EAST divertor); domestic build","Relieve allied PFC qualification bottleneck; tie to private fusion","None","High","Moderate (fusion)","Sandia HHF; EU labs","Capability + diagnostics + materials data moat","PFC designs freeze & demand drops; labs expand capacity free","CLEARED_WITH_WEAKNESS","S26;S27;S24"
"EXT-19","Closed-loop screening-current-stress-aware ramp controller for high-field HTS magnets","Controller using FBG strain + EM model to manage screening-current stress/field error during ramps, closing ramp-rate loop","Screening-current stress as static margin -> actively controlled variable","Real-time screening-current stress estimation & ramp control in >=20T REBCO coils","Ultra-high-field magnet developers (fusion; NMR/MRI; science magnets)","Magnet Controls / Mechanical Integrity Lead","Screening currents cause field errors & stress concentrations that crack/degrade coils","Conservative ramp rates; large margins; post-hoc shimming","Open-loop margins waste field/cost & miss coil-specific hot spots","FBG strain sensors; field probes; fast power-supply interface","Coupled EM-mechanical model; stress observer; ramp optimizer; alarm-to-control loop","2026 strain-instrumented coil; 2027 closed-loop ramp; 2028 high-field integration","CHMFL high-field program (45T-class); domestic sensing","NHMFL users + fusion primes; allied controller","None","Mid","Moderate","In-house magnet teams; FBG vendors (sensing only)","Coupled model + control IP + coil datasets","Tape transverse-Jc engineering removes screening stress as binding constraint","CLEARED","S11;S08"
"EXT-20","Compact high-power 4.5K helium cryoplant / cold-compressor module for private fusion","Standardized factory-built 4.5K helium refrigeration module (cold compressors) sized for private-fusion magnets","Bespoke cryoplant megaproject -> productized repeatable module","Multi-kW @ 4.5K in containerized package (ITER ref: 75 kW @ 4.5K)","Private fusion companies building pilot plants & magnet test halls","Cryogenics Systems Director","Each program needs large 4.5K cooling; only tiny cryocoolers or one-off giant plants exist; long lead","Air Liquide/Linde custom plants (slow, costly) or stacked cryocoolers","Custom plants slow/expensive; cryocoolers can't reach capacity","He turbo/cold compressors; heat exchangers; oil removal; control valves; cold box","Plant control; load-following; predictive maintenance","2026 module design+cold-compressor test; 2027 sub-scale plant; 2028 deploy at fusion test hall","ASIPP cryogenics heritage; domestic build; localize compressors","Allied cryoplant supply to private fusion fleet; cut lead times","None","Very High","Moderate-high (fusion + large machinery)","Air Liquide; Linde Kryotechnik; SHI","Modularization + reliability + service","Incumbents productize first; 20K HTS shifts cooling off 4.5K helium","CLEARED_WITH_WEAKNESS","S32;S33"
"EXT-21","Rad-hard / high-temp wireless telemetry & data link for in-vessel fusion and in-containment nuclear","Radiation- and temperature-tolerant SiC/GaN data-link module extracting sensor data from in-vessel/in-core zones","Sensing edge limited by cabling/silicon -> active edge inside radiation boundary","Survives in-vessel neutron flux ~1e13 cm-2 s-1 / in-core fluence at high T","Fusion device operators & advanced-reactor developers","Instrumentation & Controls Lead","Cabling & silicon degrade under radiation/heat; hundreds of leads impractical","Long MI cable runs; ex-vessel electronics; sparse sensing","Cable count/length & silicon failure limit in-vessel density","SiC/GaN front-end; rad-hard transceiver; HT antenna/feedthrough; sensor links","Robust low-rate protocol; error correction; sensor fusion","2026 SiC front-end+link bench; 2027 irradiation/HT test; 2028 in-vessel/in-containment demo","EAST/BEST in-vessel diagnostics demand; domestic SiC","ITER/DEMO + advanced reactors; allied rad-hard supply","Die outsourced; module in-house","Mid","High (nuclear/fusion export)","National-lab I&C groups; rad-hard vendors","Rad-hard packaging + protocol IP + qualification","Wired MI cabling stays adequate/cheaper; wireless can't meet licensing","CLEARED_WITH_WEAKNESS","S29;S22;S38"
"EXT-22","Compact cryocooler-cooled HTS fault-current limiter for dense data-center grid nodes","Compact cryocooler-cooled REBCO SFCL module for data-center campus substations & dense urban nodes","Utility-substation one-offs -> packaged module for high-density loads","Sub-cycle fault interruption with REBCO quench-and-recover, no liquid cryogen","Hyperscale data-center power teams; dense urban utilities","Director of Electrical Infrastructure / Substation Engineering","GW load raises fault current above switchgear ratings; SFCLs bespoke/bulky","Bus splitting; series reactors; switchgear upgrades","Reactors add losses; upgrades costly/slow; SFCLs not productized for campuses","REBCO fault-limiting elements; cryocooler; vacuum cryostat; MV terminations","Fault detection; recovery management; condition monitoring","2026 element+cryocooler bench; 2027 MV module; 2028 campus pilot","China grid SFCL deployments + domestic REBCO (SST)","Data-center fault-current crisis; allied superconductor supply","None","High","Moderate","SuperPower legacy; Nexans; solid-state FCL makers","Packaging + recovery control + REBCO supply integration","Solid-state FCL/reconfiguration win on cost; REBCO element cost too high","CLEARED_WITH_WEAKNESS","S34;S40"
"EXT-23","Cryogenic high-voltage dielectric qualification & bushing subsystem for superconducting cables","Cryo-HV dielectric test capability + qualified cryo-HV bushings/terminations for SC MVDC/HVDC cables","Project-specific unknown -> qualified cryo dielectric/bushing subsystem with data sheet","Tens-of-kV DC hold-off across cold-warm boundary (50 kV DC shown on MgB2/LH2 leads)","SC cable developers & high-current cryogenic power-system builders","HV/Insulation Systems Engineer","Cryo HV insulation (PD, breakdown) differs from RT & lacks productized components","Project-specific bushings; ad hoc HV testing","No standardized cryo-HV qualification or off-the-shelf bushings","Cryo-HV test cell; PD diagnostics; bushing/termination; current leads","PD analysis; breakdown statistics; insulation database","2026 cryo-HV test cell+PD; 2027 qualified bushing; 2028 integrate with cable demo","China SC cable + grid programs; domestic HV","Allied cable supply chain; data-center MVDC","None","Mid","Moderate","Cable-maker in-house; HV component vendors","Cryo-HV dataset + qualified bushing IP","SC MVDC/HVDC cable deployment stalls; demand evaporates","CLEARED_WITH_WEAKNESS","S34;S14"
"EXT-24","Cold-powering feeder & valve-box subsystem for fusion magnet systems","Integrated cold-powering feeder (HTS leads + cryo valves + instrumentation + He feed box) qualified for fusion magnets","Dispersed bespoke cold-powering interface -> one qualified serviceable module","Tens-of-kA powering with minimized 4.5K heat load + reliable cryo valve actuation","Fusion magnet system integrators","Magnet Systems / Cryogenics Integration Lead","Feeder/valve-box interface complex, leak-prone, bespoke; gates magnet commissioning","Custom feeders per project; mix of vendors","Per-project complexity; long lead; leak risk at cryo joints/valves","HTS current leads; cryo valves/actuators; He feed box; instrumentation; vacuum jacket","Feeder control; leak/thermal monitoring; interlocks","2026 lead+valve box bench; 2027 integrated feeder; 2028 magnet-system integration","ASIPP feeder heritage (built ITER feeders); strong domestic capability","Allied feeder supply for private fusion; cut bespoke engineering","None","High","Moderate-high (fusion)","ASIPP; national labs; cryo integrators","Integration + qualification + reliability data","Builders keep feeders in-house & won't buy a module","CLEARED_WITH_WEAKNESS","S32;S14;S09"
```

---

## 7. CSV-ready evidence ledger rows

```csv
source_id,worker,citation,publisher_or_body,url,source_type,quality_tier,peer_reviewed,impact_label,supports_candidates,evidence_status
"S01","EXT","Quench detection for HTS magnets: Rayleigh-backscattering interrogated optical fibers","Superconductor Science and Technology (IOP)","https://iopscience.iop.org/article/10.1088/0953-2048/29/3/03LT01","journal_article","PR-Q1/Q2","yes","high (JCR/SJR Q1)","EXT-01","CLEARED"
"S02","EXT","Fiber-optic quench detection for large-scale HTS magnets on VIPER cable at SULTAN","Superconductor Science and Technology (IOP)","https://iopscience.iop.org/article/10.1088/1361-6668/abdba8","journal_article","PR-Q1/Q2","yes","high","EXT-01;EXT-13","CLEARED"
"S03","EXT","Quench detection by fiber-optic sensors for HTS model conductors of China next-gen fusion magnets","Superconductor Science and Technology (IOP)","https://iopscience.iop.org/article/10.1088/1361-6668/ae6984","journal_article","PR-Q1/Q2","yes","high","EXT-01;EXT-13","CLEARED"
"S04","EXT","IntelliMIK: intelligent quench detection method for fusion devices","Nuclear Fusion (IOP)","https://iopscience.iop.org/article/10.1088/1741-4326/adb0dd","journal_article","PR-Q1/Q2","yes","high (Q1 flagship)","EXT-01","CLEARED"
"S05","EXT","Soldered joints - an essential component of demountable HTS fusion magnets","Superconductor Science and Technology (IOP)","https://iopscience.iop.org/article/10.1088/0953-2048/29/7/075005","journal_article","PR-Q1/Q2","yes","high","EXT-02","CLEARED"
"S06","EXT","A low-resistance joint of REBCO stacked cable for large-scale superconducting magnets","Superconductivity (Elsevier)","https://www.sciencedirect.com/science/article/pii/S2772830725000420","journal_article","PR-Q1/Q2 (new journal verify)","yes","unranked-new","EXT-02;EXT-15","CLEARED_WITH_WEAKNESS"
"S07","EXT","Analysis of current and heat transfer in locations with reduced critical current in coated-conductor tape","Superconductor Science and Technology (IOP)","https://iopscience.iop.org/article/10.1088/1361-6668/ad6484","journal_article","PR-Q1/Q2","yes","high","EXT-03;EXT-13;EXT-15","CLEARED"
"S08","EXT","Transverse variability of Jc mitigates screening-current stress in high-field REBCO magnets","Scientific Reports (Nature)","https://www.nature.com/articles/s41598-024-81902-0","journal_article","PR-Q1/Q2","yes","moderate-high (Q1/Q2)","EXT-03;EXT-19","CLEARED"
"S09","EXT","Optimization of operating temperature in cryocooled HTS magnets","Cryogenics (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S0011227502001479","journal_article","PR-Q1/Q2","yes","moderate (Q2)","EXT-05;EXT-24","CLEARED"
"S10","EXT","Charging-delay elimination of solder-impregnated HTS coils with specific excitation current","Cryogenics (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S0011227524001000","journal_article","PR-Q1/Q2","yes","moderate (Q2)","EXT-04;EXT-19","CLEARED"
"S11","EXT","Effect of screening current on electro-magnetic-force of high-field no-insulated coils","Journal of Applied Physics (AIP)","https://pubs.aip.org/aip/jap/article/137/9/093906","journal_article","PR-Q1/Q2","yes","moderate-high (Q1/Q2)","EXT-19","CLEARED"
"S12","EXT","Power supply system for 45 T hybrid magnet superconducting outsert at CHMFL","Cryogenics (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S0921453423001752","journal_article","PR-Q1/Q2","yes","moderate (Q2)","EXT-04;EXT-19","CLEARED"
"S13","EXT","HTS transformer-rectifier flux pump for no-insulation magnet","Cryogenics (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S0921453418303368","journal_article","PR-Q1/Q2","yes","moderate (Q2)","EXT-04","CLEARED"
"S14","EXT","Design/experiment of conduction-cooling HTS current leads for wiggler magnets","Cryogenics (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S0921453423002241","journal_article","PR-Q1/Q2","yes","moderate (Q2)","EXT-05;EXT-23;EXT-24","CLEARED"
"S16","EXT","High-Temperature Tools and Sensors, Down-hole Pumps and Drilling; NREL HT electronics","US DOE EERE / NREL","https://www.energy.gov/eere/geothermal/high-temperature-tools-and-sensors-down-hole-pumps-and-drilling","gov_program","AUTH","n/a","authoritative-non-article","EXT-06","CLEARED"
"S17","EXT","Thermal management systems for electronics in deep downhole environment: a review","Int. Communications in Heat and Mass Transfer (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S0735193322005723","journal_article","PR-Q1/Q2","yes","high (Q1)","EXT-06","CLEARED"
"S18","EXT","Drilling for Superhot Geothermal Energy: A Technology Gap","Stanford Geothermal Workshop proceedings","https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2025/Pearce.pdf","workshop_proceedings","AUTH (institutional)","partial","institutional","EXT-06","CLEARED_WITH_WEAKNESS"
"S19","EXT","SiC and GaN Devices With Cryogenic Cooling","US DOE / OSTI national-lab report","https://www.osti.gov/servlets/purl/1817397","national_lab_report","AUTH","n/a","authoritative-non-article","EXT-07","CLEARED"
"S20","EXT","GaN-based cryogenic-temperature power electronics for superconducting motors (cryo-electric aircraft)","peer-reviewed (venue verify; Cardiff repository copy)","https://orca.cardiff.ac.uk/id/eprint/161404/1/pdf.pdf","journal_article","PR-Q1/Q2 (verify)","yes","verify","EXT-07","CLEARED_WITH_WEAKNESS"
"S21","EXT","SiC P-N detectors under thermal/fast neutron irradiation at RA-6 reactor","Scientific Reports (Nature)","https://www.nature.com/articles/s41598-025-32175-8","journal_article","PR-Q1/Q2","yes","moderate-high (Q1/Q2)","EXT-10","CLEARED"
"S22","EXT","SiC detectors for high-flux neutron monitoring at near-core locations","Nuclear Instruments and Methods A (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S0168900219314433","journal_article","PR-Q1/Q2","yes","moderate (Q2)","EXT-10;EXT-21","CLEARED"
"S23","EXT","Wireless subsurface microsensors for health monitoring of TPS on hypersonic vehicles","NASA NTRS (+ SPIE proc.)","https://ntrs.nasa.gov/citations/20010097314","gov_tech_report","AUTH","partial","authoritative-non-article","EXT-11","CLEARED"
"S24","EXT","Review of large-area thermal-protection structures for hypersonic vehicles","Acta Astronautica (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S009457652500205X","journal_article","PR-Q1/Q2","yes","high (Q1)","EXT-11;EXT-18","CLEARED"
"S25","EXT","Real-time TPS surface-temperature sensor via full-time-domain inversion","Sensors (MDPI)","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11991591/","journal_article","PR-Q1/Q2","yes","moderate (Q1/Q2 verify)","EXT-11","CLEARED"
"S26","EXT","Recent progress in liquid-metal plasma-facing components for magnetic fusion","Nuclear Materials and Energy (Elsevier)","https://www.sciencedirect.com/science/article/pii/S2352179124001996","journal_article","PR-Q1/Q2","yes","moderate-high","EXT-08;EXT-18","CLEARED"
"S27","EXT","Fast-flow liquid-Li divertor for FNSF (coupled plasma + LM MHD/heat-transfer)","Nuclear Fusion (IOP)","https://iopscience.iop.org/article/10.1088/1741-4326/ad3a7b","journal_article","PR-Q1/Q2","yes","high (Q1 flagship)","EXT-08;EXT-18","CLEARED"
"S28","EXT","Construction and initial operation of MHD PbLi facility at UCLA","Fusion Engineering and Design (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S0920379613003128","journal_article","PR-Q1/Q2","yes","moderate (Q1/Q2)","EXT-08","CLEARED"
"S29","EXT","Long-term operation of radiation-hard Hall probes + path to hybrid magnetic field sensor","Nuclear Fusion (IOP)","https://iopscience.iop.org/article/10.1088/1741-4326/ac8aad","journal_article","PR-Q1/Q2","yes","high (Q1 flagship)","EXT-09;EXT-21","CLEARED"
"S30","EXT","Steady-state magnetic diagnostic based on antimony Hall sensors for fusion reactors","Fusion Engineering and Design (Elsevier)","https://www.sciencedirect.com/science/article/abs/pii/S0920379619300183","journal_article","PR-Q1/Q2","yes","moderate (Q1/Q2)","EXT-09","CLEARED"
"S32","EXT","ITER cryoplant: 75 kW @ 4.5 K helium refrigeration","ITER Organization / Fusion for Energy","https://www.iter.org/machine/supporting-systems/cryogenics","international_agency","AUTH","n/a","authoritative-non-article","EXT-12;EXT-20;EXT-24","CLEARED"
"S33","EXT","Innovative cryogenic cooling material from abundant elements (helium-supply pressure)","Scientific Reports (Nature)","https://www.nature.com/articles/s41598-025-29709-5","journal_article","PR-Q1/Q2","yes","moderate-high (Q1/Q2)","EXT-12;EXT-20","CLEARED"
"S34","EXT","MgB2-based MVDC superconducting power cable in liquid hydrogen","IEEE Trans. Applied Superconductivity","https://ieeexplore.ieee.org/document/10380545/","journal_article","PR-Q1/Q2","yes","moderate (Q2 field flagship)","EXT-14;EXT-22;EXT-23","CLEARED"
"S35","EXT","Cryogenic tests of 30 m flexible hybrid LH2 + superconducting MgB2 cable","Physics Procedia (Elsevier, conf. proceedings)","https://www.sciencedirect.com/science/article/pii/S1875389215004149","conference_proceedings","PR-Q1/Q2 (proc.)","yes","proceedings","EXT-14;EXT-23","CLEARED_WITH_WEAKNESS"
"S36","EXT","Review: opportunities in single-event effects in radiation-exposed SiC/GaN power electronics","Penn State (peer-reviewed; venue verify)","https://pure.psu.edu/en/publications/review-opportunities-in-single-event-effects-in-radiation-exposed/","journal_article","PR-Q1/Q2 (verify)","yes","verify","EXT-16","CLEARED_WITH_WEAKNESS"
"S37","EXT","Pioneering evaluation of GaN transistors in geostationary satellites (6-yr Alphasat)","peer-reviewed (PMC-indexed)","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9334328/","journal_article","PR-Q1/Q2","yes","moderate (verify)","EXT-16","CLEARED"
"S38","EXT","Overview of radiation-damage effects and protection in microelectronics (2024)","Science and Technology of Nuclear Installations (Wiley)","https://onlinelibrary.wiley.com/doi/10.1155/2024/3616902","journal_article","PR-Q1/Q2 (moderate)","yes","moderate","EXT-16;EXT-21","CLEARED_WITH_WEAKNESS"
"S39","EXT","Classical interfaces for controlling cryogenic quantum computing technologies","APL Quantum (AIP)","https://pubs.aip.org/aip/apq/article/2/4/041501/3373674","journal_article","PR-Q1/Q2 (newer venue)","yes","verify","EXT-17","CLEARED_WITH_WEAKNESS"
"S40","EXT","REBCO capacity expansion + record Jc / SFCL cost trajectory (industry overview)","Superconductor market overview (GlobeNewswire release)","https://www.globenewswire.com/news-release/2025/01/10/3007450/0/en/Superconductors-Materials-Products-and-Applications-Overview-2024.html","market_release","TRI","no","triangulation-only","EXT-22","WEAK_SIGNAL_ONLY"
```

---

### Notes for the merger / source auditor
- **Verify before scoring:** journal venue/quartile for S06 (Elsevier *Superconductivity*, new), S20 (Cardiff repository — find final journal), S25 (*Sensors* quartile in instrumentation), S36 (Penn State review final venue), S37 (final journal name), S39 (*APL Quantum* indexing). All are currently flagged CLEARED_WITH_WEAKNESS pending confirmation.
- **S40 is triangulation only** (market release) and must be replaced with a primary source on the data-center fault-current driver before EXT-22 can be ranked.
- **China feasibility is strongest** for the HTS/fusion-magnet engine-layer candidates (EXT-01/02/03/04/05/13/15/19/24) given Shanghai Superconductor REBCO scale-up (2,000->4,000 km/yr), ASIPP feeder/diagnostic heritage, and CHMFL high-field labs; weakest (export-blocked, US-first) for EXT-16 (space rad-hard GaN), EXT-11 (hypersonics, ITAR), and EXT-17 (advanced-node cryo-CMOS).
- No candidate's core technical or pain claim rests solely on preprints, company claims, or market reports; preprint hits found during search (arXiv) were used only as leads and replaced with peer-reviewed or authoritative sources.
