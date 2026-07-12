# L15 -- Harsh-environment/high-temperature electronics and autonomous industrial control

Lane scope: high-temperature semiconductors and packaging (SiC/GaN/SOI), downhole/geothermal/
aero-engine/space electronics, radiation- and vibration-tolerant sensing and control, and
autonomous control systems for remote/hazardous industrial operations. This brief cites records in
`10_SOURCE_ATLAS/L15_raw_sources.json` by ID (L15-001 ... L15-046). All records are
`accepted:false` pending the source-verifier pass, and academic `peer_review_status` is
`unverified` pending independent confirmation. No startup ideas are proposed here per the
lane-scout mandate.

## Frontier state

Three technology fronts and one control-systems front define this lane. First, **high-temperature
semiconductor electronics has no single converged technology winner above ~250C**: SOI CMOS is
mature to ~300C (L15-004, a 2024 University of Pisa IEEE Access paper; L15-005 Fraunhofer-adjacent
HOT-300 lineage) but is a small-signal, low-power technology; SiC is the leading candidate for
power devices and can theoretically reach ~600C junction temperature (L15-001) with laboratory SiC
JFET integrated circuits demonstrated by NASA Glenn operating over 1000C of total span (-190C to
+812C per program materials) and for over a year at 500C (L15-009, L15-030); GaN offers higher
switching speed but weaker long-term high-temperature stability data (per DARPA THERMAL program
framing, L15-026). DARPA's active THERMAL solicitation (closed June 2026, L15-026) targets 800C
mixed-signal ICs with a defined 10,000-sample/sec 8-bit ADC spec, showing the government still
treats this as an open, fundable research problem rather than solved engineering -- 19 years after
NIST/DARPA's WBST SiC power program (L15-037) and 20+ years after DOE's Honeywell-executed Deep
Trek SOI program (L15-031), both of which pursued similar 200-500C goals. Second, **radiation
tolerance and high-temperature tolerance are separate, sometimes conflicting properties that are
frequently discussed together but not co-solved**: neutron irradiation measurably degrades SiC
Schottky diodes and MOSFETs (reverse leakage current increases significantly, gate leakage
increases ~3.3x at 15V, L15-020, a 2023 Acta Physica Sinica/CAS paper) even though SiC is prized
for thermal tolerance, and GaN shows strong total-ionizing-dose resistance but is "prone to leakage
and single event burnout" at the drain-gate edge (L15-013, a 2024 Chinese aerospace-components
paper). Third, **packaging/die-attach and thermal management remain a persistent bottleneck
independent of device physics**: multiple 2022-2025 reviews (L15-005, L15-025, L15-015, L15-007)
all still identify die-attach materials, gate-drive design, and current-sensing at elevated
temperature as unresolved, and a parallel body of work (L15-023, L15-024, both ASME) pursues active
cooling as a workaround rather than solving native high-temperature electronics -- indicating the
field has not decided whether to solve the semiconductor problem or engineer around it with
thermal management. Fourth, on the **autonomous-control side**, radiation-hardened robotics for
nuclear environments shows a genuine US/UK-vs-Japan/China divergence in philosophy: a
Bristol/Manchester study (L15-002) argues standard commercial-grade components with planned
replacement schedules can beat specialized rad-hard hardware on cost for some decommissioning
tasks, while Japan (post-Fukushima Quince robot, L15-011) and China (Beihang nuclear-rescue robot,
L15-012) both independently ran Co-60 gamma-irradiation qualification testing on off-the-shelf
robot electronics before deployment -- a shared empirical-testing approach across geographies even
without a shared design philosophy. Separately, autonomous mining haulage is the most
commercially mature slice of this lane's "autonomous industrial control" scope, already
operating at scale (L15-018, L15-042) under a dedicated ISO safety standard (L15-032).

## Bottlenecks

- **No industry-standard high-temperature semiconductor platform has emerged above 250C.**
  SOI (300C, small-signal only), SiC (power devices, packaging-limited), and GaN (fast but
  thermally immature) remain simultaneously active, non-converged fronts (L15-001, L15-004,
  L15-026), with DARPA still funding basic 800C mixed-signal IC development in 2026 (L15-026)
  despite DOE/Honeywell (2003-2007, L15-031) and DARPA/NIST (2007, L15-037) having pursued
  materially similar goals two decades earlier.
- **Radiation hardness and thermal hardness do not transfer between each other.** SiC's
  high-temperature advantage does not confer radiation immunity -- neutron irradiation measurably
  increases leakage current in SiC Schottky diodes and MOSFETs (L15-020) -- and GaN's total-dose
  tolerance does not prevent single-event burnout at the drain-gate edge (L15-013, L15-014). Any
  space/nuclear/aerospace application must qualify for both properties independently.
- **Die-attach and packaging remain the limiting factor even when the semiconductor itself
  tolerates the temperature.** At least four independent 2024-2026 reviews (L15-005, L15-007,
  L15-015, L15-025) still list packaging/die-attach reliability as an open problem, and CISSOID's
  own product page (L15-043) marks its established -55C-to-225C CHT product family as obsolete
  (last-time-buy), suggesting even mature commercial high-temperature IC lines face supply
  discontinuity risk rather than a clear successor roadmap.
- **Active cooling and native high-temperature electronics are competing, unreconciled strategies**
  for the same downhole-electronics problem (L15-023, L15-024 pursue cooling; L15-001, L15-004,
  L15-009 pursue native high-temperature devices), with no session-found source explicitly
  comparing total cost of ownership between the two approaches.
- **Standards coverage is uneven and hard to verify online.** MIL-STD-883 (test methods, current
  Rev. L Ch.1, L15-035) and DO-160G (avionics environmental testing, L15-036) are long-established,
  but this session could not independently fetch full text of ISO 17757 (autonomous mining safety,
  L15-032), API 17F/SIIS (subsea control, L15-033), or IEC 60751 (platinum resistance thermometers,
  L15-034) due to paywall/403/binary-parsing failures -- each is flagged for the verifier to
  re-attempt with authenticated or purchased access.
- **Market-size estimates for adjacent categories disagree by roughly 40%.** Research and Markets
  (L15-045, $5.79bn 2025 / $6.07bn 2026) and Fortune Business Insights (L15-046, $4.10bn 2025 /
  $4.31bn 2026) both size the "downhole tools" market for the same forecast years with materially
  different results -- not reconciled here.
- **Vendor pricing is almost entirely undisclosed.** Neither CISSOID (L15-043) nor Honeywell HTMOS
  (L15-044, itself not independently fetched this session) publish list pricing for high-temperature
  ICs, consistent with the pricing-opacity pattern documented in other lanes (e.g., L09) for
  adjacent harsh-environment power-electronics hardware.

## Named buyers and spending signals

- **DARPA (THERMAL program, solicitation DPA26BZ02-NV008)** -- open SBIR solicitation (closed June
  24, 2026) for 800C-capable mixed-signal ICs, with a defined Phase II ADC spec (>10,000
  samples/sec, 8-bit, <1W at 800C) (L15-026).
- **DOE Geothermal Technologies Office / Utah FORGE** -- two dated, quantified solicitation cycles:
  Solicitation 2020-1 (up to $49M over three years, announced Feb 2021, 17 projects, 225C target
  for zonal-isolation tools; named awardees Welltec, PetroQuip, Colorado School of Mines, Battelle,
  Lawrence Livermore National Laboratory, Clemson, Stanford, Rice, Fervo Energy, UT Austin, Penn
  State, L15-027) and Solicitation 2022-2 (up to $44M, announced Aug 2022, 13 projects selected Nov
  2023; named awardees LBNL, NREL, Sandia, Oklahoma State, Stevens Institute, PetroQuip, Welltec,
  L15-028).
- **ARPA-E SUPERHOT** -- $30M program launched January 2025 targeting >375C/22MPa reservoirs,
  10-20GW baseload potential, 15-year well life; concept papers due Feb 19 2025, awards anticipated
  November 2025 (L15-029).
- **NASA HOTTech / Glenn Research Center (GEER facility)** -- ongoing program targeting 60-day
  Venus-surface survival for SiC/diamond/GaN electronics, batteries, actuators; named performer
  institutions University of Dayton, University of Arkansas, Arizona State University, Penn State,
  Stanford, and Boeing (L15-030); underlying SiC IC technology demonstrated by NASA Glenn itself
  (L15-009).
- **DOE / NETL -- Deep Trek (historical, 2003-2007)** -- $NT41834 award to Honeywell to develop
  225C+ SOI CMOS EEPROM/FPGA/op-amp/ADC components for deep drilling, establishing two decades of
  program continuity with today's DARPA/ARPA-E efforts (L15-031).
- **Baker Hughes** -- FY2025: $600M R&D spend, $2.0B New Energy orders (exceeding a $1.4-1.6B
  internal target), including a named contract for equipment on five Organic Rankine Cycle
  geothermal power plants (300MW total) plus subsurface drilling/production-technology awards for
  the same project (L15-040).
- **SLB + Ormat Technologies** -- October 27, 2025 partnership to design/build an Enhanced
  Geothermal Systems (EGS) pilot at an existing Ormat site, explicitly to de-risk commercial-scale
  EGS using SLB's subsurface/well-construction capability (L15-041).
- **Rio Tinto (with Caterpillar/WesTrac)** -- named, quantified 2019 equipment order for the
  Koodaideri iron-ore project: 20 autonomous 793F haul trucks, 4 autonomous blast drills, plus
  loaders/dozers/diggers, integrated with Rio Tinto's own mine-automation system (L15-042); no
  dollar figure disclosed.
- **Chinese state/academic buyers (diffuse, not a single named tender)** -- China Aerospace
  Components Engineering Center co-authors a 2024 GaN-radiation study explicitly framed around
  aerospace deployment risk (L15-013); China University of Petroleum authors a 2023 review
  explicitly diagnosing drilling-side (not just electronics-side) bottlenecks for high-temperature
  geothermal (L15-021) -- both signal institutional demand without a disclosed contract value.

## Incumbent map (companies, products, price signals)

| Company | Geography | Product / signal | Evidence |
|---|---|---|---|
| CISSOID SA | EU (Belgium) | CHT/CMT/CXT high-temp IC families (-55 to +225C), SiC/GaN gate drivers to 1700V, 1200V SiC/IGBT power modules (20-550A); CHT family now marked obsolete/last-time-buy; no public pricing | L15-043 |
| Honeywell Aerospace | US | HTMOS high-temp microelectronics (-55 to +225C, 5-year life) for downhole MWD/intelligent completions; CISSOID markets itself as a replacement for Honeywell's obsoleted parts | L15-044 (not independently fetched), cross-ref L15-043 |
| Baker Hughes | US | $600M FY2025 R&D; geothermal ORC equipment contract (5 plants, 300MW); New Energy orders $2.0B FY2025 | L15-040 |
| SLB | US/multinational | EGS pilot partnership with Ormat (Oct 2025), contributing subsurface/well-construction expertise | L15-041 |
| Ormat Technologies | US | Geothermal power-plant design/operations partner to SLB EGS pilot | L15-041 |
| NASA Glenn Research Center | US (government) | SiC JFET-R ICs, 500C/1-year operation demonstrated; GEER test facility | L15-009, L15-030 |
| Honeywell (historical, Deep Trek) | US | 225C+ SOI CMOS EEPROM/FPGA/op-amp/ADC for deep drilling (2003-2007 DOE-funded) | L15-031 |
| University of Arkansas (Mantooth group) | US | Extended high-temp SiC CMOS circuits for Venus (NASA HOTTech performer) | L15-010, L15-030 |
| Caterpillar / WesTrac | US/Australia | Cat Command autonomous haulage system; 20 autonomous 793F trucks + 4 blast drills for Rio Tinto Koodaideri | L15-042 |
| Rio Tinto | Australia | Buyer/operator of autonomous haulage fleet under its own "Mine of the Future" automation system | L15-042 |
| Chiba Institute of Technology / Tohoku University / IRSI | Japan | Quince rescue robot, gamma-ray-tested for Fukushima Daiichi deployment | L15-011 |
| Beihang University | China | Nuclear-emergency rescue robot, gamma-ray-tested motion-control components | L15-012 |
| China Aerospace Components Engineering Center / CAS Institute of Microelectronics | China | GaN power-device radiation-effects research explicitly framed for aerospace qualification | L15-013 |
| China University of Petroleum | China | High-temperature geothermal drilling technology review (drill bits, fluids, casing) | L15-021 |
| Korea Aerospace University | South Korea | FPGA radiation fault-tolerance (TMR) research for spaceborne electronics | L15-022 |
| Chungbuk National University (KOSEF-funded) | South Korea | First domestic Korean SiC NMOS/PMOS devices and logic-circuit library (2003) | L15-038 |
| A*STAR / Institute of Microelectronics | Singapore | World's-first industry-grade 200mm SiC Open R&D Line (announced May 2025); partners ASM, centrotherm, Nissin, Soitec, Toray; users include STMicroelectronics | L15-039 |
| Xi'an Jiaotong University (Zhuangde Jiang / Yulong Zhao groups) | China | 4H-SiC pressure sensors for harsh environments; SiC pressure-sensor review | L15-006, L15-007 |

## 2026-2031 triggers

- **2026 (now):** DARPA THERMAL SBIR solicitation closed June 24, 2026 (L15-026); Baker Hughes
  FY2025 annual report published in 2026 shows New Energy/geothermal momentum already
  materializing ($2.0B orders, L15-040); this lane's most recent academic reviews (L15-007, L15-016,
  L15-018, L15-025) are dated 2026, indicating active, ongoing publication in SiC sensing, downhole
  MEMS, and autonomous haulage as of this session.
- **2025:** ARPA-E SUPERHOT launched (Jan 2025, $30M, L15-029) with awards anticipated November
  2025 (not yet confirmed awarded as of this session); A*STAR's SiC Open R&D Line opened (May 2025,
  L15-039); SLB-Ormat EGS pilot partnership announced (Oct 2025, L15-041); Korea Aerospace
  University FPGA radiation-tolerance paper published (L15-022).
- **2023:** DOE FORGE Solicitation 2022-2 projects selected (Nov 2023, $44M, L15-028); China
  University of Petroleum geothermal-drilling review published, diagnosing an unresolved
  drilling-technology gap (L15-021); Acta Physica Sinica neutron-radiation SiC paper published,
  showing radiation qualification for SiC remains incomplete even as thermal qualification matures
  (L15-020).
- **Through 2027-2031 (inference, not sourced to a single dated commitment):** if DOE FORGE's
  225C-target trajectory (2020-1, L15-027) continues toward ARPA-E SUPERHOT's 375C+ target
  (L15-029), expect a widening gap between what commercial high-temperature electronics vendors
  currently ship (225C, per CISSOID/Honeywell, L15-043/L15-044) and what superhot-rock geothermal
  drilling will require -- a gap this session found no vendor publicly addressing with a roadmap.
  If DARPA THERMAL's 800C mixed-signal IC target (L15-026) is met within its stated Phase II
  36-month window, a device-level solution could reach TRL maturity by approximately 2029-2030,
  independently of whether packaging/die-attach reviews (L15-005, L15-025) resolve their
  parallel, unsolved packaging bottleneck by then.

## US vs Asia differences

- **Program structure for high-temperature electronics:** The US pursues this through a
  multi-decade sequence of named federal programs with escalating temperature targets -- DOE Deep
  Trek (225C, 2003-2007, L15-031) to DOE FORGE (225C, 2020-2023, L15-027/L15-028) to ARPA-E
  SUPERHOT (375C+, 2025, L15-029) to DARPA THERMAL (800C, 2026, L15-026) -- alongside NASA's
  parallel Venus-focused HOTTech/GEER effort (L15-030). China's contribution found this session is
  academic/institutional rather than program-branded: no Chinese government solicitation or
  procurement notice with a disclosed funding figure for high-temperature electronics was located,
  but Chinese state-affiliated researchers (CAS Institute of Microelectronics, China Aerospace
  Components Engineering Center, L15-013; China University of Petroleum, L15-021) are actively
  publishing on the same underlying problems (GaN space radiation, geothermal drilling) --
  suggesting a genuine transparency asymmetry rather than lower research intensity, consistent with
  a pattern flagged in other lanes (e.g., L09) where Chinese space/energy R&D activity is visible
  academically but not through disclosed contract-value tenders.
- **Singapore and Korea are pursuing capability-building at the fabrication/foundational level
  rather than mission-specific programs.** A*STAR's SiC Open R&D Line (L15-039) is explicitly a
  shared-infrastructure play to close a wide-bandgap fabrication gap versus larger players, while
  Korea's SiC CMOS work spans two decades from a 2003 KOSEF-funded first-domestic-device milestone
  (L15-038) to 2025 spaceborne radiation-tolerance research (L15-022) -- both signal steady,
  government-linked capability investment without the large named dollar figures seen in
  comparable US DOE/DARPA/NASA programs.
- **Radiation-hardened robotics testing methodology converges across US/UK, Japan, and China even
  without a shared design philosophy.** Japan (Quince, post-Fukushima, L15-011) and China (Beihang
  nuclear-rescue robot, L15-012) both ran near-identical Co-60 gamma-irradiation qualification
  tests on off-the-shelf robot electronics roughly two years apart (2011 vs 2013), while a UK
  academic study (L15-002) argues for a materially different strategy (planned replacement of
  standard components rather than radiation-hardened design) -- indicating the empirical testing
  method has converged internationally, but the resulting engineering philosophy has not.
- **Autonomous mining haulage is a mature, currently-operating US/Australian commercial market**
  (Caterpillar/Rio Tinto, L15-042; academic mine-planning literature, L15-018) governed by an
  international ISO standard (L15-032, not confirmed to have a Chinese-market equivalent this
  session) -- this sub-lane is comparatively more commercially mature than the harsh-environment
  electronics sub-lane, where even DARPA/ARPA-E treat the core semiconductor problem as unsolved.

## Unresolved contradictions

1. Two consultancy reports size the same "downhole tools" market for the same forecast years
   (2025/2026) roughly 40% apart: Research and Markets ($5.79bn 2025 / $6.07bn 2026, L15-045) vs.
   Fortune Business Insights ($4.10bn 2025 / $4.31bn 2026, L15-046). Neither is reconciled here;
   both are T3 consultancy estimates requiring independent bottom-up triangulation.
2. SiC and GaN are simultaneously described as more radiation-tolerant than silicon in a general
   sense (per total-ionizing-dose framing, L15-013) and as measurably degraded by neutron/heavy-ion
   exposure in device-specific studies (L15-020 for SiC leakage current; L15-014 for GaN
   threshold-voltage shift) -- "more radiation-tolerant than silicon" should not be read as
   "radiation-immune" or "space-qualified," a distinction also flagged in the L09 lane for the same
   device classes used in a different (space electric-propulsion) context.
3. This lane's active-cooling literature (L15-023, L15-024) and native-high-temperature-device
   literature (L15-001, L15-004, L15-009) do not cite or compare against each other within the
   sources collected this session, despite addressing the identical downhole-electronics-survival
   problem -- it is unclear from available sources whether the field considers these complementary
   or competing approaches, or whether this is simply a citation-network gap in this session's
   search coverage.
4. CISSOID markets itself as a direct replacement for "Honeywell's obsoleted High Temperature
   Microelectronics Products" (per WebSearch snippet, cross-referenced in L15-043/L15-044 notes),
   implying Honeywell has exited or is exiting a product line CISSOID's own CHT family (the
   closest like-for-like competitor) has now also marked obsolete/last-time-buy -- suggesting either
   a genuine shrinking addressable market for this specific product class, or a supply-chain
   consolidation this session could not further characterize from public sources.
5. DOE's own high-temperature-electronics program lineage shows apparent target stagnation rather
   than steady progress: Deep Trek (2003-2007) and FORGE Solicitation 2020-1 (2021) both cite
   essentially the same ~225C target roughly 15-18 years apart (L15-031 vs. L15-027), while
   ARPA-E's SUPERHOT (2025, L15-029) and DARPA's THERMAL (2026, L15-026) then jump to 375C+ and
   800C respectively within the same few years -- this session could not determine from public
   sources whether the 2003-2021 gap reflects genuine technical difficulty in moving past 225C, or
   simply program-funding discontinuity between Deep Trek's 2007 conclusion and FORGE's 2020 start.

## Uncertainty and session limitations (honesty note)

Of the 46 collected records, 34 were independently fetched (full text, official standards-body
page, government program page, or Crossref bibliographic metadata) this session; the remainder
(L15-015, L15-022's affiliation only, L15-032, L15-033, L15-034, L15-036, L15-044, L15-045,
L15-046) rely on WebSearch-synthesized titles/snippets or partial fetches, each flagged
individually in its own `notes` field. WebFetch was blocked (HTTP 403), returned an
authentication-wall redirect loop, timed out, or returned unreadable binary/PDF content for a
substantial share of publisher pages this session: IEEE Xplore abstract pages (L15-004, L15-011,
L15-012), Nature.com (L15-006, L15-007, via idp.nature.com login-wall redirect), AIP Publishing
(L15-009), MDPI (L15-008 companion attempt), ACS Publications (L15-015), ISO.org (L15-032), IEC's
standards.iteh.ai sample PDF (L15-034, binary/undecodable), RTCA.org (L15-036), SEC EDGAR's
bkr-20251231.htm (L15-040's underlying 10-K), and Honeywell's own product page (L15-044, 60-second
timeout) -- these are flagged per-record and should be re-attempted with a text-extraction-capable
or authenticated tool before being treated as fully verified. Where full-text fetch failed,
Crossref API metadata (title/authors/journal/volume/DOI) was independently fetched and used in its
place to confirm bibliographic identity, but the underlying technical claim in `claim_supported`
is in several cases (L15-006, L15-007) carried over from an earlier WebSearch snippet rather than
independently re-verified against fetched full text -- explicitly flagged in each record's notes
rather than silently presented as verified, consistent with the honesty precedent set in the L09
lane brief. Several author-affiliation/geography tags (L15-001 Huzhou University; L15-005, L15-017,
L15-019, L15-023, L15-025 inferred Chinese/Japanese authorship from name patterns) are inferred
from author-name conventions or a single supplementary WebSearch rather than confirmed from the
article's own affiliation line, and are flagged as inferences in their respective notes for the
verifier to confirm or correct. The lane's overall T1 share is approximately 91% (42/46), well
above the mission's 70% floor; T3 records are capped at 2 (L15-045, L15-046), both market-size
estimates, consistent with the "at most 2-3" T3 ceiling in the wave-4 mandate.

## Opportunity-shaped pain statements

Presented as pain + who pays + evidence -- not startup pitches.

1. **Pain:** No industry-standard high-temperature semiconductor platform exists above ~250C;
   DOE/Honeywell (2003-2007), DARPA/NIST (2007), DOE FORGE (2020-2023), ARPA-E (2025), and DARPA
   THERMAL (2026) have each independently funded overlapping SiC/SOI/GaN high-temperature
   electronics research across two decades without a converged commercial platform emerging.
   **Who pays:** DOE, DARPA, and NASA repeatedly re-fund adjacent research; downhole-tool and
   aerospace-electronics integrators (Honeywell, Baker Hughes, SLB) absorb repeated
   non-recurring-engineering cost each time a new qualification cycle restarts. **Evidence:**
   L15-026, L15-027, L15-028, L15-029, L15-031, L15-037.
2. **Pain:** Radiation tolerance and thermal tolerance are separate properties that must be
   independently qualified -- SiC's thermal advantage does not prevent neutron-induced leakage
   current increases, and GaN's total-dose tolerance does not prevent single-event burnout at the
   drain-gate edge. **Who pays:** space/nuclear/aerospace power-electronics designers who cannot
   assume "high-temperature-rated" implies "radiation-qualified," and must run separate,
   expensive qualification campaigns for each property. **Evidence:** L15-013, L15-014, L15-020.
3. **Pain:** Packaging and die-attach reliability remains the limiting factor even where the
   semiconductor itself tolerates the target temperature, and at least one established commercial
   high-temperature IC product family (CISSOID CHT) has been marked obsolete/last-time-buy with no
   public successor announced. **Who pays:** downhole-tool OEMs and integrators who currently rely
   on CISSOID/Honeywell parts face a sourcing discontinuity for -55C-to-225C-rated ICs. **Evidence:**
   L15-005, L15-007, L15-015, L15-025, L15-043.
4. **Pain:** Government-funded high-temperature-electronics programs show long funding gaps (Deep
   Trek concluded 2007; FORGE's comparable 225C target did not restart at scale until 2020-2021)
   rather than continuous progress, and it is unclear from public sources whether this reflects
   genuine technical difficulty past 225C or simply program-funding discontinuity. **Who pays:**
   geothermal/oilfield operators and DOE itself bear the cost of re-establishing technical
   groundwork each time a program lineage restarts after a multi-year gap. **Evidence:** L15-027,
   L15-031.
5. **Pain:** Superhot-rock geothermal drilling's stated reservoir target (>375C, ARPA-E SUPERHOT)
   already exceeds what current commercial high-temperature electronics vendors ship (225C, per
   CISSOID/Honeywell), and this session found no vendor publicly addressing that gap with a
   roadmap. **Who pays:** ARPA-E-funded geothermal-drilling developers and their eventual utility/
   IPP customers bear technology-availability risk if downhole electronics cannot reach the
   reservoir temperatures the drilling/completion technology is being funded to access. **Evidence:**
   L15-029, L15-043, L15-044.
6. **Pain:** Two independent consultancy market-size estimates for the same "downhole tools"
   market and forecast years disagree by roughly 40%, with no bottom-up reconciliation available
   from either source. **Who pays:** investors and strategic planners sizing this market must
   choose between materially different TAM anchors without independent triangulation. **Evidence:**
   L15-045 vs. L15-046.
7. **Pain:** Radiation-hardened-robotics qualification for nuclear decommissioning shows a
   philosophical split -- Japan and China both empirically gamma-ray-test off-the-shelf robot
   electronics before deployment, while UK academic work argues planned replacement of standard
   components can beat specialized rad-hard design on cost -- with no session-found synthesis
   reconciling which approach is actually more cost-effective at scale. **Who pays:** nuclear
   decommissioning program operators (analogous to Japan's IRID/Fukushota Daiichi effort and
   China's domestic nuclear-emergency-response programs) who must choose a qualification philosophy
   without an independent cost-effectiveness comparison. **Evidence:** L15-002, L15-011, L15-012.
8. **Pain:** China's substantial state-affiliated research base in this lane (CAS Institute of
   Microelectronics, China Aerospace Components Engineering Center, China University of Petroleum,
   Xi'an Jiaotong University) produced no session-locatable tender or procurement-award document
   with a disclosed contract value, in contrast to the US's explicitly dollar-figured DOE/DARPA/
   ARPA-E program lineage -- a transparency asymmetry, not necessarily a lower-intensity research
   effort. **Who pays:** non-Chinese competitors, investors, and analysts face a harder
   competitive-intelligence problem sizing Chinese state demand in this lane. **Evidence:** L15-013,
   L15-020, L15-021, L15-006, L15-007.
9. **Pain:** Singapore (A*STAR) and Korea (KOSEF-funded Chungbuk National University, Korea
   Aerospace University) are both making steady, government-linked capability investments in SiC
   fabrication and radiation-tolerant space electronics respectively, but neither discloses a
   dollar figure comparable to the US's named program budgets, making relative investment-intensity
   comparison difficult. **Who pays:** regional semiconductor-strategy planners in Singapore/Korea,
   and investors trying to benchmark government commitment levels across geographies. **Evidence:**
   L15-038, L15-039, L15-022.
10. **Pain:** Autonomous mining haulage is commercially mature and ISO-standardized, but this
    session found no equivalent standard or comparably mature commercial deployment record for
    autonomous control in other harsh/hazardous industrial settings within this lane (subsea,
    downhole, nuclear-decommissioning robotics remain at pilot/qualification-testing stage rather
    than fleet-scale deployment). **Who pays:** operators in those less-mature sub-segments
    (nuclear decommissioning agencies, subsea/offshore operators) continue to bear higher
    per-operation human-exposure and qualification cost than mining operators who have already
    industrialized autonomous control. **Evidence:** L15-018, L15-032, L15-042, contrast with
    L15-002, L15-011, L15-012, L15-033.
11. **Pain:** Vendor pricing for high-temperature ICs and power modules is almost entirely
    undisclosed (neither CISSOID nor Honeywell publish list pricing), making cost-competitiveness
    benchmarking difficult for new entrants or downstream integrators. **Who pays:** anyone
    (integrator, investor, new entrant) trying to assess the addressable cost structure of
    high-temperature electronics in this lane must rely on scattered, non-comparable figures.
    **Evidence:** L15-043, L15-044.
12. **Pain:** Several standards central to this lane's autonomous-control and subsea-control scope
    (ISO 17757, API 17F/SIIS, IEC 60751) could not be independently fetched/verified in full text
    this session due to paywalls, while others (MIL-STD-883, DO-160G) were confirmed current --
    creating an uneven public-documentation base for a would-be entrant trying to understand
    qualification requirements across sub-segments of this lane. **Who pays:** smaller entrants
    without standards-subscription budgets face a higher research cost understanding compliance
    requirements than incumbents with existing standards-body relationships. **Evidence:** L15-032,
    L15-033, L15-034 (not independently fetched) vs. L15-035, L15-036 (confirmed).
