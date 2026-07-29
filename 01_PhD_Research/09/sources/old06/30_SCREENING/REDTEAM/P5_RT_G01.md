# P5 adversarial red team — group G01

Scope: `P3R2-D-02`, `P3R2-G-03`, `P3R2-D-13`, `P3R2-F-06`, and
`P3R2-A-13`. This review tries to kill the business, not the underlying field. It treats a funded
system as different from a purchased subsystem, a vendor roadmap as different from a buyer order,
and an inexpensive learning task as different from a decisive experiment. Founder fit is never
used to rescue a gate.

The score suggestions below are independent P5 recommendations; they do not modify the
authoritative P4 scorecards. New web findings are cited by direct URL and should pass the normal
source-ledger/origin audit before canonical use.

## Executive disposition

| Idea | P4 score | Suggested score | Kill probability | Current gate failures | Verdict |
|---|---:|---:|---:|---|---|
| `P3R2-D-02` | 76.6 | 64.0 | 40% | G7 on the evidence currently in the ledger | **HOLD** |
| `P3R2-G-03` | 67.0 | 42.2 | 75% | G1 | **HOLD** |
| `P3R2-D-13` | 63.0 | 47.0 | 80% | none hard, but G1/G4/G5 are marginal together | **KILL** |
| `P3R2-F-06` | 60.4 | 36.0 | 88% | G1, G7 | **KILL** |
| `P3R2-A-13` | 57.2 | 29.6 | 92% | G1, G7 | **KILL** |

`HOLD` means not eligible for the final 24 today. It is a near-miss with a specific evidence event
that can flip the verdict. `KILL` means the present product thesis should not consume a final-24
slot; it may be regenerated later only if the commercial architecture changes materially.

## `P3R2-D-02` — reel-to-reel REBCO acceptance metrology

### Strongest bear case

The opportunity is real, but P4 confuses growth in REBCO tape with whitespace in REBCO tape
metrology. THEVA already sells the contactless reel-to-reel critical-current scanner, and the best
new buyer evidence shows sophisticated magnet builders adopting that incumbent rather than waiting
for a neutral referee. CERN reports that it procured a THEVA Tapestar XL-HF for 33 km of four-supplier
REBCO procurement, at 200 m/h, for critical-current homogeneity and defect localization
([CERN HFM program, p.23](https://indico.cern.ch/event/1298458/contributions/5977855/attachments/2877627/5039933/240613_HTS_HFM.pdf)).
Bruker states that acceptance of long REBCO conductors already relies on magnetic Tapestar data plus
transport-Ic testing, with in-house short-sample checks
([Bruker/ASC presentation, pp.22–23](https://snf.ieeecsc.org/files/ieeecsc/slides/Vonlanthen%20presentation.pdf)).
THEVA's own published product sheet specifies reel-to-reel operation, up to 55 m/h for the older
unit, and ±3% of measuring range accuracy
([THEVA product sheet](https://www.theva.de/wp-content/uploads/2018/05/specs-theva-tapestar-101114.pdf)).

Those records validate product-category demand but weaken the supposed neutral-referee opening.
The buyer can purchase THEVA's instrument directly, accept supplier Tapestar maps, and add its own
transport samples. The proposed product must therefore prove a buyer-valued result that the incumbent
does not provide: for example, materially faster measurement at equal accuracy, previously missed
delamination prediction, or a cross-vendor acceptance decision that changes lot disposition. Merely
combining a Hall array with thermal imaging is not a moat.

There is also a source-quality defect in the China timing case. Canonical
`P3R2-D-02-S02` is a T2 Eastmoney *Caifuhao* retail-stock post, not a Shanghai
Superconductor filing, tender, or buyer procurement. It should not be described as “company-sourced”
or “procurement-grade.” A fresh official company page does support a 4,000 km/year 2025 capacity and
a Phase III target of 20,000 km/year by the end of 2027
([Shanghai Superconductor 2025 review](https://www.shsctec.com/en/news/sst2025summary/)), but that
date still does not satisfy the binding requirement for one primary/official source specifying a
2028–2035 trigger. The current official evidence is excellent evidence of scale-up, not a compliant
in-window G7 source.

The hidden operating burden is nontrivial: cryogenic liquid handling, lift-off and temperature
calibration, tape-width and stack-specific models, reference-sample traceability, transport-Ic
correlation, vendor-line integration, and on-site service in both the US and China. A “certified”
instrument also needs a live acceptance standard or bilateral buyer specification; the cited IEC
record remains unfetched.

### Disconfirming evidence and steelman

This is the strongest of the five ideas. CERN's actual purchase proves buyers spend on this exact
instrument class. Bruker's reliance on full-length magnetic scans proves the data affects acceptance,
not just process R&D. Tape volume is scaling independently of any one fusion program, and the
Shanghai Superconductor capacity build is a direct, eligible company disclosure. Physics is bounded,
the existing $120,000 experiment is close to the preferred range, and an independent multi-modal
instrument could still win if it catches failure modes that supplier-generated Tapestar data misses.
The US and China both have real tape ecosystems, even though no China buyer of this new instrument
has yet been named.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **PASS** | CERN's instrument procurement plus Bruker's buyer-side reliance on Tapestar acceptance data closes product-category demand far better than the P4 tape-volume proxies. The new product's incremental demand remains unproven, but the category is purchased. |
| G2 | **PASS** | The core defect/current-measurement physics has eligible peer-reviewed support. Do not use unfetched IEC material or the irrelevant `L03-050` cryocooler record. |
| G3 | **PASS** | The blinded tape-to-transport correlation is bounded and falsifiable. It must add an incumbent benchmark and customer-blinded material. |
| G4 | **PASS_MARGINAL** | THEVA is the direct incumbent. Multi-modal delamination screening and independent acceptance are non-cosmetic in principle, but CERN and Bruker show buyers already accept the incumbent workflow. |
| G5 | **PASS** | No exotic physics or unlimited capital is required. |
| G6 | **PASS_MARGINAL** | Ordinary metrology is not structurally blocked, but official restricted-party screening for every proposed China counterparty and bilateral data/IP partitioning are still absent. |
| G7 | **FAIL on current canonical evidence** | The official company source now found targets end-2027 capacity. The ledger's claimed 2030 source is a T2 retail-stock post, not a primary/official trigger. Obtain a primary/official 2028–2035 capacity, procurement, or magnet-build trigger before selection. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 4 | 4 | Actual incumbent-instrument procurement is now visible. |
| Frontier/coolness | 4 | 3 | Contactless tape mapping is established; novelty is the multi-modal/acceptance layer. |
| High-end niche | 4 | 4 | Few quality-critical buyers and high conductor value remain attractive. |
| Competition whitespace | 2 | 1 | CERN procured the incumbent; Bruker already relies on its data. |
| Reachable budget | 5 | 5 | $120k remains decisive if the benchmark is honest. |
| Elegance/controllability | 4 | 3 | Production-speed inversion, lift-off, cryogenic uniformity, and cross-vendor calibration interact. |
| 10x edge | 3 | 2 | No eligible comparison yet proves 10x throughput, yield, or avoided scrap against Tapestar XL-HF. |
| US–China leverage | 4 | 3 | Tape demand exists in both; a Chinese metrology buyer and official counterparty clearance do not. |
| 2030 window | 4 | 3 | Scale-up is real, but the strict official in-window source is missing. |
| Expansion | 3 | 2 | Cable/coil passports are plausible, but each geometry needs fresh calibration. |
| Founder transfer | 5 | 5 | No change; still only 2% of score. |

Suggested total: **64.0/100**.

### Cheapest decisive falsification

**$85k–$95k, 6–9 months, potentially a genuine sub-$100k test.** Secure 30–50 m of customer-blinded
tape across at least two vendors, including naturally occurring defects; obtain the supplier's
Tapestar map only after predictions are frozen; scan at the incumbent's 200 m/h class; and blind-test
30 transport coupons plus at least ten delamination/structural outcomes. Pass only if the prototype
achieves ≤5% Ic error, ≥95% localization of buyer-defined rejectable defects, and changes at least one
lot-disposition decision relative to the incumbent data. Kill if it merely reproduces Tapestar or if
the buyer will not provide blinded tape. This is decisive for the *incremental wedge*; it does not
validate the later m/s production-speed claim.

**Final verdict: HOLD.** Promote only after both the blind incumbent benchmark and a compliant
primary/official 2028–2035 timing source exist.

## `P3R2-G-03` — DC-conversion commissioning and acceptance island

### Strongest bear case

No named operator, hyperscaler, commissioning agent, or Chinese integrator has purchased the proposed
swept-impedance/IT-network acceptance product. NVIDIA's 800 VDC roadmap proves an architecture shift,
not demand for this instrument. MIR/Huxiu proves a heterogeneous Chinese installed base, not a paid
commissioning socket. This fails the product-specific reading of G1.

The alleged whitespace also narrowed during red-team refresh. Ampere Development currently markets
rentable 800 VDC commissioning load banks from rack scale to 1 MW+, including programmable transients,
step-load/ripple simulation for converter stability, and Levels 4/5 integrated-system testing
([Ampere 800 VDC commissioning](https://ampere.dev/800v-dc-load-banks-data-centers)). TÜV SÜD already
offers neutral data-center testing and commissioning, on-site electrical measurements, power-quality
analysis, power-architecture assessment, and five-level integrated testing
([TÜV SÜD data-center services](https://www.tuvsud.com/en/services/inspection/data-centre-infrastructure-services)).
Neither source proves a swept-impedance clone, but together they occupy the equipment and trusted-
dossier sides of the proposed bundle. Keysight, CQC, CEPREI, incumbent commissioning agents, and
integrator self-certification can fill the remaining method gap without adopting the startup's
hardware.

The service model is also much heavier than the score implies. Deliberately perturbing an energized
800 VDC bus creates safety, uptime, warranty, and professional-liability exposure. Operators may
allow it only in factory test or a segregated dummy load, eliminating the “live-site” advantage.
Every architecture and firmware revision changes impedance; maintaining a cross-vendor library is
continuous applications engineering, not software-like margin. The China route adds entity
screening, local certification, source-code/IP partitioning, and on-site service. The existing
OpenSanctions no-hit record is a T3 aggregator search, not an official US Consolidated Screening List
clearance.

### Disconfirming evidence and steelman

The underlying pain is credible. NVIDIA plans full-scale 800 VDC production from 2027, multiple DC
architectures will coexist, and neutral commissioning is already an accepted data-center service.
The proposed swept-impedance and unearthed-IT-network tests are more diagnostic than a resistive load
bank. If an operator pays for that extra evidence and if the method predicts an instability that
ordinary Level-5 testing misses, the sequence library could become valuable. The concept is also
technically controllable in a partner testbed.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **FAIL** | Architecture roadmaps and installed-base estimates are not two independent demand sources for this product; there is no named buyer order, paid pilot, procurement line, or primary buyer specification for swept-impedance acceptance. |
| G2 | **PASS** | The general power-electronics methods are established, although the cited `L02-010`, `L02-036`, and `L02-112` records do not by themselves validate the complete product. |
| G3 | **PASS_MARGINAL** | The $300k experiment is bounded only if the 100 kW testbed is contractually available. It does not validate safe live-site permission. |
| G4 | **PASS_MARGINAL** | Swept impedance plus signed dossiers is non-cosmetic, but Ampere now covers 800 VDC commissioning hardware/transients and TÜV SÜD covers neutral commissioning evidence. |
| G5 | **PASS** | No new physics is required; commercial adoption, not feasibility, is the dominant risk. |
| G6 | **PASS_MARGINAL** | Commercial instrumentation is not inherently blocked, but official restricted-party screening, local safety/certification scope, data export, and liability allocation are unresolved. |
| G7 | **PASS_MARGINAL** | The 2027–2030 architecture transition is real. Persistence of paid startup-owned acceptance through 2034 is not; incumbents could absorb it before launch. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 2 | 1 | No product-specific paid demand. |
| Frontier/coolness | 4 | 3 | Interesting systems method, but adjacent tools already exist. |
| High-end niche | 3 | 2 | Reachability and willingness to pay are unproven. |
| Competition whitespace | 3 | 1 | Ampere plus neutral commissioning firms bracket the product. |
| Reachable budget | 3 | 2 | Depends on loaned high-power hardware and later field liability. |
| Elegance/controllability | 4 | 3 | Lab method is controlled; live heterogeneous sites are not. |
| 10x edge | 3 | 1 | No quantified advantage over load-bank/Level-5 commissioning. |
| US–China leverage | 4 | 2 | Independent macro demand exists; neither leg has a frame agreement. |
| 2030 window | 4 | 3 | Architecture timing is good, absorption risk is high. |
| Expansion | 4 | 3 | Adjacent DC sites are possible only if the method wins credibility. |
| Founder transfer | 5 | 5 | No change; still capped at 2%. |

Suggested total: **42.2/100**.

### Cheapest decisive falsification

**$25k–$40k, 6 months, commercial rather than hardware.** Deliver a written, vendor-neutral test
protocol and a small analyzer emulator to 15 named US commissioning agents/operators and 10 named CN
integrators. Pass only if one US counterparty pays at least $15k for a controlled pilot and one CN
counterparty signs a separately enforceable paid-pilot or frame-agreement term naming impedance or
IT-network testing that its current commissioning stack cannot perform. Kill the relevant geography
if that condition fails. This is genuinely decisive for the business's central willingness-to-pay
risk; a cheap 10 kW lab demo alone is not decisive and must not count as the portfolio's sub-$100k
first experiment.

**Final verdict: HOLD.** Exclude from the final 24 until G1 closes with paid product-specific demand.

## `P3R2-D-13` — directed-energy thermal magazine

### Strongest bear case

This is a mature subsystem category dressed as whitespace, with an unfavorable mass trade at the
claimed scale. General Atomics demonstrated 3 MJ in a 35 kg, 230 kW PCM unit in 2010. Scaling that
demonstrated *system* specific energy to 300 MJ implies roughly 3,500 kg before any non-linear
structure, plumbing, or qualification penalty. P4's “roughly 1.2 tonnes” uses ~250 kJ/kg PCM latent
heat and therefore omits encapsulation, heat exchangers, two-phase spreaders, pumps, structure, and
working fluid. On a mobile container, shrinking chiller power can simply be exchanged for several
tonnes of thermal magazine and a long recharge constraint.

Competition is materially worse than the scorecard states. ACT markets custom PCM hardware for
30+kW directed-energy systems. General Atomics has demonstrated a dedicated DEW device. Honeywell
acquired Rocky Research and states that the unit specializes in cooling systems for directed energy
([Honeywell directed-energy capabilities](https://ws.aerospace.honeywell.com/us/en/pages/directed-energy/electromagnetic-spectrum-operations));
Honeywell also says Rocky had major DoD power/thermal contracts and complete-product support
([acquisition release](https://www.honeywell.com/us/en/news/press-releases/2020/10/honeywell-acquires-rocky-research-a-technology-leader-in-power-and-thermal-management)).
Rocky is the assignee of active US patent 11,605,929 covering a directed-energy thermal-management
system with phase-change storage
([patent record](https://patents.google.com/patent/US11605929B2/en)). A 2030 startup would therefore
face a defense prime, a merchant specialist, and a Honeywell-owned specialist with IP, contracts,
qualification, and platform access.

The funded JLWS/E-HEL programs prove laser-system demand, not a merchant thermal-LRU purchase. E-HEL
at 30 kW is below the product's claimed need; IFPC-HEL and DE M-SHORAD setbacks show that the broader
fleet can shrink. The idea is concentrated in a few classified programs with long security,
qualification, and prime-integration cycles. Service burden includes ITAR, AS9100, MIL environmental
qualification, PCM containment and aging, field recharge behavior, and prime-owned thermal control
integration.

There is also a citation-integrity error to repair: the canonical ledger maps
`P3R2-D-13-S02` to ACT and `P3R2-D-13-S03` to General Atomics, while both the evidence
dossier and scorecard reverse those aliases. The facts are directionally right; the IDs are wrong.

### Disconfirming evidence and steelman

The underlying transient-thermal problem is real, the JLWS power ladder is dated and funded, and
the governing thermal quantities can be measured. A new entrant might win a narrow component if it
achieves a customer-specified system-level energy density at 300–500 kW that the incumbent products
cannot meet, particularly as a supplier to a non-integrated laser prime. SBIR can finance early work.
The “magazine” framing is operationally intuitive and expansion to radar/EW pulse loads is plausible.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **PASS_MARGINAL** | Funded laser systems plus existing merchant DEW thermal products prove a category, but no cited buyer procurement specifies the proposed 300 MJ LRU. |
| G2 | **PASS** | No unreviewed academic claim is required, but several cited technical records concern data-center immersion, satellite heat pipes, or phased arrays rather than a 300 MJ DEW PCM system. |
| G3 | **PASS** | The $220k brassboard is bounded, measurable, and within the rubric's outer range. |
| G4 | **PASS_MARGINAL** | Closest competitors are now named. The only non-cosmetic difference is unproven 300 MJ/MW scale; incumbents are better placed to scale. |
| G5 | **PASS_MARGINAL** | Physics exists, but the base claim hides the system-mass and recharge trade. It passes only if the claim becomes customer-envelope-specific rather than “10x smaller chiller.” |
| G6 | **PASS** | US-only ITAR/defense route is acknowledged and structurally possible. |
| G7 | **PASS** | JLWS's 300–500 kW ladder falls in the launch window; the greater risk is incumbent capture, not timing. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | 2 | System funding is one layer removed from the LRU. |
| Frontier/coolness | 3 | 3 | The operational framing remains compelling. |
| High-end niche | 3 | 2 | Few programs and entrenched suppliers. |
| Competition whitespace | 2 | 1 | GA, ACT, and Honeywell/Rocky occupy the niche. |
| Reachable budget | 4 | 3 | Brassboard is reachable; qualified v1 and platform access are not clearly sub-$5M. |
| Elegance/controllability | 4 | 3 | Coupon physics is clean; tonne-scale mobile integration is not. |
| 10x edge | 3 | 1 | No system-level 10x SWaP comparison; chiller power is traded for magazine mass/recharge time. |
| US–China leverage | 3 | 3 | Solid US-only case; China is correctly excluded. |
| 2030 window | 4 | 3 | Timing is credible but fielding consolidation is severe. |
| Expansion | 3 | 2 | Adjacent burst loads have different temperature and duty constraints. |
| Founder transfer | 1 | 1 | No change. |

Suggested total: **47.0/100**.

### Cheapest decisive falsification

A sub-$100k experiment is decisive **only with a prime-supplied platform envelope**. For
**$85k–$100k**, build a geometrically representative ~0.6 MJ module, test ≥100 W/cm² source flux,
<10 K plate excursion, 500 cycles, complete system gravimetric energy density, pressure/containment,
and recharge behavior, then compare against the prime's chiller baseline inside its written mass,
volume, power, and revisit-time envelope. Kill if the full system does not beat that baseline or if
no prime will provide the envelope. Without the customer baseline this is just a materials coupon,
not a decisive experiment, and should not count toward the portfolio's sub-$100k quota.

**Final verdict: KILL.** The combination of mass trade, concentrated demand, and incumbent/IP
position overwhelms the present differentiation.

## `P3R2-F-06` — wideband DC sensing for HVDC

### Strongest bear case

The demand evidence does not point to this product. Southern Spirit is a real HVDC project, but its
project page does not specify a merchant wideband sensor. PRC-028 is not a 100 kHz DC-side
transducer mandate. NERC's official standard is titled “Disturbance Monitoring and Reporting
Requirements for Inverter-Based Resources”; its enumerated current and voltage measurements are
largely AC-side fault/disturbance records, with a minimum 64 samples per cycle, even where a dedicated
VSC-HVDC connection is in scope
([NERC PRC-028-1 draft text](https://www.nerc.com/globalassets/standards/projects/2021-04/2021-04-prc-028-1_redline_to_last_posted_05312024.pdf)).
That is orders of magnitude below, and a different measurement job from, the proposed DC-to-100 kHz
traveling-wave sensor. The compliance date cannot serve as product-specific demand.

LEM already ships ppm-class zero-flux sensors up to 24 kA and explicitly targets HVDC. ABB/Hitachi
optical sensing and converter OEM station packages occupy the optical side. The startup's only wedge
is “combined accuracy + bandwidth + open protocol,” but no buyer requirement quantifies that
combination, no incumbent benchmark proves a 10x edge, and no protection OEM exposes a merchant
socket. Worse, the idea is structurally conditional on a separate third-party protection idea
winning station access. A product cannot receive a standalone portfolio slot when its market exists
only if another unproven architecture first displaces vertically integrated OEM control/protection.

Utility service burden is high: 10 kA/high-voltage calibration, insulation coordination, station
EMI, long-life drift, traceable round robins, outage windows, spares, cyber/configuration control,
and multi-year OEM qualification. China is correctly excluded as a beachhead; Xuji/NR domestic
bundling makes a royalty-only route speculative, and no term sheet exists.

### Disconfirming evidence and steelman

HVDC construction is real, Southern Spirit's 2029/2032 dates fit launch, and traveling-wave
protection benefits from faithful wideband measurements. The technical stack is buildable and a
national-lab round robin could create a credible reference. A narrow US research/OEM evaluation
instrument might sell even if the station-component business does not. The product also fits the
founder's generic instrumentation skills, though that is only 2%.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **FAIL** | Neither Southern Spirit nor PRC-028 is a product-specific order/specification for a merchant wideband DC sensor; no second independent buyer source exists. |
| G2 | **PASS** | The protection/sensing literature is peer-reviewed and eligible. |
| G3 | **PASS_MARGINAL** | $300k is above the preferred range and depends on written 10 kA facility access. |
| G4 | **PASS_MARGINAL** | Incumbents are named and combined bandwidth/accuracy is non-cosmetic in theory, but the difference is unbenchmarked and the merchant socket is absent. |
| G5 | **PASS** | No nonexistent physics; vertical integration is the commercial killer. |
| G6 | **PASS** | US route is possible and China is honestly excluded. Utility qualification remains substantial. |
| G7 | **FAIL** | The dated project is a system trigger, while the cited regulatory deadline is for a different measurement job. No 2030–2034 product procurement/design-in trigger is identified. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | 1 | No sensor order or buyer specification. |
| Frontier/coolness | 4 | 3 | Wideband measurement matters, but it is an incremental component stack. |
| High-end niche | 3 | 2 | Narrow, but the merchant socket may not exist. |
| Competition whitespace | 2 | 1 | LEM and optical/OEM incumbents cover the base functions. |
| Reachable budget | 3 | 2 | Facility and qualification dependencies are understated. |
| Elegance/controllability | 4 | 3 | Bench metrics are controllable; station EMI/insulation/life are coupled. |
| 10x edge | 2 | 1 | No benchmark proves a customer-valued order-of-magnitude improvement. |
| US–China leverage | 2 | 1 | US only; China royalty upside is uncontracted. |
| 2030 window | 3 | 1 | No product-level trigger. |
| Expansion | 3 | 2 | Each adjacent application requires different qualification. |
| Founder transfer | 4 | 4 | No change; capped at 2%. |

Suggested total: **36.0/100**.

### Cheapest decisive falsification

**$20k–$35k, 6 months, commercial socket test.** Before building 10 kA hardware, present a quantified
DC-to-100 kHz requirement/architecture to at least six converter OEMs, EPCs, and protection vendors.
Pass only if one signs a paid evaluation/NRE agreement naming an unbundled sensor interface and
supplies an incumbent performance baseline. Kill if all require the sensor inside their proprietary
station package. This is decisive for the merchant-socket thesis. A cheap 1 kA sensor demo alone is
not decisive and must not count as a sub-$100k first experiment.

**Final verdict: KILL.** It currently fails both demand and timing gates.

## `P3R2-A-13` — modular rad-tolerant GaN PPU

### Strongest bear case

The primary SDA source does not specify electric propulsion or a PPU. It specifies approximately 40
Transport Layer vehicles, optical communication terminals, tactical data links, PNT, and network
management, subject to funding
([SDA T3TLu notice](https://www.sda.mil/sda-requests-industry-feedback-on-tranche-3-transport-layer-upsilon-variant-draft-solicitation/)).
Thruster scarcity is not demand for a separable merchant PPU. The observed buyer response is
vertical integration: York acquired Orbion, and Rocket Lab launched an integrated Hall thruster,
PPU, and propellant-management assembly. Rocket Lab says Gauss uses GaN electronics, is ITAR/EAR-
free, has a production line exceeding 200 thrusters/year, and deliberately removes complex PPU
parameter management
([Rocket Lab Gauss announcement](https://rocketlabcorp.com/updates/rocket-lab-unveils-new-electric-propulsion-satellite-thruster-to-meet-constellation-demand/)).
That directly attacks the proposed merchant module and interface layer.

The technical “extreme edge” is also partly on the market already. EPC Space's current 300 V
rad-hard GaN product claims SEE immunity at LET 83.2 MeV/mg/cm² at 250 V and at LET 63 at 300 V
([EPC7030MSH product page](https://epc.space/products/rad-hard-gan-hemts/epc7030msh/)).
The startup can still engineer a 2–20 kW PPU around such devices, but “survives heavy ions at full
bus voltage” is no longer a unique 10x platform claim. The qualification file, flight heritage,
thermal-vac, EMI, thruster coupling, firmware assurance, parts-lot control, and failure review are
the product. Those are expensive trust and process assets held by primes and established propulsion
vendors.

G7 is worse than marginal. The T3 solicitation was subject to funding and the canonical second
source says the 2026 request zeroed the line and paused solicitations. The independent York/Orbion
event is 2026–2027 behavior, not a 2030–2034 trigger. There is therefore no compliant, funded forward
volume trigger. Export controls further disadvantage a US merchant module against Rocket Lab's
ITAR/EAR-free integrated product, while China is correctly unavailable.

### Disconfirming evidence and steelman

Spacecraft electric propulsion demand and supply stress are real. Standardized PPUs can reduce
program NRE for smaller thruster vendors, and EPC Space's components make a breadboard technically
plausible. A prime or independent thruster company that lacks in-house power electronics could fund
a reusable qualification dossier. The staged SEE-map-first approach is sound, and radiation test
results are measurable. If a paid design partner explicitly accepts an open PPU interface, a narrow
business could survive outside the vertically integrated constellation primes.

### Hard-gate verdicts

| Gate | Verdict | Red-team rationale |
|---|---|---|
| G1 | **FAIL** | SDA's notice does not name EP/PPUs; thruster demand and prime integration do not establish two independent sources for a merchant PPU, including one primary buyer requirement. |
| G2 | **PASS** | Radiation and converter technical claims have eligible peer-reviewed support. |
| G3 | **PASS_MARGINAL** | The $700k system experiment is bounded but outside the preferred range; device SEE tests alone do not validate the PPU. |
| G4 | **PASS_MARGINAL** | Competitors are named and modularity is non-cosmetic, but no buyer accepts the interface and Rocket Lab's integrated GaN PPU is already scaling. |
| G5 | **PASS** | The hardware is physically possible; trust, qualification, and market architecture are the blockers. |
| G6 | **PASS_MARGINAL** | US base case is legal, but ITAR/EAR overhead is a commercial handicap and China is unavailable. |
| G7 | **FAIL** | The only primary forward trigger is paused/unfunded, and the second source is near-term behavior rather than a 2030–2034 trigger. |

### Score adjustment suggestion

| Criterion | P4 raw | Suggested raw | Reason |
|---|---:|---:|---|
| Demonstrated demand | 3 | 1 | No merchant-PPU buyer requirement. |
| Frontier/coolness | 4 | 3 | Rad-hard GaN is compelling but already commercial at device and integrated-system levels. |
| High-end niche | 3 | 1 | Vertical integration leaves few reachable buyers. |
| Competition whitespace | 2 | 0 | Rocket Lab, Rocketdyne, York/Orbion, Busek, and EPC Space surround the product. |
| Reachable budget | 2 | 1 | $700k experiment and $6–15M v1 exceed mission preference; flight heritage remains unfunded. |
| Elegance/controllability | 4 | 3 | SEE/efficiency are measurable; coupled system qualification is not a reusable lab-only step. |
| 10x edge | 3 | 1 | Existing rad-hard devices and integrated GaN PPU erase the unqualified 10x claim. |
| US–China leverage | 1 | 1 | US only, correctly. |
| 2030 window | 3 | 1 | Forward program trigger is absent. |
| Expansion | 3 | 2 | High-voltage buses are plausible only after flight trust is won. |
| Founder transfer | 2 | 2 | No change. |

Suggested total: **29.6/100**.

### Cheapest decisive falsification

The cheapest decisive *business* test is **$25k–$40k**: take a frozen electrical/interface and
qualification-file proposal to at least 12 named US primes and independent thruster vendors. Pass
only if two confirm an unbundled merchant socket and one signs paid NRE or a non-cancellable
qualification partnership. Kill if buyers require vertically integrated propulsion or flight
heritage before NRE. No credible sub-$100k technical experiment is decisive for the claimed product:
device SEE testing does not validate a 2–20 kW flight PPU, thermal-vac/EMI, or qualification-file
acceptance. Do not count this idea toward the portfolio's sub-$100k decisive-experiment quota.

**Final verdict: KILL.** It fails product demand and the 2030 timing gate, while its technical edge
and merchant socket are already converging into incumbent integrated products.

## Group-level adjudication notes

1. **Category demand inflation:** all five P4 scorecards lean to some degree on demand for the host
   system. Only `P3R2-D-02` now has direct evidence of an actual buyer procuring the incumbent
   product category. The other four need product-specific paid evidence.
2. **Sub-$100k quota discipline:** `P3R2-D-02` has a plausible decisive <$100k incumbent benchmark.
   `P3R2-D-13` qualifies only if a prime supplies a binding platform envelope. The cheap tests for
   `P3R2-G-03`, `P3R2-F-06`, and `P3R2-A-13` are commercial socket tests; their cheap technical
   demos are not decisive and should not be relabeled to satisfy portfolio arithmetic.
3. **Citation repairs:** fix the swapped `P3R2-D-13-S02/S03` aliases. Stop calling
   `P3R2-D-02-S02` a company disclosure or procurement-grade source. Do not cite PRC-028 as a
   100 kHz DC sensor mandate.
4. **Geography:** `P3R2-D-02` and `P3R2-G-03` retain possible US+China logic, but neither has a
   current, separately committed Chinese buyer for the proposed new product. `P3R2-F-06` and
   `P3R2-A-13` correctly exclude China; `P3R2-D-13` is correctly US-defense-only. No excluded
   market is used.

## Final verdict lines

- `P3R2-D-02` — **HOLD**, 40% kill probability, suggested 64.0; strongest near-miss, blocked by
  incumbent-gap proof and a compliant official 2028–2035 trigger.
- `P3R2-G-03` — **HOLD**, 75% kill probability, suggested 42.2; do not select until a paid US and/or
  China product-specific pilot closes G1.
- `P3R2-D-13` — **KILL**, 80% kill probability, suggested 47.0; system-mass trade and three incumbent
  positions overwhelm the present scale-only wedge.
- `P3R2-F-06` — **KILL**, 88% kill probability, suggested 36.0; no merchant sensor order and the
  regulatory citation supports a different measurement job.
- `P3R2-A-13` — **KILL**, 92% kill probability, suggested 29.6; merchant PPU demand and the 2030
  trigger fail while integrated rad-hard GaN competitors are already shipping/scaling.
