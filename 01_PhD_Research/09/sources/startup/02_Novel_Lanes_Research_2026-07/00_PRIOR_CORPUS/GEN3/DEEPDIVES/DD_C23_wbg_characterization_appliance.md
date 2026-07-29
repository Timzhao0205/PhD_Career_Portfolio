# DD-C23 — JEDEC-compliant automated WBG characterization appliance (DPT + dynamic-Ron + short-circuit ruggedness)

**Candidate:** C23 · **Red-team kill probability going in: 75%** · **Sources:** `DD_C23_sources.json` (26 unique; cited inline as [DD-C23-xx])

This deep dive was written against an adversarial red team whose core finding — "the founding premise 'no product exists' is false" — is **confirmed**. The report therefore reframes C23 from "create the category" to "is there a defensible tier inside an existing category," and answers the four mandated resolution points explicitly (§2, §4, §6, §7).

---

## 1. Problem & who has it

Every SiC/GaN device maker, module maker, automotive tier-1, and power-electronics lab must generate dynamic switching data (double-pulse test, DPT), GaN dynamic RDS(on), and ruggedness data (short-circuit withstand, avalanche) to publish datasheets, qualify parts, and select devices. The physics is unforgiving: DPT accuracy is dominated by fixture parasitics, probe deskew, and bandwidth — a mainstream conference tutorial exists solely on how to build the setup correctly [DD-C23-10]. GaN adds trapping-driven dynamic-Ron, standardized only at the method-guideline level (JEP173, JEDEC JC-70's first document, 2019) and known to give method-dependent results [DD-C23-07][DD-C23-09]. SiC short-circuit withstand is measured in single-digit microseconds at rated bus voltage — commercial 1200 V parts survive "only several microseconds" at 750 V bus [DD-C23-11][DD-C23-12] — so ruggedness testing is a controlled-destruction discipline requiring purpose-built containment.

In June 2026 JEDEC's JC-70 committee (now 70+ member companies, up from 23 at its 2017 founding) published **JEP203** (*Guideline for Short Circuit Evaluation in Power Conversion Transistors*) and **JEP204** (*Catalog of Stress Procedures for SiC Devices*) [DD-C23-06][DD-C23-08]. NASA's GaN Body of Knowledge likewise flags reliability-evaluation limitations as a barrier to adoption [DD-C23-25]. The same month, the UK's CSA Catapult launched an automated DPT *service* (1.5 kV / 1 kA, 25–150 °C, IEC 60747-8-4-compliant) explicitly because device makers and OEMs need this data and many can't produce it well in-house [DD-C23-22][DD-C23-23].

**User archetypes (named):** (a) device-qualification engineer at a mid-size SiC/GaN maker who must now answer customer RFQs referencing JEP203/204; (b) power-module/tier-1 engineer doing incoming-device selection under time pressure; (c) national-lab/university reliability researcher who today builds one-off rigs. The problem is real. The open question — the red team's correct challenge — is whether it is *unserved*.

## 2. Product definition & the extreme-performance edge (resolving red-team point 1: what tier is actually unserved?)

**What incumbents already ship.** Keysight PD1500A: turnkey automated DPT for discretes, 1200 V / 200 A, with dynamic on-resistance, gate charge, and reverse recovery, AutoCal calibration [DD-C23-01]. Keysight PD1550A: modules, 1500 V / 3000 A, solderless contacts, isolated high-side probing, safety interlocks [DD-C23-02]. Tektronix WBG-DPT: a scope software option ("automated switching, timing, and diode reverse recovery measurements per JEDEC and IEC standards") on 4/5/6-Series MSOs — i.e., **JEDEC-referenced measurement automation is already a firmware/software feature at incumbents** [DD-C23-03]; Tektronix additionally holds a 2025 US patent on flexible WBG DPT methodology, a freedom-to-operate consideration [DD-C23-13]. PE-Systems (Germany): fully automated DPT to 2 kV / 3.6 kA, −55 to 250 °C, fixtures for all packages, **including short-circuit testing** [DD-C23-04]. LEMSYS — now sold under Teradyne — SLIC-AC: switching + short-circuit SCSOA to 12 kA for automotive SiC modules, production-grade [DD-C23-05]. RIGOL attacks from below with a Chinese-priced component bundle (DG5000 Pro dual-pulse source with dead-time control, PIA1000 1-GHz isolated probe with 180 dB CMRR, 12-bit DHO5000 scopes) aimed at EV-drive customers [DD-C23-18].

**What the evidence says is actually thin.** Three residual gaps survive contact with the product pages:

1. **Price-tier gap (unverified, testable).** Keysight's systems are quote-only and above the online-purchase threshold [DD-C23-26]; no public price exists for Keysight, PE-Systems, or UniSiC. Industry word-of-mouth puts configured PD1500A-class systems in the several-hundred-k$ range, but **this mission could not verify any incumbent price** — so "sub-$150K integrated appliance is whitespace" is a hypothesis, not a fact. Getting real quotes is validation experiment #1 (§10). The Tektronix path is cheaper (~$80–150K of scope+probes+supplies at list, judging by its component architecture [DD-C23-03]) but is *not an appliance*: the user still builds the power stage, fixture, and safety containment.
2. **JEP203-native short-circuit ruggedness at lab scale.** Commercial SC benches exist (PE-Systems option; LEMSYS at 12 kA production scale [DD-C23-04][DD-C23-05]) but a compact, JEP203-parameterized, destructive-test-safe SC/avalanche bench with statistical withstand-time workflows (the JEP203 methodology of varying VDS/VGS/temperature [DD-C23-11]) is not a configured product from the majors — Keysight's pages list no short-circuit capability [DD-C23-01][DD-C23-02].
3. **Data/compliance software layer.** No vendor sells the cross-instrument piece: JEP173/203/204-templated test plans, lot-to-lot statistics, datasheet-table generation, audit-ready traceability. JEP204 is precisely a *catalog of procedures* [DD-C23-06] — a natural schema for software.

**Honest spec target vs. state of the art:** 1.2–1.7 kV / ≤600 A discrete-and-small-module class, <10 nH power-loop (UniSiC advertises 6 nH busbar loops [DD-C23-15] — parity, not superiority), integrated −40 to 175 °C thermal, DPT + JEP173 dynamic-Ron + JEP203 SC in one enclosure, compliance-report software. There is **no order-of-magnitude performance edge available in this category**; the differentiator would be integration + price + software, which is a business-model edge, not an extreme-physics edge. That materially weakens C23 against the founder's "extreme as identity" criterion.

## 3. Technical feasibility & TRL path (sellable unit 2029–2031)

Founder fit is genuine: he performs GaN/SiC characterization daily, with precision-analog, FPGA, and software depth. Feasibility is not the binding constraint; certification, fixturing breadth, and channel are.

**BOM sketch (buy vs. build), qty-1 estimate $60–90K:**
- *Bought:* 2 kV HV DC source (~$15–25K); 12-bit ≥1 GHz digitizer/scope module ($15–25K); isolated gate-side probe(s) ($5–15K; PIA1000-class parts now exist at Chinese prices [DD-C23-18]); thermal plate/forced-air stage ($8–15K); HV relays, caps.
- *Built (the moat, such as it is):* laminated-busbar DC-link hitting <10 nH per package family; programmable gate driver with per-pulse parameter sweep; **dynamic-Ron clamp** (published academic circuits; JEP173 implementations are known to disagree — an accuracy-benchmarked clamp is a publishable edge [DD-C23-09]); SC test leg with desat detection, crowbar, and arc/fragment containment; sequencing FPGA; all software.
- *Hard parts:* per-package fixtures (TO-247, D2PAK, SMD GaN, small modules) — this is where DPT accuracy lives and where every incumbent earns its price [DD-C23-10]; CE/UL/CSA certification of a kV-class pulsed instrument with destructive-test modes (est. $50–150K + 6–9 months, one-time); calibration traceability.

**Cleanroom dependence: none.** TRL path: lab-grade prototype exists in effect today in his PhD work; productized, certified v1 is **18–24 months from funding** (the red team's correction of the one-pager's 9–12 months is accepted). HTRB/1,000-h chamber stress does *not* belong in this box — the red team's incoherence charge is accepted; JEP204-catalog chamber tests stay out of scope, addressed only in the software layer's test-plan templates.

## 4. Competitive landscape — global and China (resolving red-team point 2: does a US/EU version still have room against UniSiC?)

**Global:** Keysight (PD1500A/PD1550A — the reference tier) [DD-C23-01][DD-C23-02]; Tektronix (scope-software tier, JEDEC/IEC measurement automation, patent activity) [DD-C23-03][DD-C23-13]; PE-Systems (automated appliance tier, 2 kV/3.6 kA, SC-capable, EU) [DD-C23-04]; Teradyne/LEMSYS (production switching + SC to 12 kA — note a top-3 global ATE company now owns this line, signaling consolidation into majors) [DD-C23-05]; plus test-as-a-service entrants (CSA Catapult, June 2026 [DD-C23-22]).

**China (中文检索结果):**
- **忱芯科技 UniSiC** (Shanghai, 2020): full line — 晶圆级动态WLR、KGD、动态/静态、双极退化、逆变器对拖 test systems plus precision SMUs; **>200 systems shipped**, 100+ patents, 6 nH stacked-busbar main loop, cooperation with domestic tier-1 IDMs and "Wolfspeed 等知名企业," first overseas installations completed, **Munich office opening**; RMB 200M+ B/B+ round led by state fund 国投创业 (Dec 2024) explicitly to fund 全球化业务布局 (global expansion) [DD-C23-14][DD-C23-15]. UniSiC is not only C23-already-built in China; it is arriving in Europe.
- **联讯仪器 Lianxun** (Suzhou): first STAR-board IPO approval of 2026, raising RMB 17.11亿; **21.7% share of China's SiC power-device test-equipment market (#1 domestic), 43.6% share in wafer-level burn-in**; revenue RMB 2.14亿 (2022) → 7.89亿 (2024), customers include BYD Semiconductor [DD-C23-16].
- **华峰测控 Huafeng** (688200): STS8200-derived power test platforms extending into GaN/SiC third-gen coverage (3 kV range claims), >8,000 cumulative testers installed, H1-2025 revenue RMB 5.34亿, +41% YoY [DD-C23-17].
- **RIGOL 普源精电**: sub-$50K DPT component bundles for EV-drive customers [DD-C23-18].
- Demand context: 高端仪器 (high-end instruments) is a named key-core-technology 攻关 field in the 15th Five-Year-Plan Recommendations, alongside ICs and industrial machine tools [DD-C23-24] — Chinese state money and procurement preference will keep flowing to UniSiC/Lianxun/Huafeng, not to a US vendor.

**Answer to point 2:** A US/EU-market version does **not** get room by being "UniSiC for the West" on hardware alone — PE-Systems already is that, incumbent-priced, and UniSiC itself is entering the EU with nine figures of state-backed capital [DD-C23-15]. Residual room exists only where three things stack: (a) UniSiC's China/state-fund provenance triggers trusted-vendor screening at US primes, national labs, and automotive tier-1s (a real but policy-dependent moat); (b) the JEP203 SC-bench + compliance-software wedge the majors haven't configured (§2); (c) a genuinely lower certified price point — unproven until quotes are in hand.

**Answer to point 3 (defensibility given JEDEC-as-software-update):** Confirmed that measurement math per JEDEC docs arrives at incumbents as software [DD-C23-03]. What does *not* arrive as a firmware update: the SC-ruggedness power stage and containment, integrated thermal + fixture + HV in one certified enclosure at 1/3 the incumbent configured price, and a per-seat compliance-data layer (test-plan templates, statistics, datasheet generation) that is instrument-agnostic. If C23 proceeds, the defensible core is **the SC bench plus the software layer** — with the software deliberately built to also ingest Keysight/Tek data, so it survives even if the hardware wedge closes.

## 5. Market: bottom-up beachhead, expansion, TAM/SAM/SOM

**Beachhead (US/EU/JP/KR only — China excluded per §7):**
- Buyer universe: JC-70 alone has 70+ member companies [DD-C23-06]; adding non-member module makers, tier-1s, and labs, a defensible count is **60–80 commercial organizations** running formal WBG dynamic-qualification programs outside China, plus **~200 university/RTO power-electronics groups** in US/EU.
- Units: commercial orgs hold 1–3 benches → 100–240 installed; at ~20%/yr additions+refresh → **20–50 commercial units/yr**. Labs: ~5% buy in a given year → **~10 units/yr**. Addressable: **30–60 units/yr**.
- Arithmetic: 30–60 units × $100–150K ASP = **$3–9M/yr beachhead revenue pool**; a credible new-entrant share by year 3 is 20–30% → **$1–3M/yr SOM**. Add software at $10–20K/seat/yr across, optimistically, 50–150 seats → +$0.5–3M/yr.
- **Honesty check:** this beachhead alone is a lifestyle-business, not a venture-scale, number — and it is contested by six-plus named vendors. The red team's "~$30–50M SAM" is consistent with my figures.

**Top-down triangulation (SAM):** Chinese proxies: Lianxun's #1 position at 21.7% share with total revenue RMB 7.89亿 (2024, all product lines) implies a China SiC-test-equipment market (all insertion points: WLBI, KGD, static, dynamic) of roughly **RMB 1.5–2.5B/yr (~$210–350M)** [DD-C23-16]; UniSiC's >200 units over ~4 years corroborates a substantial dynamic-test slice [DD-C23-15]. Taking dynamic characterization + ruggedness as 15–25% and the ex-China market as comparable in size to China's, global SAM for this niche is **~$60–150M/yr**, growing with device markets: power GaN $355M (2024) → $3B (2030, 42% CAGR, Yole) [DD-C23-21], while SiC digests a downturn — substrate revenue fell 9% to $1.04B in 2024 amid price war and oversupply [DD-C23-19], and Wolfspeed exited Chapter 11 in Sept 2025 with ~70% of debt eliminated [DD-C23-20]. The red team's "mid-tier capex is collapsing" point stands for SiC through ~2027; GaN (data-center/AI power, 800-VDC architectures) is the growing demand leg [DD-C23-21][DD-C23-22].

**Expansion (what could make it venture-scale):** production-line dynamic screening (competing with Teradyne/LEMSYS — hard), wafer-level dynamic test (competing with UniSiC/Lianxun core — hard), or the software layer as the land-and-expand product across all vendors' instruments (most plausible). TAM including production test: $0.5–1B-class, but that arena is owned by ATE majors and Chinese IPO-funded champions.

## 6. Go-to-market (re-sequenced; resolving red-team point 4)

**China-first: eliminated** — on both policy (§7) and market logic. China is the one market where domestic substitution (国产替代) is the explicit, subsidized buying criterion [DD-C23-24][DD-C23-14]; a US-person founder selling imported test gear there competes against UniSiC/Lianxun's state-backed pricing *and* against US outbound/end-user rules. Nothing about the founder's native-Chinese advantage overcomes a market whose organizing principle is "don't buy foreign."

**US-first (recommended if pursued at all):**
1. 2029–2030: 3–5 reference systems at trusted-buyer sites where UniSiC cannot sell and Keysight is overkill/overbudget: DoE labs (NREL/Sandia power-electronics programs), university centers, one US GaN device maker, one defense-adjacent module house. Federal labs' trusted-vendor screening is a tailwind here.
2. Publish JEP203/JEP204 benchmark data on commercial devices (the founder's academic credibility is the marketing engine); seat the company in JC-70 [DD-C23-06].
3. 2030–2031: EU via APEC/PCIM presence — but expect PE-Systems (incumbent) and UniSiC-Munich (price aggressor) in every deal [DD-C23-04][DD-C23-15].
4. Software sold separately from day one, instrument-agnostic, so revenue survives hardware commoditization.
**Channel reality (red-team point accepted):** T&M needs demo inventory, FAEs, calibration/service infrastructure. A solo founder must budget for a commercial co-founder or first sales hire at seed — this is a structural, not optional, cost (§8).

## 7. Regulatory & geopolitical exposure (per `50_PHASE5_POLICY/POLICY_BRIEF.md`)

The policy brief's archetype (e) — "WBG semiconductor test/burn-in instruments sold into Chinese fabs" — is C23's China leg, rated **CN ⚠️ / US-first-into-China ⛔→⚠️ / parallel ⛔**, the harshest rating of any archetype reviewed. Engaging that finding directly:

- **Selling into China from a US entity:** many target fabs are Entity-Listed (SMIC ecosystem; Fudan Micro added Sept 2025), with the Affiliates Rule extending coverage to subsidiaries from Nov 2026. Test gear itself is often 3B992/EAR99, but **end-user rules dominate**, and §744.6 means the founder's *labor* supporting an advanced-node Chinese fab is controlled even with zero US-origin content. Customer-by-customer licensing plus node-drift liability makes China revenue unbankable.
- **Founding/expanding a Chinese entity:** greenfield formation by a US person is a covered transaction under 31 CFR 850; test-equipment manufacturing is arguably outside today's prohibited list, but COINS implementing regs (~March 2027) carry sector-expansion authority, and any drift toward IC production (including GaN ICs) is flatly prohibited. A parallel CN/US structure for this archetype is rated near-blocked.
- **Consequence adopted in this report:** the China angle in the original one-pager is **removed from the plan**, not merely postponed — which deletes the founder's China-network advantage from C23's fit case entirely. What remains is a modest compliance surface: US-built bench instruments to US/EU/JP/KR civil customers are EAR99-class with standard screening; CE/UL product-safety certification is the real burden (§3). One quiet upside: the same geopolitics that blocks his China leg also handicaps UniSiC in US federal/defense-adjacent accounts (§4). **All of the above is research, not legal advice; counsel required before any structuring.**

## 8. Capital & milestones (2029 → 2032)

- **2029 H2 (found, pre-seed/seed $1.5–3M):** solo + 2 engineers + fractional compliance; v1 architecture frozen (1.2 kV/600 A DPT + dyn-Ron + JEP203 SC leg); burn ~$70–100K/mo.
- **2030 H2:** certified v1 (CE/UL); 3–5 paid pilots at $80–120K; first revenue **~$0.4M** (18–24 months post-founding — not the one-pager's 9–12).
- **2031:** 10–15 units + software seats; revenue $1.5–2.5M; gross margin problem becomes visible (BOM $60–90K against $120–150K ASP → 35–50% hardware GM, thin for T&M); software attach is what makes the model work.
- **2032 (Series A gate):** ≥25 cumulative units, ≥$3M ARR-equivalent with ≥30% software mix, one automotive tier-1 logo. If hardware GM <40% and software attach <20%, the correct move is to pivot fully to the software/data layer or sell the line to a Keysight/Teradyne-tier acquirer.

## 9. Risks & kill criteria

| Risk | Assessment |
|---|---|
| **Category already served at both price ends** (Keysight/PE-Systems above; Tek/RIGOL components below; UniSiC everywhere with state capital) | **Top risk; confirmed by this dive** [DD-C23-01..05][DD-C23-14][DD-C23-18] |
| JEDEC compliance = incumbent software update; Tek patent activity narrows FTO | Confirmed for measurement layer [DD-C23-03][DD-C23-13] |
| Beachhead too small for venture returns ($3–9M/yr pool, 6+ vendors) | Confirmed by bottom-up arithmetic (§5) |
| SiC capex depression through ~2027 (price war, Wolfspeed restructuring) | Real; GaN/data-center partially offsets [DD-C23-19][DD-C23-20][DD-C23-21] |
| Solo founder vs. channel-heavy T&M business | Unmitigated without a commercial hire |
| China leg near-blocked (policy) + 国产替代 demand-side lockout | Structural; removed from plan (§7) [DD-C23-24] |

**Kill criteria (any one suffices):**
1. 2027 quotes show a configured Keysight PD1500A-class or PE-Systems system at **<$200K** — the price gap doesn't exist.
2. Buyer interviews (n≥20 at APEC/PCIM) show **<30%** of qualification managers with budget intent for a dedicated JEP203/dyn-Ron bench vs. DIY or test services (CSA-style [DD-C23-22]).
3. UniSiC or PE-Systems lists a **sub-$150K integrated unit in US/EU** before end-2028 [DD-C23-15].
4. JC-70 member polling confirms JEP203 adoption is satisfied by scope-software + in-house rigs (compliance pull evaporates).

## 10. Verdict

**Conviction: LOW** (as specced in the one-pager: effectively a no-go; the red team's 75% kill probability is ratified — the "no product exists" premise is false, the extreme-performance edge is absent, the China angle is policy-dead, and the honest beachhead is $3–9M/yr contested by six-plus funded vendors). A **narrow MEDIUM** survives only for the reframed wedge — JEP203-native short-circuit ruggedness bench + instrument-agnostic JEDEC-compliance software — and only if the 2027 validation gates pass. C23's best role in the portfolio is as a **fallback/companion**: the cheapest-to-start, deepest-founder-fit idea that monetizes his exact PhD skills if bolder candidates fail, and whose validation costs almost nothing.

**Validation experiments during the PhD (2026–2028, total cost <$5K + time):**
1. **Get the real prices (2026 H2, free):** request configured quotes for Keysight PD1500A/PD1550A, PE-Systems ADPT, and a full Tek WBG-DPT stack via Stanford procurement; the entire thesis stands or falls on whether the integrated tier really starts above ~$250K [DD-C23-26].
2. **Build-and-publish (2027, uses existing lab resources):** implement a JEP203-parameterized SC-withstand + JEP173 dynamic-Ron mini-bench as part of his research; publish an APEC/WiPDA benchmarking paper on commercial 650 V GaN / 1.2 kV SiC parts [DD-C23-09][DD-C23-11]. Every inbound "can we buy/replicate this?" email is a pre-order signal; zero inbound interest is a kill signal.
3. **Structured buyer discovery (2027–2028, conference travel he'd do anyway):** 20+ interviews of qual/reliability managers on last-setup cost, JEP203 budget intent, and service-vs-appliance preference; join JC-70 through Stanford or personally to watch whether the standards create equipment purchase orders or just software updates.

---
*Report: ~3,100 words. 26 unique sources (Tier 1: 8, Tier 2: 6, Tier 3: 12 — Tier 1–2 = 54%); 6 Chinese-language. All load-bearing prices, dates, market sizes verified "fetched" except where explicitly flagged as unverified/snippet (incumbent list prices — none are public — and Huafeng interim-report color).*
