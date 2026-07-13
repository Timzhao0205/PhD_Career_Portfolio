# L01 — Industrial Plasma, Plasma Chemistry, and Plasma Power Supplies

Lane scout brief. Sources cited as `L01-0NN` refer to `10_SOURCE_ATLAS/L01_raw_sources.json`
(55 candidate records, all `accepted: false` pending verifier review). This document does not
propose startup ideas; it summarizes evidence for later phases. Founder background was not used
to select topics within this lane.

## 1. Frontier state

Industrial plasma splits into four evidence clusters found this session:

- **Plasma chemistry / electrification of chemical conversion.** Non-thermal and gliding-arc
  plasma for N2 fixation (ammonia/NOx fertilizer), CO2 conversion (to CO, methanol, higher
  hydrocarbons), and VOC/odor abatement is a large, active peer-reviewed literature (L01-001–005,
  007–009, 014–021, 025, 027–029). Reactor engineering has moved from single-cell demonstrations toward
  numbering-up/sizing-up strategies (L01-014, 015, 016) explicitly aimed at industrial throughput,
  but review articles as recent as 2020–2024 still describe the technology as pre-industrial
  (L01-009, L01-028: "currently only performed on lab-scale... not yet implemented in industrial
  processes").
- **Atmospheric-pressure surface treatment.** A mature, already-commercial equipment category
  (textiles, packaging, electronics, medical, automotive), i.e., low capex per tool but a
  large *installed base* opportunity.
- **RF/pulsed power supplies and matching networks.** A duopoly-like vendor structure (Advanced
  Energy, MKS/Plasmart, Comet, TRUMPF Hüttinger) supplies 13–60 MHz, sub-kW to tens-of-kW RF
  generators plus real-time impedance-matching electronics (L01-012, 013, 040, 049, 050). Advanced
  Energy explicitly frames "plasma power" as a named growth product line with new platforms
  (Everest, EVOS, NavX) generating "double-digit millions" in 2025 (L01-040).
  Semiconductor-etch/deposition end demand is the dominant revenue driver for this hardware today
  (L01-040, L01-044), which is adjacent to but distinct from L06's semiconductor-fab scope — this
  lane's angle is the plasma power-electronics/matching-network layer itself, usable across
  non-semiconductor industrial plasma too.
- **Plasma torches and thermal plasma processing** (waste gasification, metal cutting, PFAS
  destruction, vitrification). This is where the clearest *paid, delivered* US demand sits
  (PyroGenesis contracts, L01-034/035/036).

## 2. Bottlenecks

- **Energy efficiency vs. Haber-Bosch/incumbent thermal routes.** ARPA-E's own framing (per
  search-summary, L01-030, unconfirmed by direct fetch) is that plasma nitrogen fixation needs a
  ~10x efficiency improvement just to match Haber-Bosch — i.e., the incumbent thermochemical
  process, not the plasma process, remains the efficiency benchmark to beat.
  A verifier must re-fetch L01-030 before this number is used in any downstream idea.
- **Reactor scale-up is still additive ("numbering up"), not a single large reactor.** L01-014,
  015, 016 all describe parallelizing many small plasma cells rather than building one big one —
  this changes the economics (many small power supplies + many matching networks, not one big
  one) and is a mechanical/reliability burden distinct from thermal-plant scale-up.
  Non-thermal plasma physics (short-timescale, non-equilibrium electron energy distribution) does
  not scale the way thermal reactors do — bigger volumes lose the non-equilibrium character that
  makes selective chemistry work.
- **RF/matching-network engineering complexity** rises with multi-frequency "tailored voltage
  waveform" plasma control (L01-012, 013) — a real, active area of publication, meaning
  state-of-the-art matching is still a research problem, not a solved commodity, at the frontier
  end of the market even though basic RF generators are commoditized (L01-049, 050).

## 3. Named buyers and spending signals

- **PyroGenesis Canada Inc.** (TSXV: PYR) — three confirmed contracts with a confidential "prime
  aeronautics, defense, and military contractor for the U.S. government": CAD$4.1M (4.5MW plasma
  torch, 2023, L01-034), $27M (20MW plasma torch, Oct 2024, L01-035), and a separate US DoD
  contract worth $2.25M for PFAS ("forever chemical") destruction that treated >300 tonnes of
  contaminated material (completed Dec 2024, L01-036). Backlog rose to >$55M (+90%) after the
  $27M award. This is the single clearest paid-and-delivered US industrial-plasma demand signal
  found this session.
- **US Department of Defense** — direct buyer via the PyroGenesis PFAS contract (L01-036);
  AECOM-cited $200B US / $250B global PFAS remediation addressable market (unverified, vendor/
  trade-press sourced).
- **Institute of Plasma Physics, Chinese Academy of Sciences (ASIPP)** — two active 2025/2026
  tenders for plasma power electronics: ITER PF converter control modules (L01-037) and an "RMP
  power supply system expansion/renovation" (L01-038). Both are fusion-research buys, not
  general-industry buys, but they are real, dated, named-institution procurement.
- **China Aviation Industry Corporation (AVIC), Xi'an Flight Automatic Control Research
  Institute** — awarded a PECVD (plasma-enhanced CVD) equipment contract via China's official
  MOFCOM e-procurement portal, announced 2026-03-19 (L01-039). Defense-industrial buyer of
  plasma-deposition equipment.
- **NEDO (Japan)** — funding a FY2025–2027 "ammonia and plasma" carbon-recycling R&D project
  (Tokai National Universities + Kawada Industries) under its CO2 Effective Utilization Hub,
  targeting practical implementation ~2030 (L01-043).
- **Nitricity, Inc. (US)** — production at its Delhi, CA plasma-nitrogen fertilizer plant is
  reported "sold out through 2028" under agreements with local organic growers (L01-031) — a rare
  case of confirmed forward customer commitment, not just investor funding.
- **N2 Applied AS (Norway)** — partnered with global livestock-equipment maker GEA for
  distribution of plasma-treated slurry fertilizer technology (L01-033).
- **Advanced Energy Industries (NASDAQ: AEIS)** — FY2025 revenue $1.8B, semiconductor segment
  $840M; explicitly names "plasma power" as a >$1B addressable-market product category in
  investor communications (per search synthesis; the Q4 2025 transcript itself, L01-040, confirms
  segment revenue but not the specific $1B figure — flag for verifier).
- **Chinese plasma-equipment vendors (NAURA, Piotech, ACM Research)** — all reported strong Q1
  2026 revenue growth (+26–57% YoY, L01-044), indicating continued Chinese capital-equipment
  demand, primarily semiconductor-linked.

## 4. Incumbent map (companies, products, price signals)

| Company | Product | Signal |
|---|---|---|
| Advanced Energy Industries (US) | Everest, EVOS, NavX RF/plasma power generators | FY2025 $1.8B revenue; new platforms in early production ramp (L01-040) |
| MKS Instruments (US, incl. Plasmart) | RF plasma generation/monitoring systems | Q1 2026 semiconductor segment $466M (43% of revenue) per trade press; SEC 10-K fetch blocked (403), unconfirmed directly |
| Comet Group / Comet PCT (Switzerland) | Synertia, cito Plus, cito RF generators | 13–60 MHz, 0.6–6 kW, pulsing to 100 kHz (L01-050); no price disclosed |
| TRUMPF Hüttinger (Germany) | TruPlasma RF Series 1000/3000 | Claims up to 80% efficiency, 50% energy-cost cut vs. conventional (L01-049, vendor claim) |
| PyroGenesis Canada Inc. | MW-class plasma torches (1MW–20MW) | $4.1M/$27M/$2.25M US contracts (L01-034/035/036) |
| InEnTec (US) | Plasma Enhanced Melter (PEM) | 13 facilities worldwide (per search synthesis, L01-053 context) |
| OMNI Conversion Technologies | OMNI200 GPRS plasma-refining gasifier | 200 t/day capacity claim, "99.95% tar removal" (L01-053, vendor claim via industry association) |
| Nitricity, Inc. (US) | Non-thermal plasma N-fixation reactor | $50M Series B (L01-032); Delhi, CA plant sold out through 2028 (L01-031) |
| N2 Applied AS (Norway) | Plasma-treated slurry fertilizer unit | €10M raised, GEA distribution partnership (L01-033) |
| KIMM (Korea, government institute) | Full-spectrum plasma equipment (vacuum→atmospheric) | "World-first" semiconductor-contamination-removal plasma equipment commercialized 2013 (L01-047) |
| NAURA / Piotech / ACM Research (China) | Plasma etch/deposition tools | Q1 2026 revenue +26–57% YoY (L01-044) |

**Pricing signals found:** RF generators 0.6–6 kW commodity-priced but undisclosed
(L01-049, 050); MW-class plasma torches run into the multi-million-dollar range per unit
(L01-034/035 implied by $4.1M/$27M contract values, though contracts likely bundle engineering,
integration, and multi-year service, not a single unit price).

## 5. 2026–2031 triggers

- **Japan:** NEDO's FY2025–2027 ammonia-plasma carbon-recycling project targets practical
  implementation "around 2030" (L01-043) — a concrete government-funded timeline.
- **US:** PyroGenesis' 20MW torch contract runs ~3 years from Oct 2024 (i.e., through ~2027,
  L01-035); continued DoD PFAS-destruction demand is plausible given the cited $200B US
  remediation TAM (unverified vendor/trade-press figure, L01-036).
  US EPA-driven PFAS regulation (not independently confirmed this session — flagged for
  government/regulator lane cross-check) is the most likely regulatory trigger multiplying this
  demand 2026–2031.
- **China:** Two live 2025/2026 ASIPP tenders (L01-037, 038) plus a March 2026 AVIC PECVD award
  (L01-039) show continued state-institute capital deployment into plasma power electronics;
  China's VOCs emissions-standards regime (2020 Management Plan, per search synthesis around
  L01-related searches, not independently fetched this session) is a plausible regulatory trigger
  for non-thermal-plasma VOC-abatement equipment demand — needs a dedicated regulator-source fetch
  in a follow-up wave.
- **Standards:** ISO 24674:2022 (plasma nitriding + PVD coatings on cold-work mould steels,
  L01-046) is a recent (2022) standard, suggesting active tooling-industry standardization —
  a proxy signal for continued industrial adoption of plasma nitriding in precision tooling.

## 6. US vs. Asia differences

- **US** evidence in this lane skews toward (a) defense/DoD-linked plasma-torch and remediation
  contracts (PyroGenesis, L01-034-036) and (b) RF/plasma-power-supply public-company revenue
  (Advanced Energy, MKS) tied mostly to semiconductor capex cycles, plus (c) a deep bench of
  university/national-lab (Sandia, L01-045) fundamental plasma science.
- **China** evidence found this session is dominated by state-research-institute procurement
  (ASIPP fusion-adjacent tenders, L01-037/038) and defense-industrial-complex equipment buys
  (AVIC/Xi'an institute, L01-039), plus commercial semiconductor-equipment vendor growth
  (NAURA/Piotech/ACM, L01-044) — i.e., government and quasi-government buyers dominate the
  Chinese evidence trail collected here, more than commercial industrial end-users.
- **Korea** evidence (KIMM, L01-047) shows a government research institute that has already
  achieved a "world-first" plasma-equipment commercialization (semiconductor contamination
  removal, 2013) — Korea's plasma-equipment ecosystem appears semiconductor-anchored, similar to
  the US MKS/Advanced Energy pattern, but state-research-institute-led rather than pure-private.
- **Singapore** evidence (A*STAR SIMTech, L01-055) is older (2013) and research-stage
  (roll-to-roll PET activation for solar coatings) with no confirmed commercialization outcome —
  weakest demand signal of the Asian sources collected.
- Overall: this session found **more confirmed paid-and-delivered demand in the US** (PyroGenesis'
  three contracts) than in any single Asian market; Asian evidence is stronger on **government
  R&D funding commitments and state-institute procurement** than on confirmed commercial revenue.

## 7. Unresolved contradictions

1. **ARPA-E/Nitricity award details are unconfirmed.** The only mention of a specific ARPA-E
   dollar figure and "10x efficiency" target for plasma nitrogen fixation (L01-030) could not be
   verified by direct fetch this session (page returned only navigation chrome). Nitricity's own
   $50M Series B announcement (L01-032) does not mention any ARPA-E/DOE award at all. This
   specific claim should not be used until independently re-confirmed.
4. **Whether Advanced Energy's "$1B plasma power market" framing is confirmed.** The Q4 2025
   transcript fetch (L01-040) confirmed segment revenue figures but did NOT surface the specific
   ~$1B addressable-market claim attributed to the company in initial search summaries — flag as
   unconfirmed pending a dedicated investor-day or 10-K fetch.
5. **China VOCs-standard regulatory trigger** was identified only via search synthesis, not a
   directly fetched primary MEE (Ministry of Ecology and Environment) document this session —
   the regulatory-trigger claim in Section 5 should be treated as a lead, not confirmed evidence.

## 8. Opportunity-shaped pain statements (NOT startup pitches)

1. **Pain:** Non-thermal/gliding-arc plasma reactors for chemical conversion (N2 fixation, CO2
   conversion) cannot scale as single large units — the whole field is stuck "numbering up" many
   small cells, each needing its own power supply and matching network, which multiplies capital
   and reliability burden. **Who pays:** distributed-fertilizer and carbon-recycling project
   developers (Nitricity, N2 Applied, NEDO-funded consortia). **Evidence:** L01-014, 015,
   016, 031, 033, 043.
2. **Pain:** RF plasma power supplies for advanced multi-frequency "tailored voltage waveform"
   processes still require bespoke, actively-researched impedance-matching solutions — commodity
   matching networks do not cover the frontier use case. **Who pays:** semiconductor-adjacent and
   advanced-materials plasma-process developers licensing from Advanced Energy/MKS/Comet/TRUMPF.
   **Evidence:** L01-012, 013, 040, 049, 050.
3. **Pain:** PFAS ("forever chemical") remediation has an actively growing, currently-funded US
   federal buyer (DoD) willing to pay multi-million-dollar contracts for plasma-torch-based
   destruction, but only one confirmed vendor (PyroGenesis) with delivered contracts found this
   session — a thin, concentrated supplier base against a reportedly $200B+ addressable
   remediation market. **Who pays:** US DoD and (per vendor claims) broader industrial/
   environmental-remediation buyers. **Evidence:** L01-036.
4. **Pain:** Defense/aerospace primes are already paying tens of millions of dollars for
   ever-larger (4.5MW → 20MW) commercial plasma torches from a single small-cap Canadian supplier,
   implying an internal need (described only as "critical defense, military, and aeronautics
   challenges," confidential) that is scaling faster than the supplier's own prior backlog.
   **Who pays:** a confidential US aeronautics/defense prime contractor. **Evidence:** L01-034,
   035.
5. **Pain:** Chinese state research institutes (ASIPP) and defense-industrial buyers (AVIC/
   Xi'an institute) are actively procuring high-voltage/high-current plasma power electronics
   and PECVD equipment via public tenders, but technical specification detail is opaque (PDF
   text extraction failed for the two ASIPP tenders this session) — meaning competitive/pricing
   intelligence on this specific demand is currently poor from open sources. **Who pays:**
   Chinese state research institutes and state-owned aviation-industry buyers. **Evidence:**
   L01-037, 038, 039.
6. **Pain:** Livestock-slurry and organic-fertilizer plasma-treatment ventures (N2 Applied,
   Nitricity) are reporting real forward customer commitment (sold-out capacity, distribution
   partnerships) years before reaching industrial-average cost parity with Haber-Bosch ammonia —
   suggesting the customer segment (small/regional organic growers, livestock operations) may
   value on-site/low-carbon sourcing enough to pay a premium over pure $/kg-N economics.
   **Who pays:** regional organic growers (Nitricity, California) and livestock/dairy operations
   (N2 Applied, via GEA). **Evidence:** L01-031, 033.
7. **Pain:** Plasma nitriding of precision tool steels has an actively updated international
   standard (ISO 24674:2022) and continuing peer-reviewed materials-science output (L01-022, 023,
   024), suggesting steady industrial tooling demand, but no primary-source pricing, volume, or
   named-buyer procurement evidence was found this session for plasma-nitriding *service* or
   *equipment* purchases specifically (as opposed to general market reports). **Who pays:**
   precision toolmakers/mold-makers (unconfirmed which specific buyers). **Evidence:** L01-022,
   023, 024, 046.
8. **Pain:** Non-thermal plasma VOC/odor abatement has strong peer-reviewed technical support
    (up to 99% removal claimed in some field tests, L01-025) and a plausible Chinese regulatory
    trigger (VOCs emissions standards), but no confirmed primary buyer-tender or company-filing
    evidence of industrial VOC-plasma-abatement purchases was found this session — this is a
    technology-push story until a named buyer is found. **Who pays:** unconfirmed — likely
    chemical/coatings/printing manufacturers under emissions-compliance pressure. **Evidence:**
    L01-017, 018, 019, 020, 021, 025.

## Methodology notes and gaps for the verifier

- 55 candidate records collected (target range 45-55). 29 are academic_peer_reviewed candidates
  (exceeds the >=25 floor), but only ONE (L01-011, RSC Advances) was independently fetched and
  fully confirmed (title/authors/venue/DOI); the other 28 rely on search-result titles and
  literally-shown DOI strings in URLs — every one of them needs a verifier fetch pass before
  `peer_review_status` can move from `unverified` to `verified`.
- Several important pages could not be fetched this session (403/404): ACS/RSC paywalled article
  pages, ISO catalogue, an FDA guidance-document URL, SEC EDGAR (MKS Instruments 10-K), NETL/DOE
  Westinghouse-plasma page, Fortune Business Insights, and Taiwan Plasma Corporation's history
  page. These are flagged individually in the JSON `notes` fields with `fetched: false` and should
  be retried by a verifier or a follow-up scout with different fetch tooling (the two ASIPP PDF
  tenders were technically fetched but their embedded technical-spec tables could not be extracted
  as text).
  - Taiwan (TW) has no dedicated fetched primary source this session — weakest single-geography
  coverage in the Asia set; a follow-up wave should target ITRI or a Taiwanese plasma-equipment
  vendor directly.
- No SAM.gov/US-federal solicitation search returned a directly relevant open plasma-processing
  tender this session (only general vendor/technical pages) — US federal buyer-tender evidence in
  this lane rests entirely on the already-awarded PyroGenesis DoD contract (L01-036), not on an
  open solicitation.

## T1 top-up addendum (2026-07-12)

15 new, strictly-T1 candidate records collected in `L01_t1topup_raw_sources.json` (IDs
L01-101–115) to raise the lane's T1 share, targeting sub-niches not yet covered by the base
55-record ledger: DBD ozone generation for industrial water treatment (L01-101); plasma
processing/pyrolysis of scrap-tire rubber (L01-102); atomic layer etching physics/chemistry for
SiO2 and Al2O3 (L01-103, 109) as a semiconductor sub-niche distinct from RF-matching-network
electronics; plasma-activated water as an agricultural irrigation/seed-treatment input, distinct
from manufactured-fertilizer plasma-N2-fixation (L01-104); a tunable-electron-energy ICP reactor
paper and a DOE/DoD/ONR-funded nanosecond-pulsed-power SBIR award portfolio, both plasma
power-supply/source-electronics sub-niches distinct from the RF-CW vendor cluster and
ITER/tokamak DC tenders already in the ledger (L01-105, 112); plasma arc welding parameter
optimization, a joining sub-niche with no prior representation (L01-106); cold-plasma
food-contact-surface decontamination, distinct from the VOC/emission-abatement cold-plasma
cluster (L01-107); PEALD barrier-coating deposition on polymers for flexible-electronics
packaging (L01-108); plasma methane pyrolysis carbon-black co-product valorization for batteries
(L01-110); NIST's plasma-process-metrology program as measurement-science infrastructure
(L01-111); an ISO tungsten-electrode standard covering plasma welding/cutting/thermal-spraying
consumables (L01-113); a real, dated Chinese PCB-manufacturer tender for a plasma cleaning
machine (L01-114); and Nordson Corporation's audited FY2025 10-K disclosing its MARCH gas-plasma
surface-treatment product line inside a large diversified filing (L01-115). Mix: 10
academic_peer_reviewed, 2 government, 1 standard, 1 buyer_procurement, 1 company_filing; 14 of 15
fetched successfully this session (only the ISO 6848 standards-catalogue page was blocked with
403, consistent with prior methodology-notes flags in the base ledger; the Nordson 10-K's primary
SEC.gov URL also 403'd but was independently fetched via a StockTitan filing-mirror instead). All
records
`accepted: false`, `peer_review_status` left `unverified`/`not_applicable` per top-up
instructions, pending verifier review.

## P2A origin-audit repair (2026-07-13)

- removed IDs: L01-006, L01-010, L01-026, L01-041, L01-042, L01-051, L01-052, L01-054
- removed/trimmed claims:
  - Trimmed the N2-fixation/CO2/VOC literature range citation to exclude L01-006 and L01-010 (Sec. 1).
  - Deleted the atmospheric-surface-treatment ~73% consultancy market-size-disagreement claim and the ~$5,000-$8,000 unit-price claim (Sec. 1, Sec. 4 pricing paragraph, Sec. 7 contradiction) — needs a re-sourced TAM and unit-price figure from an eligible market-research provider.
  - Deleted the "repeated commercial failures" clause (Air Products, Thermoselect, Plasco, Pune) from the plasma-torches frontier-state bullet (Sec. 1) — needs re-sourcing from eligible providers if this claim is to be retained.
  - Deleted the "Feedstock heterogeneity and tar/contamination management" bottleneck bullet in full (Sec. 2) — needs a fresh, eligible source for the gasification-failure/heterogeneity claim.
  - Deleted the "Market-sizing itself is unreliable" bottleneck bullet in full (Sec. 2).
  - Deleted the NTPC/NETRA India named-buyer entry in full (Sec. 3).
  - Deleted the Westinghouse Plasma Company incumbent-table row in full (Sec. 4) — needs a re-sourced legacy-tech reference if retained.
  - Trimmed InEnTec incumbent-table row to drop the L01-054 citation, keeping only L01-053 (Sec. 4).
  - Deleted the India National Green Hydrogen Mission trigger bullet in full (Sec. 5).
  - Deleted the Japan "historical Westinghouse-licensed plasma-gasification plant" bullet in full (Sec. 6, US vs. Asia) — needs re-sourcing if the historical-Japan-plant claim is retained.
  - Deleted the India government-linked-buyer/Pune-failure bullet in full (Sec. 6, US vs. Asia).
  - Deleted contradiction item "Market size for plasma surface-treatment equipment" (Growth Market Reports vs. Persistence Market Research) in full (Sec. 7).
  - Deleted contradiction item "Plasma gasification: vendor optimism vs. graveyard of failures" in full (Sec. 7) — needs re-sourced evidence on both sides (viability and failure) from eligible providers.
  - Trimmed pain-statement item (numbering-up reactors) evidence list to drop L01-006 (Sec. 8, now item 1).
  - Deleted pain-statement item "Plasma-gasification waste-to-fuel/hydrogen projects keep failing..." in full (Sec. 8) — needs re-sourced heterogeneity/failure and India-NTPC evidence from eligible providers.
  - Deleted pain-statement item "Market-size estimates for even a 'mature'... plasma-equipment category" in full (Sec. 8).
  - Renumbered remaining Sec. 7 contradiction items and Sec. 8 pain-statement items sequentially after deletions.
