# D04 — Applied Superconductivity Systems

## Landscape

Applied superconductivity is bifurcating into two demand waves: (1) a fusion-driven HTS tape boom
pulling REBCO conductor demand up ~10x since 2020 and forecast to grow another 10x in five years
[D04-08][D04-11]; and (2) slower but real non-fusion product markets — compact MRI, induction
heating, SMES, aviation motors, maglev, semiconductor/PV crystal-growth magnets — where turnkey
systems, not raw wire, are the product. "HTS magnet market" TAM figures from report mills disagree
wildly ($47M→$195M by 2032 in one [D04-07] vs. $1.23B in 2024 in another) — neither is verified, so
treat top-line TAM as directional only. What is verifiable: AMSC, the largest pure-play public
HTS/grid company, grew revenue 34% YoY to $299.2M in FY2025, Grid segment $251.3M, backlog up ~40%
to ~$280M [D04-14]; Tokamak Energy's spinoff TE Magnetics targets £300M ($394M) annual revenue by
decade-end from non-fusion HTS magnet sales [D04-15]; China's 联创光电/联创超导 booked roughly RMB 5B
in fusion-linked orders and is scaling HTS magnetic-Czochralski crystal-growth furnace production
from 100 to a planned 1,600 units/year by 2027 [D04-09][D04-13]. Cryocooler capacity and REBCO tape
supply, not magnet design, are the binding constraints across nearly every sub-market [D04-11][D04-24].

## Pain points & buyers

Fusion developers (CFS, Tokamak Energy, Chinese state programs) buy magnet subsystems at
national-lab prices; magnets run 28–40% of total reactor construction cost per China's CRAFT/BEST
accounting [D04-09]. Hospitals/imaging OEMs want compact, cryogen-free MRI magnets for
point-of-care imaging: Magnetica's 3T system weighs <450 kg vs. >5,000 kg conventional, but is
still pre-regulatory-approval [D04-04]; a NZ/Minnesota consortium has a sub-400mm, ~14 km-conductor
1.5T brain magnet prototype on a single Cryomech cooler [D04-06]. Metalworking buyers (aluminum/
copper extrusion, forging) pay for HTS induction heaters because resistive induction heating of
non-ferrous billets is only ~50% efficient; Zenergy Power's early commercial HTS heater at a German
extruder delivered ~25% productivity gains [D04-10]. Utilities pay for fault current limiters and
SMES to manage fault currents and power-quality events as distributed generation grows [D04-16];
SMES sells on sub-100ms response and >95% efficiency with near-unlimited cycle life vs. batteries
[D04-19]. Aerospace buyers want extreme power density: Hinetics' prototype HTS aircraft motor
demonstrates 10 kW/kg with a 40 kW/kg design target, beating anything commercial today [D04-01].
Fab/PV buyers pay for HTS magnetic-Czochralski systems because superconducting fields suppress
silicon-melt convection better than resistive electromagnets, improving crystal/wafer yield
[D04-13].

## Incumbents & gaps

MRI/NMR magnets: Magnetica, Scientific Magnetics, SuperConducting Systems, Tesla Engineering,
Bruker, Oxford Instruments dominate; benchtop NMR systems run $30K–$150K new, but ultra-compact
point-of-care HTS systems remain pre-commercial [D04-04]. Induction heating: only two named
commercial HTS heater vendors found (Zenergy Power, Japan's Supercoil Co., 300 kW-class,
commercialized 2017) — essentially no visible new entrant since [D04-10]. SMES: legacy
demonstration-scale players and DOE-funded pilots; "broad market use is considered long-term" per
one vendor's own positioning — stalled on cost/integration, not physics [D04-12]. Quench
protection and winding: almost entirely custom in-house engineering at magnet builders — no named
third-party turnkey quench-protection or automated NI-winding equipment vendor surfaced, directly
matching the founder's undergrad winding-machine experience. Fault current limiters: Nexans and
AMSC are named incumbents, but transmission-class SFCLs have been "5 years from commercial-ready"
for over a decade — a chronically stalled category [D04-16]. HTS aviation motors: Hinetics
(US, ARPA-E-backed) and Strathclyde's ASL lab lead; both pre-production, leaving cryocooler-rotor
packaging and quench-safe flight operation wide open [D04-01][D04-02].

## 2029 inflections

REBCO tape street prices sit near $15–30/m (~$150–300/kA-m), with an industry roadmap targeting
$50/kA-m near-term and $10–20/kA-m longer-term for non-fusion cost-competitiveness [D04-11]. If
tape cost roughly halves by 2029 (plausible given 10x demand-driven scale-up underway), induction
heating, SMES, and compact MRI cross into commercial viability windows that don't exist today.
Fusion megaprojects are absorbing most near-term tape supply, driving capacity investment (Faraday
Factory Japan, Fujikura, Yangtze River Delta producers) [D04-08][D04-11] and creating a
supply-security angle for anyone sourcing/making tape or joints domestically as China scales its
own chain (100%-domestic 582-ton TF magnet delivered June 2026) [D04-09]. Cryocooler supply-chain
tightening from export restrictions and tariffs is a second inflection, favoring
lower-cryocooler-count designs like the single-pulse-tube 1.5T MRI magnet [D04-24][D04-06].
Hydrogen-electric aviation electrification timelines put HTS motor integration on roughly the same
2029–2032 horizon certification programs need lead time for now [D04-01][D04-02].

## China notes

China is executing an explicit, funded HTS industrial policy: the 十五五 (2026–2030) plan and its
新材料产业发展规划 name superconducting materials a frontier-material priority, with specific
language on MRI (磁共振) and low-temperature superconductor applications, and push HTS wire/cable/
magnet industrialization [D04-08]. Concrete proof points: a 1.2 km HTS cable demo in Shanghai, a
10 kV three-phase HTS cable in Shenzhen, and the world's first grid-connected superconducting
substation [D04-08]. 联创光电/联创超导's HTS magnetic-Czochralski furnace business has real
disclosed orders (宁夏旭樱 RMB 95M, then RMB 478M add-on in 2023) against a stated 2025 addressable
pool of ~RMB 77B for new-generation crystal-growth furnaces in China's PV/semiconductor sector
[D04-13]. China's HTS maglev program (Southwest Jiaotong University, Chengdu) has run a 620 km/h
prototype since 2021, targeting 800 km/h, using liquid-nitrogen HTS instead of liquid-helium,
cutting cooling cost roughly 50x versus Japan's low-Tc approach [D04-18]. Eight named A-share
suppliers (西部超导, 永鼎股份, 国机重装, 广大特材, 上海电气, 冰轮环境, 宝胜股份, 联创光电) sit across
the domestic fusion-magnet chain with billion-RMB order books — China is building a parallel,
vertically integrated HTS supply base, not importing [D04-09].

## Opportunity seeds

1. **Turnkey cryocooler-integrated compact HTS magnet modules for OEM instrument builders.** Small
   NMR, metrology, and point-of-care imaging OEMs need a reliable, quench-safe magnet subsystem but
   lack in-house magnet engineering; incumbents (HTS-110, Magnetica) sell fully custom systems or
   whole instruments, not a modular component. Field homogeneity, ramp time, and cooldown are hard
   engineering problems where a winding/joint/quench specialist team out-executes generalist OEMs.
   A 2–5 person team can qualify one bore-size/field-class platform without a full MRI regulatory
   pathway. US OEMs need domestic supply as China scales HTS; a China-fluent founder could also sell
   into Chinese instrument makers who currently import magnets.

2. **Automated NI/MI winding-and-joint equipment for HTS magnet manufacturers.** Every named magnet
   builder (CFS, TE Magnetics, 联创超导, HTS-110, national labs) winds and joins coils by custom,
   semi-manual processes; no third-party turnkey equipment vendor surfaced. Buyers are magnet
   manufacturers who pay capital-equipment prices, not magnet prices — a direct extension of the
   founder's own laser-aligned automated NI-winding machine, a rare demonstrated capability. A tiny
   team sells one machine at a time into a fragmented, fast-growing buyer base (10x tape demand
   growth) without building magnets or carrying end-market risk, into both US fusion/aerospace shops
   and China's 联创超导-style furnace producers.

3. **HTS induction heating systems for mid-size metals fab shops.** Non-ferrous induction heating
   is stuck at ~50% efficiency, and the only two named commercial HTS heater vendors (Zenergy Power,
   Supercoil) show no visible new products in years — a stalled but proven category. Buyers are
   extrusion/forging shops who already pay six-to-seven figures for conventional heaters and can see
   25%+ throughput gains, a clean ROI. A small team can target one billet-size class as a beachhead,
   cryocooler-integrated to avoid liquid-nitrogen logistics, selling into both US reshoring-driven
   fabrication and China's large extrusion industry.

4. **Cryocooler-integrated SMES units for data-center power-quality ride-through.** SMES's
   sub-100ms response and near-unlimited cycle life are real advantages over batteries, but the
   category is stuck selling one-off demonstration systems; DOE-funded pilots target 100MW+ fossil
   assets, leaving smaller buyers unaddressed. AI-load data-center operators facing transient
   power-quality problems are a plausible near-term buyer willing to pay for guaranteed sub-cycle
   ride-through. A small team can productize a modest sub-MJ standardized unit rather than chase
   utility-scale contracts, selling into US data-center buildouts and China's grid-modernization push.

5. **HTS magnetic-Czochralski retrofit magnets for crystal growers outside China.** 联创光电/联创超导
   proved this product category is real and well-paid (RMB billions in orders, capacity to 1,600
   units/year by 2027) but is a China-domestic supplier; Western PV and wafer producers rely on
   resistive electromagnet MCZ systems or lack an HTS-magnet supplier entirely. A US-based team with
   credible magnet-engineering pedigree could sell a retrofit HTS module to Western furnace makers
   seeking the same yield gains, positioned against China-sourced equipment as export controls
   tighten — a proven willingness-to-pay transplanted to an underserved market.

6. **Cryocooler-count-minimized cryostat/rotor-cooling subassemblies for HTS integrators.**
   Cryocooler supply-chain tightening is a binding constraint across MRI, motor, and SMES products
   alike; the named ultra-compact MRI prototype hits its size via single-cryocooler operation
   [D04-06], and Hinetics' motor centers on a rotor-integrated Stirling cooler [D04-01]. A small
   hardware team strong in cryogenic packaging and power electronics could license a
   cryostat/rotor-cooling subassembly (not a full magnet) to multiple downstream integrators (MRI
   OEMs, motor builders, SMES vendors) who all face the same cooling-count problem, turning a shared
   supply-chain pain point into a multi-segment component business.
