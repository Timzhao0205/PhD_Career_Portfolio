# P4 global independent cross-batch audit

Date: 2026-07-13  
Scope: frozen 65-idea longlist; all 65 P4 evidence dossiers; canonical score batches S1-S4; P4 group ledgers and canonical source ledger where load-bearing.  
Write boundary: advisory only. No scorecard, state, source, or log was edited.  
Runtime model/effort for this audit: **unknown**; the runtime does not expose either value to this auditor.

## Executive judgment

The current P4 decisions are not ready to drive P5 unchanged.

- Population reconciles: 65 frozen ideas, 65 evidence dossiers, and score batches of 17/16/16/16 ideas.
- Canonical decisions retain **31** and eliminate **34**, so there is no canonical top 32.
- On a single strict interpretation of G1 and G7, only a small core is clean enough to advance without a condition. The practical P5 pool below therefore contains **7 clean advances and 25 explicit conditional holds**, not 32 falsely gate-cleared survivors.
- The largest substantive defect is demand transference: several high scores prove spending in an underlying market, but not demand for the proposed merchant product. Comparable records were eliminated for the same gap.
- S2 surviving-score mean is 70.0, versus 62.6 in S1, 63.1 in S3, and 62.0 in S4. Idea mix explains some of this, but S2 also contains the most generous high scores for derivative product demand.
- The score batches fail the current machine check with **107 errors**. These include 13 unscored eliminated records in S1/S3, unresolved or ineligible citations, cross-idea citations, unsupported scores above 3, and one arithmetic error.
- The experiment portfolio cannot meet its own final-24 gate: **0/65** ideas have a decisive experiment at or below $100k, while the final portfolio requires at least eight below $100k. Forty-six of 65 exceed $250k; 21 are at least $500k; three are at least $1M.
- V1 capital is also systematically optimistic: 61/65 idea ranges have an upper bound above $5M. Among the current 31 survivors, 20 experiments exceed $250k and only one idea has a v1 range wholly at or below $5M.
- The source ledger has 1,417 rows but only 1,219 unique IDs: 198 IDs occur twice, generally as an accepted verified record plus a rejected raw shadow. Accepted works themselves remain unique (1,112 accepted rows and 1,112 unique accepted canonical keys), but ID lookup is ambiguous.
- The curation log states that all 63 dossiers were read even though 65 exist. The 13 group ledgers do cover all 65, so this is at minimum a provenance/counting defect that needs an explicit correction.

## Binding interpretation used

1. **G1 is product demand, not merely end-market growth.** A necessary embedded function may pass marginally when a buyer specification explicitly names the function and incumbent sales prove the socket. A general project award, sector backlog, regulation, or capacity target does not prove demand for an optional merchant overlay.
2. **G7 requires a launch-relevant open window.** Present demand can qualify only when two independent timing sources show that a merchant design-in/procurement opportunity persists into 2030-2034, including one primary/official 2028-2035 trigger. A current award that fixes the design before 2030 is negative timing evidence.
3. **`pass_marginal` is treated as a conditional pass, not a third hard-gate state.** The binding rubric defines gates as pass/fail. Every marginal call therefore needs a named flip condition and cannot be silently counted as fully cleared.
4. **Capital scores cover both the decisive experiment and sellable v1.** A $250k experiment does not justify raw 4-5 if the v1 path is mostly above $5M and no smaller sellable wedge is specified.
5. **A 10x score requires a demonstrated or tightly evidenced order-of-magnitude advantage on a buyer-valued dimension.** A temperature-class gap, 15-point efficiency gain, 8x channel count, or target cost is not automatically raw 4-5.
6. **A structurally blocked China route cannot remain a co-equal base case.** Removing China from the rationale but leaving `china_beachhead=true` is not a G6 pass.

## Mechanical and source-integrity findings

| Finding | Audit result | Consequence |
|---|---|---|
| Current `tools/validate_p4.py` result | FAIL, 107 errors | P4 cannot be treated as mechanically complete. |
| Eliminated-score schema | S1/S3 leave all 13 eliminated ideas unscored; S2/S4 fully score 21 eliminated ideas | Cross-batch ranking and near-miss comparison are not comparable. |
| F-01 arithmetic | Stored 73.8; weighted fields sum to 71.8 | Correct before any substantive downgrade. |
| Missing/stale citation IDs | `L02-043` is absent from the canonical ledger under that ID although the same NVIDIA work survives as `P3R2-G-03-S01`; A-21 cites missing S02/S04; C-03 cites missing S04 | Citation aliases/provenance must be repaired before scoring claims are considered verified. |
| Ineligible/demoted load-bearing citations | Examples: A-10 uses demoted S02; C-07 and C-22 cite rejected L11-051; F-01 cites ineligible L06-040; several D-01/D-02 technical IDs have empty canonical `claim_supported` fields | Scores above 3 and some gate rationales are not currently supported under the validator's own rules. |
| Cross-idea citation leakage | Examples include C-09 using D-08 evidence, C-19 using C-08 evidence, F-11 using F-10 evidence, and C-01 using B-06 evidence | Shared facts need canonical shared IDs or explicit cross-idea eligibility, not idea-local leakage. |
| Scores above 3 without source-ID support | Repeated for reachable-budget, expansion, and founder-fit fields | Either cite an eligible record/file or reduce raw score to 3; a budget copied from the seed is not external evidence. |
| Curation coverage statement | Log says 63; folder and group-ledger reconciliation show 65 | Correct provenance before relying on the claimed full read. |

## Cross-batch calibration

| Batch | Ideas | Current survivors | Survivor mean / median | Model self-report | Calibration observation |
|---|---:|---:|---:|---|---|
| S1 | 17 | 9 | 62.6 / 62.0 | `claude-fable-5` | Moderate scores, but all eight eliminations are left unscored. Several survivors use permissive underlying-market G1 logic. |
| S2 | 16 | 6 | 70.0 / 69.3 | `unknown` | Clear upward shift. C-22 (76.2) and D-01 (71.4) receive high scores despite explicit absence of product-specific procurement. Ten eliminated records are fully scored. |
| S3 | 16 | 11 | 63.1 / 61.4 | `claude-fable-5` | More permissive survival rate. F-01 has the only arithmetic error and a structurally blocked China chapter; D-13/E-04 survive on derivative demand. Five eliminations are unscored. |
| S4 | 16 | 5 | 62.0 / 60.4 | `unknown` | Strictest on G1/G7 and therefore the best calibration anchor. Eleven eliminated records are fully scored. Similar derivative-demand gaps that fail here survive S1-S3. |

Routing-log note: S1-S4 were initially requested as Fable/xhigh. S2 and S4 were later regenerated in the continuation run with requested `GPT-5.6 Sol`, while actual model and effort were logged `unknown`; the canonical S2/S4 files also self-report `unknown`. Do not describe their runtime route as verified.

### G1 consistency examples

- F-19 correctly fails because datacenter liquid-cooling growth does not prove demand for a coolant-health skid. The same rule should apply to E-02 (cooling backlog does not prove a merchant controller), D-12 (cooling specifications do not prove an EHD pump), and C-22 (hydrogen projects do not prove a degradation-emulation bench).
- C-19 correctly fails because sCO2 projects do not prove a merchant bearing/seal cartridge. The same rule should apply to F-03's merchant turbo-generator cartridge and D-13's thermal magazine.
- G-02 correctly fails because accelerator growth does not prove merchant targets/windows. G-03 currently survives even though its rationale says no buyer procures third-party acceptance instrumentation.
- A-03 correctly fails because the regulation buys modeling/passive monitoring rather than the proposed MW field emulator. E-14 should not receive a clean G1 pass merely because HVDC projects exist when no merchant relay/HIL procurement is shown.

### G7 consistency examples

- D-10 is correctly eliminated despite a strong 75.2 score: the exact design slot closes in 2026-2028, before a 2030 launch.
- C-05, C-09, F-16, and D-09 are correctly blocked today because present demand is not accompanied by an eligible 2028-2035 product trigger. C-05 is the best recheck candidate, not a current pass.
- A-21, A-22, D-19, and F-12 rely substantially on current/near-term programs plus an inference of persistence. Their G7 calls should remain conditional unless a primary 2028-2035 procurement/standard/refit trigger is added.

## All-65 compact review

Legend: `S` = canonical survivor; `E` = canonical eliminated; `Keep` = defensible advance; `Hold` = retain only in a conditional P5 review pool; `Elim` = elimination supported; `Recheck` = best eliminated candidate to revisit after a specific evidence repair. Adjusted scores are advisory counterfactuals and do not override a failed gate.

| Idea | Canonical | Audit | Compact independent review |
|---|---:|---|---|
| P3R2-A-02 | S 55.2 | Hold-G1/G3 | Demand is explicitly one step removed from an MVDC-breaker purchase; $1.5M experiment and $10-25M v1 are not pre-company-realistic. Counterfactual ~52.0. |
| P3R2-A-03 | E | Elim | PRC-029 spend goes to EMT modeling/passive monitoring, not the proposed field-MW emulator; timing closes on the wrong product. |
| P3R2-A-05 | S 66.8 | Keep | Real big-science procurement and established coating category; reduce negative-search whitespace and capital raw scores. ~63.2; TAM remains unpriced. |
| P3R2-A-10 | S 62.0 | Hold-G1/G6 | US waveform market is real but the merchant IEDF retrofit is not purchased; named China customers are restricted. Dual record fails as written; US-only ~57.2. |
| P3R2-A-11 | E | Elim | No MFC buyer/LOI and no MFC-specific 2030 trigger; incumbent technology already approaches the claimed response class. |
| P3R2-A-13 | S 57.2 | Hold-G1/G7 | SDA/EP demand exists, but vertical integration and paused Tranche 3 weaken merchant PPU demand and persistence; $700k experiment. ~54.0. |
| P3R2-A-14 | S 74.0 | Keep | Strongest US timing/supply-gap case; 300C is a capability gap, not demonstrated 10x buyer value. Downgrade launch/10x/expansion to ~70.4. |
| P3R2-A-16 | E | Elim | Thermal pain is real, merchant TIM demand is not; direct-liquid substitution and incumbent qualification can close the 2030 window. |
| P3R2-A-21 | S 51.0 | Hold-G7/capital | Charging grants and standards are real, but much of the funded wave precedes launch; $1.2M experiment and $8-20M v1 are weak. |
| P3R2-A-22 | S 61.0 | Hold-G7/G6 | DoD PFAS need and a paid plasma precedent support G1; regulator acceptance, utility delay, $550k experiment, and inferred post-2030 pipeline keep it conditional. ~59.2. |
| P3R2-B-01 | S 64.6 | Hold-G1 | China liquid-cooling demand is proven; negative-pressure two-phase demand is not. Partner-only route and $3-8M v1 do not justify validation raw 4. ~59.6. |
| P3R2-B-06 | E | Elim | Binding ESC-localization/LOI condition not met; evidence favors in-house/full-stack domestic supply. |
| P3R2-B-14 | E | Elim | No buyer wants the dual-standard bridge; both named channels vertically integrate and G7 does not open. |
| P3R2-B-22 | E | Elim | No prognostics LOI; incumbents bundle predictive maintenance and the aging-fleet trigger is inference. |
| P3R2-C-01 | S 72.0 | Keep | Buyer specifications name the protection/grounding gap on both legs. Discount demand/niche/expansion for rapid platform-owner absorption. ~66.2. |
| P3R2-C-02 | E | Elim | Function is being standardized and supplied by named ecosystem vendors before 2030; commoditization gate is correctly fatal. |
| P3R2-C-03 | E | Elim | Missing hyperscaler RFI, crowded funded field, $1.2M experiment and $25-60M v1; 2030 entrant is late. |
| P3R2-C-04 | S 67.2 | Keep | Exact two-phase deployment plus regulatory fluid pressure supports a wedge; China is not chemistry-specific and $10-25M v1 is heavy. ~61.8. |
| P3R2-C-05 | E 69.2 | Recheck-G7 | Strong current conformance demand and excellent experiment, but no eligible 2028-2035 trigger. Reopen only with one; conservative conditional ~60.2. |
| P3R2-C-07 | E 60.0 | Elim | CN tender source is rejected in the ledger; US policy window narrows before launch and no durable buyer trigger replaces it. |
| P3R2-C-08 | S 62.2 | Keep | Operating/demonstration projects and essential PCHE function support demand; merchant sourcing, rapid-transient edge, $600k test, and $15-35M v1 cap upside. ~60.2. |
| P3R2-C-09 | E 64.4 | Elim | Equipment demand exists but modular-platform demand and an in-window trigger do not; incumbents expand before launch and China counterparty is restricted. |
| P3R2-C-12 | E 44.4 | Elim | Cryogenic need is real, but SPARC's plant is already procured; merchant 20K demand, capital path, and 2030 trigger fail. |
| P3R2-C-13 | S 63.2 | Hold-G1/G6 | Funded laser programs support the socket, but outsource willingness is unproven and the China buyer set must exclude Raycus. Validation raw 4 is generous; ~61.4. |
| P3R2-C-19 | E 48.4 | Elim | Derivative sCO2 demand does not prove a merchant cartridge; OEM sourcing unknown and capital path poor. |
| P3R2-C-21 | E 48.8 | Elim | R&D/vendor activity is not a campus procurement; incumbents already occupy the architecture and China is not reachable. |
| P3R2-C-22 | S 76.2 | Hold-G1 | Hydrogen hubs, stack sales, and targets prove the underlying market, not demand for a merchant degradation-emulation system. G1 pass -> fail pending buyer proof; ~64.6. |
| P3R2-D-01 | S 71.4 | Hold-G1 | Fusion/magnet spending does not yet buy a merchant quench subsystem. Frontier/elegance and capital are over-rewarded; counterfactual ~58.6. |
| P3R2-D-02 | S 80.0 | Keep | Best combination of direct category use, tape contracts, cheap experiment, dual-market timing. Discount direct THEVA incumbency and launch certainty: ~76.6. |
| P3R2-D-07 | E 51.8 | Elim | DOE R&D is not an MSDC retrofit order; no channel agreement or 2030 procurement trigger. The 15-point efficiency gain is not a 10x edge. |
| P3R2-D-08 | E 53.2 | Elim | Real sterilization capex, but regulatory forcing weakened and incumbents fill capacity before launch; no durable 2030 opening. |
| P3R2-D-09 | E 58.2 | Elim | Exact solicitation expired in 2023; technical pain is not a second current buyer source and no future regulatory wall is documented. |
| P3R2-D-10 | E 75.2 | Elim | Excellent near-term product, wrong company-formation date. Prime design and procurement decisions finish before 2030; do not rescue on score. |
| P3R2-D-11 | E | Elim | No buyer, industrial repetition-rate physics absent, sole-buyer roadmap favors CO2, and China is structurally closed. Science option only. |
| P3R2-D-12 | S 59.6 | Hold-G1 | Cooling/regulatory demand does not prove EHD co-development; consolidation points to build-in-house. Reduce validation raw 4; ~57.8. |
| P3R2-D-13 | S 67.6 | Hold-G1/10x | Directed-energy awards prove systems, not a thermal-magazine purchase. The 10x SWaP claim is a target, not demonstrated. ~61.4. |
| P3R2-D-16 | S 56.2 | Hold-G1/G7 | FSP funding is real, but merchant Brayton/PMAD demand waits on downselect; $500k experiment and $10-30M v1 make this a government option. ~53.0. |
| P3R2-D-18 | S 65.6 | Keep | Exact Army solicitation with price target is unusually product-specific. Second anchor and 10x cost result remain contingent; ~64.2. |
| P3R2-D-19 | S 60.4 | Hold-G7 | Exact architecture has been purchased, but by Piller; timing sources are mostly 2025-27 and lack a clean official 2028-35 trigger. Keep at ~60.4 only conditionally. |
| P3R2-D-20 | E | Elim | No liquid-metal BOP buyer/order, company-only roadmap, extreme materials/service burden, and science-only risk beyond 2030. |
| P3R2-E-02 | S 61.4 | Hold-G1/G7 | Regulation/backlog prove a cooling transition, not a merchant controller. US rule is contested and buy-vs-build unresolved. ~56.4. |
| P3R2-E-04 | S 65.4 | Hold-G1/G7 | QIS funding is not interconnect-loader procurement; IBM/SEEQC roadmaps can pre-empt the harness, $500k test and licensing burden matter. ~57.2. |
| P3R2-E-11 | E | Elim | CPO demand is real, but OSAT/foundry/switch incumbents internalize package thermal design before 2030. |
| P3R2-E-14 | S 76.2 | Hold-G1/geography | Strong US HVDC timing, but no merchant relay/HIL purchase. Dual-market raw 4 is indefensible: China is license-only and KR is optional. ~64.4. |
| P3R2-F-01 | S 73.8 | Hold-G6/G1 | Stored score first corrects to 71.8. Fast-match gap is real, but no paid evaluation and named CN accounts are restricted. US-only/rescoped ~64.8. |
| P3R2-F-02 | S 57.6 | Hold-G1 | Magnet programs and incumbent skid vendors prove a category, but no merchant standardized-skid buyer and CN demand is unconfirmed. ~54.4. |
| P3R2-F-03 | S 50.8 | Hold-G1/capital | Turbomachinery projects are real; every cited transaction is vertically integrated and no merchant cartridge order exists. $900k experiment. ~47.6. |
| P3R2-F-04 | E | Elim | Externalization thesis has no buyer on either leg; China substitution is already closing the route. |
| P3R2-F-05 | E | Elim | Zero-emission equipment grants do not buy repower kits; policy tailwind is being repealed and no certification-service buyer exists. |
| P3R2-F-06 | S 60.4 | Hold-G1 | HVDC projects/regulation and LEM incumbency prove the sensing category, not a merchant open socket. $300k facility-dependent test; ~55.4. |
| P3R2-F-07 | E 47.6 | Elim | End markets are large, but thermal/contact assemblies are already supplied or vertically integrated before launch. |
| P3R2-F-09 | E 39.0 | Elim | In-scope product demand absent; positive ITER evidence is outside primary geography and CEPC timing is adverse. |
| P3R2-F-10 | E 41.2 | Elim | Welding-equipment demand is not laser-UT demand; neither leg has a design-in or 2030 trigger. |
| P3R2-F-11 | E 29.6 | Elim | No MPW buyer, proposed coil-life milestone already beaten, and incumbent ultrasonic process dominates. |
| P3R2-F-12 | S 56.4 | Hold-G7/G6 | CCS rules and vessel fleet support G1, but product competition is intense and official post-2028 trigger/screened CN partner remain incomplete. |
| P3R2-F-15 | E 39.2 | Elim | No per-stack management tender; procurement is bundled and Kuqa uses in-house control. Policy is not a budget line. |
| P3R2-F-16 | E 57.4 | Elim | Current plasma-cleaner tenders do not request the metrology premium; no 2030 trigger and incumbents can absorb the feature. |
| P3R2-F-17 | E 46.4 | Elim | Standards work and voluntary guidance are not buyer demand; no enforcement/procurement trigger. |
| P3R2-F-19 | E 36.6 | Elim | Cooling-fleet growth and a mechanical incident do not prove chemistry-skid demand; incumbent convergence precedes launch. |
| P3R2-F-20 | E 42.8 | Elim | Current equipment orders do not buy merchant HV modules; competitor map refutes the dominant-vendor thesis and China is domestic-only. |
| P3R2-F-22 | E 30.8 | Elim | Component demand is real, but localization is already being captured and no buyer requests a second source. |
| P3R2-F-23 | S 59.0 | Hold-G1/G7 | Hydrogen awards/contracts do not buy the controller/logger; lender requirement is absent and the China evidence is alkaline, not PEM. ~52.2. |
| P3R2-G-01 | S 67.4 | Hold-G1 | Chamber awards and acceptance responsibility make this close to product demand, but no hydrogen-outgassing clause exists. Negative-search competition raw 4 -> 3; ~65.6. |
| P3R2-G-02 | E 40.2 | Elim | Accelerator/isotope growth is not merchant target/window demand; principal account has export-screening risk and no 2030 trigger. |
| P3R2-G-03 | S 67.0 | Hold-G1/G7 | Architecture change forces commissioning work but no buyer procures third-party instrumentation; dual/launch scores overstate inference. ~63.4. |

## Ranked substantive adjustment recommendations

These are recommendations, not edits. A failed hard gate eliminates the idea regardless of the counterfactual numeric score.

1. **Apply one product-demand rule to all batches.** Change G1 to fail pending product-specific buyer evidence for C-22 (pass/76.2 -> fail/~64.6), E-14 (pass/76.2 -> fail/~64.4), D-01 (marginal/71.4 -> fail/~58.6), G-03 (marginal/67.0 -> fail/~63.4), E-04 (pass/65.4 -> fail/~57.2), A-02 (marginal/55.2 -> fail/~52.0), B-01 (marginal/64.6 -> fail/~59.6), D-12 (marginal/59.6 -> fail/~57.8), D-13 (pass/67.6 -> fail/~61.4), E-02 (marginal/61.4 -> fail/~56.4), F-03 (marginal/50.8 -> fail/~47.6), and F-23 (marginal/59.0 -> fail/~52.2). Each rationale currently admits the proposed merchant product is unpurchased.
2. **Correct and rescope F-01.** Mechanical score 73.8 -> 71.8. As written, G6 marginal -> fail because the co-equal China base names Entity-Listed buyers and an unsafe Hong Kong structure. If rewritten US-only with clean China upside excluded, use ~64.8 after high-niche 4->3, 10x 5->4, dual 3->2, and launch 4->3.
3. **Protect the 2030 gate from score rescue.** Keep D-10 eliminated at 75.2. Keep C-09 (64.4), C-05 (69.2), F-16 (57.4), and D-09 (58.2) eliminated until an eligible product-specific 2028-2035 trigger exists. C-05 is the first recheck, not an automatic reinstatement.
4. **Downgrade D-02 modestly, not punitively.** Keep G1/G7 pass; score 80.0 -> ~76.6 for competition 3->2 (THEVA/TAPESTAR is direct) and launch 5->4 (capacity growth does not guarantee a new entrant's design win).
5. **Downgrade A-14's 10x/timing narrative.** Keep gates; score 74.0 -> ~70.4 for 10x 4->3, launch 5->4, expansion 4->3. A 300C capability class is valuable but not an evidenced order-of-magnitude customer metric.
6. **Calibrate C-01 to the buyer specification, not a booked product.** Keep/conditional pass; 72.0 -> ~66.2 for demand 4->3, niche 4->3, expansion 4->3. Repair the stale `L02-043` alias.
7. **Calibrate G-01's whitespace.** Competition 4->3 and 67.4 -> ~65.6; absence of an integrated product in a search is not proof of high whitespace. Keep G1 marginal until a paid acceptance clause or fabricator order appears.
8. **Calibrate C-04 for capital and chemistry specificity.** 67.2 -> ~61.8 for demand 4->3, launch 5->4, expansion 4->3. The China leg supports liquid cooling, not the PFAS-free two-phase premium; v1 is $10-25M.
9. **Calibrate A-05's validation and negative-search claims.** 66.8 -> ~63.2 for competition 4->3 and validation 4->3. The $250k experiment is at the ceiling, v1 reaches $6M, and no direct price/TAM was found.
10. **Calibrate D-18's 10x claim.** Keep conditional pass; 65.6 -> ~64.2 for 10x 4->3. The Army's $300k target versus a $1-3M comparison frames an aspiration; it does not demonstrate cost per steered watt.
11. **Do not count E-14 as dual-market leverage.** In addition to the G1 hold, dual-market raw 4 -> 2: US is the base, China is unproven license-only upside, and Korea is optional. This is the largest geography inflation in the surviving set.
12. **Treat A-10 as US-only or eliminate.** G6 marginal -> fail as written; the named China accounts are structurally blocked. With China removed and product demand still conditional, 62.0 -> ~57.2.
13. **Make A-21/A-22/D-19/F-12 prove persistence.** Retain only as G7 holds until each has a primary 2028-2035 product procurement, refit, standard, or capacity trigger. Present programs and general installed-base persistence are insufficient.
14. **Repair source eligibility before honoring any raw score above 3.** Resolve/dedupe stale IDs; replace demoted/rejected sources; prohibit idea-local cross-citation unless the canonical record carries both idea IDs; populate missing `claim_supported`; then rerun the validator.
15. **Redesign the experiment portfolio before final selection.** The present longlist has zero sub-$100k experiments, making the final-24 gate mathematically impossible. Require at least eight genuinely decisive sub-$100k tests, not relabeled partial tests, and downgrade validation scores where sellable v1 is not plausibly below $5M.

## 10x, commoditization, science-only, and export-control audit

### 10x edge

- Only F-01 has a measured order-of-magnitude speed gap against a named incumbent class, but buyer value and export-safe market access remain unproven.
- A-14 (temperature class), D-07 (15-point efficiency), D-10 (unproven production-effort collapse), D-18 (target cost), and E-04 (8x channels / 5x heat) should not be raw 4 on current evidence.
- D-13's 10x chiller SWaP is physically plausible for burst duty but remains a system target; keep at raw 3 until a duty-cycle-matched brassboard proves it.

### Commoditization/incumbent convergence before 2030

- Correct eliminations: C-02, C-03, E-11, F-07, F-19, F-22, and F-16.
- High-risk survivors/holds: C-01 (platform owner may absorb protection), C-04/B-01/E-02/D-12 (cooling consolidation), F-01 (incumbent roadmap unknown), E-04 (on-chip/optical links), G-03 (commissioning absorbed by OEM/integrator), and A-13 (vertically integrated propulsion).

### Science-only or procurement-fragile after 2030

- Correct eliminations: D-11, D-20, C-12, F-09, and D-07.
- Holds: D-16 remains a single US government-program option; E-04 depends on quantum scaling architecture; D-01 depends on fusion/magnet buyers externalizing protection; G-01 is protected by live paid chamber awards but remains China-big-science concentrated.

### Structural export-control blocks

- A-10: named China buyers are restricted; China must be removed from the base case.
- F-01: NAURA/Piotech and affiliate-rule exposure make the recorded China structure unsafe; pull counsel to the first gate and use a clean US-only base.
- C-13: Raycus is excluded; no China score without a separately screened buyer and domestic-content chain.
- C-09/G-02/F-20: CGN-linked accounts cannot support a casual dual-market thesis; current eliminations are reinforced.
- F-12: no US-origin technology transfer until the CN partner passes CSSC/affiliate screening.
- E-04: quantum/cryo licensing and deemed-export lead time materially weaken the Taiwan/Korea manufacturing/test path, though not the US base.

## Provisional ranked top-32 P5 review pool

This is the closest defensible answer to a requested top 32. It is **not** a claim that 32 ideas pass all hard gates. `Advance` means the present gate case is defensible enough for red-team. `Conditional` means P5 may review it only to resolve the named gate; absent that evidence it is eliminated. Adjusted scores are calibration estimates, not canonical edits.

| Rank | Idea | Audit score | Status | Required condition / why retained |
|---:|---|---:|---|---|
| 1 | P3R2-D-02 | 76.6 | Advance | Direct metrology use, contracts, cheap experiment; red-team THEVA and China screening. |
| 2 | P3R2-A-14 | 70.4 | Advance | Strong 2030 geothermal trigger and supply gap; prove buyer-valued edge. |
| 3 | P3R2-C-01 | 66.2 | Advance | Buyer specs name the protection gap; test platform absorption and repair citation alias. |
| 4 | P3R2-G-01 | 65.6 | Conditional | Obtain paid outgassing/acceptance clause; keep China concentration visible. |
| 5 | P3R2-F-01 | 64.8 | Conditional | US-only rescope, clean G6, and paid fast-match evaluation. |
| 6 | P3R2-C-22 | 64.6 | Conditional | Named OEM/financier procurement or paid beta for the test system. |
| 7 | P3R2-E-14 | 64.4 | Conditional | Merchant relay/HIL buyer evidence; US-only score, not dual. |
| 8 | P3R2-D-18 | 64.2 | Advance | Exact solicitation; require award/second product anchor and measured cost edge. |
| 9 | P3R2-G-03 | 63.4 | Conditional | Paid third-party acceptance-instrument frame agreement and in-window persistence. |
| 10 | P3R2-A-05 | 63.2 | Advance | Real procurement/category; obtain price/TAM and second-source buyer validation. |
| 11 | P3R2-C-04 | 61.8 | Advance | Exact two-phase deployment/regulation; prove fluid lifetime and sub-$5M wedge. |
| 12 | P3R2-C-13 | 61.4 | Conditional | Paid outsource evaluation and clean China buyer; keep defense/commercial split. |
| 13 | P3R2-D-13 | 61.4 | Conditional | Thermal-subsystem procurement signal and duty-cycle brassboard 10x proof. |
| 14 | P3R2-D-19 | 60.4 | Conditional | Eligible 2028-2035 trigger and merchant whitespace versus Piller. |
| 15 | P3R2-C-08 | 60.2 | Advance | Merchant PCHE order/sourcing proof; capital partner and transient qualification. |
| 16 | P3R2-C-05 | 60.2 | Conditional recheck | Add a primary 2028-2035 conformance/procurement trigger; otherwise remains eliminated. |
| 17 | P3R2-B-01 | 59.6 | Conditional | Buyer request for negative-pressure/two-phase architecture and credible CN partner. |
| 18 | P3R2-A-22 | 59.2 | Conditional | Regulator acceptance plus named post-2028 remediation procurement; shrink test budget. |
| 19 | P3R2-D-01 | 58.6 | Conditional | Quench-protection RFP/LOI or paid coil program; avoid fusion/HTS familiarity inflation. |
| 20 | P3R2-D-12 | 57.8 | Conditional | EHD-specific OEM co-development and outside-licensor socket. |
| 21 | P3R2-A-10 | 57.2 | Conditional | US-only legal base and paid IEDF/control retrofit evaluation. |
| 22 | P3R2-E-04 | 57.2 | Conditional | Loader/readout procurement, architecture survival, and license-aware build path. |
| 23 | P3R2-E-02 | 56.4 | Conditional | Merchant-controller buyer/LOI and durable regulatory trigger. |
| 24 | P3R2-F-12 | 56.4 | Conditional | Official post-2028 vessel/refit trigger and screened domestic partner. |
| 25 | P3R2-F-06 | 55.4 | Conditional | OEM/EPC merchant sensing socket and written high-current facility access. |
| 26 | P3R2-F-02 | 54.4 | Conditional | Standardized-skid buyer/LOI; independently prove China leg or remove it. |
| 27 | P3R2-A-13 | 54.0 | Conditional | PPU-specific solicitation/design-in and funded post-2028 constellation continuity. |
| 28 | P3R2-D-16 | 53.0 | Conditional | FSP downselect to an addressable architecture and <$5M sellable wedge. |
| 29 | P3R2-F-23 | 52.2 | Conditional | Lender/OEM requirement or paid logging-controller pilot; correct PEM/CN mismatch. |
| 30 | P3R2-A-02 | 52.0 | Conditional | Breaker-specific pilot/RFP plus sponsored <$250k decisive module experiment. |
| 31 | P3R2-A-21 | 51.0 | Conditional | Post-2028 charger procurement and a much smaller decisive experiment. |
| 32 | P3R2-F-03 | 47.6 | Conditional | Merchant cartridge co-development/order and sponsored test facility; otherwise cut first. |

Pool notes:

- The 32 span 15 lanes but are overconcentrated in L14; P5 should not confuse a red-team pool with a diversity-compliant final portfolio.
- D-10 is the highest-scoring excluded near-miss and remains excluded because its design window closes before formation. F-16 and C-09 remain excluded for the same timing/commoditization discipline.
- If the 25 conditions cannot be resolved with eligible evidence, the honest outcome is fewer than 32 P5 survivors, not relaxed gates.

## Final audit disposition

**P4 substantive status: FAIL / REPAIR REQUIRED.** The strongest ideas are worth preserving, but score inflation, product-demand transference, inconsistent marginal-gate treatment, capital infeasibility, source/citation defects, and 2030 timing inconsistencies are large enough to change both rank and survivor membership. Repair the 107 machine errors, enforce the G1/G7 interpretation above, redesign the sub-$100k experiment set, and only then freeze the P5 top 32.
