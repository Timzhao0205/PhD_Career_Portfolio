# L07 — Vacuum, cryogenic, leak-tight, and ultra-clean process hardware

Lane scout brief. No startup ideas are proposed here; this is evidence collection only. All
citations refer to record IDs in `L07_raw_sources.json`. Uncertainty is flagged explicitly where
the underlying evidence is a single source, a search-index snippet rather than a direct fetch, a
vendor claim, or a consultancy estimate.

## Frontier state

Vacuum/cryogenic/ultra-clean hardware is a mature engineering discipline experiencing a demand
re-shape rather than a technology discontinuity. Four demand fronts are pulling on the same
supplier base at once: (1) semiconductor fabs pushing sub-3nm etch/deposition processes that need
higher-flow, higher-reliability dry vacuum pumps and tighter ultra-high-purity (UHP) gas/water
delivery (L07-030, L07-031, L07-039, L07-049, L07-051, L07-052); (2) big-science facilities
(ITER, JT-60SA, HEPS) procuring vacuum vessels, cryostats, and pressure-suppression hardware at
hundred-million-dollar-class scale (L07-033, L07-034, L07-041 through L07-045); (3) quantum
computing scale-up pushing dilution-refrigerator cooling power and vibration performance well
beyond historical scientific-instrument norms (L07-014 through L07-017); and (4) continued
incremental gains in the decades-old core physics of UHV/XHV — outgassing control, NEG coatings,
magnetic-bearing turbomolecular pumps, and helium leak detection (L07-001 through L07-013,
L07-023, L07-024). Pharma freeze-drying (lyophilization) is a fifth, smaller-but-real vacuum-
contamination-control demand front distinct from semiconductor/accelerator vacuum (L07-020,
L07-021). No single breakthrough physics result defines this lane; the pattern is steady
materials/engineering optimization (outgassing, magnetic bearings, vibration isolation) layered
under fast-growing, well-capitalized demand (AI-driven fab capex, fusion/big-science builds,
quantum computing).

## Bottlenecks

- **Turbomolecular pump bearing reliability and vibration remain an active engineering problem
  even after 30+ years of magnetic-bearing development.** Comparative reliability work dates to
  1988-1990 (L07-013, L07-010) but current research still addresses shock-induced rotor
  instability in high-speed maglev turbopumps (L07-012, 2023) and large-scale active-magnetic-
  bearing pump design (L07-011, 2016) — the problem has not been "solved," only incrementally
  improved.
- **Hydrogen outgassing control requires a narrow, energy-intensive bakeout/heat-treatment
  process window.** A 250°C, 30-hour bakeout is reported to cut hydrogen outgassing more than
  70,000x versus untreated 300-series stainless steel, but this is a capital- and time-intensive
  step that must be built into every UHV chamber's fabrication schedule (L07-009, L07-007,
  L07-008).
- **XHV pressure measurement below ~10^-10 Pa still fights the same two physical limits
  identified decades ago** — the X-ray limit and electron-stimulated-desorption ions — with newer
  approaches (CNT-cathode ionization gauges, laser-based ionization) still described as active
  research rather than settled commercial technology (L07-002, L07-003, L07-004).
- **Dilution-refrigerator cooling power and physical footprint are a hard constraint on quantum-
  computer scaling.** Conventional units deliver only tens of µW at 10-20 mK; recent primary
  research reports pushing to ~2 mW near 100 mK and ultra-low-vibration split designs, but this is
  presented as a current research frontier, not an already-solved commercial capability (L07-016,
  L07-015, L07-014, L07-017).
- **UHP gas/water delivery for leading-edge fabs is a fast-growing, high-capex-intensity cost
  center that is itself becoming a bottleneck to new fab ramp.** A single ultra-pure-water EPC
  contract package at one fab phase runs into the tens of billions of KRW (L07-046, L07-047), and
  gas-delivery-subsystem suppliers report customer concentration above 75% in just two OEM
  customers (L07-049) — a fragile, thin supplier base relative to fab-expansion pace.
- **Vacuum-pump vendor market-size estimates disagree by nearly 2x across consultancies with no
  disclosed bottom-up methodology** (L07-038), undermining capital-planning confidence for new
  entrants or investors sizing this space.
- **Cryostat/vacuum-vessel manufacturing for big science remains a single-supplier-chain
  dependency in several countries** — e.g., India's ITER cryostat work is effectively sole-sourced
  through INOXCVA/L&T (L07-033, L07-048), and China's HEPS insertion-device vacuum chambers must
  be sourced from China-registered manufacturers only, by tender rule (L07-045).

## Named buyers and spending signals

- **ITER Organization** — actively tendering/awarding vacuum-adjacent hardware in 2025-2026:
  a €4M-€12M liquid/gaseous helium supply contract (ongoing, L07-041); Vacuum Vessel Pressure
  Suppression System (VVPSS) instrumentation and valves contracts, each in the €300K-€2M range,
  both awarded in 2025 (L07-042, L07-043); and a VVPSS cooler-condenser contract (up to €400K)
  awarded to Spain's MAP Industrial Projects, S.L. (L07-044).
- **India's Department of Atomic Energy / Institute for Plasma Research (ITER-India)** — delivered
  the 3,850-tonne ITER cryostat (completed 2022, manufactured by L&T in Gujarat) as its flagship
  procurement package (L07-033), and INOX India (INOXCVA) separately booked a ₹145 crore
  (~USD 17M) FY25 repair order for the ITER Cryostat Thermal Shield (L07-048).
- **Japan's JAEA/QST and the EU's Fusion for Energy** — split JT-60SA vacuum-vessel (Toshiba-built,
  10 sectors, ~17 tonnes each) and cryostat procurement under the Japan-EU Broader Approach
  Agreement (L07-034).
- **China's Institute of High Energy Physics (IHEP)** — tendered HEPS storage-ring insertion-
  device vacuum chambers and support frames (RMB 2.6M, China-manufacturer-only bid rule,
  L07-045); HEPS passed process acceptance in October 2025 per background reporting.
- **Samsung E&A / Samsung Electronics / DB HiTek (Korea)** — commissioned Hansung Clean Tech for
  a KRW 22.18B ultra-pure-water facility at Samsung's Pyeongtaek P5 fab (L07-046) and a further
  combined ~KRW 31B water-treatment EPC package with DB HiTek (L07-047), both explicitly tied to
  AI/HBM-driven fab investment.
- **TSMC** — signed a joint-development agreement with Ebara for high-end etch-process dry vacuum
  pumps targeting sub-3nm nodes; Ebara is separately investing USD 200M to upgrade Korea and
  Taiwan supply hubs for localized fab delivery (L07-051).
- **Lam Research and Applied Materials** — together account for 76% of Ichor Holdings' FY2025
  gas/fluid-delivery-subsystem sales ($947.7M total revenue), the clearest disclosed customer-
  concentration figure found in this lane (L07-049).
- **NASA** — operates and funds the Space Environments Complex at the Neil Armstrong Test Facility,
  the world's largest space-simulation/EMI vacuum chamber, as a standing capital asset for
  spacecraft qualification (L07-035); NASA also authored a primary technical-uncertainty framework
  for helium leak detection used across its qualification programs (L07-032).
- **US DOD Missile Defense Agency** — funded Sierra Lobo, Inc. (SBIR Phase II, $495,907, 2003) for
  densified-cryogen storage with integrated leak/vapor sensing — an older but directly-fetched
  government award record illustrating intermittent rather than steady niche funding (L07-054).

## Incumbent map (companies, products, price signals)

| Company | Country | Product | Signal |
|---|---|---|---|
| ULVAC | JP | Vacuum/thin-film deposition & sputtering equipment | FY2025 vacuum-application orders ¥521.37B, backlog ¥174.1B (L07-052) |
| Ebara Corporation | JP | Dry vacuum pumps (new EV-H model), plasma abatement (ELF) | TSMC joint development for sub-3nm etch pumps; $200M Korea/Taiwan hub investment (L07-051) |
| MKS Inc. | US | Vacuum Solutions Division (pumps, gauges, subsystems) | Total FY2025 revenue $3,931M (+9.6% YoY); semiconductor revenue $432M in Q2 2025 alone (L07-050) |
| Ichor Holdings | US | Gas/fluid delivery subsystems for semiconductor capital equipment | FY2025 revenue $947.7M; Lam Research + Applied Materials = 76% of sales (L07-049) |
| INFICON | CH | Leak detection, gas analysis, vacuum gauges ("Semi & Vacuum Coating" segment) | FY2025 sales $673.7M; APAC +19.2% to ~$169M, Americas -12.4% to ~$156M (L07-053) |
| Edwards Vacuum (Atlas Copco) | GB/SE | Dry vacuum pumps, abatement | 2024 revenue ~$2.10B per market-report aggregation (not independently fetched); part of "top 6" holding ~62% of global semiconductor vacuum-pump revenue (L07-039) |
| Pfeiffer Vacuum | DE | Turbo pumps, backing pumps, leak detection | Named among top-6 global vendors (L07-039); revenue figures found this session were consultancy-aggregated only, not independently fetched |
| Busch Vacuum Solutions | DE | Dry/oil-sealed vacuum pumps | Named among top-6 global vendors; "entrenched OEM relationships" per market aggregation (L07-039) |
| INOX India (INOXCVA) | IN | Cryogenic tanks, ITER cryostat/cryoline systems | Largest Indian cryogenic-tank exporter; one of <10 companies globally certified for full cryogenic-equipment range; ₹145 crore FY25 ITER repeat order (L07-040, L07-048) |
| SAES Getters | IT | NEG-coating solutions (IntegraTorr) for accelerators | Vendor claim; commercializes the same NEG-coating physics studied in L07-001 |
| Kurt J. Lesker Company | US | CF flanges, feedthroughs, vacuum components | 1,200+ feedthrough variants catalogued; pricing is quote-on-request, not list-priced (L07-036) |
| Forward Science Corp. | TW | AI-monitored ("V-pro") vacuum pumps | Reported new orders from PSMC and Macronix (2025); order size not disclosed (paywalled trade press, not independently verified this session) |

Price signals are thin and mostly quote-on-request in this lane (L07-036). The clearest hard
dollar figures found are project/contract values (ITER tender cost bands L07-041 to L07-044; Korean
water-treatment EPC contracts L07-046/L07-047; INOX India's ₹145 crore ITER order L07-048) rather
than unit prices for pumps, gauges, or feedthroughs — consistent with an industry that sells
mostly through negotiated system contracts, not catalog list price.

## 2026–2031 triggers

- **2026**: ITER liquid/gaseous helium supply contract execution and further VVPSS-related
  procurement expected to continue (L07-041 through L07-044); Samsung Pyeongtaek P5 Phase 1
  ultra-pure-water facility construction (L07-046) scheduled to run through July 2027.
- **2026-2027 (ongoing)**: EBARA's new EV-H dry vacuum pump and ELF plasma abatement system enter
  mass production/sequential release, timed to sub-3nm-node fab ramps (L07-051).
- **2027-2028**: Ichor Holdings' 2025 "Consolidation Restructuring Plan" (per its FY2025 10-K,
  L07-049) is a dated internal capacity-realignment response to semiconductor-cycle volatility —
  a signal that even top-tier gas-delivery suppliers see near-term demand as uncertain despite
  headline AI-driven fab capex growth.
- **2030-2031**: Consultancy-estimated market-size horizon for both the general vacuum-pump market
  (USD 7.56B to 10.81B, or alternative estimates of USD 6.5B to 8.4B / USD 5.73B(2022) to
  8.75B(2030), depending on source, L07-038) and the semiconductor dry-vacuum-pump sub-market
  (USD 1.46B(2024) to 3.12B(2033), L07-039) — flagged as unreconciled consultancy estimates, not
  independently triangulated in this pass.
- **Ongoing/undated**: China's HEPS program (vacuum-closed-loop completed 2024, process
  acceptance passed October 2025 per background search) suggests further Chinese synchrotron/
  accelerator vacuum-hardware tenders are likely but no specific dated follow-on tender was found
  in this record set (L07-045).

## US vs Asia differences

- **Fab-side ultra-clean demand is currently most visibly dated and dollar-quantified in Korea**,
  where Samsung E&A/Samsung Electronics/DB HiTek water-treatment and ultra-pure-water contracts
  with Hansung Clean Tech are disclosed as discrete, KRW-denominated regulatory filings with
  explicit AI/HBM-demand framing (L07-046, L07-047) — a more transparent near-term demand signal
  than anything found for US fabs in this pass (US demand evidence here is mostly OEM-level,
  e.g., Ichor's Lam/Applied Materials customer concentration, L07-049, rather than fab-owner-level
  contract disclosure).
- **Japan and Taiwan anchor the incumbent supply side, not just the demand side.** ULVAC (JP) and
  Ebara (JP) are named, audited-filing-backed vacuum-equipment incumbents (L07-051, L07-052), and
  Ebara is actively investing in Taiwan/Korea supply-hub capacity specifically to serve TSMC and
  regional customers locally (L07-051) — the opposite direction of a "US demand, Asia supply"
  simplification; Asia is both the largest incumbent producer and a fast-growing buyer.
- **Big-science vacuum-hardware procurement is nationally protectionist in China, internationally
  distributed in Japan/EU/India.** China's HEPS tender explicitly restricts bidding to China-
  registered manufacturers (L07-045), while JT-60SA (Japan/EU) and ITER (global, India delivering
  the cryostat) show cross-border procurement as the norm (L07-033, L07-034, L07-041 to L07-044).
- **US strength in this pass is concentrated in components/subsystems and government facilities**
  (Ichor gas-delivery subsystems, MKS vacuum solutions, Kurt J. Lesker components, NASA space-
  simulation facilities and leak-detection methodology, L07-049, L07-050, L07-036, L07-032,
  L07-035) rather than in large finished systems (fab tools, cryostats) — those finished-system
  wins in this record set skew Japanese (ULVAC, Ebara) or activity-specific (INOXCVA in India for
  cryogenics).
- **Export-control friction is a live, dated (FY2025) financial fact, not speculation.** INFICON's
  own FY2025 results show Americas revenue falling 12.4% while Asia-Pacific rose 19.2%, explicitly
  attributed to US trade-restriction impact versus China/AI-driven re-acceleration (L07-053) — a
  concrete US-vs-Asia divergence data point from an audited-adjacent earnings disclosure.

## Unresolved contradictions

- **Vacuum-pump and semiconductor-dry-vacuum-pump market-size estimates disagree by up to ~2x
  across consultancy sources with no disclosed bottom-up methodology** (L07-038, L07-039) —
  flagged as unverified and not usable for capital-allocation decisions without independent
  triangulation.
- **Is EBARA's $200M Korea/Taiwan investment and TSMC joint-development claim a confirmed near-
  term revenue driver or an aspirational press-release framing?** The only source for this claim
  is EBARA's own press release, aggregated via search snippet; direct WebFetch of the release was
  blocked (HTTP 403), so the figure could not be cross-checked against EBARA's investor-relations
  disclosures this session (L07-051).
- **INOX India's ₹145 crore ITER Cryostat Thermal Shield repair-order figure could not be traced
  to a specific primary-document page this session** — it appears in trade-press aggregation of
  INOX India's own disclosures, but the underlying FY2025-26 annual report PDF was not
  independently searched line-by-line to confirm the figure (L07-048).
- **Is the dilution-refrigerator scaling bottleneck (µW-to-mW cooling power at ~100 mK) close to
  resolved or still fundamentally limiting?** Recent primary papers report ~2 mW cooling power
  near 100 mK as a new achievement (L07-016) alongside separate ultra-low-vibration split-cryostat
  work (L07-015), but no source in this record set states a roadmap or timeline for when
  quantum-computer-scale (many-qubit, rack-of-cryostats) cooling-power requirements will be
  routinely met by commercial (rather than single-lab-demonstrated) systems.
- **Two possibly-overlapping Hansung Clean Tech/Samsung contract disclosures were found**
  (a ~KRW 8B Samsung-only order and a ~KRW 31B combined Samsung+DB HiTek order, both reported in
  similar date ranges) — only the larger, more clearly sourced KRW 31B figure was retained
  (L07-047), but the verifier should check whether these are the same underlying disclosure
  described inconsistently by different news aggregators, or genuinely separate contracts.
- **A DOD SBIR award surfaced by a "recent DOE grant" search query turned out to be a 2003
  Missile Defense Agency award**, not a current DOE grant (L07-054) — retained with corrected
  facts rather than discarded, but this indicates recent, dated US government funding
  specifically for cryogenic leak/vapor-detection technology may be sparse or simply not
  well-indexed in general web search, which is itself a data gap worth flagging rather than
  papering over.

## Opportunity-shaped pain statements

Pain statements only — no startup pitches, no product framing.

1. **Turbomolecular-pump bearing reliability/vibration is still an active engineering problem
   after three-plus decades of magnetic-bearing development**, forcing fabs and accelerator
   labs to accept periodic pump failure/vibration risk as a cost of doing business. Who pays:
   semiconductor fabs and accelerator vacuum groups operating large turbopump fleets. Evidence:
   L07-010, L07-011, L07-012, L07-013.
2. **Hydrogen-outgassing bakeout is a rigid, multi-day, energy-intensive process step** (e.g.,
   30 hours at 250°C for a >70,000x outgassing reduction) that every UHV chamber fabricator must
   build into schedule and capex, with no faster validated alternative found in this record set.
   Who pays: UHV chamber manufacturers and their accelerator/semiconductor/quantum-computing
   customers. Evidence: L07-009, L07-007, L07-008.
3. **XHV pressure measurement below ~10^-10 Pa still fights the same X-ray-limit and ESD-ion
   physical barriers identified decades ago**, meaning labs pushing toward XHV cannot simply buy
   an off-the-shelf gauge with confidence at the extreme end of the range. Who pays: national labs
   and university groups running XHV-regime experiments. Evidence: L07-002, L07-003, L07-004.
4. **Dilution-refrigerator cooling power and vibration performance lag what multi-qubit,
   rack-scale quantum-computer scale-up will eventually require**, with current commercial units
   delivering only tens of µW at 10-20 mK versus early-research-stage ~2 mW demonstrations. Who
   pays: quantum-computing hardware companies and national labs building superconducting-qubit
   systems. Evidence: L07-014, L07-015, L07-016, L07-017.
5. **Ultra-pure-water and gas-delivery EPC capacity is being bid out in tens-of-billions-of-KRW
   packages per fab phase, with a thin, concentrated supplier base**, creating schedule risk for
   fab owners racing to meet AI/HBM demand. Who pays: Samsung, DB HiTek, and other fabs expanding
   capacity, plus their EPC contractors. Evidence: L07-046, L07-047.
6. **Gas/fluid-delivery subsystem suppliers report extreme customer concentration (76% of sales
   from two OEM customers)**, meaning a single customer's capex pause can directly threaten a
   whole supplier's revenue base, and new entrants face a very narrow qualification path into
   the OEM relationships that control fab-tool sales. Who pays (risk-bearer): incumbent and
   prospective gas-delivery subsystem suppliers. Evidence: L07-049.
7. **Big-science vacuum-vessel/cryostat manufacturing is effectively sole-sourced in several
   national programs** (India's ITER cryostat work through INOXCVA/L&T; China's HEPS tender
   restricted to China-registered manufacturers), leaving no qualified alternate supplier if the
   incumbent has a capacity or quality problem. Who pays: national fusion/accelerator programs
   and, ultimately, their government funders. Evidence: L07-033, L07-040, L07-045, L07-048.
8. **Vacuum-pump and semiconductor-dry-vacuum-pump market-size estimates disagree by up to ~2x
   across consultancies with no disclosed bottom-up methodology**, leaving investors and new
   entrants without a trustworthy total-addressable-market baseline. Who pays (information gap
   cost): investors, new entrants, and incumbent strategic planners relying on these figures.
   Evidence: L07-038, L07-039.
9. **Export-control-driven revenue divergence is already a measured FY2025 financial fact for at
   least one named vacuum/leak-detection incumbent** (INFICON: Americas -12.4% vs Asia-Pacific
   +19.2%), indicating firms serving both US and Chinese/Asian semiconductor customers face a
   live, ongoing geographic bifurcation of demand rather than a future risk. Who pays: vacuum/
   leak-detection/instrumentation vendors with US-and-China-exposed product lines. Evidence:
   L07-053.
10. **Pharmaceutical freeze-drying (lyophilization) vacuum/thermal process control remains a
    recurring source of FDA manufacturing-inspection findings**, per review-level evidence,
    indicating existing validation/monitoring practice does not fully close the gap between
    lyophilizer vacuum-control capability and regulatory expectations. Who pays: pharmaceutical
    manufacturers and their quality/regulatory-affairs functions. Evidence: L07-020, L07-021.
11. **NEG-coating and other distributed-pumping technologies studied academically since the
    1990s-2010s are still marketed by essentially a single named vendor (SAES Getters) in the
    sources gathered here**, with no second/third independent commercial NEG-coating supplier
    surfaced in this pass — a potential single-point-of-supply risk for accelerator builders
    relying on this pumping architecture. Who pays: accelerator/synchrotron builders specifying
    NEG-coated beam pipe. Evidence: L07-001, L07-037.
12. **Vacuum-component pricing (feedthroughs, flanges, custom chambers) is almost entirely
    quote-on-request rather than published**, making early-stage cost estimation for new
    vacuum-hardware projects (academic labs, startups, new fab lines) slow and dependent on
    vendor sales-cycle timing rather than self-service catalog pricing. Who pays: any buyer
    (lab, startup, fab) trying to budget a vacuum system before engaging a vendor sales process.
    Evidence: L07-036.

## Notes on evidence quality (honest uncertainty flags)

- The large majority of academic records (L07-001 through L07-027) were identified via search-
  index snippets rather than full-text fetch; most publisher pages (AIP, ScienceDirect, AAAS)
  returned HTTP 403 on direct WebFetch attempts this session. DOIs are populated only where
  visibly confirmed in the URL structure (IOP, Springer, AAAS records); ScienceDirect PII-based
  URLs do not expose DOI in the URL and are left blank rather than invented, per source standards.
- Several geography codes on older/anonymous-search-index academic records (e.g., L07-001,
  L07-006, L07-010, L07-013, L07-015, L07-016, L07-023) are explicitly labeled as tentative
  inferences from institutional/authorship context, not confirmed author affiliations — flagged
  in each record's `notes` field rather than asserted as fact.
- Three Japanese-language J-STAGE records (L07-025, L07-026, L07-027) were identified via listing
  metadata (title, journal, volume/issue/page) rather than full-text extraction; their
  peer-review status is inferred from the hosting journal's general editorial policy, not
  confirmed per-article.
- The INOX India ₹145 crore ITER figure (L07-048) and the EBARA $200M Korea/Taiwan investment
  figure (L07-051) both rely on secondary aggregation of primary company disclosures rather than
  a directly fetched primary-document page; both are flagged for verifier re-confirmation.
- The SBIR award record (L07-054) was directly fetched but turned out to be a 2003 DOD/Missile
  Defense Agency award rather than the intended "recent DOE grant" — kept with corrected facts
  as an honest, on-topic government-funding data point rather than discarded or mislabeled.
- Four ITER tender/award records (L07-041 through L07-044) share a single listing-page URL
  because the ITER procurement portal does not expose individual permalinks per tender in the
  fetched view; each record's `canonical_key` uses the unique tender ID to avoid false
  deduplication.
