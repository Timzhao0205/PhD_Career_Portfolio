# L03 — Superconducting systems beyond sensing: magnets, machines, current leads, cryogenics

Lane scout brief. No startup ideas are proposed here; this is evidence collection only. All
citations refer to record IDs in `L03_raw_sources.json`. Uncertainty is flagged explicitly where
the underlying evidence is a single source, a vendor claim, or a consultancy estimate.

## Frontier state

REBCO (2G HTS coated conductor) magnet technology has crossed from laboratory demonstration into
first commercial deployment inside a five-year window. MIT/Commonwealth Fusion Systems validated
a 20 T REBCO toroidal-field model coil, and CFS has since installed the first of 18 SPARC magnets
using its own Devens, Massachusetts manufacturing line (L03-001, L03-003, L03-018 background;
CFS status via L03-035). Tokamak Energy is building ST80-HTS at UKAEA Culham and has spun out a
dedicated magnet business, TE Magnetics (L03-033, L03-044). China's ASIPP set a new steady-state
all-superconducting magnet world record of 35.1 T in September 2025 by nesting an HTS insert
inside LTS coils (L03-029, L03-037), and separately leads CFETR toroidal-field magnet engineering
(14.5 T design target vs ITER's 11.8 T) (L03-024). Japan's JT-60SA — the world's largest
superconducting tokamak — began integrated commissioning of its magnet system in February 2026
under a Japan-EU Broader Approach agreement (L03-025, L03-026, L03-036). On the grid side, HTS
cable and fault-current-limiter (SFCL) technology has moved from pilot to "fully commercial"
status in at least one case: State Grid Shanghai's 35 kV, 1.2 km, 133 MVA cable has operated
commercially since December 2021 (L03-012, L03-041, L03-052). Rotating-machine HTS (wind
generators, ship-propulsion motors) remains earlier-stage: the EU EcoSwing 3.6 MW wind generator
reached TRL 6-7 in field tests (L03-015), and the US Navy's 36.5 MW AMSC/Northrop Grumman motor
program from the 2000s has not scaled beyond prototype/demonstration status even though the
underlying HTS degaussing product line (a lower-power, simpler application) did reach volume Navy
deployment (L03-045, L03-046).

## Bottlenecks

- **Quench detection/protection remains unsolved at scale for HTS.** Unlike LTS magnets, HTS coils
  have very high minimum quench energy, making conventional detection (voltage taps, quench
  heaters, CLIQ) unreliable; no-insulation (NI) winding is a partial workaround that trades quench
  tolerance for worse ramp-rate and stored-energy control (search-index corroboration behind
  L03-004 through L03-008; L03-018 mechanical-stress review).
- **REBCO tape manufacturing capacity and uniformity.** Fujikura, Furukawa/SuperPower, Shanghai
  Superconductor, and SuNAM together represent well under 10 vendors capable of PLD/MOD tape
  production at scale (>3,000 km/year 12mm-equivalent across top-tier PLD producers per search
  aggregation behind L03-019); a single large tokamak or magnet-heavy customer can absorb a
  meaningful share of global annual output (L03-003's "largest-volume order the HTS industry has
  seen to date" claim).
- **Mechanical/strain degradation at high field.** REBCO critical current degrades under strain,
  delamination, and screening-current-induced stress at the multi-tesla level relevant to fusion
  and ultra-high-field magnets (L03-018, L03-020, L03-021).
- **No standardized critical-current test method for finished cables**, which the IEC/TC90
  international round-robin test was explicitly organized to address — the search evidence behind
  L03-053 states the absence of a widely accepted Ic measurement standard "impeding the
  industrialization of superconducting cables."
- **Cryogenic plant/cryocooler scale-up.** Fusion and grid HTS systems need kW-class 4-20K cooling
  (JT-60SA's helium plant is ~9.5 kW-equivalent at 4.5K per background literature behind
  L03-025/L03-026), which is a different regime from the mW-to-W scientific-instrument cryocoolers
  that dominate current catalog products (L03-050 PT205: 10 mW at 2.5K).
- **Naval/rotating-machine HTS has stalled commercially** relative to cable/FCL applications: the
  2007-era 36.5 MW Navy motor program (L03-045) has no confirmed public successor of similar power
  class in the current record set, while AMSC's HTS product roadmap emphasizes the lower-power
  degaussing SPS line instead (L03-046).

## Named buyers and spending signals

- **ITER Organization / US ITER / Oak Ridge National Laboratory** — completed final central
  solenoid deliveries (world's most powerful pulsed superconducting magnet) in April 2026
  (L03-030); China (via Western Superconducting Technologies, Xi'an) supplied ~65% of NbTi and
  7.5% of Nb3Sn strand under a decade-long procurement arrangement completed 2017 (L03-031).
- **US Department of Energy** — Milestone-Based Fusion Development Program ($415M authorized
  through FY2027, $46M initial obligation) named Commonwealth Fusion Systems and Tokamak Energy
  among 8 awardees in May 2023; awardees raised >$350M in new private capital against that $46M
  (L03-032). DOE separately funded ~$51.8M across five cost-shared HTS grid-modernization projects
  circa 2007, including SuperPower Inc. (L03-038, L03-039 — this second figure corroborated only
  via the ORNL press release, not independently fetched). ARPA-E awarded $4.2M (of $5.25M total)
  to Brookhaven National Laboratory, ABB, SuperPower, and University of Houston for grid-scale SMES
  in 2010 (L03-040).
- **Commonwealth Fusion Systems** — selling HTS magnets as near-term revenue: "largest deal of
  this kind to date" with Realta Fusion, plus a prior sale to the University of Wisconsin WHAM
  experiment and a technology license to Type One Fusion (L03-035).
- **Tokamak Energy / TE Magnetics** — $125M raised November 2024 (Furukawa Electric among new
  investors), $335M total to date, explicitly to commercialize HTS magnet technology beyond fusion
  into "science, mobility, renewable energy and security" (L03-033); separately signed a named
  supply agreement with Furukawa Electric/SuperPower for "several hundred kilometers" of HTS wire
  for ST80-HTS (L03-044).
- **RTE (French grid operator) / ADEME / France 2030** — EUR7.3M grant to the Nexans-led
  SupraMarine consortium to demonstrate an HTS HVAC offshore-wind export cable, testing planned by
  2028 (L03-034).
- **State Grid China (Shanghai, Liaoning)** — commissioned the world's first "fully commercial"
  kilometer-class 35kV HTS cable (Dec 2021) (L03-041) and multiple SFCL prototypes at 10kV/66kV
  substations (L03-011, L03-013).
- **KEPCO (Korea)** — operating a 23kV superconducting cable pilot and has signed an MOU with LS
  Cable & System and LS Electric (July 2025) to build a data-center-oriented superconducting power
  grid explicitly to meet AI-driven power demand growth (L03-042, L03-043).
- **U.S. Navy / Office of Naval Research** — historical $8M (5MW) and later 36.5MW HTS
  ship-propulsion motor contracts with AMSC/Northrop Grumman (L03-045); ongoing HTS degaussing
  Ship Protection System deliveries to San Antonio-class amphibious ships (USS Fort Lauderdale
  2022, USS Richard M. McCool Jr. 2025) per AMSC's own 10-K (L03-046).

## Incumbent map (companies, products, price signals)

| Company | Country | Product | Signal |
|---|---|---|---|
| Commonwealth Fusion Systems | US | REBCO tape + SPARC magnets, magnets-as-product | Vertically integrated tape/magnet factory (Devens, MA); selling magnets externally (L03-035) |
| Tokamak Energy / TE Magnetics | GB | HTS magnets (fusion + non-fusion) | $335M raised; supply deal with Furukawa for wire (L03-033, L03-044) |
| Fujikura, Furukawa/SuperPower | JP | REBCO tape | Named as 2 of "well under 15" global HTS wire vendors; DOE/ORNL licensing history (L03-038); Furukawa now a Tokamak Energy investor and supplier |
| SuNAM | KR | RCE-DR 2G HTS wire, HTS magnets | ~400 km/yr capacity claim (search-index only, not independently fetched this session) |
| Shanghai Superconductor / Shanghai Int'l Superconducting Tech | CN | PLD/MOD 2G tape, HTS cable systems | Built and operates the Shanghai State Grid cable (L03-041, L03-052) |
| Western Superconducting Technologies (WST) | CN | NbTi/Nb3Sn LTS strand | Sole Chinese ITER strand supplier, ~65%/7.5% of ITER NbTi/Nb3Sn volumes (L03-031) |
| American Superconductor (AMSC) | US | HTS wire, SFCL, ship degaussing (SPS), grid cable/FCL systems | >$15B addressable market claimed in 10-K; active Navy SPS deliveries 2022/2025 (L03-046) |
| LS Cable & System / LS Electric | KR | HTS cable, SFCL, power equipment | Named 2025 KEPCO data-center superconducting grid MOU partner (L03-043) |
| Nexans | FR | HTS HVAC cable (SupraMarine) | EUR7.3M government-backed demonstrator with RTE (L03-034) |
| Sumitomo Heavy Industries, Cryomech/Bluefors, Northrop Grumman, Thales, Sunpower/AMETEK | JP/US/FR | Cryocoolers | PT205 spec sheet: 10 mW@2.5K for 1.1kW input (L03-050, vendor claim) |
| Siemens Healthineers, GE HealthCare, ASG Superconductors | DE/US/IT | Helium-free MRI magnets | Vendor/trade-press claims of <1L helium systems (context only, not independently fetched this session) |

Price signals are thin in this record set: no independently fetched superconducting-cable or
magnet unit price was found (vendor pricing is generally quoted-on-request in this industry).

## 2026–2031 triggers

- **2026**: CFS plans to complete all 18 SPARC magnets and target first plasma; ITER final central
  solenoid module installation (L03-030); JT-60SA plasma-heating experiments begin (L03-036).
- **2027**: End of current DOE Milestone-Based Fusion Development Program authorization window
  ($415M total, L03-032) — a natural re-appropriation/renewal decision point.
- **2028**: SupraMarine HTS offshore-wind cable demonstrator testing (L03-034) — a dated,
  grant-triggered milestone with a named grid operator (RTE).
- **2030-2031**: AI/data-center load growth is cited by KEPCO/LS Cable/LS Electric as
  a live, current-decade trigger for urban superconducting-grid deployment (L03-043), not a
  future-dated one.
- **Ongoing/undated but active**: CFETR construction-decision timeline in China remains publicly
  described only as "post-ITER" bridge to a demonstration reactor without a firm procurement
  start date in this record set (L03-024) — flagged as an open uncertainty, not asserted as a
  2026-2031 trigger.

## US vs Asia differences

- **Magnet fabrication ownership model differs.** US frontier players (CFS) are vertically
  integrating tape-to-magnet manufacturing in-house; Japan/Korea incumbents (Fujikura, Furukawa,
  SuNAM) remain merchant tape suppliers selling into both domestic and Western fusion customers
  (L03-003, L03-038, L03-044); China's WST is a merchant LTS-strand supplier to ITER but domestic
  REBCO tape capacity (Shanghai Superconductor, Shanghai Shangchuang) is being built specifically
  to reduce import dependence (L03-052).
- **Grid HTS commercialization is furthest along in Korea and China, not the US.** KEPCO achieved
  "world-first" commercial 23kV HTS cable in 2019 and is now the only identified buyer explicitly
  citing AI/data-center load as the demand driver for a new superconducting grid MOU (L03-042,
  L03-043); China's Shanghai cable is described as the world's first "fully commercial" kilometer-
  class HTS cable for megacities (L03-041). No equivalent US utility-scale commercial (non-pilot)
  HTS cable deployment appears in this record set — US grid-HTS activity found here is earlier-
  stage federal R&D funding (L03-038, L03-039, L03-040), not a utility capital commitment.
- **Fusion national-lab investment is more centralized in Asia.** Japan (QST/JT-60SA) and China
  (ASIPP/CFETR) run their programs as direct national-lab-led builds with bilateral/international
  cost-sharing (Japan-EU Broader Approach for JT-60SA, L03-036; China's 13 ITER procurement
  packages, cited in L03-022). The US public-private model (DOE Milestone Program, L03-032) instead
  funds multiple competing private companies rather than one national flagship device.

## Unresolved contradictions

- **Is grid-scale HTS cable "commercial" or still demonstration-subsidized?** Chinese and Korean
  sources describe their flagship cables as "fully commercial"/"world-first commercialization"
  (L03-041, L03-042), yet the same projects are State-Grid- or KEPCO-led single installations
  without confirmed evidence of repeat, third-party-financed orders in this record set. Whether
  this represents genuine unsubsidized commercial viability or state-directed demonstration
  procurement dressed as "commercial operation" is not resolved by the sources gathered here.
- **Navy rotating-machine HTS: dead end or dormant?** The 2007-era 36.5MW motor program (L03-045)
  has no confirmed successor in this record set, yet AMSC continues to describe an addressable
  market above $15B (L03-046) without specifying how much of that market is rotating machines
  versus grid/cable/FCL/degaussing. Whether ship-propulsion HTS motors are commercially abandoned
  or simply outside AMSC's current public disclosure is unresolved here.
- **DOE $51.8M grid-modernization figure** (L03-039) could only be corroborated indirectly via the
  ORNL press release (L03-038); the primary energy.gov URL returned HTTP 404 this session. This
  number should be treated as provisionally reliable (corroborated by a national-lab primary
  source) but not independently confirmed at the originating agency page.

## Opportunity-shaped pain statements

Pain statements only — no startup pitches, no product framing.

1. **HTS magnet builders lack a validated, fast quench-detection/protection method at multi-tesla,
   multi-megajoule scale.** Pain: fusion and high-field-magnet developers must currently choose
   between conservative no-insulation windings (worse ramp rate/control) or unproven fast-detection
   schemes. Who pays: fusion device builders (CFS, Tokamak Energy) and national labs (ITER, ASIPP,
   QST) funding magnet R&D. Evidence: L03-004 through L03-008, L03-018.
2. **No industry-standard method exists for measuring critical current (Ic) on finished
   superconducting cables**, forcing every buyer/vendor pair to negotiate bespoke acceptance
   testing. Who pays: cable manufacturers and grid buyers (State Grid, KEPCO) needing bankable
   acceptance criteria. Evidence: L03-053 (IEC/TC90 round-robin motivation).
3. **REBCO tape capacity is concentrated in under 10 vendors globally, and a single large fusion
   order can consume a meaningful share of annual output.** Who pays: any new magnet-heavy buyer
   (new fusion entrant, accelerator upgrade, MRI/NMR expansion) competing for allocation against
   incumbent buyers. Evidence: L03-003, L03-019.
4. **Grid operators (KEPCO, LS Cable/LS Electric) are explicitly citing AI/data-center load growth
   as a live driver for superconducting-grid investment but lack a repeatable, cost-validated
   deployment template beyond single pilot cables.** Who pays: utilities and data-center developers
   facing substation/right-of-way constraints in dense urban areas. Evidence: L03-042, L03-043.
5. **Offshore wind developers need HTS export cables to avoid ~EUR1B-per-2GW-project HVDC
   conversion costs for far-shore connections, but the enabling cryogenic (Turbo-Brayton) and cable
   technology is only at demonstrator scale with 2028 testing.** Who pays: offshore wind
   developers and grid operators (RTE) bearing interconnection capex. Evidence: L03-034.
6. **Cryogenic plant for large fusion/accelerator magnets (kW-class at 4.5K) is a different
   engineering problem than the mW/W-class cryocoolers dominating current commercial catalogs**,
   creating a capability gap for mid-scale (non-flagship) magnet projects that cannot justify a
   bespoke helium-refrigeration plant. Who pays: mid-scale national-lab and university magnet/
   accelerator programs. Evidence: L03-025/L03-026 (JT-60SA ~9.5kW-equivalent plant, per background
   literature), L03-050/L03-051 (catalog cryocooler scale).
7. **US Navy-class HTS rotating machines (ship propulsion) have not progressed publicly beyond a
   2007-era prototype despite HTS motors' size/weight advantages for DD(X)-class vessels.** Who
   pays: Navy shipbuilding programs seeking power-density gains without a credible current
   commercial-off-the-shelf HTS motor option at that power class. Evidence: L03-045, L03-046
   (contrast between historical motor program and current AMSC product emphasis on degaussing).
8. **China's fusion program (CFETR) has completed magnet engineering design but this record set
   contains no confirmed, dated construction-procurement start**, leaving global suppliers
   (including non-Chinese ones) without visibility into when/whether a CFETR magnet
   procurement wave will open. Who pays: any supplier planning capacity investment against
   CFETR as a demand signal. Evidence: L03-024 (design-only status as found).
9. **REBCO conductors show strain-, delamination-, and screening-current-induced critical-current
   degradation at the field/stress levels relevant to next-generation high-field magnets**, meaning
   magnet designers must over-engineer structural support, raising cost and schedule risk. Who
   pays: any high-field magnet program (fusion, NMR, accelerator) needing to certify
   long-term operational margins. Evidence: L03-018, L03-020, L03-021.
10. **AMSC's own 10-K discloses an addressable market above $15 billion annually but does not
    break out how much is attributable to SFCL, cable, motor, or degaussing product lines**,
    leaving buyers and competitors without a transparent, audited breakdown of where actual paid
    demand concentrates within AMSC's own portfolio. Who pays (information asymmetry cost):
    competitors and investors trying to size addressable sub-markets. Evidence: L03-046.

## Notes on evidence quality (honest uncertainty flags)

- Many peer-reviewed candidates (L03-001 through L03-028 excepting L03-018) were identified via
  search-index snippets rather than full-text fetch; DOIs are populated only where visibly
  confirmed (IOP articles embed DOI in URL structure; Nature/MDPI/Cell DOIs confirmed via search
  cross-listing). Where a DOI could not be confirmed without risk of invention, the field is left
  blank and the publisher URL is used as the canonical key instead, per SOURCE_STANDARDS.
- Two records (L03-048, L03-055) are Japanese-language academic/technical PDFs whose content could
  not be extracted as readable text this session (WebFetch returned raw PDF byte streams); they are
  retained with title/journal/volume metadata only and marked `fetched: false`.
- SEC EDGAR (sec.gov) blocked direct WebFetch access (HTTP 403) on two attempts; AMSC 10-K content
  was instead read via a StockTitan mirror of the same filing (L03-046), and the canonical key
  points to the EDGAR filer index rather than a confirmed accession-number URL.
- The DOE $51.8M grid-modernization figure (L03-039) could not be confirmed at its primary
  energy.gov URL (HTTP 404) and is corroborated only indirectly through the ORNL press release
  (L03-038).

## P2A origin-audit repair (2026-07-13)

- removed IDs: L03-047, L03-049, L03-054
- removed/trimmed claims:
  - Dropped the "Market-report-named leaders (L03-047, L03-049)" clause from the cryocooler-vendors incumbent-table row, keeping only the eligible PT205 vendor spec citation (L03-050).
  - Deleted the "Market-size figures (cryocooler..., superconducting wire...)" sentence in full from the incumbent-map price-signals paragraph — needs a re-sourced cryocooler/HTS-wire TAM figure from an eligible provider.
  - Deleted the "Consultancy market-size horizon for both cryocooler and superconducting-wire markets" clause from the 2030-2031 triggers bullet, keeping only the eligible KEPCO/LS Cable AI-load-growth trigger.
  - Deleted the "India remains conductor-import-dependent for legacy assets" bullet in full (Sec. "US vs Asia differences") — needs re-sourced India-conductor-supply-chain evidence from an eligible provider if retained (note: India is also excluded from geography analysis under the mission's binding scope).
  - Deleted the "REBCO tape supply: scarcity or over-capacity?" contradiction bullet in full (Sec. "Unresolved contradictions") — needs re-sourced evidence for the "adequate supply" side of this contradiction from an eligible provider.
  - Deleted pain-statement item "Vendor and vendor-adjacent HTS wire market-size claims are not independently triangulated" in full (Sec. "Opportunity-shaped pain statements").
  - Deleted pain-statement item "India's legacy superconducting-tokamak assets (SST-1)..." in full (Sec. "Opportunity-shaped pain statements").
  - Renumbered the remaining pain-statement items sequentially after deletions (former item 12 is now item 10).
