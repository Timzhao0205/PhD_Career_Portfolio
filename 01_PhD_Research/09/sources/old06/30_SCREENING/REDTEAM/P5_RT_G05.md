# P5 Red Team G05

Assigned ideas: `P3R2-D-01`, `P3R2-C-13`, `P3R2-C-04`, `P3R2-D-12`, and
`P3R2-A-21`. This is an independent adversarial review of the authoritative P4 records; it does
not modify P4. The probability below means the chance that the concept fails to become a viable
standalone venture by its stated 2033/2034 kill date, not merely the chance that its next bench
test fails. Requested route was Terra/high; the runtime model and effort are not exposed and are
therefore **unknown**.

## Executive verdicts

| Idea | P4 score | Red-team score | Kill probability | G1 | G7 | Verdict |
|---|---:|---:|---:|---|---|---|
| P3R2-D-01 | 69.6 | **62.8** | **45%** | pass_marginal | pass_marginal | **KEEP, partner-gated** |
| P3R2-C-13 | 63.2 | **52.6** | **68%** | pass_marginal | pass_marginal | **HOLD** |
| P3R2-C-04 | 61.8 | **47.4** | **78%** | **fail** | **fail** | **KILL as scoped** |
| P3R2-D-12 | 57.8 | **42.0** | **88%** | **fail** | **fail** | **KILL** |
| P3R2-A-21 | 51.0 | **39.6** | **84%** | pass | **fail** | **KILL** |

Counts: **KEEP 1 / HOLD 1 / KILL 3**. The main cross-cutting finding is that four ideas cite
spending on a host system as if it were demand for the proposed merchant subsystem. That is
acceptable only as an explicitly marginal bridge. It is fatal where the product-specific bridge
is absent and the launch-window thesis also depends on a rule or procurement wave that is not in
force after 2030.

## Decision-changing source refresh

- The U.S. EPA still described all 53 Clean Ports projects as being implemented in June 2026 and
  said implementation lasts three to four years. This protects A-21's *current infrastructure*
  demand finding, but it also confirms that much of the funded wave finishes around 2028-2029,
  before a 2030 company can sell. [EPA awards page](https://www.epa.gov/ports-initiative/clean-ports-program-awards).
- DOE's FY2027 request says it would enhance support for the Milestone-Based Fusion Development
  Program, while DOE's June 2026 roadmap targets pilot plants/commercial power in the mid-2030s
  and makes the schedule contingent on future appropriations and public-private partnerships.
  This supports a real D-01 window but not an assured procurement.
  [FY2027 request](https://www.energy.gov/documents/fy-2027-fusion-energy-sciences-budget-request);
  [2026 fusion roadmap](https://www.energy.gov/articles/energy-department-releases-finalized-fusion-science-and-technology-roadmap-accelerate).
- nLIGHT's own July 9, 2026 release confirms a $44M initial JLWS award, a ceiling up to $627M,
  possible production options, and demonstrations as early as 2028. It also calls nLIGHT
  vertically integrated from laser chip through system level, which is direct evidence against
  C-13's outsourcing premise. [nLIGHT release](https://investors.nlight.net/news-releases/news-details/2026/nLIGHT-Awarded-627-Million-Joint-Laser-Weapon-System-JLWS-Contract/default.aspx).
- The official 2021 Entity List rule confirms Wuhan Raycus was added for risk of unauthorized
  military end use; the rule applies a license requirement to all items subject to the EAR, a
  presumption of denial, and no license exceptions for the applicable group. Raycus cannot be a
  reachable base-case buyer for C-13. [Federal Register rule](https://public-inspection.federalregister.gov/2021-14656.pdf).
- EPA's AIM program limits specified **HFCs** in specified sectors; it is not a general PFAS ban.
  ECHA's universal PFAS restriction was still in committee review after the March-May 2026
  consultation, with a final SEAC opinion expected by end-2026 and a later Commission decision.
  The two are not interchangeable product deadlines.
  [EPA HFC scope](https://www.epa.gov/hfcs/technology-transitions-program);
  [ECHA PFAS status](https://poisoncentres.echa.europa.eu/en/web/guest/hot-topics/perfluoroalkyl-chemicals-pfas).
- China's GB 40879 revision remained a **standard plan**, not a published final revision; the
  SAMR record shows the drafting/review/approval/publication sequence and a 16-month project from
  April 30, 2025. It supports a broad liquid-cooling direction, not current EHD or two-phase
  procurement. [SAMR revision record](https://std.samr.gov.cn/gb/search/gbDetailedCNF?id=2E4DD4D8E2E84A4BE06397BE0A0AE354).

## P3R2-D-01 — merchant HTS quench detection and protection

### Strongest bear case

This is a safety-critical custom magnet-engineering program disguised as a merchant electronics
subsystem. DOE, CFS, Tokamak Energy, and US ITER are spending on fusion and magnets, but no buyer
has issued an RFP, tender, paid evaluation, or specification for an independent quench-protection
package. The closest possible customers have the strongest reasons and technical teams to keep
protection in house: protection is inseparable from winding architecture, conductor mechanics,
insulation, current sharing, dump voltage, and the machine safety case. A third party would carry
catastrophic-loss liability without controlling those inputs.

The proposed 1-2 T double-pancake campaign can validate a sensor on a small coil, but it cannot
establish kilometer-scale fiber survivability, multi-kA isolation, false-trigger behavior under
real fusion transients, or safe extraction from a 100 MJ magnet. The P4 wording correctly retreats
from "sub-millisecond extraction" to "sub-millisecond protection initiation"; full energy removal
is necessarily much slower. That distinction removes some of the apparent 10x claim. No-insulation
windings and in-house multi-modal sensing are not merely competitors; they can eliminate the
independent product category.

Commercially, the buyer count is tiny, procurement is programmatic, partner access is mandatory,
qualification cycles are multi-year, and field failures can destroy a unique magnet. Service and
applications-engineering burden will be high even if the electronics are compact. The $3-8M v1
range also understates the capital and insurance needed for representative high-field validation.

### Disconfirming evidence

- `L03-030`, `L03-032`, and `L03-035` prove magnet/fusion spending and external magnet
  transactions, not quench-subsystem procurement. The dossier explicitly found no
  protection-specific RFP.
- `L03-004` supports the physical difficulty of HTS detection. `L03-018` primarily supports REBCO
  mechanical stress and degradation; it does not by itself validate the proposed co-wound,
  kilometer-scale Rayleigh sensing product.
- The DOE program's continued progress remains contingent on appropriations and milestone
  negotiation. The refreshed FY2027 request is favorable, but a request is not an enacted award.
- `L03-035` and `L03-044` show that CFS/TE Magnetics are vertically capable magnet builders. Lack
  of a named merchant competitor is therefore not whitespace evidence.

### Steelman

The problem is real, technically important, unusually measurable at small scale, and frontier in
a way buyers can understand. DOE's current support and the mid-2030s pilot-plant roadmap create a
credible preparation-to-launch sequence. Merchant magnet sales (`L03-035`) show at least some
organizational willingness to transact across firm boundaries. A vendor that enters through one
magnet builder as a jointly qualified safety package could accumulate a valuable precursor-event
dataset and later expand into HTS cable and test-magnet monitoring. The concept is worth retaining
as a **partner-led qualification program**, not as an assumption of a catalog product.

### Gate adjudication

- **G1 pass_marginal:** two independent primary/official spending sources exist, but demand is for
  magnets/fusion programs, not this product. Flip to pass only with a paid evaluation or signed
  joint-development statement from a magnet builder.
- **G2 pass:** the core quench literature used is peer-reviewed; do not use duplicate rejected
  ledger versions of `L03-005` through `L03-008`.
- **G3 pass:** $250k and 6-18 months are bounded. It is decisive only for small-coil detection and
  trigger logic, not for production-magnet protection.
- **G4 pass_marginal:** CFS/TE in-house solutions and CLIQ/no-insulation approaches are named;
  difference is non-cosmetic, but buy-versus-build is unresolved.
- **G5 pass_marginal:** physics exists; scale, isolation, and system safety remain stacked risks.
- **G6 pass_marginal:** keep US-only. No China sale, license, or technical-data transfer belongs
  in the base case without current export counsel and counterparty screening.
- **G7 pass_marginal:** the FY2027 funding decision and DOE mid-2030s roadmap are real triggers;
  the procurement outcome is appropriation- and partner-dependent.

### Score adjustment

| Criterion | P4 raw | RT raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | **2** | funded host ecosystem, zero product-specific procurement |
| Technical elegance/controllability | 5 | **4** | small-coil controllability does not extend cleanly to full-magnet safety |
| 10x technical edge | 3 | **2** | warning-time advantage is plausible but unproven; extraction headline narrowed |

All other raw scores remain. Adjusted total: **62.8/100**.

### Cheapest decisive falsification

No honest whole-product test below $100k exists. A **$120k-$160k partner-facility kill test** is
the minimum credible first cut: instrument an existing REBCO pancake with co-wound Rayleigh fiber,
voltage taps, acoustic/RF channels, and an FPGA trigger; run at least 50 seeded disturbances and
20 controlled quenches across current-ramp and cryogenic transients. Kill if median warning is
under 100 ms, any thermal-runaway event is missed, false trips exceed 1%, fiber calibration drifts
over 5% after cycling, or the partner refuses a path to a representative multi-kA coil. A positive
result does not validate 100 MJ protection; it only earns the existing $250k campaign.

### Verdict

**KEEP, partner-gated (45% kill probability).** Do not advance to a deep dive without a named US
magnet-builder access path and an explicit liability/qualification model.

## P3R2-C-13 — precision GaN pump-driver and laser-power modules

### Strongest bear case

The large numbers belong to laser systems, not merchant driver modules. nLIGHT's own release says
it is vertically integrated from laser chip through system level. IPG, Coherent, Han's, and Raycus
also have in-house electronics and laser-control teams; these are not slow incumbents overlooking
a component but sophisticated OEMs for whom driver behavior, diode lifetime, safety, and TMI are
core intellectual property. Nanosecond edge speed is not a customer outcome, and the dossier has
no evidence that the proposed modulation increases output power, beam quality, uptime, or diode
life enough to justify redesign and requalification.

The dual-market story is structurally weak. Raycus, the best-documented named China buyer, is
Entity-Listed with presumption of denial for items subject to the EAR. A two-entity structure does
not make a US-origin design, firmware, component, or technical-data flow disappear. The remaining
China buyer hypothesis is Han's, which has neither been officially cleared for the contemplated
transaction nor shown willingness to outsource. Meanwhile a US defense customer will scrutinize
ownership, staff, data, firmware reuse, and supply-chain overlap, making the supposed cross-market
volume economy largely unavailable. Separate entities and clean-room engineering duplicate cost
rather than create leverage.

JLWS demonstrations begin as early as 2028. A company formed in 2030 risks arriving after the
driver architecture and suppliers are frozen. A&D qualification, ITAR/EAR controls, diode-lifetime
testing, EMI, functional safety, and OEM service integration make $5-12M v1 capital optimistic.

### Disconfirming evidence

- The official nLIGHT release proves $44M initial/$627M ceiling system demand but also states
  vertical integration. It does not disclose demand for a third-party driver.
- `L12-025` concerns LLC modulation shapes; `L12-026` is a 9 ps timing-resolution driver;
  `L12-027` is a >100 W pulsed driver. None demonstrates an eight-channel, 1 kA aggregate module
  improving TMI on a 1 kW industrial amplifier, much less a production design win.
- `L12-016` through `L12-018` establish TMI physics. They do not establish that pump-current
  modulation is the preferred or 10x mitigation versus fiber design, mode filtering, thermal
  management, or OEM control algorithms.
- `L12-033`, `L12-037`, and `L12-038` establish industry revenue and price pressure. Price pressure
  can encourage outsourcing, but it also compresses merchant-component margins and rewards
  already-amortized in-house designs.
- P4's new Raycus listing sources were secondary; the official Federal Register refresh confirms
  the restriction and makes the negative finding stronger.

### Steelman

The $180k experiment is bounded, the circuits and control loops fit a compact engineering team,
and official JLWS funding plus industrial laser volume create large, real host markets. A narrow
US-only commercial/defense-adjacent telemetry-and-driver module could work if a smaller OEM lacks
the NRE for a modern driver. Diode-health telemetry and a quantified laser-stability benefit are
more defensible than raw switching speed. The concept deserves a commercial willingness-to-buy
test before being folded into D-10.

### Gate adjudication

- **G1 pass_marginal:** system demand is strong and primary, but merchant-driver demand remains
  unproven. The already-frozen two-paid-evaluation gate is mandatory.
- **G2 pass:** cited academic mechanisms are peer-reviewed; do not overextend them to product
  performance they did not measure.
- **G3 pass:** $180k/6-18 months is bounded and can falsify the technical claim.
- **G4 pass_marginal:** in-house OEM teams are named; telemetry/TMI-aware control is non-cosmetic
  only if it produces a measured OEM-valued benefit.
- **G5 pass:** no new physics, but integration performance remains unproven.
- **G6 pass_marginal:** remove Raycus. A US defense line and any China commercial work require
  separate personnel, IP, BOM, firmware, data, ownership review, and counsel-approved counterparties;
  assume no cross-market volume economy until counsel proves otherwise.
- **G7 pass_marginal:** potential JLWS production options extend into the early 2030s, but the
  design-in window begins by 2028. Failure to secure paid evaluations by end-2028 is a kill/fold.

### Score adjustment

| Criterion | P4 raw | RT raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | **2** | host-system spending, no merchant-driver order |
| High-end niche quality | 3 | **2** | few reachable buyers; in-house design is core IP |
| Reachable validation budget | 4 | **3** | bench test fits, but v1 and segregated qualification exceed the preferred path |
| US-China dual-market leverage | 2 | **1** | Raycus blocked; no screened, committed China substitute; clean-room duplication |
| 2030 launch-window fit | 3 | **2** | architecture/design-ins may freeze before formation |

All other raw scores remain. Adjusted total: **52.6/100**.

### Cheapest decisive falsification

A genuinely decisive **commercial** test can be run for **$45k-$75k** before the full driver build:
prepare an interface-control document, credible BOM/EMI/safety plan, and diode-health/TMI data-room
mock-up; conduct structured make-versus-buy reviews with at least six US commercial/defense-adjacent
OEMs and six screened China commercial OEMs through counsel-approved channels; ask each to sign a
paid evaluation contract of at least $25k. Kill the standalone company if two paid evaluations
(one per market) are not signed by 2028, or if the US buyer requires controls incompatible with
the China entity. This falsifies willingness to buy, not physics, and should not be relabeled as
the technical first experiment. The existing $180k build remains necessary after the commercial
gate.

### Verdict

**HOLD (68% kill probability).** Preserve only until the two paid evaluations and a written export/
entity-separation plan exist. Otherwise fold the power stage into D-10 as already specified.

## P3R2-C-04 — PFAS-free pumped two-phase direct-to-chip loop

### Strongest bear case

The demand and timing thesis conflates three different facts: hyperscalers buy high-capacity CDUs;
some vendors deploy two-phase cooling; and several jurisdictions regulate some fluorinated
chemicals. None is a primary buyer specification for a **PFAS-free pumped two-phase loop**.
Google's Deschutes document is a 2 MW CDU specification and does not require two-phase or PFAS-free
operation. The named Accelsius deployment comes from a T2 newsletter, and its fluid's PFAS status
is explicitly undisclosed. China's PUE rules are technology-neutral and can be met by single-phase
water, facility design, or other efficiency measures.

Most importantly, the P4 dossier overstates the regulatory clock. EPA AIM rules address specified
HFCs in specified sectors, not all PFAS and not necessarily this direct-to-chip working-fluid
application. The EU F-gas regulation and the still-pending universal PFAS proposal are different
instruments. ECHA had not completed its opinion, and the Commission had not enacted a universal
restriction as of this refresh. EU evidence may inform fluid-supply risk, but it is not counted as
a target market or a guaranteed 2030 US/CN product deadline.

The competitive field is already well funded and strategically owned: ZutaCore reports $100M+
Series C and 75+ deployments (`L14-046`); Accelsius raised $65M; JetCool belongs to Flex; LiquidStack
belongs to Trane. Absence of a public "PFAS-free dataset" claim is not whitespace. Fluid vendors
and incumbents can co-qualify replacements, while a startup must solve fluid chemistry, materials,
micro-pumping, hermeticity, charge management, orientation, controls, warranty, and datacenter
qualification simultaneously. The core work sits outside the shallow founder profile and demands
heavy chemistry/thermal partners.

The $400k first campaign and $10-25M v1 are outside the mission's preferred capital path. A
1,000-hour run is only six weeks and is not a datacenter lifetime warranty. The proposed 2031 fluid
kill is too late for a 2030 launch: the central product input should be qualified before formation,
not one year afterward.

### Disconfirming evidence

- `L14-043` proves demanding CDU procurement, but even the ledger notes that exact technical
  figures were taken from secondary coverage because the source PDF was not text-extractable.
- `P3R2-C-04-S01` proves a funded two-phase competitor and named campus, not demand for C-04's
  architecture or chemistry.
- `L14-033` is explicitly an HFC phasedown; it does not establish a PFAS-free deadline. The ECHA
  universal PFAS process was still pending after consultation.
- `L14-035`, `L14-036`, `L14-039`, and `P3R2-C-04-S02` support China's broad PUE/liquid-cooling
  direction; none specifies pumped two-phase or PFAS-free fluid. SAMR still lists the GB 40879
  revision as a plan.
- `L14-009` demonstrates 206.5 W/cm2 on a microchannel cold plate. The proposed >500 W/cm2 edge
  with candidate non-PFAS fluids, stable at datacenter lifetime, remains unproven.
- `L14-053` is a Taiwan trade-press report of an ITRI result, not a US/CN merchant product or
  customer acceptance.

### Steelman

The physical architecture is testable, a negative-pressure loop has a real leak-safety advantage,
and fluid/loop qualification data could be valuable if regulators and 3M's exit leave a persistent
gap. AI heat density is a durable demand engine and both US and China have large cooling supply
chains. A fluid supplier plus ODM partner could turn the dataset into a moat. That steelman,
however, requires two partners that do not currently exist in the record and does not justify a
standalone selection now.

### Gate adjudication

- **G1 fail:** no primary buyer/procurement source requires or pays to evaluate a PFAS-free pumped
  two-phase loop. Broad CDU demand plus a competitor deployment is insufficient as scoped.
- **G2 pass:** boiling and cold-plate mechanisms use eligible peer-reviewed sources.
- **G3 pass_marginal:** technically bounded, but $400k exceeds the $250k ceiling and positive
  results would still leave long-life qualification open.
- **G4 pass:** competitors are named and negative-pressure/fluid-menu qualification is
  non-cosmetic; whitespace is unproven.
- **G5 pass_marginal:** no new physics, but viable fluid availability is an external stacked
  dependency, not yet a controlled input.
- **G6 pass:** export exposure is low; chemistry/regulation must be mapped by exact substance and
  use, not by the blanket label "PFAS."
- **G7 fail:** the US HFC schedule is not a PFAS-free two-phase procurement trigger; the universal
  PFAS restriction is not enacted; China rules are technology-neutral and the GB revision is not
  final. A named ODM 2030-2034 design-in is absent.

### Score adjustment

| Criterion | P4 raw | RT raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | **2** | broad cooling demand; no product-specific primary buyer |
| High-end niche quality | 3 | **2** | crowded, partner-heavy, long qualification |
| Reachable validation budget | 2 | **1** | $400k first campaign; $10-25M v1 |
| Technical elegance/controllability | 4 | **3** | fluid chemistry and lifetime sit outside the control loop |
| US-China dual-market leverage | 3 | **2** | China does not share the chemistry-specific willingness-to-pay thesis |
| 2030 launch-window fit | 4 | **2** | regulatory clocks overstated; 2031 input kill is post-launch |

All other raw scores remain. Adjusted total: **47.4/100**.

### Cheapest decisive falsification

A **$85k-$95k negative screen** is possible, but it is not a decisive positive validation and
must not be credited as the portfolio's <$100k decisive first experiment. Build one instrumented
100-250 W subatmospheric evaporator channel; test two specifically identified candidate fluids and
one water variant over pressure/orientation cycles; run 500 hours plus accelerated material-soak,
vacuum-decay, non-condensable-gas, and pump-cavitation tests. Kill if no candidate maintains stable
boiling without dryout across orientation, materials mass/volume change exceeds 1%, vacuum loss
exceeds the predefined leak budget, or thermal performance is less than 20% better than a
single-phase cold-plate control at equal auxiliary power. A pass only authorizes the $400k/2 kW
campaign.

### Verdict

**KILL as scoped (78% kill probability).** Reconsider only after a named fluid supplier warrants a
specific chemistry and a US or China ODM pays for an evaluation under a pre-launch qualification
schedule.

## P3R2-D-12 — EHD-pumped two-phase cold plates

### Strongest bear case

This is exactly the atlas's "lab-strong, industry-thin" failure signature. `L16-001` demonstrates
upstream EHD flow distribution in meso-scale evaporators; `L16-002` studies an EHD **gas** pump;
neither demonstrates an embedded pump in a high-vapor-quality AI cold plate. `L16-003` and
`L16-004` are reviews, with the latter explicitly finding limited industrial-scale deployment.
There is no EHD-specific buyer, paid evaluation, OEM co-development, procurement document, or
industrial reliability record.

The product stacks two existential risks: EHD must beat an optimized mechanical plate exactly
where conduction pumping weakens near high vapor quality/CHF, and a simultaneously dielectric,
non-PFAS, low-GWP fluid must exist and remain stable around electrodes. Electrode fouling, charge
injection, electrochemistry, EMI, dielectric breakdown, non-condensables, and 1,000-hour drift are
not secondary engineering. A "no moving parts" slogan does not imply no service when the electrodes
and fluid can age inside a sealed plate.

The incumbents have not ignored cooling innovation. Flex/JetCool, ZutaCore, Vertiv, Eaton/Boyd,
and Ecolab/CoolIT are capitalized, qualified channels with mechanical designs that already work.
The reported consolidation values are T3 working evidence and should not set market arithmetic,
but the official acquisitions in `L14-045`/`L14-051` independently establish strategic absorption.
An OEM can reproduce a patentable pump cell, acquire the team, or simply increase mechanical flow.
The claimed 10x edge is not demonstrated on pressure head, CHF, hotspot response, reliability,
plate cost, or customer TCO.

China is not a credible beachhead: the GB 40879 revision remains a standards project and no China
buyer has requested EHD. Generic PUE pressure cannot carry a product-specific score. The ECHA PFAS
process is pending, not an enacted 2030 trigger, and is not a target-market substitute.

### Disconfirming evidence

- The dossier itself found no named OEM/COOLERCHIPS co-development and zero EHD-specific demand.
- `L14-030` is an R&D award for efficient cooling broadly; it is not procurement of EHD plates.
- `L14-043` specifies a CDU, not in-plate EHD pumping.
- `L16-001` supports active flow distribution but not the product's 3-5 kW package, embedded
  electrodes, near-CHF performance, proposed fluids, or 1,000-hour reliability.
- `L16-002` is a gas pump and is weak support for two-phase liquid conduction pumping.
- `L14-035` remains a revision plan; `L14-036` explicitly contains no quantified liquid-cooling
  mandate.
- `P3R2-D-12-S01` and `S02` are T3 trade sources; they cannot carry a hard gate or price/TAM claim.

### Steelman

The idea is elegant and falsifiable. A no-local-moving-parts flow-balancing element would be useful
if it delivered a clear CHF/hotspot advantage, and the $180k experiment is in the preferred band.
Core electronics and feedback control are measurable. Because a negative result can be reached
cheaply, it is a reasonable university research project or option on future IP. It is not yet a
venture-selection candidate.

### Gate adjudication

- **G1 fail:** broad cooling demand does not satisfy current product-specific demand; the frozen
  named-OEM bridge is unmet.
- **G2 pass:** the cited EHD literature is peer-reviewed, with claim-scope cautions above.
- **G3 pass:** $180k and explicit parity-equals-kill thresholds are genuinely bounded.
- **G4 pass:** competitors and the non-cosmetic mechanism difference are named; lack of an EHD
  product reflects immaturity as much as whitespace.
- **G5 pass_marginal:** physics exists, but EHD superiority plus a compliant stable fluid are two
  stacked contingencies.
- **G6 pass:** no unusual export restriction; chemical/regulatory mapping remains mandatory.
- **G7 fail:** no named 2030-2034 EHD procurement/design-in trigger; China's revision is not final,
  ECHA's proposal is not enacted, and the 2028 OEM bridge is absent.

### Score adjustment

| Criterion | P4 raw | RT raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 2 | **1** | zero product-specific demand |
| High-end niche quality | 3 | **2** | accessible only through consolidated OEM channels |
| Competition whitespace | 3 | **2** | no product may mean inadequate performance, not whitespace |
| Technical elegance/controllability | 3 | **2** | fluid/electrode aging and near-CHF regime are weakly controlled |
| 10x technical edge | 3 | **2** | qualitative no-moving-parts claim; no measured customer edge |
| US-China dual-market leverage | 2 | **1** | no China buyer and unfinalized standard |
| 2030 launch-window fit | 3 | **1** | no product trigger; incumbents can close window before 2030 |

All other raw scores remain. Adjusted total: **42.0/100**.

### Cheapest decisive falsification

A genuinely kill-capable core-physics test can fit **$80k-$95k** if a university already supplies
the flow loop and diagnostics. Build a single EHD pump cell upstream of two parallel boiling
microchannels using two named candidate fluids; sweep vapor quality, heat flux, electrode field,
and orientation against an optimized mechanical-pump control at equal total pumping/drive power.
Run at least 250 hours after screening. Kill if pressure head or controllable flow split collapses
above 50% vapor quality, channel modulation is under 20%, CHF/hotspot response is not at least 20%
better than the control, electrode current or EMI violates the predefined electronics envelope,
or performance drifts over 10%. A pass still needs the full $180k integrated-plate/1,000-hour test.

### Verdict

**KILL (88% kill probability).** Retain only as a research option; do not use it to satisfy a final
portfolio cooling, China, or <$100k-product-validation quota.

## P3R2-A-21 — ruggedized multi-megawatt charging systems

### Strongest bear case

The demand is real, but the startup wedge is not. EPA is currently implementing nearly $3B of
Clean Ports projects, yet the awards buy existing zero-emission equipment and infrastructure over
the next three to four years. A company launched in 2030 will miss much of that funded procurement.
No source shows a post-2030 order for an independent 1.5-6 MW ruggedized merchant charger. The
rail case is ten Union Pacific FLXdrive locomotives from 2022 with no identified follow-on fleet
order; the mine cases show the opposite of merchant demand.

The most advanced buyers and OEMs vertically bundle the solution. Fortescue built its own 6 MW
charger. China's operating 100-truck Huaneng fleet uses XCMG, Huawei, State Grid, and Huaneng in a
domestic consortium. Wabtec and Caterpillar can bundle charging with vehicles and warranties.
ABB, Siemens, Kempower, utilities, EPCs, and storage integrators already possess most of the power
conversion and site-integration capability. IEC TS 63379 publication standardizes interfaces and
reduces risk, but it also lowers differentiation and invites established EVSE suppliers.

There is no 10x technical edge. The concept is a capital- and working-capital-intensive EPC/product
hybrid with utility interconnection, civil works, medium-voltage equipment, thermal management,
hazardous-site compliance, spares, remote monitoring, and 24/7 field service. The $1.2M test and
$8-20M v1 are outside the founder-scale mission; customer deposits do not eliminate warranty,
inventory, and performance-bond exposure. China has demand but no credible entrant access, so the
dual-standard option adds engineering burden without a beachhead.

### Disconfirming evidence

- Current EPA implementation protects G1 but its three-to-four-year schedule confirms pre-2030
  concentration. The page also notes active grants can change if recipients stop pursuing projects.
- `P3R2-A-21-S07`/`L10-032` prove only a ten-unit UP order; no scale order is in the record.
- `P3R2-A-21-S05` and `L10-029` prove the 6 MW envelope and simultaneously prove in-house build.
- `P3R2-A-21-S06` proves China demand and simultaneous vertical capture. It does not create a China
  beachhead.
- The $75M-$600M niche is an extrapolation from grant footprint and assumed $1.5M-$4M site price,
  not a buyer-derived bottom-up market.
- `L10-050`/IEC publication is a certification enabler, not a 2030-2034 order trigger.

### Steelman

Unlike the two thermal wildcards, this concept sells into active, named, funded infrastructure.
The physics is proven, EPA awards remain live, and harsh-duty fleet/site integration is genuinely
hard. A focused engineering company could win paid front-end design, controls, buffering, and
fleet-API work for a subset of ports or mines that do not receive a complete OEM bundle. It may be
a viable later-stage project-finance/EPC business with a well-capitalized partner. It is a poor fit
for this portfolio's frontier, 10x, and reachable-capital objectives.

### Gate adjudication

- **G1 pass:** active EPA projects are primary, named, and directly include charging/electrical
  infrastructure; UP adds independent buyer evidence.
- **G2 pass:** no load-bearing academic-peer-review defect found.
- **G3 pass_marginal:** the test is bounded but $1.2M, more than four times the preferred ceiling,
  and requires a test yard/interconnection.
- **G4 pass:** OEM bundles, EVSE majors, and in-house builds are named; rugged fleet integration is
  non-cosmetic but weakly defensible.
- **G5 pass:** no new physics or single forecast dependency.
- **G6 pass:** ordinary industrial compliance path; no export route is required. Keep China out of
  the base case.
- **G7 fail:** the primary grant wave mostly implements before launch, the standard is already
  published, and no named 2030-2034 port/rail/mine procurement or design-in trigger is documented.

### Score adjustment

| Criterion | P4 raw | RT raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 4 | **3** | real infrastructure demand, but thin merchant/post-2030 evidence |
| High-end niche quality | 3 | **2** | customer reachable; sale captured by OEM/EPC/in-house channels |
| Competition whitespace | 2 | **1** | established suppliers and vertical bundling; standard reduces moat |
| Technical elegance/controllability | 3 | **2** | site/interconnection/service complexity dominates |
| 2030 launch-window fit | 3 | **2** | grant deployment is concentrated before launch |
| Expansion economics | 3 | **2** | expansion adds project and working-capital burden, not software-like leverage |

All other raw scores remain. Adjusted total: **39.6/100**.

### Cheapest decisive falsification

A **$55k-$80k commercial kill test** is possible and should precede any power build. Complete
site-specific one-line, load profile, interconnection, duty-cycle, uptime/SLA, and total-installed-
cost studies for one port, one railroad, and one mine; require each counterparty to provide data
and pay at least $20k for front-end engineering or sign a funded pilot term sheet. Kill the merchant
system concept if none pays, if all require vehicle-OEM prime responsibility, if target gross margin
after EPC/field service is under 25%, or if no pilot can begin by 2029. This test is decisive for the
merchant-channel thesis, not technical validation, and does **not** convert the $1.2M first hardware
experiment into a <$100k experiment.

### Verdict

**KILL (84% kill probability).** The opportunity may suit ABB/Wabtec/Cat, an EPC, or a project-
finance vehicle; it does not satisfy this mission's capital, 10x, whitespace, or 2030-window bar.

## Portfolio handoff

- Advance `P3R2-D-01` only with a named US magnet partner; keep its China flag false.
- Keep `P3R2-C-13` out of the final 24 unless the two-paid-evaluation gate is satisfied with an
  officially screened China counterparty and written technology-control separation. Raycus is out.
- Do not count `P3R2-C-04` or `P3R2-D-12` toward China, product-specific demand, or sub-$100k
  decisive-validation quotas. Their low-cost tests are negative screens, not complete product
  validation.
- Do not count `P3R2-A-21` as a G7-passing 2030 opportunity without a named post-launch procurement
  path. Current EPA implementation is demand evidence, not a post-2030 startup order.
