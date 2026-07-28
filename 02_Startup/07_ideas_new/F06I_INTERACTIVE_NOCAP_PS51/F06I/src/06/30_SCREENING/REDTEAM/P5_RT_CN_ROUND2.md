# P5 China regeneration round 2 — independent red team

Date: 2026-07-14  
Scope: exactly `P5R2-CN-01` through `P5R2-CN-04` from `P5_CN_REGEN_ROUND2_PROPOSAL.json`  
Decision semantics: **REINSTATE** means all hard gates pass now and the China beachhead may count; **HOLD** and **KILL** contribute zero to current portfolio quotas. Scores use the binding eleven-factor 100-point rubric. Founder fit remains only 2/100.

## Executive verdict

| Idea | Score | China countable now | Disposition | Thesis-kill probability by 2029-12-31 | <$100k decisive-experiment credit now |
|---|---:|---|---|---:|---|
| P5R2-CN-01 | 55.6 | **Yes** | **REINSTATE** | 65% | No — conditional on signed cabinet access and third-party quotes |
| P5R2-CN-03 | 50.0 | No | **HOLD** | 76% | No — conditional on a paid industrial-steam site and metrology quote |
| P5R2-CN-04 | 47.2 | No | **KILL** | 86% | No |
| P5R2-CN-02 | 40.8 | No | **KILL** | 91% | No |

The kill probabilities are red-team judgment under correlated technical, access, buyer, and incumbent risks; they are not measured frequencies. Only CN-01 survives. The proposal's four `fetched: true` declarations are not a substitute for canonical-ledger acceptance: none of the `P5R2-CN-S*` records was in `90_BIBLIOGRAPHY/sources.json` at review time.

## Cross-cutting source and classification audit

- The CN-01 MOFCOM events are genuinely independent buyer procurements despite sharing a platform. Guangzhou Guangxin tender `0730-264010SZ0036/46` is an X-ray inspection machine for layer deviation; Wuxi Shennan tender `0730-264010SZ0024/15` is one online X-ray inspection machine, open to domestic and foreign bidders. These prove present X-ray-inspection purchasing, not demand for a retrofit or laminography.
- The official Tongji record behind CN-03 is narrower than the proposal says. It procures a 2,000-hour demonstration site/service for a specific PEM-fuel-cell/heat-pump power-and-steam R&D system, including hydrogen, power, steam takeoff, cooling water, safety, and space. It does not procure a portable measurement-and-verification island. MIIT's 2026-2028 plan does call for wide-load actual-performance evaluation, but it is an official category direction rather than a second named buyer.
- CN-04's SDIC notice is exact-category evidence, but it is a 45-day R&D service to localize dry arsenic-waste-gas POU equipment and requires a bidder with its own exhaust-equipment factory and similar project experience. That requirement is also adverse proof that qualified domestic incumbents already exist. The CRRC tender says only “exhaust-gas treatment equipment,” not dry arsine POU.
- CN-02's SJTU procurement is for a complete helium-recovery system. The Jianxin filing supports outsourced recovery/purification work, not purifier-only buying. The same filing family also documents rapid growth of helium-free MRI products, adverse to the claimed 2030 demand bridge.
- The proposal's suggested ledger objects need normalization before any acceptance. Values such as `primary_buyer_procurement`, `peer_reviewed_journal_article`, `competitor_product_page`, and `official_forward_plan` are outside the binding `source_type` enum; `geography` is a string rather than an array; and the academic origin audits do not enumerate all resolved institutions. The two academic records inspected are final journal records and appear non-India-origin, but their claims are only adjacent: CN-S04 supports advanced-package tomography, not retrofit computed laminography; CN-S14 supports monitoring-boundary discipline, not industrial high-temperature steam-heat-pump field accuracy.
- Lane/role/archetype calls are honest as proposed: CN-01 and CN-03 are `diagnostic_test`/industrial; CN-04 is infrastructure/industrial; CN-02 is infrastructure/scientific-big-physics. None is an HTS idea. CN-01 belongs primarily in L06, CN-03 in L04, CN-04 in L01, and CN-02 in L07.

## P5R2-CN-01 — retrofit X-ray computed laminography

**Disposition: REINSTATE. China countable: YES.** Current China demand clears literal G1; H2-2028 advanced-packaging equipment completion is a relevant customer-system trigger; and the installed-cabinet stage/calibration retrofit remains a non-cosmetic physical product. This is a low-scoring, high-kill survivor, not an automatic final-24 selection.

| Gate | Verdict | Red-team finding |
|---|---|---|
| G1 | PASS_MARGINAL | Two independent named CN buyers procure the exact X-ray-inspection job. Neither buys a retrofit or 3D laminography, so demand score stays 3/5. The SAM/NIST page did not independently expose its opportunity details in this pass and is not needed for the CN gate. |
| G2 | PASS_MARGINAL | CN-S04 is final peer-reviewed work, but it supports tomography for package failure analysis, not this cabinet conversion. Computed-laminography calibration requires a separately accepted final paper before a final card. |
| G3 | PASS_MARGINAL | The 12-month blinded coupon protocol would kill sensitivity, false-positive, throughput, repeatability, and buyer premises. The stated $92k is not yet quota-creditable because neither cabinet access nor destructive-sectioning/reference-CT pricing is evidenced. |
| G4 | PASS_MARGINAL | The proposal names complete-system companies, and cabinet reuse plus a tilted stage/calibration artifact is non-cosmetic. However, the closest 2026 threats are ZEISS **NLX**, already an in-line 3D X-ray laminography system for advanced packaging, and Fraunhofer EZRT's **VOLEX retrofit** service for existing industrial X-ray systems. TRI also launched a new high-throughput 3D AXI platform in June 2026. |
| G5 | PASS_MARGINAL | Laminography is established. What is not established is that two arbitrary installed cabinets have sufficient mechanical clearance, source/detector stability, dose control, raw-data access, and geometric repeatability. The proposed two-brand test is an appropriate falsifier. |
| G6 | PASS_MARGINAL | A locally built stage, artifact, and independently developed software for civilian packaging is plausible. Final use still needs current export classification, restricted-party screening, radiation-equipment service permissions, and written confirmation that no source/shielding modification is required. |
| G7 | PASS_MARGINAL | JCET's exchange filing gives an H2-2028 production-equipment completion point for a high-end packaging factory; the official 2026-2030 IC plan and present tenders provide independent context. Post-installation yield learning in 2030 is a reasonable inference, not a committed retrofit order. |

### Score arithmetic

| Criterion | Raw | Weighted |
|---|---:|---:|
| Demonstrated demand | 3 | 9.6 |
| Frontier/coolness | 3 | 9.0 |
| High-end niche | 3 | 6.0 |
| Competition whitespace | 1 | 1.8 |
| Reachable validation budget | 3 | 5.4 |
| Elegance/controllability | 3 | 6.6 |
| 10x edge | 1 | 1.4 |
| US-China leverage | 3 | 6.0 |
| 2030 window | 4 | 6.4 |
| Expansion economics | 3 | 1.8 |
| Founder transfer | 4 | 1.6 |
| **Total** |  | **55.6** |

**Exact blockers/conditions:** before final selection, accept normalized sources; add the exact ZEISS NLX and VOLEX competitors; obtain signed access to two cabinet brands, raw-data/service-interface permission, a line-item budget under $100k if claiming that quota, and one buyer-signed paid evaluation contingent on the blinded thresholds.

**Factual vs inference:** the tenders, ZEISS product, VOLEX service, and JCET completion date are factual source statements. Installed-base size, retrofit compatibility, “small fraction of replacement cost,” and 2030 paid appetite are inferences still to be tested.

## P5R2-CN-03 — industrial heat-pump field M&V island

**Disposition: HOLD. China countable: NO.** The policy need is real, but the only named procurement does not purchase the proposed job. The candidate therefore lacks the primary-buyer half of literal G1 as presently evidenced.

| Gate | Verdict | Red-team finding |
|---|---|---|
| G1 | **FAIL** | Tongji's official scope purchases a demonstration site and operating support for a specific R&D system; it does not specify independent transient COP/exergy measurement. MIIT calls for wide-load evaluation and the national action plan promotes industrial heat pumps, but neither is a named buyer purchase of the M&V island. |
| G2 | PASS_MARGINAL | CN-S14 is final peer-reviewed monitoring work but is not evidence for industrial-steam accuracy. No claimed 2-3% field accuracy may be imported from it. |
| G3 | PASS_MARGINAL | A blinded 5% degradation test is load-bearing and potentially decisive. The $68k figure lacks a committed 300 kW-3 MW site, traceable reference-calorimetry quote, steam-quality instrumentation, travel/safety, and two-season coverage. |
| G4 | PASS_MARGINAL | The true closest products are ClimaCheck Onsite and Articae PilotE2, both portable non-invasive heat-pump performance/commissioning analyzers; China CVC already performs on-site heat-pump-system acceptance. Whole-boundary steam enthalpy, auxiliaries, transient uncertainty, and a performance-guarantee dossier can remain non-cosmetic only if benchmarked against them. |
| G5 | PASS | All observables are established engineering. Boundary closure, wet-steam state, clamp-on-flow bias, fouling, and transient synchronization are measurable failure modes. |
| G6 | PASS | Local commodity instrumentation and civilian industrial energy-service channels have no evident structural cross-border block. Chinese calibration, data-security, pressure-system access, and site-safety rules remain normal diligence. |
| G7 | PASS_MARGINAL | MIIT's official program runs through 2028 and the national industrial-heat-pump action plan reaches 2030, inside the required window. The 2030-2034 recurring acceptance market is an inference; a paid 2029 industrial-owner engagement remains necessary. |

### Score arithmetic

| Criterion | Raw | Weighted |
|---|---:|---:|
| Demonstrated demand | 3 | 9.6 |
| Frontier/coolness | 2 | 6.0 |
| High-end niche | 3 | 6.0 |
| Competition whitespace | 1 | 1.8 |
| Reachable validation budget | 3 | 5.4 |
| Elegance/controllability | 3 | 6.6 |
| 10x edge | 1 | 1.4 |
| US-China leverage | 2 | 4.0 |
| 2030 window | 4 | 6.4 |
| Expansion economics | 2 | 1.2 |
| Founder transfer | 4 | 1.6 |
| **Total** |  | **50.0** |

**Exact blockers/conditions:** reinstate only after a named industrial heat-pump owner/integrator signs a paid or budgeted field-acceptance/M&V engagement, the product is narrowed to high-temperature steam/whole-boundary acceptance, ClimaCheck/PilotE2/CVC are benchmarked, and a quoted experiment stays under the claimed budget. The US flag is also unproven; DOE project funding is a partner lead, not a merchant buyer.

**Factual vs inference:** the Tongji scope/budget, MIIT evaluation language, 2028/2030 policy dates, and incumbent product capabilities are facts. A recurring acceptance socket, willingness to pay for a neutral dossier, and achievable 2-3% whole-boundary uncertainty are inferences.

## P5R2-CN-04 — local dry arsine-abatement cartridges

**Disposition: KILL. China countable: NO.** Exact demand exists, but it simultaneously reveals experienced domestic suppliers, and independently found domestic products already erase the claimed localization wedge. G4 and G7 fail.

| Gate | Verdict | Red-team finding |
|---|---|---|
| G1 | PASS_MARGINAL | SDIC/Shiyuan procures exact dry arsenic-waste-gas POU localization R&D. CRRC independently procures generic exhaust treatment. Only the first source is dry-arsine-specific. |
| G2 | PASS | No academic result is used to claim startup performance. All removal/capacity numbers remain experiment targets. |
| G3 | PASS_MARGINAL | The challenge test is technically decisive, but $86k lacks a licensed arsine-lab quote, imported benchmark cartridge cost, certified analyzers, emergency engineering, insurance, and disposal. It cannot count as a <$100k portfolio experiment. |
| G4 | **FAIL** | Gaopin/Hefei Taimi already advertises domestically manufactured dry media, dry single/double-canister local scrubbers, customization, installation, and on-site maintenance for Chinese fabs. CS Clean already refills used dry columns. The proposal did not name the closest domestic incumbent, and local media plus service/take-back is no longer a defensible wedge. |
| G5 | PASS | Chemisorption is established and a licensed challenge can test it. Safety and waste qualification, not nonexistent physics, dominate. |
| G6 | PASS_MARGINAL | A local civilian route is possible only with licensed toxic-gas testing, pressure/electrical conformity, hazardous-waste classification and take-back permits, emergency response, and fab vendor qualification. |
| G7 | **FAIL** | The 2026-2030 IC plan is sector-generic. CRRC's current capacity and 2025/2026 equipment activity do not specify a 2028-2035 arsine/dry-cartridge qualification or expansion event. Recurring cartridge replacement through 2034 is an unsupported extrapolation. |

### Score arithmetic

Raw scores `4,2,3,1,2,3,2,1,2,2,3` yield weighted values `12.8+6.0+6.0+1.8+3.6+6.6+2.8+2.0+3.2+1.2+1.2 = 47.2/100`.

**Exact blockers:** the thesis would require a buyer-signed arsine-specific second-source qualification extending into 2030-2034, an unmet metric against Gaopin/Taimi and CS Clean (not merely localization/take-back), a named licensed test/waste chain, and quoted safety economics. Those conditions amount to a different, post-incumbent product thesis; do not hold quota space.

**Factual vs inference:** the exact SDIC R&D notice, its experienced-factory requirement, CRRC generic tender, Gaopin/Taimi domestic product stack, and CS Clean refill practice are facts. Process-gas mix, 2030 replacement volume, premium willingness, and attainable lab cost are inferences.

## P5R2-CN-02 — dirty-return helium purifier and mass balance

**Disposition: KILL. China countable: NO.** Current helium-recovery spending is real, but the purifier-only layer is already sold by multiple vendors and the cited 2030 triggers do not force dirty-return helium demand.

| Gate | Verdict | Red-team finding |
|---|---|---|
| G1 | PASS_MARGINAL | SJTU budgets a complete recovery system; Jianxin purchases recovery/purification services. Both prove the job, neither proves demand for a merchant purifier-only retrofit. |
| G2 | PASS | No academic performance value is borrowed. Startup purity/recovery/endurance remains to be generated. |
| G3 | PASS_MARGINAL | The 500-hour contamination-envelope test is load-bearing. The $78k claim lacks compressor, membrane, twin-bed, certified trace-analyzer, pressure-vessel, contaminated-gas, and partner-manifold quotes; <$100k credit is not defensible. |
| G4 | **FAIL** | Quantum Design/Cryomech sell purifier modules; RYTS lists a standalone ATP30 purifier; Shanghai LifenGas, Fullcryo, and Zhengfan already integrate China helium recovery/purification. Automatic diversion and custody mass balance are controls/software features incumbents can add, not a protected non-cosmetic wedge. |
| G5 | PASS | Membrane/adsorption purification is established. The proposed run can test integration but not create whitespace. |
| G6 | PASS | A local standard-pressure-equipment route is credible, subject to ordinary vessel, electrical, purity, and university procurement compliance. |
| G7 | **FAIL** | A quantum-platform standard and generic 2026-2030 quantum policy do not imply vented dirty-return helium: many quantum cryogenic platforms are closed-cycle. Jianxin's own rapid shift toward helium-free MRI is adverse substitution evidence. No primary/official 2028-2035 purifier-only trigger survives. |

### Score arithmetic

Raw scores `3,2,2,1,3,3,1,1,1,2,3` yield weighted values `9.6+6.0+4.0+1.8+5.4+6.6+1.4+2.0+1.6+1.2+1.2 = 40.8/100`.

**Exact blockers:** a named site with an existing downstream liquefier must specify purifier-only procurement; an official or primary 2028-2035 installed-base trigger must involve recoverable helium rather than dry/closed-cycle systems; and the candidate must beat named purifier modules on contamination acceptance, recovery, service cost, and auditable loss reduction. The combined substitution and commodity risks make repair disproportionate.

**Factual vs inference:** the SJTU complete-system intention, Jianxin outsourced service, Jianxin helium-free product trend, and named purifier products are factual. The size of the purifier-only installed-base socket and value of per-user custody accounting are inferences unsupported by a buyer.

## Final red-team instruction to the main adjudicator

Only `P5R2-CN-01` may add one China beachhead after the proposed records are normalized, origin-audited, accepted, and associated in the canonical ledger. `P5R2-CN-03` is a zero-quota HOLD pending exact primary-buyer evidence. `P5R2-CN-04` and `P5R2-CN-02` should not be revived. None of the four presently contributes to the portfolio's “decisive experiment under $100k” count without access agreements and third-party cost evidence.
