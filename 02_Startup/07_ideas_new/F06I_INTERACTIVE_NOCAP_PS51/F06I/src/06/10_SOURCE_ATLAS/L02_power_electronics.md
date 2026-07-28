# L02 -- Extreme-efficiency and ultra-high-density power electronics

Lane scope: wide/ultra-wide-bandgap (WBG/UWBG) converters, medium-voltage solid-state
transformers (SST), high-density datacenter/AI power delivery, 800VDC rack architectures,
high-frequency magnetics, advanced gate drivers, and converter reliability. This brief cites
records in `10_SOURCE_ATLAS/L02_raw_sources.json` by ID (L02-001 ... L02-054); all records are
`accepted:false` pending the source-verifier pass, and academic `peer_review_status` is
`unverified` pending independent confirmation. No startup ideas are proposed here per the
lane-scout mandate.

## Frontier state

The lane's live commercial inflection is the AI datacenter power-delivery rearchitecture from
54V/415-480VAC distribution to centralized 800VDC (with a path to 1500VDC), driven by GPU racks
moving from ~120kW today toward 600kW-1MW by 2027 (L02-043, L02-044). NVIDIA's own technical blog
(fetched, L02-043) states the 800VDC architecture "improves end-to-end efficiency by up to 5%,"
"enables 45% reduction in copper requirements," and cuts maintenance cost up to 70% and TCO up to
30% versus 54V systems, aligning to Kyber rack-scale systems and Rubin Ultra GPUs in 2027. The Open
Compute Project's "Mount Diablo" initiative -- authored by Google, Meta, and Microsoft -- is
standardizing both conventional transformer-rectifier and solid-state-transformer power units for
this transition, with an updated whitepaper due later in 2026 (L02-044).

Underneath this systems-level shift, three technical fronts are advancing in parallel:
(1) wide-bandgap (SiC, GaN) device performance and reliability (L02-004, L02-005, L02-006,
L02-013, L02-014, L02-015, L02-016), (2) medium-voltage solid-state transformers that could
eventually replace line-frequency transformers in both grid distribution and EV fast-charging
(L02-001, L02-002, L02-017, L02-021, L02-029, L02-030), and (3) extreme point-of-load
conversion (48V-to-<1V at 1500-2000A) to feed GPU/CPU/FPGA dies directly (L02-022, L02-023,
L02-024). Ultra-wide-bandgap materials (Ga2O3, diamond, AlN) remain earlier-stage, with Sandia
explicitly researching them alongside SiC/GaN (L02-031) and multiple 2019-2025 reviews tracking
Ga2O3's high Baliga figure-of-merit (>3000) but immature device/reliability base (L02-025,
L02-027).

## Bottlenecks

- **Converter reliability at the device and package level.** GaN dynamic Ron / trapping effects
  (L02-006, L02-013, L02-014, L02-015, L02-016) and WBG packaging/thermal-cycling failure modes
  (L02-028) remain active research areas, not solved problems -- directly relevant to warranty and
  field-failure economics for 800VDC-era hardware operating at higher current density.
- **DC-link capacitor reliability.** Electrolytic/film capacitors remain a leading converter
  failure mechanism (L02-010); higher power density and higher ambient temperature in 800VDC racks
  compress the margin for capacitor lifetime.
- **Standards mismatch for solid-state transformers.** SST prototypes must still satisfy IEC 60076
  conventional-transformer test requirements designed for magnetic-core devices, a documented
  compliance/cost bottleneck slowing SST commercialization in both grid and EV-charging contexts
  (L02-036).
- **High-frequency magnetics design.** Planar transformer winding-loss vs. parasitic-capacitance
  tradeoffs (L02-019, L02-020) and HF transformer insulation design for MV-to-LVDC conversion
  (L02-001) are still open optimization problems limiting power density gains from higher switching
  frequency.
- **Extreme point-of-load delivery.** Feeding GPU/CPU/FPGA dies at sub-1V and thousands of amps
  from a 48V (or 800V-derived) bus is an unresolved power-density/loss problem occupying multiple
  concurrent APEC/ECCE research groups (L02-022, L02-023, L02-024) -- current designs still rely on
  multiple conversion stages that NVIDIA's own roadmap is trying to eliminate (L02-043).
- **Gate driver robustness under WBG switching stress.** Negative-voltage overshoot and mid/high
  power driving-circuit design remain reliability risks specific to SiC/GaN gate drives (L02-011,
  L02-012).
- **Grounding, hot-swap, and inrush/oscillation control at the 800V rack inlet.** Chinese trade
  coverage of Huawei's HVDC engineering work flags DC protection, grounding, hot-plug, and
  inlet-node voltage oscillation as unresolved system-integration pain points at 800V (L02-054) --
  distinct from, and less studied than, the device-level literature above.

## Named buyers and spending signals

- **NVIDIA** is the architecture-setting buyer: its 800VDC specification names Analog Devices,
  Infineon, Texas Instruments, STMicroelectronics, Eaton, Schneider Electric, and Vertiv as
  ecosystem partners (L02-043, fetched) and lists Navitas (L02-045, L02-046) and Innoscision
  (L02-050) among chip-level 800V suppliers.
- **Google, Meta, Microsoft** co-author the OCP Mount Diablo / Power Architecture Evolution
  whitepaper defining 400VDC-now / 800VDC-next rack power targets for their own datacenters
  (L02-044).
- **Navitas Semiconductor** disclosed the NVIDIA collaboration in an SEC Form 8-K (L02-045, a
  company filing -- audited-adjacent regulatory disclosure) and showcased a quantified 800V-to-6V
  power delivery board (97.5% peak efficiency, 2100 W/in^3) at NVIDIA's May 2026 Partner Ceremony in
  Taipei (L02-046, fetched).
- **Wolfspeed** reports ~30% sequential AI-datacenter revenue growth (Q2->Q3 FY2026) and is
  "actively collaborating with AI ecosystem partners on the transition from 400-volt to 800-volt
  architectures," though management is explicit that "it will take time for them to scale" and
  discloses no named customers (L02-047, fetched) -- an important caveat against overstating
  currently-booked revenue.
- **Alibaba**, with Delta and Zhongheng Electric, deployed the "Panama Power Supply" HVDC system in
  China's datacenters as early as 2019 (L02-048), and Shenzhen Autrans (奥特迅) is separately reported
  as a power-product supplier to Alibaba datacenters (L02-049) -- but as of ~2021, HVDC penetration
  in China datacenters was only ~12% versus 78% for UPS (cited within L02-048's source ecosystem),
  showing large unconverted incumbent base.
- **Singapore's EDB/IMDA** ran a >=200MW Data Centre Call-for-Application (DC-CFA2, closed 31 March
  2026) requiring "best-in-class" energy/IT efficiency and >=50% green power -- a dated,
  requirements-bearing government procurement trigger for efficient power electronics in Southeast
  Asia (L02-053).
- **ARPA-E** (U.S. DOE) has funded MV SST development directly, including a named award to Georgia
  Tech Research Corporation for a compact SiC-based modular MV SST under the CIRCUITS program
  (L02-035, official project award) plus the newer DC-GRIDS program ($35M / 12 projects, 2026)
  targeting HVDC converter technology for grid modernization (L02-034).

## Incumbent map (companies, products, price signals)

| Company | Geography | Product / signal | Evidence |
|---|---|---|---|
| Delta Electronics | Taiwan | 800VDC In-Row Power rack, 2.4MW/3MW liquid-cooling CDUs; "Panama Power Supply" HVDC (with Alibaba) | L02-037 (fetched), L02-048 |
| Navitas Semiconductor | US | GaNFast (650V/11mOhm) + GeneSiC (2300V/3300V) 800V-to-6V PDB, 97.5% eff., 2100 W/in^3 | L02-038, L02-046 (fetched) |
| Wolfspeed | US | TOL D portfolio "purpose-built for AI direct power"; first commercial 10kV SiC MOSFET | L02-047 (fetched) |
| Eaton, Schneider Electric, Vertiv | US/France | Named 800VDC power-system ecosystem partners in NVIDIA's own architecture spec | L02-039, L02-040, L02-043 |
| ROHM | Japan | 750V SiC MOSFET SCT4013DLL adopted in AI-server BBUs, Tj max 175C, works across +/-400V and 800VDC | L02-051 (fetched) |
| Microchip | US (reported via Korea) | 3.3kV HV-D3 mSiC power module for AI-datacenter SST, ~halves device count vs. ~1.2kV parts | L02-052 (fetched) |
| Innoscience (英诺赛科) | China | Only mainland Chinese chip company on NVIDIA's 800V supplier list; full-chain GaN, 98.5% claimed HF efficiency; per follow-on coverage still in testing, no confirmed orders | L02-050 |
| Shenzhen Autrans (奥特迅) | China | Reported power-product supplier to Alibaba datacenters | L02-049 |
| Infineon, Analog Devices, Texas Instruments, STMicroelectronics | US/EU | Named silicon providers in NVIDIA's 800VDC ecosystem | L02-043 |

Price signals are thin in what was fetched this session: no vendor list price for SiC/GaN power
modules or gate-driver ICs was captured with a locator (searches returned datasheets but no
transactable price -- see Assumptions/uncertainty note below). This is a gap for the verifier/
deep-dive stage to close with distributor pricing (Digi-Key/Mouser) or vendor investor materials.

## 2026-2031 triggers

- **2026 (now):** OCP updated Power Architecture Evolution whitepaper due later in 2026 (L02-044);
  Singapore DC-CFA2 window closed March 2026 (L02-053); ARPA-E DC-GRIDS awards issued (L02-034);
  Wolfspeed reporting sequential AI-datacenter growth quarter to quarter (L02-047).
  COMPUTEX 2026 (Taipei, late May) was a visible 800VDC ecosystem showcase (L02-046).
- **2027:** NVIDIA Kyber rack-scale systems and Rubin Ultra GPUs targeted for full-scale 800VDC
  production, 600kW-1MW per rack (L02-043, L02-044).
- **Through 2031 (inference, not sourced to a dated commitment):** if the 800VDC transition
  proceeds as specified, expect a multi-year replacement cycle for PSUs, busbars, and gate-driver
  ICs across every hyperscaler build-out; MV SST commercialization for grid and EV-XFC remains
  gated by IEC standards-compliance work (L02-036) and is a slower, less-dated trigger than the
  datacenter rack transition.

## US vs Asia differences

- **Supply-chain participation:** NVIDIA's 800V ecosystem list is dominated by US/Japan/Taiwan/
  Europe silicon and power-system vendors (Analog Devices, Infineon, TI, STMicroelectronics, Eaton,
  Schneider Electric, Vertiv -- L02-043) plus ROHM (Japan, L02-051), Delta (Taiwan, L02-037), and
  Microchip (US, reported via Korean press, L02-052). Innoscience is explicitly the *only* mainland
  Chinese chip company on that list (L02-050), and Korea's own compound-power-semiconductor global
  market share is reported at only ~2% versus a combined ~95% for EU/US/Japan (L02-042) -- Korea is
  a buyer/system-integrator (kt cloud, Samsung/SK-adjacent coverage found in search but not logged
  as a record this session) more than a device supplier today.
- **Deployment/adoption gap:** China's own HVDC data-center adoption reached only ~12% penetration
  versus 78% for UPS as of ~2021 (per L02-048's cited context), even though Chinese vendors (Delta
  China, Autrans) were early movers with Alibaba starting in 2019 -- suggesting Chinese demand
  signals are real but adoption has lagged the marketing narrative.
- **Government posture:** US policy response is R&D-program-centric (ARPA-E CIRCUITS/DC-GRIDS,
  DOE AMMTO strategic framework -- L02-032, L02-033, L02-034, L02-035) and national-lab-centric
  (Sandia -- L02-031). Singapore's response is procurement/permitting-centric (DC-CFA2 efficiency
  and green-power conditions on new data-center capacity -- L02-053). No Chinese-government-level
  procurement/regulatory record was captured this session (a gap -- Chinese coverage found was
  vendor/trade-press only, L02-048/L02-049/L02-050/L02-054).
- **Language/access asymmetry:** Chinese, Japanese, and Korean trade press (L02-048 through
  L02-052, L02-054) disclose adoption and supplier detail (e.g., Innoscience's "testing stage, no
  confirmed orders," Microchip's "customer undisclosed") more candidly about deal *status* than the
  polished English-language vendor/OEM press releases (L02-037, L02-038, L02-046), which tend to
  announce partnerships without revenue confirmation.

## Unresolved contradictions

1. NVIDIA/OCP marketing frames 800VDC as a near-consensus 2026-2027 industry standard (L02-043,
   L02-044), while Wolfspeed -- a direct SiC supplier into this transition -- describes AI
   datacenter revenue as still a "moderate portion" of its business needing "time to scale"
   (L02-047). The demand signal is real but its near-term revenue materiality is contested even by
   a named participant.
2. Innoscience is publicly named on NVIDIA's 800V supplier list (a strong design-in signal,
   L02-050), yet the same Chinese coverage states the relationship is "still in testing, no
   substantive orders yet" -- illustrating that "supplier list inclusion" and "booked demand" are
   not the same evidence tier and should not be conflated in later scoring.
3. Alibaba/Delta HVDC deployment dates to 2019 (L02-048), but China HVDC penetration was reportedly
   still only ~12% by ~2021 versus 78% UPS -- a 2+ year gap between a flagship deployment and
   market-wide adoption that current 2026 "AI power revolution" narratives (L02-054) do not
   reconcile.
4. IEC 60076-series standards remain written for magnetic-core transformers and are described as a
   compliance bottleneck for SST (L02-036), yet ARPA-E has been funding "first commercially viable"
   MV SST projects since at least the CIRCUITS program era (L02-033, L02-035) -- over a decade of
   government-funded R&D has not resolved the standards-compliance gap blocking commercial MV SST
   deployment.

## Uncertainty and session limitations (honesty note)

Most academic records in the ledger (L02-001 through L02-029) were located via WebSearch synthesis
only; publisher pages were not directly fetched this session (IEEE Xplore blocked automated
fetches during this session), so DOIs, exact author lists, and peer-review status are marked
`unverified` pending the source-verifier. Several DOIs (e.g., L02-012, L02-027, L02-028) were
inferred from publisher URL/numbering conventions rather than confirmed via a direct doi.org
resolve, and are flagged in each record's `notes` field. Two government-document fetch attempts
(L02-032, L02-035) returned unusable/garbled content; those records rely on search-snippet
summaries only. No vendor list-price data was captured this session despite searching -- this is a
gap for the next research pass.

## Opportunity-shaped pain statements

Presented as pain + who pays + evidence -- not startup pitches.

1. **Pain:** GPU-rack power conversion still requires multiple AC/DC and DC/DC stages between grid
   and die, each adding loss and failure surface. **Who pays:** hyperscalers (Google, Meta,
   Microsoft, and NVIDIA's own reference design push to eliminate stages) bear the TCO and
   reliability cost. **Evidence:** L02-043 (fetched), L02-044 (fetched).
2. **Pain:** Dynamic Ron / trapping in GaN HEMTs degrades efficiency and complicates lifetime
   prediction under the high switching frequencies 800V racks require. **Who pays:** power-module
   vendors and their hyperscaler customers absorb derating margin and warranty risk. **Evidence:**
   L02-006, L02-013, L02-014, L02-015, L02-016.
3. **Pain:** DC-link capacitors remain a leading converter failure mechanism, and higher power
   density compresses thermal margin for capacitor lifetime. **Who pays:** PSU/rack-power vendors
   (Delta, Eaton, Vertiv) and ultimately the datacenter operator via failure/replacement cost.
   **Evidence:** L02-010.
4. **Pain:** Solid-state transformers cannot commercialize cleanly because they must still pass
   IEC 60076 test regimes designed for magnetic-core transformers. **Who pays:** SST developers
   (ARPA-E-funded teams, Georgia Tech) and utilities/EV-charging site hosts who cannot yet deploy
   at scale. **Evidence:** L02-036, L02-035, L02-030.
5. **Pain:** Point-of-load conversion from 48V (or 800V-derived) buses to sub-1V GPU/CPU dies at
   1500-2000A is still an open power-density problem, with academic groups (UC Berkeley) still
   publishing new bus-converter topologies as of 2024-2025. **Who pays:** GPU/AI-accelerator makers
   and the board/rack integrators who must fit conversion into shrinking rack volume. **Evidence:**
   L02-022, L02-023, L02-024.
6. **Pain:** Negative-gate-voltage overshoot and driving-circuit design for WBG devices remains a
   reliability risk specific to SiC/GaN, distinct from silicon gate-drive practice. **Who pays:**
   gate-driver IC vendors and power-module integrators who must re-qualify designs per device
   generation. **Evidence:** L02-011, L02-012.
7. **Pain:** 800V rack-inlet grounding, hot-swap, and inrush/oscillation behavior is an unresolved
   systems-integration problem separate from (and less studied than) device-level WBG reliability.
   **Who pays:** rack/system integrators (Huawei and peers) engineering around it ad hoc today.
   **Evidence:** L02-054.
8. **Pain:** China's own HVDC/800V supply base is thin -- Innoscience is the sole named mainland
   chip supplier on NVIDIA's list, and the relationship is still in testing with no confirmed
   orders -- while broader adoption of HVDC in China datacenters has historically lagged flagship
   deployments by years. **Who pays:** Chinese hyperscalers and domestic power-electronics vendors
   racing to close a supply gap under geopolitical and export-control uncertainty (contextual, not
   separately sourced this session). **Evidence:** L02-050, L02-048.
9. **Pain:** Korea's compound-power-semiconductor global market share is reported at only ~2%
   despite strong domestic demand from memory/foundry/datacenter buyers. **Who pays:** Korean
   system integrators and hyperscale/cloud buyers (e.g., kt cloud, referenced in search but not
   separately logged) who must import SiC/GaN devices rather than source domestically. **Evidence:**
   L02-042.
10. **Pain:** High-frequency planar transformers face an unresolved winding-loss vs.
    parasitic-capacitance design tradeoff that limits how far switching frequency can rise without
    a new efficiency penalty. **Who pays:** magnetics/module vendors and converter OEMs redesigning
    for each new frequency/power target. **Evidence:** L02-019, L02-020, L02-001.
11. **Pain:** Government R&D funding for MV SST has continued for over a decade (ARPA-E CIRCUITS
    era through DC-GRIDS in 2026) without producing a standards-compliant, commercially deployed MV
    SST product. **Who pays:** DOE/ARPA-E as funder, and downstream utilities/EV-charging
    operators who still lack a qualified MV SST to buy. **Evidence:** L02-033, L02-034, L02-035,
    L02-036.
12. **Pain:** Vendor and OEM announcements (Navitas, Innoscience, ROHM, Microchip) consistently
    disclose product specs and partnership existence but withhold customer names and order volumes,
    making it hard for outside buyers/investors to distinguish genuine booked demand from
    design-in marketing. **Who pays:** anyone trying to underwrite investment or supply decisions
    against this market currently pays an information-asymmetry cost. **Evidence:** L02-046,
    L02-050, L02-051, L02-052, L02-047.

## T1 top-up addendum (2026-07-12)

Fifteen new T1-only records (L02-101 through L02-115, in
`10_SOURCE_ATLAS/L02_t1topup_raw_sources.json`) were added to raise this lane's T1 share, targeting
sub-niches the original 54-record ledger under-covered:

1. **EV traction-inverter power-module packaging** (double-side-cooled SiC MOSFET modules with
   sintered-silver interposers, 100 kW/L targets) via a Virginia Tech CPES paper (L02-101) and an
   ORNL-authored segmented-inverter proceedings paper (L02-102) -- the prior ledger had SST and
   device-reliability records but nothing on traction-inverter packaging specifically.
2. **Multiphase VRM / high-density DC-DC magnetics** via two Virginia Tech CPES coupled-inductor
   papers (L02-103, L02-104) -- a companion sub-niche to the existing planar-transformer records,
   focused on VRM transient response vs. ripple tradeoffs rather than winding loss.
3. **Datacenter AC-DC front-end (PFC stage)** via a Taiwan-authored GaN totem-pole PFC paper
   (L02-105) -- the prior ledger covered 800VDC racks and 48V-to-<1V point-of-load but not the
   upstream PFC/rectifier stage.
4. **EV drivetrain electronics beyond fast-charging SST**: a GaN three-level traction-inverter
   design paper (L02-106) and a bidirectional GaN CLLC on-board-charger paper (L02-109, Oxford) --
   traction and OBC power stages the prior ledger did not reach.
5. **Grid-scale (not EV-charging) SST**: an MVDC-interconnection multiport SST paper from a
   China/Denmark author group (L02-107), distinct from the prior ledger's EV-XFC-oriented SST
   records.
6. **WBG packaging/die-attach reliability**: an Osaka-University-authored SiC power-module
   Ag-paste sinter-joining reliability paper (L02-108) -- complements, but does not duplicate, the
   prior ledger's capacitor-reliability and gate-driver records.
7. **400V-to-48V datacenter bus stage**: a GaN modular LLC/planar-transformer paper (L02-110)
   bridging the prior ledger's planar-magnetics and 48V-to-<1V records.
8. **Government (non-ARPA-E) grid-modernization funding**: DOE Office of Electricity's FITT
   transformer program and SiC Packaging Prize (L02-111, fetched) -- a different DOE office/program
   line than the ARPA-E CIRCUITS/DC-GRIDS records already logged.
9. **General converter-safety standard**: IEC 62477-1:2022 (L02-112, fetched), the horizontal
   safety standard for power-electronic converter systems broadly, distinct from the prior ledger's
   transformer-specific IEC 60076-24.
10. **High-density-DC-DC company filing**: Vicor Corporation's FY2025 10-K (L02-113) -- a
    module-level high-density-power specialist not previously represented (prior filings were
    WBG-device makers Navitas/Wolfspeed).
11. **Real procurement/demand evidence for grid-scale and defense power conversion**: a SAM.gov
    aircraft ground-power-converter solicitation (L02-114) and a fetched GE Vernova press release
    reporting TenneT's BalWin5 2.2GW HVDC converter-station contract award (L02-115) -- the first
    ledger record of an actual utility capital-procurement action for HVDC conversion equipment,
    versus only R&D-program and academic MVDC-SST coverage previously.

All 15 are `tier: T1`, `accepted: false` (pending verifier pass), and `fetched: true` with a real
locator; two (L02-113 Vicor 10-K, L02-115 TenneT/GE Vernova) note honestly where a direct
SEC.gov/TenneT.eu fetch was blocked (HTTP 403) and a secondary fetch was used instead to confirm the
same underlying facts. No canonical-key or title collisions were found against the existing 54
L02 raw/verified records.

## P2A origin-audit repair (2026-07-13)

- removed IDs: L02-003, L02-008
- removed/trimmed claims: none deleted outright -- both citations were co-supported by other
  eligible IDs, so only the excluded ID was trimmed from each citation list (MV-SST claim in
  Frontier state para 2, still supported by L02-001/002/017/021/029/030; Ga2O3 Baliga-FOM claim
  in Frontier state para 2, still supported by L02-025/027).
