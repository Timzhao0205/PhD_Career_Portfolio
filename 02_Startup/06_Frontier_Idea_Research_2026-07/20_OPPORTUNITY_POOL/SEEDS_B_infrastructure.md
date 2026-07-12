# SEEDS — Batch B: Energy & Digital Infrastructure (L02, L03, L08, L14)

Architect: idea-architect, claude-fable-5 / xhigh. Date: 2026-07-12. 18 seeds (B01–B18), all
anchored in accepted ledger IDs; rejected IDs in these lanes were checked and none are cited.
ATLAS constraints honored: no grid-forming-services plays (NESO zero-award, L08-035 context); all
two-phase plays carry explicit post-Novec/PFAS fluid plans; HTS "commercial" cable caution applied
(L03-041); design-in vs booked-order distinction flagged where relevant (L02-050, L02-047).

## B01 — 800VDC rack-inlet solid-state power controller (L02/L08)
Product: 800V/100–200A bidirectional SiC SSPC with zero-arc hot-swap, active pre-charge, <100 µs
clearing, oscillation damping, OCP form factor. Buyers: Delta, Eaton, Vertiv, Schneider; hyperscalers
via OCP Mount Diablo. Pain: 800V inlet grounding/hot-swap/inrush unresolved (L02-054); no resettable
DC breaker at this class (L08-017). Demand: L02-043/044, L08-033, L02-053. Incumbents miss: AC-heritage
protection portfolios; OCP spec fluid; chips-not-subsystems vendors. Experiment ($140k): SSPC + rack-inlet
emulator, witnessed 20 kA-prospective clearing and oscillation-free hot-swap. Vision: protection layer of
the DC datacenter. Substitutes: fuses+contactors, Hitachi hybrid breaker concepts (L08-052).
Uncertainty: OCP may absorb protection into power-shelf spec; unwritten UL/IEC path. Confidence: high.

## B02 — Vertical 48V→sub-1V power-delivery tile (L02/L14)
Product: hybrid-SC + coupled-inductor tile mounted under the accelerator package, >2 A/mm², per-phase
telemetry. Buyers: MGX-ecosystem ODMs, hyperscaler custom-silicon programs. Pain: 48V→<1V @ 2000A
unsolved (L02-022/023); NVIDIA eliminating stages (L02-043). Demand: L02-043/044/046. Competitors: Vicor
(L02-113), Navitas (L02-046), ecosystem silicon (L02-043). Experiment ($180k): 1.2 kW tile, ≥89% full-load,
1 A/ns transient, calorimetric. Vision: the standard "power socket" for >2 kW silicon. Uncertainty: captive
sockets; Vicor patent thicket; entry via AI-ASIC startups. Confidence: medium.

## B03 — Qualified MV high-frequency transformer brick for SSTs (L02/L08)
Product: 250 kW, 30–50 kHz, 13.8 kV-isolation PD-free transformer + resonant tank subsystem, test data
mapped to IEC 62477-1/60076 clauses. Buyers: OCP SST-track vendors (Delta/Eaton/Vertiv), ARPA-E DC-GRIDS
teams, Microchip 3.3 kV module users (L02-052). Pain: MV-HF insulation and winding-loss/parasitic tradeoffs
open (L02-001/019/020); SST standards-blocked (L02-036). Demand: L02-044, L02-034, L02-052, L02-111.
Experiment ($200k): 100 kW prototype, PD inception >2x working voltage, calorimetric loss map. Vision:
the magnetic core of grid-edge solid-state power. Uncertainty: SST commercialization timing — wedge must
live on datacenter/DC-GRIDS pilots. Confidence: medium.

## B04 — GaN/SiC dynamic-reliability qualification bench (L02)
Product: mission-profile stressor with ns-resolution on-state clamp: in-circuit dynamic Ron, trapping,
threshold drift at 800 V real switching; standardized qual report. Buyers: Navitas, Innoscience (publicly
stuck "in testing," L02-050), ROHM, module/PSU vendors, hyperscaler qual labs. Pain: dynamic Ron defeats
lifetime prediction (L02-006, L02-013–016). Demand: L02-050/047/044/046. Substitutes: one-off academic
rigs (L02-013/016). Experiment ($90k): reproduce published trapping signatures blind; one paid vendor
pilot. Vision: the reliability-evidence layer ("JEDEC-plus") of the WBG transition. Uncertainty: modest
instrument TAM; standardization commoditizes method. Confidence: high.

## B05 — Adaptive active gate driver for 3.3–10 kV SiC with ageing telemetry (L02/L08)
Product: fiber-isolated module-mounted drive: per-event dv/dt shaping, overshoot suppression, Vds(on)
degradation trending. Buyers: datacenter-SST builders (L02-052), Wolfspeed 10 kV adopters (L02-047), MMC
valve OEMs (L08-033/034). Pain: WBG gate-drive robustness open (L02-011/012); packaging failures unseen
until field (L02-028, L02-108). Experiment ($120k): 3.3 kV double-pulse/short-circuit campaign, ~30%
switching-loss gain vs passive drive. Vision: every MV SiC position self-reports health. Substitutes:
Power Integrations-class generic drivers; OEM-internal boards. Uncertainty: long design-ins; small MV SiC
volumes near-term. Confidence: medium.

## B06 — Series-stackable hybrid MVDC breaker brick (L08/L02)
Product: 1.5 kV/2 kA hybrid brick (Thomson-coil isolator + SiC/IGCT interrupter + MOV), stackable to
±10 kV, built-in traveling-wave fault location, self-test. Buyers: GE Vernova ($2.4bn/qtr datacenter
electrification, L08-033), Hitachi Energy, DC-GRIDS teams (L02-034), State Grid supply chain (L08-034).
Pain: DC breakers the documented showstopper; no converged topology (L08-001/003/013–015/017). Experiment
($220k): synthetic-circuit 1.5 kV/1 kA interruption, 100-op resettability. Vision: meshed DC grids made
protectable — the "Square D of DC". Substitutes: full-bridge MMC fault blocking (L08-022/023); Hitachi
bespoke breakers (L08-052); ORNL prototypes (L08-051). Uncertainty: qualification cycles; converter-embedded
blocking may cap it to the MVDC/datacenter beachhead. Confidence: medium.

## B07 — Deterministic DC arc-fault detection/location for 800VDC halls (L08/L02/L14)
Product: busway/shelf nodes fusing RF + HF current signature + optical flash in deterministic FPGA logic;
<5 ms trip to rack SSPCs; per-node synthetic-arc self-test; segment-level location. Buyers: busway/rack
vendors (Delta, Vertiv, Eaton per L02-043), hyperscalers; insurers as channel. Pain: DC arc detection
unsolved even at PV voltages (L08-019–021); 800 V halls raise stakes (L02-054). Demand: L08-033,
L02-043/044. Experiment ($80k): UL1699B-style arc rig + rack-noise soak, zero false trips/72 h. Vision:
fire-safety layer for all DC infrastructure (BESS, PV, MVDC). Uncertainty: nuisance-trip liability;
no standard yet — must drive it. Confidence: medium.

## B08 — MMC submodule health monitor + fast bypass (L08/L02)
Product: per-submodule capacitor ESR/C drift + IGBT Vce(on) trending from existing sensing, plus <200 µs
hardened bypass; vendor-agnostic, fiber-networked. Buyers: GE Vernova (~$10bn HVDC backlog, L08-033),
Hitachi/BHEL (L08-030), owners POWERGRID/Adani (L08-028/029), XJ-class vendors (L08-034). Pain: submodule
fault tolerance live research (L08-022–024); forced outages cost GW-days. Experiment ($110k): aged-capacitor
submodule bench, ESR tracking + 1000 bypass ops. Vision: condition-based maintenance for the global MMC
fleet. Substitutes: OEM-internal monitoring; scheduled replacement; redundancy margin. Uncertainty: OEM
access/warranty walls — may need mid-tier or new-build design-in first. Confidence: medium.

## B09 — DC-PD + traveling-wave integrity monitor for 525 kV XLPE HVDC (L08/L03)
Product: termination/joint-mounted HFCT+UHF DC-PD monitor with pulse-sequence discrimination plus passive
traveling-wave recorders using converter transients as probing signals; <100 m pre-location. Buyers:
TenneT (NKT ~EUR2bn, L08-031), SPT/NGET (Prysmian EGL1, L08-032), cable-OEM warranty arms. Pain: first-of-kind
insulation at multi-billion-euro scale, standards lag (L08-044/046), no continuous condition visibility.
Experiment ($150k): defected MV-DC samples at 1.5x Uo + VSC transients — build the missing public dataset.
Vision: insulation-health telemetry as a standard cable-contract clause. Uncertainty: sparse DC-PD physics;
slow TSO procurement; OEM conflict-of-interest as channel. Confidence: medium.

## B10 — Multi-modal REBCO quench detection/protection controller (L03)
Product: co-wound Rayleigh-backscatter fiber + acoustic emission + ramp-synchronized low-noise taps, FPGA
fusion, <1 ms decision, drives extraction/heater/CLIQ protection; per-magnet config. Buyers: CFS magnet
customers (Realta, WHAM — L03-035), TE Magnetics (L03-033/044), DOE milestone awardees (L03-032), labs
(L03-029/030). Pain: HTS quench detection unsolved at MJ scale; NI windings a costly workaround
(L03-004–008, L03-018). Experiment ($85k): 77 K pancake coil, quantified detection lead vs voltage taps.
Vision: certified safety layer of the HTS magnet industry. Substitutes: in-house tap+heater stacks; bare
fiber interrogators. Uncertainty: bespoke-per-magnet NRE vs product; export screening for some Asian
buyers. Confidence: high.

## B11 — Reel-to-reel REBCO tape Ic/defect mapping line (L03)
Product: magnetic-knife + Hall-array continuous Ic mapper in LN2 with eddy/ultrasonic delamination
channels; per-meter quality passport feeding winding-plan software. Buyers: magnet builders doing incoming
inspection (Tokamak Energy's several-hundred-km Furukawa order, L03-044; CFS L03-035) and tape producers
(L03-019, L03-052). Pain: <10 vendors, allocation-constrained tape, strain/delamination degradation
(L03-018/020/021), sampled acceptance tests. Experiment ($70k): prototype vs 4-point ground truth on
seeded-defect tape, m/min, <2% agreement. Vision: the acceptance-data standard for HTS conductor.
Uncertainty: small buyer universe; producers may give data away. Confidence: high.

## B12 — Modular N+1 cryogenic power skid, 20–77 K (L03/L14/L08)
Product: containerized cryocooler array on a common cold bus, N+1 hot-swap without load warm-up,
load-sharing control, standardized cryostat interfaces — cryo specified like a UPS. Buyers: KEPCO/LS
datacenter-HTS program (L03-042/043), SupraMarine/RTE (L03-034), mid-scale magnet labs, fusion supply
chain (L03-032/035). Pain: nothing exists between mW-class coolers (L03-050) and bespoke helium plants
(L03-025/026). Experiment ($190k): two-cooler cold bus, hot-swap under load, temperature held in spec.
Vision: "cold as a utility" for HTS deployment. Substitutes: single coolers + manual spares; LN2 delivery
contracts; big plants (L03-047/049/050). Uncertainty: HTS grid demand may stay pilot-scale; COTS physics
means incumbents can follow. Confidence: medium.

## B13 — HTS DC bus segments (10–50 kA) for AI-campus power spines (L03/L02/L08) [frontier/wildcard]
Product: factory-built rigid vacuum-jacketed REBCO DC bus segments (50–500 m runs) with plug-together
joints and engineered low-loss current leads; integrates with B12 skid; sold per-segment vs copper-busway
TCO. Demand bridge: KEPCO/LS/LS Electric MOU explicitly citing AI datacenter load (L03-042/043); NVIDIA's
45% copper-reduction pressure (L02-043); GE datacenter electrification wave (L08-033). Pain: copper
economics/space at kA-scale DC. Experiment ($240k): 10 m/5 kA demo bus, end-to-end losses incl. lead heat
leak and cooling COP vs copper benchmark. Incumbents miss: cable giants do utility projects, not productized
short runs (L03-041 caution: all installs are single state-directed demos). Uncertainty: whether HTS-vs-copper
closes at realistic campus currents — decisive risk, honestly flagged. Confidence: low.

## B14 — Hermetic pumped two-phase cold-plate loop with post-PFAS dual-fluid strategy (L14/L02)
Product: per-shelf sealed loop (micro-pump + manifold-microchannel flow-boiling evaporator + rack condenser
to Deschutes-class facility water); fluid plan by design: R-1233zd(E)-class low-pressure HCFO qualification
track (ITRI-validated class, L14-053) plus <150 g micro-charge R-600a PFAS-free endgame track (AIM Act
L14-033, EU F-gas L14-034). Buyers: Deschutes-ecosystem ODMs/CDU vendors (L14-043), hyperscalers, Singapore
DC-CFA2 builds (L14-037). Pain: 3–5 kW chips, 800–1000 W/cm² local flux (L14-009/010); field's fluid base
collapsed mid-literature (L14-022). Competitors: ZutaCore ($100M C, L14-046), Flex/JetCool (L14-045),
Trane/LiquidStack (L14-051), ITRI (L14-053). Experiment ($130k): 3.5 kW test vehicle, both fluids, dry-out
margin + resistance curves vs single-phase. Uncertainty: TFA scope creep onto HCFOs; single-phase keeps
stretching; 3M exit dates need primary confirmation in P4. Confidence: medium.

## B15 — Contained liquid-metal TIM preforms ("gasketed LM-TIM") (L14/L02)
Product: galinstan caged in microstructured honeycomb carrier with Ni/W barriers — pad-like handling,
no pump-out, 500 W/cm² hotspots, <5 K·mm²/W, 1000-cycle qualified. Buyers: AI-accelerator packagers/ODMs
(GB200-class, L14-044), cold-plate vendors (L14-043 ecosystem), COOLERCHIPS-lineage integrators (L14-030).
Pain: TIMs now first-order constraint for 2.5D/3D chiplets (L14-014–018). Experiment ($60k): D5470+transient
vs PCM and bare LM, cycling with X-ray/acoustic pump-out imaging, corrosion coupons. Vision: standard
interface material for every >1 kW package. Substitutes: PTM-class films, graphite sheets, bare LM, sintered
silver. Uncertainty: 12–24 month quals; gallium edge cases; IP on containment is the moat question.
Confidence: medium.

## B16 — Microchannel liquid-liquid HX cartridge for 2 MW CDUs at 3°C approach (L14)
Product: diffusion-bonded 316L counterflow microchannel core with fractal headers: ~98% effectiveness,
half the volume, ~40% lower pumping power vs brazed-plate at the Deschutes 3°C/~80 psi corner (L14-043);
PG25-fluid compatible (L14-049). Buyers: the 7+ Deschutes CDU vendors (Boyd, CoolerMaster, Delta, Envicool,
Nidec, nVent, Vertiv — L14-043), Flex/JetCool (L14-045); demand backdrop: Vertiv +50% liquid orders,
$15B backlog (L14-048). Experiment ($95k): 150 kW core vs commercial BPHE on instrumented rig + fouling
soak. Vision: the standard heat-transfer core of the liquid-cooled datacenter, then two-phase condensers
and heat-reuse. Uncertainty: diffusion-bonding cost at datacenter price points; incumbent response speed.
Confidence: medium.

## B17 — AM oscillating-heat-pipe conformal spreaders for radar/satellite payloads (L14)
Product: laser-printed AlSi10Mg/Ti panels with embedded OHP channel networks — structure that moves heat;
>5 kW/m·K panel-scale conductivity, passive, orientation-insensitive, PFAS-free fluids by construction.
Buyers: radar primes (Raytheon — named COOLERCHIPS awardee, L14-030), satellite bus makers, NASA/DoD
programs. Pain: three decades of DARPA thermal programs and still no transferable commodity (L14-025);
LHP/OHP and radar co-design open (L14-023/024/027). Experiment ($110k): 300 mm panel through vibration,
thermal-vac, and 12-month hermeticity — the qual dataset primes ask for first. Vision: OHP-embedded skins
default on radar faces and satellite panels, feeding back to terrestrial power electronics. Uncertainty:
MIL/NASA qual burden, AM hermeticity yield, slow defense cycles. Confidence: medium.

## B18 — Two-phase MCS cable/connector thermal module, post-Novec (L14/L02/L10 link) [weakest-demand seed]
Product: sealed two-phase annular cable core + connector-pin evaporator insert + charger-side condenser
(HCFO or micro-charge hydrocarbon fill), sold as qualified subsystem to cable/connector OEMs; 1500 A
continuous in a hand-manageable cable. Pain: published state of the art validated on now-discontinued
Novec 7500 (L14-022); connector hotspot research unsettled (L14-019–021) while MW hardware ships. Experiment
($100k): 3 m mockup at 1000–1500 A vs glycol baseline and published Novec data, both fluids, 500 bend
cycles. Vision: thermal backbone of electrified heavy transport. Uncertainty: demand evidence in this
batch's ledger is technical-literature-led — MCS fleet procurement (L10) must be confirmed in P4 before
advancing; retained for supply-shock timing and clean subsystem shape. Confidence: low.

---
Founder-fit: per mission rule 3, founder profile was read only after the 18 seeds above were frozen;
each seed's founder_fit_note in the JSON carries a one-sentence generic EE/CE capability-transfer note
(capped at 5/100, applied later, no reranking performed).
