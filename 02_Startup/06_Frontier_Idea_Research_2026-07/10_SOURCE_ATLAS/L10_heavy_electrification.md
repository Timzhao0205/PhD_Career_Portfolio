# L10 -- Maritime, mining, rail, and off-highway electrification

Lane scope: ship electric propulsion and shore power, battery/hybrid vessels, mining truck and
underground equipment electrification, battery-electric locomotives and catenary alternatives, port
equipment, agriculture/construction machinery electrification, and megawatt charging. This brief
cites records in `10_SOURCE_ATLAS/L10_raw_sources.json` by ID (L10-001 ... L10-055); all records are
`accepted:false` pending the source-verifier pass, and academic `peer_review_status` is `unverified`
pending independent confirmation. No startup ideas are proposed here per the lane-scout mandate.

## Frontier state

Four parallel electrification fronts define this lane, at very different maturity levels. **Open-pit
mining haul trucks** are the most commercially advanced: Fortescue has live orders for up to 300-400
zero-emission 240t trucks split between Liebherr (T264 BEV, 3.2 MWh battery) and China's XCMG
(L10-028, L10-029, L10-052), and Fortescue commissioned its own in-house 6 MW charger in May 2026
(L10-029); BHP, Rio Tinto, and Caterpillar are jointly trialing Cat 793 XE "Early Learner" trucks
integrated with existing autonomous fleet management at Jimblebar (L10-030); and Rio Tinto has
separately launched a Chinese-technology (SPIC) battery-swap truck trial at Oyu Tolgoi in Mongolia
(L10-031). Academic literature on mining-truck sizing, trolley-assist configurations, and swap
scheduling is active and primary (not just review), 2023-2026 (L10-001, L10-002, L10-003, L10-013,
L10-015, L10-017, L10-018). **Battery-electric rail** is in a multi-railroad pilot/early-deployment
stage: Wabtec's FLXdrive has been ordered by Union Pacific (10 units, 2022, L10-032), Vale (3 units
for the Carajas Railroad, 2023, L10-033), BHP, Rio Tinto, Roy Hill, and CN, with a second-generation
7.0 MWh Heavy-Haul variant now in the product line (L10-051); primary academic work models specific
US freight corridors and finds meaningful but geography-dependent energy/emissions benefits
(L10-010, L10-011, L10-012). **Maritime electrification** is bifurcated: short-sea/inland battery and
hybrid vessels are commercially normal (Norway operates ~70 battery-electric ferries and continues
ordering more, L10-039; China has multiple in-service battery-swap cargo and passenger vessels,
L10-040, and CATL is explicitly targeting transoceanic electric vessels within three years per
trade-press reporting), while shore power (cold ironing) remains capital-intensive, standards-heavy,
and reliant on 2030/2035 regulatory deadlines rather than pure economics to justify investment
(L10-007, L10-008, L10-009, L10-043). **Port equipment, agricultural, and construction-machinery
electrification** are earlier and more fragmented: RTG crane electrification is a live global
procurement category (YILPORT/Konecranes 53-crane order, L10-041) but agricultural/construction
electric-machinery literature is dominated by forward-looking reviews rather than settled
deployment (L10-019, L10-020), and Hitachi/ABB's Japan-originated full-battery mining dump truck
only reached its first African mine-site deployment (Zambia) in 2024 (L10-054). **Megawatt charging
(MCS)** is the common enabling-infrastructure thread across all four fronts: IEC TS 63379 was
published in February 2026 (L10-050), and NREL is building a 20 MW-capable Megawatt Charging Emulator
research facility (L10-049) -- foundational standards and national-lab infrastructure exist, but this
session found no independently fetched, methodologically transparent bottom-up TAM estimate for MCS
deployment across mining, rail, port, and marine applications, only conflicting unfetched consultancy
estimates that were excluded from the ledger as insufficiently load-bearing (see Uncertainty note).

## Bottlenecks

- **Underground-mine battery-electric LHDs cannot complete a full shift without mid-shift
  intervention using current battery technology alone.** Trolley-assisted charging (overhead
  catenary + static connection) is an active 2025-2026 research response, not a settled commercial
  standard, claiming up to 75% energy-cost reduction vs. diesel in simulation (L10-014, L10-024).
- **Open-pit battery-electric haul truck fleets require either megawatt-class static charging,
  trolley-assist overhead infrastructure, or battery-swap stations -- and no single approach has
  won.** Fortescue is pursuing in-house 6 MW static chargers (L10-029) and trolley-assist-compatible
  trucks simultaneously (L10-052); Rio Tinto is separately trialing Chinese battery-swap technology
  (L10-031) at a different site. Academic literature still actively compares battery-only,
  stationary-trolley, and dynamic-trolley configurations without a converged answer (L10-002).
- **Shore power (cold ironing) economics remain marginal without regulatory compulsion.** Multiple
  2023-2025 reviews and techno-economic studies frame cold ironing as reliant on hybrid
  renewable/storage systems to pencil out environmentally and financially (L10-007, L10-008), and
  the EU's FuelEU Maritime OPS mandate does not bind major EU ports until 2030 (all ports 2035,
  L10-043) -- meaning the compliance clock, not unit economics, is the primary demand driver today.
- **US drayage/off-road zero-emission mandates are being actively reversed, not tightened.** CARB
  announced it will formally repeal the Advanced Clean Fleets' High Priority Fleet and Drayage Fleet
  provisions (final action by 31 Aug 2026) following a legal settlement (L10-044) -- a live regulatory
  reversal that directly undercuts a previously assumed 2035 all-zero-emission-drayage deadline.
- **IMO's global net-zero shipping framework has itself slipped.** MEPC 83 approved the Net-Zero
  Framework in April 2025 (L10-042), but the October 2025 adoption session was adjourned by majority
  vote to October 2026, pushing possible entry into force to 1 March 2028 at the earliest --
  directly delaying the global pricing/GHG-intensity trigger that would most strongly incentivize
  shipboard battery/hybrid retrofits and shore power.
- **Vendor pricing for nearly all heavy-electrification hardware in this lane is undisclosed.**
  Wabtec's FLXdrive (L10-051), Liebherr's T264 BE (L10-052), and Caterpillar's R1700 XE (L10-053)
  product pages all omit price; multiple named contract announcements (Fortescue-XCMG, L10-028;
  Fortescue-Liebherr, L10-029; BHP/Rio Tinto/Cat trial, L10-030) also omit dollar values --
  consistent with the pricing-opacity pattern documented in the L02/L08 lanes for adjacent
  power-electronics and HVDC hardware.
- **Megawatt-charging market-size estimates disagree by more than 10x across research vendors.**
  Five consultancy forecasts found in a single WebSearch this session ranged from ~$150M (2025) to
  ~$3.68B (2026) for ostensibly the same MCS market; none was independently fetched or judged
  sufficiently load-bearing to enter this ledger (see Uncertainty note), so no record number is
  cited here -- the category is too new and inconsistently defined for confident TAM arithmetic
  today, and any single-source MCS TAM claim encountered downstream should be treated with caution.

## Named buyers and spending signals

- **Fortescue (Australia)** ordered up to 400 zero-emission 240t haul trucks split between Liebherr
  (T264 BEV) and XCMG (China), targeting fossil-fuel elimination from land operations by 2030;
  commissioned its first in-house 6 MW fast charger in the Pilbara in May 2026 (L10-028, L10-029).
- **BHP, Rio Tinto, and Caterpillar** are jointly trialing two Cat 793 XE "Early Learner"
  battery-electric haul trucks at BHP's fully autonomous Jimblebar mine, explicitly testing
  integration with existing autonomous fleet-management systems (L10-030).
- **Rio Tinto and China's State Power Investment Corporation (SPIC) Qiyuan** deployed an 8-truck,
  91-tonne battery-swap fleet (13 x 800kWh batteries, sub-7-minute swaps) at the Oyu Tolgoi copper
  mine in Mongolia, announced 27 October 2025, testing through end-2026 (L10-031).
- **Union Pacific** ordered 10 Wabtec FLXdrive locomotives (2022, its largest battery-technology
  investment to date, L10-032); **Vale** ordered 3 FLXdrive units for the Carajas Railroad, Brazil's
  largest iron-ore train (2023, L10-033), with Wabtec estimating ~25M litres of diesel saved
  annually.
- **China Gold Group** (Inner Mongolia) tendered a 2026-2028 open-pit equipment lease requiring a
  minimum 60-truck fleet (40x70t + 15x60t) plus 9 excavators -- a conventional-equipment baseline
  tender showing the fleet scale against which electrification alternatives compete (L10-034).
- **Baogang Steel Union** (Inner Mongolia, Barun open-pit mine) tendered a phase-two 5G +
  remote-intelligent-control retrofit for dozers/rollers (~RMB3.75M of ~RMB18.06M total project
  investment, bids due 29 July 2026) -- an adjacent autonomy/remote-control investment at the same
  class of buyer that is separately piloting battery-electric equipment (L10-035).
- **YILPORT Holding** (Turkey-headquartered terminal operator) ordered 53 Konecranes E-Hybrid RTG
  cranes across terminals in Portugal, El Salvador, and Ghana, recorded Q2 2026 (L10-041).
- **Maersk and CATL** signed an MOU (October 2025) to electrify port yard tractors, reach stackers,
  and cranes, building on a June 2025 CATL-APM Terminals agreement (L10-036).
- **Fjord1**, under a Norwegian Public Roads Administration development contract, ordered 4
  battery-electric autonomous-capable RoRo ferries from Turkey's Tersan Shipyard for the
  Lavik-Oppedal route (L10-039).
- **China Communications and Transportation Association** named the CATL-powered Jining "6006"
  pure-electric cargo ship (Beijing-Hangzhou Grand Canal, 15-min battery swap) a 2025 national
  transportation-innovation benchmark (L10-040).
- **EPA's Clean Ports Program** awarded 53 grants totaling nearly $3B (IRA-funded) across 26 US
  states/territories for zero-emission port equipment and infrastructure (L10-048).

## Incumbent map (companies, products, price signals)

| Company | Geography | Product / signal | Evidence |
|---|---|---|---|
| Caterpillar | US | Cat 793 XE battery-electric haul truck (BHP/Rio Tinto trial); R1700 XE underground BE LHD (<20min charge w/ 2x MEC500 chargers); record $63bn backlog (Q1 2026) | L10-030, L10-038, L10-053 |
| Liebherr | DE/CH | T264 Battery Electric haul truck, 240t/3.2MWh, Trolley Assist + "Power Rail" dynamic charging compatible, claimed 86% energy-cost/tonne reduction | L10-029, L10-052 |
| XCMG | CN | XDE240 BEV 240t haul truck (Fortescue order, phased 2028-2030); also supplies battery wheel loaders/dozers to Fortescue | L10-028 |
| Wabtec | US | FLXdrive battery-electric locomotive family (Shunter 1.2MWh to Heavy-Haul 7.0MWh); orders from UP, Vale, BHP, Rio Tinto, Roy Hill, CN | L10-032, L10-033, L10-051 |
| CATL | CN | Marine battery systems (Jining 6006 cargo ship, Yujian 77 passenger vessel); Maersk/APM Terminals port-electrification MOU; battery-swap mining truck technology (via SPIC) at Oyu Tolgoi | L10-031, L10-036, L10-040 |
| Hitachi Construction Machinery / ABB | JP / CH | World's first ultra-large full-battery haul truck (hybrid battery+trolley+regen), deployed to Kansanshi mine, Zambia (2024); joint electrification team with Komatsu | L10-054 |
| Konecranes | FI | E-Hybrid RTG cranes and electric empty container handlers; 53-crane YILPORT order (Portugal/El Salvador/Ghana) | L10-041 |
| Fortescue / Fortescue Zero | AU | In-house 6MW mining-truck fast charger; integrator of Liebherr/XCMG battery-electric trucks | L10-028, L10-029 |
| CharIN e.V. / IEC | DE (assoc. HQ) | Megawatt Charging System (MCS), IEC TS 63379 (Feb 2026), up to 3.75MW / 1,250V / 3,000A | L10-050 |
| NREL | US | National-lab megawatt-charging emulator research program (targeting 20MW site capability) | L10-049 |

No independent, load-bearing vendor list price was captured for any battery-electric haul truck,
locomotive, or underground LHD product in this lane this session (L10-051, L10-052, L10-053 all
confirm this gap explicitly) -- consistent with the pricing-opacity pattern documented in the L02
(power electronics) and L08 (DC grids/HVDC) lane briefs.

## 2026-2031 triggers

- **2026 (now):** CharIN/IEC published IEC TS 63379 MCS standard (Feb 2026, L10-050); CARB required
  to finalize repeal of Advanced Clean Fleets drayage/high-priority provisions by 31 Aug 2026
  (L10-044); China Gold Group open-pit equipment tender bids due 27 Feb 2026 (L10-034); Baogang
  Barun 5G retrofit tender bids due 29 July 2026 (L10-035); YILPORT's 53-crane Konecranes order
  recorded Q2 2026 with 2-year phased delivery (L10-041); Fortescue targeting first operational
  240t electric haul truck in the Pilbara before end-2026 (L10-029); IMO's adjourned Net-Zero
  Framework adoption session reconvenes October 2026 (L10-042).
- **2027:** KEPCO-style/other regional megawatt-charging build-outs expected to scale (cross-lane
  reference to L08's Korea HVDC localization target); Fjord1's autonomous-capable Norway ferries
  begin autocrossing/autodocking trials (L10-039, targeted from 2027).
- **2028:** Fjord1 ferries targeted for full autonomous navigation (L10-039); IMO Net-Zero Framework
  entry into force possible "at the earliest" 1 March 2028 if the October 2026 session adopts it
  (L10-042, cross-referenced).
- **2028-2030:** Fortescue-XCMG phased 240t truck deliveries (L10-028); Vale/Wabtec FLXdrive
  deliveries from Wabtec's Contagem, Brazil plant (L10-033, targeted 2026 but part of a longer
  multi-unit rollout).
- **2030:** EU FuelEU Maritime OPS (shore power) mandate takes effect at TEN-T core ports for
  passenger/container ships (L10-043); Singapore's MPA requires all new harbour craft to be fully
  electric, B100-biofuel-capable, or net-zero-fuel-compatible from 2030 (L10-055).
- **2035:** EU FuelEU OPS mandate extends to all EU ports (L10-043); CARB's original (now
  under formal repeal) target for a fully zero-emission drayage fleet at California ports/railyards
  (L10-044) -- now a live open question rather than a settled date.
- **Through 2031 (inference, not sourced to a single dated commitment):** if the CARB repeal
  proceeds as announced and the IMO Net-Zero Framework adoption continues to slip past October 2026,
  expect near-term US and global regulatory *compulsion* for maritime/port/drayage electrification to
  weaken relative to 2023-2024 expectations, while China's state-directed procurement and standards
  activity (CCS battery-ship rules, SAC excavator battery-swap standard, provincial mining tenders)
  continues on schedule regardless -- a directional read, not a quantified forecast.

## US vs Asia differences

- **Regulatory posture:** The US is fragmented and currently *loosening*: CARB is formally repealing
  its drayage/high-priority zero-emission fleet mandate (L10-044) even as EPA separately disburses
  $3B in Clean Ports Program grants for zero-emission equipment (L10-048) and FRA studies battery
  locomotive options (L10-047) -- an internally inconsistent US federal-vs-state signal. The EU is
  schedule-driven and firm (FuelEU Maritime OPS mandate, fixed 2030/2035 dates, L10-043). China is
  standards-and-tender-driven: CCS updated its battery-powered-ship rules for a 31 Dec 2025 effective
  date (L10-045) and a national standard for excavator battery-swap systems exists (L10-046),
  alongside a steady cadence of state-owned-enterprise equipment tenders (L10-034, L10-035) --
  regulatory/standards activity that is proceeding independent of Western compliance-deadline
  slippage. Singapore (MPA) is specification-and-subsidy-driven with a firm 2030 all-electric harbour
  craft target and a dedicated charging/battery-swap safety standard (TR136, L10-055).
- **Deployment scale and technology choice:** China is running large-scale battery-swap deployments
  across multiple vehicle classes simultaneously -- cargo ships (L10-040), mining trucks (L10-031,
  via SPIC technology exported to Mongolia), and a dedicated national standard for excavator battery
  swap (L10-046) -- suggesting swap-based architectures are a distinctively Chinese strategic bet,
  while Australian (Fortescue, BHP/Rio Tinto) and Brazilian (Vale) deployments lean toward static/
  megawatt charging and trolley-assist rather than swap. Japan's entrant (Hitachi/ABB) reached only a
  single-truck Zambia deployment by 2024 (L10-054), a materially slower commercial pace than
  Fortescue's simultaneous multi-hundred-truck order book (L10-028).
- **Supply chain:** XCMG (China) is now a direct haul-truck supplier to an Australian iron-ore major
  (Fortescue) alongside Germany's Liebherr (L10-028) -- a level of Chinese heavy-mining-equipment
  market penetration into a Western-aligned market that does not have an equally visible mirror image
  (no Western mining-truck OEM was found supplying at comparable committed volume into China's
  domestic open-pit tenders, L10-034, which specify equipment by tonnage class without naming
  international bidders).
- **Local-language primary evidence gaps:** Chinese-language primary sourcing (tenders, CCS
  standard, CSAE journal) was substantially more accessible this session than Japanese-language
  primary sourcing -- a Japan Railway Construction, Transport and Technology Agency (JRTT) PDF survey
  of Norway's electric-ferry sector was located but could not be successfully decoded/fetched this
  session, leaving Japan's own domestic-language regulatory/industry perspective under-represented
  relative to China's and Korea's in this collection. This is a flagged gap, not a claim that Japan
  lacks relevant primary sources.

## Unresolved contradictions

1. Fortescue is simultaneously investing in static megawatt charging (its own 6MW charger, L10-029)
   and trolley-assist-compatible trucks (Liebherr T264's "Power Rail" system, L10-052), while Rio
   Tinto is separately trialing Chinese battery-swap technology at a different mine (Oyu Tolgoi,
   L10-031) -- three different major mining companies (or the same company, in Fortescue's case)
   are betting on three different charging architectures concurrently, and this session found no
   evidence of convergence on a dominant approach.
2. The IMO approved its Net-Zero Framework in April 2025 with language describing it as a landmark,
   binding, first-of-its-kind mechanism (L10-042), yet the formal adoption vote was adjourned by a
   majority of member states in October 2025 to October 2026 (cross-referenced from companion
   WebSearch synthesis) -- the "approved" framing and the actual adoption status are in tension, and
   entry into force may now be no earlier than March 2028, a meaningful delay to the primary global
   economic driver for shipboard electrification and shore power.
3. CARB is formally repealing its Advanced Clean Fleets drayage/high-priority provisions (L10-044)
   in the same period that EPA is disbursing nearly $3B in Clean Ports Program grants explicitly to
   fund zero-emission port equipment (L10-048) -- one arm of US environmental policy is pulling back
   a regulatory mandate while another arm is actively funding the equipment that mandate would have
   required, a direct within-US-government contradiction in signal strength for port electrification
   demand.
4. Cold-ironing (shore power) academic literature frames the technology as economically marginal
   without hybrid renewable/storage support (L10-007, L10-008), yet EU FuelEU Maritime imposes a hard
   2030/2035 OPS mandate regardless of unit economics (L10-043) -- implying EU compliance costs may
   be underwritten by regulatory compulsion rather than the technology having reached independent
   cost-competitiveness, a distinction future demand modeling should not blur.
5. The IMO's Net-Zero Framework -- the single most-publicized global maritime decarbonization
   mechanism -- applies only to ships over 5,000 GT engaged in *international* trade (L10-042), which
   is precisely the segment where this session found the least evidence of proven battery-electric
   deployment. The strongest evidence of actual battery-electric vessels in commercial service
   (Norway's ~70-ferry short-sea fleet, L10-039; China's inland canal/river cargo and passenger
   vessels, L10-040) falls outside IMO's international-shipping scope entirely and is instead governed
   by a patchwork of national/regional rules (EU FuelEU Maritime, L10-043; Singapore's TR136,
   L10-055; China's CCS battery-ship rules, L10-045) -- the highest-profile global regulatory lever
   is not aimed at the market segment where the underlying technology already works.

## Uncertainty and session limitations (honesty note)

Most ScienceDirect, IEEE Xplore, SAGE, and one Nature/Springer academic record in this set could not
be independently fetched this session (HTTP 403 paywalls, empty-page access gates, or a login-wall
redirect); those records rely on WebSearch-synthesized titles/authors/DOIs and are individually
flagged in their own `notes` fields. Several DOIs (L10-008, L10-018, L10-021, L10-022) are inferred
from MDPI's documented, deterministic numbering convention rather than independently resolved via
doi.org, and one Nature DOI (L10-016) is inferred from Nature's standard article-ID pattern --
consistent with the precedent set in the L02 and L08 lane briefs. A Japanese-government-affiliated
PDF (JRTT survey of Norway's electric-ferry sector) was located but returned only undecodable
binary/compressed content on fetch and could not be cited for its actual content; it was excluded
from the ledger entirely rather than cited on the basis of its title alone. The EPA Clean Ports
Program's specific Port of Oakland award figure ($322M, encountered in earlier WebSearch synthesis)
could NOT be independently confirmed on the EPA program page actually fetched this session (L10-048)
and was deliberately excluded from that record's `claim_supported` field rather than reported as
fact. The Chinese national standard for excavator battery-swap systems (L10-046) was found via
search but both HTTP and HTTPS fetch attempts failed with SSL/protocol errors; its formal standard
number (e.g., a GB/T identifier) was not independently confirmed and is flagged for verifier
follow-up. Two SEC filings (L10-037, L10-038) were identified by URL via WebSearch but not
independently read this session. Tier balance in this 55-record set is 42 T1 / 13 T2 / 0 T3 (76.4%
T1), which clears the mission's 70% mission-critical floor but falls short of the 78% aspirational
target stated in the scout brief; the shortfall is concentrated in maritime cold-ironing reviews,
agricultural-machinery reviews, and vendor datasheets/trade-press demand records, which this session
judged should be tiered honestly as T2 (per SOURCE_STANDARDS' explicit rule that reviews remain T2
regardless of venue) rather than reclassified upward to hit the target.

## Opportunity-shaped pain statements

Presented as pain + who pays + evidence -- not startup pitches.

1. **Pain:** Underground battery-electric LHD loaders cannot complete a full production shift on
   battery alone with current technology, forcing mid-shift charging stops or swaps that disrupt
   production; trolley-assisted charging is still an active research response (up to 75% simulated
   energy-cost reduction), not a deployed commercial standard. **Who pays:** underground mine
   operators absorb either production disruption (mid-shift charging/swaps) or the capital cost of
   overhead trolley infrastructure retrofits. **Evidence:** L10-014, L10-024.
2. **Pain:** Major open-pit mining companies are each committing capital to a different, mutually
   incompatible charging architecture (Fortescue: static megawatt charging + trolley-assist-ready
   trucks; Rio Tinto: Chinese battery-swap technology) with no evidence of convergence, meaning
   fleet-wide infrastructure standardization across the industry is not close. **Who pays:** mining
   companies bear stranded-infrastructure risk if their chosen architecture does not become the
   industry standard; equipment OEMs (Liebherr, XCMG, Caterpillar) must support multiple competing
   charging interfaces simultaneously. **Evidence:** L10-028, L10-029, L10-031, L10-052.
3. **Pain:** No public list price exists for any battery-electric haul truck, underground LHD, or
   battery-electric locomotive product examined this session, despite active multi-billion-dollar
   procurement activity (Fortescue, Vale, Union Pacific). **Who pays:** anyone underwriting an
   investment, supply, or competitive-positioning decision in this hardware category currently pays
   a real information-asymmetry cost and must rely on partial contract-scale disclosures instead of
   unit economics. **Evidence:** L10-051, L10-052, L10-053, L10-028, L10-029, L10-030.
4. **Pain:** Cold-ironing (shore power) economics remain marginal without hybrid renewable/storage
   support per multiple 2023-2024 techno-economic studies, yet the EU's FuelEU Maritime regulation
   imposes a hard, economics-independent 2030/2035 OPS compliance deadline. **Who pays:** shipowners
   and port authorities must fund shore-power infrastructure ahead of independent cost-competitiveness,
   with the regulation's EUR-per-unused-kWh penalty (per cross-referenced trade sources, not
   independently confirmed on the fetched EUR-Lex page) as the compulsion mechanism. **Evidence:**
   L10-007, L10-008, L10-043.
5. **Pain:** US federal port-electrification policy is internally contradictory: CARB is repealing
   its drayage zero-emission mandate at state level while EPA disburses nearly $3B in Clean Ports
   Program grants at federal level for the same category of equipment. **Who pays:** port operators
   and equipment vendors face genuine near-term demand uncertainty -- capital committed against an
   assumed regulatory mandate (drayage ZEV) may no longer have that mandate in place by the time
   equipment is delivered. **Evidence:** L10-044, L10-048.
6. **Pain:** The IMO's global Net-Zero Framework, described by the IMO itself as a landmark binding
   mechanism, has had its formal adoption vote adjourned by member-state majority to October 2026,
   pushing possible entry into force to no earlier than March 2028 -- delaying the single largest
   potential global economic driver for shipboard battery/hybrid retrofit and shore-power investment.
   **Who pays:** shipowners and equipment vendors who invested in early compliance capability face a
   longer-than-expected payback horizon before the pricing mechanism actually bites. **Evidence:**
   L10-042.
7. **Pain:** China is running simultaneous battery-swap deployments across cargo ships, mining
   trucks, and (per a dedicated national standard) excavators, while Australian and Brazilian heavy
   mining/rail electrification bets lean toward static charging and trolley-assist -- these
   architectures use different connector, safety, and facility standards, and this session found no
   evidence of cross-recognition between the Chinese swap-standard ecosystem (L10-045, L10-046) and
   the CharIN/IEC MCS static-charging standard (L10-050). **Who pays:** multinational mining/shipping
   operators with assets in both ecosystems (e.g., Rio Tinto, which is piloting both Cat static-charge
   trucks in Australia and Chinese swap trucks in Mongolia) bear the cost of maintaining two
   incompatible technology stacks. **Evidence:** L10-031, L10-045, L10-046, L10-050.
8. **Pain:** Singapore's MPA published its e-HC charging/battery-swap infrastructure safety standard
   (TR136) only in March 2025, yet the same regulatory program requires ALL new harbour craft
   operating in the Port of Singapore to be fully electric (or B100/net-zero-fuel-compatible) from
   2030 -- leaving under five years between the safety-infrastructure standard's publication and a
   fleet-wide new-build mandate. **Who pays:** Singapore-registered harbour-craft operators (crew
   transfer, cargo supply, bumboat operators) face compressed capex-timing risk; MPA bears
   program-execution risk if charging/battery-swap infrastructure rollout lags the 2030 deadline.
   **Evidence:** L10-055.
9. **Pain:** China's state-owned mining enterprises run frequent, precisely-scoped, publicly
   disclosed equipment tenders (fleet size, tonnage class, budget) that Western competitors and
   analysts cannot easily benchmark against Australian/Brazilian contract announcements, which
   typically disclose truck count and battery capacity but omit dollar values. **Who pays:**
   non-Chinese vendors and market analysts assessing competitive position in the global mining
   equipment market face an asymmetric-transparency problem -- mirroring the identical finding in the
   L08 (DC grids/HVDC) lane brief for Chinese vs. Indian/European contract disclosure. **Evidence:**
   L10-034, L10-035 vs. L10-028, L10-030, L10-033.
10. **Pain:** Japan's mining-electrification entrants (Hitachi/ABB) reached only a single prototype
    deployment (Zambia, 2024) by the time this session was conducted, a materially slower commercial
    pace than Australia's Fortescue (simultaneous multi-hundred-truck order book) or China's
    multi-site battery-swap rollout -- despite Japan possessing a globally significant construction-
    machinery OEM base (Komatsu, Hitachi). **Who pays:** Hitachi/Komatsu bear opportunity-cost risk of
    ceding early mining-electrification share to XCMG/CATL-enabled and Caterpillar/Liebherr-enabled
    competitors; this session could not determine whether the gap reflects a deliberate technology
    (trolley/hybrid vs. pure-battery) choice or a genuine capability lag. **Evidence:** L10-028,
    L10-030, L10-031, L10-054.
11. **Pain:** Underground and open-pit mining-electrification academic literature is thick with
    primary optimization/sizing papers (battery sizing, gear ratios, swap scheduling, trolley-assist
    simulation) but this session found comparatively few primary techno-economic studies validating
    those models against real multi-year fleet operating data -- most named-buyer evidence in this
    lane (Fortescue, BHP/Rio Tinto, Rio Tinto/SPIC) describes trials and early deployments, not
    multi-year operating results. **Who pays:** mine operators and financiers must currently
    underwrite electrification capex against simulation-validated rather than field-validated
    economic models. **Evidence:** L10-001, L10-002, L10-013, L10-014, L10-015, L10-017, L10-018 vs.
    L10-028, L10-030, L10-031.
12. **Pain:** Agricultural machinery electrification literature captured this session skews toward
    forward-looking reviews (L10-019, L10-020) rather than primary field-validated deployment
    studies -- only one primary experimental study (dynamometer/field-test battery sizing, L10-016)
    was found -- suggesting this sub-segment of the lane is meaningfully less mature than mining or
    rail electrification despite active vendor marketing (Kubota, John Deere/Wacker Neuson, Volvo
    CE, per companion WebSearch context not independently fetched this session). **Who pays:**
    ag-equipment OEMs and early-adopting farmers currently lack independent field-validated economic
    evidence (beyond vendor claims and single-study estimates) to justify battery-electric tractor
    capex. **Evidence:** L10-016, L10-019, L10-020.
