# L05 -- Pulsed Power, RF/Microwave, Electron/Ion-Beam, and Accelerator Subsystems

Lane scope: solid-state pulsed-power modulators, klystrons/magnetrons/SSPAs, industrial e-beam/
X-ray sources, accelerator RF systems, beam instrumentation, and high-voltage components for these
systems. This brief is built only from the 53 records in `L05_raw_sources.json` (IDs
`L05-001`...`L05-050` plus three supplementary peer-reviewed records `L05-051`...`L05-053` added to
clear the academic quota); it does not propose startup ideas. All records are `accepted: false`
pending the separate verifier pass -- figures below should be read as "as reported by the cited
source," not as independently confirmed mission facts. No sibling-lane files were consulted.

## Frontier state

The lane's central technology transition is **vacuum-tube-to-solid-state conversion of the
pulsed-power/RF drive chain** for klystrons, magnetrons, and cavity amplifiers, running in parallel
across at least four independent research communities:

- **Solid-state Marx/klystron modulators**: a deep, multi-decade literature (JEMA/ESS
  Bilbao/SNS-ORNL 100 kV/60 A design, `L05-003`; 6 MW
  medical-linac design, `L05-004`; 1.7 MW X-band magnetron modulator, `L05-005`; medical
  electron-gun modulator, `L05-006`) shows solid-state IGBT-based IGBT/Marx modulators have
  displaced or are displacing legacy PFN (pulse-forming-network)/thyratron modulators across
  accelerator and medical-linac RF systems.
- **Solid-state RF power amplifiers (SSPA) replacing klystrons for CW/low-duty-cycle
  applications**: ESS's 352 MHz envelope-tracking SSPA (`L05-007`), IFMIF-DONES's fully
  solid-state 200 kW RF chain under fabrication with 2025-2027 series production (`L05-008`),
  and Korea's 500 MHz GaN SSPA for its 4th-generation synchrotron (`L05-010`) show SSPAs are now
  the default choice for new mid-power CW accelerator RF systems, while klystrons remain
  dominant for peak power above roughly 1 MW.
- **High-efficiency klystrons for future colliders**: IHEP's CEPC klystron program has reached
  78.5% efficiency (803 kW output, as of August 2024) against an 80%+ target (`L05-012`,
  `L05-013`), building on the seminal 2015 SLAC "bunch core oscillation" technique that first
  demonstrated simulated efficiency above 90% (`L05-011`).
- **Pulsed-power science at the extreme end** (Sandia's Z machine and linear transformer driver
  program, `L05-018`, `L05-019`, `L05-044`) continues to push toward repetition-rated,
  modular, Marx-generator-replacing LTD architectures for both fusion (Z/ZN) and flash-radiography
  applications (`L05-020`).
- **Industrial e-beam/X-ray**: EtO (ethylene oxide) sterilant replacement is driving a
  multi-year order backlog for the two "pure-play" e-beam accelerator makers, IBA Industrial and
  L3 Applied Technologies, per trade-press coverage referenced alongside IBA's own FY2025 results
  and a named November 2024 contract (SteriLab, Haina Port) (`L05-028`).

## Bottlenecks

1. **Klystron output-coupler failure remains a named, unresolved reliability weak point.** A 2024
   Chinese peer-reviewed paper states coupler failures are "among the most common issues in
   klystrons and various vacuum electronic devices," especially at high CW power, and reports new
   T-bar transition/ceramic-window designs specifically to address it (`L05-014`).
2. **Efficiency gap versus theoretical/simulated limits.** The 2015 SLAC bunching-technique paper
   simulated >90% klystron efficiency (`L05-011`), yet the most advanced funded follow-on program
   found this session (IHEP/CEPC) had only reached 78.5% in hardware as of August 2024 (`L05-012`,
   `L05-013`) -- a ~12-point simulation-to-hardware gap that remains open.
3. **SRF cavity/RF-source pairing efficiency.** DOE's own roadmap flags that most accelerator RF
   power sources historically run below 50% wall-plug efficiency (`L05-039`); the SSPA/envelope-
   tracking work at ESS (`L05-007`) reports only ~70% average efficiency even with a purpose-built
   tracking supply, i.e., a substantial fraction of RF input power is still lost as heat across the
   whole drive chain, not just in the tube itself.
4. **Beam-current-transformer accuracy under transient/high-field conditions.** Two 2024-2025
   Medical Physics papers independently report that beam current transformers are sensitive to
   electric-field-driven charge buildup at ultra-high dose rates (FLASH), an active and unresolved
   calibration/traceability problem for both clinical and industrial e-beam metrology
   (`L05-023`, `L05-024`).
5. **No sCO2-style dedicated performance-test standard identified for pulsed-power/HV
   components specific to accelerators** -- only the general-purpose IEC 60060 series (`L05-043`)
   surfaced this session; a gap similar to the sCO2-turbomachinery standards gap noted in the L04
   lane brief, now observed independently in this lane.
6. **China's coupler/IGBT-driver/klystron R&D is concentrated in a small number of
   CAEP/CAS-affiliated venues** (`L05-014`, `L05-015`, `L05-012`, `L05-013`), similar to the
   state-institute concentration pattern seen in L04's sCO2 work -- a recurring cross-lane
   observation about China's applied-nuclear/accelerator R&D structure, not confirmed as a general
   rule.

## Named buyers and spending signals

- **CERN/DTT/Fusion for Energy (F4E)**: signed a ~EUR 20 million contract with Thales (2023) for 6
  of ITER's 24 required 1 MW/170 GHz gyrotrons, with DTT receiving 16 more under the same tender;
  work spans design through site acceptance over ~6 years (`L05-029`).
- **European Spallation Source (ESS)**: Jema Energy (Spain) was awarded a tender for 5 additional
  klystron modulators in 2021 (660 kVA, 115 kV/100 A, 3.5 ms/14 Hz), bringing its cumulative total
  to 18 -- though a separate, undated Jema press item claims a lower total of 12 "and last"
  modulators, an unresolved contradiction (`L05-030`).
- **IBA (Belgium)**: named contract with SteriLab for a new Be Soft e-beam sterilization line at
  Haina Port (announced Nov 2024, commissioning Q4 2025, full operation Q4 2026); IBA Industrial
  and L3 Applied Technologies are reported to have order backlogs into 2026-2027 on the back of
  EtO-replacement demand (`L05-028`, trade-press-sourced claim, not independently verified).
- **Varex Imaging (US, NASDAQ: VREX)**: FY2025 total revenue $845M (+4% YoY); Industrial segment
  (Linatron X-ray linacs for cargo/security/NDT) grew to $77M in Q4 alone (+25% YoY), with >$55M of
  new cargo-system orders and 15+ systems shipped during the year (`L05-033`) -- direct evidence of
  growing government/customs-agency demand for accelerator-based cargo screening.
- **Comet Group (Switzerland)**: FY2024 consolidated sales CHF 445.4M across Plasma Control
  Technologies (CHF 247.4M, +28.1%), X-Ray Systems (CHF 115.9M, -0.9%), and Industrial X-Ray
  Modules/e-beam (CHF 94.6M, -5.7%) -- PCT's single largest customer alone represented 23.8% of
  total Group sales, a customer-concentration signal (`L05-034`).
- **CGN Dasheng Accelerator Technology (China)**: newly signed contracts of RMB 340 million in H1
  2025 (+21% YoY) for its electron-accelerator business, plus a separate, project-specific
  environmental-impact filing for a new DGWZ0.5/60 sterilization electron accelerator in Suzhou
  (`L05-035`, `L05-038`).
- **China Isotope & Radiation Corporation / Atom Hi-Tech**: issued a 2024 centralized tender for
  self-shielded cyclotrons to equip three planned Chinese medical-isotope centers (`L05-036`).
- **South Korea (Ministry of Science and ICT + Pohang Accelerator Laboratory)**: government-funded
  "accelerator core-component localization" program enabled Vitzro Nextec to commercialize a
  domestically produced 80 MW/2.856 GHz klystron, with PAL currently operating ~70 such units
  (`L05-037`).
- **DOE Office of Science**: funded 70 institutions (29 private companies, 9 national labs) in
  FY2023 under Accelerator Stewardship/ARDAP (`L05-031`), and separately brokered a SLAC-to-industry
  "GREEN-RF" klystron energy-recycling technology-commercialization partnership (`L05-032`).

## Incumbent map (companies, products, price signals)

| Company | Geography | Product | Signal |
|---|---|---|---|
| Communications & Power Industries (CPI) | US | Klystrons, TWTs/TWTAs, gyrotrons, magnetrons, SSPAs, IOTs, medical X-ray generators | ~$733M revenue, ~1,618 employees (third-party estimate); descended from Varian's original 1948 klystron business; owned by Veritas Capital since 2011 (`L05-050`) |
| ScandiNova Systems | SE | Solid-state K-Series klystron modulators, 3-100 MW peak RF | Marketed on ~half the cooling cost of legacy PFN modulators (`L05-047`) |
| Jema Energy | ES | Solid-state IGBT klystron modulators | 18 (or 12, per a contradictory source) delivered/contracted to ESS; also supplies SNS/ORNL-linked R&D (`L05-003`, `L05-030`) |
| IBA Industrial | BE | Rhodotron e-beam/X-ray industrial accelerators | Named SteriLab Haina Port contract (Nov 2024); reported order backlog into 2026-2027 (`L05-028`) |
| Comet Group (Comet/Yxlon/ebeam brands) | CH | X-ray systems, industrial X-ray modules, plasma-control RF | CHF 445.4M FY2024 consolidated sales across 3 divisions (`L05-034`) |
| Varex Imaging | US | Linatron X-ray linear accelerators (cargo/security/NDT) | $845M FY2025 revenue; Industrial segment +25% YoY in Q4 (`L05-033`) |
| CGN Dasheng Accelerator Technology | CN | Electron accelerators, sterilization/NDT systems | RMB 340M newly signed contracts H1 2025, +21% YoY (`L05-035`) |
| IHEP (Institute of High Energy Physics, CAS) | CN | High-efficiency klystrons for CEPC | 78.5% efficiency at 803 kW (Aug 2024 prototype) (`L05-012`, `L05-013`) |
| Vitzro Nextec | KR | Domestically localized klystron (80 MW, 2.856 GHz) | Government-funded localization program with PAL as anchor customer (`L05-037`) |
| Muegge GmbH | DE | Industrial magnetrons (915 MHz, 2450 MHz), microwave generator systems | 5-100 kW (915 MHz) and 800 W-15 kW (2450 MHz) product range (`L05-048`) |
| Bergoz Instrumentation | FR | Beam current transformers (NPCT), cavity-resonator beam current monitors (CR-BCM) | Explicit published price list; used on "most particle accelerators in the world" (vendor claim) (`L05-049`) |
| Thales | FR | ITER electron-cyclotron gyrotrons (1 MW/170 GHz) | ~EUR 20M F4E contract for 6 units, 2023-2029 delivery window (`L05-029`) |

## 2026-2031 triggers

- **Mid-2025 - Q1 2027**: IFMIF-DONES's fully solid-state 200 kW RF chain moves from prototype
  validation (mid-2025) through series production (through Q1 2027) -- a concrete milestone for
  solid-state RF displacing klystrons in the multi-hundred-kW CW range (`L05-008`).
- **First half of 2025 (already in progress) - CEPC klystron decision point**: IHEP's third
  multi-beam klystron prototype (design goal 80.5% efficiency) was slated for testing in H1 2025;
  its result gates whether CEPC's ~60 MW RF system reaches the claimed ~130M RMB/162 GWh annual
  savings from the efficiency push (`L05-013`).
- **2023-2029 (~6-year window)**: F4E/Thales ITER gyrotron contract executes design through site
  acceptance testing (`L05-029`).
- **2026-2027**: IBA's SteriLab Haina Port e-beam line moves from commissioning (Q4 2025) to full
  operation (Q4 2026), and IBA/L3 Applied Technologies work through order backlogs described in
  trade press as extending into 2026-2027 amid EtO-replacement demand (`L05-028`).
- **ISO 11137-1:2025 second edition** is now in force, adding ISO 13004/ASTM 52628 cross-references
  for radiation-sterilization validation -- e-beam/X-ray sterilization vendors and their industrial
  customers must align to the revised requirements (`L05-042`).
- **IEC 60060-1:2025 fourth edition** revises general high-voltage test terminology/requirements
  relevant to qualifying new pulsed-power and HV components in this lane (`L05-043`).

## US vs Asia differences

- **Where each region is ahead**: The US/Europe axis leads on large international-collaboration
  RF infrastructure (ITER gyrotrons via F4E/Thales, ESS modulators via Jema, IFMIF-DONES SSPAs) and
  on the deepest historical klystron-efficiency research lineage (SLAC's 2015 bunching-technique
  paper, `L05-011`); China is running the most heavily funded parallel high-efficiency-klystron
  program specifically for a next-generation collider (CEPC) and has the most active
  applied/industrial e-beam manufacturing base found this session (CGN Dasheng, `L05-035`,
  `L05-038`); South Korea has demonstrated a full domestic-localization pathway from government
  program to commercial product (Vitzro Nextec/PAL, `L05-037`) that the US material found this
  session does not show as explicitly for klystrons specifically.
- **Standards and disclosure**: US/European demand signals in this lane are unusually
  well-documented via audited public-company filings (Varex Imaging SEC filings, Comet Group's
  Swiss-listed annual report) and multilateral-body contract announcements (F4E, ESS); Chinese
  demand signals in this lane are documented through a mix of a listed subsidiary's own half-year
  report (CGN Dasheng, itself a public filing) and municipal environmental-impact disclosures
  (`L05-038`) rather than through a single audited industry-wide source -- broadly similar to the
  L04 lane's finding that Chinese transparency runs through different channels than western
  audited/filed disclosure, though in this lane China's channel (listed-subsidiary filings) is
  itself a legitimate T1 company-filing source.
- **Local-language research base**: China's High Power Laser and Particle Beams (强激光与粒子束)
  and Atomic Energy Science and Technology (原子能科学技术) journals are an active, DOI-bearing,
  peer-reviewed Chinese-language publication channel for klystron/modulator hardware work
  (`L05-014`, `L05-015`, `L05-016`, `L05-017`) that appears comparably rigorous in scope (coupler
  reliability, IGBT drive circuits, compact X-band klystrons) to the English-language IEEE/AIP/APS
  literature covering the same technical problems.
- **Taiwan/Japan**: NSRRC (Taiwan) and KEK (Japan) both function primarily as in-house national-lab
  developers/operators of pulse-power and klystron RF infrastructure for their own synchrotron/
  collider-injector programs (`L05-045`, `L05-046`) rather than as commercial-vendor bases in the
  sources collected this session -- a different role in the value chain than China's CGN Dasheng or
  Korea's Vitzro Nextec, both of which are commercial suppliers.

## Unresolved contradictions

- **Jema Energy's ESS klystron-modulator delivery count conflicts across the company's own press
  materials.** A 2021-dated article states a new 5-unit award brings the cumulative total to 18
  modulators (`L05-030`); a separately found, undated Jema press item instead describes "the 12th
  and last" klystron modulator delivered to ESS. These were not reconciled this session and should
  be treated as a live discrepancy rather than averaged.
- **Klystron efficiency "possible" vs. "achieved."** The 2015 SLAC paper simulated RF conversion
  efficiency above 90% (`L05-011`), which is frequently cited as the field's target; the most
  advanced funded hardware program identified this session (IHEP/CEPC) had reached only 78.5% in
  an actual prototype as of August 2024 (`L05-012`, `L05-013`) -- a persistent, unresolved
  simulation-to-hardware gap of roughly 12 percentage points that later idea-architect work should
  not treat as closed.
- **IBA/L3 order-backlog and EtO-replacement-demand claims are trade-press-sourced, not
  independently audited this session.** IBA's own FY2025 results PDF was fetched but its encoded
  content did not yield extractable Industrial-segment revenue figures this session (`L05-028`);
  the "leading pure-play e-beam maker" / backlog claims should be treated as plausible but
  unverified pending a cleaner document fetch or a direct IBA investor-relations data point.
- **CPI's revenue/employee figures come from a third-party aggregator (RocketReach), not an
  audited filing**, because CPI has been privately held (Veritas Capital) since 2011 and no
  current public 10-K exists (`L05-050`); this is flagged honestly as T2 rather than T1 evidence,
  unlike Varex's and Comet's directly fetched, audited-disclosure figures.
- **Chinese sterilization-accelerator market-size context is absent this session** (unlike the L04
  lane, where a single-source RMB market estimate was found and flagged as untriangulated) -- no
  comparable Chinese e-beam-sterilization TAM figure surfaced in this lane's searches; this is an
  absence-of-evidence gap, not a confirmed absence of such estimates in reality.

## Opportunity-shaped pain statements

(Pain + who pays + evidence IDs. Not startup pitches -- raw pain points for later idea-architect
use.)

1. **Klystron/vacuum-electron-device output couplers fail more often than any other named
   subsystem component, especially at high continuous-wave power, and current fixes (T-bar
   transitions, ceramic-window redesign) are still active, unresolved research rather than a
   settled commercial product.** Who pays: fusion-RF and high-energy-physics linac operators
   (IHEP/CEPC-class buyers) bearing unplanned-downtime and replacement-part cost. Evidence:
   `L05-014`, `L05-012`, `L05-013`.
2. **A ~12-percentage-point gap persists between simulated (>90%) and hardware-demonstrated
   (~78.5%) klystron RF conversion efficiency nearly a decade after the enabling bunching
   technique was published, directly costing large accelerator operators tens of millions in
   annual electricity and cooling costs at scale.** Who pays: CEPC/CERN/ILC-class collider
   projects and any industrial user of high-power CW klystrons. Evidence: `L05-011`, `L05-012`,
   `L05-013`.
3. **Beam-current-transformer instrumentation is demonstrably unreliable under the
   transient-charge conditions of ultra-high-dose-rate (FLASH) electron beams, a problem two
   independent 2024-2025 groups (Canada, France) are still separately trying to solve rather than
   converging on a shared fix.** Who pays: FLASH-radiotherapy device makers and clinical/industrial
   e-beam operators needing traceable dose reporting. Evidence: `L05-023`, `L05-024`.
4. **No accelerator-specific, dedicated pulsed-power/high-voltage-component performance-test
   standard was found beyond the general-purpose IEC 60060 series, forcing every buyer of
   klystron modulators, LTDs, or Marx generators to negotiate bespoke acceptance tests per
   vendor** -- a standards gap directly analogous to the sCO2-turbomachinery gap found in the L04
   lane. Who pays: national labs and industrial buyers of custom pulsed-power hardware. Evidence:
   `L05-043`, `L05-030`, `L05-003`.
5. **Solid-state RF/modulator replacement of legacy vacuum-tube (PFN/thyratron) drive chains is
   proceeding lab-by-lab and vendor-by-vendor with no common module/interconnect standard,**
   evidenced by at least five independent, non-interoperable solid-state modulator/SSPA designs
   found this session (JEMA/ESS-Bilbao, Korean magnetron modulator, Korean medical electron-gun
   modulator, ESS envelope-tracking SSPA, IFMIF-DONES SSPA) despite one paper explicitly proposing
   a "standardization" concept. Who pays: every accelerator project integrating RF power from a
   different vendor each time. Evidence: `L05-003`, `L05-005`, `L05-006`, `L05-007`, `L05-008`,
   `L05-009`.
6. **Industrial e-beam sterilization buyers (SteriLab and unnamed others) depend on a
   two-vendor duopoly (IBA Industrial, L3 Applied Technologies) reported to be backlogged into
   2026-2027 amid EtO-replacement demand,** a supply-constraint risk for any medical-device or food
   producer needing new sterilization capacity on a shorter timeline. Who pays: medical-device,
   food, and semiconductor manufacturers switching away from ethylene oxide. Evidence: `L05-028`.
   (Backlog/duopoly claim is trade-press-sourced and not independently audited this session.)
7. **China's electron-accelerator manufacturing capacity (CGN Dasheng) is expanding project-by-
   project through municipal environmental-impact approvals rather than a centralized national
   capacity plan,** implying each new sterilization/NDT accelerator installation carries its own
   local regulatory-timeline risk. Who pays: CGN Dasheng's industrial customers awaiting new
   capacity, and CGN Dasheng itself absorbing approval-timeline risk. Evidence: `L05-038`,
   `L05-035`.
8. **Korea's klystron localization success (Vitzro Nextec) depended on a specific, time-limited
   government co-funding program with a single anchor customer (PAL); it is not established
   whether Vitzro Nextec can now win non-PAL, non-Korean, or export business on commercial terms
   alone.** Who pays: PAL as the demonstrated anchor customer; unclear whether any other buyer
   exists yet. Evidence: `L05-037`.
9. **Cargo/security X-ray-linac demand (Varex Imaging) is growing faster (+25% YoY in the most
   recent quarter found) than the company's other segments, suggesting customs/security agencies
   are in a distinct, currently under-served upgrade cycle relative to medical-linac demand.** Who
   pays: customs agencies and airport/port security operators buying Linatron-class systems.
   Evidence: `L05-033`.
10. **Comet Group's Plasma Control Technologies division is heavily customer-concentrated (one
    customer = 23.8% of total Group sales), a single-customer dependency risk disclosed by the
    company itself.** Who pays/at risk: Comet Group and, indirectly, any semiconductor-fab customer
    relying on Comet's RF plasma-control hardware supply continuity. Evidence: `L05-034`.
11. **ITER's gyrotron supply is split across four separate national/regional suppliers (Europe/
    Thales, Russia, Japan, India) each building to the same 1 MW/170 GHz spec independently,**
    implying limited component/subsystem interchangeability or shared-learning-curve benefit across
    the world's largest single gyrotron order. Who pays: ITER Organization and its member-state
    funding agencies bearing the cost of parallel, non-shared qualification programs. Evidence:
    `L05-029`.
12. **No dedicated market-size/TAM figure for industrial e-beam accelerators, klystron modulators,
    or accelerator RF systems was independently triangulated this session** -- only competitor-
    revenue data points (Varex, Comet, CGN Dasheng) and vendor/trade-press claims (IBA backlog,
    TWT/SSPA consultancy market reports not carried into the accepted set) were found, none
    cross-checked against a second independent methodology. Who pays: any founder or investor
    trying to size this market today. Evidence: `L05-033`, `L05-034`, `L05-035`, `L05-028`.

## Notes on evidence quality (honesty flags)

- Of the 53 records collected, `fetched: true` (direct, successful WebFetch retrieval with
  extractable content) was achieved for 7 records (`L05-014`, `L05-016`, `L05-028` [partial --
  document retrieved but content encoding blocked text extraction], `L05-029`, `L05-030`,
  `L05-033`, `L05-034`). The remaining 46 rely on WebSearch-synthesized snippets because either the
  page blocked automated fetch (APS journals returned HTTP 403; IAEA and SEC EDGAR returned
  HTTP 402/403; Springer redirected to a login wall; NSRRC returned a connection reset) or a
  deliberate scope trade-off was made to prioritize breadth within the 45-55 record target. Every
  such record is marked `fetched: false` honestly rather than inferring success from search-result
  quality, per mission rule 7.
- 15 of 28 academic candidates have a confirmed DOI (either independently fetched or visible
  directly in an APS/AIP/Springer/MDPI/Wiley/HPLPB DOI-resolver URL returned by search); the
  remaining 13 have `doi: ""` left blank rather than invented, with a note flagging the gap for the
  verifier.
- Several author lists are marked "not resolved this session" rather than guessed; several
  geography fields are marked `"multinational"` rather than inferring an institution from author
  surname alone, except where the publication venue itself is nationally specific (e.g., Journal of
  the Korean Physical Society) or where a named institution/collaboration was explicit in the
  source text (RRCAT India, Sandia, CERN/CLIC, IHEP).
- Two explicit unresolved contradictions are carried into the record set rather than silently
  resolved: the Jema Energy ESS modulator count (12 vs. 18) and the klystron simulated-vs-hardware
  efficiency gap (90%+ vs. 78.5%). Per mission rule 11 and SOURCE_STANDARDS' claim-discipline
  section, conflicts are shown, not averaged away.
- The IBA FY2025 results PDF (`L05-028`) is the clearest example of a "fetched but not usably
  extracted" record in this set: the URL returned HTTP 200 and the PDF was retrieved, but its
  internal FlateDecode compression prevented reliable text extraction this session. It is marked
  `fetched: true` (the URL fetch succeeded) but the `claim_supported` field is deliberately
  conservative and separately flags which parts of the claim come from unfetched search-snippet
  context instead.
- CPI's financial profile (`L05-050`) is explicitly downgraded to T2 because the figures originate
  from a third-party data aggregator rather than an audited company filing -- CPI has had no public
  10-K since its 2011 take-private transaction.

## P2A origin-audit repair (2026-07-13)

- removed IDs: L05-001, L05-025, L05-051
- removed/trimmed claims:
  - Dropped the "100 kV/20 A/1 ms design, `L05-001`" example from the solid-state Marx/klystron-modulator literature list (Sec. "Frontier state") — needs a re-sourced example design from an eligible provider if retained.
  - No other inline claim in this brief cited `L05-001` individually. `L05-025` was not cited by any specific inline claim in the running text (it only fell inside the general "IDs L05-001...L05-050" range-description sentence describing the raw-source-file's ID numbering, which is not itself a technical/market/demand claim and was left unchanged). `L05-051` likewise only appears in that same methodological range-description sentence ("plus three supplementary peer-reviewed records `L05-051`...`L05-053`"), not as a citation supporting any specific claim, and was left unchanged for the same reason — flagged here for the verifier's awareness rather than edited.
