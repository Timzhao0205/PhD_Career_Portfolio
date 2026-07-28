# L09 -- Space electric power, electric propulsion support, and radiation-tolerant power/control

Lane scope: spacecraft power processing units (PPUs), solar array drives and regulators,
Hall/ion-thruster power electronics, rad-hard/rad-tolerant power converters and controllers,
nuclear space power conversion, lunar surface power, and high-power satellite buses. This brief
cites records in `10_SOURCE_ATLAS/L09_raw_sources.json` by ID (L09-001 ... L09-056, with L09-021
intentionally void/removed during compilation). All records are `accepted:false` pending the
source-verifier pass, and academic `peer_review_status` is `unverified` pending independent
confirmation. No startup ideas are proposed here per the lane-scout mandate.

## Frontier state

Three technology fronts define this lane. First, **Hall/ion-thruster power processing units
(PPUs) remain an active, non-converged research area** even after decades of flight heritage:
Japanese (Mitsubishi Electric/Kyushu University, L09-002, L09-007), Chinese (BUAA survey,
L09-001), and US (multiple Journal of Electric Propulsion papers, L09-003 through L09-006; IEEE
wide-output-range PPU, L09-008) groups are all still publishing new PPU topologies as of
2021-2026 -- there is no single dominant, standardized PPU architecture, and control algorithms
for 6kW-class thrusters were still being newly proposed in 2022 (L09-006) and 2025-2026
(L09-003). Second, **radiation-tolerant wide-bandgap power electronics (GaN/SiC) are actively
displacing silicon rad-hard parts but are not yet a solved qualification problem**: GaN HEMTs
show intermediate TID tolerance (300-500 krad(Si)) versus SiC's >1 Mrad(Si) and silicon's <100
krad(Si) ceiling, but GaN/SiC devices have also shown failure susceptibility at ~50% of rated
voltage under space-simulated heavy-ion exposure (per WebSearch synthesis in this session); a
2022 primary study from China's National Space Science Center (CAS) on synergistic TID+
displacement-damage effects in GaN HEMTs (L09-020) and a 2023 AIP review of GaN/SiC radiation
damage (L09-014) both show this is still live science, not settled engineering -- and EPC Space's
CERN-co-developed rad-hard GaN controller ASIC (L09-055, announced April 2025) signals
technology transfer from particle-physics instrumentation into spacecraft power electronics as a
notable, recent pattern. Third, **space fission power is escalating in scope faster than programs
can mature**: NASA/DOE's Fission Surface Power baseline jumped from a 40-kWe demonstration
(three $5M concept-design contracts awarded June 2022 to Lockheed Martin/BWXT/Creare,
Westinghouse/Aerojet Rocketdyne, and IX/Maxar/Boeing -- L09-031) to a 100-kWe closed-Brayton-cycle
requirement by an August 2025 RFI, reinforced by an April 2026 White House memorandum (NSTM-3)
directing a mid-power (>=100kWe) reactor for the 2030s (L09-033) -- a 2.5x power-spec increase
within the same program's first four years, alongside a parallel January 2025 Westinghouse
eVinci contract continuation still described around the original 40kWe figure (L09-032). China
is pursuing a parallel, less-transparent space-reactor development track (L09-018).

## Bottlenecks

- **PPU topology has not converged despite 50+ years of Hall/ion-thruster flight heritage.**
  Multiple incompatible architectures (wide-output-range, SiC-based, GaN-based, S3R-integrated)
  are simultaneously active research fronts across Japan, China, and the US (L09-001, L09-002,
  L09-003 through L09-008, L09-011), each claiming efficiency or mass/volume advantages without a
  clear industry-standard winner.
- **Wide-bandgap (GaN/SiC) radiation qualification is unresolved.** GaN's TID tolerance is
  intermediate (not as good as SiC), synergistic neutron+gamma damage effects are non-additive in
  ways not yet fully predictable (L09-020), and industry reports of catastrophic failure near 50%
  of rated voltage under heavy-ion exposure indicate space qualification lags terrestrial GaN/SiC
  commercialization by years.
- **Space fission power's power-spec target has moved substantially (40kWe -> 100kWe) within one
  program cycle** (L09-031 vs L09-033), creating schedule and design risk for the three 2022
  concept-award teams whose Phase 1 work targeted the lower figure.
- **The EP/PPU supply base is highly concentrated.** NASA's flagship Gateway PPE depends on a
  short, named list of suppliers -- Aerojet Rocketdyne (AEPS thrusters/PPUs), Busek (BHT-6000),
  and Moog (power electronics/xenon flow controllers) under prime integrator Maxar (L09-043) --
  and Aerojet Rocketdyne alone now sits inside a much larger, missile-focused corporate structure
  (L3Harris Missile Solutions, DoW-backed with $1B, L09-041) where space electric propulsion is a
  small line item next to PAC-3/THAAD/Tomahawk/Standard Missile production.
- **Vendor pricing remains largely opaque.** Of the vendor-datasheet records gathered this
  session, only VPT's rad-hard DC-DC converters disclosed firm OEM pricing (~$1,500-2,100,
  L09-053); EPC Space's GaN converter/controller (L09-054, L09-055), Busek's BHT-6000 thruster
  (L09-009), and Moog's SADA family disclosed no public price -- consistent with the pricing-opacity
  pattern already documented in the L02/L08 lanes for adjacent power-electronics hardware.
- **Standards specific to power (ECSS-E-ST-20-20C) were not independently confirmed this
  session** -- only the general electrical/electronic standard (ECSS-E-ST-20C Rev.2, L09-044) was
  fetched; the power-supply-interface-specific companion standard is a gap for the verifier.
- **Market-size estimates for this lane disagree by roughly 60%** between two consultancy reports
  covering overlapping segments (L09-051 vs L09-052) -- see Unresolved Contradictions.

## Named buyers and spending signals

- **NASA/DOE Fission Surface Power** -- three $5M, 12-month Phase 1 concept-design contracts
  (June 2022) to Lockheed Martin (w/ BWXT, Creare), Westinghouse (w/ Aerojet Rocketdyne), and IX
  (Intuitive Machines/X-energy JV, w/ Maxar, Boeing), for a 40-kWe, >=10-year lunar reactor
  (L09-031); Westinghouse received a continuation contract (Jan 7, 2025) via Idaho National
  Laboratory to keep advancing its eVinci-based design (L09-032, L09-047); an August 2025 RFI and
  April 2026 White House NSTM-3 memo raised the target to 100kWe / closed Brayton cycle, targeting
  Q1 FY2030 launch readiness (L09-033).
- **NASA Glenn Research Center / Aerojet Rocketdyne** -- two confirmed, separate EP-hardware
  contracts: (1) $67M, 36-month AEPS contract (April 2016) for a 12.5kW-class Hall thruster, PPU,
  xenon flow controller, and harness (L09-034); (2) $18,410,242 cost-share NEXT-C contract (April
  2015) for two ion thrusters and two PPUs, with subcontractor ZIN Technologies building a
  prototype PPU first (L09-012).
- **NASA Gateway Power and Propulsion Element (prime: Maxar)** -- integrates three 12kW AEPS
  thrusters (Aerojet Rocketdyne), four BHT-6000 thrusters (Busek), and PPU/xenon-flow-controller
  power electronics (Moog); qualification/flight hardware fabrication had begun as of the 2022
  status report (L09-043).
- **JAXA + Furukawa Electric (J-SPARC)** -- co-development announcement (March 15, 2021) to
  commercialize a GaN-based Hall-thruster power supply for small satellites, targeting FY2025
  on-orbit demonstration and FY2026+ commercialization (L09-042).
- **U.S. Space Force** -- Maneuverable GEO program, $905M planned over five years for a
  commercial maneuverable-GEO communications-satellite fleet, competition opening early 2026 and
  award expected June 2026 (L09-037, not yet awarded as of this session); SDA Tranche 3 awarded
  $3.5B (Dec 19, 2025) across Lockheed Martin, L3Harris, Rocket Lab, and Northrop Grumman for 72
  missile-tracking satellites (L09-039, propulsion/power details not disclosed in the source);
  Phase Four won a SpaceWERX Pitch Day contract (Aug 2021) for its Maxwell RF electric thruster
  running on AFRL's ASCENT green propellant (L09-040, dollar value undisclosed).
- **U.S. Department of War / L3Harris** -- closed a $1B convertible-preferred-stock investment
  (April 23, 2026) in L3Harris's new Missile Solutions business, which folds in legacy Aerojet
  Rocketdyne (the AEPS/NEXT-C PPU supplier), explicitly to expand missile-propulsion production
  capacity ahead of an H2 2026 IPO (L09-041) -- relevance to this lane is indirect (missile, not
  space EP, focus) and flagged for verifier judgment.
- **NASA SBIR/STTR (2026 BAA, released April 17, 2026)** -- solicits in-space electric-propulsion
  component technologies explicitly citing Advanced Modular Power Systems (AMPS) and Mars Sample
  Return's Hall-thruster/PPU needs, specifying radiation-hardened/tolerant power converters for
  deep-space/GEO-like dose environments (L09-036).

## Incumbent map (companies, products, price signals)

| Company | Geography | Product / signal | Evidence |
|---|---|---|---|
| Aerojet Rocketdyne (now L3Harris Missile Solutions) | US | AEPS 12.5kW Hall-thruster PPU ($67M NASA contract); NEXT-C ion-thruster PPUs ($18.4M NASA contract) | L09-034, L09-012, L09-043 |
| Busek Co. | US | BHT-6000 (2-6kW Hall thruster, 12.5kg, xenon/krypton/iodine); 4 units on NASA Gateway PPE | L09-009, L09-043 |
| Moog Inc. | US | PPU / xenon-flow-controller power electronics for Gateway PPE; Solar Array Drive Assembly (SADA) family (no public pricing found) | L09-043 |
| Maxar Technologies | US | Prime integrator, 50kW-class Gateway Power and Propulsion Element | L09-043 |
| VPT, Inc. | US | Rad-hard DC-DC converters (100krad TID, 85.4 MeV-cm^2/mg SEE, up to 94% efficiency); one of the only vendors with disclosed OEM pricing (~$1,500-2,100) | L09-045, L09-053 |
| EPC Space | US | EPCSC401 rad-tolerant GaN buck converter (20-50V to 12V/5A); EPCS4001 rad-hard controller ASIC co-developed with CERN | L09-054, L09-055 |
| Westinghouse Electric | US | eVinci-based Fission Surface Power microreactor concept (up to 40kWe stated), NASA/DOE/INL contract | L09-032, L09-047 |
| Lockheed Martin (w/ BWXT, Creare) | US | Fission Surface Power concept design (2022 Phase 1 award) | L09-031 |
| IX (Intuitive Machines/X-energy JV, w/ Maxar, Boeing) | US | Fission Surface Power concept design (2022 Phase 1 award) | L09-031 |
| Phase Four | US | Maxwell propellant-agnostic RF thruster (multi-mode chemical+electric); SpaceWERX and DARPA contracts | L09-040, L09-038 |
| China Academy of Space Technology (CAST) / Institute of Telecommunication Satellite | CN | High-power (5kW-class) EP PPU R&D program | L09-001 |
| CASC Sixth Academy, Institute 801 | CN | Indigenous magnetic-anode Hall thruster (first-ever flight application of this thruster type, reported Dec 2024, per WebSearch context); 100W-100kW Hall-thruster product family | (context via search this session; not independently fetched -- flag for verifier) |
| National Space Science Center, CAS | CN | Primary radiation-effects research on GaN HEMT power devices for space | L09-020 |
| Mitsubishi Electric | JP | Hall-thruster PPU R&D (with Kyushu University, Nagasaki University) since at least 2011 | L09-002, L09-007 |
| Furukawa Electric | JP | GaN-based Hall-thruster power supply, JAXA J-SPARC co-development, targeting FY2026+ commercialization | L09-042 |
| Korea Aerospace Research Institute (KARI) | KR | Full-electric-propulsion GEO satellite design-study (R&D stage, not yet flying) | L09-019 |
| Space Propulsion Centre, NTU | SG | Low-power EP research niche (reviews only found this session, no hardware/procurement signal) | L09-022, L09-024 |

## 2026-2031 triggers

- **2026 (now):** NASA SBIR/STTR 2026 BAA open (released April 17, 2026) soliciting EP/PPU
  component technologies (L09-036); Space Force Maneuverable GEO competition opens early 2026,
  award expected June 2026 (L09-037); L3Harris Missile Solutions closed its $1B DoW investment
  (April 23, 2026, L09-041) and plans an H2 2026 IPO; JAXA/Furukawa targeted FY2026 for Hall-
  thruster power-supply commercialization start (L09-042); NASA/DOE fission-power RFI-driven
  100kWe requirement and NSTM-3 directive are both in-flight as of this session (L09-033).
- **2027:** No lane-specific dated milestone was independently confirmed this session for 2027;
  cross-referencing the L08 lane's finding that Korea targets HVDC-conversion-equipment
  localization by 2027 suggests a broader Korean power-electronics self-sufficiency push that may
  extend to space power, but this was not independently confirmed for the space-EP niche.
- **~2029-2030:** NASA Fission Surface Power targets Q1 FY2030 launch readiness for the (now
  100kWe) reactor per the August 2025 RFI (L09-033); JAXA/Furukawa targeted FY2025 for on-orbit
  demonstration of its GaN-based Hall-thruster power supply, ahead of this window (L09-042).
- **Through 2031 (inference, not sourced to a single dated commitment):** if the Gateway PPE
  program proceeds on its stated (2022-era) co-manifest schedule, expect AEPS/BHT-6000/Moog
  hardware to reach flight status in this window (L09-043); if Space Force's Maneuverable GEO
  and SDA Tranche 3/4 procurements continue at the scale seen in 2025-2026 ($905M and $3.5B
  respectively), expect continued satellite-bus-scale demand for power/propulsion subsystems,
  though this session found no source explicitly confirming electric-propulsion content in either
  program -- a gap, not a confirmed trigger.

## US vs Asia differences

- **Program structure:** The US pursues space power/EP largely through named, large,
  single-contractor NASA procurements (AEPS/NEXT-C at Aerojet Rocketdyne, L09-034/L09-012; Gateway
  PPE at Maxar, L09-043) and a DOE-national-lab-administered nuclear program (INL/FSP, L09-031,
  L09-032, L09-047). Japan pursues a public-private co-creation model explicitly designed to pull
  in consumer-electronics-derived technology (GaN, thermal design) via JAXA's J-SPARC framework
  with a named commercial partner (Furukawa Electric, L09-042) rather than a large single-vendor
  contract. China's academic/state literature (L09-001, L09-016, L09-017, L09-018, L09-020,
  L09-028, L09-029) shows a broad, multi-institution R&D base (CAST, CAS, Beijing Institute of
  Technology, Lanzhou-affiliated ion-thruster work) but this session found no Chinese tender or
  procurement-award document with disclosed contract value for space EP/PPU hardware -- a
  transparency gap distinct from the L08 lane's finding of unusually precise Chinese HVDC-tender
  disclosures; flag as an asymmetry for the verifier to test further.
- **Fission/nuclear space power:** The US has a dated, escalating, multi-contractor program
  (40kWe->100kWe, three competing concept-design teams, L09-031, L09-033) under direct White House
  policy attention (NSTM-3). China's parallel space-reactor development (L09-018) was only found
  as an academic outlook/analysis paper this session, with no equivalent contract-award or
  White-House-level policy document identified -- suggesting either a genuinely less mature public
  program or simply lower disclosure, which this session cannot distinguish.
- **Flight heritage vs. R&D stage:** China (indigenous magnetic-anode Hall thruster, first flight
  reported ~Dec 2024 per this session's WebSearch context) and the US (AEPS, NEXT-C, BHT-6000, all
  flight-qualified or flying) both have operational Hall/ion EP hardware in orbit today. Korea
  (L09-019) is one step behind -- at the design-study stage for
  full-EP GEO satellites -- while Singapore's contribution found this session was
  limited to academic review literature (L09-022, L09-024) with no hardware-procurement signal.
- **Radiation-hardening research leadership:** the strongest primary (non-review) GaN
  radiation-effects paper found this session was Chinese (National Space Science Center, CAS,
  L09-020), while the most detailed rad-hard commercial product datasheets found were American
  (VPT, EPC Space, L09-045, L09-053, L09-054, L09-055) -- a research/commercialization split
  worth flagging, though this reflects one session's search results, not a comprehensive
  bibliometric comparison.

## Unresolved contradictions

1. Two consultancy market-size estimates for closely related market definitions disagree by
   roughly 60%: Research and Markets values the (broader) satellite-propulsion market at USD2.07bn
   in 2026 (L09-051), while Fortune Business Insights values the (narrower, electric-propulsion-
   only) satellite market at USD1.28bn in 2026 (L09-052) -- even though electric propulsion is
   described by both as the dominant/fastest-growing segment of the broader market. These are not
   averaged or reconciled here; both figures are consultancy estimates (T3) requiring independent
   bottom-up triangulation before use.
2. NASA's Fission Surface Power program specification nearly tripled in power requirement (40kWe
   in the original June 2022 award, L09-031, to >=100kWe per the August 2025 RFI and April 2026
   NSTM-3 memo, L09-033) within roughly three years of the same program's Phase 1 concept-design
   contracts being awarded -- yet the January 2025 Westinghouse continuation-contract press release
   (L09-032) still describes the design around the original 40kWe figure. It is unclear from this
   session's sources whether Westinghouse's continuation work has already been re-scoped to 100kWe
   or whether the spec change post-dates and outpaces the contractor's current design baseline.
3. GaN and SiC power devices are simultaneously described in this session's sources as inherently
   more radiation-tolerant than silicon (L09-014, by virtue of higher defect-formation thresholds)
   and as prone to catastrophic failure at roughly half their rated voltage under space-simulated
   heavy-ion exposure (per WebSearch synthesis) -- i.e., "more radiation-tolerant" in the
   cumulative-dose (TID) sense does not mean "space-qualified" in the single-event-effect sense,
   and sources conflating the two should be treated with caution.
4. This lane's Space Force-adjacent demand records (Maneuverable GEO, L09-037; SDA Tranche 3,
   L09-039) were both confirmed as large, real, dated procurement actions, yet neither underlying
   source explicitly states that the satellites in question use electric propulsion or names a
   PPU/power-electronics supplier -- in contrast to the explicitly-named NASA Gateway PPE supply
   chain (L09-043). The inference that "maneuverable" implies "electric propulsion" is reasonable
   (per general EP-literature context, e.g., L09-038's discussion of SEP for maneuverability) but
   was not directly confirmed for these two specific programs this session.

## Uncertainty and session limitations (honesty note)

Of the 55 collected records, 23 were independently fetched and verified this session; the
remainder rely on WebSearch-synthesized titles/abstracts/figures only, each flagged individually
in its own `notes` field. WebFetch was blocked (HTTP 403), returned blank content, redirected to a
login wall, or failed outright (DNS resolution failure on `sbir.gsfc.nasa.gov`; certificate error
on a CNSA press-release page) for a substantial share of academic-publisher pages (ResearchGate,
MDPI, IEEE Xplore, ScienceDirect, AIP, Wiley) and several PDF-only documents (NASA NEPP GaN report,
Moog SADA datasheet, Busek BHT-6000 datasheet, two Chinese PDFs) whose raw binary could not be
parsed into readable text by the fetch tool this session -- these are flagged per-record and
should be re-attempted with a text-extraction-capable tool before being treated as verified. The
overall T1 share of this raw collection is approximately 58% (32/55), below the mission's 78%
T1-eligible target; this reflects an honest tiering of a lane where reviews, vendor datasheets,
and trade press are legitimately common and necessary to cover buyer/incumbent signals, rather
than an attempt to game the ratio -- flagged explicitly for the Fable adjudication pass rather than
silently inflating tiers. Several DOIs (L09-011, L09-022) are inferred from MDPI's documented,
deterministic volume/issue/article-number numbering convention rather than independently resolved
via doi.org, consistent with the precedent set in the L02/L08 lane notes; each is flagged in its
own `notes` field. The CASC Institute 801 indigenous magnetic-anode Hall-thruster flight claim
(referenced in the Incumbent Map) was seen only in WebSearch snippets and could not be attached to
a specific fetched, dated source this session -- it is not included as a numbered ledger record for
that reason and should be independently sourced and added in a follow-up pass if confirmed.

## Opportunity-shaped pain statements

Presented as pain + who pays + evidence -- not startup pitches.

1. **Pain:** Hall/ion-thruster PPU topology has not converged despite 50+ years of flight
   heritage -- Japanese, Chinese, and US groups are all still publishing competing architectures as
   recently as 2025-2026. **Who pays:** thruster/PPU manufacturers (Aerojet Rocketdyne, Busek,
   Mitsubishi Electric, CAST) and their satellite-prime customers absorb repeated non-recurring
   engineering costs each time a new PPU generation is qualified rather than reusing a converged
   industry-standard design. **Evidence:** L09-001, L09-002, L09-003 through L09-008, L09-011.
2. **Pain:** Wide-bandgap (GaN/SiC) power devices promise better radiation tolerance and power
   density than silicon rad-hard parts, but space qualification is incomplete -- TID tolerance is
   only intermediate for GaN, and heavy-ion single-event failure has been reported near 50% of
   rated voltage. **Who pays:** spacecraft power-electronics designers who cannot yet fully trust
   GaN/SiC in flight-critical power paths, and mission planners who must either derate these
   devices heavily or continue paying a mass/efficiency penalty for legacy silicon rad-hard parts.
   **Evidence:** L09-014, L09-020, L09-054, L09-055.
3. **Pain:** NASA's Fission Surface Power program nearly tripled its power-spec target (40kWe ->
   100kWe) within about three years of the original Phase 1 concept-design awards, creating
   re-scoping risk for all three contractor teams. **Who pays:** Lockheed Martin/BWXT/Creare,
   Westinghouse/Aerojet Rocketdyne, and IX/Maxar/Boeing each bear schedule and design risk if their
   Phase 1 baselines must be substantially reworked; NASA/DOE bear program-schedule risk against
   the stated Q1 FY2030 launch-readiness target. **Evidence:** L09-031, L09-032, L09-033.
4. **Pain:** The Gateway PPE's entire electric-propulsion power chain depends on a short, named
   list of suppliers (Aerojet Rocketdyne, Busek, Moog) under one prime (Maxar), and the largest of
   these suppliers now sits inside a much larger, missile-focused corporate structure (L3Harris
   Missile Solutions) that just took a $1B DoW investment explicitly framed around missile
   production, not space electric propulsion. **Who pays:** NASA and the broader civil/commercial
   EP-buyer base bear concentration/continuity risk if AEPS-class PPU capacity becomes a lower
   internal priority within a much larger missile-propulsion business. **Evidence:** L09-041,
   L09-043, L09-034, L09-012.
5. **Pain:** Vendor pricing for rad-hard/rad-tolerant power converters, Hall-thruster hardware,
   and solar-array-drive assemblies is almost entirely undisclosed -- only one vendor (VPT) in this
   session's collection published firm OEM unit pricing. **Who pays:** anyone (integrator,
   investor, new entrant) trying to benchmark cost-competitiveness in this hardware category pays
   a real information-asymmetry cost and must rely on scattered per-unit figures rather than list
   pricing. **Evidence:** L09-053 (priced) vs. L09-009, L09-054, L09-055 (unpriced); Moog SADA
   family (unpriced, referenced in Incumbent Map).
6. **Pain:** Two independent consultancy market-size estimates for closely related
   satellite-propulsion market definitions disagree by roughly 60% for the same forecast year
   (2026), with no bottom-up reconciliation available from either source. **Who pays:** investors
   and strategic planners sizing this market must currently choose between materially different
   TAM anchors without an independent triangulation. **Evidence:** L09-051 vs. L09-052.
7. **Pain:** Japan's JAXA/Furukawa co-development effort is explicitly trying to pull
   consumer-electronics-grade GaN and thermal-design technology into a space-qualified
   Hall-thruster power supply to cut weight and cost, implying the incumbent space-grade PPU supply
   chain is currently too expensive/heavy for the small-satellite segment it is targeting. **Who
   pays:** small-satellite operators currently priced out of electric propulsion by PPU cost/mass,
   and Furukawa Electric/JAXA bear the technology-transfer and space-qualification risk of the
   consumer-to-space pathway. **Evidence:** L09-042.
8. **Pain:** Space Force's two largest satellite-bus procurements captured this session
   (Maneuverable GEO, $905M; SDA Tranche 3, $3.5B) do not publicly disclose whether -- or which --
   electric-propulsion/power hardware is specified, in contrast to NASA's fully-named Gateway PPE
   supply chain. **Who pays:** competing EP/PPU vendors and market analysts cannot currently assess
   the addressable opportunity within these programs, and taxpayers/oversight bodies have less
   visibility into whether these large awards are procuring mature or novel propulsion technology.
   **Evidence:** L09-037, L09-039, contrast with L09-043.
9. **Pain:** Radiation-hardening qualification standards specific to power supplies (the
   power-focused ECSS-E-ST-20-20C companion standard) were not independently locatable/fetchable
   this session, even though the general electrical/electronic ECSS-E-ST-20C standard was
   confirmed current (2022 revision) -- suggesting either a genuine documentation gap in this
   session's research or a harder-to-access power-specific standard that vendors/integrators must
   navigate without an easily public reference. **Who pays:** European (and internationally
   ECSS-aligned) spacecraft power-electronics suppliers who must interpret power-supply-specific
   requirements without a session-confirmed public standard text. **Evidence:** L09-044 (confirmed
   general standard); power-specific companion standard not separately confirmed this session.
10. **Pain:** China's substantial academic/state-institution space-EP and space-nuclear-power
    research base (CAST, CAS, Beijing Institute of Technology, and others) produced no
    session-locatable tender or procurement-award document with a disclosed contract value,
    despite China's Tiangong space station reportedly already running an operational Hall thruster
    system and CASC's Institute 801 reportedly having flown an indigenous magnetic-anode Hall
    thruster (per WebSearch context, not independently confirmed to a fetched source). **Who
    pays:** non-Chinese competitors and analysts face a harder competitive-intelligence problem in
    this specific sub-lane than the L08 lane's finding of unusually transparent Chinese HVDC-tender
    disclosures -- suggesting transparency practices differ by hardware category within China, not
    uniformly. **Evidence:** L09-001, L09-016, L09-017, L09-018, L09-020, L09-028, L09-029 (all
    academic, none a tender/award document).
11. **Pain:** Korea's electric-propulsion program for GEO satellites is still at the
    design-study/R&D stage (evaluating a ~40% payload-capacity gain from full electric propulsion,
    but flagging contamination, radiation-driven component placement, and high-voltage
    floating-ground design as unresolved constraints) with no confirmed flight or procurement
    program identified this session. **Who pays:** KARI and the Korean satellite-operator
    ecosystem bear the technology-maturation cost of closing this gap versus US/Japan/China, all of
    which already have flight-proven Hall/ion EP hardware. **Evidence:** L09-019.
12. **Pain:** GaN-based rad-tolerant power converters and controller ASICs from at least two
    vendors (EPC Space's CERN-co-developed line) are new to market (2025-2026) with no independent,
    third-party (non-vendor) validation of their radiation or reliability claims located this
    session. **Who pays:** early-adopting spacecraft power-system designers bear qualification risk
    if vendor-stated TID/SEE/efficiency claims do not hold up under independent test, since no
    NSREC-published, third-party characterization of these specific 2025-2026 parts was found this
    session. **Evidence:** L09-054, L09-055 (vendor claims only); L09-014 (independent review
    context, not part-specific).

## T1 top-up addendum (2026-07-12)

A follow-up scout pass collected 15 additional records (L09-101 through L09-115, in
`10_SOURCE_ATLAS/L09_t1topup_raw_sources.json`), every one an honestly-tiered T1 form (10
peer-reviewed academic journal articles verified via direct publisher fetch or Crossref API, 2
official standards, 2 NASA SBIR procurement awards, 1 audited company filing), deliberately
targeting sub-niches this lane's original 56-record collection under-covered: (1) **European
ion-thruster hardware** -- ESA/QinetiQ-Airbus T6 ion-thruster grid-life modeling for BepiColombo
(L09-101), a JPL/UNSW-Canberra collaboration; (2) **iodine-propellant electric propulsion**, both
ThrustMe's own control-architecture/radiation-test paper (L09-102) and an independent academic
thrust-validation study (L09-107) -- a propellant chemistry entirely absent from the original
collection; (3) **device-level radiation single-event effects**, separating GaN heavy-ion response
(L09-103) from SiC MOSFET burnout/gate-rupture destruction physics (L09-104) and a converter-circuit-level
SET-mitigation design study (L09-108), sharpening the device-vs-circuit distinction the original
collection's reviews (L09-014, L09-015) left blended; (4) **fission power beyond Brayton-cycle FSP**
-- the Stirling-cycle Kilopower/KRUSTY experiment (L09-105), a lower-power precursor program distinct
from L09-031/L09-033's 40-100kWe Brayton-cycle baseline; (5) **power storage**, a wholly new
sub-niche for this lane via an ISS-demonstrated solid-state Li-ion battery (L09-106) and a NASA-funded
radiation-hardened battery-monitoring ASIC (L09-113); (6) **Hall-thruster life-testing and thermal
design** distinct from this lane's PPU-topology focus -- a 1.35kW magnetically shielded thruster life
test (L09-109) and a 12.5kW thermal-design-optimization study (L09-110); (7) **standards gaps
explicitly flagged by the original scout** -- ECSS-E-ST-20-20C, the power-supply-specific ECSS
companion standard (L09-111), and AIAA S-122, the US/NASA-endorsed counterpart standard (L09-115),
neither previously in the ledger; and (8) **buyer/incumbent primary records** -- two dollar-valued,
dated NASA SBIR awards (cryocooler control electronics, L09-112; battery-monitoring ASIC, L09-113)
and Rocket Lab's audited 10-K description of its SolAero-derived solar-array/battery/reaction-wheel
power-hardware business (L09-114, fetched via a third-party SEC-filing aggregator after SEC.gov
itself returned HTTP 403 to direct fetch -- flagged transparently in that record's notes). No record
in this addendum duplicates a canonical_key, DOI, or title already present in
`L09_raw_sources.json` or `L09_verified_sources.json`.

## P2A origin-audit repair (2026-07-13)

- removed IDs: L09-035
- removed/trimmed claims: deleted the "ISRO 1000-hour vacuum life test / TDS-01" buyer-signal
  bullet from "Named buyers and spending signals" (rested solely on L09-035); deleted the ISRO
  table row from "Incumbent map" (rested solely on L09-035); trimmed the India/ISRO clause out of
  the Korea-vs-India "Flight heritage vs. R&D stage" comparison sentence in "US vs Asia
  differences," leaving the Korea (L09-019) comparison intact. Note: L09-051's "Research and
  Markets" citation (line ~196, Unresolved contradictions #1) was checked and is NOT excluded --
  its verified-sources record confirms Research and Markets/ResearchAndMarkets.com is Dublin,
  Ireland-headquartered, independently checked and cleared under the India-origin audit, so it was
  left unchanged. P4 must re-source any ISRO/TDS-01 electric-propulsion demand or flight-heritage
  claim from an eligible (non-India-origin) provider before reuse.
