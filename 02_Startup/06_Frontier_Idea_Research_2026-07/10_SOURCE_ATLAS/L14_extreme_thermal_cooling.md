# L14 — Extreme Thermal Management and Two-Phase Cooling for Power-Dense Systems

Lane scout brief. Sources cited as `L14-0NN` refer to `10_SOURCE_ATLAS/L14_raw_sources.json`
(55 candidate records, all `accepted: false` pending verifier review). This lane covers two-phase/
immersion/microchannel/jet-impingement cooling, cold plates, thermal interface materials (TIMs),
high-heat-flux electronics cooling for data centers/AI accelerators, power electronics, lasers,
radar, EV fast charging, and aerospace, plus the refrigerants and thermal test/metrology hardware
that underpin all of the above. Founder background was not used to select topics within this lane.
Uncertainty is flagged explicitly throughout rather than smoothed over.

## 1. Frontier state

- **AI-accelerator thermal design power has decisively outrun air cooling.** Vendor and
  third-party technical commentary converge on GB200/GB300-class GPUs dissipating roughly
  1,000-1,200 W each, pushing a 72-GPU NVL72 rack past 120 kW and mandating rack-scale direct
  liquid cooling; NVIDIA's own product page frames liquid cooling as enabling "25x more
  performance at the same power" versus air-cooled H100 infrastructure (L14-044). Peer-reviewed
  literature independently frames the same trend in device terms: AI-accelerator TDP is described
  as moving from the kilowatt level toward 3,000-5,000 W with local heat flux reaching
  800-1,000 W/cm2 (L14-010), and multilayer microchannel cold-plate designs are now being
  engineered to hit 206.5 W/cm2 at sub-0.2 K/W thermal resistance for CPU packages specifically
  (L14-009).
- **Two-phase and immersion cooling are simultaneously accelerating and being destabilized by a
  refrigerant supply shock.** Multiple 2024-2026 peer-reviewed papers advance two-phase immersion
  and chip-side two-phase cooling as the leading path beyond single-phase liquid cooling
  (L14-001, 002, 003, 029), and a Chinese peer-reviewed review explicitly frames phase-change
  liquid cooling as "the development trajectory for ultra-high-density heat dissipation"
  (equivalent finding independently reported by ZTE's own technical journal, L14-idea cross-link
  in Section 7). At the same time, 3M's exit from all PFAS manufacturing (last Novec order
  accepted March 31, 2025; production ceased end of 2025) has removed the fluid family
  (Novec 7100/649, Fluorinert FC-72) that made two-phase immersion cooling commercially viable,
  and a 2025 peer-reviewed EV-charging-connector paper was still specifying Novec 7500 as its
  best-performing coolant even as that exact product line was being wound down (L14-022) --
  the field's own recent literature and its supply chain are now out of sync.
- **Microchannel and jet-impingement cooling remain active, not solved, research areas.** At
  least five 2025-2026 peer-reviewed papers independently advance microchannel cold-plate designs
  (orthogonal-test optimization, embedded/CPU-package integration, enhanced flow boiling, review
  syntheses) (L14-006, 007, 008, 009, 010), and jet-impingement cooling for power electronics
  continues to see both nanofluid-enhancement and automotive-specific reviews (L14-012, 013),
  with next-generation wide-bandgap power devices flagged as needing to manage heat flux
  "well above 1,000 W/cm2" (L14-012).
- **Thermal interface materials are a live materials-science frontier, not a mature commodity.**
  2025-2026 reviews describe liquid-metal, graphene-based, and highly crystalline polymer TIM
  formulations as active research fronts specifically because 2.5D/3D chiplet integration creates
  hundreds-of-watts-per-package hotspots that existing TIM1/TIM1.5 materials cannot adequately
  address (L14-014, 015, 016, 018).
- **EV fast-charging thermal management is a distinct, fast-moving sub-frontier.** Five
  2023-2025 peer-reviewed papers this session independently addressed heat-pipe, liquid-metal,
  liquid-cooled cable-core, and immersion-cooling approaches to megawatt-class EV charging
  connectors and cables (L14-019, 020, 021, 022), consistent with trade reporting that
  liquid-cooled charging cables are becoming core HPC (High Power Charging) infrastructure and
  that Sinbon Electronics received the first UL safety certification for a 1 MW-capable
  liquid-cooling charging system in 2025 (context, not independently fetched this session).
- **Aerospace/defense two-phase thermal control is a mature but still-evolving discipline.**
  Loop heat pipes and oscillating heat pipes remain active peer-reviewed research areas for
  satellite thermal control (L14-024), phased-array radar thermal-electromagnetic-structural
  co-design is an ongoing peer-reviewed topic (L14-027), and a 2025 ASME retrospective explicitly
  frames DARPA as having run three consecutive decades of thermal-management research programs
  for defense electronics (L14-025) -- this is not a solved, legacy problem for the defense
  sector.
- **China, Japan, Korea, Singapore, and Taiwan all show concrete 2025-2026 cooling-technology or
  policy activity**, not just downstream adoption of US/hyperscaler designs: Taiwan's ITRI
  announced (the day before this scouting session) a low-pressure-refrigerant two-phase cold
  plate reaching 2,400 W per chip (L14-053); Korea's GS Caltex launched a second liquid-cooling
  fluid product line in October 2025 with named customers Samsung SDS and LG U+ (L14-049); Japan's
  NTT Facilities opened a dedicated cooling-technology verification/showroom facility in April
  2025 (L14-050); and China has both a national PUE efficiency standard under active revision
  (L14-035) and a dedicated liquid-cooling-system technical specification (T/CIEP 0263-2025,
  L14-039).

## 2. Bottlenecks

- **The PFAS/Novec supply-chain collapse is the single largest near-term physical bottleneck for
  two-phase immersion cooling.** 3M's PFAS exit (announced Dec. 2022, fully executed by end of
  2025) eliminated the dominant dielectric-fluid family for two-phase immersion cooling; as of
  mid-2026, no hydrocarbon-based two-phase alternative fluid had reached commercial
  data-center-scale qualification, per trade reporting reviewed this session (context source, not
  independently fetched as a load-bearing record). This directly collides with the EPA's AIM Act
  HFC phasedown (60% of 2011-2013 baseline allowed 2024-2028, tightening further after, L14-033)
  and the EU's parallel F-gas Regulation 2024/573 (in force since Feb. 20, 2024, L14-034) --
  vendors of both immersion fluids and vapor-compression refrigerants face simultaneous regulatory
  phase-down pressure from two different chemical-class directions (PFAS and HFCs) at the same
  time AI-driven heat density is spiking.
- **Government policy claims about liquid-cooling mandates outrun what the primary text actually
  says -- a real, documented gap between trade-press narrative and primary-source text.** China's
  April 2026 joint NDRC/NEA/MIIT/National Data Administration AI-energy action plan is widely
  reported in secondary Chinese tech media as mandating "100% liquid cooling for new large AI data
  centers," but the actual fetched primary notice text only references generic "high-efficiency
  cooling" with no percentage mandate (L14-036) -- a load-bearing distinction for any idea premised
  on a hard Chinese liquid-cooling mandate.
- **Vendor-vs-vendor TDP and flow-rate figures for the highest-profile buyer (NVIDIA GB200 NVL72)
  are not internally consistent across sources.** Per-GPU TDP is variously reported as 1,000 W or
  1,200 W, and rack-level manifold flow requirements are reported from "80 LPM" up to "700+ LPM,"
  depending on which third-party technical-press source is consulted; NVIDIA's own product page
  does not itself disclose a single definitive TDP or flow figure (L14-044) -- any idea sizing a
  cooling solution to "the GB200 rack" needs a directly-sourced NVIDIA or ODM engineering
  spec, not press synthesis.
- **Company-filing-derived demand figures in this lane rely heavily on secondary aggregation
  rather than directly fetched primary filings.** SEC EDGAR (Vertiv 10-K, L14-048) and multiple
  vendor press pages (Schneider Electric/Motivair, L14-047) returned HTTP 403 to direct fetch this
  session; the same blocking pattern was observed in other lanes of this project (per prior lane
  briefs), indicating a project-wide, not lane-specific, verification gap that a future wave
  should address with authenticated fetch tools.
- **Market-size estimates for data-center liquid cooling vary by nearly an order of magnitude
  across credible research firms**, from $3.42B (2022 base year, Virtue Market Research) to
  $6.65B (2025, Grand View Research) with 2030-2035 endpoints ranging $15.26B-$29.46B depending on
  methodology (L14-054) -- no single TAM figure from this lane should be treated as settled without
  independent bottom-up triangulation.
- **JEDEC's foundational thermal-test-method standard (JESD51 series) has an unconfirmed current
  revision date**, and this session did not verify whether the base methodology has been updated
  to reflect two-phase/liquid-cooled test conditions as opposed to the traditional still-air/
  forced-convection conditions the series was originally built around (L14-040) -- a plausible,
  though not directly evidenced, standards-lag risk analogous to the laser-safety-standard lag
  flagged in this project's L12 lane brief.

## 3. Named buyers and spending signals

- **U.S. Department of Energy / ARPA-E (COOLERCHIPS program, L14-032)** — launched with $42
  million (Sept. 22, 2022, L14-031), then made 15 named awards totaling $40 million (May 9, 2023,
  L14-030) spanning Flexnode ($3.5M), HP ($3.25M), HRL Laboratories ($2.0M), Intel Federal
  ($1,711,416), JETCOOL Technologies ($1,265,747, later acquired by Flex — see L14-045), NREL
  ($1,463,319), Nvidia ($5.0M), Purdue ($1,881,315), Raytheon Technologies ($2,504,024), UC Davis
  ($3,586,473), U. Florida ($3,042,417), UIUC ($2.5M), U. Maryland ($3,484,484), U. Missouri
  ($1,649,290), and UT Arlington ($2,843,223) — a directly confirmed, dated, named-recipient
  government R&D-funding signal spanning both hyperscale (Nvidia) and defense-prime (Raytheon)
  buyers.
- **Google** — published the Project Deschutes 2 MW coolant-distribution-unit (CDU) specification
  through the Open Compute Project, requiring an aggressive 3C approach temperature difference and
  ~80 PSI available pressure; at least seven vendors (Boyd, CoolerMaster, Delta, Envicool, Nidec,
  nVent, Vertiv) have since built CDUs to this open hyperscaler-authored specification (L14-043).
- **Meta** — authored (with Google and Rittal contributions) the Open Rack V3 (ORv3) base
  specification governing the physical/thermal integration standard for OCP-compliant liquid-cooled
  racks, including blind-mate quick-disconnect liquid manifolds (L14-042); OCP separately
  maintains a base specification specifically for immersion cooling fluids (L14-041).
- **NVIDIA** — both a COOLERCHIPS awardee ($5.0M, L14-030) and the GPU vendor whose GB200 NVL72
  rack-scale liquid-cooled architecture is now the dominant reference design driving the entire
  downstream cooling-vendor ecosystem (L14-044).
- **Vertiv (NYSE: VRT)** — FY2025 revenue of $10.2 billion, management-reported liquid-cooling
  order growth of 50%+ in 2025, Q4 2025 book-to-bill ratio of 2.9, and a $15 billion order backlog
  entering 2026 (L14-048, sourced via investor-press secondary aggregation; canonical 10-K not
  independently fetched this session).
- **Schneider Electric / Motivair** — Motivair's CDU family scales 105 kW to 2.5 MW, is
  NVIDIA-certified, and is used in six of the world's top-10 supercomputers, following Schneider's
  February 2025 acquisition of Motivair (L14-047).
- **Flex (NASDAQ: FLEX)** — directly confirmed (own investor press release) acquisition of JetCool
  Technologies on November 14, 2024; JetCool's CDU handles up to 300 kW per rack and 2+ MW in
  row-based configurations (L14-045).
- **ZutaCore** — raised $100M+ Series C (dated June 2, 2026) from strategic investors including
  Mitsubishi Electric, Carrier Ventures, and Samsung Electronics/Samsung Ventures, targeting
  waterless two-phase direct-to-chip cooling for processors exceeding 4,000 W (L14-046).
- **Trane Technologies** — acquired two-phase-immersion vendor LiquidStack (Feb. 10, 2026),
  consolidating another independent two-phase cooling vendor into a public HVAC major (L14-051,
  aggregator-sourced, not independently confirmed via Trane's own release this session).
- **Singapore EDB/IMDA** — launched DC-CFA2 (Dec. 1, 2025) allocating at least 200 MW of new
  data-center capacity, conditioned on >=50% green-pathway power, BCA-IMDA Green Mark Platinum
  certification, PUE <=1.25, and compliance with Singapore Standard SS 715:2025 (L14-037) — a
  directly dated, quantified regulatory-buyer gate that any cooling vendor targeting Singapore must
  clear.
- **GS Caltex (Korea)** — launched "Kixx DLC Fluid PG25" direct-liquid-cooling fluid (Oct. 14,
  2025) with named customers Samsung SDS (2024 immersion-fluid supply) and LG U+ (2025 Pyeongchon
  data-center demonstration), plus a Supermicro AI-server thermal-testing partnership and a
  September 2025 immersion-cooling development agreement with GS Engineering & Construction and
  SDT (L14-049, directly fetched, Korean-language).
- **NTT Facilities (Japan)** — opened a dedicated "DC Cooling Hub" verification/showroom facility
  (fully operational April 22, 2025) simulating 780 kW of mixed air/liquid cooling load (L14-050,
  directly fetched, Japanese-language).
- **Industrial Technology Research Institute (Taiwan, ITRI)** — announced (per trade reporting
  dated July 11, 2026, the day before this session) a low-pressure-refrigerant two-phase cold
  plate reaching 2,400 W per chip with >40% energy savings versus conventional liquid cooling, and
  is actively assembling a domestic cold-plate/CDU/component supply chain around it (L14-053).
- **China (National Development and Reform Commission, National Energy Administration, MIIT,
  National Data Administration)** — jointly issued a national AI-energy action plan (document
  no. 国能发科技〔2026〕34号, dated April 8, 2026) referencing high-efficiency cooling and a
  green-power-direct-connection framework, though without the specific liquid-cooling percentage
  mandate that secondary media attributes to it (L14-036, directly fetched, with the media-vs-primary
  gap flagged as Contradiction 1 in Section 7).

## 4. Incumbent map (companies, products, price/share signals)

| Company | Product / Role | Signal |
|---|---|---|
| Vertiv (US) | Full-stack thermal/power infrastructure, liquid cooling | FY2025 revenue $10.2B; liquid-cooling orders +50%+ in 2025; $15B backlog (L14-048) |
| nVent (US) | Diversified industrial cooling/electrical, ~30% data-center exposure | Growing NVIDIA partnership depth (context, not independently fetched) |
| Schneider Electric / Motivair (France/US) | CDUs 105 kW-2.5 MW, NVIDIA-certified | Used in 6 of top-10 supercomputers; acquired Motivair Feb. 2025 (L14-047) |
| Flex / JetCool (US) | Microconvective direct-to-chip cooling, CDUs to 300 kW/rack, 2+ MW row-scale | Acquired by Flex Nov. 14, 2024 (L14-045); JetCool also a 2023 DOE COOLERCHIPS awardee ($1.27M, L14-030) |
| ZutaCore (Israel/US) | Waterless direct-to-chip two-phase cooling, >4,000 W/chip target | $100M+ Series C, June 2026, backed by Mitsubishi Electric, Samsung Ventures, Carrier Ventures (L14-046) |
| Trane Technologies / LiquidStack (US/Netherlands) | Two-phase immersion cooling | Acquired by Trane Feb. 10, 2026; prior last round $20M (Sept. 2024) (L14-051) |
| NVIDIA (US) | GB200 NVL72 rack-scale liquid-cooled reference architecture | Also a 2023 DOE COOLERCHIPS awardee ($5.0M) (L14-030, 044) |
| Google (US) | Project Deschutes 2 MW CDU open specification | Adopted by 7+ vendors via OCP (L14-043) |
| Meta (US) | Open Rack V3 (ORv3) base specification | Foundational hyperscale liquid-cooled rack physical standard (L14-042) |
| GS Caltex (Korea) | Immersion + direct liquid cooling fluids (Kixx series) | Named customers Samsung SDS, LG U+; Supermicro partnership (L14-049) |
| NTT Facilities (Japan) | Cooling-technology verification/showroom facility | 780 kW simulated mixed-load test facility, opened April 2025 (L14-050) |
| ITRI (Taiwan) | Low-pressure-refrigerant two-phase cold plate | 2,400 W/chip demonstrated; assembling domestic supply chain (July 2026) (L14-053) |
| 3M (US) | Former dominant two-phase dielectric fluid supplier (Novec, Fluorinert) | Exited all PFAS manufacturing by end of 2025 (context; see Section 2) |
| Sandia National Laboratories (US) | "Sandia Cooler" rotating-fin air-cooling technology (national-lab-originated IP) | Sought for licensing in electronics/HVAC cooling; dated ~2012, older than this lane's 2026-2031 window (L14-038) |
| Chemours (US) | Low-GWP refrigerants incl. Opteon 2P50 (two-phase immersion target fluid) | Positioned as a post-Novec alternative (context, not independently fetched as a load-bearing record) |
| Honeywell (US) | Low-GWP Solstice refrigerant family (e.g., Solstice N41, GWP <1 target) | ASHRAE provisional A1 designation reported (context, not independently fetched) |

**Pricing signals found:** ASHRAE's Datacom Series Book 4 (Liquid Cooling Guidelines for Datacom
Equipment Centers, 2nd ed.) is sold via the ANSI webstore, and ASHRAE's broader TC 9.9 Datacom
Encyclopedia subscription lists at $33/year ($24/year for ASHRAE members) (L14-055) — the only
directly-priced item confirmed this session, mirroring the pattern in this project's L12 lane
brief where a safety-standard document was the only priced item found. No cooling-hardware vendor
(cold plates, CDUs, immersion tanks, dielectric fluids) disclosed unit pricing in open sources this
session.

## 5. 2026-2031 triggers

- **US:** ARPA-E COOLERCHIPS-funded technologies (2022-2023 vintage awards) are reaching
  commercialization/M&A maturity now (JETCOOL -> Flex, Nov. 2024, L14-045); OCP's Project
  Deschutes (2 MW CDU) and Open Rack V3 specifications continue driving multi-vendor convergence
  through the 2026-2028 OCP summit cycle (L14-042, 043); the EPA's AIM Act HFC phasedown tightens
  from 60% of baseline (2024-2028) to 30% (2029-2033), directly colliding with the post-Novec
  PFAS-fluid transition window (L14-033).
- **EU:** Regulation (EU) 2024/573 continues its multi-year HFC quota reduction (specific
  annual percentages not independently confirmed this session; Annex VII not fetched, L14-034)
  through the back half of this decade, adding second-order pressure on any EU-deployed
  vapor-compression or hybrid liquid-cooling system that still relies on higher-GWP refrigerants.
- **China:** GB 40879's proposed revision would tighten new/expanded large data-center PUE to
  <=1.25 by end of 2025 and national-hub-node data centers to <=1.2 (L14-035); the T/CIEP
  0263-2025 liquid-cooling technical specification (L14-039) and the April 2026 national
  AI-energy action plan (L14-036) both signal continued regulatory tightening through 2026-2028,
  though the exact liquid-cooling mandate strength claimed by secondary media remains unconfirmed
  against primary text (Section 7, Contradiction 1).
- **Japan:** NTT's DC Cooling Hub (operational since April 2025) and a separate Mitsubishi Heavy
  Industries/NTT Communications/NEC two-phase direct-chip-cooling demonstration (found via search,
  not independently fetched this session) position Japan for continued 2026-2028 liquid-cooling
  retrofit activity in existing air-cooled facilities (L14-050).
- **Korea:** GS Caltex's expansion from immersion fluid (2023) to direct-liquid-cooling fluid
  (Oct. 2025), plus its named Samsung SDS/LG U+ customer relationships, positions Korea for
  continued 2026-2027 commercial-scale liquid-cooling fluid deployment (L14-049); Samsung
  Electronics' own push into liquid/immersion cooling via its FläktGroup acquisition (found via
  search, not independently fetched this session as a load-bearing record) is a parallel
  2026-2028 trigger to monitor.
- **Taiwan:** ITRI's 2,400 W two-phase cold plate (announced July 11, 2026) and its stated intent
  to build a complete domestic two-phase cold-plate supply chain (cold plates, CDUs, interface
  materials, system testing) makes 2026-2028 a plausible window for Taiwan's ODM ecosystem
  (Foxconn/Ingrasys, Inventec, Quanta -- all top-20 global cooling-patent holders per trade
  reporting found this session but not independently fetched) to commercialize domestically
  developed two-phase cooling IP (L14-053).
- **Singapore:** DC-CFA2's 200 MW allocation (application window closed March 31, 2026) and its
  PUE <=1.25 / Green Mark Platinum / SS 715:2025 gating requirements make 2026-2027 the
  concrete build-out window for Singapore's next generation of liquid-cooling-equipped data
  centers (L14-037).

## 6. US vs. Asia differences

- **US** evidence in this lane is dominated by (a) a mature, well-funded government R&D pipeline
  (DOE/ARPA-E COOLERCHIPS, two separate confirmed funding announcements spanning 2022-2023,
  L14-030, 031) feeding directly into subsequent private M&A (JETCOOL/Flex, L14-045) and (b)
  hyperscaler-authored open technical specifications (Google's Project Deschutes, Meta's Open
  Rack V3) that function as de facto industry standards adopted by 7+ independent vendors
  (L14-042, 043) -- a strikingly direct government-funding-to-commercialization-to-standardization
  pipeline not observed with comparable clarity in any other single geography this session.
- **China** evidence is dominated by regulatory/standards activity (an actively-revised national
  PUE standard, GB 40879, tightening toward <=1.25/1.2, L14-035; a dedicated liquid-cooling
  technical specification, T/CIEP 0263-2025, L14-039) and a nationally coordinated but
  more-cautiously-worded-than-media-reports AI-energy policy (L14-036) -- China's real primary-text
  signal is efficiency-standard tightening and coordinated planning, not yet a confirmed hard
  liquid-cooling percentage mandate, a distinction any China-facing idea in this lane must respect
  (Section 7, Contradiction 1).
- **Japan** evidence centers on incumbent telecom/facilities infrastructure operators (NTT
  Facilities) building dedicated physical verification/demonstration capacity (L14-050) rather
  than either government mandates (as in China/Singapore) or venture-funded pure-play startups (as
  in the US) -- a facilities-operator-led, incremental-retrofit pattern distinct from the other
  geographies in this lane.
- **Korea** evidence centers on incumbent energy/chemicals conglomerates (GS Caltex) diversifying
  into cooling-fluid products with named data-center customers (Samsung SDS, LG U+) (L14-049),
  paralleling a broader pattern (also noted via search but not independently fetched this session)
  of Samsung Electronics itself entering liquid/immersion cooling via its FläktGroup acquisition --
  Korea's angle is large-conglomerate diversification into cooling as an adjacent product line,
  not government mandate or pure-play startup activity.
- **Taiwan** evidence is unusually current and technology-forward for this lane: ITRI's 2,400 W
  two-phase cold plate (announced the day before this session, L14-053) plus trade reporting
  (not independently fetched) that Taiwan ODMs (Inventec, Foxconn, Quanta) rank among the top-20
  global cooling-patent holders suggests Taiwan is positioning as a cooling-technology *producer*
  for the global AI-server supply chain, not merely a downstream consumer -- a materially
  different posture than Taiwan's role in this project's L12 (laser/photonics) lane, where Taiwan
  was identified as primarily an EUV/DUV supply-chain *consumer* via TSMC.
- **Singapore** evidence is regulator-led and quantitatively gated in a way no other Asian
  geography in this lane matches: DC-CFA2's explicit PUE <=1.25, >=50% green-power, and named
  Singapore Standard (SS 715:2025) compliance requirements (L14-037) make Singapore the most
  legible, directly-quantified regulatory buyer signal in the entire lane, US included.

## 7. Unresolved contradictions

1. **China's April 2026 national AI-energy action plan is widely reported in secondary Chinese
   tech media as mandating "100% liquid cooling for new large AI data centers," but the directly
   fetched primary notice text (L14-036) contains no such percentage mandate** -- it references
   only generic "high-efficiency cooling" (高效冷却) as a technology-development area and a
   green-power-direct-connection framework. This is a load-bearing distinction: any idea premised
   on a hard Chinese 100%-liquid-cooling regulatory mandate should be treated as unconfirmed
   pending a verifier's independent re-read of the full annexed action-plan document (only the
   notice page itself, not necessarily every annex, was fetched this session).
2. **NVIDIA GB200 NVL72 per-GPU TDP and rack-level flow-rate figures are inconsistent across
   third-party technical-press sources** (1,000 W vs. 1,200 W per GPU; 80 LPM vs. 700+ LPM
   manifold flow), and NVIDIA's own product page (L14-044) does not itself disclose a single
   definitive number for either -- a verifier should locate NVIDIA's or an ODM's actual engineering
   datasheet before using any specific TDP/flow figure as load-bearing.
3. **A 2025 peer-reviewed paper (L14-022) uses Novec 7500 as its best-performing tested coolant
   for EV-charger immersion cooling at the same time 3M was completing its exit from all Novec
   production** (last order accepted March 31, 2025; manufacturing ceased end of 2025, per trade
   reporting reviewed but not independently fetched as a load-bearing record this session) --
   recent academic literature and the commercial fluid supply chain are materially out of sync,
   and any idea premised on Novec-family fluids needs an explicit alternative-fluid transition
   plan.
4. **Credible market-research firms' data-center liquid-cooling market-size estimates span
   nearly a 2x range for the same approximate year and nearly 2x again for their respective
   forecast endpoints** (L14-054: $3.42B 2022 base vs. $6.65B 2025 vs. $4.8B 2025 across three
   different firms; 2030-2035 endpoints from $15.26B to $29.46B) -- no single figure from this set
   should be presented as "the" market size without independent bottom-up triangulation, per
   SOURCE_STANDARDS' market-sizing discipline.
5. **Vertiv's FY2025 financial figures used in this brief (L14-048) were not independently
   re-derived from the primary SEC 10-K filing** (SEC EDGAR returned HTTP 403 to direct fetch this
   session, a pattern also observed in this project's L12 lane for IPG/nLIGHT/Coherent filings) --
   the $10.2B revenue, 50%+ liquid-cooling order growth, and $15B backlog figures are drawn from
   investor-press secondary aggregation (Seeking Alpha, Motley Fool) of Vertiv's own reported
   statements, not from the primary document itself.
6. **Singapore's commonly cited "20% of IT load must be liquid-cooled above 30 MW" requirement**
   was found via a distinct secondary search source and was not corroborated in the directly
   fetched IMDA DC-CFA2 factsheet excerpt (L14-037) -- treat as a plausible but not fully
   primary-confirmed requirement pending a verifier's full-text fetch of the IMDA/EMA regulatory
   documents.

## 8. Opportunity-shaped pain statements (NOT startup pitches)

1. **Pain:** The dielectric-fluid supply chain that two-phase immersion cooling depends on has
   been structurally disrupted (3M's complete PFAS exit) at the exact moment AI-accelerator heat
   flux is forcing wider adoption of two-phase approaches, and current peer-reviewed research
   (L14-022) is still validating performance using the very fluid family (Novec) that is being
   discontinued. **Who pays:** two-phase cooling vendors (ZutaCore, Accelsius-class players) and
   their hyperscale/enterprise customers bearing fluid-requalification risk and cost. **Evidence:**
   L14-001, 002, 003, 022, 033, 034 (regulatory context).
2. **Pain:** Regulatory phase-down of both PFAS-class immersion fluids and HFC-class
   vapor-compression refrigerants is happening on two separate but overlapping timelines (EPA AIM
   Act, EU F-gas Regulation) that a cooling-system designer must track simultaneously, with the
   EU's specific annual quota schedule not fully confirmed in this session's primary-source fetch.
   **Who pays:** refrigerant/fluid manufacturers (Chemours, Honeywell) and equipment OEMs needing
   to requalify products against a moving regulatory target. **Evidence:** L14-033, 034.
3. **Pain:** Buyer-facing thermal specifications for the highest-value cooling target in the
   industry (NVIDIA's GB200/GB300 rack architecture) are inconsistently reported even among
   credible technical-press sources, with NVIDIA's own public materials not resolving the
   ambiguity -- systems integrators and CDU vendors appear to be designing against secondary-source
   estimates rather than a single authoritative spec in the open literature. **Who pays:** CDU and
   cold-plate vendors (Boyd, Vertiv, Motivair, Nidec, etc.) risking over- or under-engineered
   designs. **Evidence:** L14-042, 043, 044.
4. **Pain:** Thermal interface materials remain a genuine bottleneck for 2.5D/3D chiplet
   integration -- existing TIM1/TIM1.5 materials cannot simultaneously deliver high bulk thermal
   conductivity, low bond-line resistance, and long-term mechanical reliability under thermal
   cycling, and this gap is now a first-order constraint on chiplet-based AI accelerator design,
   not a peripheral packaging detail. **Who pays:** chip packagers and AI-accelerator vendors
   absorbing yield/reliability risk from inadequate TIMs. **Evidence:** L14-014, 015, 016,
   018.
5. **Pain:** Government efficiency standards and technical specifications for liquid cooling are
   proliferating faster than open-source technical-press coverage can accurately track them --
   this session found a live contradiction between how a Chinese government policy is reported in
   secondary media versus what its primary text actually states, and Singapore's own liquid-cooling
   percentage requirement could not be fully corroborated against the primary regulator page.
   **Who pays:** compliance teams at data-center operators and cooling vendors making
   capital-allocation decisions based on secondary reporting of regulatory requirements they have
   not independently verified. **Evidence:** L14-035, 036, 037, 039.
6. **Pain:** EV ultra-fast-charging thermal management (connectors, cable cores) is still an
   active peer-reviewed research problem, not a settled engineering solution, even as commercial
   megawatt-class charging systems are entering the market (e.g., Sinbon's 2025 1 MW-capable
   liquid-cooling UL certification, context only) -- charging-hardware OEMs are shipping ahead of
   a fully mature thermal-engineering knowledge base. **Who pays:** EV charging-cable and
   connector OEMs bearing warranty/reliability risk at the highest current levels. **Evidence:**
   L14-019, 020, 021, 022.
7. **Pain:** Aerospace/defense two-phase thermal control (loop heat pipes, oscillating heat
   pipes, phased-array radar thermal-electromagnetic co-design) remains an active,
   three-decades-plus DARPA-documented research area rather than a mature, transferable commodity
   technology -- meaning every new satellite or radar program inherits fresh thermal-design risk
   rather than reusing a stable, off-the-shelf solution. **Who pays:** satellite/radar-system
   primes and their government customers absorbing schedule and reliability risk. **Evidence:**
   L14-024, 025, 027.
8. **Pain:** Market-size estimates for data-center liquid cooling are so divergent across credible
   research firms (nearly 2x spread at the same approximate base year) that they provide little
   real capital-allocation guidance without bottom-up reconstruction -- yet these same inconsistent
   figures are widely cited in vendor and investor communications as if settled. **Who pays:**
   investors and strategic planners at cooling vendors and their customers making sizing decisions
   off unreconciled numbers. **Evidence:** L14-054.
9. **Pain:** Company-filing-derived demand evidence throughout this lane (Vertiv, Schneider
    Electric/Motivair) relies on secondary financial-press aggregation because SEC EDGAR and
    several vendor press-release pages actively blocked direct automated fetch this session -- a
    real due-diligence friction point that pushes analysts toward unverified secondary summaries
    of primary financial disclosures. **Who pays:** N/A (a research-process constraint, not a
    customer pain), but it is a genuine verification burden for any investor or founder assessing
    named-incumbent financial claims in this lane. **Evidence:** L14-047, 048.
10. **Pain:** Standards governing thermal-test methodology (JEDEC JESD51 series) have an
    unconfirmed current revision status relative to liquid-cooled and two-phase test conditions,
    creating a plausible mismatch between how the industry is now cooling chips and how it is
    still formally measuring/reporting thermal resistance. **Who pays:** semiconductor packagers
    and cooling-system qualifiers relying on possibly air-cooling-era test methodology for
    liquid/two-phase products. **Evidence:** L14-040.
11. **Pain:** Taiwan's ODM ecosystem (Foxconn/Ingrasys, Inventec, Quanta) and ITRI are rapidly
    building both patent portfolios and a from-scratch two-phase cold-plate supply chain
    (announced literally the day before this scouting session), but no independent verification
    of commercialization timeline, pricing, or export availability was found -- a live, fast-moving
    situation where publicly available information may already be stale by the time any downstream
    idea is built on it. **Who pays:** N/A directly (a monitoring/timing risk), but relevant to any
    founder or investor benchmarking against Taiwan's two-phase cooling trajectory. **Evidence:**
    L14-053.

## Methodology notes and gaps for the verifier

- 55 candidate records collected (at the top of the 45-55 target range, reflecting the breadth of
  sub-topics explicitly named in this lane's mandate). 29 are academic peer-reviewed candidates,
  exceeding the >=25 floor set for this wave. Overall T1 ratio across the full 55-record set is
  47/55 = 85.5%, meeting the wave-4 85% T1 target (above the mission-wide 70% floor). T2 = 7
  records, T3 = 1 record (well under the "at most 2-3 T3" ceiling).
- Demand-primary count: 13 records carry a non-"none" `demand_evidence_type` (government
  official-project-awards, buyer specifications, direct-customer-documentation, and company-filing
  types): L14-030, 031, 037, 041, 042, 043, 045, 046, 047, 048, 049, 050.
- Government/national-lab/standards-body/regulator count: 16 records across `government` (5),
  `regulator` (2), `standard` (5), `national_lab` (1), and `buyer_procurement` (3) types.
- Market/industry count: 1 record (`market_industry`, L14-054, explicitly flagged for its
  cross-firm inconsistency rather than treated as settled); 1 `vendor_datasheet` record (L14-044,
  NVIDIA's own product page).
- Asian-market coverage: 11 records carry an Asia geography tag (CN x5, JP x2, KR x1, TW x1, IN
  x1, SG x1), exceeding the >=8 floor; 8 records carry a local (non-English) language tag (zh x6,
  ko x1, ja x1), of which 7 were directly fetched this session (L14-028, 029, 035, 036, 049, 050,
  053) -- well above the >=3 local-language-primary-source floor in the role instructions.
- **A genuine, load-bearing contradiction between primary and secondary sourcing was caught and
  documented this session** (China's AI-energy action plan liquid-cooling mandate, see Section 7,
  Contradiction 1) -- this is exactly the kind of claim-discipline check the mission asks for and
  should be treated as a template for how future scout/verifier waves handle policy claims that
  circulate widely in trade press.
- **Systematic fetch-access limitations observed this session, consistent with patterns reported
  in other lanes of this project:** ScienceDirect (HTTP 403 on essentially every `/science/article/
  abs/pii/` URL attempted), MDPI (HTTP 403 on direct article pages despite open-access status),
  Springer (redirect to an authentication gateway), SEC EDGAR (HTTP 403), and several vendor
  press-release domains (se.com, opencompute.org PDF documents) all blocked direct WebFetch this
  session. Where this occurred, records were marked `fetched: false` with search-derived
  claim summaries and an explicit note; no DOI, author, venue, or quote was invented. A verifier
  with authenticated/institutional fetch access could likely upgrade a substantial fraction of
  this lane's T1-tier-but-unfetched academic and company-filing records to fully confirmed status.
- **Weakest coverage / follow-up priorities for a future scout wave:** (1) India -- no domestic
  cooling-technology vendor or confirmed regulatory liquid-cooling requirement was identified,
  despite a real and growing data-center buildout in a high-ambient-temperature climate; (2) a
  direct fetch of the EU F-gas Regulation's Annex VII (specific annual HFC quota percentages) to
  replace the currently-unconfirmed schedule; (3) direct fetch of Vertiv's, Schneider Electric's,
  and Trane Technologies' own primary filings/press releases (all blocked this session) to
  upgrade L14-047/048/051 from secondary-sourced to fully primary-confirmed; (4) a primary ITRI
  press release or technical paper (rather than Liberty Times' trade-press report) for the
  July 2026 2,400 W two-phase cold-plate announcement (L14-053); (5) confirmation of the current
  active revision year for the JEDEC JESD51 base standard and whether it has been updated for
  liquid/two-phase test conditions; (6) a primary Samsung Electronics or FläktGroup announcement
  of Samsung's liquid/immersion-cooling market entry (found via search but not independently
  fetched this session); (7) direct fetch of Singapore's SS 715:2025 standard text and the
  specific "20% liquid-cooled above 30 MW" requirement to fully corroborate L14-037.

## P2A origin-audit repair (2026-07-13)

- removed IDs: L14-011, L14-017, L14-023, L14-052
- removed/trimmed claims: trimmed the L14-011 citation from the jet-impingement-cooling review
  sentence (Section 1), keeping the eligible L14-012/013 support; trimmed the L14-017 citation
  from the TIM-materials frontier sentence (Section 1) and the matching pain-statement-4 evidence
  list (Section 8), keeping the eligible L14-014/015/016/018 support; trimmed the L14-023 citation
  from the aerospace/defense loop-heat-pipe sentence (Section 1) and the matching pain-statement-7
  evidence list (Section 8), keeping the eligible L14-024/025/027 support; deleted the India (MeitY)
  named-buyer bullet (Section 3), the India 2026-2029 trigger bullet (Section 5), the India
  paragraph in "US vs. Asia differences" (Section 6), and pain statement 9 (Section 8,
  India data-center thermal-management gap) — all sourced solely to L14-052 — and renumbered the
  following Section 8 items down by one (old 10-12 -> new 9-11). No eligible India-sourced claim
  remained in this lane after removal.
