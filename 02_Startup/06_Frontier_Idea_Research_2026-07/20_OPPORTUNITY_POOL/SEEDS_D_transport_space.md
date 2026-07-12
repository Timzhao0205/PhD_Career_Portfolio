# SEEDS batch D — transport, space & harsh environments (L09/L10/L15)

Architect: claude-fable-5 / xhigh. Date: 2026-07-12. 16 seeds (D01–D16); more than the 12 minimum
so weak concepts can be discarded. All demand/technical/competitor claims cite accepted ledger IDs
only (rejected IDs L09-010/025/036/052, L10-037/038/047/049, L15-032/036/044/046 deliberately not
used). Binding cautions respected: no IMO-timing-dependent maritime seed (D11 rests on Singapore's
national MPA mandate, not IMO); Space Force EP content treated as inference and flagged (D04);
mining trial-stage economics flagged where load-bearing (D06–D08).

## D01 — Modular rad-tolerant GaN PPU brick for small-sat electric propulsion (L09)
- Product: 300–1,500 W GaN anode-discharge power brick (28–100 V in, 200–600 V out) with ignition
  sequencing, breathing-mode-tolerant control, and a parallelable current-share bus.
- Buyer: EP integrators and small-sat OEMs — Busek, Furukawa/JAXA, ISRO ecosystem, Rocket Lab-class channels.
- Pain/demand: PPU non-convergence and per-generation NRE (L09-001..008, L09-011); small-sat PPU
  cost/mass pain is the explicit premise of JAXA/Furukawa J-SPARC (L09-042); NASA paid $67M/$18.4M
  for bespoke PPU chains (L09-034, L09-012, L09-043); ISRO life-testing its own SPT (L09-035).
- Mechanism: 500 kHz–1 MHz GaN full-bridge/LLC + planar magnetics; SET clamping (L09-108); heavy-ion
  derating (L09-103/104); ECSS-E-ST-20-20C / AIAA S-122 interfaces (L09-111, L09-115).
- Incumbents miss: Aerojet/L3Harris in missile-first parent (L09-041); Moog bespoke; VPT/EPC sell
  generic converters, not thruster-aware supplies (L09-053/054/055).
- Experiment: 500 W EM brick fired against lab Hall thruster + laser/cyclotron SEE spot-check — $220k.
- Vision: merchant power layer of EP up to paralleled 50–100 kW tug arrays.
- Substitutes: in-house PPUs; VPT (L09-045/053); EPC Space (L09-054/055); Furukawa if it ships (L09-042).
- Uncertainty: build-vs-buy culture; GaN SEE qualification at useful derating. Confidence: medium.

## D02 — Hall-thruster electrical emulator (PHIL discharge load) (L09)
- Product: 600 V/2 kW (parallelable to 20 kW) power-HIL load reproducing ignition inrush,
  negative-resistance V-I, breathing-mode spectra, and fault modes for PPU qualification without vacuum time.
- Buyer: PPU/thruster developers and labs — Mitsubishi Electric, Busek, ISRO, NASA Glenn-class facilities.
- Pain/demand: worldwide non-converged PPU programs each pay coupled vacuum-test cost (L09-001/002);
  ISRO 1,000-h campaign (L09-035); NEXT-C built prototype PPU first (L09-012); JAXA/Furukawa (L09-042).
- Mechanism: >1 MHz-bandwidth bidirectional stage driven by FPGA 0-D discharge model built from
  published dynamics (L09-004/005/006, L09-008) incl. end-of-life signatures (L09-109, L09-110).
- Incumbents miss: market too small for test majors; discharge models are thruster-house IP; skills span orgs.
- Experiment: 600 V/10 A stage reproducing published SPT-100-class spectra within ~10% — $80k.
- Vision: de facto electrical pre-qualification reference for EP; thruster digital-twin library.
- Substitutes: vacuum coupled tests (L09-035); dumb load banks; one-off lab rigs.
- Uncertainty: buyer population likely tens of accounts. Confidence: medium.

## D03 — Pulsed-laser SEE screening station for WBG space power devices (L09→L15)
- Product: turnkey two-photon-absorption laser SEE station with kV-biased fixtures for GaN/SiC power
  parts + laser-to-ion derating database.
- Buyer: rad-tolerant part vendors and primes — EPC Space, VPT, NASA/prime power groups, rad-hard ASIC houses.
- Pain/demand: unresolved WBG SEE qualification, burnout near 50% rated voltage (L09-014, L09-020,
  L09-103/104); unvalidated new parts (L09-055); NASA SBIR money flowing to rad-hard power ASICs
  that all need screening (L09-112, L09-113).
- Mechanism: backside fs-laser TPA charge deposition triggers the same SEB/SEGR paths as ions
  (L09-104, L09-103); die-mapping under bias yields safe-operating-voltage without beam time.
- Incumbents miss: beamlines are national facilities, not products; vendors can't self-certify.
- Experiment: single-channel bench, correlate laser threshold to published ion data on 2 device types — $140k.
- Vision: the underwriting lab for space power silicon; wafer-level screening at the edge.
- Substitutes: cyclotron campaigns; national-lab laser services; blanket derating.
- Uncertainty: laser-ion correlation fidelity for destructive kV events; concentrated demand. Confidence: low.

## D04 — Rad-tolerant cryocooler drive electronics module (L09→L15)
- Product: 50–300 W rad-tolerant GaN sinusoidal cryocooler drive with active exported-vibration
  cancellation; 100 krad TID, SET-clamped.
- Buyer: cryocooler OEMs and IR-payload integrators; NASA (SBIR precedent, L09-112); SDA primes
  (cooler content inferred — flagged).
- Pain/demand: NASA pays for "low cost radiation-hardened cryocooler control electronics" (L09-112);
  $3.5B Tranche 3 proliferation multiplies cooled payloads (L09-039, EP/cooler content not disclosed);
  merchant space components proven as a business (L09-114).
- Mechanism: dual GaN half-bridges, 30–120 Hz sine drive; adaptive narrowband vibration cancellation;
  SET clamping (L09-108); GaN derating per L09-103; Stirling-control heritage (L09-105).
- Incumbents miss: drives are bundled cost centers at cooler OEMs; rad-hard houses sell DC-DC, not motor control.
- Experiment: drive a tactical pulse-tube cooler, hit flight-representative exported vibration, 100 krad TID — $150k.
- Vision: standard drive inside every constellation IR cooler; ZBO cryo plants at the edge.
- Substitutes: OEM in-house drives; Creare SBIR result (L09-112); legacy Si drives (L09-053-class).
- Uncertainty: SDA content inference; OEM bundling. Confidence: medium.

## D05 — High-voltage neutron-tolerant SiC PMAD bricks for fission surface power (L09+L15/L04)
- Product: 1,000 VDC / 25 kW PMAD brick (SiC solid-state breaker + isolated DC-DC + telemetry),
  neutron/TID characterized, 150–200 C coldplate; scale 40→100 kWe by paralleling.
- Buyer: FSP teams — Westinghouse (L09-032/047), LM/BWXT/Creare, IX/Maxar/Boeing (L09-031); NASA/DOE-INL.
- Pain/demand: FSP spec tripled 40→100 kWe mid-program with NSTM-3 backing (L09-031 vs L09-033),
  stranding Phase 1 power baselines; rad and thermal must be qualified separately (L15-020).
- Mechanism: 1.2 kV SiC stages, desat solid-state breaking (<10 us), LLC isolation; margins from
  neutron-degradation data (L15-020) and SiC SEB physics (L09-104); SiC headroom per L15-009.
- Incumbents miss: kV-class neutron-tolerant PMAD falls between reactor primes and 100 V spacecraft
  power houses; spec churn rewards modular merchant bricks.
- Experiment: one 1 kV/25 kW brick, fault interruption + 96% efficiency at 150 C + reactor irradiation — $240k.
- Vision: grid hardware of cislunar industrialization; MW-class NEP distribution at the edge.
- Substitutes: prime in-house PMAD; Moog heritage (L09-043).
- Uncertainty: single government customer, schedule politics; thin kV SiC neutron data. Confidence: medium.

## D06 — Robotic megawatt-charging connection cell for autonomous haul trucks (L10+L15)
- Product: vision-guided, dust-sealed robotic MCS coupler (IEC TS 63379, to 1,250 V/3,000 A) mating
  driverless 240 t BEV trucks to multi-MW chargers; ±150 mm capture, wear-cartridge contacts.
- Buyer: Fortescue Zero, BHP/Rio (Jimblebar autonomous BEV trial), Liebherr, Caterpillar, charger integrators.
- Pain/demand: Fortescue self-built a 6 MW charger (L10-029) for a 400-truck order book (L10-028);
  BHP/Rio/Cat explicitly trial BEV-plus-autonomy integration (L10-030) on fleets already autonomous
  at scale (L15-042); driverless trucks have nobody to plug in a megawatt connector.
- Mechanism: fiducial+lidar pose estimation, 6-DOF arm, floating-compliance coupler, contact-resistance
  and RTD monitoring feeding charger derating per MCS envelope (L10-050); IP66 + purge for pit dust.
- Incumbents miss: interface orphaned between charger OEMs and truck OEMs; MCS standard is new (Feb 2026).
- Experiment: subscale 500 kW coupler, 1,000 mate cycles in dust chamber with misalignment — $180k.
- Vision: lights-out energy exchange for all autonomous heavy fleets.
- Substitutes: manual connection; Liebherr trolley/Power Rail (L10-052); battery swap (L10-031); MEC500 (L10-053).
- Uncertainty: architecture non-convergence (swap/trolley may win); OEM in-housing. Confidence: medium.

## D07 — Trolley-assist retrofit power kit for underground battery LHDs (L10)
- Product: 300–400 kW drift-rail collector + vehicle-side bidirectional SiC converter + mine-side
  rectifier skid; OEM-agnostic retrofit eliminating mid-shift charge stops.
- Buyer: underground mine operators running battery LHDs; Cat dealer channel.
- Pain/demand: LHDs cannot finish a shift on battery (L10-014); trolley-assist shows up to 75%
  simulated energy-cost reduction but is unproductized (L10-024); incumbent answer is 20-min charge
  stops with two MEC500s (L10-053).
- Mechanism: sprung dual-shoe collector on drift back-rail; isolated SiC DC-DC blends rail and
  traction bus, regen priority on down-ramps (configs per L10-014/024, L10-002); ties to mine 1 kV.
- Incumbents miss: OEMs monetize chargers/batteries and stop at the machine boundary; trolley skills
  sit with surface/rail suppliers.
- Experiment: 300 kW chain on emulated 750 VDC rail; validate shift-completion model on hardware — $150k.
- Vision: powered-corridor underground mines with ventilation capex designed out; deep hot mines at the edge.
- Substitutes: swap bays; more chargers (L10-053); bigger batteries; Chinese swap standard (L10-046).
- Uncertainty: simulation-heavy evidence; per-mine code approvals. Confidence: medium.

## D08 — Relocatable containerized trolley-assist substation for open pits (L10)
- Product: 3–6 MW containerized SiC-AFE rectifier substation (11–33 kV in, 1.8–3 kV DC catenary out)
  with jack-and-roll relocation in days plus modular mast/catenary sections.
- Buyer: Fortescue (trolley-ready T264s), Hitachi/ABB trolley-hybrid users, BHP-class pits.
- Pain/demand: T264 is trolley-ready with claimed 86% energy-cost/tonne cut (L10-052); Hitachi/ABB
  flagship is trolley-hybrid (L10-054); stranded-infrastructure fear blocks convergence (L10-028/029).
- Mechanism: SiC AFE rides 2–3 MW truck load steps (dynamics per L10-002, L10-015) with supercap
  smoothing for weak mine grids; pre-terminated container = crane lift, not civil works.
- Incumbents miss: grid vendors sell permanence; truck OEMs stop at the pantograph; "infrastructure
  that moves with the pit" is unowned.
- Experiment: 250 kW AFE demonstrator + power-quality validation + certified relocation study — $170k.
- Vision: movable pit electrification as a category; fully trolley-electrified pits at the edge.
- Substitutes: fixed substations (L10-054); static charging farms (L10-029); swap (L10-031).
- Uncertainty: trolley uptake breadth; OEM package bundling. Beachhead is AU/Africa (neither flag set). Confidence: medium.

## D09 — Automated wayside megawatt charging mast for battery locomotives (L10)
- Product: yard-installed overhead mast with automated inverted-pantograph head, 1–3 MW MCS-derived
  power core (IEC TS 63379), dispatch-integrated charge scheduling within existing dwell.
- Buyer: Union Pacific (L10-032), Vale (L10-033), BHP/Rio/Roy Hill/CN programs; Wabtec channel.
- Pain/demand: FLXdrive orders reaching 7.0 MWh units (L10-051) while corridor studies show benefits
  hinge on recharge siting/speed (L10-010/011/012); no rail-adapted MW charging product exists.
- Mechanism: rising mast locates on roof rails; actively cooled MCS-grade contacts; stacked SiC AFE +
  isolated DC-DC from 13.8/25 kV yard feed (envelope per L10-050).
- Incumbents miss: Wabtec sells locomotives, not charging; electrification vendors think catenary-miles;
  MCS world is road-truck oriented.
- Experiment: 350 kW automated head, 5,000 outdoor engage cycles, corridor charge-window validation — $200k.
- Vision: corridor-scale battery-rail enablement; 10 MW five-minute boost at the edge.
- Substitutes: in-consist diesel charging; catenary segments; future Wabtec depot chargers (L10-051).
- Uncertainty: pilot-scale order flow; Wabtec verticalization; slow rail capex. Confidence: low.

## D10 — Diesel-RTG hybrid conversion kit monetizing Clean Ports grants (L10)
- Product: retrofit kit for diesel rubber-tired gantries — 600 kW bidirectional SiC DC-bus converter,
  LTO pack capturing hoist regen, genset downsizing controller; <2 weeks per crane.
- Buyer: EPA Clean Ports grant-holding US terminals (L10-048); YILPORT-class operators; APM/Maersk programs.
- Pain/demand: ~$3B in 53 awarded (already-obligated, CARB-repeal-proof) grants for zero-emission
  port equipment (L10-048); category appetite shown by 53-crane E-Hybrid order (L10-041) and
  Maersk/CATL port MOU (L10-036); the installed diesel fleet has no productized mid-life path.
- Mechanism: common DC bus inserted between genset and hoist drives; LTO absorbs 200+ daily regen
  micro-cycles now burned in resistors; peak-shave allows half-size genset or shore cable — the
  E-Hybrid architecture (L10-041) delivered as retrofit.
- Incumbents miss: OEMs prefer new-crane sales; battery majors chase fleet deals; mixed-OEM retrofits
  are fragmented work — but grant deadlines create urgency now.
- Experiment: 2-week datalog of a working RTG + bench validation of converter/pack on measured
  profile + bankable savings model for one grant-holder — $120k.
- Vision: default electrification path for tens of thousands of yard cranes; zero-genset terminals at the edge.
- Substitutes: new E-Hybrid cranes (L10-041); lane busbar electrification; CATL-OEM offerings (L10-036).
- Uncertainty: grant administration politics; per-site variance vs kit margins. Confidence: medium.

## D11 — TR136-compliant swappable harbour-craft battery module, Singapore (L10)
- Product: crane-handled ~250 kWh LFP swap module (blind-mate HV connector, runaway containment,
  coded keying) + quayside charge-and-swap cabinet serving 4–6 craft.
- Buyer: Singapore harbour-craft operators and yards under MPA's firm 2030 all-electric new-build mandate.
- Pain/demand: TR136 published Mar 2025 with mandate from 2030 — under five years of runway (L10-055);
  swap proven at vessel scale in China (L10-040); class rules in force (L10-045). National mandate,
  not IMO timing — compliant with the binding caution.
- Mechanism: IP67 module per swap-standard practice (L10-046); vent channeling/mist suppression for
  runaway; 0.5C cabinet recharge decouples turnaround from charge time (as in L10-040).
- Incumbents miss: CATL-scale players chase big vessels/fleets (L10-036); segment too fragmented for
  majors, too capital-heavy for local yards; TR136 too new for compliant incumbents.
- Experiment: module + cabinet prototype, TR136 gap analysis with certifier, 100 swap cycles +
  containment test — $180k.
- Vision: SEA small-vessel swap standard; autonomous craft at unmanned pontoons at the edge.
- Substitutes: fixed DC charging; the B100 compliance path (L10-055); adapted Chinese systems (L10-040).
- Uncertainty: new-build-only mandate = slow fleet turnover; MPA execution; B100 leakage. Confidence: low.

## D12 — 225 C IC obsolescence-bridge chipset on merchant SOI (L15)
- Product: pin/function-compatible replacements for the discontinued CISSOID CHT / Honeywell 225 C
  catalog (gate driver, precision op-amp, reference first) on a live 180 nm SOI foundry process,
  ceramic-hermetic, published 1,000 h/250 C HTOL data, 10-year availability guarantee.
- Buyer: downhole/geothermal tool OEMs — Welltec, PetroQuip (FORGE awardees, L15-027/028), Baker
  Hughes (L15-040), SLB.
- Pain/demand: CHT family marked obsolete/last-time-buy while CISSOID itself markets as replacement
  for Honeywell's exited line (L15-043) — a live supply gap against $93M of FORGE tool programs
  (L15-027/028) and $2.0B Baker Hughes New Energy orders (L15-040); market context L15-045.
- Mechanism: PD-SOI kills bulk leakage above 150 C, functional to ~300 C (L15-004); HT design kit
  reproduces Deep Trek/Honeywell approach (L15-031) on merchant fab; AuGe/sintered-Ag die-attach +
  hermetic ceramic addresses the packaging failure layer (L15-005, L15-025).
- Incumbents miss: Honeywell exited (small volumes vs aero core); CISSOID stuck on obsolete fab;
  foundry SOI now makes small-volume HT parts economical — a supply-shock wedge.
- Experiment: MPW tape-out of driver + op-amp, ceramic assembly, 1,000 h/250 C HTOL, publish drift — $200k.
- Vision: trusted merchant extreme-environment IC source; Venus-class (465 C) ICs at the edge (L15-030).
- Substitutes: LTB hoards; CISSOID CMT/CXT (L15-043); 175 C parts + dewars.
- Uncertainty: opaque real volumes — obsolescence may signal shrinking, not stranded, demand. Confidence: high.

## D13 — 300 C-native downhole DAQ module for superhot geothermal (L15)
- Product: cooling-free 300 C downhole instrumentation sub — SiC-JFET AFE, 300 C SOI digitizer,
  SiC pressure/temperature sensing; no dewar, no bottom-hole time limit.
- Buyer: EGS/superhot players — Fervo (FORGE awardee L15-027), SLB-Ormat pilot (L15-041), Baker
  Hughes (L15-040), ARPA-E SUPERHOT teams (L15-029).
- Pain/demand: SUPERHOT targets >375 C (L15-029) and FORGE spent $93M at 225 C (L15-027/028) while
  the commercial electronics ceiling stays at 225 C with no vendor roadmap (L15-043) — a widening
  capability gap against contracted geothermal spend (L15-040, L15-041).
- Mechanism: SiC JFET ICs (500 C/1-yr proven, L15-009) + 300 C SOI ADC (L15-004) digitize downhole;
  SiC piezoresistive dies (L15-006/007, L15-016) replace capillary gauges; contrasts with the
  dewar/active-cooling workaround literature (L15-023/024).
- Incumbents miss: oilfield majors optimized for 150–200 C + dewars; superhot volume too small to
  bend their roadmaps — hence two decades of federal programs without a purchasable platform.
- Experiment: SiC AFE + SOI ADC module streaming through HT cable head at 300 C/30 MPa autoclave,
  500 h — $220k.
- Vision: the sensing layer that unlocks >375 C baseload; permanent 400 C arrays / Venus reuse at the edge.
- Substitutes: dewared tools (L15-023/024); memory gauges; derated 225 C designs (L15-043).
- Uncertainty: small near-term well count; drilling-side bottlenecks may gate (L15-021). Confidence: medium.

## D14 — 300 C-junction SiC power module platform: packaging as the product (L15)
- Product: qualified half-bridge SiC module family for 250–300 C junction — silver-sintered
  die-attach on AMB Si3N4, organics-free encapsulation, hermetic option, published qual dossier.
- Buyer: downhole/geothermal tool OEMs, aero-engine actuator integrators, THERMAL-era performers;
  CISSOID's stranded module customers.
- Pain/demand: packaging/die-attach named the unresolved limiter by four 2024–2026 reviews
  (L15-005, L15-025, L15-015, L15-007) while the only merchant HT vendor obsoletes its line
  (L15-043); program demand context L15-026, L15-029, L15-040.
- Mechanism: pressure-assisted Ag sintering (~960 C remelt) removes the solder failure layer;
  Si3N4 AMB CTE-matches SiC; no organics above 250 C; die from merchant SiC supply (L15-039);
  headroom to SiC's ~600 C ceiling (L15-001).
- Incumbents miss: automotive giants stop at 175 C where volume is; die startups don't fund
  packaging; public 300 C qual data is slow, unglamorous, defensible.
- Experiment: 20 modules through 500 shock cycles (-55/+300 C) + 1,000 h HTGB at 300 C junction;
  publish delamination/drift dossier — $150k.
- Vision: the qualified packaging layer for all >250 C power electronics; 600 C junction at the edge.
- Substitutes: CISSOID lower-rated modules (L15-043); prime in-house hybrids; active cooling (L15-023).
- Uncertainty: per-customer requalification burden; >250 C die (gate oxide) supply. Confidence: medium.

## D15 — Teleoperation/drive-by-wire retrofit cell for ancillary pit equipment (L15+L10)
- Product: OEM-agnostic retrofit kit (sealed actuators or CAN injection, bonded 5G/LTE + mesh,
  safety PLC with geofence and loss-of-comms stop) + operator station multiplexing 3–6 machines.
- Buyer: Baogang Steel Union (live RMB3.75M phase-two 5G remote-control retrofit tender within
  ~RMB18M program, L10-035); Rio Tinto-class autonomous-mine operators; Cat dealer channel.
- Pain/demand: truck autonomy is mature and ordered at scale (L15-042; literature L15-018) but
  dozers/graders/rollers still expose humans; SOE tenders are paying for exactly this retrofit now (L10-035).
- Mechanism: electrohydraulic bolt-on or CAN-level control execution; deterministic-latency video;
  watchdogged failsafes; one operator per several intermittent-duty machines is the economics.
- Incumbents miss: OEM autonomy stacks monetize flagship truck fleets; mixed-fleet ancillary
  retrofit is per-machine-variant integrator work they avoid.
- Experiment: retrofit one used dozer; 8-h production-representative teleop shift with latency and
  failsafe validation across two multiplexed machines — $160k.
- Vision: ancillary-fleet autonomy layer worldwide; zero-human-in-pit at the edge.
- Substitutes: single-OEM remote options; Cat Command expansion (L15-042); operators in cabs.
- Uncertainty: jurisdictional safety cases; Western access to Chinese SOE tenders. Confidence: medium.

## D16 — Dose-managed sacrificial electronics cartridge for nuclear robotics (L15)
- Product: quick-swap spot-shielded cartridge (COTS compute, motor drives, cameras) with onboard
  dosimeter and replace-before-failure prognostics; sold as cartridge subscription.
- Buyer: decommissioning programs — Fukushima Daiichi ecosystem (Quince lineage, L15-011), Chinese
  nuclear-emergency robotics (L15-012), UK/EU agencies whose cost case exists (L15-002).
- Pain/demand: every program re-runs ad hoc Co-60 qualification of COTS electronics (L15-011/012);
  UK analysis shows planned replacement beats rad-hard on cost (L15-002) — no product embodies it.
- Mechanism: W-Cu spot shielding + TMR FPGA supervision (L15-022) extend COTS life 3–10x; dosimeter
  prognostics enforce the planned-replacement schedule; device degradation bounded by L15-013/014.
- Incumbents miss: rad-hard vendors profit from $1,500–2,100 parts (L09-053-class), not disposables;
  robot OEMs lack irradiation access; consumables model foreign to both.
- Experiment: cartridge with dosimeter, five units irradiated to failure under Co-60 for a
  dose-to-failure distribution, glovebox hot-swap demo — $90k.
- Vision: consumable-electronics model for all rad-heavy robotics incl. fusion in-vessel maintenance.
- Substitutes: full rad-hard stacks (L09-053-class); per-program ad hoc testing (L15-011/012); tethers.
- Uncertainty: few, slow government buyers; pilot-stage sub-lane — revenue timing. Confidence: low.
