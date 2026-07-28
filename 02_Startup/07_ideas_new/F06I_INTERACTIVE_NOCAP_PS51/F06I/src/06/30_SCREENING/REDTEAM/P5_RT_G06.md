# P5 adversarial red team — group G06

Scope: `P3R2-E-14`, `P3R2-A-05`, `P3R2-A-22`, `P3R2-F-02`, and
`P3R2-F-03`. This review attacks the proposed product and beachhead, not whether the underlying
field is important. A funded transmission line, accelerator, fusion magnet, PFAS program, or
geothermal plant is not automatically demand for the startup's subsystem. An inexpensive interview
program is not relabeled as a decisive hardware experiment. Founder fit remains exactly 2% and does
not rescue a failed gate.

The score suggestions are independent P5 recommendations and do not modify P4. New web evidence is
linked directly and must pass the normal source-ledger and origin audit before canonical use.

## Executive disposition

| Idea | P4 score | Suggested score | Kill probability | Current hard-gate failures | Verdict |
|---|---:|---:|---:|---|---|
| `P3R2-E-14` | 69.0 | 56.4 | 60% | None outright; G1/G4/G7 remain marginal | **HOLD** |
| `P3R2-A-05` | 63.2 | 39.8 | 82% | G1, G7 | **KILL** |
| `P3R2-A-22` | 61.0 | 44.2 | 90% | G2, G4, G7 | **KILL** |
| `P3R2-F-02` | 57.6 | 49.4 | 72% | None outright; G1/G3/G4/G6/G7 remain marginal | **HOLD** |
| `P3R2-F-03` | 50.8 | 33.8 | 96% | G1, G4, G7 | **KILL** |

`HOLD` means ineligible for the final 24 today but capable of flipping through a specified customer
or procurement event. `KILL` means the present product thesis should not consume a final-24 slot;
later regeneration would require a materially different commercial architecture, not a nicer score.

## `P3R2-E-14` — multi-terminal DC protection relay and neutral HIL qualification

### Strongest bear case

The field need is genuine, but the US product-demand bridge is still missing. Southern Spirit,
Grain Belt Express, and Grid United prove that HVDC construction is funded. They do not show that a
US developer, TSO, EPC, or converter OEM will buy a third-party DC relay or neutral HIL service.
Moreover, “connects four grid regions” is not sufficient evidence that Grain Belt is a meshed,
multi-terminal DC network requiring the proposed discrimination logic. The P4 packet never verifies
the terminal topology of the anchor US projects.

The proposed whitespace is also less empty than P4 suggests. Hitachi's MACH platform integrates all
HVDC control and protection functions, is designed for a 30-year life, and uses common hardware
across VSC-HVDC, LCC-HVDC, and FACTS
([Hitachi MACH](https://www.hitachienergy.com/us/en/products-and-solutions/hvdc/mach-control-and-protection-system)).
SEL already markets traveling-wave relays for HVDC-adjacent links, with 1–5 ms operation rather than
the proposed startup's unqualified `<1 ms` headline
([SEL time-domain protection](https://selinc.com/solutions/time-domain-line-protection/)). The exact
neutral-test-platform vision is already being built through the EU's InterOPERA consortium: four
HVDC vendors, eight TSOs, two wind-turbine vendors, and three developers are delivering control
cubicles into a 500 kV, 2 GW, five-terminal real-time demonstrator, with standardized HIL interfaces,
tender-ready specifications, and a verification benchmark
([European Commission CORDIS report](https://cordis.europa.eu/project/id/101095874/reporting)).
That is excellent category validation but direct disconfirmation of “the niche is empty.” It also
shows that access to proprietary models, cubicles, and fault behavior is a consortium/governance
problem, not merely an algorithm-and-FPGA problem.

The hidden service burden is high: OEM nondisclosure agreements, model/version control, protection
settings governance, cyber-security review, certification evidence, 24/7 field-event support, and
liability when a trip decision disconnects a multi-billion-dollar link. China is not a beachhead;
NR Electric already bundles LCC/VSC control and protection, and exporting source logic or detailed
plant models would require end-use and EAR review even if the counterparties are not listed.

### Disconfirming evidence and steelman

The same InterOPERA evidence is the strongest steelman. Serious buyers and vendors are spending real
money to create precisely the multi-vendor control/protection and HIL framework this idea describes.
The US project pipeline and `L08-041`/`P3R2-E-14-S01` supply an independent launch window; the
technical work is unusually measurable; and a small team can prototype a relay without building a
power stage. The best surviving wedge is not “a faster relay.” It is an independent US conformance
lab that implements an emerging public benchmark and sells pre-procurement studies to developers.
That wedge remains plausible if a US project owner and at least one converter OEM consent to provide
the models/cubicles needed to make the benchmark real.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **PASS_MARGINAL** | Funded US HVDC projects plus InterOPERA validate the problem class, but no target-market buyer has ordered the startup's relay/HIL service. A US utility, EPC, or OEM paid study/design-in is still required. |
| G2 | **PASS** | `L08-004`–`L08-007` are relevant peer-reviewed multi-terminal protection studies. `L08-019`–`L08-021` concern PV arc detection and should not support the HVDC claim. |
| G3 | **PASS** | A relay/HIL benchmark is bounded and instrumentable, although the frozen $300k budget is just above the preferred range. |
| G4 | **PASS_MARGINAL** | MACH, SEL, NR Electric, and InterOPERA are direct or near-direct alternatives. Neutrality is non-cosmetic only if proprietary interfaces are actually available. |
| G5 | **PASS** | No exotic physics or single forecast is required. |
| G6 | **PASS_MARGINAL** | The US base case is viable, but cyber-security, protection liability, model confidentiality, and any China technology transfer need explicit controls. |
| G7 | **PASS_MARGINAL** | US projects enter construction/in-service near 2030, but their multi-terminal topology and third-party qualification needs are unverified; the exact official category trigger is European, not a target market. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | 3 | Category demand is strong; target-market product demand is absent. |
| Frontier/coolness | 4 | 3 | InterOPERA is already implementing the benchmark vision. |
| High-end niche | 4 | 3 | Valuable, but access is controlled by OEMs and TSOs. |
| Competition whitespace | 3 | 2 | Integrated OEM platforms and the InterOPERA consortium narrow the gap. |
| Reachable budget | 3 | 3 | Software/relay prototype is bounded; certification is not. |
| Elegance/controllability | 5 | 4 | HIL is controllable, but proprietary models and grid interactions limit observability. |
| 10x edge | 2 | 1 | No 10x buyer-valued advantage over OEM/SEL protection is shown. |
| US–China leverage | 2 | 2 | US is plausible; China remains license-only and incumbent-controlled. |
| 2030 window | 4 | 3 | Project dates fit, product-specific procurement does not yet. |
| Expansion | 4 | 3 | MVDC/datacenter extensions are plausible but separately qualified. |
| Founder transfer | 5 | 5 | No change; still only two points. |

Suggested total: **56.4/100**.

### Cheapest decisive falsification

**$85k–$95k over 6–9 months; genuinely sub-$100k for the commercial wedge.** Budget $35k for
engineering and a relay front end, $20k for university RTDS access, $15k for model/interface work,
and $15k–$25k for customer/legal/cyber diligence. Implement one public four/five-terminal benchmark,
then ask one converter OEM and two US developer/utility teams to submit black-box models and blinded
fault cases. Pass only if the prototype reproduces all buyer-defined cases, at least one OEM signs a
model-sharing/HIL memorandum, and one target-market buyer pays at least $25k for a follow-on study.
Kill if OEM data cannot be obtained or every owner requires the converter prime to own protection.

**Final verdict: HOLD.** Promote only after the US paid-study/model-access event and topology audit.

## `P3R2-A-05` — US merchant NEG coating and low-outgassing surface service

### Strongest bear case

P4 mistakes accelerator/facility spending for merchant NEG-coating demand. The cited ITER tenders
are for helium, VVPSS instrumentation, valves, and a cooler-condenser—not NEG coating. The DOE QIS
award funds research centers, not coated chambers. PIP-II's stated completion is 2028, before the
company launches. EIC is the only specific NEG anchor, and official BNL evidence cuts both ways:
the EIC design requires magnetron-sputtered TiZrV NEG in its interaction-region chambers
([EIC design study](https://wiki.bnl.gov/eic/upload/EIC.Design.Study.pdf)), but BNL has already built,
activated, and tested a NEG-coated chamber and records mid-`10^-11` torr performance
([DOE project assessment](https://indico.bnl.gov/event/21787/attachments/52063/89648/2311%20EIC%20Status%20CD-3A%20Rpt%20final.pdf)).
BNL's NSLS-II installed an EIC NEG-coated chamber for photon-desorption testing
([BNL NSLS-II](https://www.bnl.gov/nsls2/newsletter/news.php?a=221688)), and a prior BNL beam-pipe
plan explicitly assigned the new NEG coating to BNL rather than an outside merchant
([BNL sPHENIX plan](https://indico.bnl.gov/event/8496/contributions/37528/attachments/28093/43120/2020MAY15_BEAM_PIPE_DESIGN_STATUS_PRR_V1.pdf)).

Thus the real alternatives are SAES **and buyer self-performance**, not SAES alone. The proposed US
sovereignty wedge has no confirmed procurement rule: P4 itself concedes BABA applicability to DOE
R&D-facility components is unverified. The supposed 10,000x edge belongs to established NEG physics,
not the entrant. Process recipes are public enough to reproduce, while the scarce asset is years of
qualification data on geometry, adhesion, activation cycles, particulate contamination, and photon/
electron-stimulated desorption. A lab can keep that know-how in-house; SAES can add local capacity;
and a startup coating line would face lumpy utilization, difficult warranties, and no public price
with which to establish venture-scale economics.

### Disconfirming evidence and steelman

The steelman is a disciplined second-source service, not a frontier materials company. EIC really
does require NEG; SAES really is the only identified merchant brand; and the process experiment is
technically bounded. Smaller chamber OEMs without a coating rig could value a domestic supplier with
traceable outgassing and activation data. That case becomes investable only after an actual DOE lab
or chamber OEM chooses outside procurement over BNL-style self-performance.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **FAIL** | No cited primary source orders merchant NEG coating. Broad facility awards and unrelated vacuum tenders cannot substitute; the most direct buyer evidence shows in-house BNL capability. |
| G2 | **PASS** | `L07-001`, `L07-008`, and `L07-009` are peer-reviewed, though only `L07-001` is directly NEG-specific. |
| G3 | **PASS** | The 1 m coating and independent vacuum characterization are bounded at the $250k ceiling. |
| G4 | **PASS_MARGINAL** | SAES and lab self-performance are named; domestic merchant service is non-cosmetic, but no buyer has valued it. |
| G5 | **PASS** | Mature physics and ordinary industrial equipment; commercial utilization is the risk. |
| G6 | **PASS_MARGINAL** | No obvious export block, but BABA is not proven to apply and coating acceptance/cleanliness standards are missing. |
| G7 | **FAIL** | PIP-II completes before launch; EIC need is real but coating procurement may occur pre-2030 or in-house. No primary product procurement trigger in 2030–2034 is established. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 4 | 2 | NEG need is real; external merchant purchase is not. |
| Frontier/coolness | 2 | 2 | Mature process replication. |
| High-end niche | 4 | 2 | Narrow but potentially too lumpy and insourced. |
| Competition whitespace | 3 | 1 | SAES plus national-lab in-house capability. |
| Reachable budget | 3 | 3 | First experiment fits; v1 may exceed $5M. |
| Elegance/controllability | 4 | 3 | Bench metrics are clear, but long-geometry process yield is craft-heavy. |
| 10x edge | 3 | 2 | The large outgassing improvement is category physics, not entrant advantage. |
| US–China leverage | 2 | 1 | US-only and not yet purchased. |
| 2030 window | 4 | 2 | Facility dates do not prove in-window coating orders. |
| Expansion | 3 | 2 | Quantum/EUV adjacency remains speculative without quotes. |
| Founder transfer | 1 | 1 | No change. |

Suggested total: **39.8/100**.

### Cheapest decisive falsification

**$70k–$95k over six months; genuinely sub-$100k for demand, not full process qualification.** Use
existing university sputter access to produce three short, geometry-distinct coupons/pipes; allocate
$35k–$45k to deposition and materials, $20k to an independent pumping/outgassing laboratory, and
$15k–$30k to controlled buyer qualification. Before coating, require two US labs or chamber OEMs to
provide blinded acceptance specifications and a conditional RFQ. Pass only if both samples meet the
specification and at least one counterparty issues a conditional order/LOI worth at least $250k.
Kill if buyers will not provide specifications, insist on in-house coating, or name SAES qualification
history as non-substitutable. This does not validate a production line; it decisively tests whether a
merchant socket exists.

**Final verdict: KILL** in the current final-24 contest. Regenerate only after an external US RFQ.

## `P3R2-A-22` — modular plasma destruction for concentrated PFAS waste

### Strongest bear case

The proposal is behind both regulation and competitors. EPA's April 2026 interim guidance still
identifies only thermal destruction, landfills, and underground injection as large-scale-capacity
options; plasma and SCWO remain outside that recognized set
([EPA 2026 guidance](https://www.epa.gov/pfas/interim-guidance-destruction-and-disposal-pfas-and-materials-containing-pfas)).
At the same time, the “thin foreign plasma supplier” story is obsolete. EPA now describes US company
Onvector's plasma-vortex system destroying more than 99% of PFOA/PFOS and entering pilot testing with
the US Air Force
([EPA SBIR technologies](https://www.epa.gov/sbir/test-and-treat-pfas-epa-sbir-technologies)).
Aquagga has already deployed a containerized 5–10 gallon/hour hydrothermal system at a 3M facility
and processed more than 1,000 gallons while surpassing destruction targets
([EPA Aquagga profile](https://www.epa.gov/sbir/epa-sbir-funded-technology-provides-solution-pfas-destruction-industrial-wastewater-producers)).
Add PyroGenesis's completed DoD plasma contract and 374Water's multi-site SCWO traction, and the
startup faces several funded, field-tested competitors—not a lonely supplier gap.

The evidence chain for the claimed `<50 kWh/kg-PFAS`, `>99.99%` destruction with closed fluorine
mass balance is especially weak. P4 cites `L01-101` (an ozone-generator paper), `L01-105` (a general
controllable-energy plasma reactor), and `L01-112` (an SBIR portfolio record). None demonstrates PFAS
destruction, concentrate-scale energy economics, HF capture, or closed fluorine balance. The real
system burden includes feed variability, corrosion, fluoride/HF capture, off-gas and byproduct
measurement, analytical chain-of-custody, uptime, and years of regulator/customer validation. A
$550k skid is above the preferred experiment band and the stated $5M–$12M v1 exceeds the founder
capital envelope. The 2026 AFFF replacement deadline creates waste; it does not mandate plasma
destruction. EPA's delayed drinking-water compliance weakens the second buyer leg.

### Disconfirming evidence and steelman

The steelman is that DoD has paid for plasma destruction and EPA reports a US Air Force plasma pilot,
so product-category demand is more direct than P4 knew. Concentrated AFFF and regenerant streams are
better initial feeds than dilute drinking water. Verification instrumentation could become valuable
across destruction technologies. But this evidence improves G1 while simultaneously destroying the
competition-whitespace thesis: Onvector already occupies the proposed US plasma-vortex wedge.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **PASS** | PyroGenesis's paid DoD contract and EPA's independent report of an Onvector/USAF pilot prove product-category demand. They do not prove demand for this entrant. |
| G2 | **FAIL** | The cited peer-reviewed papers are affirmatively reviewed but not PFAS-destruction evidence. The load-bearing energy, destruction, and mass-balance claims lack relevant peer-reviewed support in the current packet. |
| G3 | **PASS_MARGINAL** | The skid test is explicit and bounded but costs $550k; no complete sub-$250k real-feed protocol is specified. |
| G4 | **FAIL** | Onvector is an exact US plasma competitor; PyroGenesis, Aquagga, and 374Water cover plasma/hydrothermal alternatives. No supported non-cosmetic advantage remains. |
| G5 | **PASS_MARGINAL** | Plasma destruction is real, but the entire economics rests on an undemonstrated energy/mass-balance operating point. |
| G6 | **PASS_MARGINAL** | The regulatory path is acknowledged, yet EPA still omits plasma from the large-scale-capacity list; verification acceptance is unresolved. |
| G7 | **FAIL** | The primary deadline is AFFF replacement in 2026, not 2030–2034 destruction procurement; utility compliance is delayed and no named in-window plasma buy is cited. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 4 | 4 | Paid DoD plasma work plus an independent USAF pilot. |
| Frontier/coolness | 4 | 4 | Auditable molecular destruction remains technically compelling. |
| High-end niche | 3 | 2 | Buyers exist, but competitors already field systems. |
| Competition whitespace | 2 | 1 | Onvector directly overlaps; SCWO/HALT competitors have field traction. |
| Reachable budget | 3 | 1 | $550k first skid and $5M–$12M v1 are outside the preferred path. |
| Elegance/controllability | 3 | 2 | Feed chemistry, byproducts, mass balance, and corrosion interact. |
| 10x edge | 2 | 1 | No 10x advantage over plasma, SCWO, or HALT is demonstrated. |
| US–China leverage | 2 | 1 | US only; China is absent. |
| 2030 window | 3 | 1 | The binding mandate predates launch and the later trigger is inferential/adverse. |
| Expansion | 3 | 2 | Other wastes require fresh chemistry and regulatory validation. |
| Founder transfer | 3 | 3 | No change; power and instrumentation help but do not solve process chemistry. |

Suggested total: **44.2/100**.

### Cheapest decisive falsification

**$180k–$230k over 9–12 months; not sub-$100k and therefore not a portfolio cheap-test credit.** Use
an existing plasma lab and analytical subcontractor; run matched real AFFF/IX-regenerant feeds
against the Onvector/PyroGenesis-relevant operating envelope, not clean surrogates. Pre-register
energy, destruction, total-organic-fluorine, fluoride/HF, short-chain byproducts, corrosion, and
uptime metrics. Pass only at `>99.99%` destruction with at least 95% fluorine closure, `<50
kWh/kg-PFAS`, and five consecutive 8-hour runs without material failure, while a DoD/prime observer
signs a follow-on pilot letter. Kill on any mass-balance gap above 5%, persistent toxic byproducts,
energy above threshold, or no buyer observer. A sub-$100k coupon campaign would not test the
load-bearing system economics and should not be counted as decisive.

**Final verdict: KILL.** A verification-only product could be regenerated separately.

## `P3R2-F-02` — superconducting-magnet drive-and-dump electrical BOP

### Strongest bear case

This is an integration bundle offered against incumbents that already own nearly every component.
OCEM supplies converters to 50 kA at 5 ppm and fusion switching/safety units; Danfysik advertises
0.1 ppm stability, one hundred times tighter than the proposal's 10 ppm headline. Current leads,
busbars, dumps, interlocks, and acceptance tests are not optional whitespace—they are established
project-engineering work performed by those vendors, labs, magnet suppliers, or EPC teams. The
startup's “catalog + protocol” packaging is useful but easily copied, and site commissioning of
kiloamp-class energy extraction creates high warranty and service exposure.

The US demand sources prove magnets and fusion programs, not an external electrical-island purchase.
CFS can bundle this BOP once volumes justify it. The China evidence is better than the P4 narrative
states but cuts against a US entrant: ASIPP's official 2026 ITER PF converter-control-module tender
had a RMB 6.3M ceiling
([ASIPP tender](https://www.ipp.cas.cn/ztbxx/zbxx/202512/t20251225_813649.html)), and its 2025 RMP
power-system upgrade had a RMB 2.85M ceiling and a three-month delivery obligation
([ASIPP RMP tender](https://www.ipp.cas.cn/ztbxx/zbxx/202507/t20250729_643575.html)). These are genuine,
product-adjacent buyer records that repair the dossier's “could not confirm” statement, but they are
small, near-term, domestic government procurements—not evidence that ASIPP will buy a US standardized
drive-and-dump skid in 2030. The fusion mid-2030s schedule also creates a timing mismatch: serial
commercial demand may arrive after the portfolio's 2034 kill horizon.

### Disconfirming evidence and steelman

The steelman is a narrower entry SKU: instrumented binary current leads/feedthroughs with certified
heat-load and quench-tolerance data. CFS/Realta establishes merchant magnet commerce, DOE funds eight
fusion teams, and the two official ASIPP tenders prove recurring high-current power-electronics
procurement in China. Physics is mature and all performance metrics are measurable. A supplier could
win if a merchant magnet builder explicitly refuses to internalize the electrical island and asks
for standardized interfaces. No such buyer commitment exists today.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **PASS_MARGINAL** | Magnet demand and official ASIPP power-system tenders are real; no buyer orders the combined skid or entry-SKU lead product. |
| G2 | **PASS** | Cited magnet/power-engineering literature is peer-reviewed where academic, although several cited records (`L03-018`, `L03-020`, `L03-021`, `L05-003`, `L07-009`) do not directly validate the full BOP bundle. |
| G3 | **PASS_MARGINAL** | The $400k full demonstration is above range. The lead track could be cheaper, but the current packet does not specify its decisive budget and thresholds. |
| G4 | **PASS_MARGINAL** | OCEM, Danfysik, CFS, and lab in-house teams are named. Integration is non-cosmetic, but the incumbents can bundle it rapidly. |
| G5 | **PASS** | Mature components and multiple demand programs. |
| G6 | **PASS_MARGINAL** | US sales are viable; high-current fusion exports and ASIPP end use need official restricted-party/end-use review, not an OpenSanctions negative alone. |
| G7 | **PASS_MARGINAL** | DOE/CFS point to mid-2030s plants and ASIPP buys now, but no primary 2030–2034 integrated-skid procurement trigger is established. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | 3 | Strong adjacent demand; no skid order. |
| Frontier/coolness | 3 | 2 | Integration/catalog play, not a technical leap. |
| High-end niche | 3 | 3 | Few valuable buyers, but incumbents already serve them. |
| Competition whitespace | 2 | 1 | OCEM/Danfysik/CFS can cover the bundle. |
| Reachable budget | 3 | 2 | $400k experiment and $5M–$12M v1 exceed preference. |
| Elegance/controllability | 4 | 4 | Stability, dump waveform, and heat load are measurable. |
| 10x edge | 1 | 1 | The proposal trails incumbent stability specifications. |
| US–China leverage | 3 | 3 | Both markets show adjacent demand; China access remains uncertain. |
| 2030 window | 3 | 2 | Serial commercial plants skew toward/after mid-2030s. |
| Expansion | 3 | 3 | Accelerator and industrial magnet adjacencies are credible. |
| Founder transfer | 3 | 3 | No change. |

Suggested total: **49.4/100**.

### Cheapest decisive falsification

**$110k–$160k over 9 months; not honestly sub-$100k.** With a university magnet lab, build only the
5 kA instrumented binary-lead/feedthrough entry SKU and publish blinded heat-load, vacuum-leak,
thermal-cycle, and quench-tolerance results against one commercial alternative. Budget $50k–$70k
hardware, $30k–$45k cryogenic facility/test time, and $30k–$45k independent metrology and customer
qualification. Pass only if heat leak is at least 30% lower at equal current/temperature boundary,
ten thermal cycles and three induced quenches cause no loss of seal, and one merchant magnet buyer
issues a paid pilot or conditional order above $100k. Kill the startup thesis if the buyer wants
OCEM/CFS/lab integration or if no performance/warranty advantage appears. Cutting the plan below
$100k would require donated cryogenic time and would not be a credible independent budget.

**Final verdict: HOLD.** Promote only after the paid entry-SKU order and a dated in-window skid path.

## `P3R2-F-03` — high-speed PM generator/converter electrical cartridge

### Strongest bear case

The proposed merchant socket is contradicted by the transaction used to prove demand. Fervo buys
complete proprietary ORC units from vertically integrated Turboden; the framework explicitly expands
Turboden's US supply chain. Ormat is vertically integrated. Hanwha builds turbo-expander-generator
systems. Calnetix already sells the generator + magnetic bearings + power-electronics cartridge at
125 kW. The remaining scale wedge is also occupied by established machine companies: ABB documents
a high-speed PM generator family for full-converter systems expanding to 7 MW
([ABB product note](https://new.abb.com/docs/default-source/ewea-doc/hs-pm-generators-series-for-full-converter-concept.pdf?sfvrsn=2)),
while Nidec markets dedicated ORC turbine generators
([Nidec ORC generators](https://www.nidec.com/en/machine-tool/products/B108/M106/S102/NASI-GeneratorsForOrcTURBINES/)).
The startup therefore has neither a new category nor a clean 0.3–20 MW gap.

The technical and capital burden is severely understated. Scaling a 250 kW prototype to 20 MW is
not a product-family extension; it changes rotor dynamics, bearings, containment, insulation,
cooling, converter voltage, grid compliance, manufacturing, and field service. Sandia's `L04-113`
documents unresolved sCO2 bearing/material issues. The first hardware test is $900k and v1 is
$8M–$20M. China has one state-linked demonstration and an untriangulated retrofit forecast; there is
no evidence that CNNC or a steel EPC will license a US electrical cartridge rather than source the
domestic institute/OEM ecosystem. Export classification is probably manageable, but plant access,
local certification, IP leakage, and long-duration service remain material.

### Disconfirming evidence and steelman

The steelman is strong underlying market pull. Fervo's 1.75 GW framework and Chaotan One's operation
are real; high-speed PM machines and active-front-end converters are established; interviews can
cheaply prevent a bad hardware build. A narrowly specified 0.3–1 MW cartridge for a non-sCO2 niche
might find one OEM. But that would be a new, smaller idea competing with Calnetix, not validation of
the frozen 0.3–20 MW sCO2/ORC platform.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **FAIL** | Every cited transaction purchases a complete turbine/integrated plant, not a third-party cartridge. No machine builder has ordered or committed to the product. |
| G2 | **PASS** | The cited sCO2 technical work is peer-reviewed/official where required and is appropriately adverse. |
| G3 | **PASS_MARGINAL** | The $900k experiment is explicit and staged, but far outside the reachable band and not decisive across 0.3–20 MW. |
| G4 | **FAIL** | Calnetix, ABB, Nidec, Turboden, Ormat, and Hanwha occupy the cartridge, generator, or integrated alternatives. Scale/duty alone is not a demonstrated defendable difference. |
| G5 | **PASS** | Physics is established; the commercial architecture, not physics, fails. |
| G6 | **PASS_MARGINAL** | Ordinary EAR/grid-code review is plausible, but the CN licensing/service/IP path is not evidenced. |
| G7 | **FAIL** | Fervo's three-year framework largely precedes launch; Chaotan One is an in-house demonstration. No named 2030–2034 merchant-cartridge procurement trigger exists. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | 2 | Turbine demand is strong; cartridge demand is absent. |
| Frontier/coolness | 2 | 2 | Useful standardization, already established. |
| High-end niche | 2 | 1 | OEM socket is vertically integrated or already supplied. |
| Competition whitespace | 2 | 0 | Multiple direct and adjacent incumbents cover the proposed range. |
| Reachable budget | 2 | 1 | $900k experiment and $8M–$20M v1. |
| Elegance/controllability | 4 | 3 | Drive-stand tests are bounded at one rating, not across the family. |
| 10x edge | 1 | 1 | No order-of-magnitude advantage. |
| US–China leverage | 3 | 2 | Underlying demand exists in both; product beachheads do not. |
| 2030 window | 3 | 2 | Anchor framework precedes launch; CN follow-on is speculative. |
| Expansion | 3 | 2 | Each thermodynamic cycle and rating needs fresh qualification. |
| Founder transfer | 3 | 3 | No change. |

Suggested total: **33.8/100**.

### Cheapest decisive falsification

**$45k–$70k over four months; a genuine sub-$100k commercial test but not a decisive hardware
experiment.** Conduct NDA-backed specification workshops with at least eight independent ORC/sCO2/
waste-heat machine builders, excluding end customers already committed to Turboden/Ormat. Give each
the same interface, rating, price, warranty, and service proposal; require written make/buy feedback.
Pass the merchant-socket test only if two unrelated OEMs provide signed requirements with forecast
volume and one commits at least $150k of co-development cash or an equivalent paid NRE purchase.
Kill before hardware if fewer than two will externalize the electrical island. Even a pass does not
earn the portfolio's sub-$100k decisive-experiment credit because rotor/bearing/grid performance
still requires the $900k-class rig.

**Final verdict: KILL.** Do not build the rig without a paid OEM socket; regenerate a narrower rating
only if the commercial test identifies one.

## Group conclusion

The two holds are conditional, not portfolio-ready: E-14 needs a US paid HIL/model-access event, and
F-02 needs a paid current-lead entry order plus a dated drive-and-dump path. A-05, A-22, and F-03
fail because their cited system-level demand does not establish the proposed merchant product, while
direct buyer self-performance or incumbents occupy the supposed gap. No geography argument or
founder-fit score changes those conclusions.
