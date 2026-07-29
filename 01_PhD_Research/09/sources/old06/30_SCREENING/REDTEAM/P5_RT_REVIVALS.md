# P5 fresh adversarial red team — proposed revivals C-09 and F-16

Date: 2026-07-14 (America/Los_Angeles)  
Scope: independent P5 red-team review of `P3R2-C-09` and `P3R2-F-16` under the literal published G1/G4/G6/G7 rules and all eleven weighted criteria. This review read the frozen longlist, P4 scorecards/evidence, the strict China/G7 audit, and `P5_CN_DEFICIENCY_REGEN_PROPOSAL.json`, then independently checked the new proposal sources and searched for adverse evidence. It does **not** require a future purchase order for a startup product that does not yet exist. It does require two independent present demand sources, including one primary buyer/procurement/filing, and two forward-timing sources, including one primary/official 2028–2035 trigger.

## Executive disposition

| Idea | Proposed score | Hard-gate result | China beachhead countable now? | Disposition | Subjective probability thesis is killed by 2034 |
|---|---:|---|---|---|---:|
| `P3R2-C-09` | **52.2/100** | **G7 FAIL**; G1/G3/G4/G6 marginal | **No** | **KILL** for reinstatement; retain only as a watchlist concept | **78%** |
| `P3R2-F-16` | **48.2/100** | **G4 FAIL; G7 FAIL**; G3/G6 marginal | **No** | **KILL** for reinstatement; a narrower sensor-only wedge may be regenerated later | **83%** |

Neither proposed revival is selection-ready. The arithmetic need for two additional China flags is not evidence and must not change a gate verdict.

## `P3R2-C-09` — interoperable solid-state pulsed-power bricks

### Gate table

| Gate | Verdict | Adversarial finding |
|---|---|---|
| G1 | **PASS_MARGINAL** | Varex/IBA filings, China accelerator-system procurement, and CEPC RF-system design establish present spending on beam/RF systems. That is enough under the literal category-demand rule even though no buyer has ordered the proposed open brick. Demand for a merchant, cross-integrator brick remains an inference and is scored down. |
| G2 | **PASS** | The physical mechanisms are supported by final peer-reviewed accelerator/modulator work. The new CEPC RF article is a final 2025 journal article. No preprint-only claim is needed for the gate. |
| G3 | **PASS_MARGINAL** | A 12-month, $220k two-brick test is bounded and has droop, jitter, fault, interchangeability, life, and swap-time thresholds. It does not test multi-vendor interoperability, qualification burden, export partitioning, or willingness to adopt an open interface. Frozen v1 capital remains $6M–$15M, above the preferred sub-$5M path. |
| G4 | **PASS_MARGINAL** | ScandiNova, JEMA, CPI/Continental, IHEP/HEPS, and domestic integrators are named. A genuinely cross-vendor open interface would be non-cosmetic, but modularity, redundancy, feedback control, easy service, and even sub-five-minute module replacement already exist in incumbent offerings. The residual distinction is standards adoption, not modular hardware. |
| G5 | **PASS** | Solid-state pulse modulators and active control are established physics; the proposed brick can be falsified without a top-down market forecast. |
| G6 | **PASS_MARGINAL, CHINA NOT COUNTABLE** | Removing CGN and keeping controlled/high-energy variants US-only is a material repair. However, “PRC-registered, locally manufactured, independently developed” is a proposed corporate architecture, not a demonstrated route. No named civilian PRC integrator has agreed to qualify the brick, and prior IHEP procurement required PRC-origin products. Count China only after counsel, end-use screening, domestic-origin qualification, and a named integrator agreement. |
| G7 | **FAIL** | The proposal relies on a superseded 2023 CEPC schedule. The CEPC team’s December 2025 update says the proposal was **not selected** for the 15th Five-Year Plan and would be prepared for application during the 16th plan; a final 2026 peer-reviewed status paper says the government application is now planned for **2030**, with construction during 2030–2035. That is not the proposal’s claimed continuing 2026–2035 construction/procurement cycle. CEPC remains a conditional project application, not a committed 2030 customer procurement trigger for merchant bricks. CSNS-II completion in 2029 is an independent project date but does not name a merchant modulator procurement or external qualification socket. |

### Source-specific findings

- **Factual support — current category demand:** the existing Varex/IBA and China system sources are sufficient for literal G1 at the host-system level. The new CEPC RF-source article confirms RF power is a required subsystem and documents mature prototypes; it is technical/category linkage, not buyer demand for an open brick.
- **Factual support — CEPC bill of system:** the official CEPC cost-review report separately states that collider RF uses 96 650 MHz, 800 kW klystrons. The proposal attributes “96 sets” to `P5-CNREGEN-S02`, but the cited slide’s extract says only that three klystron prototypes were developed and the PSM was developed with industrial collaboration. The quantity is real in another CEPC document, but the proposed locator is wrong. In any case, 96 klystrons do not imply 96 externally purchased interoperable 3 kV bricks.
- **Factual adverse timing:** the [December 2025 IHEP update](https://indico.ihep.ac.cn/event/27681/contributions/209044/attachments/98529/130963/20251212-19TeV-Workshop-CEPC-Beijing.pdf) says CEPC was not selected by CAS in 2025 and would prepare an application for construction during the 16th Five-Year Plan. The final April 2026 journal version, DOI [`10.1142/S0217751X26410010`](https://doi.org/10.1142/S0217751X26410010), says EDR completes in 2027 and the proposal application is planned for 2030. These later sources supersede the 2023 IHEP announcement used as `P5-CNREGEN-S01` for the claimed 15th-plan construction start.
- **Factual adverse competition:** [ScandiNova](https://scandinovasystems.com/technology/) already markets solid-state pulse control, feedback, reliability, and proprietary complete-system technology; its current product guide calls the architecture modular. [JEMA](https://www.jema-power.com/range/radio-frequency-amplifiers/) markets modular redundant RF power systems with module replacement in under five minutes, and its accelerator modulator is already described as modular/scalable. [IHEP’s HEPS result](https://lssf.cas.cn/sszs/ggsy/gntbfsgy/xwdt/202210/t20221024_5058228.html) demonstrates a domestically developed 315 kV/380 A, 120 MW solid-state modulator at international-comparable performance, with a local firm supporting manufacture/process improvement.
- **Factual metadata defect:** `P5-CNREGEN-S04` is an accelerator/CSNS-II source used by C-09, but the proposal’s ledger-ready metadata assigns it to lane `L01` and idea `P3R2-F-16`. It must be corrected to the accelerator lane/idea before any ledger merge.
- **Inference:** a cross-vendor acceptance standard could reduce integration and service cost. No fetched buyer source says OEMs will cede their proprietary interface, accept third-party bricks, or value interchangeability enough to bear requalification risk.

### Weighted score

| Criterion | Weight | Raw 0–5 | Weighted | Reason |
|---|---:|---:|---:|---|
| Demonstrated demand | 16 | 3 | 9.6 | Real beam/RF system spend; no merchant-brick pull. |
| Frontier/coolness and vision | 15 | 4 | 12.0 | Catalog pulsed power is a strong platform vision. |
| High-end niche quality | 10 | 3 | 6.0 | Valuable buyers, but highly concentrated and qualification-heavy. |
| Competition whitespace | 9 | 1 | 1.8 | Incumbents already own modularity, feedback, service, and domestic manufacture; only cross-vendor standard adoption remains. |
| Reachable validation budget | 9 | 2 | 3.6 | $220k test is bounded; v1 remains $6M–$15M and commercial qualification is not tested. |
| Technical elegance/controllability | 11 | 4 | 8.8 | Pulse/fault/life variables are directly measurable. |
| 10x technical edge | 7 | 1 | 1.4 | No buyer benchmark supports 10x; JEMA already claims module replacement in under five minutes. |
| US–China dual-market leverage | 10 | 2 | 4.0 | US leg plausible; China route conditional and not quota-countable. |
| 2030 launch-window fit | 8 | 1 | 1.6 | Latest evidence moves CEPC to a 2030 application, not committed procurement. |
| Expansion economics | 3 | 3 | 1.8 | Several beam/pulsed-power adjacencies exist if the interface wins. |
| Founder skill transfer | 2 | 4 | 1.6 | Controls/interfaces transfer; HV insulation, certification, and China structure require specialists. |
| **Total** | **100** |  | **52.2** | Plausible technology, failed timing thesis. |

Score range: **43–60**. Confidence: **medium-high** on the kill decision because the adverse CEPC schedule is newer than the repair’s load-bearing timing source.

### Kill probabilities and explicit revival conditions

Subjective, non-additive risk estimates: 75% that CEPC/China is not a reachable paid design-in by end-2029; 70% that system vendors or IHEP-affiliated suppliers absorb/block the socket; 65% that an open standard fails to gain two OEM adopters; 78% overall commercial kill by 2034.

Reconsider only after **all** of the following exist:

1. A government/project approval or funded procurement schedule, not merely a 2030 application, explicitly covering 2030–2034 RF-power-system qualification or production.
2. A named, independently reachable PRC civilian integrator signs a paid evaluation/design-in and clears origin, end-use, and export counsel; no CGN-group base case.
3. Two OEMs accept the same open electrical/mechanical/control interface and agree that a third-party brick can be requalified without full-system redesign.
4. The decisive experiment demonstrates cross-vendor interchangeability, not only swapping two startup-built bricks, and benchmarks service/qualification time against ScandiNova/JEMA/IHEP baselines.
5. A capital plan brings the first sellable wedge plausibly below $5M or documents committed non-dilutive/customer funding.

## `P3R2-F-16` — closed-loop plasma surface-treatment cell

### Gate table

| Gate | Verdict | Adversarial finding |
|---|---|---|
| G1 | **PASS** | Wuxi Shennan and Guangzhou Guangxin are independent named buyers running exact-category plasma-cleaner tenders, one on the MOFCOM-supervised international-bidding portal. Literal G1 does not require them to have ordered a future metrology feature. Demand score remains 3 because neither tender values or specifies the premium feature. |
| G2 | **PASS** | The two new final journal papers support OES monitoring of plasma chemistry/uniformity/abnormality. They do **not** demonstrate that OES predicts post-treatment substrate surface state or downstream bond/underfill outcomes at production rate; the proposal correctly leaves that to experiment. |
| G3 | **PASS_MARGINAL** | The $95k, 9–12 month partner-lab test has useful held-out thresholds and can kill proxy robustness. “Simulated line rate” is not a production-line qualification, and obtaining a paid China beta is a customer-development milestone outside the lab experiment’s direct control and likely outside its stated budget. |
| G4 | **FAIL** | The regeneration says direct on-substrate verification is the residual whitespace. Plasmatreat and KRÜSS publicly demonstrated an integrated, automated Plasma Treatment Unit with contact-angle measurement before and after treatment in 2024, providing continuous wettability QC and synchronized documentation. Plasmatreat already offers comprehensive inline plasma parameter monitoring. Thus the proposed surface-state-measurement layer is not whitespace. The remaining “close the recipe loop” software is readily absorbable unless the product is narrowed to a demonstrably superior non-contact, no-liquid, line-rate predictor with protected data/IP. |
| G5 | **PASS** | Plasma treatment and OES monitoring are established; the key inference is experimentally falsifiable. |
| G6 | **PASS_MARGINAL** | Two international-open tenders demonstrate a legally reachable category channel. However, advanced-packaging equipment classification, restricted-party/end-use screening, local service, data localization, and any US-origin sensor/software content still require current counsel. No structural prohibition is shown, so this is not a hard fail. |
| G7 | **FAIL** | The JCET filing is one valid primary 2028 customer-system trigger, but not a plasma-cleaner order: it says phase-one facilities and production equipment complete in H2 2028; product mix/capacity are undisclosed and phase-two timing is dynamic. This can pull equipment procurement **before** a 2030 company launch. The two 2025–2026 tenders and 2019 MIIT catalogue are current/historical category evidence, not a second independent 2030-timing source. No second explicit forward timing source survives, and no source establishes a 2030–2034 metrology-bearing ramp. |

### Source-specific findings

- **Factual support — G1 and reachability:** the [MOFCOM portal notice](https://chinabidding.mofcom.gov.cn/bidDetail/bidding/bulletin/202603/ff8080819a82040b019cfb23570d6ed2.html) names Guangzhou Guangxin Packaging Substrate, an international-open retender for a plasma cleaner, and eligibility for legal persons from China or normal-trade countries/regions. Together with the independent Wuxi Shennan tender, category demand passes. The new proposal’s canonical key is wrong: the official page shows project `0730-264010SZ0023/11`, not `0730-254010SZ0149`. The record also appears to be another notice/lot in the already researched Guangzhou project and must be deduped against `P3R2-F-16-S01`; independence from Wuxi remains intact.
- **Factual support — one forward trigger only:** the [SSE-hosted JCET account](https://english.sse.com.cn/news/newsrelease/voice/c/c_20260629_10823788.shtml) confirms CNY7.8B investment and H2-2028 completion of first-phase facilities/equipment. It also says product mix and planned capacity were not disclosed and second-phase timing will be dynamically adjusted. Linking some of that capex to plasma cleaning is reasonable category inference, not stated procurement.
- **Factual adverse competition:** Plasmatreat’s official 2024 announcement describes [integrated automated contact-angle measurement](https://www.plasmatreat.com/de/neuigkeiten-und-geschichten/aktuelles-und-presse/detail/pr-umweltfreundlich-und-inlinefaehig-plasmavorbehandlung-fuer-effiziente-und-langlebige-batterien) in its Plasma Treatment Unit, with before/after robot measurement and continuous wettability quality control in seconds. Its current [process-monitoring product](https://www.plasmatreat.com.tr/en/products-and-services/openair-plasmar-process-monitoring) already monitors plasma light, power, movement, pressure, and deviations. This directly contradicts the proposal’s claim that direct surface-state verification is unoccupied, even though the 2024 demo is not proof of an advanced-packaging production install.
- **Factual technical limitation:** DOI [`10.1016/j.rcim.2018.02.003`](https://doi.org/10.1016/j.rcim.2018.02.003) detects plasma uniformity and abnormalities from OES. DOI [`10.1109/TPS.2011.2123111`](https://doi.org/10.1109/TPS.2011.2123111) monitors chemical reactions during polypropylene plasma treatment. Neither source validates a universal proxy across PCB/packaging materials, contaminants, bond chemistries, or line rates. The proposed cross-material R² and false-reject thresholds are experimental aspirations.
- **Factual timing weakness:** `P5-CNREGEN-S11` is a 2019 first-set-equipment catalogue. It is explicitly not a timing source. An independently checked 2024 edition does not return an inline plasma-cleaner entry; absence is not proof of policy withdrawal, but it prevents treating the 2019 item as a durable 2030 forcing function.
- **Inference:** an OES-derived, non-contact surface-state predictor with closed-loop recipe correction could still outperform droplet/contact-angle QC for high-throughput packaging. No current source proves that performance, that it avoids contamination, or that a buyer will pay a premium after incumbent integration.

### Weighted score

| Criterion | Weight | Raw 0–5 | Weighted | Reason |
|---|---:|---:|---:|---|
| Demonstrated demand | 16 | 3 | 9.6 | Two exact-category procurements; zero premium-feature procurement. |
| Frontier/coolness and vision | 15 | 2 | 6.0 | Treat-to-spec is attractive, but integrated surface QC was already demonstrated by an incumbent in 2024. |
| High-end niche quality | 10 | 3 | 6.0 | Valuable packaging lines; willingness to pay and service access unproven. |
| Competition whitespace | 9 | 1 | 1.8 | Plasmatreat/KRÜSS already cover direct surface QC; other global/CN tool vendors can absorb feedback software. |
| Reachable validation budget | 9 | 4 | 7.2 | $95k bench/partner test is attractive; beta/production qualification is excluded. |
| Technical elegance/controllability | 11 | 3 | 6.6 | Measurable and falsifiable, but mapping OES to substrate/bond outcomes is confounded across materials. |
| 10x technical edge | 7 | 1 | 1.4 | No 10x result or incumbent benchmark exists. |
| US–China dual-market leverage | 10 | 2 | 4.0 | A reachable China-only category; no US leg claimed. |
| 2030 launch-window fit | 8 | 2 | 3.2 | One H2-2028 factory trigger; no second forward source and procurement may precede launch. |
| Expansion economics | 3 | 2 | 1.2 | Sensor/control layer could expand, but incumbents own the installed tool channel. |
| Founder skill transfer | 2 | 3 | 1.2 | Instrumentation/control transfer; plasma chemistry and China field service require partners. |
| **Total** | **100** |  | **48.2** | Cheap experiment, failed whitespace and timing gates. |

Score range: **40–57**. Confidence: **high** that the present record cannot pass G4/G7; medium on the long-run technical opportunity because a narrower non-contact sensor could still emerge.

### Kill probabilities and explicit revival conditions

Subjective, non-additive risk estimates: 80% incumbent absorption by 2030; 65% no paid premium commitment; 55% proxy robustness failure across real contaminants/materials; 60% JCET/other capacity procurement occurs before a 2030 startup can qualify; 83% overall commercial kill by 2034.

Reconsider only after **all** of the following exist:

1. Narrow the product to a non-contact, no-liquid, line-rate substrate-state predictor demonstrably unavailable from Plasmatreat/KRÜSS/Nordson/Surfx/CN vendors; complete patent/prior-art and roadmap review.
2. Obtain a paid beta or conditional order whose line item explicitly prices metrology/traceability, not merely a commodity plasma cleaner.
3. Produce blinded production-line data over at least three real substrate/contaminant/bond families, including held-out downstream bond/underfill outcomes and cycle-time/false-reject cost.
4. Add a second independent forward timing source and one named 2030–2034 packaging-line qualification/procurement trigger; do not count an unspecified 2028 factory or 2019 catalogue twice.
5. Classify the exact equipment/sensors/software and clear the buyer, end use, servicing route, and local-data architecture before counting China.

## Factual support, inference, and geography/origin audit

- Factual statements above are tied to fetched official institute/project pages, exchange/filing material, buyer procurement, final journal records, or incumbent primary pages. Search snippets were used to locate sources, not as sole final support where a fetched page was available.
- Inference is explicitly labeled. The strongest inferences are: host-system spending can support a merchant component category; JCET’s general equipment capex includes plasma cleaning; and technical prototypes can become externally purchasable sockets. None is treated as a purchase order.
- The new-source origin audit contains no India-origin or Singapore-origin evidence. `P5-CNREGEN-S08` resolves to Croatia/Slovenia and `S09` to South Korea; both are technical publications only. South Korea is not used as a substitute market. India and Singapore do not appear as buyers, beachheads, market-size inputs, competitors, or routes.
- China is the only claimed market for F-16 and one of two claimed markets for C-09. No generic “Asia” substitution is used. The adverse verdicts therefore cannot be repaired by optional Japan/Taiwan/South Korea demand.

## Final red-team judgment

`P3R2-C-09` has real physics and host-system demand, but the load-bearing CEPC schedule in the repair was stale when compared with the project team’s later 2025–2026 record. Its China leg is a conditional 2030 application plus an uncontracted local-entity theory, not a countable 2030 beachhead.

`P3R2-F-16` has the better cheap experiment and cleaner China procurement route. It nevertheless fails the current revival because its claimed residual whitespace was demonstrated by Plasmatreat/KRÜSS in 2024, and JCET supplies only one broad 2028 factory trigger whose procurement may occur before launch. A sensor-only regeneration may be worth doing, but the present tool concept cannot be reinstated honestly.
