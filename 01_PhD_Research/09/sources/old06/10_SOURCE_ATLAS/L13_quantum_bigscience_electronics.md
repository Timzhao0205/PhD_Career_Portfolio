# L13 -- Quantum/Big-Science Classical Electronics, Timing, Control, and Facility Hardware

Lane scout brief. Sources cited as `L13-0NN` refer to `10_SOURCE_ATLAS/L13_raw_sources.json`
(52 candidate records, all `accepted: false` pending verifier review). This lane covers
room-temperature and cryogenic classical control electronics, timing/synchronization systems,
control-system software/hardware stacks, cryostat-adjacent wiring/interconnect, and facility-scale
hardware serving quantum computers, particle accelerators, fusion experiments, and radio/detector
astronomy facilities -- explicitly NOT the qubits, plasmas, or beams themselves. Founder background
was not used to select topics within this lane. Uncertainty is flagged explicitly throughout.

## 1. Frontier state

- **Cryo-CMOS control electronics is a decade-long, still-active research program, not a solved
  commodity.** The TU Delft group's foundational 2016-2020 body of work (L13-004, 005, 017, 019)
  established that scaling beyond a few thousand qubits requires classical control circuitry
  co-located at 4K, and 2024-2025 papers are still pushing the frontier: a 65nm ISSCC-2025 dual-DAC
  manipulator achieving 4.6 microvolt precision at 60mK (L13-022, University of Electronic Science
  and Technology of China) and a 28nm bulk-CMOS 1.08 mW/qubit frequency-division-multiplexed
  readout ASIC presented at the 2025 VLSI Symposium in Kyoto (L13-023, Shanghai Jiao Tong
  University) show China's circuit-design groups are now publishing at the same top-tier venues
  (ISSCC, VLSI Symposium) as the pioneering European teams.
- **Two parallel, government-backed open-source FPGA control platforms (US) are converging toward
  commercialization at the same time.** Fermilab's QICK (L13-001, RSI 2022, 99.93% average gate
  fidelity) and Lawrence Berkeley National Laboratory's QubiC (L13-025) both target the same
  Xilinx RFSoC silicon (L13-045) and the same problem -- open, auditable, low-cost qubit control --
  and QICK has now moved from research tool to a formal DOE-Fermilab-Qblox manufacturing/licensing
  partnership (L13-032, Letter of Intent Nov 2025, CRADA to follow).
- **Cryogenic low-noise-amplifier (LNA) design remains an active, geographically distributed
  research race**, not a mature catalog item: 2020-2026 peer-reviewed cryo-LNA papers were found
  from Russia (L13-012, BJNANO, 6K noise temperature), China (L13-021, Chip journal 2025, GaAs
  MMIC at 4K), and a 2026 multinational paper (L13-013, physica status solidi) -- three
  independent groups still publishing new cryo-LNA architectures in the same 24-month window
  indicates no dominant design has emerged.
- **Facility-scale timing/synchronization is a mature, standards-anchored technology now
  diffusing beyond its CERN origin.** White Rabbit (L13-027) extends IEEE 1588-2019 PTP (L13-026)
  to sub-nanosecond accuracy/picosecond precision and was formalized as an open, multi-vendor
  collaboration only in 2024 -- meaning the underlying physics/engineering is mature but the
  commercial/governance ecosystem around it is still being built.
- **Big-science control-system software (EPICS) is the de facto global standard**, used at over
  100 major facilities including KEKB (Japan), LCLS (US), ITER (per WebSearch; not independently
  verified this session with a fetched primary source), and multiple Chinese facilities
  (BEPCII, SSRF, CSNS, SHINE) -- this is a mature layer, but ITER's own instrumentation-and-control
  system still requires ~161 distinct plant-system integrations across seven domestic agencies
  (L13-030), which is itself a live, unsolved systems-integration problem, not a finished product.
- **Cryogenic cabling/interconnect density is now an explicitly acknowledged scaling bottleneck**,
  with vendor Delft Circuits (Netherlands) projecting a need to grow from 256 to 4,096
  channels-per-loader between 2025 and 2029 (L13-042) -- a 16x density increase in four years,
  which if it fails to materialize would directly constrain how many physical qubits any dilution
  refrigerator can practically wire out.
- **China has made an explicit, high-profile claim of "100% domestic localization" of quantum
  measurement-and-control-system hardware alongside its Zuchongzhi 3.0 result (105 qubits, PRL
  cover paper, March 2025, L13-003)** -- but this specific localization claim, though widely
  repeated in secondary Chinese media, could NOT be confirmed this session even after directly
  fetching two official primary pages (Chinese Academy of Sciences, L13-048; USTC news office,
  L13-049), both of which independently confirmed the qubit-performance metrics but neither of
  which repeated the localization statement. This is flagged as an important unresolved
  contradiction (Section 7).

## 2. Bottlenecks

- **Cryogenic wiring/interconnect I/O density, not qubit count alone, may be the nearer-term
  scaling constraint.** Delft Circuits' own roadmap (L13-042) frames the problem explicitly:
  today's best solution (256 channels/loader) is still an order of magnitude short of what a
  few-thousand-qubit machine would need, and the company's own claimed growth curve (4x every two
  years) has not yet been independently validated by a fielded thousand-plus-qubit system.
- **Cryo-LNA and cryo-CMOS control-IC power budgets remain in tension with dilution-refrigerator
  cooling capacity.** Multiple 2024-2025 papers (L13-013, 021, 023) explicitly optimize for
  milliwatt-per-channel or milliwatt-per-qubit power figures precisely because the 4K and
  mK cooling stages of a dilution refrigerator have hard, limited cooling power -- this is a
  physics-level constraint, not merely an engineering inconvenience, and no single design in this
  session's records has been shown to scale linearly to 1,000+ channels without a fresh
  power-budget redesign.
- **ITER's instrumentation-and-control integration is a documented, structural procurement
  challenge, not just a technical one:** the split between "in-fund" central I&C (procured by the
  ITER Organization) and "in-kind" plant-system I&C (procured separately by seven domestic
  agencies across roughly 161 plant systems) creates an integration burden acknowledged in ITER's
  own technical literature (per WebSearch summary; L13-030 confirms the live tender activity but
  the "161 plant systems" figure itself was not independently fetched this session).
- **Export-control uncertainty is a live, unresolved policy bottleneck for firms and researchers
  moving quantum control hardware or cryogenic-adjacent components internationally.** The
  September 2024 U.S. rule (L13-031, fetched) confirms worldwide export controls on "quantum
  computers, related equipment, components, materials, software, and technology," but this
  session could not independently confirm the specific ECCN classification number, nor
  independently fetch the Federal Register text describing which additional Chinese
  cryogenic-equipment and photonics-supplier entities were added to the Entity List in early 2025
  (both attempts returned HTTP 403/redirect-blocks) -- a documented session-level access gap that
  a verifier should close by fetching the primary Federal Register/BIS text directly.
- **Legislative funding continuity in the US is not fully settled.** The National Quantum
  Initiative Reauthorization Act was introduced in the 118th Congress in December 2024 (L13-029)
  but a further "2026" version (S.3597, 119th Congress) was also found in this session's
  searches -- suggesting the 2024 bill had not been enacted by the time of this scouting session,
  creating funding-continuity uncertainty for any company depending on NQI-linked federal
  contracts through 2026-2027.
- **Korea's public disclosure of control-electronics technical detail is thin relative to its
  stated qubit-scaling ambitions.** KRISS's own 20-qubit cloud-service announcement (L13-040,
  fetched) contains no control-electronics, timing, or hardware-sourcing detail at all, despite a
  stated roadmap to 1,000 qubits by 2032 -- a disclosure gap, not necessarily an activity gap.

## 3. Named buyers and spending signals

- **U.S. Department of Energy** -- $625 million (of which $125M in FY2025) announced Nov 4, 2025
  for five National QIS Research Centers (Brookhaven C2QA, Fermilab SQMS, Argonne Q-NEXT, LBNL
  QSA, Oak Ridge QSC), explicitly including new refrigeration methods and scaling-chip components
  (L13-028, directly fetched).
- **DOE Office of Technology Commercialization + Fermilab + Qblox** -- Nov 18, 2025 Letter of
  Intent (CRADA/full license to follow) to manufacture and supply-chain the QICK quantum-control
  platform domestically in the US (L13-032, directly fetched); per unfetched June 2026 trade
  press, this was subsequently finalized.
- **ITER Organization** -- live open tenders as of this session include a EUR 4-12M liquid/gaseous
  helium supply contract (PIN deadline 24 July 2026) and a CATIA/ENOVIA engineering-software
  maintenance contract (L13-030, directly fetched); China (ASIPP, all 31 magnet feeders, L13-035)
  holds a major national procurement package.
- **Japan's AIST (National Institute of Advanced Industrial Science and Technology), G-QuAT
  center** -- took delivery of the world's first commercially delivered 1,000+-qubit-capable
  quantum control system from Keysight, July 29, 2025 (L13-037, directly fetched); no price
  disclosed.
- **Singapore's National Research Foundation / National Quantum Office** -- S$300 million over
  five years (announced 30 May 2024), with the National Quantum Processor Initiative explicitly
  naming "a targeted grant call for photonics and control electronics components" (L13-036,
  directly fetched) -- the most explicit dated Asian government funding call for control
  electronics specifically found in this lane.
- **Taiwan's ITRI** -- two parallel initiatives: (1) an in-house 4K low-temperature control chip on
  TSMC's 28nm process, verified interfacing with Academia Sinica's qubits (L13-047, connection
  failed on fetch this session, WebSearch-sourced only); (2) a Dec 2025 manufacturing-line
  partnership with SEEQC (US) for Single Flux Quantum superconducting control chips, also
  involving Kinpo (room-temperature electronics) and National Taiwan University (L13-038, directly
  fetched).
- **Korea's KRISS** -- demonstrated a 20-qubit domestically-built quantum-computer cloud service
  (March 2025, L13-040, directly fetched) and separately signed MOUs with Quantum Machines
  (Israel) in June 2023 to advance quantum control systems (L13-039).
- **China's Institute of Plasma Physics (ASIPP, Hefei)** and **University of Science and
  Technology of China** -- ASIPP manufactures all 31 ITER magnet feeders (L13-035); USTC/CAS's
  Zuchongzhi 3.0 105-qubit prototype was independently confirmed by two official press pages
  (L13-048, L13-049) with a widely-repeated but not-independently-verified claim of 100% domestic
  localization of cryogenic-refrigeration and measurement-control hardware.
- **Bluefors (Finland)** -- opened an expanded Syracuse, NY facility in Sept 2024, becoming the
  largest North American dilution-refrigerator producer, enabling first-time US-based
  manufacturing (L13-041, directly fetched); no revenue figures disclosed in the release itself.

## 4. Incumbent map (companies, products, price/share signals)

| Company | Product / Role | Signal |
|---|---|---|
| Keysight Technologies (US) | Quantum Control System (QCS) | First commercial 1,000+-qubit control system, delivered to Japan's AIST G-QuAT, July 2025 (L13-037) |
| Quantum Machines (Israel) | OPX+/OPX1000 control hardware | MOUs with Korea's KRISS/QCILA (L13-039); no public pricing found (L13-046) |
| Zurich Instruments (Switzerland) | SHFQC qubit controller | Up to 6-qubit control/readout in one instrument, scaling to 100+ qubit systems; no public pricing found (search only, not logged as a separate raw-source record) |
| Qblox (Netherlands) | Q1ASM control hardware; now QICK manufacturing partner | DOE/Fermilab CRADA Letter of Intent, Nov 2025 (L13-032) |
| Bluefors (Finland) | Dilution refrigerators | Largest North American producer after Sept 2024 Syracuse expansion (L13-041) |
| Delft Circuits (Netherlands) | Cri/oFlex cryogenic cabling | Roadmap: 256 to 4,096 channels/loader, 2025-2029 (L13-042, vendor claim) |
| AMD/Xilinx (US) | Zynq UltraScale+ RFSoC (RF-ADC/DAC silicon) | Underlies QICK, QubiC, and multiple commercial control systems (L13-045) |
| SEEQC (US) | Single Flux Quantum (SFQ) superconducting control chips | Taiwan (ITRI) manufacturing-line partnership, Dec 2025 (L13-038) |
| QuEL, Inc. (Japan, spun out of Osaka University) | Quantum control devices | Deployed at RIKEN, March 2023, "already being sold" (L13-044) |
| Origin Quantum / 本源量子 (China) | OriginQ Quantum AIO measurement-control system | China's first domestic integrated control system; product-detail fetch attempt returned no substantive content this session (L13-043) |
| ITRI (Taiwan) | 4K low-temperature control chip (TSMC 28nm) | ~40% control-instrument size reduction claimed; verified against Academia Sinica qubits (L13-047, not independently fetched) |
| CERN / RD53 Collaboration (multinational) | RD53 pixel-readout ICs for ATLAS/CMS HL-LHC | 1 Grad radiation tolerance, 5.12 Gbit/s/chip readout, production chips submitted 2023 (L13-009, L13-052) |

**Pricing signals found:** essentially no vendor in this lane (Quantum Machines, Zurich
Instruments, Qblox, Delft Circuits, Origin Quantum, Bluefors) publicly discloses unit or system
pricing. The only pricing figure found this session is a third-party estimate, not vendor-quoted:
full entry-level cryogenic quantum-computing systems bundling Qblox- or Quantum-Machines-class
control electronics are estimated at roughly $1-3M system cost plus $200-400K/year operations
(L13-046, notes field; unverified secondary estimate). This mirrors the pricing-opacity pattern
documented in this project's L06 and L12 lane briefs.

## 5. 2026-2031 triggers

- **US:** the DOE-Fermilab-Qblox QICK manufacturing partnership (L13-032) moves from Letter of
  Intent (Nov 2025) toward a finalized CRADA/license through 2026, aiming to establish a domestic
  supply chain for open-source quantum control hardware; the $625M DOE QIS Research Center funding
  (L13-028) continues through the FY2025-onward period; the National Quantum Initiative
  Reauthorization Act's enactment timeline remains unresolved as of this session (L13-029).
- **China:** continued rapid-cadence publication at top circuit-design venues (ISSCC 2025,
  L13-022; VLSI Symposium 2025, L13-023) suggests China's cryo-CMOS/control-IC research capacity
  will keep converging toward parity with the pioneering Dutch program through 2026-2028; ASIPP's
  ITER magnet-feeder delivery (L13-035) and the widely-claimed (but not independently confirmed)
  domestic-localization narrative around Zuchongzhi 3.0 (L13-003, 048, 049) both point to a
  deliberate 2026-2031 domestic-supply-chain-independence push.
- **Japan:** Keysight's AIST G-QuAT delivery (L13-037) and QuEL Inc.'s RIKEN deployment (L13-044)
  both point to Japan positioning itself as an early adopter/testbed for both foreign-vendor and
  domestic-spinout control-hardware approaches simultaneously through 2026-2028.
- **Korea:** KRISS's stated roadmap (50 qubits by 2026, 1,000 qubits by 2032, L13-040) is a
  concrete, dated scaling trigger, though the underlying control-electronics supply chain remains
  under-disclosed in English- and Korean-language sources found this session -- a follow-up
  scouting priority.
- **Taiwan:** the SEEQC-ITRI SFQ manufacturing-line partnership (L13-038) and ITRI's own in-house
  28nm cryo-control-chip work (L13-047) both point to Taiwan explicitly leveraging its
  semiconductor-manufacturing base to enter quantum-control-electronics manufacturing during
  2026-2028, a distinct strategy from Japan's or Korea's adopter-first approach.
- **Singapore:** the National Quantum Processor Initiative's control-electronics-specific grant
  call (L13-036) is a live, near-term (2024-2029, within the S$300M/5-year window) funding trigger
  explicitly naming this lane's technology.
- **Standards/policy:** IEEE 1588-2019 (L13-026) and the White Rabbit open-hardware collaboration's
  2024 formal launch (L13-027) suggest a 2026-2031 window in which facility-timing technology
  standardizes and commercializes further beyond its CERN/GSI origin; US export-control scope
  (L13-031) remains only partially confirmed and is a live compliance trigger for any company
  selling control hardware, cryogenic components, or related software internationally.

## 6. US vs. Asia differences

- **US** evidence in this lane is dominated by (a) two competing but converging DOE-national-lab
  open-source FPGA control platforms (QICK/Fermilab, QubiC/LBNL) now both moving toward or already
  achieving commercial licensing, and (b) large, dated, quantified federal funding ($625M DOE QIS
  centers) paired with unresolved legislative-continuity risk (NQI Reauthorization Act status).
  The US approach favors open-source-then-commercialize, government-funded national-lab platforms
  competing directly with venture-backed vendors (Quantum Machines, Zurich Instruments, Keysight)
  in the same market.
- **China** evidence shows a deliberate, high-profile domestic-sovereignty narrative (Zuchongzhi
  3.0's localization claim) paired with genuinely fast-improving indigenous circuit-design
  capability now publishing at top international venues (ISSCC, VLSI Symposium, JSSC) --
  structurally different from the L06/L12 lanes' China narratives (displacing a foreign incumbent,
  or a price war within an already-dominant domestic industry): here, China is simultaneously
  claiming supply-chain independence AND publishing internationally, a combination that should be
  read cautiously until the specific "100% domestic localization" claim (unconfirmed this session,
  Section 7) is independently verified.
- **Japan** evidence shows a distinctive "domestic-startup-plus-foreign-vendor" pattern not seen
  elsewhere: RIKEN adopted a homegrown Osaka University spinout (QuEL Inc.) for its own national
  quantum computer, while AIST simultaneously became the first customer anywhere for Keysight's
  1,000+-qubit foreign-vendor control system -- Japan is hedging between indigenous and imported
  control-hardware strategies rather than committing exclusively to either.
- **Korea** evidence is real (KRISS's 20-qubit domestic cloud service, dated scaling roadmap to
  2032) but the control-electronics supply chain specifically remains a disclosure gap: no
  Korean-language technical source on control-electronics hardware was independently confirmed
  this session, despite Korea's large semiconductor-manufacturing base that should, in principle,
  be well-positioned to build this hardware domestically.
- **Taiwan** evidence uniquely combines (a) leveraging existing world-class semiconductor
  fabrication (TSMC 28nm process) for an in-house ITRI-developed cryo-control chip, and (b)
  simultaneously hosting a foreign company's (SEEQC, US) manufacturing line for a different
  superconducting-control-chip technology (SFQ) -- Taiwan appears to be positioning itself as a
  neutral, semiconductor-capability-driven manufacturing hub for multiple competing quantum-control
  chip architectures rather than backing a single indigenous product line.
- **Singapore** evidence (S$300M National Quantum Strategy, explicit control-electronics grant
  call) is the most explicitly funding-programmatic of any Asian market in this lane -- Singapore's
  angle is government-directed ecosystem-building via targeted grant calls rather than either a
  national champion (China, Japan) or semiconductor-fab leverage (Taiwan) strategy.
## 7. Unresolved contradictions

1. **China's widely-repeated claim that Zuchongzhi 3.0 achieved "100% domestic localization"
   (国产化) of extreme cryogenic refrigeration and quantum measurement-control-system core
   components could not be confirmed this session, even after directly fetching two official
   primary pages** (Chinese Academy of Sciences press release, L13-048; USTC news office article,
   L13-049) -- both independently confirmed the qubit-performance metrics (105 qubits, 99.90%/
   99.62%/99.13% fidelities) but neither repeated the localization statement found in an unfetched
   secondary search snippet (ncsti.gov.cn). This is a load-bearing claim for any idea premised on
   China's domestic quantum-control-hardware supply chain being fully independent of foreign
   components, and a verifier should locate and fetch the original source of the localization
   claim before it is used in any downstream analysis.
2. **The National Quantum Initiative Reauthorization Act's status is ambiguous as of this
   session's 2026-07-12 reference date.** A 118th Congress version (S.5411/H.R.6213, introduced
   Dec 2024, L13-029) and a distinct 119th Congress "2026" version (S.3597, found via WebSearch but
   not logged as a separate record) both exist -- suggesting the 2024 bill was not enacted before
   this session, with a fresh reauthorization effort underway. A verifier should determine current
   enactment status directly from Congress.gov (which returned HTTP 403 to this session's fetch
   attempts).
3. **U.S. export-control scope for quantum-computing-adjacent components is only partially
   confirmed.** The fetched quantum.gov page (L13-031) confirms a September 2024 rule imposing
   worldwide export controls on quantum computers and related equipment, but the specific ECCN
   classification number (reported elsewhere as a proposed "4A006") and the scope/dates of
   additional 2025 Entity List additions targeting Chinese cryogenic-equipment and photonics
   suppliers were not independently fetched this session (Federal Register and Commerce.gov both
   returned access errors) -- treat these specific details as unconfirmed pending direct fetch.
4. **Keysight's "world's first 1,000-qubit quantum control system" claim (L13-037) is sourced
   from a financial-news aggregator's republication of Keysight's own press release, not
   Keysight's primary press page nor an independent government/customer confirmation** -- AIST's
   own confirmation of the delivery and its stated qubit-count capability was not independently
   located this session. Treat the specific "1,000+ qubit" figure as a vendor claim pending
   independent AIST-side confirmation.
5. **Origin Quantum's specific "本源天机4.0" (4th-generation measurement-and-control system)
   product claims could not be substantiated this session** -- the only content-bearing
   information about Origin Quantum's control-system products comes from WebSearch snippets, not
   a successfully fetched page; the one direct fetch attempt returned only site navigation with no
   article content. Any downstream claim about specific channel counts, fidelity, or performance
   figures for Origin Quantum's control hardware should be treated as unconfirmed.
6. **Delft Circuits' cryogenic-cabling density roadmap (256 to 4,096 channels/loader, 2025-2029,
   L13-042) is entirely a vendor-authored, self-reported roadmap with no independent third-party
   validation found this session** -- treat the specific "4x every two years" growth-rate claim as
   a vendor projection, not a demonstrated or independently audited trajectory, consistent with
   this project's general claim-discipline rule that vendor claims are never independent
   validation.

## 8. Opportunity-shaped pain statements (NOT startup pitches)

1. **Pain:** Cryogenic wiring/interconnect channel density (256 channels/loader today, per one
   vendor) is roughly an order of magnitude short of what thousand-plus-qubit machines will need,
   and the only publicly disclosed scaling roadmap is a single vendor's self-reported,
   unindependently-verified projection. **Who pays:** superconducting-qubit quantum-computer
   builders (any vendor scaling past a few hundred physical qubits) and their component-sourcing
   teams. **Evidence:** L13-042.
2. **Pain:** Cryo-CMOS and cryo-LNA control-electronics power budgets remain in direct tension with
   dilution-refrigerator cooling-power limits, and multiple independent research groups (Russia,
   China, a 2026 multinational team) are still publishing competing point solutions rather than a
   converged design, three-plus years after the underlying problem was first formalized. **Who
   pays:** quantum-computer builders and their cryogenic-supply-chain partners bearing continued
   custom-IC R&D risk rather than being able to buy an interchangeable commodity component.
   **Evidence:** L13-004, 005, 012, 013, 021, 023.
3. **Pain:** ITER's instrumentation-and-control system requires integrating roughly 161 separately
   procured plant systems across seven domestic agencies under a split in-fund/in-kind procurement
   model, creating a documented systems-integration burden distinct from any single component's
   technical difficulty. **Who pays:** the ITER Organization (integration-schedule risk) and its
   domestic agencies/suppliers (interface-compliance risk). **Evidence:** L13-030.
4. **Pain:** U.S. export-control scope for quantum-computing-adjacent classical hardware
   (cryogenic equipment, control electronics, photonics) is only partially disclosed in
   easily-accessible primary sources, creating real compliance uncertainty for any company selling
   across borders in this lane -- this session could not even independently confirm the specific
   ECCN number or the full current Entity List scope from primary government sources. **Who
   pays:** any control-hardware, cryostat, or cryogenic-component vendor with international
   customers or supply chains, plus their legal/export-compliance functions. **Evidence:** L13-031.
5. **Pain:** Essentially no vendor in this lane discloses unit or system pricing in open sources
   (Quantum Machines, Zurich Instruments, Qblox, Delft Circuits, Origin Quantum, Bluefors all
   omit public pricing), forcing every buyer and analyst to rely on RFQs or third-party estimates
   rather than transparent price discovery -- the same opacity pattern documented in this
   project's L06 and L12 lane briefs. **Who pays:** N/A directly (a research/due-diligence
   constraint rather than a customer pain), but it is a real burden for any founder or buyer
   entering this lane. **Evidence:** L13-041, 042, 043, 046.
6. **Pain:** Korea's and India's public disclosure of quantum/facility control-electronics
   technical and commercial detail is markedly thinner than China's, Japan's, Taiwan's, or
   Singapore's in this lane, despite both countries having (Korea: semiconductor manufacturing;
   India: a large synchrotron/accelerator base) the underlying industrial capability to
   participate -- a coverage gap that may reflect either genuinely less activity or simply less
   English/searchable-language disclosure. **Who pays:** unclear from this session's evidence; a
   coverage gap, not a confirmed absence of activity. **Evidence:** L13-040, 051 (present but
   thin); absence otherwise noted in Section 6.
7. **Pain:** China's own official communications about its Zuchongzhi 3.0 milestone, when
   directly fetched from two separate primary institutional sources, did not substantiate the
   widely-circulated "100% domestic localization of cryogenic refrigeration and control-system
   hardware" claim -- creating real uncertainty about whether China's superconducting-qubit
   control-electronics supply chain is actually independent of foreign components, a load-bearing
   fact for any competitive or export-control analysis. **Who pays:** any analyst or company making
   strategic decisions based on assumed China supply-chain independence in this specific hardware
   category. **Evidence:** L13-003, 048, 049.
8. **Pain:** Legislative continuity for U.S. federal quantum funding is not fully settled --
   evidence of both a 2024 and a apparently-still-pending 2026 version of the National Quantum
   Initiative Reauthorization Act suggests multi-year federal funding for this lane's US national-
   lab-adjacent demand signals (DOE QIS centers, Fermilab-Qblox CRADA) rests on a legislative
   vehicle whose enactment timeline is not yet confirmed. **Who pays:** national laboratories and
   their commercialization partners (e.g. Qblox) whose funding/program continuity depends partly
   on this reauthorization. **Evidence:** L13-028, 029, 032.
9. **Pain:** Taiwan is simultaneously hosting two structurally different quantum-control-chip
   manufacturing efforts (ITRI's in-house 4K CMOS control chip vs. the SEEQC superconducting SFQ
   partnership) without a clear public accounting of how these relate strategically or compete for
   the same TSMC/ITRI fabrication capacity. **Who pays:** ITRI and its manufacturing partners
   (capacity-allocation and strategic-focus risk), and potential new entrants trying to identify
   which architecture Taiwan is actually betting on. **Evidence:** L13-038, 047.
10. **Pain:** Facility-timing technology (White Rabbit/IEEE 1588) is technically mature but
    commercially/governance-wise still forming -- the White Rabbit Collaboration was only formally
    launched in 2024, more than a decade after the underlying CERN/GSI engineering work began,
    meaning multi-vendor interoperability, long-term support, and commercial-supply-chain
    resilience for facility-timing hardware are all still being actively established rather than
    settled. **Who pays:** every big-science facility (accelerators, telescopes, fusion
    experiments) depending on White-Rabbit-class timing for procurement and long-term maintenance
    planning. **Evidence:** L13-026, 027.
11. **Pain:** Japan is the only geography in this session's evidence base clearly running both an
    indigenous-startup strategy (QuEL Inc./RIKEN) and a foreign-vendor-adoption strategy (Keysight/
    AIST) at the same time for the same underlying control-hardware problem, without any found
    source explaining Japan's institutional rationale for hedging across both approaches
    simultaneously rather than converging on one. **Who pays:** Japanese national labs (AIST,
    RIKEN) bearing the cost/complexity of maintaining parallel control-hardware ecosystems; a
    potential whitespace for a company that can serve both segments. **Evidence:** L13-037, 044.

## Methodology notes and gaps for the verifier

- 52 candidate records collected (within the 45-55 target range). 25 are academic peer-reviewed
  candidates, meeting the wave-4 floor of at least 25. Overall T1 ratio across the full 52-record
  set is 40/52 = 76.9%, above the mission's >=70% floor but below the wave-4 aspirational >=85%
  target. As in this project's L06 and L12 lane briefs, the shortfall is structural: satisfying
  the mix requirement for "incumbents/products/prices" coverage necessarily pulls in vendor
  press releases and datasheets (T2), and several strong T1-eligible academic papers (L13-009,
  010, 011, 013, 014, 015, 017-025) were found with confirmed or highly-plausible peer-reviewed
  venues and DOIs but could not be independently fetched this session (IOPscience and ScienceDirect
  returned HTTP 403/paywall errors repeatedly). A follow-up verifier wave successfully fetching
  those canonical publisher pages directly would likely both confirm several currently-uncertain
  DOIs and would not change the tier count (they are already counted as T1) but would substantially
  increase confidence and reduce the number of "not independently fetched" notes.
- T3 count: 1 record (L13-050, a market-research aggregator report), well within the 2-3 record
  cap. [Update 2026-07-13: L13-050 was quarantined by the P2A India-origin audit and no longer
  counts; the lane T3 count is now 0.] No arXiv/preprint/thesis/slide-deck was included as a record; several were explicitly
  identified during search and excluded per the discovery-only rule (e.g. CEPC clock-synchronization
  arXiv paper 2606.11590, CO-QLink arXiv 2511.22920, Qibosoq arXiv 2310.05851).
- Demand-primary count: 12 records carry a non-"none" `demand_evidence_type` (L13-028, 030, 032,
  033, 034, 035, 036, 037, 038, 039, 040, 044), spanning official project awards, procurement
  awards, a buyer tender, and direct customer documentation across US, EU, Japan, Taiwan, Korea,
  Singapore, India, and China.
- Government/national-lab/standards-body count: 15 records (L13-026 standard; L13-027, 032, 035,
  048, 049, 052 national_lab; L13-028, 029, 031, 033, 036, 051 government; L13-030, 034 buyer_
  procurement), exceeding a reasonable floor for this mix category.
- Asian-market coverage: 22 records carry an Asia-relevant geography tag (China 11, Japan 3,
  Korea 3, Taiwan 2, Singapore 1, India 2, with some overlap), far exceeding the >=8 floor; 7
  records are local-language primary sources (zh x5: L13-016, 035, 043, 048, 049; ja x1: L13-044;
  plus L13-047 zh trade press though not independently fetched), exceeding the >=3 floor with room
  to spare, and 5 of the 7 were independently fetched in full this session (L13-016, 043 [fetch
  attempt failed to return content], 044, 048, 049).
- **Two records (L13-043, L13-047) had WebFetch attempts that failed to return usable content**
  (an empty-navigation redirect chain, and a connection reset, respectively) -- flagged explicitly
  so a verifier does not mistake the "fetched: false" / partial-fetch status for a lack of effort;
  both should be retried with a different fetch strategy (e.g. targeting a specific product/news
  sub-page directly, or via an archived/cached version) before acceptance is decided.
- **Weakest coverage / follow-up priorities for a future scout wave:** (1) Korea -- no
  Korean-language technical source on control-electronics hardware specifically (as opposed to
  qubit/materials research) was found or fetched this session, despite Korea's large
  semiconductor-manufacturing base; (2) India -- zero quantum-computing-specific control-
  electronics signal found (only fusion/accelerator-facility hardware), a notable gap relative to
  every other geography in this lane; (3) direct fetch of IOPscience (JINST, Nuclear Fusion) and
  ScienceDirect (Fusion Engineering and Design, Nuclear Instruments and Methods) canonical pages
  for L13-009, 010, 011, 015, all of which returned HTTP 403 or were not attempted directly this
  session; (4) direct fetch of the Federal Register / BIS primary text on the 2025 Entity List
  additions and the ECCN 4A006 rule, to resolve Contradiction 3; (5) direct fetch of Congress.gov
  or an alternative primary source to resolve the National Quantum Initiative Reauthorization Act's
  current enactment status (Contradiction 2); (6) a content-bearing fetch of an Origin Quantum
  product/news page to substantiate or correct the "本源天机4.0" claims (Contradiction 5); (7)
  locating and fetching the original ncsti.gov.cn (or equivalent primary) source of the "100%
  domestic localization" claim for Zuchongzhi 3.0, to resolve Contradiction 1.

## P2A origin-audit repair (2026-07-13)

- removed IDs: L13-034, L13-050, L13-051
- removed/trimmed claims: trimmed the ITER Organization named-buyer bullet (Section 3) to remove
  the India/Institute for Plasma Research cryostat clause (L13-034), keeping the eligible China/
  ASIPP clause; trimmed the Bluefors incumbent-map row (Section 4) to remove the "~34%+ global
  share" market-share estimate sourced solely to L13-050, keeping the eligible Syracuse-facility
  fact; deleted the India 2026-2031 trigger bullet (Section 5, ITER cryostat + RRCAT) sourced
  solely to L13-034/051; deleted the India paragraph in "US vs. Asia differences" (Section 6),
  same underlying evidence; deleted pain statement 11 (Section 8, India fusion/accelerator
  presence) sourced solely to L13-034/051 and renumbered the following item to 11. No eligible
  India-sourced control-electronics or big-science-facility claim remained after removal; any
  future India evidence in this lane must come from an eligible non-India source and remains
  excluded from demand/market/geography scoring per the binding geography-scope rule regardless.
