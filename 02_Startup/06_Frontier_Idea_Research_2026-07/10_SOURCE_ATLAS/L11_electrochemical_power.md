# L11 -- Electrochemical Manufacturing, Hydrogen, E-Fuels, and Precision Power Delivery

Lane scope: electrolyzer stacks (PEM/alkaline/AEM/SOEC) and their rectifiers/power supplies,
industrial electrowinning/electroplating power, CO2 electrolysis, e-fuel synthesis hardware
(ammonia, methanol), battery formation/cycling equipment, and precision DC power delivery/control
for electrochemical processes generally. This brief is built only from the 55 records in
`L11_raw_sources.json` (IDs `L11-001`...`L11-055`); it does not propose startup ideas. All records
are `accepted: false` pending the separate verifier pass -- figures below should be read as "as
reported by the cited source," not as independently confirmed mission facts. Several load-bearing
company-filing and government figures were fetched directly this session (noted per claim below);
most academic records were confirmed via search-index synthesis rather than full-text fetch and
need verifier follow-up (Nature.com in particular blocked WebFetch behind a cookie-consent redirect
loop all session; several other publisher pages returned HTTP 403).

## Frontier state

- **Electrolyzers are in a capacity glut, not a capacity shortage.** Global installed electrolysis
  capacity reached only ~2 GW in 2024, versus ~20 GW/yr of Chinese manufacturing capacity alone and
  47.7 GW/yr of total Chinese manufacturing capacity in 2024 (rising toward 58 GW/yr in 2025)
  (`L11-035`, `L11-051`). China holds 65% of global installed/FID capacity and ~60% of global
  manufacturing capacity (`L11-035`). The bottleneck across almost every Western OEM is *project
  bankability and FID*, not stack technology or factory throughput -- both Nel ASA and thyssenkrupp
  nucera reported shrinking order backlogs and order intake collapsing (thyssenkrupp nucera green-H2
  order intake fell from EUR636M to EUR348M FY24/25; gH2-segment order intake alone was just EUR26M)
  even as their factories sit built and ready (`L11-047`, `L11-048`).
- **PEM stack chemistry is maturing on durability/degradation science, not on a single breakthrough.**
  Multiple 2024-2025 primary studies decompose PEM voltage decay into catalyst dissolution
  (Ir/Pt anode), membrane crossover, and contact-resistance contributions under both steady and
  intermittent (renewable-coupled) operation (`L11-001`, `L11-002`, `L11-003`, `L11-004`,
  `L11-031`). PGM-free/low-PGM anion-exchange-membrane (AEM) electrolysis is the leading
  cost-reduction lever under active research, with lab demonstrations of >550-hour stable
  PGM-free pure-water operation (`L11-009`, `L11-010`).
- **Solid oxide electrolysis (SOEC) is the efficiency frontier but the least commercially proven.**
  Industry requires <=0.75%/kh (ideally <=0.5%/kh) degradation to hit a 20%-performance-loss-over-
  5-years bar; dynamic/degradation-aware operating strategies can cut levelized H2 cost 9.5-16%
  versus naive control (`L11-014`, `L11-015`, `L11-034`). Topsoe's ModuLite (SOEC + ASU + Haber-
  Bosch in one modular skid) reaching commercial availability in late 2025 is the clearest sign SOEC
  is crossing from lab to shippable product for ammonia synthesis specifically.
- **Precision power delivery (rectifiers) is a quietly load-bearing, underappreciated sub-market.**
  Six-pulse thyristor rectifiers -- still the default for MW-scale electrolyzer stacks -- carry
  poor partial-load power factor and current ripple that measurably degrades cell efficiency and
  accelerates catalyst-layer wear; switching to transistor/IGBT-based or modular-multilevel-
  converter (MMC) hybrid rectifiers is documented to cut specific energy consumption by up to 14%
  and energy losses by ~13% versus conventional thyristor supplies (`L11-016`, `L11-017`, `L11-019`,
  `L11-020`, `L11-021`). The same rectifier-quality problem repeats verbatim in copper electrowinning,
  where SCR-thyristor vs. IGBT switch-mode rectifier choice is marketed as a direct lever on
  recovery rate and energy cost (`L11-045`).
- **CO2 electrolysis to multicarbon products is real chemistry with a real instability problem.**
  Copper remains the only catalyst family that reliably makes C2+ products from CO2/CO, with recent
  primary results reaching >500 mA/cm^2 to >4 A/cm^2 current densities and 83-87% Faradaic
  efficiency (`L11-005`, `L11-006`, `L11-007`, `L11-008`), but copper's own structural instability
  under reducing conditions is the still-unsolved rate-limiting problem for scale-up.
- **Direct seawater electrolysis is a genuine, active research cluster** (not vaporware) aimed at
  removing deionized-water pretreatment cost/complexity, but chloride-driven corrosion and parasitic
  chlorine evolution remain unresolved at anything beyond lab/pilot scale (`L11-022`, `L11-023`,
  `L11-024`).
- **Battery formation/cycling equipment is a mature, separately-financed precision-power-electronics
  market** riding the EV/ESS gigafactory wave (CATL, LG Energy Solution, Samsung SDI, SK On,
  Panasonic, and new entrants), dominated by Chroma ATE (Taiwan) and Hioki (Japan) on the
  test/formation side and NOVONIX/Arbin/BioLogic on the R&D-precision-cycler side (`L11-043`,
  `L11-044`). This sub-market is largely decoupled from the hydrogen-electrolyzer demand cycle
  above -- it tracks EV/grid-storage cell volumes, not hydrogen policy.

## Bottlenecks

1. **Rectifier/power-supply quality is a first-order (not second-order) lever on electrolyzer
   economics**, yet the incumbent installed base is still six-pulse thyristor technology optimized
   for capex, not for the ripple-driven efficiency losses now well documented in the literature
   (`L11-016`-`L11-021`). This is a precision-power-delivery gap hiding inside a chemistry-labeled
   industry.
2. **Catalyst degradation under intermittent (renewable-coupled) operation is still being
   characterized, not solved.** Multiple 2025 primary papers are still isolating *which* stress
   (OCV rest periods, ripple current, load-cycling amplitude) drives which failure mode
   (`L11-001`, `L11-003`, `L11-004`, `L11-021`, `L11-031`) -- a sign the industry does not yet have
   a settled answer for how to warranty stacks running on variable wind/solar power.
3. **Alkaline stack scale-up is limited by stray/shunt currents, not just tank size** -- current
   efficiency falls as cell count rises unless channel/manifold geometry is specifically
   re-engineered, which is a non-trivial (and apparently still-active) electrochemical-engineering
   problem, not a solved manufacturing one (`L11-012`, `L11-013`).
4. **Chinese electrolyzer manufacturing overcapacity is severe and likely to get worse before
   better**: ~2x demand-to-manufacturing-capacity ratio in 2024, with the gap projected to widen
   into 2025 (`L11-035`, `L11-051`). This directly threatens Western OEM (Nel, thyssenkrupp nucera,
   Plug) unit economics on price, and raises the question of where non-Chinese entrants can compete
   at all except on service, integration, or power-delivery differentiation rather than stack cost.
5. **Hydrogen embrittlement of pipeline/transport steel remains materially unresolved** for
   blended-gas and pure-hydrogen transport at scale, with active 2025-2026 research still building
   basic mechanical-testing standards and multiscale material-design guidance rather than deploying
   settled solutions (`L11-028`, `L11-029`, `L11-030`).
6. **Green hydrogen demand-side bankability, not electrolyzer supply, is the binding constraint
   in 2025-2026.** The clearest evidence: two of the most bellwether Western electrolyzer OEMs
   (Nel ASA, thyssenkrupp nucera) both reported *shrinking* order backlogs in the same period that
   government award programs (DOE H2Hubs, EU Hydrogen Bank, Japan CfD) were actively
   disbursing money (`L11-032`, `L11-039`, `L11-047`, `L11-048`, `L11-054`) -- the
   public-subsidy pipeline and the private order book are moving in opposite directions.

## Named buyers and spending signals

- **US DOE Regional Clean Hydrogen Hubs**: up to $2.2B committed (Nov 2024) to Gulf Coast
  (HyVelocity, TX, up to $1.2B federal share, electrolysis + gas-CCS) and Midwest (MachH2,
  IL/IN/IA/MI, up to $1B) hubs, part of a broader up-to-$7B/7-hub program under the Bipartisan
  Infrastructure Law (`L11-032`).
- **EU Hydrogen Bank (Innovation Fund) auctions**: three completed rounds identified -- EUR ~720M/7
  projects (2024, 6 signed grant agreements worth EUR270.6M), EUR992M/15 projects (2025, including 3
  maritime-fuel projects at EUR0.45-1.88/kg premiums), and >EUR1B/9 projects (Dec2025-Feb2026 round)
  (`L11-039`).
- **Japan METI/JOGMEC CfD scheme**: JPY3T (~$19-20B) 15-year contract-for-difference support;
  first two awardees named Oct 2025 -- Toyota Tsusho (1,600 t/yr green H2) and Resonac (20,000
  t-NH3/yr), both targeting 2030 first supply (`L11-037`, `L11-054`).
- **Air Products / NEOM (Saudi Arabia)**: >2 GW alkaline electrolysis contract awarded to
  thyssenkrupp Uhde Chlorine Engineers, targeting 600 t/day H2 and up to 1.2 Mt/yr green ammonia for
  exclusive export by Air Products (`L11-052`) -- the largest single electrolyzer-equipment
  procurement identified this session.
- **China named industrial buyers**: Sinopec (Kuqa 260 MW demonstration project, running below
  nameplate at times; Uxin Banner 24-set alkaline electrolyzer tender won by LONGi) (`L11-049`,
  `L11-050`); China Energy Construction (125-set alkaline+PEM tender, won by LONGi/Peric/Sungrow)
  (`L11-051`); China Coal Group (Pingshuo open-pit coal mine, 48 MW Sungrow alkaline electrolyzers
  for on-site H2 use) (`L11-055`) -- a genuinely unusual non-power-sector green-H2 buyer.
- **Company order books (self-reported, company_filing tier)**: Plug Power -- $187M 2025
  electrolyzer revenue, ~$8B sales funnel, named 100 MW Galp Sines (Portugal), 55 MW Carlton Power
  (UK), 25 MW Iberdrola (Spain) deployments (`L11-046`); Nel ASA -- NOK1,319M backlog at FY2025 end
  (down 18% y/y), Q4 order intake up 364% q/q but full-year trend still negative (`L11-047`);
  thyssenkrupp nucera -- EUR0.6B backlog (down from EUR1.1B), named PGS 1.4 GW Australia and TGV
  SRAAC India contracts, but its *chlor-alkali* (non-hydrogen) segment is the profitable, growing
  half of the business (`L11-048`).

## Incumbent map

- **PEM**: Siemens Energy (Silyzer 300, 17.5 MW/stack-array, >75.5% plant efficiency, vendor claim)
  (`L11-040`); Cummins/Accelera (HyLYZER 500/1000/5000, 1.25 MW-200+ MW range, US-manufactured in
  Fridley MN) (`L11-041`); Plug Power (GenEco, US, >300 MW cumulative shipped) (`L11-046`).
- **Alkaline**: LONGi Hydrogen, Peric Hydrogen, and Sungrow Hydrogen collectively hold ~70% of
  China's cumulative electrolyzer tender-win share since 2023 (`L11-051`); John Cockerill (Belgium/
  France, targeting 18 GW/yr global output by 2030 across France/India/China/Middle East/Europe
  plants, absorbed key McPhy assets July 2025) (`L11-042`); Nel ASA (Norway) (`L11-047`).
- **Chlor-alkali / large-scale electrochemical membrane incumbency**: thyssenkrupp nucera is the
  dominant Western player bridging chlor-alkali (mature, profitable) and green-H2 (immature,
  loss-making) using the same underlying membrane-electrolyzer engineering base (`L11-048`).
- **Battery formation/cycling test equipment**: Chroma ATE (Taiwan, full cell-to-pack test/
  formation portfolio), Hioki (Japan, precision resistance/QC instrumentation), NOVONIX/Arbin/
  BioLogic (US-oriented precision R&D cyclers) (`L11-043`, `L11-044`).
- **Copper electrowinning/electrorefining power supplies**: Advint and comparable rectifier vendors
  market SCR-thyristor vs. IGBT switch-mode systems directly as a recovery-rate/energy-cost lever
  (`L11-045`) -- an underexplored analog of the electrolyzer rectifier problem in an older, more
  conservative industry (mining).

## 2026-2031 triggers

- **Japan METI CfD-scheme projects** (Toyota Tsusho, Resonac) target first supply in **2030**
  (`L11-054`) -- a dated, government-backed demand trigger, though six years out.
- **NEOM/Air Products** electrolyzer commissioning and first ammonia export originally targeted
  **2026-2027** (`L11-052`) -- a near-term test of gigawatt-scale alkaline electrolysis reliability.
- **EU Hydrogen Bank** auctions are now an annual, recurring procurement trigger (three rounds in
  2024-2026 identified) (`L11-039`) -- each round is a fresh, dated government-money-moving event
  that resets which projects are actually funded rather than merely announced.
- **China's manufacturing-capacity overhang** (47.7 GW/yr in 2024, projected >58 GW/yr in 2025 vs.
  ~2 GW/yr global 2024 deployment) (`L11-035`, `L11-051`) implies continued price pressure and
  likely consolidation/shakeout among China's ~dozens of electrolyzer makers through at least 2027,
  which is itself a trigger for Western buyers seeking non-Chinese-sourced equipment (export-control
  and supply-chain-resilience angle, not directly evidenced in this set and flagged for red-team).
- **DOE H2Hubs Phase 1-to-Phase 2 transitions** are an ongoing, multi-year gating trigger --
  several hubs remained in Phase 1 (planning) as of this session, meaning Phase 2 (construction)
  disbursements are a forward, not yet realized, trigger (`L11-032`).

## US vs. Asia differences

- **Manufacturing scale**: China dominates on both installed capacity (65% of global) and
  manufacturing capacity (~60% of global, ~20 GW/yr nameplate) (`L11-035`); the US and Europe
  compete on smaller absolute volumes but claim higher per-unit efficiency/quality positioning
  (Siemens Energy, Cummins/Accelera, John Cockerill Western plants) (`L11-040`, `L11-041`,
  `L11-042`).
- **Demand-side structure**: China's demand signals include an unusual industrial (non-power-
  sector) buyer -- a state-owned coal-mining group using electrolytic H2 on-site (`L11-055`) --
  whereas named US/EU demand is concentrated in refinery decarbonization (Galp Sines via Plug,
  `L11-046`), ammonia/steel decarbonization (DOE hubs, Japan CfD winners), and CCS-paired hydrogen
  hubs (Gulf Coast) (`L11-032`).
- **Policy mechanism design differs**: the US uses direct capital-cost-share grants (H2Hubs), the
  EU uses recurring competitive premium-per-kg auctions (Hydrogen Bank), and Japan uses a 15-year
  contract-for-difference price-gap mechanism (`L11-032`, `L11-037`, `L11-039`) -- each
  creates a different bankability profile and a different point of leverage for a hardware vendor
  selling into that market.
- **Overcapacity risk is asymmetric**: Chinese manufacturers face a severe capacity/demand mismatch
  domestically and are responding by exporting aggressively (Indonesia, Uzbekistan, Namibia, Oman,
  Europe, South America orders identified for LONGi and Sungrow this session) (`L11-050`, `L11-055`
  context), which Western OEMs facing their own order-book contraction (`L11-047`, `L11-048`) may
  experience as direct price competition in third markets, not just at home.

## Unresolved contradictions

1. **"Hydrogen boom" headlines vs. two leading OEMs' shrinking order books.** IEA's Global Hydrogen
   Review narrative of accelerating deployment (`L11-035`) sits awkwardly next to Nel ASA's 18%
   backlog decline and thyssenkrupp nucera's ~45% order-intake decline in the same reporting period
   (`L11-047`, `L11-048`). Both can be true simultaneously (aggregate pipeline growing, near-term
   Western order books shrinking as China captures share and FIDs slip) but the mission should not
   accept either framing uncritically.
2. **Government award announcements vs. realized construction.** Several billion-dollar-scale
   awards (DOE H2Hubs, EU Hydrogen Bank rounds, Japan CfD) are confirmed as *awarded*
   (`L11-032`, `L11-037`, `L11-039`, `L11-054`) but this session found limited evidence
   of Phase-2/construction-stage disbursement completion for most of them -- the gap between award
   and construction is itself a data point the mission should track, not assume closed.
3. **Sinopec Kuqa as flagship vs. Sinopec Kuqa as cautionary tale.** The same project is cited in
   different sources both as the "world's first/largest" green-hydrogen demonstration success and
   as running at a fraction (reportedly as low as ~20% at one point, recovering to ~51%) of
   nameplate electrolyzer utilization (`L11-049`) -- both framings appear in the record set and are
   preserved rather than averaged away.
4. **Chinese electrolyzer manufacturing capacity claims are hard to reconcile with each other.**
   IEA states ~20 GW/yr Chinese manufacturing capacity in 2024 (`L11-035`) while a Chinese-language
   industry source states 47.7 GW/yr total China capacity in 2024, projected >58 GW/yr in 2025
   (`L11-051`) -- these may be measuring different scopes (electrolyzer-stack-only vs. full-system,
   or "nameplate announced" vs. "IEA-verified operating"), but the ~2.4x discrepancy is unresolved
   in this record set and should not be silently reconciled by a later phase.

## Opportunity-shaped pain statements

(Pain + who pays + evidence IDs -- not startup pitches.)

1. **Electrolyzer operators lose measurable efficiency and stack life to rectifier current ripple,
   but the installed base is still six-pulse thyristor technology.** Pain: up to ~13-14% avoidable
   specific-energy-consumption penalty from ripple/harmonics at MW scale. Who pays: electrolyzer
   OEMs and their industrial/utility customers absorbing higher electricity opex per kg H2 over a
   15-20-year asset life. Evidence: `L11-016`, `L11-017`, `L11-019`, `L11-020`, `L11-021`, `L11-018`.
2. **Alkaline stack scale-up loses current efficiency to shunt/stray currents as cell count grows,**
   forcing bespoke channel/manifold redesign rather than simple linear scale-up. Who pays: alkaline
   electrolyzer manufacturers (LONGi, Peric, Sungrow, John Cockerill, Nel) engineering each new
   stack generation. Evidence: `L11-012`, `L11-013`.
3. **PEM stack warranties are being written before the industry has settled which specific stress
   (OCV cycling, ripple amplitude, load-following rate) drives which degradation mode under
   renewable-variable operation.** Who pays: project developers and financiers pricing performance-
   guarantee risk into green-H2 project debt, and OEMs (Nel, Plug, Cummins/Accelera) absorbing
   warranty claims. Evidence: `L11-001`, `L11-003`, `L11-004`, `L11-021`, `L11-031`.
4. **Copper electrowinning/electrorefining plants face the same rectifier-quality economics problem
   as electrolyzers but in a far more conservative, less-instrumented industry.** Who pays: mining
   companies operating electrowinning tank houses, paying avoidable energy cost per tonne of Cu.
   Evidence: `L11-026`, `L11-027`, `L11-045`.
5. **Hydrogen pipeline/blending infrastructure lacks settled mechanical-testing standards for
   hydrogen embrittlement,** creating design-margin uncertainty (and likely over-conservative,
   expensive steel specs) for anyone building H2 transport infrastructure now. Who pays: pipeline
   operators and hydrogen-hub developers (e.g., Gulf Coast/Midwest H2Hubs) sizing capex against
   unresolved material-science guidance. Evidence: `L11-028`, `L11-029`, `L11-030`, `L11-032`.
6. **SOEC degradation-aware operation is not yet a standard, deployable control product** -- it
   exists as academic optimization results (9.5-16% LCOH improvement) rather than off-the-shelf
   plant control software. Who pays: SOEC plant operators (e.g., Topsoe ModuLite customers) currently
   likely leaving double-digit-percent cost savings on the table via naive fixed-mode operation.
   Evidence: `L11-014`, `L11-015`, `L11-034`.
7. **Western/non-Chinese electrolyzer OEMs cannot compete with Chinese manufacturers on stack unit
   cost given the ~2x capacity/demand overhang inside China,** forcing a choice between exiting
   stack manufacturing or competing on integration, service, power-electronics quality, or
   application-specific engineering instead. Who pays: OEM shareholders/employees (Nel, thyssenkrupp
   nucera) absorbing margin compression now. Evidence: `L11-035`, `L11-047`, `L11-048`, `L11-051`.
8. **Direct seawater electrolysis cannot yet escape the lab** because chloride corrosion and
   parasitic chlorine evolution degrade electrodes/membranes faster than freshwater systems, which
   keeps coastal/offshore green-H2 projects dependent on costly desalination pretreatment. Who pays:
   offshore/coastal green-H2 project developers carrying desalination capex/opex they would
   otherwise avoid. Evidence: `L11-022`, `L11-023`, `L11-024`.
9. **CO2-to-multicarbon-product electrolyzers cannot hold performance at industrially relevant
   copper-catalyst loadings** because copper itself restructures/dissolves under reaction
   conditions, capping run life below what a chemical-plant operator would consider bankable. Who
   pays: e-fuel/e-chemical project developers whose unit economics depend on catalyst replacement
   frequency. Evidence: `L11-005`, `L11-006`, `L11-007`, `L11-008`.
10. **Green ammonia plants must currently choose between mature (Haber-Bosch-coupled electrolysis)
    and emerging (direct electrochemical N2-to-NH3) synthesis routes with very different technology-
    readiness and cost profiles**, complicating capital-allocation decisions for buyers like AM Green
    (Kakinada) and NEOM. Who pays: green-ammonia project developers and their offtake customers
    bearing the technology-choice risk. Evidence: `L11-025`, `L11-052`.
11. **A state-owned coal-mining buyer (China Coal, Pingshuo) is already using electrolytic hydrogen
    operationally at an open-pit mine** -- a demand pattern (captive industrial H2 use outside the
    power/refining/ammonia mainstream) that is under-documented relative to its apparent commercial
    reality. Who pays/benefits: mining-sector buyers seeking on-site H2 for equipment or processes,
    an underexplored buyer category relative to refinery/ammonia/steel narratives. Evidence:
    `L11-055`.
12. **Battery-formation/cycling precision-power equipment demand is decoupled from the volatile
    hydrogen-policy cycle** (it tracks EV/ESS cell volumes instead), meaning teams building
    precision DC power-delivery IP for electrochemical processes face a choice of end-market with
    very different demand volatility profiles even though the underlying power-electronics problem
    (precise, low-ripple, high-current DC delivery) is nearly identical. Who pays: gigafactory
    operators (CATL, LG Energy Solution, Samsung SDI, SK On, Panasonic and new entrants) versus
    hydrogen-project developers, as two structurally different customer bases for the same core
    power-electronics competency. Evidence: `L11-043`, `L11-044`, `L11-016`-`L11-021`.

## Session limitations (honesty notes)

- Nature.com (nature.com/articles/...) blocked WebFetch behind a persistent cookie-authorization
  redirect loop for every attempt this session; all Nature/Nature Communications/Nature Reviews
  Materials/Communications Engineering records in this set (`L11-005` through `L11-008`, `L11-011`,
  `L11-022` through `L11-024`) are search-index-synthesis only, not full-text-verified, and should
  be prioritized for re-fetch by the verifier.
- IOPscience, MDPI, and RSC PDF endpoints returned HTTP 403 on direct WebFetch attempts multiple
  times this session (`L11-001`, `L11-003`, `L11-016` full-text, `L11-017`, `L11-028`, `L11-014`) --
  likely bot-blocking rather than content absence, since DOI resolution via doi.org succeeded for
  several of these.
- `docs.nrel.gov` failed DNS resolution during this session (`L11-033`) -- a transient network
  issue, not a content-availability problem.
- The Nel ASA Q4 2025 PDF (`L11-047`) was downloaded successfully but returned as unparsed binary
  stream rather than extractable text; figures used come from the accompanying search-index
  synthesis of the same report, not from direct PDF parsing.
- This lane's collected set reaches 38/55 (69%) T1-tier records, short of the 78% T1-eligible
  target in the scout brief. The shortfall is concentrated in genuinely review-type literature
  (Chemical Reviews, Nature Reviews Materials, RSC review articles) that cannot honestly be
  relabeled T1 per the source standards' "reviews are T2 even in top journals" rule; four
  originally-review placeholders were already swapped for primary-research equivalents to improve
  this ratio before finalizing the set.

## P2A origin-audit repair (2026-07-13)

- removed IDs: L11-036, L11-053
- removed/trimmed claims: deleted the "India MNRE/SECI SIGHT scheme" buyer-signal bullet from
  "Named buyers and spending signals" (rested solely on L11-036/L11-053); deleted the "India
  SIGHT-II" trigger bullet from "2026-2031 triggers" (rested solely on L11-036); trimmed the
  Ohmium clause out of the PEM incumbent list in "Incumbent map" (rested solely on L11-053);
  trimmed "India SIGHT"/L11-036 out of the co-supported government-award-programs citation list
  in Bottlenecks item 6 (claim remains co-supported for DOE H2Hubs/EU Hydrogen Bank/Japan CfD);
  trimmed the India/SIGHT clause and L11-036 out of the co-supported "Policy mechanism design
  differs" sentence in "US vs. Asia differences" (US/EU/Japan mechanisms remain, each still
  co-supported); trimmed "India SIGHT"/L11-036 out of the co-supported awarded-vs-constructed
  citation list in "Unresolved contradictions" #2 (claim remains co-supported for DOE
  H2Hubs/EU Hydrogen Bank/Japan CfD). P4 must re-source any India electrolyzer-manufacturing
  incentive (SIGHT/SIGHT-II) or Ohmium capacity claim from an eligible (non-India-origin)
  provider before reuse.
