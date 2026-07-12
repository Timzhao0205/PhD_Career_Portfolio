# L06 — Semiconductor Manufacturing Plasma/RF/High-Voltage Subsystem Niches

Lane scout brief. Sources cited as `L06-0NN` refer to `10_SOURCE_ATLAS/L06_raw_sources.json`
(55 candidate records, all `accepted: false` pending verifier review). This lane covers the
*subsystem* layer inside semiconductor fab tools -- RF generators and impedance-matching
networks, plasma sources, electrostatic chucks (ESCs), high-voltage modules for implanters and
EUV sources, chamber sensors/arc detection, gas delivery, and subfab power quality -- not the
fab tools themselves (etchers, deposition systems, scanners) or the fab-tool OEMs' whole-tool
business. Founder background was not used to select topics within this lane.

## 1. Frontier state

- **RF impedance matching and plasma-source control is an active, unsettled research area, not
  a solved commodity.** Multiple 2024-2026 peer-reviewed papers model and control L-type matching
  networks (L06-001), frequency-modulation-assisted matching (L06-002), dual-frequency matching
  circuits (L06-003), and dual-coil-antenna current/phase control for ICP uniformity (L06-008).
  "Tailored voltage waveform" biasing -- precisely shaping the RF bias waveform to control ion
  energy distribution for atomic-scale etch -- is a particularly active 2024-2026 cluster
  (L06-009, 010, 011, 027) with direct industry co-authorship (Samsung's Sang Ki Nam on L06-009).
- **Electrostatic chucks are a distinct, ceramics-heavy materials-science + electrical-engineering
  problem**, not just a mechanical fixture: dielectric breakdown physics (L06-005), Johnsen-Rahbek
  charging/discharging behavior under plasma exposure (L06-006), yttrium-doped AlN resistivity
  tuning (L06-014), and thermal/temperature-uniformity modeling (L06-007, 015) are all
  independent, currently active research threads. A Chinese systematic design-space framework
  (L06-004, directly fetched and confirmed) shows this is also a live topic for China's domestic
  equipment-component developers, not only US/Japan incumbents.
- **Arc detection / chamber-sensor technology is dominated by patent activity, not peer-reviewed
  publication** -- the initial search pass surfaced roughly a dozen relevant US patents (Applied
  Materials, Advanced Energy-lineage assignees) for RF-reflected-power arc detection, gas-emission
  spectroscopy arc detection, and micro-arc detection, but only one confirmed peer-reviewed paper
  (L06-018, a Korean KIEEME-journal in-situ abnormal-discharge-detection method). This is a
  technology area where the commercial/patent literature runs well ahead of open academic
  publication -- a real evidence gap, not necessarily a real technology gap.
- **High-voltage ion-implanter modules have a deep historical lineage** (L06-019 through 022,
  spanning 1976-1992: 200kV design philosophy, high-current systems, Fraunhofer-AIS Erlangen
  work) that still structurally underlies today's commercial implanters. The live commercial
  frontier is SiC power-device implantation: Axcelis' Purion H200/Purion Power Series+ platform
  is reported to hold a 70-80% share of SiC ion-implantation equipment over its nearest competitor
  Applied Materials (per search-synthesis; unconfirmed by a direct market-share primary source
  this session -- flag for verifier).
- **EUV source physics (laser-produced tin-droplet plasma) is a distinct high-voltage/high-power
  drive-laser subsystem frontier** with an active 2024 publication cluster on pre-pulse shaping
  (L06-016) and droplet-irradiation modeling for a proposed next-generation 2-micrometer-laser
  architecture (L06-017) -- i.e., even the current >500W-1000W EUV source generation is not
  considered a finished technology; a further architecture change is already being modeled.
- **Gas delivery / mass flow control (MFC) is a narrower, more mature-sounding technical area**
  but still has live 2025 control-theory publication (L06-026, estimated-output-feedback MFC
  control) and a dedicated SEMI standard on transient-response testing (SEMI E17, L06-035) --
  precisely because process-gas switching speed (sub-1-second step response, no overshoot) is
  a real limiting factor for atomic-layer deposition/etch throughput.
- **Subfab power quality is governed by an old (2007) but still-cited SEMI standard** (SEMI F47
  voltage-sag immunity, L06-034) rather than a large open peer-reviewed literature; most current
  material on this topic found this session was vendor-blog/consultancy content (Powerside,
  Schneider Electric, Ampersure) making specific-sounding claims (e.g., "harmonic distortion
  >8% THD increases defect density 4-7x in sub-5nm production") that could not be traced to a
  primary study and were therefore NOT logged as accepted-candidate sources -- this is a real gap
  the mission's demand for load-bearing citation discipline is designed to catch.

## 2. Bottlenecks

- **RF power/impedance-matching component localization in China lags far behind whole-tool
  localization.** China's overall semiconductor-equipment localization rate reportedly reached
  21-35% by 2025 depending on methodology (L06-051 vs. L06-052, a genuine unresolved
  contradiction -- see Section 7), and etch/deposition *tools* are reported above 27-40%
  localized. But RF power *components specifically* were reportedly under 12% localized as of
  2024 (L06-054), with domestic entrants (Hengyunchang, Injet Electric) only breaking the
  MKS/Advanced Energy duopoly very recently (Hengyunchang IPO'd January 2026, L06-042/043).
  Precision valves, quartz parts, and precision ceramics show similarly lagging localization
  versus whole-tool figures (per search synthesis, not independently fetched as a standalone
  primary source this session -- treat as a lead).
- **Customer concentration inside the (thin) domestic-China RF-power supply base is severe.**
  Hengyunchang's single largest customer, Piotech (拓荆科技), is simultaneously a shareholder and
  accounted for 45-63% of Hengyunchang's revenue in 2022-2024, with the top five customers at
  90.62% of 2024 revenue (L06-042). This is a structural fragility (and potential conflict of
  interest) in the very supply chain China is building to reduce dependence on MKS/Advanced
  Energy.
- **MFC transient response is a real, standards-codified throughput constraint** (SEMI E17,
  L06-035): fast atomic-layer process-gas switching needs sub-1-second step response with no
  overshoot, and current thermal-flow-sensor-based MFCs are reported to still show overshoot
  under transient conditions (per search synthesis around L06-026's topic area).
- **Subfab voltage-sag tolerance is decades-old engineering** (SEMI F47 dates to 2007, last
  reapproved 2008, L06-034) governing equipment that must now support far higher power densities
  and tighter process windows than when the standard was written -- a plausible mismatch between
  an aging standard and current tool requirements, though this session found no primary technical
  paper directly testing whether SEMI F47's sag-immunity thresholds remain adequate for
  leading-edge (<=3nm) RF/plasma tool power electronics.
- **EUV source power scaling keeps requiring new subsystem generations, not incremental tuning**:
  the ~500W-1000W current generation is already being followed by proposed 2-micrometer-drive-laser
  architectures in the peer-reviewed literature (L06-017), meaning EUV high-voltage/high-power
  drive-laser subsystem suppliers face a moving technical target, not a mature commodity.

## 3. Named buyers and spending signals

- **US Department of Commerce / CHIPS Program Office** -- finalized a $18 million direct CHIPS
  award (within a $307.2 million total project) to Edwards Vacuum for the first-ever US-based
  dry-vacuum-pump manufacturing facility (Genesee County, NY; up to 600 jobs; milestones through
  end of 2028) (L06-033, directly confirmed on nist.gov/chips). Dry vacuum pumps are a
  subfab/chamber-environment subsystem directly adjacent to L06's gas-delivery and chamber-sensor
  scope.
- **Advanced Energy Industries (NASDAQ: AEIS)** -- FY2025 total revenue $1.8 billion (+21.4%),
  semiconductor-equipment segment $840 million (+6% YoY); new RF/plasma-power platforms (Everest,
  EVOS, NavX) already generating "double-digit millions" in revenue while still described as
  "early pilot or early production stage" by CFO Paul Oldham on the Q4 2025 earnings call
  (L06-039, L06-040) -- i.e., real, dated, quantified customer adoption of next-generation RF
  power products at the leading edge (sub-2nm).
- **Wolfspeed, Inc.** -- took shipment of an Axcelis Purion H200 SiC ion-implant evaluation
  system (2023-07-26) in the context of its $6.5 billion capacity-expansion program for
  electric-vehicle-driven SiC power-device demand (L06-041) -- a concrete, named, dated
  high-voltage-implanter-module purchase.
- **Piotech (拓荆科技), AMEC (中微公司/Advanced Micro-Fabrication Equipment), NAURA (北方华创), ACM
  Shanghai (盛美上海), Wei Dao Nano (微导纳米)** -- named as Hengyunchang's largest customers
  (L06-042/043); AMEC alone reported 2024 revenue of ~RMB 9.065 billion (+44.73% YoY), etch
  equipment ~RMB 7.277 billion (+54.73% YoY) (L06-048) -- these are the real domestic-China
  buyers of RF-power/ESC/gas-delivery subsystems, several times larger than their own component
  suppliers.
- **SMIC and Yangtze Memory Technologies (YMTC)** -- named as chipmaker partners/customers in
  Hengyunchang's IPO coverage (L06-043), i.e., China's leading-edge fabs are the ultimate
  end-demand pull for the domestic RF-power-supply-chain buildout.
- **Tata Electronics / Tata Semiconductor Manufacturing (with Taiwan's PSMC)** -- signed a
  technology-transfer agreement (2024-09-26) for India's first commercial logic fab in Dholera,
  Gujarat (investment up to INR 91,000 crore / ~US$11 billion, 50,000 wafer-starts/month
  capacity), with a companion India Semiconductor Mission Fiscal Support Agreement reportedly
  covering 50% of project cost (L06-047) -- a large, dated, government-linked *future* trigger
  for etch/deposition/implant/RF/gas-delivery subsystem purchases from AMAT/TEL/Lam/Axcelis-tier
  suppliers, though no L06-subsystem-level order has yet been placed/disclosed.
- **A*STAR / Applied Materials (Singapore)** -- launched the APEX joint lab (2024-09-05) across
  five A*STAR institutes to build local semiconductor-equipment-component and supply-chain
  capability targeting ICAPS markets (L06-046) -- a real, dated, government-backed Singapore
  equipment-ecosystem-development signal, though the investment amount was not disclosed in this
  announcement.
- **TSMC** -- its own Supplier Sustainability Standards (Version 2.0, March 2025) impose specific
  safety-engineering requirements (static-electricity grounding for gas/chemical equipment,
  leak-proof/leak-sensor requirements) directly binding on L06 subsystem vendors selling into its
  supply chain (L06-045) -- a genuine buyer specification, though the full document could not be
  directly re-fetched this session (403 on both hosted PDF URLs).

## 4. Incumbent map (companies, products, price signals)

| Company | Product / Role | Signal |
|---|---|---|
| Advanced Energy Industries (US) | Everest, EVOS, NavX RF/plasma power generators | FY2025 revenue $1.8B; semiconductor segment $840M; new platforms "double-digit millions" (L06-039/040) |
| MKS Instruments (US) | RF power supplies, gas/vapor delivery, vacuum subsystems | Named (alongside Advanced Energy) as the incumbent duopoly that Hengyunchang says it is displacing in China (L06-042/043); not independently re-confirmed via a direct MKS filing this session |
| Comet Group / Comet PCT (Switzerland) | Synertia RF Power Delivery Platform (matching networks, RF generators, vacuum capacitors) | Product positioned for "multi-layer next-generation memory and atomic-scale plasma processes" (L06-049); market-size figure ($1.6B RF-power-subsystem market) found only via search synthesis, NOT confirmed by direct fetch -- do not cite without re-fetch |
| Kyosan Electric Manufacturing (Japan) | RF generators (HFK15TP 400kHz/1.5kW; RFK35TS 13.56MHz/3.5kW), electronic matchers | Directly confirmed spec sheet (L06-050); no pricing disclosed |
| Axcelis Technologies (US) | Purion H200 / Purion Power Series+ SiC ion implanters | Shipped evaluation system to Wolfspeed 2023-07-26 (L06-041); reported 70-80% share of SiC-implant market over Applied Materials (unconfirmed primary source this session) |
| Applied Materials (US) | Ion implanters, etch/deposition tools, APEX joint lab (Singapore) | A*STAR partner for equipment-component R&D (L06-046); described as Axcelis' nearest SiC-implant competitor (unconfirmed share) |
| Hengyunchang / Shenzhen CSL Vacuum Science and Technology (China) | CSL/Bestda/Aspen plasma RF power-supply systems (Bestda: 28nm; Aspen: 14nm) | IPO'd SSE STAR Market 2026-01-28, raised RMB 1.469-1.55B, #1 domestic China RF-power-system share (2023); top customer Piotech = 45-63% of revenue (L06-042/043) |
| Sichuan Injet Electric (China) | RF power supplies for PECVD equipment | FY2024 revenue RMB 1.78B; semiconductor/electronic-materials segment RMB 185.2M (23.24% of revenue), PECVD RF-power orders already exceeding full-year 2023 (L06-044) |
| AMEC / Advanced Micro-Fabrication Equipment (China) | CCP/ICP plasma etch tools (buyer of RF power/ESC/gas-delivery subsystems) | FY2024 revenue ~RMB 9.065B (+44.73%); etch segment ~RMB 7.277B (+54.73%); >95% domestic-etch-application coverage claimed (L06-048) |
| NAURA (China) | Etch/deposition/oxidation-diffusion tools; also a Hengyunchang customer | >60% share of oxidation/diffusion furnaces on SMIC's 28nm lines; H1 2025 revenue ~$2.2B (L06-051/052) |
| Edwards Vacuum (UK/US) | Dry vacuum pumps (subfab/gas-delivery-adjacent) | $18M CHIPS award within $307.2M Genesee County, NY facility -- first US-based production of this equipment class (L06-033) |
| Wonik IPS (Korea) | PECVD/deposition equipment (Samsung/SK Hynix-anchored) | >60% of revenue from Samsung Electronics and SK Hynix; 2014 3D NAND mold-process mass production, 2018 10nm-class High-K DRAM entry (L06-055) |
| SEMI (US, standards body) | SEMI F47 (voltage-sag immunity), SEMI E17 (MFC transient test) | F47: $286/$380; E17: $148/$193 (L06-034/035) -- the only directly priced items found in this lane this session |

**Pricing signals found:** SEMI standards themselves are the only directly-priced items
confirmed this session ($148-$380 per standard document, L06-034/035). No vendor publicly quoted
a unit price for an RF generator, matching network, ESC, ion-implanter module, or MFC this
session -- all commercial pricing in this lane is opaque from open sources and would require
direct RFQ/distributor contact (e.g., through Taiwan distributors like Junsun Technology, whose
product page could not be fetched this session, 403).

## 5. 2026-2031 triggers

- **US:** Edwards Vacuum's Genesee County dry-pump facility runs through end of 2028 on a
  milestone basis (L06-033); Wolfspeed's $6.5B SiC capacity expansion continues to drive Axcelis
  implanter demand (L06-041); Advanced Energy's Everest/EVOS/NavX platforms are described as still
  "early pilot or early production" in Feb 2026, implying the bulk of their revenue ramp is still
  ahead in 2026-2028 (L06-039).
- **China:** Domestic RF-power-component localization (reported <12% as of 2024, L06-054) is the
  most likely multi-year catch-up trigger, given China's overall equipment localization target
  trajectory (21-35% by 2025 depending on source, L06-051/052) and two now-public domestic RF-power
  suppliers (Hengyunchang, Injet Electric) with real, growing order books (L06-042/043/044).
- **India:** Tata-PSMC's Dholera fab (up to INR 91,000 crore, 50,000 WSPM capacity) is a
  multi-year construction project (technology-transfer agreement signed Sept 2024) that will
  require substantial future purchases of etch/deposition/implant/RF/gas-delivery subsystems from
  AMAT/TEL/Lam/Axcelis-tier suppliers once construction completes -- a dated but not-yet-realized
  L06-subsystem demand trigger for 2026-2029 (L06-047).
- **Singapore:** The A*STAR-Applied Materials APEX joint lab (announced Sept 2024) is an ongoing
  equipment-component R&D program targeting ICAPS markets, with no disclosed end date or
  investment figure found this session (L06-046) -- a live but under-specified trigger.
- **Standards:** SEMI E17's 2018 revision and SEMI F47's 2007/2008 revision are both aging
  relative to the pace of sub-3nm process requirements -- a plausible (but not directly evidenced
  this session) trigger for a standards-revision cycle in 2026-2031 as leading-edge fabs push MFC
  transient-response and power-quality requirements harder than these standards currently specify.

## 6. US vs. Asia differences

- **US** evidence in this lane skews toward (a) large, established public-company RF-power/plasma
  suppliers (Advanced Energy) reporting real segment revenue and new-platform ramp-up on investor
  calls, (b) a federal government CHIPS-funded subfab/gas-delivery-adjacent equipment
  manufacturing buildout (Edwards Vacuum), and (c) SiC power-device-driven implanter demand
  (Axcelis/Wolfspeed) tied to the EV/power-electronics capex cycle -- i.e., US evidence is
  concentrated in mature public-company disclosure and one concrete federal award, not new
  entrant activity.
- **China** evidence is dominated by very recent (2024-2026) domestic-substitution IPO/financial
  activity: Hengyunchang's IPO (Jan 2026) and Injet Electric's RF-power order growth are both
  *new* commercial entrants explicitly framed (by themselves and financial media) as breaking a
  US-supplier (MKS/Advanced Energy) duopoly -- but the underlying component-level localization
  rate is still reportedly under 12%, meaning the "catch-up" narrative is well ahead of the
  quantified reality for RF power specifically, even as whole-tool localization (etch, deposition)
  is progressing much faster (21-40%+ depending on category/source).
- **Japan** evidence found this session (Kyosan Electric) is narrower -- one confirmed
  vendor-datasheet-level product page with real specs but no market-share, revenue, or customer
  data; Japan's role in this lane's evidence base is weaker than China's, Korea's, or the US's
  this session and should be a target for follow-up scouting (e.g., Tokyo Electron's own RF/
  matching-network technology, or Kyosan's competitive position versus MKS/Advanced Energy/Comet).
- **Korea** evidence combines strong *academic* output (two fully-confirmed peer-reviewed papers
  from Korean institutions this session, L06-024/025, both on plasma/RF diagnostics for
  production-line monitoring) with a large, Samsung/SK Hynix-anchored domestic equipment maker
  (Wonik IPS, L06-055) whose deposition-equipment business is well documented but whose RF-power/
  gas-delivery-component-specific activity was not confirmed this session (product pages not
  fetched) -- Korea's evidence is academically strong but commercially under-specified in this
  pass.
- **Taiwan** evidence is the weakest single-geography coverage in this lane: TSMC's own supplier
  standards were identified but could not be directly re-fetched (403 both attempts), and a
  Taiwan-based RF-power distributor (Junsun Technology/CSL) page also returned 403. Taiwan
  geography tags in this ledger (TrendForce being TW-headquartered; PSMC as a named Taiwanese
  company transferring technology to India) are present but indirect -- a follow-up scout should
  target ITRI or a Taiwan-domiciled RF-power/plasma-equipment vendor directly.
- **Singapore** evidence (A*STAR/Applied Materials APEX joint lab) is real and dated but
  investment-amount-blind and product-agnostic at this stage -- Singapore's angle in this lane is
  equipment-component R&D capability-building rather than either mature commercial revenue (US) or
  fast-growing domestic-substitution IPOs (China).
- **India** evidence (Tata-PSMC Dholera) is a large, real, dated fab-construction commitment but
  is upstream of any L06-subsystem-specific purchase -- India's demand signal in this lane is
  currently a *future* trigger, not yet a realized subsystem order.

## 7. Unresolved contradictions

1. **China's semiconductor-equipment localization rate is reported inconsistently by two
   contemporaneous (2026) research sources**: TrendForce says overall localization rose from 25%
   (2024) to 35% (2025), beating a 30% target (L06-051); BigGo Finance/faxiangongchang.com
   describes a 4%->13%->21% trajectory through 2018-2025 (L06-052). Both cite NAURA, AMEC, and
   similar named companies, but the headline percentages differ by roughly 10-14 percentage
   points for what is nominally the same metric -- likely a scope/methodology difference (e.g.,
   value-weighted vs. unit-weighted, or different equipment-category baskets) that neither source
   makes explicit. Do not average these; a verifier should try to locate each source's underlying
   methodology before either number is used in an idea's market-sizing arithmetic.
2. **RF-power-component-specific localization (<12%, L06-054) sits far below the whole-tool
   localization figures (21-40%+, L06-051/052) for the same country/period** -- this is not
   necessarily a contradiction (component-level and tool-level localization can legitimately
   differ), but it means any claim that "China's semiconductor equipment is X% localized" is
   silently averaging over very different realities at the subsystem vs. tool level, and L06's
   specific niche (RF power, gas delivery components, precision valves, ceramics) is
   systematically behind the more commonly cited etch/deposition *tool*-level number.
3. **Comet Group's RF-power-subsystem market-size figure (~$1.6B, ~5% CAGR) could not be
   re-confirmed by direct fetch this session** despite appearing in an initial search-engine
   synthesis of what appeared to be Comet's own investor/annual-report material (L06-049 notes
   field). This figure should NOT be treated as an accepted market-sizing input until a verifier
   locates and directly fetches its exact source page.
4. **Axcelis' reported 70-80% share of the SiC ion-implantation equipment market over Applied
   Materials** was found only via a third-party investment-research summary (search synthesis),
   not a primary company disclosure or independent market-research report fetched this session --
   flag as unconfirmed pending direct verification.
5. **Vendor-blog claims about subfab power-quality impact** (e.g., "harmonic distortion >8% THD
   increases defect density 4-7x in sub-5nm production," "74% of unplanned tool downtime linked to
   power-quality events") appeared repeatedly across multiple vendor/consultancy pages
   (Powerside, Ampersure, Schneider Electric) with suspiciously specific-sounding statistics but no
   traceable primary study cited in any of them. These were deliberately NOT logged as accepted
   candidate sources in this session's ledger -- if a future scout finds the same figures
   recurring, they should be treated as an unsourced-claim cluster, not independently corroborated
   evidence, unless a primary study is located.

## 8. Opportunity-shaped pain statements (NOT startup pitches)

1. **Pain:** China's semiconductor equipment makers (AMEC, NAURA, Piotech) are scaling revenue
   40-55% year-over-year and are actively trying to domesticate their RF-power supply chain, but
   the domestic RF-power-component localization rate was reportedly still under 12% as recently as
   2024, and the two visible domestic entrants (Hengyunchang, Injet Electric) have thin, highly
   concentrated customer bases (one customer = 45-63% of Hengyunchang's revenue). **Who pays:**
   Chinese etch/deposition tool OEMs (AMEC, NAURA, Piotech) and, indirectly, the fabs buying their
   tools (SMIC, YMTC). **Evidence:** L06-042, 043, 044, 048, 051, 052, 054.
2. **Pain:** Tailored-voltage-waveform RF biasing is a fast-moving, still-unsettled research
   frontier (five 2024-2026 peer-reviewed papers found this session alone) needed for atomic-scale
   etch control at sub-2nm nodes, but commodity RF matching networks and generators do not yet
   incorporate this capability as a standard, off-the-shelf feature. **Who pays:** leading-edge
   logic/memory fabs and the RF-power-supply vendors (Advanced Energy, MKS, Comet) racing to
   productize it. **Evidence:** L06-009, 010, 011, 027, 039.
3. **Pain:** Electrostatic-chuck ceramic dielectric engineering (AlN doping for Johnsen-Rahbek
   resistivity tuning, dielectric-breakdown-limited thickness, thermal-uniformity control) remains
   an active, unsolved materials-science problem even though ESCs are a decades-old product
   category -- meaning today's ESC suppliers face a continuous materials R&D burden just to keep
   pace with tighter temperature-uniformity and clamping-force specs at each new process node.
   **Who pays:** ESC-integrating tool OEMs and their fab customers (specific named ESC-component
   buyers not identified this session). **Evidence:** L06-004, 005, 006, 007, 014, 015.
4. **Pain:** Mass-flow-controller transient response (sub-1-second step response, no overshoot)
   is explicitly standards-codified as a limiting factor for atomic-layer process-gas switching
   (SEMI E17), and a 2025 control-theory paper is still trying to improve MFC transient control via
   estimated-output feedback -- suggesting current commercial MFCs do not fully meet the
   throughput needs of the fastest atomic-layer deposition/etch recipes. **Who pays:** advanced
   deposition/etch tool OEMs and the fabs running throughput-limited ALD/ALE recipes. **Evidence:**
   L06-026, 035.
5. **Pain:** Arc/micro-arc detection in RF plasma chambers is a heavily patented but thinly
   peer-reviewed technology area -- only one confirmed peer-reviewed paper was found this session
   against roughly a dozen relevant patents -- meaning independent, reproducible, non-vendor
   evaluation of competing arc-detection approaches (RF-reflected-power monitoring vs. gas-emission
   spectroscopy vs. electrical-signal-based methods) is scarce in the open literature. **Who
   pays:** RF-generator/matching-network vendors and the fabs relying on arc-related tool downtime
   avoidance (no named buyer-side procurement evidence found this session). **Evidence:** L06-018
   (only confirmed peer-reviewed source); patent landscape noted in Section 1 but not logged as
   individual source records this session.
6. **Pain:** EUV source subsystems are not settling into a stable architecture -- even as the
   current laser-produced-plasma tin-droplet source scales past 500W-1000W, peer-reviewed 2024
   work is already modeling a next-generation 2-micrometer-drive-laser architecture -- implying
   EUV high-voltage/high-power drive-laser subsystem suppliers (and their component suppliers)
   face a recurring architecture-change risk rather than a maturing, incrementally-improved
   product line. **Who pays:** ASML and its EUV-source supply chain (specific named component
   suppliers below ASML/Cymer not identified this session). **Evidence:** L06-016, 017, 030, 031.
7. **Pain:** SiC power-device demand (EV-driven) is pulling hard on high-voltage ion-implanter
   capacity (Axcelis shipped a named evaluation system to Wolfspeed inside a $6.5B capacity
   expansion), but this session found no independent, primary confirmation of the oft-cited
   70-80%-share claim for Axcelis over Applied Materials in SiC implantation -- meaning the
   competitive structure of this specific high-voltage-module niche is less well-evidenced than
   the demand pull itself. **Who pays:** SiC power-device fabs (Wolfspeed and others).
   **Evidence:** L06-041 (demand confirmed); competitive-share claim unconfirmed, see Section 7.
8. **Pain:** Subfab power-quality engineering rests on a 2007/2008-vintage SEMI standard (F47)
   even as leading-edge tools' power density and process-window sensitivity have increased
   substantially since then, yet this session found no primary technical study directly testing
   whether F47's sag-immunity thresholds remain adequate for current-generation RF/plasma tool
   power electronics -- only unsourced-sounding vendor/consultancy statistics (see Section 7,
   contradiction 5) that could not be traced to a primary study. **Who pays:** fab operators
   bearing the cost of power-quality-related tool downtime and scrapped lots (no named buyer
   identified this session). **Evidence:** L06-034 (standard confirmed); downtime-cost claims
   explicitly NOT accepted as sourced this session.
9. **Pain:** India's first commercial logic fab (Tata-PSMC, Dholera, up to INR 91,000 crore) is
   under construction with a large government fiscal-support commitment, but no L06-subsystem-level
   (RF power, ESC, gas delivery, implant) purchase, tender, or supplier relationship has been
   publicly disclosed yet -- meaning India's L06 demand is currently a well-evidenced *future*
   trigger rather than a realized commercial opportunity, and the timing/sequencing of subsystem
   procurement (direct from AMAT/TEL/Lam/Axcelis vs. a local-content requirement favoring new
   entrants) is unknown. **Who pays:** Tata Electronics / Tata Semiconductor Manufacturing
   (eventual subsystem buyer, exact suppliers not yet named). **Evidence:** L06-047.
10. **Pain:** Singapore's A*STAR-Applied Materials APEX joint lab is explicitly framed around
    building local SME capability in semiconductor-equipment components and supply chain, but the
    2024 announcement disclosed no investment figure, product roadmap, or timeline -- making it
    impossible from this session's evidence alone to judge whether this is a well-funded strategic
    bet or a modest research collaboration. **Who pays:** unclear -- A*STAR/Singapore government
    and Applied Materials presumably co-fund, but the split and total is not disclosed.
    **Evidence:** L06-046.

## Methodology notes and gaps for the verifier

- 55 candidate records collected (within the 45-55 target range). 31 are academic
  peer-reviewed candidates (26 T1 primary research + 5 T2 review articles), exceeding the >=27
  floor. Two academic records (L06-024 Kwon et al. and L06-025 Lee/Kwon/Chung) were fully fetched
  and independently confirmed this session, including exact submission/acceptance/publication
  dates and DOI-matched publisher metadata -- these are the strongest-confirmed academic sources
  in the set. Most other academic records rely on search-indexed titles/DOIs with AIP/ScienceDirect
  paywalls returning HTTP 403 on direct fetch (a systematic pattern this session, not
  lane-specific) -- every one of these needs a verifier fetch pass (ideally via institutional
  access) before `peer_review_status` can move from `unverified` to `verified`.
- Estimated tier mix of the collected (not yet accepted) set: approximately 38 T1-eligible, 16 T2,
  1 T3 (~69% T1), modestly below the mission's >=70%/>=75%-target guidance for a scout's collected
  set. This reflects a deliberately conservative tiering choice: several Chinese company-filing-
  derived records (Hengyunchang, Injet Electric, AMEC) are sourced via financial-media reporting on
  official disclosures rather than the raw regulatory filing PDF itself, and were tiered T1 or T2
  based on how directly each article appeared to quote the official filing. A follow-up scout
  wave could reasonably close the gap to 70-75% either by directly fetching the underlying SSE/
  SZSE filing PDFs (upgrading confidence on existing records) or by adding a handful more
  unambiguous T1 peer-reviewed papers or primary government/standards documents.
- Demand-primary count: 10 records carry a non-"none" `demand_evidence_type` (L06-033 CHIPS award,
  L06-039 earnings transcript, L06-040 10-K, L06-041 direct customer documentation, L06-042/043/044
  company filings, L06-045 buyer specification, L06-046/047 official project awards, L06-048
  company filing) -- meets the >=10 floor.
- Government/national-lab/standards-body count: 7 records (L06-032 through L06-038), exceeding the
  >=4 floor; two of these (L06-037 GAO report, L06-038 NIST EUV workshop report) were fetched as
  binary PDFs but text extraction failed this session -- their existence and topical relevance are
  confirmed, but no specific quoted figure from either should be treated as verified until a
  verifier re-extracts the text with a different tool.
- Market/industry count: 7 records (L06-049 through L06-055 minus the ones double-counted as
  demand/government), meeting the >=4 floor; one (L06-053, Global Growth Insights) is an
  unaudited consultancy market-size estimate and is explicitly tiered T3 per SOURCE_STANDARDS.
- Asian-market coverage: CN (6 records, 5 of which are Chinese-language: L06-042, 043, 044, 048,
  054), JP (1 Japanese-language: L06-050), KR (2 records, 1 Korean-language: L06-055; plus
  KR-authored English-language academic papers L06-024/025 which add geography but not
  language-count credit), TW (2 records tagged, both indirect -- TrendForce as a TW-headquartered
  research firm, and PSMC as a named Taiwanese company; no TW-domiciled primary source was
  successfully fetched this session), SG (1 record: L06-046), IN (1 record: L06-047) -- total
  Asian-geography-tagged records exceed the >=8 floor, and local-language primary sources (CN x5,
  JP x1, KR x1 = 7) exceed the >=4 floor.
- **Weakest coverage / follow-up priorities for a future scout wave:** (1) Taiwan -- no
  Taiwan-domiciled vendor or institute (ITRI, or a Taiwan RF-power distributor) was successfully
  fetched this session (Junsun Technology page returned 403); (2) direct primary confirmation of
  Comet's RF-power-subsystem market-size claim; (3) direct SEC.gov fetch of the Advanced Energy
  10-K (403 this session, relied on secondary corroboration); (4) direct fetch of the SSE-filed
  Hengyunchang prospectus PDF and the SZSE-filed Injet Electric annual report, rather than
  financial-media reporting on them; (5) primary confirmation (not vendor-blog) of any subfab
  power-quality defect-rate/downtime-cost claim, since several specific-sounding statistics found
  this session could not be traced to a primary study and were deliberately excluded from the
  ledger.
