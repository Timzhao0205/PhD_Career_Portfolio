# G05 — Photonics & Laser Systems Integration (No Fab)

## Landscape
Four sellable-product niches sit outside co-packaged-optics/silicon-photonics packaging, excluded
from this lane: (1) industrial laser materials-processing systems (cutting, welding, cleaning,
marking) where sources are bought and systems built; (2) free-space optical communication (FSO)
ground and airborne terminals, excluding the satellite bus itself; (3) laser wireless power beaming
(ground/drone receivers and transmitters); (4) precision beam-control electronics (fast steering
mirrors, pointing/tracking/stabilization) sold as standalone products. All four share one physics
core: pointing and delivering a narrow beam through a moving or turbulent channel. Materials
processing is largest and most mature — China holds 56% of global laser-equipment sales revenue
(2023) via Han's Laser, HG Tech, and Bond Laser, with IPG, Trumpf, and Coherent leading in the
West, and a laser-cleaning sub-market alone near $1B today. FSO and power beaming are newest,
still government-demo-driven, not catalog products: DARPA's POWER program set an 8.6km/800W
laser power-beaming record in May 2025, NASA is standardizing optical ground terminals to seed a
commercial market, and China's first operational satellite-ground laser-comm station opened
September 2024.

## Pains & buyers
Materials processing: job shops, EV-battery/e-motor makers, and aerospace/conservation buyers pay
per bundled cell, not per laser — IPG's Integrated Laser Welding System pairs a 12kW fiber laser
with scanning beam delivery, machine vision (±12mm auto-correction), and sub-5-microradian
weld-placement repeatability, because in-house beam-delivery integration, not the laser source, is
what buyers pay to avoid. FSO terminals: NASA states plainly that "each mission...has to start from
scratch to provide a ground terminal network" — buyers are space agencies, Space Force programs
(GA-ASI's LAC-12 pod on MQ-1/MQ-9), and telecom/backhaul operators BridgeComm is chasing, and the
core pain is bespoke, non-repeatable engineering. Power beaming: DoD (DARPA, AFCENT/CENTCOM, Naval
Research Lab) funds demonstrations to strip battery weight from long-endurance drones and remote
bases; commercial buyers (space-solar, terrestrial power-as-a-service) remain pre-revenue.
Beam-control electronics: defense primes, satellite-terminal makers, and the Navy itself (an open
SBIR solicitation for shipboard "advanced beam control and wave slap mitigation") all buy
custom-quoted, no-catalog-price hardware — every sale is its own bespoke cycle.

## Incumbents & gaps
- **Han's Laser / HG Tech / Bond Laser** (China): commodity cutting/welding volume leaders — Bond
  Laser alone has topped global fiber-laser-cutting sales five straight years (2019-2023) and is
  the only laser-focused firm in the global Top-25 machine-tool-producer ranking. Gap: little
  presence in ultra-precision or novel-process (inline-QA cleaning/micro-welding) niches.
- **IPG / Coherent / Trumpf / Laserax**: bundled cells, rarely public-priced; laser-cleaning list
  prices run ~$25K (handheld, 200W) to $150K+ (robotic, >1kW). Gap: robotic/automated cleaning is
  the fastest-growing segment yet handheld still holds ~51% of 2025 revenue — automation retrofit
  is wide open.
- **NASA LCOT + BridgeComm/X-Lumin** (FSO ground): LCOT is a COTS-based reference design (70cm
  telescope, high-peak-power VLMA amplifiers, shop-fabricable BOM) meant to seed a market, not a
  sold product; BridgeComm's G2S line (with X-Lumin since 2023) is the only named commercial
  entrant and still discloses no price two-plus years later. Gap: nobody sells a catalog-priced,
  standards-compliant (SDA/CCSDS) OGS today.
- **DARPA POWER / PowerLight / Teravec** (power beaming): the May-2025 record (800W, 8.6km, >20%
  efficiency) used off-the-shelf photovoltaic cells rather than costly wavelength-matched ones,
  proving a receiver can be commoditized; PowerLight's ~1kW-to-5,000ft drone demo remains a
  bespoke, program-specific build. Gap: no vendor sells a drop-in receiver module to multiple
  transmitter primes.
- **Cedrat Technologies** (beam control): the reference piezo FSM supplier across space, defense,
  scientific, and medical markets, with zero public pricing anywhere on its site. Gap, per
  trade-press comparisons: no single product spans galvo-class speed, micro-gimbal-class
  compactness, and piezo-class zero-power holding — SWaP-constrained platforms (small drones,
  cubesats) are underserved, and public market-sizing data for this niche remains thin and
  inconsistent.

## 2029 inflections
DARPA's POWER program is a three-phase effort that started in 2023 and wrapped phase one in
mid-2025; phases two-three (2026-2028) should hand transmitter/receiver specs to industry as a
2029/2030 founder launches. PowerLight/Kraus Hamdani's own roadmap moves from single-transmitter
demos toward "a distributed network" with more power, range, and simultaneous aircraft — a
multi-node, standardized-hardware phase likely lands 2027-2029. NASA's LCOT and Space Force
programs pushing low-SWaP, standards-interoperable terminals both explicitly aim to convert
bespoke-payload programs into a component supply chain by the late 2020s. In materials processing,
robotic/automated cells are already the fastest-growing laser-cleaning sub-segment off a small
base — a 2029 launch rides the handheld-to-automated crossover rather than leading it.

## China notes
China anchors the largest, most mature sub-lane (56% of global laser-equipment revenue, 2023) but
is earlier-stage in the other three. Its first operational satellite-ground laser-comm station
(AIRCAS, 500mm aperture, Pamir Plateau, online September 2024) is one site with an explicit
multi-site national network still being built through the decade. A domestic power-beaming demo
(Suzhou, 2023) reached 179W from 1kW input at 20m — kilowatt-class, but far short of DARPA's 2025
8.6km record — and China's own physics-journal literature still calls the field an early research
stage ("初级研究阶段"), confined largely to labs and aerospace. Beam-control/adaptive-optics
research is deep — CAS's Institute of Optics and Electronics has run a dedicated deformable-mirror
program since 1980, spanning fusion, astronomy, and biomedical uses — but it remains
institute-embedded, not a commercial supplier base the way Han's Laser dominates cutting. Net: a
China-network founder's edge is selling beam-control and FSO/power-beaming subsystems into China's
own build-out, not competing with Han's Laser or Bond Laser on cutting/welding volume.

## Opportunity seeds
1. **Standardized COTS optical ground station**, built on NASA LCOT's open reference design (70cm
   telescope, VLMA amplifier, shop-fabricable BOM). Sold as a catalog product to smallsat
   operators, telecom backhaul, and university/gov programs that today build one-off terminals.
   This is a free-space ground-terminal system, never a die-to-die or fiber-to-PIC packaging tool,
   avoiding **CL-09** (CPO optical assembly & test) entirely.
2. **Vendor-agnostic laser-power receiver module** (concentrator optics, wavelength-matched PV
   array, power electronics) sold to multiple power-beaming transmitter companies rather than
   built in-house by each one. This extends DARPA POWER's own finding that off-the-shelf PV cells
   already clear ~20% efficiency, undercutting program-specific one-off builds on cost. It is a
   power-conversion receiver, not a photonic alignment tool, avoiding **RID-100** (automated
   optical-assembly cell).
3. **Catalog-priced, SWaP-optimized FSM-plus-tracking controller card**, targeting the
   speed/compactness/zero-power-holding gap between galvo, micro-gimbal, and piezo designs that
   trade press documents. Aimed at drone-borne FSO/power-beaming terminals and the Navy's own
   shipboard "wave slap" beam-control need, sold catalog-priced, unlike Cedrat's bespoke-quote
   model. It is a free-space pointing/stabilization actuator, never a wafer-level optical
   metrology tool, avoiding **C25** (D2W overlay inspection).
4. **Motion-control-integrated automated laser-cleaning/micro-welding head**, reusing
   laser-aligned-coil-winder-class motion-control IP to sell a robotic-cell retrofit. Targets the
   fastest-growing but still-minority automated segment of a market today dominated by handheld
   tools and unpriced bundled OEM cells (IPG, Han's Laser). It stays entirely in
   materials-processing beam delivery, avoiding **SEM-06/SEM-07/IND-06** (fiber-attach FAU cell,
   detachable optical connector, fiber-to-PIC alignment).
5. **China-facing beam-control export product**, selling precision FSM drive electronics and
   closed-loop tracking controllers into China's own national ground-station build-out and
   power-beaming R&D. Both are still early-stage in China's own literature versus US field results,
   arbitraging founder China-network access into a segment where China is a buyer, not a dominant
   supplier. It is a free-space beam-steering product, not an in-package interconnect, avoiding
   **W-AYAR** (near-package optical interconnect).
