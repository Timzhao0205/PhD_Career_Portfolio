# PHASE 2 — NOVEL CANDIDATES (V01–V15), Round 2

Synthesized from the eight Phase-1 gap-lane briefs (`10_GAP_LANDSCAPE/`). Citations `[G0x-##]`
refer to `90_BIBLIOGRAPHY/sources.json`. Template identical to Round 1 (GEN3/CANDIDATES.md) plus
the mandatory **Novelty declaration** (nearest excluded neighbor by ledger id + material
difference). Every candidate was checked against all 273 entries + 2 category bans in
`05_STATE/exclusion_ledger.json`.

**Diversity-rule compliance (checked at generation):**
- Standalone products/systems: 13/15 = 87% (≥50% required ✓)
- Test/measurement/diagnostic instruments: 2/15 = 13% — V12, V13 (≤3 allowed ✓)
- PhD-lane candidates: 1/15 — V12 (magnetometer-array + inversion instrument; flagged for extra
  red-team scrutiny) (≤2 allowed ✓)
- HTS/superconductivity candidates: 0/15 (gate G6-HTS ✓; incumbent C12 holds the single slot)
- Transformer-condition-monitoring conflicts: 0/15 (Magnefy wall ✓)
- Lanes covered: all 8 (G01×1, G02×2, G03×2, G04×2, G05×2, G06×2, G07×2, G08×2)
- Every candidate names a high-end beachhead, an expansion path, and both China and US angles;
  timeframe lens 2029/2030.

Category tags: `[S]` standalone product/system · `[T]` test/measurement/diagnostic instrument.

---

## V01 — WBG retrofit power supply + closed-loop arc-control module for industrial plasma torches [S] (lane G02)

**Concept.** A SiC-based high-power-density PSU (100 kW–2 MW class) with real-time arc
impedance sensing and closed-loop stabilization, sold as a bolt-on replacement for the legacy
supplies behind DC/AC plasma torches in hazardous-waste vitrification, ash melting, and metals
recovery. Electrode-life extension and energy-per-tonne reduction are the sold specs.
**Extreme edge.** Legacy torch supplies are decades-old designs (Tetronics/Europlasma class,
~1,500-hour electrode life); modern WBG conversion + FPGA arc control targets 2–5x electrode
life and 20–30% energy cut — on plants where the torch is the single availability driver
[G02-02][G02-18].
**Beachhead.** The bolt-on plasma stage pattern already shipping in China (Foshan 30 t/d kiln +
15 t/d plasma; CITIC Dongguan) [G02-10][G02-17] and Western hazardous-waste operators
retrofitting rather than building $400M–1B mega-plants that keep failing [G02-02]. ASP
$150–600K/system.
**Expansion.** Torch OEM partnerships → plasma metallurgy (Ti, ferroalloys) → hydrogen-plasma
pilot supplies.
**Frontier vision.** The power-and-controls layer of industrial plasma — every torch runs on it.
**HW/SW split.** SiC PSU hardware + FPGA arc-dynamics control + recipe/telemetry software.
**TRL/feasibility.** SiC modules and torch bodies purchasable; arc-control algorithms are the
IP. v1 on a 100 kW torch in 12–18 months.
**Cleanroom dependence.** None.
**China angle.** State-linked plasma-waste programs (20 t/d ≈ CNY 50M, 3-year payback
[G02-18]); component sourcing; Belt-and-Road plasma exports [G02-12-context].
**US angle.** Hazardous/medical waste operators, DOE critical-materials recovery, DoD
remediation.
**Founder fit.** High-power-density conversion (Rivas collaboration) × harsh-env packaging ×
FPGA control — near-perfect graph match; plasma is a user-named sector.
**Novelty declaration.** Nearest excluded: **N08** (industrial pulsed power/PEF) and **C10**
(precision magnet/scientific converters). Material difference: continuous-arc thermal-torch
supplies for waste/metallurgy operators — different buyer segment (waste plants, not food
processors or physics facilities) and different product category (arc PSU + electrode-life
control, not pulsed-field processors or ppm-class magnet supplies). No excluded entry covers
industrial plasma-torch power.
**Sources.** [G02-02][G02-08][G02-10][G02-17][G02-18]

## V02 — Containerized pulsed-arc PFAS destruction skid for water utilities & DoD sites [S] (lane G02)

**Concept.** A field-hardened plasma destruction unit (plasma-vortex/pulsed-arc reactor + purpose-built
high-power-density pulsed supply + PLC/telemetry) sold as the polishing stage after IX/RO/foam
fractionation concentrates PFAS. The product is the integrated skid; the differentiator is the
power electronics.
**Extreme edge.** Incumbent skids (DMAX, Onvector) are chemistry-led builds on generic supplies
[G02-04][G02-05]; a purpose-built pulsed supply with adaptive impedance matching targets 2–4x
destruction throughput per kW and utility-grade duty cycles.
**Beachhead.** US water utilities + DoD/AFFF remediation sites under the EPA NPDWR clock —
compliance deadline 2029 (extension to 2031 proposed), sector compliance cost $1.5–5.5B/yr with
~$1B EPA grants + $4B state revolving funds already appropriated [G02-14][G02-15]. ASP
$300K–1M/skid.
**Expansion.** Landfill leachate → semiconductor fab wastewater → concentrate destruction as a
service.
**Frontier vision.** Destruction-plasma as standard utility unit-operation hardware.
**HW/SW split.** Pulsed PSU + reactor hardware; control/compliance-reporting software (destruction
verification logs regulators require).
**TRL/feasibility.** Non-thermal plasma PFAS destruction is demonstrated at pilot scale by the
incumbents; the founder's version is a power-architecture upgrade, not new chemistry. v1 18–24
months.
**Cleanroom dependence.** None.
**China angle.** Component supply; China PFAS regulation is earlier-stage — watch, not launch.
**US angle.** Primary market; EPA deadline is the demand clock [G02-14][G02-15].
**Founder fit.** Pulsed power conversion × harsh-env packaging × embedded control; plasma sector.
**Novelty declaration.** Nearest excluded: **N08** (industrial pulsed power / PEF). Material
difference: different buyer segment (water utilities/DoD environmental compliance, not food/
beverage processors) and different product category (plasma destruction reactor system with
compliance software, not pulsed-electric-field pasteurization/extraction systems). C36 (medical
ablation) shares only the word "plasma" — no tissue application.
**Sources.** [G02-04][G02-05][G02-14][G02-15]

## V03 — Vendor-agnostic thermal-battery discharge power stage & controls [S] (lane G04)

**Concept.** The electronics + controls layer that turns any heat-storage bank (brick, particle,
molten-salt) into dispatchable process steam/hot air: MV-fed resistive charge control,
discharge-side flow/temperature regulation, and grid-services-aware dispatch software, sold to
storage developers and industrial-park EPCs who are not electronics companies.
**Extreme edge.** Rondo-class integrators bundle storage + electronics and keep both proprietary
[G04-02][G04-05]; independent storage builders (including Chinese molten-salt EPCs) get no
merchant discharge/controls product at any price. First mover defines the interface.
**Beachhead.** Second-wave thermal-storage integrators and zero-carbon industrial parks (China's
NDRC/MIIT/NEA program, first cohort Aug 2025, build-out 2026–2030 [G04-06]); US DOE Industrial
Heat Shot demos [G04-12]. ASP $200–800K per 10–50 MWth bank.
**Expansion.** Charge-side grid-services aggregation → heat-battery fleet software → >1000 °C
discharge interfaces.
**Frontier vision.** The inverter-equivalent of thermal storage — the standard power/controls
box of heat batteries.
**HW/SW split.** MV power stage + sensing hardware; dispatch/optimization software with
electricity-price + process-demand co-optimization (AI-native).
**TRL/feasibility.** Resistive elements, contactors, MV gear all catalog; integration + control
IP is the product. v1 24 months on a pilot bank.
**Cleanroom dependence.** None.
**China angle.** World's fastest-growing molten-salt base + zero-carbon parks channel [G04-06];
founder networks reach the EPCs directly.
**US angle.** Heat Shot demos, oilfield steam (Rondo's first unit), food/chemicals steam.
**Founder fit.** Power electronics × controls software; energy sector core.
**Novelty declaration.** Nearest excluded: **RID-015** (700 °C particle thermal-storage module)
and **PWR-15** (LDES power-conversion skid). Material difference: sells no storage medium and no
battery PCS — it is the heat-side discharge/controls interface for third-party thermal banks; the
buyer is the storage integrator/EPC, not the grid-storage owner; the product category
(electro-thermal interface electronics) exists in no ledger entry.
**Sources.** [G04-02][G04-03][G04-05][G04-06][G04-12]

## V04 — MV-rated >1000 °C resistive-heating power controller for calciner/kiln electrification retrofits [S] (lane G04)

**Concept.** A dust/vibration-hardened, medium-voltage (1–7.2 kV) solid-state power controller +
element-health analytics for >1000 °C resistive/radiant retrofit sections in cement/lime/chemical
kilns — sold to kiln OEMs (FLSmidth, Sinoma) and plant owners as the electrical heart of partial
electrification, not a full-plant EPC.
**Extreme edge.** Chromalox-class MV controllers stop near 600–1000 °C process duty and clean
environments [G04-13]; Coolbrook-class >1000 °C heaters ship bundled with EPC [G04-01]. A
merchant MV controller rated for kiln-adjacent dust/vibration/thermal cycling with per-zone
element-degradation prediction is unserved.
**Beachhead.** Cement/lime pilot electrification sections in the EU + China ETS window (cement
enters national ETS ~2027 [G04-08]); DOE industrial-decarb awardees [G04-07]. ASP $250K–1M per
zone controller.
**Expansion.** Steel reheat, glass, chemicals; couples naturally with V03 discharge stages.
**Frontier vision.** The power controller of the electric kiln era.
**HW/SW split.** MV SiC/thyristor hybrid stage + element analytics/predictive software.
**TRL/feasibility.** SiC HV devices at usable TRL [G04-17]; element suppliers exist (Kanthal
class); v1 24 months with a kiln OEM pilot.
**Cleanroom dependence.** None.
**China angle.** Largest calciner base on earth (~2.5 Bt/yr cement, 90% of its CO2 from
calcination); Dongfang-class SOEs are climbing the <200 °C tier, leaving >1000 °C open [G04-15].
**US/EU angle.** Heidelberg/Holcim pilots, DOE Heat Shot [G04-12].
**Founder fit.** Harsh-environment packaging (UHV/high-T PhD work) × MV power electronics ×
predictive software.
**Novelty declaration.** Nearest excluded: **C16** (HTS induction heaters) and **N05**
(solid-state RF/microwave process heat). Material difference: pure Joule/radiant resistive
heating — different physical mechanism, different product category (MV controller for resistive
elements), different buyer (kiln OEMs/cement plants, not extrusion shops or RF-heat users). No
ledger entry covers resistive >1000 °C process-heat power electronics.
**Sources.** [G04-01][G04-04][G04-08][G04-13][G04-17]

## V05 — Compact berthed-load shore-tie frequency/voltage converter for ports & vessels [S] (lane G03)

**Concept.** A containerized/skid GaN-SiC AC-DC-AC shore-power converter (250 kVA–2 MVA) that
matches any vessel's onboard frequency/voltage (50/60 Hz, 440/690 V) to any berth, IEC/IEEE
80005-compliant, with utilization-analytics software — sold to port authorities and shipowners
closing the "berth built, nobody plugs in" gap.
**Extreme edge.** Incumbent shore power = ABB/Siemens/Wärtsilä multi-MW substation EPC for
cruise/container berths; nothing compact and catalog-priced exists below that tier. Target
2–3x power density vs. the RMB 800K/MW (~$110K/MW) Chinese benchmark and days-not-months
installation [G03-14].
**Beachhead.** EU TEN-T ports facing the AFIR 31 Dec 2029 mandate with only ~20% of required
connections installed by mid-2025 [G03-12][G03-18]; Chinese ports where berth coverage is
73–100% but usage sat at 17% [G03-14]. ASP $150–500K.
**Expansion.** Workboat/tug DC charging dispensers (200 kW–1 MW band, unstandardized [G03-13])
→ port microgrid interfaces.
**Frontier vision.** The universal grid-to-ship power adapter.
**HW/SW split.** Converter hardware + compliance/billing/utilization software (China MOT 2025
disclosure rules make the software layer sellable alone [G03-06]).
**TRL/feasibility.** Marine-class certification (DNV/CCS) is months; power stage from catalog
modules. v1 18 months.
**Cleanroom dependence.** None.
**China angle.** MOT Order 2025 No.2 compliance instrumentation + the world's largest
underused shore-power base [G03-06][G03-14].
**US angle.** CARB at-berth rules + EPA port grants; West-coast ports.
**Founder fit.** Power conversion × embedded/software; China port networks.
**Novelty declaration.** Nearest excluded: **C01/C03** (marine propulsion power bricks/MW
inverters — incumbent). Material difference: stationary hotel-load interconnect while engines
are OFF — different buyer (port authority/shipowner shore-side budget, not propulsion
integrators), different product category (berth-side frequency converter, not a drivetrain
inverter). C04 (MCS road charging) differs in connector standard, certification path, and buyer.
**Sources.** [G03-06][G03-08][G03-12][G03-14][G03-18]

## V06 — Qualified PTO-to-grid conversion module for wave/tidal energy OEMs [S] (lane G03)

**Concept.** A ruggedized, class-certified, catalog power-conversion module (50–500 kW,
stackable) for the wildly variable output of wave/tidal power take-offs: generator-side AC-DC
with peak-to-average ratios of 5–10x, DC-link buffering, grid-side GFM/GFL inverter, marine
enclosure — sold as a component so PTO developers stop bespoke-commissioning electronics.
**Extreme edge.** Even the sector leader CorPower bespoke-commissions its SiC inverter from
Equipmake [G03-07] — proof no qualified catalog product exists. Handling 10:1 crest factors at
marine duty is a legit extreme-power-electronics problem.
**Beachhead.** WEC/tidal OEMs entering array phase 2027–2030: CorPower VianaWave 10 MW + EMEC
5 MW arrays [G03-07]; US PacWave deliveries under a BPA PPA 2026–2030 with FY2026 federal
marine-energy appropriations at a record $220M [G03-02]. ASP $80–250K/module.
**Expansion.** River hydrokinetic, offshore-wind pitch/aux power, oscillating-load industrial
drives.
**Frontier vision.** The standard power brick of ocean energy.
**HW/SW split.** Converter + wave-by-wave MPPT/predictive control software (AI-native control
is the moat).
**TRL/feasibility.** Components catalog; marine qualification via EMEC/PacWave test slots. v1
18–24 months.
**Cleanroom dependence.** None.
**China angle.** Zhoushan LHD (8+ grid-tied years [G03-16]) + SOE demonstration programs; sell
as imported qualified module or co-develop.
**US angle.** PacWave/TEAMER non-dilutive funding [G03-02].
**Founder fit.** Power electronics × control software; energy sector.
**Novelty declaration.** Nearest excluded: **N04** (subsea inductive power & docking). Material
difference: power flows FROM a harvesting device TO the grid — opposite direction, different
buyer (energy-device OEMs, not AUV/ROV operators), different category (grid-interface conversion,
not inductive couplers). C01/C03 are propulsion bricks; this is generation-side.
**Sources.** [G03-02][G03-07][G03-16]

## V07 — Vendor-agnostic laser-power-beaming receiver module [S] (lane G05, photonics × power hybrid)

**Concept.** A drop-in optical-power receiver: concentrator optics + wavelength-matched (or
broadband) PV array + MPPT/power-conditioning + thermal management + safety interlock telemetry,
sold as a qualified module to power-beaming transmitter primes, drone OEMs, and remote-site
integrators — the receive-side standard while every program now builds one-offs.
**Extreme edge.** DARPA POWER's 2025 record (800 W over 8.6 km, >20% receiver efficiency on
off-the-shelf PV) proved receivers commoditize [G05-01][G05-03]; a qualified module with 2x
that efficiency (wavelength-matched cells + active cooling) and W/kg specs no program build
matches is a clean 10x-vs-status-quo story.
**Beachhead.** DARPA POWER phases 2–3 hand specs to industry 2026–2028 [G05-02]; Kraus
Hamdani/AFB demos are already flying (Apr 2026) [G05-13]. DoD long-endurance UAS + forward-base
programs. ASP $50–200K/receiver.
**Expansion.** HALE aircraft, lunar/space assets, tower-to-tower utility power, China's earlier-stage
research programs [G05-06].
**Frontier vision.** The photovoltaic "socket" of wireless power infrastructure.
**HW/SW split.** Receiver hardware + beam-tracking/safety/power-management firmware and fleet
telemetry.
**TRL/feasibility.** PV cells, concentrators, converters purchasable; integration + qualification
is the product. v1 18 months at kW class.
**Cleanroom dependence.** None (buys cells).
**China angle.** Chinese literature calls the field 初级研究阶段 (early research) [G05-06] — sell
instrumentation-grade receivers into research programs; export-control review required (dual-use).
**US angle.** Primary: DARPA/AFRL/Navy demos → program-of-record transition ~2029.
**Founder fit.** Power conversion × precision optics-adjacent motion/alignment × harsh packaging.
**Novelty declaration.** Nearest excluded: **C29** (smallsat PPU/PCDU; space EP power neighbor)
and **C26/C28** (space power modules). Material difference: terrestrial/airborne optical-power
receive conversion — different buyer (power-beaming primes/UAS OEMs, not satellite buses),
different category (PV receiver module, not spacecraft power units). RID-100/CL-09 are assembly
tools — unrelated.
**Sources.** [G05-01][G05-02][G05-03][G05-06][G05-13]

## V08 — Catalog SWaP-optimized fast-steering-mirror drive + tracking controller card [S] (lane G05)

**Concept.** A catalog-priced FSM drive-electronics + tracking-controller card (FPGA control
loop, kHz-class closed loop, quaternion-fed feed-forward, disturbance rejection) compatible with
third-party voice-coil/piezo FSMs — the missing merchant electronics layer for FSO terminals,
drone laser links, and shipboard beam control.
**Extreme edge.** Trade press documents the gap: no product spans galvo-class speed,
micro-gimbal compactness, and zero-power holding [G05-08]; the reference supplier (Cedrat) sells
bespoke, price-on-request [G05-12]. A catalog card at <100 g / <10 W with published tracking
specs is 10x on procurement friction alone.
**Beachhead.** FSO terminal integrators (GA-ASI LAC-12 class pods [G05-07]), OGS builders,
Navy directed-energy beam control (open SBIR: wave-slap mitigation [G05-18]). ASP $15–60K/card.
**Expansion.** Optical ground stations → power-beaming pointing → quantum-link telescopes;
pairs with V07 and V09.
**Frontier vision.** The motion-control silicon of free-space photonics.
**HW/SW split.** Drive card hardware + tracking/stabilization firmware + integration SDK.
**TRL/feasibility.** Founder built laser-aligned precision motion control already; v1 12
months.
**Cleanroom dependence.** None.
**China angle.** China's OGS build-out (first operational station Sept 2024 [G05-05]) is a
buyer of beam-control electronics — export review required; likely US/allied-first.
**US angle.** SDA/Space Force proliferated-LEO ground segment + Navy SBIR channel [G05-18].
**Founder fit.** FPGA real-time control × precision electromechanics (winding machine) ×
low-noise electronics — exact graph.
**Novelty declaration.** Nearest excluded: **RID-111** (high-bandwidth piezo actuator).
Material difference: sells the drive/control ELECTRONICS + tracking software for third-party
mirrors — different product category (controller card vs. actuator) and different buyer
(FSO/directed-energy integrators vs. nanopositioning users). C25 (overlay inspection) and CL-09
(CPO assembly) are unrelated wafer-level tools.
**Sources.** [G05-07][G05-08][G05-12][G05-18]

## V09 — Field-hardened White-Rabbit-class timing & synchronization appliance [S] (lane G06)

**Concept.** A telecom-grade, environmentally hardened (-40 to +70 °C, fanless, redundant-PSU,
remote-managed) sub-nanosecond time-transfer node implementing White Rabbit / IEEE 1588 HA,
purpose-built for unattended quantum-network nodes, VLBI/optical-clock links, accelerator halls,
and defense timing — replacing lab-bench switches in the field.
**Extreme edge.** The de facto supplier ships a lab switch (-10 to 50 °C, 80 W, 18 ports)
[G06-09]; nothing exists for unattended outdoor/remote nodes that quantum networks and
six-telescope VLBI-class arrays (already at 10^-15 s/s agreement [G06-08]) deploy 2027–2030.
Sub-ns over >100 km with field MTBF is the spec war a founder can win.
**Beachhead.** National-lab quantum testbeds, QKD network pilots (CERN frames entanglement
timing as partner-built infrastructure, not product [G06-02]), radio astronomy, TSN-adjacent
defense. ASP $25–80K/node.
**Expansion.** Timing-as-infrastructure for distributed sensing, 6G fronthaul research, GPS-denied
PNT.
**Frontier vision.** The timing backbone of quantum-era infrastructure.
**HW/SW split.** Hardened node hardware + fleet-management/holdover-analytics software.
**TRL/feasibility.** White Rabbit is open (CERN OHL); hardening + productization is the work.
v1 12–15 months.
**Cleanroom dependence.** None.
**China angle.** CAS quantum-network programs buy timing; White-Rabbit-derived gear is less
export-sensitive than cryo/photonics today [G06-18] — separate SKU + compliance track.
**US angle.** DOE labs, SDA ground timing, NIST/JILA-adjacent optical-clock networks.
**Founder fit.** FPGA + low-noise instrumentation + big-physics deployment credibility
(stellarator).
**Novelty declaration.** Nearest excluded: **C10** (magnet/scientific power converters — carries
watts; this carries picoseconds) and **EXT-21** (rad-hard in-vessel telemetry). Material
difference: timing/sync distribution product for facility networks — different category (no
power conversion, no in-vessel radiation environment) and different buyer function (facility
timing engineer). Platform-agnostic across quantum/astronomy/accelerators; no superconductor
dependence (G6-HTS clean).
**Sources.** [G06-02][G06-08][G06-09][G06-18]

## V10 — Vendor-agnostic real-time QEC decoder / feedback appliance [S] (lane G06, quantum × AI hybrid)

**Concept.** A rack appliance (FPGA/ASIC-class latency, streaming architecture) that takes
syndrome data from ANY control stack and returns decode/feedback decisions under 1 µs — sold as
a catalog instrument to the long tail of QPU makers, national labs, and neutral-atom/ion
startups that cannot build in-house decoder teams.
**Extreme edge.** Riverlane's decoders ship bundled inside partner stacks (Infleqtion, OQC,
Rigetti), not as a merchant box [G06-12]; control-rack vendors lock decoding into proprietary
software [G06-03]. A vendor-neutral, sub-µs streaming decoder with open interfaces is both a
real-time-compute extreme spec and an unclaimed product category.
**Beachhead.** 20+ QPU programs worldwide entering early-QEC (2027–2030) without decoder teams;
DOE testbeds (QICK's ~500-user community as channel [G06-14]). ASP $60–250K.
**Expansion.** Real-time feedback beyond QEC: atom-array rearrangement, ion shuttling,
stabilization loops; classical co-processing for quantum-classical algorithms.
**Frontier vision.** The real-time classical brain every fault-tolerant machine buys.
**HW/SW split.** FPGA appliance + decoder algorithm library (AI-assisted decoders) + SDK.
**TRL/feasibility.** Decoding algorithms are published; productizing latency + interfaces is
the work. v1 15–18 months.
**Cleanroom dependence.** None.
**China angle.** Origin/USTC-adjacent ecosystem runs its own stack [G06-07][G06-17]; a
teaching/pilot-tier SKU is possible but export scope may widen by 2028–31 [G06-18] — plan
firewalled lines.
**US angle.** Primary; national-lab testbeds + startup QPU long tail.
**Founder fit.** FPGA real-time systems × algorithms/AI × instrumentation — direct.
**Novelty declaration.** Nearest excluded: **CL-24/EXT-17** (cryo-CMOS quantum control — BLOCKED
lane) and **C34** (ultra-low-noise SMU). Material difference: room-temperature digital decode
appliance — different category (streaming classical co-processor, not cryogenic control chips,
not analog source-measure) and different buyer function (QEC/software teams). Platform-agnostic;
zero superconductor dependence in the product (G6-HTS clean).
**Sources.** [G06-03][G06-12][G06-14]

## V11 — Robotic magnet-harvesting disassembly cell for motors, HDDs & turbine generators [S] (lane G07)

**Concept.** A semi-automated robotic cell (vision + force control + programmable fixturing +
induction-free thermal/mechanical extraction) that removes intact NdFeB magnets from EV drive
motors, HDDs, and wind-generator rotors at 10–60x manual throughput, preserving magnets for
direct reuse or high-purity recycling feed — sold as capital equipment to magnet recyclers and
dismantlers.
**Extreme edge.** Today magnets are shredded into mixed streams because manual extraction
doesn't scale; the EU's ADIR demo (2015–2019) never commercialized [G07-06]. A production cell
that harvests intact magnets flips feedstock economics (intact NdFeB ≫ mixed scrap value).
**Beachhead.** The US/EU magnet-recycling build-out: DoW committed $1.4B to
ReElement/Vulcan targeting 10,000 t/yr NdFeB [G07-13]; Noveon ($215M Series C), Cyclic ($75M
Series C) [G07-08][G07-10] — all vertically integrated and equipment-hungry. ASP $400K–1.2M/cell.
**Expansion.** E-waste boards, battery-pack disassembly (equipment sale, not grading), catalytic
converters; recipe library becomes the moat.
**Frontier vision.** Urban mining as automated manufacturing in reverse.
**HW/SW split.** Robotic cell + vision/force AI + device-recipe software.
**TRL/feasibility.** Robots/EOATs catalog; the disassembly recipes + fixturing are the IP. v1
18 months on HDD/motor mix.
**Cleanroom dependence.** None.
**China angle.** GEM-class recyclers (>99.9% purity, 57 patents [G07-12]) as customers/partners;
mechanical subsystem sourcing via founder network.
**US angle.** DoW-funded capacity 2026–2029 needs equipment NOW [G07-13]; sells picks-and-shovels
into policy money without commodity-price exposure (Li-Cycle lesson [G07-11-context]).
**Founder fit.** Precision automation/machine building (winding machine) × vision/AI × China
supply chain.
**Novelty declaration.** Nearest excluded: **IND-09** (autonomous machining cell) / **IND-23**
(micro-assembly cell) / **CL-14** (robot actuation). Material difference: DISASSEMBLY for
material recovery — different buyer segment (recyclers/dismantlers, not manufacturers), different
product category (magnet-harvesting cell). C40/RID-016 excluded (battery-pack grading/reuse) —
this cell never grades packs. Lane G07 is fully virgin per charter.
**Sources.** [G07-06][G07-08][G07-10][G07-12][G07-13]

## V12 — Heavy-REE magnetic-signature triage sensor for recycling feedstock [T] (lane G07) — PhD-LANE FLAG

**Concept.** A conveyor-mounted magnetometer-array + field-inversion sensor head that classifies
magnet-bearing feedstock pre-shred: NdFeB vs. ferrite vs. SmCo, magnetized vs. thermally
demagnetized, high- vs. low-Dy/Tb — so recyclers route high-value heavy-REE magnets out of
low-value mixed streams. Sold as a standalone instrument to recyclers and scrap processors.
**Extreme edge.** No inline REE-triage instrument exists (SGM/Sesotec ECS lines separate by
conductivity, blind to REE grade [G07-14]); magnetometer-array inversion at conveyor speed is
exactly the founder's demonstrated capability transplanted from battery cells to scrap.
**Beachhead.** HyProMag/Cyclic/Noveon-class magnet recyclers whose HPMS/hydromet feed purity
sets yield [G07-01][G07-02]; GEM-class Chinese recyclers [G07-12]. ASP $80–250K/head.
**Expansion.** Motor-sorting at auto shredders, wind-turbine decommissioning, magnet QC in
re-manufacturing.
**Frontier vision.** Field-signature fingerprinting as the routing layer of urban mining.
**HW/SW split.** Sensor-array head + inversion/classification software (AI on field maps).
**TRL/feasibility.** Room-temp magnetometer arrays + inversion algorithms demonstrated in the
founder's PhD; conveyor hardening is the work. v1 12 months.
**Cleanroom dependence.** None.
**China angle.** GEM/JL Mag ecosystem [G07-12]; Chinese separator OEMs as integration partners.
**US angle.** DoW-funded REE independence push [G07-13].
**Founder fit.** Magnetometer arrays + current/field inversion = PhD core, non-battery domain.
**PhD-lane note (criterion-1 anti-anchoring applies):** capability leverage is real but score
the LEVERAGE, not familiarity; red team must verify this is not "battery magnetic imaging
productized" — it is not (no batteries, no current injection), but it IS the magnetic-imaging
skillset, hence the flag.
**Novelty declaration.** Nearest excluded: **C33** (cryogenic coil QC instruments) and **C31**
(OPM magnetometers). Material difference: room-temperature conveyor triage of recycling
feedstock — different buyer segment (recyclers, not magnet manufacturers or biomag labs),
different category (sorting instrument, not coil QC or OPM sensor product). C40/RID-016
(pack grading) untouched.
**Sources.** [G07-01][G07-12][G07-13][G07-14]

## V13 — Bolt-on multi-modal weld-QC sensor head for battery module/pack lines [T] (lane G01)

**Concept.** A retrofit sensor head (photodiode plume + vision + eddy-current fusion, NO
magnetic-imaging) mounting on existing tab/busbar laser welders, with edge-AI classification
and IATF-grade weld serialization — sold as a sub-$100K add-on to module/pack and BESS
container lines instead of a new turnkey line.
**Extreme edge.** Production inline vision hits 97.9% accuracy with 11.5% false alarms
[G01-04]; multi-modal fusion targets >99.7% detection at <2% false alarm on the fatter, fewer,
higher-consequence 500Ah+ joints now arriving [G01-11]. Nobody sells this un-bundled [G01-10].
**Beachhead.** Second-tier US pack/BESS lines needing retrofits, not lines [G01-14]; Chinese
container integrators with documented manual-QC pain [G01-09]. ASP $60–120K/head + software.
**Expansion.** Serialization/traceability node (IATF 16949 Cpk evidence [G01-15]) → busbar NDT
→ EOL commissioning checks.
**Frontier vision.** The independent QC layer of electrification manufacturing.
**HW/SW split.** Sensor head + edge-AI inference + traceability software.
**TRL/feasibility.** Sensors catalog; fusion models are the IP. v1 12 months on a partner line.
**Cleanroom dependence.** None.
**China angle.** Wuxi-Lead-dominated lines still lack un-bundled QC add-ons [G01-10]; sell the
retrofit into the world's largest installed base.
**US angle.** Onshoring BESS/pack lines (Ford LFP-to-BESS pivot, Form Energy datacenter deal
[G01-17-context]).
**Founder fit.** Instrumentation + edge AI + machine integration; deliberately NON-magnetic
(not PhD-lane).
**Novelty declaration.** Nearest excluded: **IND-08** (silver-sinter die-attach cell w/ inline
void metrology) and **CL-13** (battery manufacturing lines). Material difference: retrofit QC
head for battery interconnect welds — different buyer segment (pack/BESS integrators, not
power-module packagers), different category (bolt-on sensor head, not a die-attach cell or
manufacturing line). C22 (PD/insulation EOL rigs) tests insulation, not welds.
**Sources.** [G01-04][G01-09][G01-10][G01-11][G01-15]

## V14 — Brand-agnostic trolley-assist retrofit interface for mining haul trucks [S] (lane G08)

**Concept.** A pantograph-to-drivetrain power interface (MW-class pantograph front-end, DC
conditioning, drivetrain-bus injection, connection-dynamics control) that lets ANY diesel-electric
haul truck (Cat, Komatsu, Liebherr, BelAZ, SANY, XCMG) use trolley lines — sold to mine
operators with mixed fleets instead of OEM-locked packages.
**Extreme edge.** OEM trolley kits are proprietary and fleet-locking [G08-03][G08-08]; a
certified brand-agnostic interface at 2–4 MW with automated wire acquisition (Komatsu proved
autonomous trolley 2025 [G08-04]) unlocks the majority mixed-fleet installed base. 170–227 L/hr
diesel burn per truck is the payback engine [G08-10].
**Beachhead.** Open-pit copper/iron mines running mixed fleets on decarbonization mandates
(Boliden-pattern economics: $31.2M for 4.8 km + 23 trucks [G08-03-context]). ASP $250–600K/truck
+ line-side services.
**Expansion.** Underground trolley variants, battery-buffer integration, autonomous-fleet
coordination software.
**Frontier vision.** The interoperability layer of mine electrification.
**HW/SW split.** Power interface hardware + wire-acquisition/fleet-coordination software.
**TRL/feasibility.** Pantographs/converters exist; the OEM-agnostic drivetrain integration +
control is the product. v1 24 months with one mine pilot.
**Cleanroom dependence.** None.
**China angle.** SANY/XCMG trucks + Chinese EPCs electrifying Belt-and-Road pits; zh sources
document trolley economics [G08-12].
**US angle.** Freeport/Rio-class US pits; IRA-adjacent decarb capital.
**Founder fit.** MW power electronics × harsh-environment (dust/vibration) packaging × controls.
**Novelty declaration.** Nearest excluded: **C04** (MCS truck-charging modules). Material
difference: dynamic rail-style current collection while hauling — different buyer segment (mine
operators, not road-charging depots), different product category (pantograph interface +
drivetrain injection, not plug-in MCS chargers), different certification path (mining, not
road-vehicle). C01/C03 are propulsion inverters — this feeds the EXISTING drivetrain.
**Sources.** [G08-03][G08-04][G08-08][G08-10][G08-12]

## V15 — Vendor-agnostic battery-buffer retrofit kit for RTG container cranes [S] (lane G08)

**Concept.** A drop-in battery-buffer + regenerative power stage (200–600 kWh LFP, bidirectional
DC-DC into the crane's native drive bus, peak-shave + regen-capture control) that converts any
OEM's cable-reel/conductor-rail or diesel-hybrid RTG to grid-light electric — cutting required
grid feed ~6x (Konecranes' own E-Hybrid: 60 kW vs. 400 kW) without buying new $1.9M cranes.
**Extreme edge.** Konecranes retrofits only its own fleet [G08-14]; ZPMC sells new cranes. The
multi-OEM legacy base (e.g., ~100 non-cable-reel RTGs at one Georgia terminal) has no
vendor-neutral kit. Regen capture on hoist-down is free energy the drive bus wastes today.
**Beachhead.** Independent terminal operators with mixed 10–25-year fleets; Gdynia-pattern
economics (EUR 10.9M NPV on 7 cranes [G08-15]); first pure-battery RTG order proves appetite
(Apr 2025 [G08-13]). ASP $250–500K/crane.
**Expansion.** Reach stackers, straddle carriers, mining shovels; port energy-management
software across retrofitted fleets.
**Frontier vision.** Retrofit-first electrification of the world's yard-equipment base.
**HW/SW split.** Buffer + converter hardware; peak-shave/regen/fleet-energy software.
**TRL/feasibility.** LFP + bidirectional DC-DC catalog; per-OEM drive-bus integration recipes
are the moat. v1 15–18 months.
**Cleanroom dependence.** None.
**China angle.** ZPMC-dominated global installed base; Chinese port retrofits + component
sourcing; land-side only (no overlap with G03 water-side scope).
**US angle.** EPA Clean Ports + CARB; Georgia/LA-class terminals [G08-11].
**Founder fit.** Power electronics × battery systems × embedded control.
**Novelty declaration.** Nearest excluded: **C08** (GPU transient buffer / facility
ride-through). Material difference: port-crane duty (hoist regen, 1–4 MW peaks, outdoor
salt/dust) — different buyer segment (terminal operators, not datacenter/colo operators),
different product category (crane drive-bus retrofit kit, not rack/facility UPS-class buffer).
C09 (SST blocks) untouched — no MV solid-state transformer stage.
**Sources.** [G08-11][G08-13][G08-14][G08-15]

---

## Gate check summary (G1–G7)

| ID | G1 seed-scale 2029/30 | G2 HW+SW | G3 cleanroom | G4 named beachhead | G5 Magnefy | G6 HTS | G7 novelty declared |
|----|----|----|----|----|----|----|----|
| V01–V15 | all pass (largest v1 capex V11/V14 ≈ $1.5–3M) | all pass (every candidate ships control/AI software) | none–low | all pass | all pass | all pass (0 superconductor-dependent) | all pass (declarations above) |

Reserve note: none of the 40 Phase-1 seeds outside these 15 was gate-blocked; the 25 unused
seeds remain available as replacement stock if red team kills a candidate (per Phase-7 rule).
