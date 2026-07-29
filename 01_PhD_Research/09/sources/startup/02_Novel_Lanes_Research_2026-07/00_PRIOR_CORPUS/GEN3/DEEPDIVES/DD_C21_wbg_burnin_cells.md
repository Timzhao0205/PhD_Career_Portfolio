# DD_C21 — Compact Wafer-Level Burn-In & Stress-Test Cells for WBG Power Devices

**Candidate:** C21 · **Sources:** `DD_C21_sources.json` (27 unique; Tier 1–2 = 14/27; 10 zh) · **Date:** 2026-07-03
**Red-team status:** REDTEAM_C21.md (kill probability 85%) — each of its four load-bearing claims is explicitly re-verified below. **This deep dive substantially confirms the red team.**

---

## 1. Problem & who has it

SiC MOSFETs have a real, physics-rooted infant-mortality problem: extrinsic gate-oxide defects (pits, voids, contamination at the SiC/SiO₂ interface) that survive fab test and fail in the field. Peer-reviewed work confirms both the need and the inadequacy of current practice: manufacturer screening at ≤~9 MV/cm for <1 s "is not enough to remove all the devices with extrinsic defects," and wafer-level stress at ≥150 °C accelerates Vth/leakage degradation enough to shorten screening times [DD-C21-03][DD-C21-04]. This is why automotive SiC is burned in — at the wafer level, before packaging value is added. Qualification standards frame the demand: AEC-Q101 defines HTRB/HTGB/temperature-cycling qualification for automotive discretes [DD-C21-06], and JEDEC's JC-70.2 published JEP203 (short-circuit evaluation) and JEP204 (catalog of SiC stress procedures) in June 2026 — note these are **guidelines, not mandatory standards**, so they standardize methods rather than compel equipment purchases [DD-C21-22].

Who has the problem, concretely:

- **Automotive SiC device makers.** The top five (ST, onsemi, Infineon, Wolfspeed, ROHM) held ~91.9% of a $2.28B (2023) SiC device market [DD-C21-26]. These are Aehr's installed base — SiC wafer-level burn-in (WLBI) was **>90% of Aehr's $66.2M FY2024 revenue** [DD-C21-08][DD-C21-14].
- **Chinese SiC fabs** (BYD Semiconductor, Silan, Yandong Micro …) — served domestically by Semight and others (§4) [DD-C21-17].
- **GaN power suppliers** — split demand: at least one top-tier *automotive* GaN supplier placed a production WLBI order with Aehr in Jan 2025 [DD-C21-15], while fabless GaN startups qualify by test-to-fail and extended qual campaigns without production burn-in capex (§5, red-team item 4) [DD-C21-27][DD-C21-23].
- **Labs and second-tier fabs** needing JEP204-style stress data — today they outsource to service labs (EAG-class US labs; Chemnitz Power Labs in the EU offers HTRB to 6.5 kV/200 °C, HTGB, AQG-324 power cycling as a service) [DD-C21-24].

**The niche quantified (and it is small):** total annual global spend on SiC WLBI equipment ≈ $50–110M in the 2024 peak year, of which the US/EU-accessible portion is ~$24–60M and highly cyclical (arithmetic in §5). This is the deep dive's central problem: the pain is real but the annual equipment budget behind it is a single mid-size company's revenue.

## 2. Product definition & the extreme-performance edge

As pitched: a benchtop-to-cell-scale burn-in system (HTGB/HTRB/dynamic stress, kV-class, high parallelism, 150–175 °C) at ~1/10th the entry price of Aehr-class platforms; ASP $300K–1M; HW + test-sequencing/analytics SW.

Specs it must beat — the *actual* state of the art at the low end is Chinese, not Aehr:

| Capability | Aehr FOX family | Semight WLBI3800 (China) | The C21 pitch |
|---|---|---|---|
| Wafers/run | FOX-XP: up to 9–18; FOX-NP: multi-wafer entry; FOX-CP: "low-cost single-wafer" [DD-C21-09][DD-C21-15] | 3 wafers, HTGB+HTRB auto-switching; sister WLBI370A: 20 wafers HTGB [DD-C21-19] | 1–3 wafers or die trays |
| Parallelism | full-wafer contact via WaferPak, thousands of source/measure channels [DD-C21-09] | 2,112 die/touchdown, ±25 µm probe-mark repeatability, 6/8-inch [DD-C21-19] | "high parallelism" (unspecified) |
| Per-die intelligence | per-device current limit, per-wafer thermal chuck | per-channel overcurrent protection, per-die Vth, Igss/Idss scan, MAP binding [DD-C21-19] | analytics SW |
| Arc management | proprietary | N₂ protection against HV arcing at temperature [DD-C21-19] | unsolved |

The uncomfortable conclusion: **the "1/10th price, good-enough" slot is already occupied — by Semight, with per-die protection, full automation, and MAP-based yield software**. A 2030 US entrant has no order-of-magnitude axis left: parallelism, price, automation and analytics are all taken. The only genuinely open technical axes are (a) *dynamic* stress at the wafer level (switching stress, D-HTRB-like profiles — which Chenxin already ships as "wafer-level dynamic WLR" in China [DD-C21-12]) and (b) module/KGD-level burn-in in the West (§4/§10). "Extreme performance edge" as required by the founder's thesis is **not available in this category** — this is a cost-engineering and field-service business, not a physics-limit business.

## 3. Technical feasibility & TRL path (2029–2031)

What can be bought: thermal chucks/plates, SMU channels (or self-built per-channel stress boards — the founder can do this well), HV supplies, probe-card PCBs, handlers (used), chillers. Cleanroom dependence: low (interfaces to finished wafers). What must be built — and is hard:

1. **Full-wafer or high-count contacting at temperature.** Thousands of contacts per touchdown, CTE-matched over 150–200 °C, uniform force, probe-mark control at ±25 µm — this is precision electromechanics plus materials, and it is exactly where the incumbents' know-how sits. Aehr's foundational WLBI patents (thermal chuck, cartridge architecture) from 1998–2001 have **expired** (US6140616A expired 2018) [DD-C21-01], which is precisely why four Chinese vendors could enter; but adjacent full-wafer-contactor IP persists (e.g., Translarity's wafer-prober-integrated contactor, active to Mar 2029) [DD-C21-02], and Aehr's newer WaferPak/Aligner filings continue. Patent risk is moderate and mappable — the moat is really trade-secret engineering + installed base + consumables lock-in (WaferPaks were 30% of Aehr's Q4 FY2025 revenue [DD-C21-14]).
2. **kV HTRB across neighboring die at 150–175 °C**: creepage/arc-over at production tolerances; Semight's answer is N₂-purged enclosures [DD-C21-19]. Solvable, but it is 12+ months of iteration by itself.
3. **Per-die current limiting** so one shorted die doesn't cascade — thousands of channels of protected stress electronics. This is the founder's genuine strength (precision instrumentation, power electronics).
4. **Production-tool wrapper**: SEMI S2/CE compliance, EAP/SECS-GEM factory integration [DD-C21-19], 24/7 uptime guarantees, resident apps engineers. A fab does not buy a burn-in cell from a solo founder without a service organization.

Realistic TRL path: a die-/carrier-level stress cell (no full-wafer contact) is achievable by one person + 2 engineers in 18 months for ~$1.5–2.5M — but that product is a bench rig, which collapses C21 into C23's appliance category. A credible *wafer-level production* cell is a $5–10M, 3-year, 10+-person program — beyond seed scale. The red team's feasibility critique **stands**.

## 4. Competitive landscape (global and China)

**Above (global incumbents):**
- **Aehr (US)** — FOX-XP/NP production systems, FOX-CP explicitly a "low-cost single-wafer" entry system [DD-C21-09]; full-wafer contact + aligner + consumables; FY2025 revenue $59.0M ($66.2M FY2024, $65.0M FY2023) [DD-C21-07][DD-C21-08]. Not "distracted by AI": while AI went from 0% to >35% of FY2025 revenue, Aehr simultaneously took an initial *production* WLBI order for automotive GaN (Jan 2025) and reports engagements with "multiple other potential new GaN customers" [DD-C21-14][DD-C21-15]. It also bought its way into package-level burn-in (Sonoma/Echo/Tahoe, >100 Echo systems installed) [DD-C21-16]. The claimed vacuum below Aehr **does not exist** (red-team item 1: confirmed).
- **Micro Control (US)** — 50 years in high-power package burn-in; HPB-8 delivers >2,000 W/DUT, 8 kW/slot, automation-ready — aimed at AI processors, and shows where PLBI capex is actually flowing [DD-C21-25]. ESPEC, KES Systems, SPEA and Chroma occupy adjacent burn-in/test slots (per red team; not re-verified individually).
- **Service labs**: US reliability-qual labs and EU's Chemnitz Power Labs sell HTRB/HTGB/power-cycling campaigns as a service — the natural choice for startups without capex budgets [DD-C21-24].

**Below/beside (China — the demand center, researched in Chinese):**
- **联讯仪器 Semight (688808, STAR board, listed 2026-04)** — **43.6% of China's 2024 SiC power-device WLBI systems market, #1 domestic**; #3 in power-chip KGD sorting systems [DD-C21-18]. Revenue 2.14→2.76→7.89亿元 (2022–24), profitable from 2024 (净利 1.4亿), customers include 比亚迪半导体, 士兰微, 燕东微; IPO raised 19.54亿元 earmarked partly for automotive-grade chip test equipment [DD-C21-17][DD-C21-10]. Product family: WLBI370A (20 wafers HTGB), WLBI3800 (fully automated, 3 wafers HTGB+HTRB, 2,112 die, ±25 µm, N₂ anti-arc) [DD-C21-19].
- **忱芯科技 Chenxin (Shanghai, f. 2020)** — SiC test specialist: WLBI, wafer-level *dynamic* WLR, KGD systems, SMUs; >200 units shipped; B/B+ rounds led by state-owned 国投创业 (SDIC) [DD-C21-12]; shipped fully automated SiC MOSFET WLBI (HTGB/HTRB multi-mode, mixed-run) to a domestic leader in Jan 2026 [DD-C21-20].
- **广立微 Semitronix (301095)** — launched WLBI B5260M for SiC/GaN power devices *and AI chips*, shown at SEMICON China 2026 [DD-C21-21].
- **英铂 YB Semi (Shanghai)** — OSTINATO WLBI line plus CP/KGD test equipment (site fetch failed; snippet-level only).
- **华峰测控 Accotest (688200)** — states GaN/SiC test core technology already "applied in equipment sold in volume" [DD-C21-11].

Four-plus funded Chinese WLBI vendors in one niche, backed by Big-Fund-era localization money, with a 20% government-procurement price preference for China-made products from 2026-01-01 [DD-C21-13]. Pricing signal: no public 中标 award for SiC WLBI was found on ccgp.gov.cn (buyers are corporate fabs, not government units), but Semight's segment economics (65% gross margin, ~2.7亿元/yr semiconductor-test-equipment run-rate across WLBI+KGD+WAT [DD-C21-17]) imply system ASPs in the low-millions RMB — i.e., the "affordable" tier sells for roughly $300–800K equivalent already. Red-team item 2: **confirmed — the mid-market exists and is occupied, in China, by Chinese vendors.**

## 5. Market: bottom-up beachhead, then top-down

**Re-deriving the red team's $25–55M/yr figure (item 3).** Aehr officer statements on the FY2025 call: SiC WLBI was ">90% of our revenue in fiscal 2024" and "<40% … this fiscal 2025" [DD-C21-14]. Arithmetic:
- FY2024: >0.90 × $66.2M ≈ **>$59.6M** [DD-C21-08]
- FY2025: <0.40 × $59.0M ≈ **<$23.6M** [DD-C21-07]

So the world's dominant vendor's SiC WLBI revenue swung between ~$24M and ~$60M across two adjacent years. The red team's "$25–55M/yr" is verified in range; refined: **$24–60M/yr, with ±2.5× cyclicality**.

**Adding China (not in the red-team figure).** Semight held 43.6% of China's 2024 SiC WLBI systems market [DD-C21-18]. Its whole semiconductor-test-equipment segment (WLBI + KGD + WAT/WLR) ran ~34% of revenue in early 2025 (~2.7亿元 annualized on 2024's 7.89亿) [DD-C21-17]. If WLBI is 30–60% of that segment (0.8–1.6亿元), the China SiC WLBI market ≈ 1.9–3.7亿元 ≈ **$26–51M (2024)** — an estimate with wide error bars, flagged as such. Global SiC WLBI equipment spend in the 2024 peak: **~$50–110M/yr**; and the China share is legally inaccessible to this founder (§7).

**Bottom-up beachhead for C21 as scoped** (sub-$500K cells; US/EU only, per §7): candidate buyers = US/EU SiC/GaN device makers, module houses and labs *not already served by Aehr*: generously ~25 organizations (mid-tier device makers ~10, module/KGD-curious Tier-1s ~8, national/university power labs ~7). Assume a strong 30% attach over 3 years, 1.5 units each, $350K ASP:
25 × 0.30 × 1.5 × $350K ≈ **$3.9M cumulative hardware over 3 years**, +~20%/yr consumables/service ≈ **$1.5–2.5M/yr steady state**. Even tripling every assumption yields <$8M/yr — below a venture-scale company and below the founder's "high-end niche that opens onto adjacent larger markets" bar.

**GaN demand check (red-team item 4).** Split verdict: (a) top-tier *automotive* GaN suppliers do pay — Aehr booked a GaN production WLBI order in Jan 2025 and cites multiple GaN engagements; Aehr pegs GaN device sales at $2.5B by 2029 [DD-C21-15][DD-C21-14]; (b) *GaN startups largely do not buy burn-in capex*: EPC's published qualification is a test-to-fail reliability-report methodology (Phase 18, 2026) [DD-C21-27]; Navitas markets "AEC-Plus" — extended D-HTRB/D-HTGB *qualification campaigns*, with no production burn-in claimed [DD-C21-23]; and cash-poor startups outsource campaigns to service labs [DD-C21-24]. The startup-beachhead premise of the one-pager is **falsified**; the customers who do pay for GaN WLBI are majors who buy Aehr.

**Top-down triangulation.** SiC devices: $2.28B (2023) → $5.33B (2026F) [DD-C21-26]. Test-equipment capex for burn-in plausibly ~2–4% of device revenue in qualification-heavy years — $45–90M on 2023 revenue — consistent with the bottom-up $50–110M peak. TAM (all WBG burn-in equipment incl. China + module-level, 2030): ~$150–300M. SAM (US/EU, sub-$500K tier): ~$15–40M/yr. SOM for a 2030 solo entrant: **$2–8M/yr by 2033**. Module-level/KGD alternative: Western PLBI spend is flowing to AI processors (Micro Control's 18-system order went to AI OSATs; Aehr's Sonoma line is AI-focused) [DD-C21-25][DD-C21-16]; power-module KGD screening is a genuine Western gap but is bounded by the same arithmetic — dozens of buyers, not hundreds.

## 6. Go-to-market

**China-first (the natural sequence for this product) is not available to this founder** (§7). If it were: the playbook would be Suzhou/Shanghai incorporation, 首台套 first-unit insurance subsidy, the 2026 20% procurement preference [DD-C21-13], and BYD-Semi-class reference customers — i.e., exactly Semight's executed playbook, now defended by an IPO war chest [DD-C21-10].

**US/EU-only sequence (the real question):** (1) 2029–30: sell 2–3 die-level stress cells to university/DoE power labs and one EU module maker as reference sites; (2) 2030–31: JEP204-aligned "compliance bundle" (hardware + automated report generation — the founder's SW edge) to mid-tier device makers; (3) 2031+: attempt KGD/module-level burn-in cells for automotive Tier-1s reshoring SiC module assembly. Channel: direct + one EU rep; reference-customer strategy through JC-70 committee visibility. The honest problem: steps (1)–(2) describe **C23's appliance business**, and step (3) is a services-heavy niche where Chemnitz-class labs and OSAT partnerships (Aehr explicitly routes small customers through OSATs with installed FOX capacity) already absorb the demand [DD-C21-24][DD-C21-15]. Lead US; China only via non-controlled, non-Entity-Listed distribution later — and expect Semight/Chenxin to contest US/EU accounts on price by 2028 (Semight already lists Broadcom and onsemi among customers [DD-C21-17]).

## 7. Regulatory & geopolitical exposure

Per `50_PHASE5_POLICY/POLICY_BRIEF.md` (archetype (e), rated **CN ⚠ / US ⛔→⚠ / parallel ⛔** — the hardest case in the matrix): (a) EAR §744.6 restricts a *U.S. person's own support* of advanced-node Chinese fabs even with zero U.S.-origin content [P-42][P-43]; (b) natural Chinese customers are increasingly Entity-Listed (Fudan Micro added Sep-2025), with the Affiliates Rule re-activating Nov-2026 [P-16][P-17][P-06][P-07]; (c) founding/capitalizing a Chinese test-equipment entity is at minimum OISP-shadowed, and anything drifting toward GaN IC *production* in China is outright prohibited for a U.S. person [P-01][P-02]; (d) COINS-era regs (~2027) can broaden sectors with months of notice [P-03]. On the item side, burn-in/test gear is typically 3B992/EAR99 — the binding constraints are customer- and activity-based, not ECCN-based [P-12]. Meanwhile China's side actively subsidizes domestic substitution: 20% procurement preference (production-location-based) [DD-C21-13], 首台套 insurance, Big Fund III [P-31][P-33]. **Net: the demand center is structurally closed to a U.S.-person founder; the open (US/EU) lane is the small, cyclical fraction sized in §5.** This section coordinates with Phase 5; not provisional.

## 8. Capital & milestones (2029→2032, if pursued)

- **2029 H2 (seed, $2.5–3.5M):** 3 engineers; die-level 1.2 kV/175 °C stress cell prototype; 2 paid lab pilots. Burn ~$120K/mo.
- **2030:** v1 die-level cell ships ($250–350K ASP); revenue $0.5–1M; begin wafer-level contactor development — **this is where the plan breaks**: contactor + automation + SEMI S2 needs $5–10M more before a fab-grade unit exists.
- **2031 (Series A, $10–15M — weak story):** raising against a ~$15–40M/yr SAM already contested by Aehr-above and (in any tariff-permitting scenario) Semight-below; first production cell 2032 at the earliest.
- First meaningful revenue 2030–31 (~$1M); cash-flow breakeven not before 2033. The production-tool version does not fit solo-founder + seed constraints; the seed-fit version is C23 wearing C21's name.

## 9. Risks & kill criteria

| Risk | Severity | Evidence |
|---|---|---|
| No whitespace: Aehr above (FOX-CP/NP + GaN production wins + PLBI), 4+ funded Chinese vendors below | Fatal | [DD-C21-09][DD-C21-15][DD-C21-16][DD-C21-18][DD-C21-12][DD-C21-21] |
| Market too small & cyclical: leader's SiC WLBI ~$24–60M/yr, −60% in one year | Fatal | [DD-C21-07][DD-C21-08][DD-C21-14] |
| Beachhead falsified: GaN startups qualify via test-to-fail/outsourced campaigns, don't buy capex | High | [DD-C21-27][DD-C21-23][DD-C21-24] |
| Production-tool + field-service model exceeds solo/seed capacity | High | §3, §8 |
| China channel closed to U.S. person; Chinese rivals can enter US/EU | High | §7; [DD-C21-17] |
| Patent exposure on full-wafer contact (residual, mappable) | Medium | [DD-C21-01][DD-C21-02] |

**Kill criteria (any one suffices):** (K1) by mid-2027, <3 of 15 interviewed US/EU mid-tier WBG quality leads report an approved ≥$300K in-house burn-in budget; (K2) Aehr ships a <$500K SiC/GaN configuration or Semight/Chenxin lands a marquee US/EU account; (K3) ex-China SiC WLBI spend (Aehr SiC revenue as proxy) stays below ~$50M/yr through FY2027; (K4) contactor prototype cannot hit ±25 µm-class contact repeatability at 175 °C within 12 months of start.

## 10. Verdict

**Conviction: LOW as scoped — recommend NO-GO on wafer-level burn-in cells.** All four red-team pillars survived verification: the sub-Aehr vacuum is occupied from above (Aehr's own FOX-CP/NP, plus its GaN production wins and PLBI expansion) and from below (Semight at 43.6% China share with IPO capital, plus Chenxin, Semitronix, YB Semi); the accessible market is ~$24–60M/yr and cyclical; the GaN-startup beachhead does not pay for burn-in; and the US-person/China constraint amputates the demand center. The salvageable assets — per-die protected stress electronics, JEP204-aligned automation software, WBG measurement credibility — transfer cleanly to **C23 (JEDEC-compliant characterization appliance)**, with a *module/KGD-level* stress option as C23's expansion module rather than a standalone company. A test-as-a-service lab is the other fallback, but it is a consulting-margin business against established labs [DD-C21-24] and fails the founder's product-company preference.

**Cheapest validation experiments (2026–2028, during PhD):**
1. **Demand audit (≈$1.5K, 2 conference trips):** 15 structured interviews with quality/reliability managers of mid-tier SiC/GaN makers at APEC/PCIM/IRPS. Question set: current screening method, in-house vs outsourced, approved capex for burn-in, what JEP203/204 changes. Directly tests K1 — and doubles as C23 discovery.
2. **JEP204 stress campaign + publication (≈$5–8K parts, lab access already in hand):** run burn-in/HTGB screening on commercial 1.2 kV SiC MOSFETs replicating the OSU methodology [DD-C21-03]; publish at IRPS/WiPDA. Inbound interest (who calls, and asking for *equipment* vs *data*) is the cleanest demand signal, and it builds the C23 reputation asset either way.
3. **Price-floor mapping (≈$0, 4 weeks of emails):** collect budgetary quotes — Aehr FOX-CP/NP config, Semight/Chenxin via China contacts (native-language advantage), plus per-campaign pricing from two service labs. If a competent wafer-level cell already lands under ~$600K or outsourced campaigns run <$60K, the "1/10th price" wedge is formally dead.

---
*Inline citations [DD-C21-xx] per `DD_C21_sources.json`; [P-xx] per `50_PHASE5_POLICY/policy_sources.json`. Load-bearing figures verified "fetched" except where explicitly flagged as estimates or snippets.*
