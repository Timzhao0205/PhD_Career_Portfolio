# DD_C33 — Cryogenic Current-Distribution & Quench-Onset QC Instruments for HTS Coil Production

**Candidate:** C33 · **Analyst prefix:** DD-C33 · **Date:** 2026-07-03 · **Sources:** 18 (see `DD_C33_sources.json`)
**Red-team status:** REDTEAM_C33.md (kill-probability ~75%) is engaged head-on. Outcome in brief: the **patent-blocking claim is overturned on the actual claim language** (§4.1), the **fiber-vs-Hall architecture question is resolved by repositioning the product as sensor-agnostic analytics + fixturing** (§2), but the **~20-buyer market critique substantially survives the recount** (§5), and the honest structural answer is that C33 lives as **C12's QC module / a bootstrap instrument line, not a standalone venture** (§10).

---

## 1. Problem & who has it

Every HTS magnet program cold-tests coils before assembly, because winding and splicing defects are invisible until cryogenic current flows. BNL's practice is canonical: every REBCO pancake is tested at 77 K "before assembling the final magnet" to verify Ic, n-value (20–32 across good coils), and splice resistance — and some double-pancake assemblies were **rejected as unsuitable** after showing broad voltage onsets and depressed Ic [DD-C33-07]. For no-insulation (NI) coils the problem is worse and newer: the coil's electromagnetic behavior is set by turn-to-turn contact resistance, which NHMFL measured to vary ~55% across winding tensions (2.22 / 1.73 / 1.42 μΩ at <1, 3, 5 kgf) and to roughly **double from 0 to 14 T** — directly changing charging time constants, current redistribution during faults, and quench survivability [DD-C33-06]. A voltage tap tells you almost nothing about an NI coil (current bypasses defects resistively); the information lives in the **magnetic field distribution**, i.e., in the current distribution.

Named archetypes who feel this in 2026–2031:

- **Fusion coil-line managers.** ~50 private fusion companies worldwide (FIA's 2026 report surveyed 25, "approximately half") with supply-chain spend of $538M in 2025 → $681M projected 2026 [DD-C33-10]. Each HTS device is dozens of coils: Energy Singularity's HH70, first plasma June 2024, is an all-HTS tokamak whose every magnet had to be qualified before stacking [DD-C33-16]. A scrapped fusion-grade TF coil is a $0.5–3M event (ASIPP's tender for a single D-shaped HTS magnet *system* was budgeted RMB 6.38M ≈ $0.9M [DD-C33-11]).
- **Test engineers at magnet OEMs** (MRI/NMR/research magnets). Ningbo Jianxin (global #5 MRI-magnet supplier by installations, revenue RMB 579M in 2025) already staffs "quality inspection personnel at each critical production phase" under ISO 13485 [DD-C33-12] — today with voltage/field-homogeneity rigs designed for insulated LTS coils, not NI-HTS.
- **Tape producers' application labs.** Tape-level QC is solved — THEVA's TAPESTAR does non-contact continuous Ic scans with mm resolution and "all well-known tape producers rely on this method" [DD-C33-08]. **Nothing equivalent exists one level up, at the wound-coil level.** That gap — TapeStar-for-coils — is the whole candidate.

The quantified niche: organizations that will wind NI/MI-HTS coils in repeated production (not one-offs) between 2029 and 2032 — counted in §5 at **~25–40 organizations globally**, of which ~8–15 are realistic instrument buyers.

## 2. Product definition & the extreme-performance edge

**Product: a coil-level cryogenic QC station — "TapeStar for coils" — that is deliberately sensor-agnostic.** Three layers:

1. **Fixture:** 77 K (LN2) test bed for pancakes/double-pancakes up to ~1.2 m OD; motorized coil handling; programmable current source (up to ~1 kA) executing charge/discharge/sudden-discharge excitation protocols. Staying at 77 K keeps cost down and avoids the sub-4 K cryocooler ECCN trap (§7).
2. **Sensing:** default transducer is a multiplexed **Hall-sensor array** (10²–10³ channels) scanned or fixed around the coil — the founder's literal PhD craft. But the chassis ingests **any channel type**: co-wound fiber readout, voltage taps, pickup coils. The sensor is not the product.
3. **Software (the actual moat attempt):** model-referenced signature analysis. Not general field-to-current inversion — which the red team correctly calls ill-posed — but (a) **parametric fits** of few-parameter circuit models (contact-resistance distribution, joint resistances, local Ic depressions) to transient field responses, exactly the technique LBNL demonstrated with Hall arrays + inverse Biot-Savart on CORC CICC terminations, extracting per-cable termination resistances and critical currents and flagging conductor damage — with the authors explicitly noting "promise for **quality control**… identifying poor joints before strenuous magnet operation" [DD-C33-03]; (b) **golden-signature anomaly detection** against the fleet's accumulated per-coil database; (c) a pass/fail certificate with Rc, joint-nΩ, and defect-localization outputs plus predicted charging constant.

**Edge, quantified:** today's alternatives are (i) a full Ic/n-value dunk test (BNL-style), which gives one scalar pair and finds gross defects only after hours of instrumented setup [DD-C33-07]; (ii) in-house one-off rigs; (iii) nothing. No commercial instrument outputs an NI coil's contact-resistance map or joint-resistance vector non-invasively. Lake Shore — the incumbent cryogenic Hall vendor — sells probes and gaussmeters, not array systems or mapping stations [DD-C33-09]; THEVA stops at the tape [DD-C33-08]. The 10x claim is honest but narrow: **per-coil physics data where the current standard is a single Ic number or nothing.**

**Fiber vs Hall, resolved honestly.** For *operational quench protection inside magnets*, fiber has won the architecture argument: FBG/ULFBG on VIPER cable at SULTAN achieved SNRs of 4–32, roughly 3–30× better than co-wound voltage taps, with fibers embedded into the cable jacket at manufacture [DD-C33-04]; ASIPP is qualifying its own fiber quench detection for China's next-generation fusion conductors, 0.3–2.2 s ahead of voltage taps [DD-C33-05]; Chinese literature and at least one fusion startup (Startorus, own quench-detection patent filing) confirm in-house fiber/electrical paths [DD-C33-17][DD-C33-18]. **C33 must not fight that battle.** A factory instrument measures coils that (a) may have no fiber, (b) come from many vendors, (c) need their *manufacturing quality* graded, not their thermal runaway caught. External field mapping is the only modality that is non-contact, retrofittable to any finished coil, and measures the quantity the customer actually ships (current distribution). Fiber and Hall are complements across the product's boundary — and the sensor-agnostic chassis means that if a customer's coils arrive with co-wound fiber, the station reads it too.

## 3. Technical feasibility & TRL path (2029–2031)

- **What exists:** every ingredient is published. Hall-array + inverse-model current-distribution monitoring: demonstrated at 76 K on three-cable CICC with quench detection at 2,000 A/s ramps and damage identification [DD-C33-03]. 77 K coil acceptance testing: routine since the 2010s [DD-C33-07]. NI contact-resistance physics: quantified [DD-C33-06]. Founder capability: in-situ GaN Hall-array sensing inside an operating stellarator is his thesis — this is the portfolio's strongest capability match; integration TRL 4–5 today, instrument TRL 8 achievable in 12–18 months.
- **BOM sketch (v1, ~$60–110K COGS at ASP $200–300K):** LN2 open dewar + fixture plate ($10–20K), 0.5–1 kA programmable supply ($15–30K), 128–512 ch Hall array on flex/rigid PCBs with custom mux/readout ($10–25K built in-house — his exact skill), nV-class joint-resistance channel, motion axes ($8–15K), industrial PC + software. **Cleanroom dependence: none** (commercial Hall dies or his packaged GaN sensors purchased as dies).
- **Hard parts:** (a) inversion identifiability — mitigated by transient-excitation protocols and parametric (not free-form) models [DD-C33-03]; (b) fixturing diversity across coil geometries (pancake vs racetrack vs D-shape) — v1 scope: planar pancakes/double-pancakes ≤1.2 m; (c) calibration traceability at 77 K; (d) the sales problem, which is not technical (§5).
- **What is bought vs built:** everything except the array readout, fixture, and software is COTS. No sub-4 K stage in v1 (deliberate, §7).

## 4. Competitive landscape — global and China

### 4.1 The Tokamak Energy patents: analyzed, not feared

This was the red team's kill shot; the claim language does not support it.

- **US11749434B2** (granted 2023, priority 2019-11-12, expires 2040-11-10, Tokamak Energy). Claim 1 is a *method* requiring, verbatim elements: a superconducting magnet "comprising **a plurality of HTS field coils**" (NI-type, radial current sharing); "monitoring strain and/or a magnetic field of **each** HTS field coil"; "**comparing** the monitored [signal] for each HTS field coil **to the monitored [signal] of at least one other HTS field coil of the plurality**"; and determining quench likelihood "in response to said comparison" [DD-C33-01]. It is a **coil-to-coil differential scheme for an assembled multi-coil magnet** (dependent claims narrow to tokamaks/TF sets). A factory QC station that measures **one coil at a time on a test fixture** and compares it to a **stored reference model / golden dataset** — outputting manufacturing metrics, not a quench-likelihood determination for a magnet — omits at least two express claim elements (the plurality, and the inter-coil comparison). Literal infringement: no. Doctrine-of-equivalents: weak, since "another coil of the plurality" is an explicit limitation that model-referencing does not equivalently meet. Design rules to hold the line: single-coil-vs-model architecture only; market it as *manufacturing metrology* (Rc, joints, defect localization), never as "quench detection" for operating magnets; FTO opinion on the family (EP/JP members, continuations) before first sale — a $15–30K counsel exercise, not a company-killer.
- **US11101059B2** (priority 2017, expires 2038) requires "a **secondary HTS tape**… divided into a plurality of strips… connected in series" plus an energy-dump protection unit [DD-C33-02]. A Hall-array/fiber-agnostic QC instrument contains neither element. Irrelevant to C33; the red-team file's framing of this patent as a direct threat was wrong.
- Residual patent risk: Tokamak Energy, CFS, and Chinese players (Startorus [DD-C33-17]) keep filing in quench detection; the crowded space raises FTO-monitoring overhead and, more importantly, **signals that flagship buyers treat this as internal IP** — a demand problem more than a legal one.

### 4.2 Global competitors

| Player | Offering | Gap vs C33 |
|---|---|---|
| THEVA TAPESTAR [DD-C33-08] | Non-contact Ic scan of **tape**, mm resolution; de-facto standard at tape producers | Stops before winding; captures upstream defect-screening value (shrinks C33's claim to winding/joint/assembly defects — conceded) |
| Lake Shore, Senis, Metrolab class [DD-C33-09] | Cryo-capable Hall probes, gaussmeters, mappers | Components, not coil-QC stations; any could package one in ~2 quarters if demand appears — low entry barrier confirmed |
| MIT/CFS fiber lineage [DD-C33-04] | Co-wound/embedded fiber quench detection | Operational protection, not vendor-neutral factory QC; complementary if C33 is sensor-agnostic |
| In-house rigs (BNL-style dunk tests [DD-C33-07]; every integrated fusion company) | 77 K Ic/n-value acceptance | The real incumbent: "good enough" scalar QC at near-zero marginal cost |

### 4.3 China landscape (中文调研)

- **Scale and trajectory:** China's superconducting-magnet industry is estimated at ~RMB 92B for 2025, projected >RMB 200B by 2030 (智研咨询; broad definition including MRI and photovoltaic monocrystal-furnace magnets) [DD-C33-14]. HTS tape: 上海超导 ships ~4,000 km/yr, is building a RMB 2.5B base targeting 15,000+ km/yr within 2–3 years, and serves 180+ customers [DD-C33-13]; second-tier producers 东部超导、上创超导 etc. [DD-C33-14].
- **Coil fabs:** 能量奇点 (HH70 all-HTS tokamak, first plasma 2024-06 [DD-C33-16]), 星环聚能 (files its own 失超检测 patents [DD-C33-17]), ASIPP/CRAFT-BEST ecosystem (procures whole HTS magnet systems by 招标, e.g., RMB 6.38M D-coil system [DD-C33-11]), 联创光电/联创超导 (HTS induction heating, 70+ orders 2023), 西部超导 (LTS wire-to-magnet integration, ~95% domestic LTS share), 健信超导 (MRI magnets, RMB 579M revenue) [DD-C33-15][DD-C33-12][DD-C33-14].
- **QC behavior:** no Chinese commercial coil-level QC instrument vendor was found in Chinese-language searching (带材检测 equipment exists; 线圈级 does not) — the gap is real in China too. But the buyers' revealed behavior is in-house: ASIPP develops its own fiber quench detection for CFETR-class conductors [DD-C33-05], Startorus patents its own detection [DD-C33-17], Jianxin runs its own stage-gate inspection under ISO 13485 [DD-C33-12]. 高端仪器 (high-end instruments) is a named 十五五 攻关 category, so a *China-domiciled* instrument maker would enjoy 首台套 insurance subsidies and the 2026 20% procurement preference — but that same machinery guarantees a domestic clone fast, and the biggest Chinese buyers are CAS-system entities where a US-person founder faces screening friction in both directions (§7).

## 5. Market: bottom-up beachhead, expansion, TAM/SAM/SOM

**The mandated recount of the "~20-buyer TAM," with arithmetic.** Candidate organizations winding HTS coils repeatedly, 2029–2032:

- **A. Fusion, ex-China:** ~50 private companies [DD-C33-10]; HTS-magnetic-confinement subset ≈ 20–25; with in-house coil lines by 2030 ≈ 12–16; **minus** the 4–6 vertically integrated leaders whose QA stacks are internal IP (CFS, Tokamak Energy, Proxima, Energy-Singularity-equivalents) → **8–12 candidate buyers**.
- **B. China coil fabs:** 能量奇点, 星环聚能, 中国聚变能源公司, ASIPP/CRAFT-BEST suppliers, SWIP, 联创超导, 瀚海聚能-class newcomers ≈ 6–9 orgs; realistically sellable to a US-linked vendor after in-house preference and screening ≈ **2–4**.
- **C. Non-fusion OEMs & labs:** MRI/NMR magnet makers where HTS/NI is entering (健信, Siemens/GE/Philips advanced programs, Bruker/JEOL, Sumitomo/JASTEC) ≈ 4–6 relevant; research-magnet OEMs (Oxford Instruments, Cryogenic Ltd, AMI, Cryomagnetics, HTS-110, Canyon-class startups) ≈ 4–6; induction-heating/motor producers ≈ 2–4; accelerator/high-field labs (NHMFL, CERN, CHMFL合肥强磁场, IHEP, KEK, PSI) ≈ 4–6 → **14–22 candidates**.
- **D. Tape producers** (coil application labs at 上海超导, Faraday, Fujikura, SuperPower, SuNAM, THEVA…): they buy TapeStar-class tape QC [DD-C33-08]; coil-level only where they forward-integrate → **2–4**.

**Total candidate pool ≈ 26–42 organizations.** Realistic conversion by 2032 (capital instrument, conservative culture, in-house alternative) 30–40% → **8–15 buyers × 1.5 systems avg = 12–23 systems cumulative**. At ASP $150–300K: **cumulative hardware $2.5–7M through 2032**, i.e., ~$1–2.5M/yr, plus software/calibration subscriptions ($20–40K/system/yr) → **steady-state ~$2–4M/yr total by 2033**. The red team's "~$1M/yr" was mildly pessimistic; the corrected figure is 2–4×, **which changes nothing strategically** — this is a profitable micro-niche, not a venture market.

**Top-down triangulation:** fusion supply-chain spend $538M (2025) → $681M (2026E) [DD-C33-10]; magnets plausibly 25–50% of device value; QC/test-instrument capex historically 1–2% of production spend → $1.5–7M/yr — consistent with the bottom-up figure. Bull case (2035: HTS coil production 5–10× on fusion pilot plants + HTS-MRI adoption, pool 60–100 orgs): TAM $10–25M/yr. Even the bull case is below a venture-scale SOM.

**Expansion paths that could change the ceiling:** (i) become the **QC/data module inside C12's winding cells** (inline Rc estimation during winding + end-of-line certification — one integrated data product); (ii) **coil test-as-a-service** (per-coil certification fees, $5–15K/coil, for startups without cryo test capacity); (iii) drift up to **commissioning-support instrumentation** for whole magnets — but that path walks toward US11749434B2's claims and is deliberately out of scope (§4.1).

## 6. Go-to-market: China vs US sequencing

- **US/EU-first (recommended if pursued at all).** Reference-customer strategy: (1) 2029 — one national-lab/high-field-lab lighthouse (NHMFL-class) with a subsidized unit and a joint SUST/IEEE-TAS methods paper; scientific buyers procure publicly and cite loudly. (2) 2030 — 2–4 second-wave fusion companies and research-magnet OEMs, pitched as "vendor-neutral coil certification your customers will trust" (an *external* certificate is worth more than an internal test when selling coils — the OEM segment C, not the integrated leaders, is the wedge). Channel: founder-led direct sales at ASC/MT conferences; partnership with tape vendors to chain TapeStar defect maps into coil signatures [DD-C33-08].
- **China sequence:** as a US person, direct China-first is legally *possible* (instruments are not an OISP-covered sector today) but commercially poor: the demand core is CAS/fusion-national-team entities that (a) prefer 国产 instruments under procurement rules, (b) develop QC in-house [DD-C33-05][DD-C33-17], and (c) increasingly sit near Entity-List screening obligations. The founder's China network is better used for component supply (Hall dies, fixturing, LN2 hardware at 60–70% of Western cost) and for monitoring the fastest-scaling coil fabs as a *market-intelligence* channel. If C33 lives inside a C12 bundle, China strategy defaults to C12's (software/licensing only).

## 7. Regulatory & geopolitical exposure (coordinated with POLICY_BRIEF.md)

Per the Phase 5 brief, C33 maps between archetypes (a)/(c)/(i) [P-01…P-15 in `50_PHASE5_POLICY/policy_sources.json`]:

- **Item level:** a 77 K LN2-based QC instrument with Hall arrays is almost certainly **EAR99**; quench/QC electronics are not named in any reviewed ECCN (POLICY_BRIEF §1.2, archetype c). The two traps to design out: **3A904** — do not put a sub-4 K pulse-tube cryocooler in the product (keep v1 at 77 K; sell 20–50 K conduction-cooled variants only with classification review), and bundling with controlled magnets (3A001.e.3/3A201) — sell the instrument, never the magnet.
- **Activity/customer level:** sales to CAS institutes require Entity-List screening; the Affiliates Rule (reactivating 2026-11) demands ownership-tree diligence on every Chinese customer (POLICY_BRIEF §1.3). Fusion is flagged as a plausible future BIS/Treasury designation area — build so a designation forces a market exit, not a violation (§5 cross-cutting logic).
- **Outbound (OISP/COINS):** instruments are **not a covered sector today**; founding a Chinese entity for this would still be a covered *transaction type* if the activity list expands by ~2027 (POLICY_BRIEF §2). US-first structure avoids the question entirely.
- **Certification burden:** CE/UL machine safety + LN2 handling only; no medical/nuclear certification attaches. **Nothing here makes the idea infeasible; nothing here rescues its market either.**

## 8. Capital & milestones (2029 → 2032)

Standalone plan (for completeness): pre-seed/seed **$1.5–2.5M** (2029H1); team of 2–3; v1 station in 12 months; first sale 2030H1 via lighthouse lab; 4–6 systems + 2 service contracts by end-2031 → revenue **$1.2–2.2M (2031)**, near breakeven at 4 staff. Series A: **not raisable on this TAM** — the honest capital plan is bootstrap-to-profitability or fold-in. Bundled plan (recommended): C33 is a **$150–250K option module + software subscription on C12's winding cells**, adding 20–30% ASP and the recurring-revenue layer C12 needs to clear its own K2 kill criterion (software+QC ≥15% of revenue) — one company, one seed round, two SKUs.

## 9. Risks & kill criteria

**Risks, ranked:**
1. **Demand thinness (dominant):** buyers' revealed preference is in-house QC [DD-C33-05][DD-C33-12][DD-C33-17]; the pool is ~30 orgs and the strongest ~6 will never buy. Probability the standalone thesis fails on this alone: high (red-team ~75% is fair for the standalone framing).
2. **Low entry barrier:** Lake Shore/Senis-class vendors can package probe+software quickly [DD-C33-09]; Chinese clone within ~2 years of first CAS-adjacent sale.
3. **Fiber pre-emption at manufacture:** if co-wound fiber becomes standard *in coils* (not just cables) and vendors certify coils off the fiber channel, the external-array value shrinks to fixturing (sensor-agnostic design is the hedge) [DD-C33-04][DD-C33-05].
4. **FTO drift:** feature creep toward multi-coil, in-operation monitoring walks into US11749434B2 claim territory [DD-C33-01]; requires standing discipline plus family monitoring.
5. **Diagnostics-cap portfolio logic:** as a solo-founder first company, a $2–4M/yr instrument line consumes the 2029 launch window that stronger candidates need.

**Kill criteria (pre-committed):**
- **K1 (demand):** <3 written buy-intents at ≥$150K from distinct organizations after the 2026–2027 interview sprint (below) → kill standalone; retain as C12 module only.
- **K2 (pre-emption):** by end-2028, ≥2 major coil OEMs ship coils with factory-integrated fiber certification as standard → kill the Hall-array-led version; keep analytics/fixture layer only.
- **K3 (FTO):** counsel review finds blocking claims in the TE family (continuations/EP) reading on single-coil model-referenced metrology → kill or license.
- **K4 (bundle test):** if C12 itself dies at its K1 gate and C33 has <$500K ARR pipeline standalone by mid-2030 → wind down.

## 10. Verdict

**Conviction: LOW as a standalone venture-scale company; MEDIUM-HIGH as a product module and validation vehicle.** The deep dive overturns two of the red team's three pillars — the Tokamak Energy patents do **not** block a single-coil, model-referenced factory instrument (the claim language requires inter-coil comparison in an assembled magnet [DD-C33-01], and US11101059B2 requires a striated HTS sensing tape [DD-C33-02]), and the physics is not a research bet (LBNL demonstrated the exact method and named QC as an application [DD-C33-03]). But the third pillar — market size — survives the recount: **~26–42 candidate organizations, 8–15 realistic buyers, ~$2–4M/yr steady state**. That is a good product line and a bad company. The correct disposition: **build C33 as the QC/data module of the C12 winding-cell family** (where it supplies exactly the recurring-software layer C12's venture case is missing), and as the founder's cheapest possible credibility engine — it is the strongest capability match in the portfolio, so its validation is nearly free.

**Cheapest validation experiments (2026–2028, during the PhD):**
1. **Joint C12/C33 interview sprint (~$3K):** 15+ structured interviews at ASC 2026 / MT-29 with coil-line and test engineers (segments A/C). Ask two prices: winding cell, and standalone coil-QC station. Success gate: ≥3 written "would pay ≥$150K" for the QC station alone. Directly tests K1 three years early.
2. **77 K seeded-defect demo (<$12K, personal equipment, no Stanford IP):** wind 6–10 small NI pancakes from offcut tape with deliberate defects (low-tension zones, degraded splices, tape nicks); measure external Hall-array transient signatures vs a parametric model; publish a defect-detection ROC curve in SUST/IEEE TAS. One paper simultaneously validates C33's physics and C12's inline-QC claim, and establishes the founder as *the* name in NI coil metrology.
3. **Paid signature-measurement pilot ($0 capex beyond #2):** offer the portable rig as a $10–25K per-campaign coil-characterization service to 1–2 magnet startups or labs in 2027–2028. If nobody pays even for the service, K1 triggers and the standalone idea dies for $0; if they do, the C12 bundle gains a reference customer before incorporation.

**Kill criteria:** K1–K4 above; K1 (three written buy-intents by end-2027) governs.
