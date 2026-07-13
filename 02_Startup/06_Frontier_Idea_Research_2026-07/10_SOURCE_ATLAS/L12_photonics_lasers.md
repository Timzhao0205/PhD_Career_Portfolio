# L12 — Photonics, High-Power Lasers, Beam Control, and Optical Manufacturing Subsystems

Lane scout brief. Sources cited as `L12-0NN` refer to `10_SOURCE_ATLAS/L12_raw_sources.json`
(54 candidate records, all `accepted: false` pending verifier review). This lane covers
industrial fiber/diode/ultrafast lasers, laser power supplies and drivers, beam delivery/scanning
optics, adaptive optics, laser processing heads, co-packaged optics (CPO) power/thermal, EUV/DUV
light-source subsystems, directed-energy support hardware, and precision optical metrology for
manufacturing. Founder background was not used to select topics within this lane. Uncertainty is
flagged explicitly throughout rather than smoothed over.

## 1. Frontier state

- **High-power fiber laser physics is still an active constraint problem, not a solved commodity.**
  Transverse mode instability (TMI) — a thermo-optical effect that abruptly degrades beam quality
  above a power threshold — remains the dominant open limiter on further power-scaling, with
  multiple 2022-2024 peer-reviewed papers still deriving new threshold theories and mitigation
  models (L12-016, 017, 018). Coherent beam combining (CBC) of many fiber channels is the leading
  path past single-fiber limits, with 2024-2025 work demonstrating both new beam-shaping modes
  (L12-001) and record-short-pulse (260 fs, 403 W) combined ultrafast systems (L12-002).
- **EUV light-source physics has not settled even as commercial power climbs.** ASML/Cymer's
  current CO2-laser-driven tin-droplet-plasma source crossed a historic 1,000 W milestone in
  April 2025 (up from 250 W in 2018 and 500 W in 2022), achieved by raising repeat rate from
  60 kHz to 100 kHz (L12-034, directly fetched from ASML's own 2025 annual report). Yet
  peer-reviewed work is simultaneously modeling an entirely different next-generation architecture
  — a 2-micron-wavelength drive laser achieving 5% EUV conversion efficiency instead of the
  10.6-micron CO2 laser (L12-003) — and continuing to refine the underlying atomic-physics model of
  tin-plasma radiative emission (L12-006, 007, 008). EUV source suppliers face a recurring
  architecture-change risk, not a maturing incremental product line.
- **Co-packaged optics (CPO) thermal/power management is a newly urgent, still-unsettled
  subsystem problem** driven by AI-datacenter optical-switch demand: at least four independent
  2024-2026 peer-reviewed treatments of CPO thermal management were found this session (L12-021,
  022, 023, 024), reflecting how concentrated power density on switch-ASIC packages (Broadcom
  reportedly targets 5.5 W per 800 Gb/s port vs. ~15 W for pluggable modules) is forcing liquid-cold-plate
  cooling designs that did not exist as a mainstream requirement three years ago.
- **Nonlinear frequency conversion (second-harmonic generation) is being reinvented at the
  chip scale.** 2024-2025 work reports SHG conversion efficiencies as high as 440,000% W^-1 in
  thin-film lithium-niobate microcavities without periodic poling (L12-012) and on-chip efficiencies
  near 150,000%/W in dual-layer lithium niobate (L12-015) — several orders of magnitude beyond
  bulk-crystal SHG, a potential future path to compact visible/UV sources for laser processing and
  metrology, though these remain low-power microphotonic demonstrations, not yet industrial-power
  building blocks.
- **Laser diode driver electronics remains an active power-electronics research area**, not a
  finished commodity: 2025-2026 papers explore GaN-HEMT high-peak-power pulsed drivers (L12-027),
  LLC-resonant-converter-based modulation-shape comparisons (L12-025), and sub-nanosecond,
  single-digit-picosecond-resolution digital drivers (L12-026) — precision current-pulse control is
  still a differentiator, not a solved problem.
- **Directed-energy laser weapons crossed from demonstrator to funded acquisition program in
  2026.** The U.S. Department of War's Joint Laser Weapon System (JLWS) program awarded $86 million
  in initial contracts (up to $847 million ceiling) to nLIGHT Defense and Lockheed Martin Aculight
  on July 9, 2026 — the week before this scouting session — explicitly to move from prototype to
  field-ready, containerized 150 kW-to-500 kW systems (L12-031, 032, directly confirmed). This is a
  materially different demand signal than the "still transitioning" picture GAO described as
  recently as 2023 (L12-045).
- **Adaptive optics for high-power beam control spans a wide maturity range**, from
  astronomy-derived real-time wavefront stabilization now deployed on multi-petawatt research
  lasers (Apollon, L12-011) to still-active strong-turbulence correction research (L12-010) to a
  distinct, more mature commercial-off-the-shelf component base (Thorlabs deformable-mirror/AO-kit
  product line, L12-052) — the custom high-power/high-energy segment and the commodity component
  segment are not converging.

## 2. Bottlenecks

- **China's fiber-laser price war has compressed margins faster than power-scaling has created
  new addressable demand.** Han's Laser's own 2025 annual report shows high-power laser equipment
  revenue *declining* 6.60% YoY (to RMB 3.16 billion) even as unit shipments of high-power cutting
  machines *rose* 30.47% (to 6,800 units) — direct evidence that per-unit average selling price is
  falling faster than volume is growing in the domestic high-power segment (L12-037). IPG
  Photonics' own FY2025 10-K states plainly that "many of our fiber laser competitors are
  increasing the output powers of their fiber lasers and reducing sales prices to compete with our
  products," naming Raycus explicitly as a competitor (L12-034).
- **TMI remains an unresolved physical ceiling on single-fiber power scaling.** Despite a decade of
  study, 2024 papers are still deriving new semi-analytic TMI-threshold theories (L12-017) and new
  dynamical-systems (Hopf-bifurcation) framings of TMI onset (L12-018) — coherent beam combining
  (L12-001, 002) is the industry's primary workaround, but CBC itself introduces new engineering
  burdens (phase-locking, dispersion management across channels) that are themselves still active
  research topics.
- **EUV source power scaling requires continually re-engineering the drive-laser architecture,
  not just incrementally improving one design.** ASML's own milestone narrative (250 W in 2018,
  500 W in 2022, 1,000 W in April 2025, via a 60 kHz-to-100 kHz repeat-rate increase) shows each
  step required new engineering, not simple scaling (L12-034); simultaneously, peer-reviewed work
  is modeling a fundamentally different 2-micron-laser drive architecture (L12-003) as a longer-term
  alternative — EUV drive-laser suppliers cannot treat the current architecture as a stable target.
- **CPO thermal management has no settled solution and is a new bottleneck for AI-datacenter
  optical switches specifically because power density is now concentrated on the same package as
  the switch ASIC** — four independent 2024-2026 papers proposing different thermal strategies
  (liquid cold-plate, device-to-system thermal co-design, heterogeneous-integration thermal
  crosstalk mitigation) found this session (L12-021 through 024) indicate the field has not
  converged on a dominant design.
- **Directed-energy laser weapon programs still face a documented "valley of death" between
  prototype and fielded acquisition program**, per GAO's still-open 2023 recommendations that the
  Navy and Air Force lack documented transition agreements (L12-045) — even as the July 2026 JLWS
  award (L12-031) suggests DoD is now trying to force this transition with dedicated funding rather
  than waiting for organic program maturity.
- **Standards governing laser safety and laser-processing-machine safety are aging relative to the
  power/precision envelope of current systems.** IEC 60825's base equipment-classification edition
  dates to 2014 (with a 2025 supplementary-parts package, L12-048); ISO 11553-1's laser-safety-
  requirements edition dates to 2020, succeeding a 2005 edition (L12-049); ISO 11553-2 for
  hand-held laser processing devices still carries a 2007 date (L12-050) even as handheld laser
  welding export volumes are growing explosively (Raycus handheld-welding exports +66.22% in 2025,
  L12-038) — a plausible, though not directly evidenced this session, mismatch between standards
  vintage and the newest handheld/high-power product classes.

## 3. Named buyers and spending signals

- **U.S. Department of War (Office of the Under Secretary of War for Research and Engineering,
  SCADE Critical Technology Area)** — awarded Joint Laser Weapon System (JLWS) agreements to
  nLIGHT Defense and Lockheed Martin Aculight on July 9, 2026: $86 million initial award, $847
  million total program ceiling, targeting 150 kW initial prototypes scaling to 300-500 kW
  containerized systems for cruise-missile/drone defense (L12-031, directly confirmed). nLIGHT's
  own announcement specifies its individual award as $44 million initial / up to $627 million
  ceiling (L12-032, search-confirmed, not independently re-fetched).
- **nLIGHT, Inc.** — FY2025 10-K shows Aerospace & Defense revenue growing from $109.5 million
  (2024) to $175.3 million (2025), now the company's largest end market, driven explicitly by
  "increased unit sales of directed energy laser products"; $161.6 million backlog and $184.4
  million in unfunded U.S. government contracts as of December 31, 2025 (L12-033) — real, dated,
  quantified defense-laser revenue growth independent of the July 2026 JLWS award.
- **DARPA (Multi X Office; AMPED program office)** — running at least two concurrent chip-scale/
  modular high-energy-laser programs: AMPED ($39 million Phase 1 + $14 million Phase 2, chip-scale
  single-mode diffraction-limited CW laser architectures, solicitation closed July 9, 2026,
  L12-040, directly confirmed) and MELT (modular "laser tile" building blocks for counter-UAS HEL
  systems, program goals directly confirmed via darpa.mil, L12-041; a $8 million Northrop Grumman
  order reported by trade press but not independently re-confirmed this session).
- **NNSA / Lawrence Livermore National Laboratory** — Enhanced Fusion Yield Capability (EYC)
  project approved to Critical Decision-1 on April 13, 2026, raising NIF's peak laser energy from
  2.2 to 2.6 megajoules; Congress appropriated $26 million in FY2026 to begin the next phase, with
  LLNL developing a long-lead procurement package (L12-042, directly confirmed) — a concrete,
  dated, appropriated national-lab high-power-laser-system upgrade.
- **DARPA (POWER program)** — demonstrated 800+ watts of optical power delivered over 8.6 km in a
  30-second transmission in May 2025, in partnership with Teravec Technologies, Packet Digital,
  RIT, the Naval Research Laboratory, and HELSTF/White Sands (L12-047, directly confirmed) — an
  adjacent directed-laser-power-relay demand signal using the same beam-control building blocks as
  weapon systems.
- **IPG Photonics** — FY2025 total net sales $1,003.8 million (High Power CW Lasers $308.8
  million; China 29% of sales); explicitly names Raycus as a price/power-competing rival in its
  own 10-K risk disclosure (L12-034, search-confirmed via secondary aggregator fetch, canonical
  SEC.gov filing not independently re-fetched this session).
- **Coherent Corp.** — FY2025 record revenue $5.81 billion; Lasers segment revenue +3% (display
  capital-equipment shipments); at its May 2025 Investor Day, detailed a roadmap for CPO/pluggable
  optical transceivers targeting a $4 billion datacenter-interconnect market opportunity (L12-035,
  036).
- **Han's Laser (大族激光, China)** — 2025 annual report: total revenue RMB 18.76 billion (+27.00%
  YoY, record high), but high-power laser equipment segment revenue *fell* 6.60% YoY to RMB 3.16
  billion despite unit-volume growth of 30.47%; the true 2025 growth driver was IT/PCB equipment
  (RMB 8.25 billion, +50%, on AI-server/high-speed-switch demand for advanced PCBs) (L12-037,
  directly confirmed, Chinese-language).
- **Wuhan Raycus Fiber Laser Technologies (锐科激光, China)** — 2025 annual report: total revenue
  RMB 3.47 billion (+8.43%), net profit RMB 162 million (+20.52%); launched a 220 kW fiber laser
  described as a global first; handheld-welding export unit sales +66.22% (L12-038, search-
  confirmed via secondary media reporting of the official SZSE-hosted filing).
- **TRUMPF (Germany)** — FY2024/25 total sales EUR 4,329 million; Laser Technology division
  revenue declined to EUR 1.2 billion (from an adjusted EUR 1.4 billion); holds roughly a 6% share
  of the global laser-processing market bundling lasers, machine tools, and software (L12-039).
- **A*STAR / GlobalFoundries (Singapore)** — signed a Master Research Collaboration Agreement in
  November 2025 to build a GF silicon-photonics R&D Center of Excellence in Singapore targeting
  400 Gbps data-transfer materials, alongside a late-2025 upgrade of A*STAR IME's 12-inch
  silicon-photonics pilot line for 3D-integration prototyping (L12-044, search-confirmed; official
  A*STAR press-release URL returned HTTP 404 this session).

## 4. Incumbent map (companies, products, price/share signals)

| Company | Product / Role | Signal |
|---|---|---|
| IPG Photonics (US) | YLS high-power CW fiber lasers (500 W-100+ kW) | FY2025 sales $1.00B; China 29% of sales; explicitly names Raycus as a price/power-competing rival (L12-034, 051) |
| nLIGHT (US) | High-power semiconductor/fiber lasers; directed-energy beam-combination systems | FY2025 A&D revenue $175.3M (largest end market); $627M JLWS contract ceiling (L12-032, 033) |
| Lockheed Martin Aculight (US) | Containerized 500 kW directed-energy laser weapon system | JLWS award, part of $847M program ceiling (L12-031) |
| Coherent Corp. (US) | Lasers segment; CPO/pluggable optical transceivers | FY2025 revenue $5.81B; Lasers segment +3%; $4B DCI transceiver market targeted (L12-035, 036) |
| TRUMPF (Germany) | Laser Technology division; laser processing machine tools | FY2024/25 sales EUR 4.33B; Laser Technology division EUR 1.2B; ~6% global laser-processing market share (L12-039) |
| ASML / Cymer (Netherlands/US) | EUV lithography light sources (CO2-laser-driven tin-droplet LPP) | 1,000 W milestone April 2025 (up from 250 W in 2018); >EUR 6B cumulative EUV R&D (L12-034) |
| Gigaphoton (Japan, Komatsu Group) | DUV (ArF immersion) and EUV excimer/drive-laser light sources | ~2,000 excimer lasers shipped cumulative; active SPIE 2025 R&D presentations (L12-053) |
| Han's Laser (China) | General industrial + high-power laser processing equipment | 2025 revenue RMB 18.76B (+27%); high-power segment revenue -6.6% despite +30.5% unit volume (L12-037) |
| Wuhan Raycus (China) | Continuous/pulsed/ultrafast fiber lasers | 2025 revenue RMB 3.47B (+8.4%); #1 domestic China market share by 2022 (26.8%), overtaking IPG domestically (L12-038, 054) |
| Maxphotonics / Chuangxin Laser (China) | Fiber lasers and core optical components | Named as one of China's top-3 fiber laser makers (CR3 >70% with Raycus/IPG) (L12-054) |
| Thorlabs (US) | Commodity adaptive-optics components (deformable mirrors, wavefront sensors, AO kits) | Broad catalog product line; no price disclosed in this session (L12-052) |
| DARPA (US, funder not incumbent) | AMPED, MELT, POWER programs | $39M+$14M AMPED; MELT laser-tile program; POWER 800W/8.6km record (L12-040, 041, 047) |

**Pricing signals found:** IEC 60825-1 Ed.3.0 is priced at $665.00 via the Laser Institute of
America store (L12-048) — the only directly-priced item confirmed this session. No fiber laser,
diode laser, EUV light source, or adaptive-optics vendor publicly disclosed a unit price this
session; pricing across essentially the entire lane is opaque from open sources, consistent with
the same pattern observed in the L06 (semiconductor RF-power subsystem) lane.

## 5. 2026-2031 triggers

- **US:** JLWS moves from prototype to fielded, containerized 150-500 kW directed-energy systems
  over a multi-year program ceiling of $847 million (L12-031); DARPA's AMPED (42-month, ~$53M) and
  MELT programs continue pushing chip-scale/modular HEL laser-tile architectures through
  2027-2029 (L12-040, 041); NNSA's EYC project is only at Critical Decision-1 (project-definition
  complete) as of April 2026, with the bulk of the NIF laser-energy-upgrade procurement and
  execution still ahead through the late 2020s (L12-042).
- **China:** The fiber-laser price war shows no sign of resolving through 2026-2028 — Han's Laser's
  high-power segment revenue is *shrinking* even as unit volumes grow (L12-037), and the domestic
  top-3 (Raycus/IPG/Maxphotonics, CR3 >70%) dynamic reported for 2022 may have shifted further by
  2025-2026 without new data confirming it (L12-054, flagged as stale). Raycus's 220 kW laser launch
  and 66% handheld-welding export growth (L12-038) suggest continued capacity/technology
  escalation despite margin pressure.
- **Japan:** Gigaphoton's continued DUV/EUV R&D investment (SPIE 2025 presentations on
  next-generation ArF immersion and EUV sources, L12-053) positions it as a 2026-2031 candidate
  to capture share if ASML/Cymer's architecture-change risk (2-micron drive laser, L12-003)
  materializes or if EUV/DUV supply diversification becomes a policy priority.
- **Singapore:** The A*STAR-GlobalFoundries silicon-photonics collaboration (Nov 2025) and IME's
  12-inch silicon-photonics pilot-line upgrade are ongoing through at least 2026-2027, targeting
  400 Gbps materials and 3D-integration prototyping for global chipmakers — a live but
  investment-amount-undisclosed trigger (L12-044).
- **Standards:** IEC 60825 and ISO 11553 series editions (2014/2020/2007 base editions) are aging
  relative to the newest handheld/high-power laser product classes; a standards-revision cycle is
  plausible in 2026-2031 but not directly evidenced this session (L12-048, 049, 050).

## 6. US vs. Asia differences

- **US** evidence in this lane is dominated by (a) a fast-moving, newly funded directed-energy
  weapons acquisition push (JLWS, DARPA AMPED/MELT/POWER, all with dated 2025-2026 announcements)
  explicitly designed to close the "valley of death" GAO flagged in 2023, and (b) mature
  public-company disclosure (IPG, nLIGHT, Coherent 10-Ks) showing real segment revenue and explicit
  named-competitor risk factors. US directed-energy demand now has concrete, quantified dollar
  figures in a way it did not as recently as three years ago.
- **China** evidence is dominated by an intensifying price war inside an already-mature domestic
  industry: Han's Laser and Raycus both grew *total* revenue substantially in 2025, but Han's
  Laser's specifically high-power segment revenue *fell*, and IPG's own 10-K explicitly cites
  Chinese competitors' rising power/falling price behavior as a named risk factor. This is a
  structurally different picture from L06's China narrative (where domestic entrants are trying to
  *displace* a foreign incumbent duopoly) — in fiber lasers, Chinese firms (Raycus) already lead
  domestic market share and are exporting aggressively (handheld welding +66% YoY), so the frontier
  question is margin sustainability, not market-entry.
- **Japan** evidence (Gigaphoton) is narrower than China's or the US's this session — one
  confirmed vendor/technology-roadmap source with no revenue, market-share, or customer data
  found; Japan's DUV/EUV-adjacent role is real (Komatsu-group ownership, ~2,000 excimer lasers
  shipped cumulative, active SPIE R&D presence) but under-quantified in this pass and should be a
  follow-up scouting priority.
- **Korea** evidence is thin and academic-only this session: one confirmed Korean-language
  peer-reviewed optical-metrology paper (L12-030) was found; no Korean laser-manufacturing company
  (comparable to a Han's Laser or Raycus) was identified or fetched — a clear coverage gap for a
  country with a very large semiconductor/display manufacturing base that must consume industrial
  and processing lasers at scale.
- **Taiwan** evidence in this lane is weak and indirect: ITRI's ultrafast-laser research center
  (with Lithuania) and its silicon-photonics optical-engine work with ASE were found via search but
  not independently logged as fetched primary records this session — Taiwan's role as an EUV/DUV
  supply-chain *consumer* (via TSMC) rather than a laser-technology *producer* may partly explain
  this, but it remains a follow-up priority.
- **Singapore** evidence (A*STAR-GlobalFoundries) is real and dated but investment-amount-blind,
  similar to the pattern seen in the L06 semiconductor-subsystem lane — Singapore's angle here is
  photonics-manufacturing-ecosystem capability-building (silicon photonics, not high-power lasers
  specifically) rather than either weapons-program-scale spending (US) or price-war dynamics
  (China).
## 7. Unresolved contradictions

1. **Han's Laser's overall 2025 revenue grew 27% while its high-power laser-equipment segment
   specifically declined 6.6% even as unit volumes for high-power cutting machines rose 30.47%**
   (L12-037) — this is not a contradiction between sources but an internally reported divergence
   worth flagging: it directly evidences average-selling-price compression outpacing volume growth
   in China's high-power segment, a load-bearing fact for any idea premised on Chinese fiber-laser
   demand growth. A verifier should confirm this reading against the full annual report (not yet
   directly fetched this session).
2. **China fiber-laser market-share/localization figures (L12-054) are dated to 2021-2022 data
   presented in a September-2025-published article** — treat any claim of "Raycus holds 26.8%
   domestic share" or "76.19% localization" as a 2021/2022 snapshot, not necessarily current for
   2025-2026, absent a more recent breakdown. This mirrors the exact kind of stale-data-presented-
   as-current risk flagged in the L06 lane brief for China semiconductor-equipment localization
   percentages.
3. **The Huajing/Sina market-report's own stated 9.6% CAGR (2018-2022) does not match the compound
   growth rate implied by its own stated endpoints** (RMB 7.74B to RMB 12.26B implies roughly a 12%
   CAGR, not 9.6%) (L12-054) — flagged as an internal inconsistency in the source itself, not
   independently reconciled this session; do not silently average or correct it in downstream
   market-sizing arithmetic without locating the report's original methodology.
4. **DARPA's MELT program's own official page (fetched directly, L12-041) does not disclose a
   contractor name or dollar figure**, while a trade-press search snippet (not independently
   fetched this session) reports an $8 million Northrop Grumman order for the same program — the
   $8M/Northrop Grumman claim should be treated as unconfirmed pending direct verifier fetch,
   separate from the confirmed program-description facts.
5. **nLIGHT's individual JLWS award figure ($44M initial / $627M ceiling, L12-032) versus the
   combined DoD-wide JLWS figure ($86M initial / $847M ceiling across both nLIGHT and Lockheed
   Martin Aculight, L12-031)** are internally consistent (nLIGHT's $44M + an implied ~$42M for
   Lockheed Martin Aculight ≈ $86M combined; nLIGHT's $627M + an implied ~$220M for Lockheed Martin
   Aculight ≈ $847M combined) but the Lockheed-specific breakdown was not independently confirmed
   this session — a verifier should locate Lockheed Martin's own announcement to confirm its
   individual award figure directly.
6. **Two different auto-summarization unit-conversion errors were caught and corrected during this
   session** (Han's Laser's "187.59亿元" mis-rendered as "RMB 187.59 billion" instead of the correct
   RMB 18.759 billion; nLIGHT's Laser Products segment mis-rendered as "$179.236 billion" instead of
   the correct $179.236 million, an amount that must be smaller than nLIGHT's ~$261M total FY2025
   revenue) — both are corrected in the ledger (L12-033, 037), but this pattern of unit/scale
   errors in tool-generated financial summaries should make any future scout or verifier
   independently sanity-check every RMB/USD figure derived from an automated summary against
   internal consistency (e.g., segment revenue must not exceed total revenue).

## 8. Opportunity-shaped pain statements (NOT startup pitches)

1. **Pain:** Chinese fiber-laser makers are growing overall revenue strongly, but their
   specifically high-power segments are seeing average selling prices fall faster than unit volumes
   rise, and the market-share/localization data available to characterize this dynamic is 2-3 years
   stale relative to any 2026 decision. **Who pays:** Han's Laser, Raycus, and Maxphotonics
   (compressed margins), and indirectly IPG Photonics (named-risk-factor competitive pressure).
   **Evidence:** L12-034, 037, 038, 054.
2. **Pain:** Transverse mode instability remains an unresolved physical ceiling on single-fiber
   laser power scaling, forcing continued reliance on coherent beam combining, which itself
   introduces unsolved multi-channel phase-locking and dispersion-management engineering burdens.
   **Who pays:** fiber-laser OEMs (IPG, Raycus, nLIGHT, TRUMPF) racing to scale power without
   sacrificing beam quality, and their industrial-processing customers. **Evidence:** L12-001,
   002, 016, 017, 018.
3. **Pain:** EUV light sources cannot be treated as a stable target architecture — ASML/Cymer's
   current CO2-laser-driven tin-plasma source required a full repeat-rate-doubling engineering
   effort to reach 1,000 W in 2025, while peer-reviewed work is already modeling a completely
   different 2-micron-drive-laser architecture as a longer-term alternative. **Who pays:** ASML,
   its EUV-source supply chain, and leading-edge fabs dependent on continued EUV power scaling for
   throughput. **Evidence:** L12-003, 006, 007, 008, 034.
4. **Pain:** Co-packaged optics for AI-datacenter switches concentrates optical-transceiver power
   density directly onto the switch-ASIC package, and no dominant thermal-management architecture
   has emerged despite at least four independent 2024-2026 peer-reviewed proposals. **Who pays:**
   optical-switch/transceiver vendors (Coherent, Broadcom-class customers) and hyperscale
   datacenter operators bearing cooling-infrastructure cost and reliability risk. **Evidence:**
   L12-021, 022, 023, 024, 036.
5. **Pain:** The U.S. directed-energy-weapons enterprise has a documented, still-open
   "prototype-to-acquisition" transition gap (per GAO, as of August 2025), even as DoD is now
   trying to force the transition with a dedicated, large, newly awarded program (JLWS) — meaning
   execution risk on turning $847 million of committed ceiling into fielded, reliable, maintainable
   containerized laser weapon systems is real and acknowledged by DoD's own oversight body.
   **Who pays:** U.S. Department of War (program risk), nLIGHT and Lockheed Martin Aculight
   (delivery risk). **Evidence:** L12-031, 032, 045.
6. **Pain:** Laser diode driver electronics (pulsed-current precision, GaN-HEMT high-peak-power
   topologies, sub-nanosecond timing resolution) is still an active power-electronics research
   frontier rather than a mature, interchangeable commodity component, meaning every laser-system
   integrator (industrial or defense) inherits driver-electronics R&D risk rather than being able
   to treat pump/seed diode drive as a solved subsystem. **Who pays:** laser-system OEMs across
   both industrial (IPG, Raycus, TRUMPF) and defense (nLIGHT, Lockheed Martin Aculight) segments.
   **Evidence:** L12-025, 026, 027.
7. **Pain:** Handheld laser-welding/cleaning export volumes are growing extremely fast (Raycus
   +66.22% in 2025) even though the governing hand-held-laser-processing-machine safety standard
   (ISO 11553-2) still carries a 2007 date, with no primary technical study found this session
   directly testing whether the 2007-era safety-requirement framework remains adequate for
   today's higher-power, higher-volume handheld product class. **Who pays:** handheld-laser-tool
   manufacturers and their end-users/regulators bearing undocumented residual safety risk.
   **Evidence:** L12-038, 050.
8. **Pain:** Adaptive-optics beam control for directed energy spans from mature astronomy-derived
   real-time wavefront correction (deployed on research lasers) to commodity off-the-shelf
   components (Thorlabs kits) with apparently little standardized middle tier purpose-built for
   fielded, ruggedized, high-power industrial/defense beam-control systems — the custom-vs-
   commodity gap itself may be a underserved segment, though no vendor bridging it was identified
   this session. **Who pays:** directed-energy-system integrators and high-power industrial-laser
   beam-delivery OEMs. **Evidence:** L12-009, 010, 011, 052.
9. **Pain:** DARPA is running at least two parallel, apparently overlapping chip-scale/modular
   high-energy-laser architecture programs (AMPED and MELT) without a clearly disclosed
   division of technical scope in the open program descriptions found this session, and MELT's own
   program page discloses no contractor or dollar figure despite trade-press reporting an $8
   million Northrop Grumman order — creating real ambiguity about where in the HEL laser-tile
   technology stack near-term government funding is actually concentrated. **Who pays:** DARPA
   (program-management/deconfliction risk), and potential new entrants trying to identify the
   actual open technical gap. **Evidence:** L12-040, 041.
10. **Pain:** Japan's and Korea's roles in this lane are the weakest-evidenced of the major Asian
    markets this session — Gigaphoton's DUV/EUV technology roadmap has no attached revenue or
    market-share data, and Korea's evidence is limited to a single peer-reviewed optical-metrology
    paper with no identified Korean high-power-laser manufacturer — despite both countries having
    very large semiconductor/display/electronics manufacturing bases that must be significant
    consumers of industrial and processing lasers. **Who pays:** unclear from this session's
    evidence; this is a coverage gap, not a confirmed absence of activity. **Evidence:** L12-030,
    053 (present but thin); absence otherwise noted in Section 6.
11. **Pain:** Essentially no vendor in this lane (fiber lasers, diode lasers, EUV sources,
    adaptive-optics components) discloses unit pricing in open sources — the only directly-priced
    item found this session was a $665 safety-standard document (IEC 60825-1) — meaning any
    idea premised on price-elasticity or cost-down competitive dynamics in this lane requires
    direct RFQ/distributor engagement rather than open-source price discovery. **Who pays:** N/A
    (a research/methodology constraint, not a customer pain) — but it is a real due-diligence
    burden for any founder entering this lane. **Evidence:** L12-048, 051, 052, 053.

## Methodology notes and gaps for the verifier

- 54 candidate records collected (within the 45-55 target range). 30 are academic peer-reviewed
  candidates (22 T1 primary research + 8 T2 review articles), exceeding the >=27 floor. Overall
  T1 ratio across the full 54-record set is 38/54 = 70.4%, at the mission's >=70% floor but below
  the >=78% aspirational target — consistent with the same shortfall pattern documented in the L06
  lane brief, for the same underlying reason: many demand/company-filing records rely on
  successfully-fetched secondary reporting (laserfair.com, stocktitan.net) of official filings that
  were not independently re-fetched at their canonical SEC.gov/SZSE URLs this session. A follow-up
  verifier wave could likely raise the ratio toward 78-80% simply by successfully fetching those
  canonical filing URLs directly (several returned 403/404/timeout errors this session, a pattern
  seen across multiple prior lanes in this project, not lane-specific).
- Demand-primary count: 15 records carry a non-"none" `demand_evidence_type` (L12-031 through
  L12-044, government/procurement/company-filing types), exceeding the >=10 floor.
- Government/national-lab/standards-body count: 10 records (6 `government`, 3 `standard`, 1
  `national_lab`), exceeding the >=4 floor.
- Market/industry count: 5 records (3 `vendor_datasheet`, 2 `market_industry`), meeting the >=4
  floor exactly; none carry a disclosed unit price for a laser/optics product itself (only the
  IEC 60825-1 standard document, L12-048, has a confirmed price, $665).
- Asian-market coverage: 11 records carry an Asia geography tag (CN x6, JP x2, KR x1, IN x1, SG
  x1, plus one multi-country review), exceeding the >=8 floor; 5 are local-language primary
  sources (CN/zh x3: L12-037, 038, 054; JP/ja x1: L12-053; KR/ko x1: L12-030), exceeding the >=4
  floor.
- **Two unit-conversion errors caught and corrected this session** (see Contradiction 6 above) —
  flagged prominently because they illustrate a systematic risk (auto-summarization tools
  mis-scaling RMB "亿" and USD "million/billion" units) that a verifier should watch for across
  this entire project, not just this lane.
- **Weakest coverage / follow-up priorities for a future scout wave:** (1) Korea — no Korean
  high-power-laser or photonics-manufacturing company (analogous to Han's Laser/Raycus for China
  or Gigaphoton for Japan) was identified or fetched this session, despite Korea's large
  semiconductor/display manufacturing base; (2) Taiwan — ITRI's ultrafast-laser and silicon-
  photonics activity was found via search but no record was logged with a directly fetched primary
  Taiwan-domiciled source; (3) direct fetch of the canonical SEC.gov 10-K filings for nLIGHT, IPG,
  and Coherent (all three returned inaccessible or were not attempted directly this session,
  relying instead on secondary aggregators); (4) direct fetch of the Raycus SZSE-hosted annual
  report PDF and the Han's Laser official annual-report PDF, rather than financial-media secondary
  reporting; (5) direct fetch of DARPA's own AMPED/MELT BAA text and the militaryaerospace.com
  Northrop Grumman/MELT article, to resolve Contradiction 4; (6) a primary Lockheed Martin
  announcement of its individual JLWS award figure, to resolve Contradiction 5; (7) confirmation of
  whether the Korean Journal of Optics and Photonics article (L12-030) is published in Korean or
  English, to firm up the local-language quota count.

## P2A origin-audit repair (2026-07-13)

- removed IDs: L12-043
- removed/trimmed claims: deleted the DRDO named-buyer bullet (Section 3, Mk-II(A)/"Surya"
  directed-energy trials) sourced solely to L12-043; deleted the India 2026-2031 trigger bullet
  (Section 5) sourced solely to L12-043; deleted the India paragraph in "US vs. Asia differences"
  (Section 6), which rested on the same India/DRDO evidence with no eligible ID; deleted pain
  statement 11 (Section 8, DRDO subsystem-supply-chain gap) sourced solely to L12-043 and
  renumbered the following item to 11. No other India-sourced claim remained in this lane after
  removal. Any future India-market laser/DEW evidence must come from an eligible non-India source
  per the binding geography-scope rule, which already excludes India from demand/market/geography
  scoring in this project.
