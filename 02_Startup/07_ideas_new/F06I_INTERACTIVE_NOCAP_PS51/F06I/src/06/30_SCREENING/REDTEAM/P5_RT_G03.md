# P5 red-team G03 — adversarial review of five P4 survivors

Date: 2026-07-13  
Scope: `P3R2-A-14`, `P3R2-G-01`, `P3R2-C-08`, `P3R2-E-02`, `P3R2-D-16`  
Routing note: supporting lane requested Terra/high; actual runtime model and effort are unavailable and therefore **unknown**, not inferred.  
Independence: this report proposes changes only. It does not modify the authoritative P4 scores or gates.

## Executive verdict

The common defect is substitution of **program-level spending for product-level demand**. All five ideas attach to real programs, but only `P3R2-C-08` has direct evidence that buyers already purchase the same component category. Even there, the evidence also reveals a mature, ASME-capable incumbent that already designs sCO2 PCHEs and works on fatigue life. Two ideas fail G1 under a product-specific reading; four fail G4 because the proposed whitespace is either already embedded in incumbent systems or is a business-model assertion rather than a technical difference.

| Idea | P4 score | Red-team score suggestion | Kill probability | Gate changes proposed | Verdict |
|---|---:|---:|---:|---|---|
| `P3R2-A-14` | 70.4 | 54.6 | 50% | G1/G3/G4/G5/G7 to marginal | **HOLD** |
| `P3R2-G-01` | 65.6 | 41.0 | 82% | G1 fail; G4 fail; G3/G6/G7 marginal | **KILL** |
| `P3R2-C-08` | 62.2 | 48.2 | 78% | G4 fail; G1/G3/G5/G6 marginal | **KILL** |
| `P3R2-E-02` | 59.6 | 41.8 | 84% | G1 fail; G4 fail; G7 fail | **KILL** as a standalone company; retain only as a feature candidate |
| `P3R2-D-16` | 56.2 | 36.4 | 88% | G4 fail; G1/G3/G5/G7 marginal | **KILL** from the final 24; retain a zero-capex watch option |

The suggested totals apply the published weights to the raw-score changes shown below. They are not claimed as authoritative.

---

## `P3R2-A-14` — 300°C-class mixed-signal SiC/SOI instrumentation platform

### Strongest bear case

The idea is trying to create a semiconductor platform without first controlling a reproducible semiconductor process. CISSOID's official discontinuation notice says X-FAB ended the XI10 process and that **no equivalent process was available**; this is evidence of supply-chain fragility, but also evidence that the prior niche could not command durable foundry support ([CISSOID discontinuation notice](https://www.cissoid.com/download/file/241001-discontinuation-notification-letter-high-temperature-process-pdf-5350); local `P3R2-A-14-S04`). A startup that cannot name a foundry, PDK, MPW cadence, minimum wafer commitment, second source, and ownership of the high-temperature models has no build path to a qualified platform.

The demand record is adjacent rather than product-specific. Baker Hughes/XGS, SLB-Ormat, and SUPERHOT prove expenditure on geothermal wells and reservoir/well-construction R&D; they do not show a purchase specification, tender, LOI, NRE payment, or design-in for a merchant 300°C chipset. The current [ARPA-E SUPERHOT program](https://arpa-e.energy.gov/programs-and-initiatives/view-all-programs/superhot) describes well construction, materials, test facilities, and heat extraction; it does not procure mixed-signal electronics. The best direct bridge is older DOE funding: DOE funded GE to design and test a 300°C MEMS gyroscope with SOI electronics ([DOE award record](https://www.energy.gov/nepa/articles/cx-101320-mems-gyroscope-reliable-long-duration-measurement-while-drilling-300degc)), and DOE still states that electronics above 225°C are limited and needed ([DOE subsurface-accessibility roadmap](https://www.energy.gov/hgeo/geothermal/subsurface-accessibility)). This supports a technical need and grant market, but not yet a 2030 merchant-platform purchase.

The wedge is also less empty than P4 implies. A peer-reviewed 2022 paper reports a 300°C SOI-CMOS sensor-electronics chipset with analog front end, sigma-delta conversion, interface electronics, and a microcontroller in development ([final journal article](https://imapsjmep.org/article/37444-a-high-temperature-soi-cmos-chipset-focusing-sensor-electronics-for-operating-temperatures-up-to-300c)). GE demonstrated an integrated 300°C navigation system, and the DOE corpus shows two decades of high-temperature-electronics programs. The market failure may therefore be qualification economics and low volume, not missing circuit physics.

The $850k first experiment and $8–18M v1 exceed the mission preference. A successful 1,000-hour eight-channel soak would still not establish foundry continuity, yield, long-term passives, pressure-vessel feedthroughs, field reliability, or a customer design-in. Meanwhile Baker Hughes, SLB, Halliburton, GE, and specialist tool vendors can vertically integrate a narrow set of electronics or use thermal isolation, flasks, duty cycling, and fiber sensing rather than buy a broad platform.

### Disconfirming evidence and steelman

The pain itself is unusually well supported. CISSOID/Honeywell exits are real; DOE explicitly identifies the lack of components above 225°C; DOE has previously funded 300°C electronics; and SUPERHOT targets reservoirs above 375°C. The physics is demonstrated, test endpoints are quantitative, and a qualified merchant module could amortize rare packaging and reliability work across several tool OEMs. This is why the idea merits HOLD rather than immediate elimination.

The steelman succeeds only if the company begins as a **qualified module/NRE supplier on an already-accessible process**, not as a broad merchant IC platform. Foundry access and two paid customer programs must precede custom silicon.

### Hard-gate verdicts

| Gate | Red-team verdict | Reason |
|---|---|---|
| G1 | **pass_marginal** | DOE funded a directly relevant 300°C electronics project and documents the need, but 2025–2026 geothermal projects do not yet name this merchant product. Require two independent paid evaluation/NRE commitments, including one tool OEM. |
| G2 | **pass** | The technical mechanism is supported by eligible peer-reviewed and government records. |
| G3 | **pass_marginal** | The experiment is bounded, but $850k is 3.4× the top of the preferred band and does not resolve foundry continuity. |
| G4 | **pass_marginal** | A qualified 300°C merchant module is non-cosmetic, but the comparison must include GE's demonstrated chipset/system work and the 2022 300°C SOI-CMOS chipset, not only discontinued catalog vendors. |
| G5 | **pass_marginal** | Physics exists, but the plan currently depends on an unnamed high-temperature process and $8–18M before v1. |
| G6 | **pass** | No prohibited cross-border route is the base case; industrial qualification and any dual-use review remain manageable. |
| G7 | **pass_marginal** | The 2030 geothermal trigger is credible, but no 2030–2034 electronics procurement/design-in is yet documented and a platform qualification cycle must start before company launch. |

### Score adjustments proposed

| Criterion | Raw P4 → proposed | Basis |
|---|---:|---|
| Demonstrated demand | 4 → **3** | Strong adjacent spending; product-specific purchase intent absent. |
| High-end niche quality | 4 → **3** | Valuable but small; tool majors may internalize and use alternative thermal architectures. |
| Competition whitespace | 4 → **2** | Catalog exit is real, but GE/DOE and current 300°C SOI work show active substitutes and long-standing R&D. |
| Reachable validation budget | 2 → **1** | $850k decisive campaign and $8–18M v1. |
| Technical elegance/controllability | 4 → **3** | Bench metrics are clean; foundry/process/package transfer is not. |
| 10× technical edge | 3 → **2** | 300°C capability is large, but not yet linked to a 10× buyer-valued cost, uptime, or well-output metric. |
| 2030 launch-window fit | 4 → **3** | Dated projects exist; the product design-in trigger is inferred. |

Other raw scores unchanged. Suggested weighted total: **54.6**.

### Cheapest decisive falsification experiment

There is **no honest sub-$100k positive validation** of the complete company thesis. A sub-$100k veto test is possible: spend at most **$75k over 12 weeks** to obtain (1) a written PDK/MPW/wafer-supply offer covering 300°C models and 2028–2034 continuity; (2) two conditional paid evaluation or NRE letters from independent tool OEMs; and (3) an N≥20 package-coupon campaign at 300°C/500 thermal cycles using known-good die with prespecified resistance, leakage, hermeticity, and drift limits. Any missing foundry commitment, fewer than two paid customer commitments, or >10% coupon failure kills the platform. Passing only licenses the $850k mixed-signal soak; it should **not** be counted as a sub-$100k decisive first experiment for portfolio quota purposes.

**Final verdict: HOLD.** Advance only after foundry continuity and two paid product-level commitments; otherwise kill by end-2028.

---

## `P3R2-G-01` — closed-loop UHV conditioning and acceptance certification for China fabricators

### Strongest bear case

The evidence proves demand for vacuum chambers and acceptance performance, not demand for a separately purchased conditioning-and-certification island. The P4 dossier concedes that no hydrogen-outgassing or bakeout-endpoint clause was fetched. NIM's [comparison-method vacuum standard](https://www.nim.ac.cn/measurement_standard/606) establishes traceability infrastructure, not a customer. BEST's RMB209M chamber award (`P3R2-G-01-S02`) establishes chamber fabrication, not endpoint-control procurement.

Primary Chinese sources make the substitution risk worse. An ASIPP tender already specifies ultimate vacuum and total leak-rate acceptance, allows the bidder to propose an alternative approved leak-test method, forbids subcontracting the chamber body, and requires ongoing maintenance ([ASIPP tender](https://www.ipp.cas.cn/ztbxx/zbxx/201911/t20191122_364430.html)). A 2025 ASIPP procurement specifies per-weld and total leak-rate thresholds plus post-acceptance service ([ASIPP specification PDF](https://www.ipp.cas.cn/ztbxx/xjxx/202509/P020250928383609787017.pdf)). ASIPP and external fabricators have also delivered a >1,000 m³ ITER test cryostat that passed vacuum and helium-leak acceptance on the first attempt ([ASIPP completion record](https://www.ipp.cas.cn/xwdt/tpxw/202507/t20250728_636699.html)). HEPS reports all 16 front-end units completed bakeout and passed final contract acceptance, reaching better than 2.7×10⁻⁸ Pa ([HEPS acceptance record](https://www.ccnta.cn/article/18255.html)). These records show that institute/fabricator teams already own the acceptance job and can execute it.

The startup therefore asks a small number of sophisticated fabricators to outsource a process they already perform, while exposing the endpoint recipe and calibration know-how to the same customers. No named China furnace maker, fabricator QA platform, or institute-built bench is compared feature by feature. “No single vendor bundles it” is not whitespace when the customer already integrates the bundle internally. The P4 TAM of roughly $3–14M cumulative through the early 2030s is an assumption based on 3–8% of chamber contract value, not a sourced purchasing ratio. It is likely too small for a China-localized hardware, calibration, and field-service organization with $3–8M v1 capital.

The geography model adds structural execution risk: a foreign founder cannot bid directly and proposes a licensed China entity while retaining models/standards. Even without a named sanctions blocker, procurement access, cybersecurity/data treatment, calibration liability, IP absorption, and on-site service are central rather than peripheral. A China-only thesis gives no independent US hedge.

### Disconfirming evidence and steelman

The chamber programs are real. BEST is independent of CEPC, acceptance thresholds are explicit, NIM supplies an authoritative traceability anchor, and conditioning endpoints are measurable. A portable retrofit that shortens bakeout while producing a tender-accepted dossier could create real value for a mid-sized fabricator that lacks an institute-grade team. The equipment-plus-recurring-calibration architecture is more defensible than selling a one-time recipe.

The steelman still requires a primary customer document naming outgassing/bakeout responsibility and a paid fabricator pilot. Neither is present. Current evidence supports a customer-discovery hypothesis, not G1.

### Hard-gate verdicts

| Gate | Red-team verdict | Reason |
|---|---|---|
| G1 | **fail** | Multiple chamber programs exist, but no primary buyer/procurement/filing requests the proposed endpoint-control/certification product or even a hydrogen-outgassing acceptance deliverable. |
| G2 | **pass** | Technical claims use eligible vacuum literature; no unreviewed paper is load-bearing. |
| G3 | **pass_marginal** | The N=10 experiment is bounded but costs $300k and assumes access to representative chambers and traceable metrology. |
| G4 | **fail** | The record does not name and benchmark Chinese furnace/QA integrators or institute/fabricator internal systems; primary evidence shows those internal systems already deliver the acceptance outcome. |
| G5 | **pass** | Physics is established and no single market forecast is necessary to test it. |
| G6 | **pass_marginal** | No named prohibited counterparty is established, but the China-local entity, retained-model/IP split, data access, and service obligations are unresolved base-case dependencies. |
| G7 | **pass_marginal** | BEST supports a 2030 facility timeline, but the proposed product's post-2030 order cadence and design-in path remain inferred; CEPC is explicitly delayed/contingent. |

### Score adjustments proposed

| Criterion | Raw P4 → proposed | Basis |
|---|---:|---|
| Demonstrated demand | 3 → **1** | Chamber procurement is not product procurement. |
| Frontier/coolness | 4 → **3** | Elegant outcome control, but primarily industrial process integration. |
| High-end niche quality | 4 → **2** | Very small, lumpy buyer set with direct in-house capability. |
| Competition whitespace | 3 → **1** | Internal fabrication/acceptance teams are the closest substitute and already pass acceptance. |
| Reachable validation budget | 3 → **2** | $300k first test; v1 can exceed $5M and carries local service cost. |
| Technical elegance/controllability | 4 → **3** | Endpoints are measurable; model transfer across chamber history/materials is difficult. |
| 10× technical edge | 3 → **2** | The claimed 30% cycle-time cut is not 10× and has not been tied to contract value. |
| 2030 launch-window fit | 3 → **2** | Facility timing exists; product timing does not. |
| Expansion economics | 3 → **2** | Expansion repeats the same access/service problem across a small number of programs. |

Other raw scores unchanged. Suggested weighted total: **41.0**.

### Cheapest decisive falsification experiment

A genuinely decisive sub-$100k route exists only with a host fabricator contributing its furnace and chamber. Cap spend at **$90k**: first require two independent China-registered fabricators to place refundable **paid** pilot deposits against a prespecified acceptance dossier; then retrofit portable RGA/rate-of-rise/throughput instrumentation to one host's existing furnace and run randomized paired coupons or subassemblies against its fixed recipe. Pass requires ≥30% median cycle-time reduction, no worse final outgassing/leak result, ≤20% agreement with the traceable reference method, and written acceptance of the generated dossier by the procuring institute's QA representative. Fewer than two paid deposits, no host access, or refusal of the dossier kills the product. A lab-only bakeout demonstration without paid fabricator and institute acceptance is not decisive and must not count toward the sub-$100k portfolio quota.

**Final verdict: KILL.** G1 and G4 fail on current evidence. Reopen only after primary product-level procurement evidence and the paid host test above.

---

## `P3R2-C-08` — rapid-transient-tolerant printed-circuit heat exchangers

### Strongest bear case

The proposed whitespace is already inside the incumbent's competence. VPE publicly offers custom diffusion-bonded PCHE/MCHE design for sCO2 Brayton cycles, hydrogen precooling, waste heat, and extreme pressure/temperature service, with ISO 9001 and an ASME U stamp ([VPE product page](https://www.vpei.com/diffusion-bonded-microchannel-heat-exchangers/)). It fabricated a **5.7 MW sCO2 recuperator** by 2017 ([VPE sCO2 record](https://www.vpei.com/2017/07/18/2017-asme-turbo-expo/)), tested a subscale unit at 500°C and 17 MPa and designed 1 MWth and 200 MWth systems ([VPE Gen3 CSP work](https://www.vpei.com/2021/05/26/next-gen-csp-plant/)), and partnered with Sandia specifically on compact heat-exchanger fatigue-life simulations ([VPE fatigue-life program](https://www.vpei.com/2018/01/29/research-improve-the-mechanical-life-of-heat-exchangers/)). P4's assertion that rapid-transient qualification is open rests on not finding a public incumbent specification, not on evidence that VPE or Heatric cannot meet it.

The demand case proves sCO2 projects, not a need for a new merchant core vendor. STEP, Chaotan One, and the 2028 CNNC project are real, but CNNC/CAS-IET can source internally and US programs already work with VPE/Heatric-class suppliers. The concept has no buyer letter stating that an incumbent failed the transient requirement, no RFQ with the proposed ramp/life target, and no price/lead-time pain. A missing public datasheet is unsurprising for custom pressure equipment.

The economics are badly mismatched to the mission. The first meaningful core test is $600k; v1 is $15–35M; full qualification couples diffusion bonding, alloy selection, creep-fatigue, corrosion, NDE, pressure-code work, headers, maldistribution, and long-life extrapolation. A 1,000-cycle subscale result is not a 20-year lifetime demonstration. The proposed edge is not 10× on any sourced customer-valued metric, and a startup would compete on the incumbents' strongest dimensions: manufacturing process control, code documentation, installed references, and ability to warranty pressure equipment.

The US/CN dual-market score also overstates leverage. The US nuclear-qualified line and China industrial-waste-heat line require separate entities, qualification evidence, counterparties, and possibly alloys/design files. China demand is real, but merchant sourcing is unproved and the RMB100B TAM remains explicitly unusable.

### Disconfirming evidence and steelman

PCHE demand is more direct than the other four ideas: actual sCO2 plants require recuperators, VPE has delivered them, STEP operates, and China has a commercial reference plant plus a dated follow-on. Thermal cycling and code qualification are real bottlenecks, and a compliant-header/graded-channel design could be a genuine innovation if it materially extends life.

The steelman is not a new full-stack PCHE manufacturer. It is a customer-funded IP/design-and-qualification program licensed to an established diffusion-bonding manufacturer. That narrower model still needs a sourced incumbent gap and a paid development agreement before inclusion in the final 24.

### Hard-gate verdicts

| Gate | Red-team verdict | Reason |
|---|---|---|
| G1 | **pass_marginal** | Buyers purchase PCHE-class equipment and multiple sCO2 projects exist, but no RFQ or buyer source demands the proposed rapid-transient product from a new merchant vendor. |
| G2 | **pass** | Technical claims rest on eligible peer-reviewed and national-lab sources. |
| G3 | **pass_marginal** | The campaign is bounded but $600k and dependent on specialist manufacturing/test access. |
| G4 | **fail** | VPE already designs, fabricates, code-certifies, and studies fatigue life in sCO2 PCHEs; the record does not prove a non-cosmetic performance gap relative to VPE/Heatric. |
| G5 | **pass_marginal** | Physics is real, but the path requires $15–35M and subscale-to-life extrapolation before a sellable warranted core. |
| G6 | **pass_marginal** | US nuclear and China industrial products are separable in principle, but technology/data/entity separation and CNNC-linked diligence are uncosted. |
| G7 | **pass** | Operating projects and a dated 2028 China trigger make the category window credible through 2030. |

### Score adjustments proposed

| Criterion | Raw P4 → proposed | Basis |
|---|---:|---|
| Demonstrated demand | 4 → **3** | Category demand is real; buyer pain with current PCHE vendors is not. |
| High-end niche quality | 4 → **3** | Valuable but capital-heavy and controlled by qualified incumbents/OEMs. |
| Competition whitespace | 2 → **0** | No proved gap versus VPE/Heatric; VPE already covers sCO2, custom design, code, and fatigue. |
| Technical elegance/controllability | 3 → **2** | Subscale cycling cannot cleanly predict full-core, 20-year behavior. |
| 10× technical edge | 2 → **1** | No order-of-magnitude advantage is specified or evidenced. |
| 2030 launch-window fit | 4 → **3** | Market timing is good, but startup qualification by 2030 is doubtful. |

Other raw scores unchanged. Suggested weighted total: **48.2**.

### Cheapest decisive falsification experiment

There is **no genuine sub-$100k decisive technical experiment**. A coupon or small bonded block can screen alloy/bond failure, but cannot validate header stress, channel maldistribution, pressure boundary, code documentation, or 1,000-cycle core performance. The cheapest honest gate is commercial: obtain a paid development agreement from an OEM/EPC that supplies the incumbent's measured transient limit and commits to a target the incumbent cannot meet. Technical validation then remains a **$400–600k** minimum subscale-core program, preferably funded by that buyer and executed with an existing bonder. Do not relabel a $75k coupon campaign as decisive or count it toward the portfolio quota.

**Final verdict: KILL.** Reopen only as a licensed design/qualification program after a paid buyer proves a specific incumbent failure.

---

## `P3R2-E-02` — refrigerant-agnostic two-phase cooling sensor and controller

### Strongest bear case

This is a subsystem feature searching for an independent company boundary. The current competitors do not merely sell a proprietary fluid; they already integrate the “brain,” sensors, controls, service, and software. Accelsius describes its NeuCool iCDU as containing **core logic, pumps, system sensors, touchscreen control, redundant components, and load-balancing pump control** ([Accelsius product architecture](https://accelsius.com/solutions/)). ZutaCore sells a complete two-phase system plus software-defined monitoring, control, and optimization ([ZutaCore HyperCool](https://zutacore.com/solutions)). Accelsius announced general availability of a fully integrated 150 kW rack-level two-phase system in 2026 ([Accelsius IR150 launch](https://accelsius.com/accelsius-announces-neucool-ir150-hyperstart-program/)). The absence of a standalone fluid-agnostic controller is therefore more likely vertical integration than whitespace.

The product-demand evidence fails a strict G1 reading. Vertiv's liquid-cooling backlog is broad, and Meta's disclosed path is not two-phase. EPA regulation constrains high-GWP fluids but does not require two-phase cooling, a fluid-agnostic sensor, or merchant control. EPA's current sector table places a GWP 700 limit on data-center/IT cooling from January 1, 2027 ([EPA sector restrictions](https://www.epa.gov/climate-hfcs-reduction/technology-transitions-hfc-restrictions-sector)); the May 2026 final reconsideration changes requirements in several cooling subsectors but does not create a procurement mandate for this product ([EPA 2026 rule status](https://www.epa.gov/hfcs/regulatory-actions-technology-transitions)). Low-GWP integrated systems already advertise refrigerants near GWP 1, so regulatory transition can strengthen incumbent whole-stack offerings instead of creating controller disaggregation.

Standards activity also does not establish the wedge. OCP lists a mature vendor-neutral single-phase cold-plate baseline while its two-phase dielectric-fluid guideline remains a draft workstream ([OCP cold-plate workstreams](https://www.opencompute.org/wiki/Cooling_Environments/Cold_Plate)). Fluid properties, evaporator geometry, control logic, materials, warranties, and service liability are coupled. An OEM has strong incentives to retain the controller and reject a third-party sensor that could invalidate its thermal warranty.

The claimed 10× edge is absent. Fluid auto-identification and a shared controller may reduce engineering work, but no buyer source quantifies requalification cost, time, dryout incidents, or willingness to pay. The $250k rig can show estimation/control performance but cannot answer the decisive buy-vs-build and warranty questions. China is absent, and the optional JP/TW/KR validation venues do not substitute for a weak US product case.

### Disconfirming evidence and steelman

The physics is controllable, AI heat flux is rising, two-phase products are now commercial, and incumbent architectures remain proprietary. A neutral metrology layer could become valuable if multiple fluids and CDU designs coexist and if OEMs need independent qualification. The electronics/software v1 is much more capital-reachable than PCHE or Brayton hardware.

The best steelman is to preserve this as the sensing/control feature of a broader cooling loop or independent qualification service. It should not survive as a standalone company without two paid OEM integrations and explicit warranty acceptance.

### Hard-gate verdicts

| Gate | Red-team verdict | Reason |
|---|---|---|
| G1 | **fail** | No primary buyer/procurement/filing requests a merchant fluid-agnostic controller; liquid-cooling backlog and HFC rules are adjacent. |
| G2 | **pass** | The technical basis uses eligible peer-reviewed work. |
| G3 | **pass** | The three-fluid rig is bounded at $250k with measurable criteria. |
| G4 | **fail** | Accelsius and ZutaCore already integrate sensors, core logic, software, and control; fluid-agnosticism has not been shown to create a purchasable non-cosmetic difference. |
| G5 | **pass** | No new physics or unlimited capital is required. |
| G6 | **pass** | US-only base case has no structural export-control barrier; safety/fluid qualification remains a product burden. |
| G7 | **fail** | EPA's dated trigger forces lower-GWP choices, not two-phase or merchant control; no primary 2030–2034 procurement/design-in trigger exists for the product. |

### Score adjustments proposed

| Criterion | Raw P4 → proposed | Basis |
|---|---:|---|
| Demonstrated demand | 3 → **1** | Product-level willingness to buy is absent. |
| High-end niche quality | 3 → **2** | Narrow and technically reachable, but OEM integration blocks access. |
| Competition whitespace | 3 → **1** | Whole-stack competitors already contain the controller and service layer. |
| Technical elegance/controllability | 4 → **3** | Bench control is elegant; cross-fluid transfer and warranty integration are harder. |
| 10× technical edge | 2 → **1** | No 10× buyer-valued metric. |
| US–China leverage | 2 → **1** | Conditional US-only case; no China leg. |
| 2030 launch-window fit | 3 → **2** | Two-phase commercializes before 2030 inside vertically integrated systems; no merchant-controller trigger. |
| Expansion economics | 3 → **2** | Adjacencies are plausible but repeat OEM integration problems. |

Other raw scores unchanged. Suggested weighted total: **41.8**.

### Cheapest decisive falsification experiment

A sub-$100k experiment is decisive only if commercial acceptance is built into it. Budget **$90k maximum** with a neutral host lab contributing a 30–50 kW loop and reference metrology. Before hardware work, require two OEMs to sign paid evaluation agreements with fixed pass criteria and a license/integration option. Run blinded identification and dryout-margin control across three eligible low-GWP fluids and two evaporator geometries under 10× heat-flux steps; require <5% quality error, no dryout, control stability after unknown-fluid insertion, and both OEMs' written acceptance for integration. If two paid agreements cannot be secured, or either OEM refuses warranty/interface responsibility after a technical pass, kill the standalone product. A university rig without precommitted OEM acceptance is not decisive and must not count toward the sub-$100k quota.

**Final verdict: KILL as a standalone company.** Preserve the IP hypothesis only as a feature inside a broader cooling product or a paid independent qualification service.

---

## `P3R2-D-16` — merchant closed-Brayton converter/PMAD for lunar fission surface power

### Strongest bear case

This is a government-program option, not yet a venture market. NASA's own 2025 announcement says it was **seeking industry feedback** for a potential 100 kWe closed-Brayton FSP system ([NASA RFI announcement](https://www.nasa.gov/centers-and-facilities/glenn/nasa-seeks-industry-feedback-on-fission-surface-power/)). The exact 10 kW closed-Brayton prototype notice is a Sources Sought record that explicitly says **“No solicitation exists”** and requests no proposal ([SAM.gov notice 80GRC025R7013](https://sam.gov/opp/dc4ee678bff146a68adcba79e3ec4fd2/view)). On 2026-03-26 NASA made the FSP technical library inactive while it reassessed the development approach ([SAM.gov update](https://sam.gov/opp/6af0e42071cb412e809511f18627cc46/view)). The later April policy memorandum may restore top-level intent, but no final PCU award, downselect, flight contract, or merchant-subsystem procurement is in the record.

The proposed whitespace is a business model, not a technical edge. Creare has decades of Brayton heritage and current NASA work; Brayton Energy is already an independent merchant turbomachinery house; primes can keep power conversion captive. “Sell the same unit to all teams” does not satisfy G4's non-cosmetic difference, especially when team interfaces, reactor temperature, radiator design, alternator voltage, fault tolerance, launch loads, and PMAD architecture may diverge. No 10× efficiency, mass, life, cost, or qualification metric relative to these competitors is offered.

Economics are structurally poor. P4 estimates only one to three flight units through 2034, no public per-unit price, a $500k first rig, and $10–30M to v1. Revenue is likely cost-plus NRE/subcontract work concentrated in one government program. The NASA RFI itself records industry concern that launch/lander cost share may make the business case difficult (local P4 source context and SAM.gov RFI record). A startup bears long flight-qualification and program-slip risk while incumbents and primes have the required contracting, export-control, quality, and heritage systems.

The idea's own binding 2028 gate—downselect/contracted flight dates plus written interest from at least two teams—is not met. Holding it as studies-only is rational; counting it in the final 24 would turn an explicitly conditional option into a selected company.

### Disconfirming evidence and steelman

The program requirement is unusually specific: at least 100 kWe and closed Brayton, and FY2026 funding indicates political support. A modular 25–50 kWe converter could become a standard across reactor teams, and domestic eligibility narrows foreign competition. The frontier vision is exceptional.

The steelman is a no-capex SBIR/consulting option until a final solicitation and team contracts appear. It is not a 2030 startup base case today.

### Hard-gate verdicts

| Gate | Red-team verdict | Reason |
|---|---|---|
| G1 | **pass_marginal** | Official program funding and exact closed-Brayton sources-sought notices exist, but the notices are not solicitations/awards and no merchant PCU buyer commitment exists. |
| G2 | **pass** | Technical heritage rests on eligible NASA/government sources. |
| G3 | **pass_marginal** | Studies are cheap but not decisive; the first technical risk test is $500k and requires external facilities. |
| G4 | **fail** | Creare, Brayton Energy, and captive prime teams are real; multi-team merchant positioning is not a non-cosmetic technical difference. |
| G5 | **pass_marginal** | Physics is real, but one government program and 1–3 units dominate the entire business case. |
| G6 | **pass** | Domestic-only procurement and normal space/nuclear qualification are acknowledged, although they raise cost. |
| G7 | **pass_marginal** | Policy dates align with 2030, but the development approach has been reassessed, no final award exists, and the binding downselect/team-interest gate is pending. |

### Score adjustments proposed

| Criterion | Raw P4 → proposed | Basis |
|---|---:|---|
| Demonstrated demand | 3 → **2** | Funded program intent, no awarded merchant PCU procurement. |
| High-end niche quality | 3 → **1** | One buyer/program, 1–3 units, heritage-heavy access. |
| Competition whitespace | 2 → **0** | Named merchant/captive competitors; no technical differentiation. |
| Reachable validation budget | 1 → **0** | $500k first hardware and $10–30M v1 for a tiny market. |
| Technical elegance/controllability | 3 → **2** | Cycle is modellable, but flight qualification and coupled reactor/radiator/PMAD interfaces are not bounded pre-company. |
| 10× technical edge | 2 → **0** | No technical edge over Creare/Brayton/primes is specified. |
| 2030 launch-window fit | 3 → **2** | Policy target exists; procurement and development path remain unstable. |
| Expansion economics | 2 → **1** | Terrestrial micro-Brayton and NEP are speculative and do not rescue the base case. |

Other raw scores unchanged. Suggested weighted total: **36.4**.

### Cheapest decisive falsification experiment

There is **no sub-$100k decisive technical experiment** for flight Brayton. A <$25k, 90-day commercial gate can decisively kill the merchant position: obtain written subsystem-interface access and conditional subcontract interest from at least two independent FSP teams, plus confirmation that the final acquisition permits a shared merchant PCU. Failure kills the option; success only authorizes the $500k 10 kWe rig and does not count as a sub-$100k decisive technical experiment. Do not build hardware before the final solicitation, contracted flight dates, and two-team interest exist.

**Final verdict: KILL from the final 24.** Preserve only a zero-capex watchlist/SBIR option until the binding 2028 gate is actually met.

## Cross-group adjudication notes

1. Product-specific G1 discipline would eliminate `P3R2-G-01` and `P3R2-E-02`; adjacent facility, regulatory, or market spending cannot substitute for a buyer of the proposed product.
2. The strongest new competitor corrections are VPE for `P3R2-C-08`, Accelsius/ZutaCore for `P3R2-E-02`, and existing ASIPP/fabricator acceptance systems for `P3R2-G-01`.
3. None of the five currently qualifies honestly as a **validated** <$100k decisive first experiment. `P3R2-G-01` and `P3R2-E-02` have plausible sub-$100k tests only if paid buyer commitments and host facilities are secured before the test. The A-14, C-08, and D-16 cheap steps are veto gates, not positive validation of the core technical/company thesis.
4. No China beachhead should be added to `P3R2-A-14`, `P3R2-E-02`, or `P3R2-D-16` without new country-specific primary demand. `P3R2-C-08` keeps a conditional China leg; `P3R2-G-01` has China program demand but fails product-specific demand.
5. All cited market evidence is from the United States, China, or optional JP/TW/KR contexts already in scope. No excluded-market source or commercial example is used.
