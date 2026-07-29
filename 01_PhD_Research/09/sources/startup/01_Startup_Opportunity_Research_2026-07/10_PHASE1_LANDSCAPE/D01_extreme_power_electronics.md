# D01 — Extreme Power Electronics & Conversion

## Landscape

Wide-bandgap (WBG) semiconductors (SiC, GaN) are pulling power conversion into a new performance
regime across five overlapping fronts: (1) AI data-center power, where NVIDIA's 800 VDC rack
architecture (full production tied to 2027 Kyber systems) replaces multi-stage AC/DC conversion
with fewer, denser stages and projects up to 5% end-to-end efficiency gain, 70% lower maintenance
cost, and 45% less copper versus legacy 415/48V chains [D01-01][D01-02]; (2) EV megawatt charging,
now standardized as IEC TS 63379 (MCS: up to 1,250 VDC, 3,000 A) [D01-03], with China's BYD (1,000V/
1,000A, ~1–1.3 MW, 4,000 planned "flash-charge" stations for passenger cars) and Huawei (up to
2,400A, 1.5 MW hubs, targeting heavy trucks) both shipping in 2025–2026 [D01-04]; (3) electric/
hybrid-electric aviation, where GE Aerospace (goals of 99% efficiency / 19 kW/kg for a 1 MW SiC
inverter, NASA-partnered) and ZeroAvia (>20 kW/kg demonstrated at 230 kW) are racing toward
FAA/EASA-certifiable megawatt-class power trains [D01-05][D01-06][D01-21]; (4) naval/defense MVDC
and pulsed power, where ONR funds SiC/GaN power-electronic building blocks (PEBBs) for shipboard
MVDC and weapon-grade pulsed loads [D01-07]; and (5) grid-facing solid-state transformers (SST),
now a hot, well-capitalized VC category — Heron Power ($140M Series B, Feb 2026), DG Matrix ($60M
Series A, Feb 2026), Amperesand ($80M Series A, Nov 2025), Hyperscale Power (€5M seed, Mar 2026) —
all raised within about 18 months [D01-08][D01-09][D01-10]. Underlying all fronts: SiC dominates
high-voltage/low-frequency power (EV traction, grid, aviation); GaN dominates high-frequency/
lower-voltage power (chargers, data-center bricks, radar/EW) [D01-01].

## Pain points & buyers

- **Data-center operators/hyperscalers** face medium-voltage transformer lead times stretching to
  3 years and a projected ~30% 2025 shortage as AI campus buildouts outpace grid-hardware supply
  [D01-11]. They will pay a premium for anything that shortens delivery or shrinks footprint per MW,
  which is why over $280M has flowed into single SST funding rounds in the last 18 months
  [D01-08][D01-09][D01-10].
- **Heavy-truck and bus fleet operators** need sub-30-minute megawatt charge cycles to match diesel
  duty cycles; CharIN/MCS (IEC TS 63379) and China's MIIT-driven national-standard effort (2025
  automotive standardization work plan tasked pre-research on a 1MW+ commercial-vehicle interface
  standard) show both US/EU and China regulators pushing hardware vendors to deliver [D01-13][D01-03].
- **Airframers and propulsion integrators** (GE Aerospace/NASA EPFD, ZeroAvia) are the buyers for
  megawatt-class, >19 kW/kg, >99%-efficiency inverters; they pay via long-cycle certification
  contracts, not commodity component pricing — GE's first full integrated ground test only closed
  in June 2026 after roughly a decade of component development, underscoring how slow this
  qualification cycle is [D01-21][D01-05].
- **Navy/DoD program offices** pay for SiC/GaN PEBBs and pulsed-power subsystems for MVDC ships and
  directed-energy weapons — e.g., Epirus's GaN-based Leonidas received an additional $250M in DoD
  funding in March 2025 for production scaling — prioritizing SWaP and reliability over unit cost
  [D01-14][D01-07].
- **Module and system reliability engineers** across every segment fight the same underlying
  problem: WBG dies switch faster and run hotter than silicon, producing heat fluxes and localized
  hot spots that are "extremely difficult to manage," which can trigger thermal runaway and force
  larger die areas that erode the very density/efficiency gains WBG is supposed to deliver
  [D01-15]. Pulsed-power capacitor systems separately face well-documented thermal, electromechanical,
  and partial-discharge aging mechanisms that limit service life under repeated high-energy
  discharge [D01-23]. Both are unmet packaging/materials pain points buyers will pay to fix, not yet
  solved by any standalone product.

## Incumbents & gaps

Device-level WBG supply is consolidating fast: Infineon bought GaN Systems for $830M (2023),
Renesas bought Transphorm for $339M (2024), and Renesas separately committed $2B to Wolfspeed for
10-year SiC wafer supply — horizontal device manufacturing is becoming a scale game dominated by
Infineon, Wolfspeed, onsemi, STMicro, Navitas, and Chinese entrants (below) [D01-12]. At the
system/module level, grid-scale SST is now crowded with well-funded startups (Heron Power, DG
Matrix, Amperesand, Hyperscale Power) all chasing the same data-center/grid customer with similar
SiC-based, high-frequency architectures [D01-08][D01-09][D01-10] — a hard space for a 2-5 person
team to differentiate in without a genuinely novel topology or a narrower beachhead (e.g., a
sub-segment SST incumbents are ignoring, such as marine/off-grid or mobile MW-class units).
Megawatt EV charging hardware is being built in-house by OEMs (BYD, Huawei) and by charging-network
majors (ABB, Alpitronic, Kempower) rather than sold as an open component market — DC fast-charger
hardware alone lists for $35K–$140K per port with total installed cost of $90K–$150K (150kW) to
$200K+ (350kW), dominated by grid/civil work, not the power electronics [D01-16]. Aviation
inverters remain the domain of propulsion primes (GE, Honeywell, ZeroAvia) working multi-year
certification programs — not an accessible market for a tiny team without an airframe/engine
partner. The clearest gaps: (a) packaging/thermal-interconnect IP that lets any WBG module run
hotter/longer without failure — a sellable component, not a full converter; (b) compact, ruggedized
MW-class power conversion for non-hyperscale niches (marine vessels, mining/off-road
electrification, mobile/backup MW power, directed-energy test benches) that incumbent SST/charging
vendors are not targeting; (c) ultra-high-power-density (>100 W/in³) building-block converters sold
as catalog products to system integrators who don't want to design their own power stage.

## 2029 inflections

8-inch SiC substrate transition is forecast to cut wafer costs 30–40% by 2028, pushing SiC toward
cost-per-amp parity with IGBTs for most sub-1700V applications around the 2028–2029 window — the
point at which SiC stops being a premium/niche choice in mid-power converters [D01-17]. NVIDIA's
800VDC data-center architecture reaches full-scale production with Kyber rack systems in 2027,
meaning the SST/rectifier supplier ecosystem will be largely locked in before 2029, so a new
entrant targeting that exact niche in 2029/2030 is very late [D01-02]. MCS truck charging (IEC TS
63379) is only now shipping first 1MW+ units in 2026 (Scania, BP Pulse, Iberdrola); by 2029 fleet
operators will be selecting second-generation hardware vendors, a more realistic entry window for a
differentiated MW-class converter or thermal/packaging subsystem [D01-03][D01-18]. GE's
NASA-partnered megawatt hybrid-electric engine program completed its first full integrated ground
test in June 2026, with flight tests "anticipated this decade" — plausibly positioning 2029/2030 as
when hybrid-electric aircraft power electronics start moving from prime-only R&D toward a broader
qualified-supplier base [D01-21]. SiC device supply constraints are expected to ease by 2029–2030 as
new fabs and yield improvements bring lead times down to 8–16 weeks, removing a current excuse
incumbents use to avoid serving small/niche customers [D01-17].

## China notes

China's electric-aviation power electronics trail international leaders on system-level metrics
even where device work is strong: a Chinese Academy of Engineering strategic-studies review reports
Chinese industrial-grade drive motors at ~4.88 kW/kg peak power density versus 5.8 kW/kg
flight-tested and 15.3 kW/kg experimental designs abroad, with domestic light electric aircraft
capped at 290 km/h and 300 km range versus 480 km/h and 800 km internationally; the review names
import-dependence on core motor/controller components and weak foundational research as the main
gaps [D01-22]. On SiC substrates China has built real scale: Tianyue Advanced (SICC) is one of a
handful of Chinese substrate makers (alongside 天科合达/TK, 三安光电/San'an, Hebei Tongguang) now
competing with Wolfspeed, Coherent, and ROHM, though market-share estimates vary sharply by research
firm — a discrepancy the sources do not reconcile [D01-17]; Tianyue Advanced separately demonstrated
the world's first 300mm (12-inch) SiC substrate at SEMICON Europa in Munich in November 2024
[D01-19]. This buildout traces to national policy: SiC/third-generation semiconductors were named a
strategic foundation material under the 14th Five-Year Plan, with province-level implementation
plans (Shanghai, Beijing, Hubei, Zhejiang) since 2020 [D01-20]. On megawatt charging, China is
moving faster than the US/EU on both OEM deployment (BYD/Huawei already shipping 1–1.5 MW systems
in 2025–2026, versus first US/EU 1MW pilots only starting in 2026) and standards (MIIT's 2025 work
plan explicitly tasked pre-research on a national 1MW+ commercial-vehicle charging standard)
[D01-04][D01-13]. Net: a China-market entry point for a bilingual founder is stronger in components
(SiC substrate supply chain, module reliability/packaging IP sold to Chinese OEMs) than in
head-to-head charger or SST hardware, where BYD/Huawei and state-linked standards bodies already
dominate.

## Opportunity seeds

1. **Ruggedized, catalog-sold power-electronics building blocks (PEBBs) for niche MW-class
   applications** (marine electrification, mining/off-road vehicles, mobile/backup MW power,
   directed-energy test infrastructure) that incumbent SST/charging vendors ignore because they are
   chasing the data-center/grid gold rush. Buyers are systems integrators and defense primes who
   would rather buy a qualified power stage than design one in-house. A 2-5 person team can win by
   offering a family of >100 W/in³ SiC-based building blocks with fast customization, not by
   out-competing $80–140M-funded SST startups on their own turf. China angle: sell into marine/
   off-road electrification supply chains where local SiC substrate access (Tianyue Advanced) gives
   a cost edge; US angle: sell into DoD/Navy PEBB procurement (ONR's own priority list) [D01-07][D01-08].

2. **High-temperature, high-reliability WBG module packaging IP sold as a licensable
   component/service, not a converter.** Every segment (aviation, EV charging, data center, naval)
   independently fights the same heat-flux and hot-spot problem that forces derating or larger die
   area, eroding WBG's density/efficiency advantage [D01-15]. Module makers (Wolfspeed, Infineon,
   onsemi) and system integrators building custom converters would pay for drop-in packaging/
   interconnect solutions that extend lifetime without a full redesign. A tiny team with deep
   device-fab and packaging experience can prototype and license this to multiple buyers rather than
   building one product line, sidestepping the capital intensity of full-converter competition.

3. **Compact, high-power-density MW-class inverter/converter units for hybrid-electric marine and
   off-highway vehicles**, a segment structurally similar to electric aviation (extreme kW/kg,
   >99% efficiency demand) but without a 5+ year FAA certification gate, making it reachable by a
   small team on a 2029/2030 timeline. Buyers are marine propulsion integrators and heavy-equipment
   OEMs electrifying fleets under emissions pressure. China's shipbuilding and inland-waterway
   electrification push plus the founder's China network is a plausible go-to-market wedge distinct
   from BYD/Huawei's passenger/truck-charging focus.

4. **Second-generation megawatt EV/truck charging power modules sold to charging-network
   integrators** (ABB, Alpitronic, Kempower, and new entrants) rather than to end customers, timed
   to the 2029 replacement cycle when the first wave of 2026-era MCS hardware needs higher-density,
   lower-cost successors [D01-03][D01-18]. A small team wins by beating incumbent module cost-per-kW
   once 8-inch SiC substrates approach cost parity (~2028) [D01-17], selling as a component supplier
   rather than standing up a competing charging network — avoiding the capital-heavy site-development
   business that dominates charger economics [D01-16].

5. **Compact pulsed-power / high-energy-density capacitor-discharge modules for directed-energy and
   industrial pulsed-load customers** (test benches, EW systems, pulsed lasers), building on GaN's
   demonstrated advantage in compact, magnetron-free power stages (as in Epirus's Leonidas) and on
   solving the thermal/electromechanical aging mechanisms that limit pulsed capacitor life
   [D01-14][D01-23]. Buyers are defense primes and national labs who already pay premium prices for
   SWaP-optimized pulsed power; a small team with device-level GaN/SiC expertise can supply
   qualified sub-systems into DoD's active funding pipeline (ONR, AFRL) without needing to build a
   full weapon system [D01-07][D01-14].

6. **China-facing SiC/GaN power-module reliability testing and qualification service** for Chinese
   EV, charging, and industrial OEMs racing to scale (BYD, Huawei, and second-tier SiC device
   makers) who need independent high-temperature/thermal-cycling qualification capacity as they
   scale substrate production [D01-19][D01-20]. This trades on the founder's fab/characterization
   background and native Chinese network; revenue is service-based initially but can convert into a
   packaging-IP product line (see seed 2) once specific failure modes are characterized across
   multiple customers.
