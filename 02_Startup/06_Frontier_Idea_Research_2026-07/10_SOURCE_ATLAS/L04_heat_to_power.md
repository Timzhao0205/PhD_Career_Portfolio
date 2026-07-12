# L04 — Advanced Generation and Heat-to-Power

Lane scope: sCO2 cycles, turbomachinery controls, thermophotovoltaics (TPV), high-temperature
energy conversion, and balance-of-plant (BOP) bottlenecks across nuclear/geothermal/industrial
waste-heat conversion hardware and thermal-energy-storage (TES) power blocks. This brief is built
only from the 55 records in `L04_raw_sources.json` (IDs `L04-001`...`L04-055`); it does not
propose startup ideas. All records are `accepted: false` pending the separate verifier pass —
figures below should be read as "as reported by the cited source," not as independently confirmed
mission facts.

## Frontier state

Supercritical CO2 (sCO2) Brayton-cycle power conversion has crossed from lab curiosity to
multi-country pilot/demo scale in the last 3-4 years, but nowhere has it reached unsubsidized
commercial-scale (>50 MW) closed-loop operation yet:

- **US**: DOE/NETL's STEP Demo pilot (GTI Energy, Southwest Research Institute, GE Vernova),
  $169M total cost, reached ~4 MW net power at 500C turbine inlet, 27,000 rpm, grid-synchronized
  in October 2024 (`L04-039`, `L04-038`, `L04-026`). Sandia's smaller test loop first delivered
  grid power (10 kW, 600F, ~50 min) in 2022 (`L04-027`). NET Power's Allam-cycle variant (direct
  sCO2 combustion with inherent carbon capture) is furthest along toward utility scale: a 300 MW
  plant at an Occidental-hosted Odessa, TX site, targeted online 2026-2028 (`L04-040`, `L04-041`).
- **China**: moved fastest on *waste-heat* (indirect-fired) sCO2, not direct-fired power plants.
  "Chaotan One" (超碳一号), a 2x15 MW (30 MW) sCO2 steel-sintering waste-heat unit built by the
  Nuclear Power Institute of China (CNNC), reached steady commercial operation in Guizhou in
  November-December 2025 (`L04-048`, `L04-051`) — arguably the world's first *commercial*
  (non-demonstration, revenue-generating) sCO2 power unit, ahead of both the US STEP Demo and
  NET Power's Allam plant. A second CNNC project pairing molten-salt storage with sCO2 generation
  is slated for Xinjiang construction in H1 2026, targeting 2028 completion (`L04-051`).
  Component-level R&D (PCHE recuperators at CAS-IET with Xi'an Jiaotong University and Tsinghua,
  `L04-029`) is advancing in parallel.
- **South Korea**: KAERI, with an industry/academic consortium (Jinsol Turbo Machinery, KAIST,
  POSTECH), reached a 100 kW sCO2 "break-even point" (output > input power) in 2024 (`L04-028`);
  Hanwha Power Systems sells a commercial sCO2 turbo-expander-generator product line and has an
  MOU with TC Energy for pipeline waste-heat recovery (`L04-047`, `L04-055`).
- **Thermophotovoltaics (TPV)**: the enabling breakthrough was the 2022 Nature paper reporting
  >40% TPV cell efficiency (`L04-001`), which every subsequent thermal-battery company (Antora,
  Fourth Power) cites as the technology unlock. A 2024 Joule paper pushed a different (lower
  emitter-temperature, air-bridge) design to a claimed 44% (`L04-002`). Selective-emitter and
  materials-stability research is an active sub-field (`L04-008`, `L04-009`, `L04-010`).
- **Adjacent conversion hardware**: ORC (organic Rankine cycle) is the incumbent, commercially
  mature technology for lower-grade waste heat and geothermal, dominated by Ormat (US, ~63% of
  installed ORC capacity) and Turboden (Italy, Mitsubishi Heavy Industries Group, ~13%) (`L04-046`
  context). Advanced/enhanced geothermal (EGS) is scaling fast on the back of data-center power
  demand (Fervo Energy, `L04-044`, `L04-050`).

## Bottlenecks

1. **Turbomachinery materials and seals at temperature/pressure extremes.** sCO2 cycles need
   turbine inlet temperatures of 500-715C+ at very high density/pressure; STEP Demo has only
   reached 500C so far against a 715C RCBC design target (`L04-026`, `L04-039`). Heat-exchanger
   (PCHE recuperator) thermal-cycling durability is an active, unresolved research area — CAS-IET's
   2025 work specifically targets "thermal inertia" and rapid-response tolerance (up to 22C/min)
   as a named open problem (`L04-029`).
2. **No sCO2-specific turbomachinery performance-test standard identified.** ASME's Performance
   Test Codes cover steam (PTC 6/6.2) and gas turbines (PTC 22) but no dedicated sCO2 PTC surfaced
   in this session's search (`L04-030`) — a possible standards/certification gap that raises
   transaction costs for buyers comparing competing sCO2 turbine vendors (absence-of-evidence
   caveat: a newer/unindexed code may exist).
3. **TPV emitter durability at >1,500-2,400C.** The record TPV efficiencies (`L04-001`, `L04-002`)
   require either very high emitter temperatures (thermal-cycling/material-stability risk) or
   accept lower efficiency at lower temperature; materials-screening papers (`L04-009`) are
   directly chasing this trade-off.
4. **Regulatory/licensing lag for non-LWR balance-of-plant.** NRC's Part 53 technology-inclusive
   licensing framework only became effective 2026-04-29 (`L04-031`) — meaning most of the
   BOP/power-conversion choices for advanced reactors (sCO2, sodium, molten-salt) were designed
   under licensing uncertainty until very recently.
5. **Single-source, unvalidated market-size claims.** The only quantified sCO2 addressable-market
   estimate found this session (~RMB 100B / ~$14B for Chinese steel-sintering retrofits) comes
   from one state-media article with no independent triangulation (`L04-051`) — a real evidence
   gap given the mission's market-arithmetic-plus-triangulation requirement.
6. **Thermal-battery/TPV cost claims are vendor-asserted, not third-party audited.** Fourth
   Power's "cheaper than natural gas" and "10x cheaper than lithium-ion" claims trace to company
   statements repeated by trade press (`L04-052`), not an independent techno-economic study.

## Named buyers and spending signals

- **Fervo Energy** committed to buy **1.75 GW of ORC turbines over three years from Turboden**
  (Mitsubishi Heavy Industries Group), announced April 2026, expanding an earlier 150 MW order for
  its Cape Station (Utah) project — one of the largest disclosed heat-to-power turbine procurement
  commitments found in this lane (`L04-044`).
- **Strathcona Resources** (Canadian oil & gas) contracted Turboden for a ~19 MW single-shaft ORC
  system at its Orion thermal-oil facility, Alberta, to offset ~80% of site grid-power use
  (`L04-046`).
- **Proman** (methanol producer) is running Malta Inc.'s Advanced Heat Pump in commercial
  deployment at its Pampa, Texas plant for 300-550C process heat (`L04-049`).
- **Google** signed what it calls the world's first corporate EGS agreement, buying carbon-free
  power from Fervo's Nevada project for its data centers since November 2023 (`L04-050`) — direct
  evidence that hyperscale data-center buyers are now a demand driver for advanced heat-to-power
  generation, not just utilities.
- **SCG Cleanergy** (Thailand cement) bought a 33 MWh Rondo Heat Battery, the first commercial
  heat battery at a cement plant (`L04-042`); an unnamed **California fuel-production facility**
  operates a 100 MWh Rondo battery (`L04-043`).
- **TC Energy** signed an MOU with Hanwha Power Systems for sCO2 waste-heat recovery at a gas
  pipeline compressor station (`L04-047`).
- **TerraPower's Natrium project** (Kemmerer, WY) awarded BOP-relevant contracts to BWXT Canada
  (intermediate heat exchanger) and Curtiss-Wright (reactor protection system) — official,
  named-vendor project awards (`L04-045`).
- **DOE/NETL put up to $80M** behind the STEP Demo sCO2 pilot (2016 award, `L04-038`) and ARPA-E
  funded Antora Energy's SCALEUP thermal-battery scale-up (`L04-033`) and Electrified Thermal
  Solutions' FIRES firebrick program (`L04-034`) — government is still a primary financier of
  first-of-a-kind heat-to-power hardware.
- **CNNC (China)** is both technology developer and demonstration-project sponsor for Chaotan
  One and the Xinjiang molten-salt+sCO2 project, the latter carrying an official "first (set of)
  major technical equipment" national designation (`L04-051`).

## Incumbent map (companies, products, price signals)

| Company | Geography | Product | Signal |
|---|---|---|---|
| NET Power | US | Allam-cycle direct-fired sCO2 (natural gas, inherent carbon capture) | 300 MW Odessa, TX plant; capex ~$900-1,200/kW industry estimate (`L04-040`); public company, SEC filer (`L04-041`) |
| GTI Energy / SwRI / GE Vernova | US | Indirect-fired sCO2 Brayton pilot (STEP Demo) | $169M, 10 MWe design, 4 MW achieved at 500C (`L04-039`) |
| Nuclear Power Institute of China (CNNC) | CN | Indirect sCO2 waste-heat units ("Chaotan One") | 30 MW commercial, steel-sintering (`L04-048`, `L04-051`) |
| KAERI / Jinsol Turbo Machinery / KAIST / POSTECH | KR | sCO2 compressor/turbine skid | 100 kW break-even demo (`L04-028`) |
| Hanwha Power Systems | KR | sCO2 Turbo Expander Generator (TEG) product line | Commercial product + TC Energy MOU (`L04-047`, `L04-055`) |
| Ormat Technologies | US | ORC turbines | ~63% of installed global ORC capacity (context, `L04-046`) |
| Turboden (Mitsubishi Heavy Industries) | IT/JP-owned | ORC turbines | ~13% global share; 1.75 GW Fervo order; 19 MW Strathcona order (`L04-044`, `L04-046`) |
| Fervo Energy | US | Enhanced geothermal (EGS) + ORC power blocks | 500 MW Cape Station; Google offtake (`L04-044`, `L04-050`) |
| Antora Energy | US | Carbon-block thermal battery + TPV/solid-state heat engine | ARPA-E SCALEUP award (`L04-033`); cites LaPotin TPV record (`L04-001`) |
| Fourth Power | US | Liquid-tin thermal battery + TPV | Vendor cost claims vs. natural gas/lithium-ion, unaudited (`L04-052`) |
| Electrified Thermal Solutions | US | Conductive firebrick ("E-brick") thermal battery | ARPA-E FIRES award (`L04-034`) |
| Malta Inc. | US | Pumped-heat / advanced heat pump | Commercial deployment at Proman, TX (`L04-049`) |
| TerraPower | US | Natrium sodium-fast-reactor + molten-salt storage | Named BOP vendor contracts (`L04-045`) |

## 2026-2031 triggers

- **2026-04-29**: NRC 10 CFR Part 53 technology-inclusive licensing framework takes effect,
  removing a major uncertainty for advanced-reactor BOP/power-conversion design choices (`L04-031`).
- **2026-2028**: NET Power's Odessa, TX 300 MW Allam-cycle plant targeted online — the first
  utility-scale sCO2 direct-fired power plant, a proof point (or failure point) for the whole
  category (`L04-040`).
- **H1 2026 - 2028**: CNNC's Xinjiang molten-salt + sCO2 demonstration construction start through
  completion, carrying a national "first-set" equipment designation that typically unlocks
  follow-on procurement in China (`L04-051`).
- **2026-2029 (3-year window)**: Fervo/Turboden's 1.75 GW turbine supply agreement executes,
  a concrete multi-year demand signal for ORC/EGS power-block hardware (`L04-044`).
- **Ongoing**: STEP Demo Phase 2 (scaling beyond the ~4 MW Phase 1 milestone toward its 10 MWe
  design point) is the next US technical checkpoint (`L04-039`).
- **Data-center-driven demand**: Google-Fervo-style 24/7 clean-power offtake agreements are a new,
  potentially large near-term buyer category for both EGS/ORC and (prospectively) sCO2/TPV
  balance-of-plant hardware, independent of traditional utility procurement cycles (`L04-050`).

## US vs Asia differences

- **Where each region is ahead**: The US leads on *direct-fired* sCO2 power generation (NET
  Power's Allam cycle) and on large-scale government-funded pilot infrastructure (STEP Demo);
  China appears ahead on *indirect/waste-heat* sCO2 commercialization speed — Chaotan One reached
  steady commercial operation before STEP Demo reached its full 10 MWe design point, and China has
  a named national industrial-equipment-designation pipeline (Xinjiang project) that provides a
  faster, state-directed path from demo to rollout (`L04-048`, `L04-051`, `L04-039`).
- **Component ecosystem**: South Korea (KAERI, Hanwha, KAIST, POSTECH) has built a smaller but
  tightly coupled national-lab + component-vendor + university consortium model that reached a
  power-generation break-even milestone with modest public disclosure of cost (`L04-028`); this
  contrasts with the US model of large, expensive, multi-party pilot plants ($169M for 10 MWe).
- **Standards and financing**: The US has an explicit new licensing pathway (Part 53) and an
  active company-filing/SEC disclosure regime (NET Power) giving outside investors auditable
  visibility; China's equivalent transparency is largely through state media rather than filed
  disclosures, making independent verification of Chinese cost/market claims harder (`L04-051`
  notes).
- **Geothermal/ORC**: The US (Fervo) and EU-headquartered-but-Japan-owned Turboden dominate the
  enhanced-geothermal/ORC deal flow found this session; no comparable large Asian EGS demand
  signal was found in this lane's search (a gap, not necessarily an absence in reality).
- **TPV**: TPV research and the thermal-battery commercialization push (Antora, Fourth Power) is
  currently a US-centric story in the sources collected; Japanese TPV research (JSME, `L04-020`)
  is decades-old academic/near-field work, and no current Japanese or Chinese TPV commercial
  product was identified this session.

## Unresolved contradictions

- **"World's first" claims collide.** US trade press implicitly treats STEP Demo/NET Power as the
  leading edge of sCO2 commercialization, while Chinese state media explicitly calls Chaotan One
  the "world's first commercial" sCO2 power unit (`L04-048`, `L04-051`). Both can be true
  simultaneously only if "commercial" (China, waste-heat retrofit) and "utility-scale direct-fired"
  (US, Allam cycle) are treated as different categories — the sources do not reconcile this
  explicitly.
- **Market-size credibility gap.** The only sCO2 market-size figure found (~RMB 100B China
  steel-sintering retrofit potential, `L04-051`) is a single-source estimate from state media with
  an obvious vendor-favorable framing (it accompanies a project-promotion article); it should not
  be treated as validated TAM without independent triangulation, which was not found this session.
- **TPV cost claims are pre-audit.** Fourth Power's public cost claims (competitive with natural
  gas, ~10x cheaper than lithium-ion, `L04-052`) have not been matched against an independent
  techno-economic analysis in the sources collected; Antora's ARPA-E-funded work (`L04-033`) is
  federally reviewed for technical merit but that is not the same as third-party cost validation.
  These are the same underlying TPV technology (`L04-001`) being commercialized by direct
  competitors with divergent claimed economics.
- **sCO2 standards gap vs. maturity claims.** Multiple sources describe sCO2 as approaching
  commercial readiness (`L04-003`, `L04-048`), yet no dedicated ASME (or other) sCO2 turbomachinery
  performance-test standard was located (`L04-030`) — a tension between "the technology is ready"
  narratives and the absence of the certification infrastructure that usually accompanies
  commercial-scale rollout.

## Opportunity-shaped pain statements

(Pain + who pays + evidence IDs. Not startup pitches — raw pain points for later idea-architect use.)

1. **Steel/cement sintering plants operating steam-based waste-heat-recovery units cannot capture
   the efficiency gains that sCO2 retrofits demonstrably deliver (up to ~50% more net power, >85%
   utilization gain) because sCO2 retrofit engineering/certification capacity is scarce outside a
   handful of state-backed Chinese demonstration teams.** Who pays: steel/cement plant operators
   with existing steam WHR infrastructure (potential retrofit market ~300 units in China alone per
   a single-source estimate). Evidence: `L04-048`, `L04-051`, `L04-011`.
2. **PCHE recuperators — the single most cited technical bottleneck across nearly every sCO2
   review paper collected — lack a standardized, rapid-thermal-cycling-tolerant, commercially
   sourceable design outside a few national-lab prototypes.** Who pays: sCO2 pilot-plant integrators
   (GTI, SwRI, CAS-IET) currently building bespoke recuperators in-house. Evidence: `L04-029`,
   `L04-004`, `L04-005`, `L04-006`.
3. **There is no dedicated ASME (or equivalent) acceptance-test standard for sCO2 turbomachinery,**
   forcing every buyer (utility, industrial waste-heat customer, national lab) to negotiate
   bespoke performance guarantees with each vendor. Who pays: any future sCO2 turbine buyer
   currently relying on ad hoc test protocols. Evidence: `L04-030`.
4. **TPV emitter materials degrade or are unproven at the >1,900-2,400C temperatures needed for
   record efficiency,** forcing thermal-battery makers to either accept lower round-trip efficiency
   (air-bridge, <1,500C designs) or unresolved durability risk (tandem, >2,000C designs). Who pays:
   Antora, Fourth Power, and their industrial thermal-battery customers bearing warranty/downtime
   risk. Evidence: `L04-001`, `L04-002`, `L04-009`.
5. **Advanced-reactor developers (TerraPower, and by extension SMR/microreactor vendors generally)
   must source novel, non-standard balance-of-plant components (intermediate heat exchangers,
   reactor protection systems) from a very small qualified-vendor pool,** as evidenced by
   TerraPower's contract awards going to a handful of named specialty suppliers. Who pays:
   TerraPower and, longer-term, utility/DOE customers of Natrium-class reactors. Evidence:
   `L04-045`, `L04-031`.
6. **Enhanced-geothermal developers are turbine-supply-constrained even with a 1.75 GW multi-year
   order in place,** implying a broader ORC/turbine manufacturing capacity bottleneck as EGS scales
   to meet data-center demand. Who pays: Fervo Energy and its data-center/utility offtake customers
   (Google). Evidence: `L04-044`, `L04-050`.
7. **Industrial process-heat buyers (methanol, cement, oil & gas thermal recovery) are already
   paying for first-of-a-kind thermal-storage/heat-pump/ORC hardware (Proman, SCG, Strathcona) but
   each deployment is a bespoke, single-site engineering project rather than a standardized,
   quickly repeatable product** — implying high integration cost per site. Who pays: Proman, SCG
   Cleanergy, Strathcona Resources. Evidence: `L04-049`, `L04-042`, `L04-046`.
8. **No independent, audited techno-economic validation exists for competing TPV/thermal-battery
   cost claims (Antora vs. Fourth Power vs. Electrified Thermal),** leaving industrial buyers unable
   to compare vendors on a trusted apples-to-apples basis. Who pays: prospective industrial thermal-
   battery buyers evaluating competing vendor claims. Evidence: `L04-052`, `L04-033`, `L04-034`.
9. **China's sCO2 demonstration pipeline depends on a small number of state-directed institutes
   (CNNC's Nuclear Power Institute, CAS-IET) with limited public technical disclosure,** making it
   hard for outside (including US/allied) technology developers or investors to benchmark against
   or license from the Chinese state of the art. Who pays: non-Chinese sCO2 developers seeking
   competitive intelligence or partnership. Evidence: `L04-048`, `L04-051`, `L04-029`.
10. **South Korea's KAERI-led sCO2 consortium reached a power break-even milestone but discloses
    no public cost or commercialization timeline,** leaving component vendors (Jinsol Turbo
    Machinery) and would-be licensees without a clear signal of when/if the technology will reach
    a procurable product stage. Who pays: Korean industrial waste-heat users awaiting a
    commercial-grade domestic sCO2 product. Evidence: `L04-028`, `L04-047`.
11. **NRC's Part 53 framework only became effective in April 2026, meaning nearly all advanced-
    reactor BOP/power-conversion engineering to date was designed under licensing uncertainty** —
    implying a backlog of designs that may need re-review or re-engineering now that the rule is
    final. Who pays: TerraPower, Kairos Power, X-energy, and other advanced-reactor developers with
    designs frozen under the old framework. Evidence: `L04-031`, `L04-045`.
12. **Waste-heat-to-power market-size claims (both the ~$14B China steel-sintering figure and the
    broader $23-75B global "waste heat to power" consultancy forecasts referenced across trade
    sources) vary by 3x+ across sources and lack bottom-up, independently triangulated arithmetic,**
    making it difficult for a new entrant to size a credible go-to-market wedge with confidence.
    Who pays: any founder or investor trying to size this market today. Evidence: `L04-051`,
    `L04-035`.

## Notes on evidence quality (honesty flags)

- Of the 55 records collected, `fetched: true` was achieved for 20 records (direct primary
  verification); the remaining 35 rely on WebSearch-synthesized snippets because either the page
  blocked automated fetch (SEC EDGAR, several ScienceDirect/MDPI/ARPA-E/NRC/federal register pages
  returned HTTP 403 or timed out) or a deliberate scope trade-off was made to prioritize breadth
  within the 45-55 record target. Every such record is marked `fetched: false` honestly rather than
  inferring success from search-result quality, per mission rule 7.
- Two academic-adjacent candidates found during search (an academia.edu-hosted Indian sCO2 paper of
  uncertain final venue, and a Hanspub-hosted Chinese sCO2 paper from a publisher with a
  known-predatory reputation) were deliberately excluded from the final 55 rather than padded in,
  to keep the academic quota honest; they remain available as discovery leads if a future wave
  needs them.
- The single Chinese market-size estimate (`L04-051`) and the vendor cost claims for Fourth Power
  (`L04-052`) are explicitly flagged above as untriangulated/unaudited — these should not be
  treated as accepted facts by downstream idea-architect or scoring agents without further work.

## T1 top-up addendum (2026-07-12)

15 new records (`L04-101`...`L04-115`, in `L04_t1topup_raw_sources.json`) were collected in a
T1-only top-up wave; every record is tiered T1 and none duplicates a DOI, canonical key, or title
already in the 55-record base ledger. Mix: 11 peer-reviewed primary technical papers, 1 standard,
1 national-lab technical report, 1 government financing record, 1 primary company press release.
Sub-niches newly covered:

1. **Turbomachinery component hardware, not just system-level reviews.** A novel elastohydrodynamic
   seal for sCO2 turbomachinery (`L04-101`), three new centrifugal-compressor experimental papers at
   100 kW/150 kW/MWe scale from three different national programs — China's Shanghai Marine Diesel
   Engine Institute (`L04-102`), South Korea's KIER (`L04-103`), and CAS-IET (`L04-106`) — and a
   turbine rotor-cooling CFD study, also CAS-IET (`L04-109`).
2. **Component-level Brayton-cycle controls.** A Tianjin University valve-by-valve dynamic-performance
   comparison (`L04-111`), complementing but distinct from the existing system-level dynamics
   (`L04-007`) and control-strategy review (`L04-022`) records.
3. **PCHE structural durability.** An India-based (Kumaraguru College of Technology) thermostructural
   analysis of airfoil-fin PCHE design (`L04-105`) — the lane's first India-geography sCO2-hardware
   primary paper.
4. **Allam-cycle-adjacent oxy-fuel combustion NOx behavior**, from Huazhong University of Science and
   Technology (`L04-104`), partially filling a gap this lane's own brief had flagged as under-studied.
5. **TPV beyond the grid-scale thermal-battery story**: a radioisotope-TPV (RTPV) space-power design
   paper from MIT (`L04-107`) and an NREL near-field, low-temperature (460C) large-area TPV device
   (`L04-110`) — both materially different technical approaches from the high-temperature
   tandem/air-bridge cells already in the base ledger.
6. **Thermal-battery balance-of-plant hardware**: an MIT (Asegun Henry group) paper on high-temperature
   molten-silicon pumping for grid-scale thermal storage (`L04-108`), the mechanical enabling
   component underlying silicon-based TPV thermal batteries.
7. **Materials/standards infrastructure**: a Sandia National Laboratories 2016 technical report on five
   named sCO2 materials challenges — alloys, turbine degradation, gas-foil bearings, corrosion
   (`L04-113`) — and the current ASTM E139-24 creep/stress-rupture test-method standard (`L04-112`)
   relevant to qualifying high-temperature alloys for this hardware.
8. **Financing-side demand signals**: DOE's $1.76B loan-guarantee conditional commitment for the
   Willow Rock A-CAES long-duration storage project (`L04-114`), and Fervo Energy's $421M non-recourse
   project-debt close for Cape Station (`L04-115`), which pairs with the existing 1.75 GW
   Fervo-Turboden turbine order (`L04-044`) to show the turbine procurement is now debt-financed.

One lead — a still-open Sandia SAM.gov industry solicitation seeking sCO2 Brayton-cycle bearing
vendors — was found and corroborated via WebSearch but could not be directly fetched (SAM.gov
serves a JavaScript-rendered shell to automated fetches) and was deliberately left out of the
15-record file rather than included as an unfetchable, likely-rejected entry; it is noted in
`L04-113`'s notes field as context for a future scout with browser-level access.
