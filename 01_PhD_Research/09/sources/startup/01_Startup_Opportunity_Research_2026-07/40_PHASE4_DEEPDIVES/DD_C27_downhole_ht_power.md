# DEEP DIVE — C27: 250–300°C-native power-conditioning modules for geothermal / downhole tools

**Sources:** `DD_C27_sources.json` (31 unique; 16 Tier 1–2). Red-team findings from `30_PHASE3_SCORING/REDTEAM_C27.md` are addressed explicitly in §3–§5 and §9. Regulatory analysis in §7 draws on `50_PHASE5_POLICY/POLICY_BRIEF.md`.

---

## 1. Problem & who has it

Downhole electronics die of heat. The industry's economic operating band is ~150–175°C: independent tool builders' current catalog directional modules are rated 165°C (Erdos Miller MicroPulse MP3+) and 175°C (MP4) [DD-C27-28]; a DOE/NETL program that pushed MWD to just 195°C concluded that screening components made HT tool day-rates **3–5× conventional** and "current electronic technology is not sufficient" [DD-C27-16]. Meanwhile the rock is getting hotter faster than the tools:

- **Fervo's Sugarloaf appraisal well (June 2025):** 15,765 ft TVD, projected bottomhole temperature **520°F (~271°C)** — drilled in 16 days, i.e., commercial-speed drilling has already outrun the 175–200°C tool fleet [DD-C27-18].
- **DOE superhot programs:** the Office of Geothermal's Feb-2026 $171.5M NOFO defines a dedicated superhot/supercritical topic at **>375°C** (Topic 4, later rounds; $4–25M per award) [DD-C27-13]; Quaise's Project Obsidian (Oregon) targets rock **>300°C** with a 50 MW plant "as early as 2030" [DD-C27-20].
- The Stanford Geothermal Workshop 2025 gap analysis lists MWD/LWD, logging tools, **power electronics**, and batteries as unsolved gaps for superhot drilling [DD-C27-17].

**User archetypes.** (a) *HT tool program engineer at an independent MWD/LWD builder* (APS Technology, Erdos Miller, Tolteq/NOV, Bench Tree, Scientific Drilling) who can buy 165–175°C boards from catalogs but has no merchant source for a >250°C power supply or pulser/motor driver. (b) *Superhot field-test PI* (DOE Topic-4 awardee, national lab, Quaise/Fervo hottest pads) who needs instrumented drilling and logging above 250°C and today gets it only via Dewar flasks with hour-limited hold times. (c) *Aero-engine distributed-control architect* who needs power/control nodes surviving 250°C on-casing ambients [DD-C27-23]. The high-end niche, quantified in §5, is small: tens of toolsets and tens of program units per year, at $25–75K-class module prices.

## 2. Product definition & the extreme-performance edge

**Product:** a family of *power-conditioning modules native to 250°C ambient (300°C survival / 300°C-native variant for program customers), with zero Dewar flask*: (i) 50–200 W isolated DC-DC supply (turbine-alternator or battery input, 12–72 V rails — the same rail set Chinese logging-tool supplies serve at 175°C [DD-C27-25]); (ii) pulser/valve driver; (iii) 0.5–2 kW three-phase motor-drive stage for rotary-steerable and ESP-adjacent actuation. Plus the software half: telemetry-grade health monitoring, remaining-life estimation from junction/passive telemetry, and derating management — genuine HW+SW, and something chip vendors do not ship.

**Edge vs. state of the art, with numbers:**

| Capability | Merchant state of the art | This product |
|---|---|---|
| Chip-level HT ICs | Honeywell HTSOI: ≥5 yr at 225°C continuous, DM300 directional module demonstrated at 300°C — *no DC-DC or motor-drive modules offered* [DD-C27-01][DD-C27-02] | not a chip vendor — integrates dies |
| Merchant DC-DC module | CISSOID EREBUS: 70 W buck at 225°C, >85% efficiency [DD-C27-11]; Watt&Well downhole PSUs/motor controllers to **220°C** [DD-C27-12]; 蓝欣 HDC100 100 W at 175°C (185°C case, 700 h) [DD-C27-25] | 50–200 W isolated at **250°C ambient**, motor drive to 2 kW; 300°C program variant |
| Tool-level workaround | Vacuum flask + phase-change heat sink: hours of hold time, fails on stationary logging | native operation, no hold-time limit |

The physics headroom is real: GaN-on-SiC HEMTs show stable DC characteristics to **600°C** in 2025 peer-reviewed work [DD-C27-30], and NASA's 4H-SiC JFET ICs ran **a year at 500°C** [DD-C27-31]. The constraint is not the transistor — see §3.

## 3. Technical feasibility & TRL path (resolving red-team issue #1: the passives wall)

**Honest BOM survey at 300°C:**

- **Capacitors — hard but not absent.** Presidio sells downhole ceramic capacitor lines rated "**250°C and above**" as catalog items [DD-C27-06]. Industry surveys confirm demand and supply in the 225–300°C band via modified-BaTiO₃ MLCCs, reconstituted mica, metallized PTFE, specialty glass, and wet-slug tantalum (the latter to ~230°C) [DD-C27-07]. At 300°C: C0G/paraelectric ceramics and glass/mica survive with derating; *bulk* capacitance (>10s of µF) is the genuine gap. Mitigation is architectural: GaN/SiC switching at 0.5–2 MHz cuts required bulk capacitance by ~an order of magnitude vs. 100 kHz designs — this is exactly the founder's Rivas-lab-adjacent skill.
- **Magnetics — research-demonstrated, never commercialized.** Standard power ferrites have Curie points ≤250°C and are optimized for ≤100°C [DD-C27-08]. But a 300°C-class MnZn ferrite *was* developed (Tc ~280°C L-perm, then a Boeing-funded material with Tc >300°C), and a **1.5 kW 270→28 V transformer ran 600 h at >290°C ambient** in AFRL-funded work (2004–05) [DD-C27-08][DD-C27-09][DD-C27-10]. The materials exist as recipes, not catalog cores. Practical 2029 path: (i) buy/relicense HT ferrite for 250°C designs; (ii) at 300°C, go **air-core / coreless planar at MHz frequencies** (no Curie limit at all; GaN makes the frequency affordable) with ceramic-insulated windings. This turns the passives wall into a high-frequency-design problem the founder is unusually well matched to.
- **Actives.** No *commercially qualified* 300°C-junction power FET exists — the red team is right. But bare GaN/SiC dies demonstrably operate far above 300°C [DD-C27-30][DD-C27-31]; SiC JFETs are the conservative choice (NASA heritage). The company buys dies and does **die-level screening + HT packaging** — elevated but acceptable "no-fab" posture: probe station, ovens, wire/ribbon bonders; no cleanroom process ownership. This is the same stack 谱析光晶 built commercially in China (chip passivation recipes aside): thick-film ceramic / HTCC substrates, **no low-melting solder** — AuGe/AuSn/TLP attach [DD-C27-26]. Harsh-environment packaging is the founder's PhD trade.
- **The rest:** connectors/wiring (ceramic/mica insulated — available), HT batteries excluded from scope (real gap, someone else's product [DD-C27-17]).

**Feasibility verdict.** A **250°C-native module is buildable by 2030 largely from catalog + screened parts** — capacitors catalog [DD-C27-06], magnetics near-catalog, SOI/SiC control ICs catalog [DD-C27-01] — and 250°C already clears every merchant module on the market (220–225°C ceilings [DD-C27-11][DD-C27-12]). A **300°C-native module is buildable as an engineered low-volume product** (every constituent has been demonstrated ≥290–500°C in Tier-1/2 sources), but with custom magnetics/caps, self-qualified dies, and 1,000+ h life-test burden — realistically **36 months to a field-trial-worthy unit, not the one-pager's 24**. The red team's "−1 TRL" stands for 300°C; it does not kill 250°C.

## 4. Competitive landscape (resolving red-team issue #2: is the power-module slot empty?)

**Global.**
- **Honeywell** (chips): HTSOI family, ≥5 yr at 225°C, ADCs/amplifiers/processors; DM300 proved 300°C system feasibility in 2012 under DOE money. Its page lists **no DC-DC converter or motor-drive modules** [DD-C27-01][DD-C27-02]. Chips, not power modules — red-team claim confirmed but it cuts both ways.
- **Ozark IC** (logic/sensing/comm): 22 SBIR/STTR awards ~$9M [DD-C27-05]; DOE Phase II for 450°C drill-head *communication/computation* (2020) [DD-C27-04]; $1.1M DOE Phase II for XNode-based *flow instruments* (2024) [DD-C27-03]. Across every award reviewed, **no power-conversion scope**. Confirmed: Ozark occupies data/logging, not power.
- **CISSOID** (225°C ceiling): EREBUS buck platform, 70 W at 225°C [DD-C27-11] — chipset/platform, low power, non-isolated.
- **Watt & Well** (the closest true competitor, missed by the one-pager *and* only partially by the red team): merchant **downhole motor controllers and power supplies, −40 to 220°C**, SOI+SiC, already "working with traditional clients in the USA and Norway on geothermal" [DD-C27-12]. The integrated-module slot is **not empty below ~220°C**.
- **Service majors** build in-house and buy chips (SLB/Halliburton/Baker Hughes); national labs (Sandia 300°C packaging, NASA Glenn 500°C SiC [DD-C27-21][DD-C27-31]) license out rather than sell.

**China (Chinese-language research; correcting the red team's "China weak" claim — it is half wrong).**
- **谱析光晶 (Hangzhou Puxi Guangjing Semiconductor)** — Tsinghua-spinoff "high-temperature chip" company: self-developed SiC power chips working at **230°C in complex systems, 280°C in simple systems**, sold into **downhole survey equipment of the three Chinese oil majors** explicitly as 国产替代 against Schlumberger-class imports; revenue RMB ~60M (2023) → 120M (2024) → **~230M (2025)**; seven rounds, RMB 500M raised, ChiNext listing prep for 2026 [DD-C27-26]. China has a venture-backed, revenue-generating incumbent at the *chip* level, one notch below this product's module level.
- **蓝欣电子 (Xi'an Lanxin/VAW):** merchant downhole DC-DC modules 30–100 W, but only 175°C rated (185°C case, 700 h) [DD-C27-25] — the Chinese merchant *module* ceiling today.
- **Demand side:** 石油科学通报's HTHP review: Yinggehai/South China Sea wells reach **249°C bottomhole**; Halliburton/SLB tooling serves ~200–210°C; domestic LWD (Daqing DQ-LWD) is 150°C-class; Bohai Drilling runs 200–230°C test series; CNPC has a 230°C memory pressure gauge [DD-C27-24]. Hot dry rock: Gonghe Basin (Qinghai) hit **236°C at 3,705 m** in 2017, and CGS-system publications note foreign ~350°C logging technology is offered to China as *service only, never sold as instruments* [DD-C27-27].
- **Net:** the red team was right that China has no >250°C merchant supplier and no superhot commercial program; wrong that the space is empty — China has real HTHP demand (249°C wells), a state HDR program, and a fast-scaling domestic chip player whose subsidized turf a US-person founder should not contest (§7).

**Slot verdict:** the merchant **integrated power module above ~230°C is genuinely unoccupied globally** — Honeywell/Ozark sell no power conversion, CISSOID/Watt&Well/蓝欣 stop at 175–225°C, 谱析光晶 sells chips at 230°C. But the slot is empty partly because paying demand above 230°C is program-scale, not fleet-scale (§5).

## 5. Market: bottom-up beachhead, expansion, TAM/SAM/SOM (resolving red-team issue #3: count POs, not press releases)

**Buyer census (honest).** Entities that could sign a PO for a >250°C power module, 2029–2032: (1) ~5–8 independent MWD/LWD tool builders (APS, Erdos Miller, Tolteq/NOV, Bench Tree, Scientific Drilling, Gyrodata-SLB) — today they build/buy at 165–175°C [DD-C27-28] and historically abandoned 195°C tools on cost [DD-C27-16]; (2) DOE Topic-4 superhot awardees — 4–10 awards at $4–25M each when the topic opens [DD-C27-13]; (3) Quaise + a handful of superhot developers [DD-C27-20]; (4) NASA/AFRL programs [DD-C27-21][DD-C27-23]; (5) national labs. **Current countable merchant POs for >250°C power modules: ~zero.** Everything above 230°C today is grant-funded engineering. That is the central fact of this deep dive.

**Bottom-up beachhead arithmetic (2031–32, US):**
- *Superhot/HT geothermal toolsets:* Fervo Cape ramps 100 MW (2026) → 500 MW (2028), approved to 2 GW [DD-C27-19]; ~15 wells drilled by Oct 2024 and accelerating. Assume next-gen geothermal drilling of 50–150 wells/yr by 2031, of which the >250°C tail (superhot field tests, hottest Fervo/Quaise pads) is **5–20 wells/yr** → 10–25 HT toolsets in service (incl. backups, high attrition).
- *Module content:* 2–3 power modules per toolset (PSU + pulser driver + steering motor drive) × ASP **$25–75K** (anchored on 195°C tools costing 3–5× conventional [DD-C27-16]; one-pager's $30–150K is the optimistic edge).
- *New-build + attrition (~40%/yr in HT service):* 15 toolsets × 2.5 modules × $50K × 1.4 ≈ **$2.6M/yr**, range **$0.9–5M/yr**.
- *Program/NRE revenue* (DOE subawards, lab buys, qualification units): **$1–4M/yr** — this is what Ozark's 15-year record shows is actually harvestable (~$9M cumulative) [DD-C27-05].
- **Beachhead SOM ≈ $2–9M/yr by 2032.** Small. The red team's "−1 market" adjustment is confirmed by the arithmetic.
- *Adjacent 200–250°C oil/gas HPHT retrofit* (competing with CISSOID/Watt&Well on power density): HT-electronics content of the MWD systems market — top-down triangulation: MWD systems ≈ **$3.7B (2025)** [DD-C27-29] (a separate Tier-3 series prints LWD services at $16.7B — the definitions conflict; both are services-heavy, so treat hardware content as far smaller); power-electronics hardware content ~5–10% → $190–370M/yr; the >200°C slice ~10–20% → **SAM ≈ $20–75M/yr**, growing with well temperature. Capturing 10–20% by 2033 adds $2–15M/yr — *if* oil capex recovers (§9).
- *Multi-market version (red-team issue #5):* aero-engine distributed control needs 250°C-ambient nodes [DD-C27-23] (decade-long quals, prime-mediated — real but slow); Venus/space 500°C (NASA HOTTech: 500°C/60-day program goal, SiC ICs already ran 60 days at Venus conditions [DD-C27-21][DD-C27-22]) — funded R&D, ~$1–3M/yr harvestable, never a market; molten-salt/nuclear instrumentation power — early. **Multi-market TAM for >200°C power electronics plausibly $100–300M/yr by early 2030s (low confidence, Tier-3-derived); venture-scale only if aero-engine electrification lands.**

## 6. Go-to-market

**Lead: US-first. China angle is structurally bad for this candidate (see §7).**
- **US sequence (2029→2032):** (1) 2029: incorporate; win DOE SBIR/GTO + AFRL non-dilutive money (Ozark's playbook, but for the *power* slot they left open); (2) 2030: paid qualification units to one DOE superhot field-test awardee and one independent tool builder — the reference-customer pattern for scientific/industrial buyers is a co-authored HiTEC/Stanford-Geothermal-Workshop paper with the customer's logo on the test data; (3) 2031: catalog 250°C PSU + pulser driver for MWD independents (displace Dewar flasks and Watt&Well at the top of their range); (4) 2032: motor-drive line; aero-engine R&D contract as second leg.
- **China sequence (do not lead):** the buyers are SOE oil majors already being served by a subsidized domestic champion at the chip level [DD-C27-26], government procurement carries a 20% evaluation preference for China-manufactured product from 2026 [POLICY_BRIEF §4.3], and CGS-system HDR programs procure domestically. A US-person founder selling US-built HT modules into Chinese SOEs fights price, preference, and export-control screening simultaneously. Treat China as: (a) competitive intelligence (谱析光晶's cost structure), (b) possible later licensing of *non-controlled* module designs — nothing more before Series A.
- **Channel:** direct, founder-led, Houston + DOE program offices; 5–10 accounts constitute the entire beachhead. Attend/publish at HiTEC (IMAPS), SPE/IADC, Stanford Geothermal Workshop.

## 7. Regulatory & geopolitical exposure (per `50_PHASE5_POLICY/POLICY_BRIEF.md`)

- **Item level:** downhole power modules from purchased dies are presumptively **EAR99**; power conversion is not an OISP-covered sector today [P-01][P-02 via POLICY_BRIEF]. Two design-stage tripwires: **3A225** (multiphase frequency changers ≥40 VA, >600 Hz, <0.2% frequency control — a precision downhole motor drive can *accidentally* classify; design out or license) and bundling with controlled sensors. Space/rad-hard variants jump to **9x515/ITAR** and make the company US-only [POLICY_BRIEF §1.2].
- **Customer level:** Chinese oil-SOE customers intersect the MEU/Entity-List and sanctioned-project screens; the policy brief's archetype (h) row flags downhole as "shares customers with sanctioned energy projects — separate analysis" and rates the China lane ⛔ for the space-adjacent variant [POLICY_BRIEF §5]. Affiliates Rule reactivates Nov-2026 — every Chinese customer needs an ownership tree.
- **Founder level:** founding/capitalizing a Chinese entity is an OISP covered-transaction question; power modules are outside covered sectors *today* but COINS gives Treasury sector-adding authority (~2027 regs) [POLICY_BRIEF §2]. Taking Chinese talent-program money would forfeit SBIR/DOE eligibility — which is this plan's cheapest capital; that alone settles US-first [POLICY_BRIEF §4.5].
- **Certification burden:** no statutory certification body; qualification is customer/program-specific (HPHT autoclave, shock/vibe per API/customer specs, 1,000+ h life test) — a cost and time burden (§8), not a legal one. **China-first is structurally hard here for demand-side reasons (procurement preference, domestic champion), before export controls even bite.** Not provisional — grounded in the Phase 5 brief.

## 8. Capital & milestones (2029→2032)

- **2029 (seed, $2.5–4M + target $1–2M non-dilutive DOE/AFRL):** 2–3 engineers; 250°C brassboard PSU (die-screened SiC/GaN, air-core or HT-ferrite magnetics); oven/HALT lab (~$400K capex); first SBIR Phase I/II. Burn ~$1.5M/yr.
- **2030:** 1,000 h life test at 250°C; 2 paid qualification units ($100–300K each, NRE-priced) to a DOE superhot awardee + 1 tool builder. First revenue **2030 ($0.3–0.8M)** — NRE, not product.
- **2031:** field trial on a customer's string (their rig slot, our module); catalog release of PSU + pulser driver; revenue $1–3M (mixed NRE/product); 300°C program variant funded by a Topic-4 subaward.
- **2032 (Series A gate):** A raise only if ≥2 design wins at tool builders + 1 aero/space contract; revenue $3–6M. If instead revenue is ~$1M of grants, the company is a fine 8-person consultancy — recognize that early and either bootstrap deliberately or fold the tech into a bigger harsh-env platform play (C26/C28 convergence).
- Total capital to Series A judgment: **$4–7M including non-dilutive** — inside deep-tech seed norms, thanks to no fab and buyable qualification equipment.

## 9. Risks & kill criteria (incl. red-team issue #4: timing)

1. **Market-timing risk (highest).** Oil upstream is in a second consecutive capex-cut year: EIA sees Brent averaging ~$59 in 2026 with production declining as rigs fall (oil rigs −33% since Dec-2022) [DD-C27-14][DD-C27-15]. The oil/gas expansion leg is dead until prices recover. The DOE bridge is real — $171.5M NOFO live in Feb-2026 with superhot topics [DD-C27-13] — but it is a *bridge funded by one agency's discretion*. **Kill if:** DOE Topic-4 (superhot field tests) has not funded awards by end-2027, or geothermal venture drilling (Fervo Phase II) slips past 2029.
2. **Demand-thinness risk.** Bottom-up beachhead is $2–9M/yr (§5). **Kill if:** ≥10 customer-discovery interviews in 2027 yield <3 tool builders willing to pay ≥$20K for a 250°C PSU, or Fervo/Quaise-class developers confirm they will keep drilling *below* the tool ceiling instead of paying for hotter tools (their current strategy: Fervo drills fast wells at ~200°C and treats 271°C as an envelope-push [DD-C27-18][DD-C27-19]).
3. **Passives supply risk.** 300°C magnetics/caps are recipes, not catalogs (§3). **Kill (the 300°C variant, fall back to 250°C) if:** by end-2027 no HT ferrite source or air-core design closes a >100 W, >85%-efficiency isolated converter at 275°C+ on the bench.
4. **Incumbent-response risk.** Watt&Well moving 220°C→250°C is a product refresh, not an invention; Honeywell can resurrect DM300-class power ASICs if DOE pays again. Moat is packaging + HF-magnetics know-how and qualification data — thin for the first 2 years.
5. **Solo-founder/channel risk.** Zero oilfield network; 2–4 yr sales cycles from a 2029 start put real product revenue at 2031–32. Needs a Houston-credible advisor/first hire by 2030.

## 10. Verdict

**Conviction: LOW-MEDIUM.** Low as the one-pager's geothermal-only "300°C module company" — the passives wall is passable but the 2031 beachhead is $2–9M/yr, grant-fed, and timed against an oil downturn; the red team's kill logic mostly survives contact with the evidence. Medium as a **multi-market harsh-environment power-electronics platform** (geothermal + aero-engine + space/nuclear R&D) launched at **250°C-native** — above every merchant module shipping today (220–225°C ceilings), buildable from catalog+screened parts by 2030 without a fab, squarely on the founder's GaN-physics + packaging + HF-power capability graph, and fundable by the same DOE/AFRL/NASA money that has kept Ozark alive for a decade — with 300°C as the program-funded flagship, not the business.

**Cheapest validations for Tim, 2026–2028 (PhD-compatible):**
1. **Bench the passives wall directly (~$20–30K, uses lab ovens):** build a 250°C-ambient, 100 W isolated GaN converter with air-core/HT-ferrite magnetics and Presidio-class caps; run 500 h hot. Publish at HiTEC or Stanford Geothermal Workshop — the publication *is* the market entry, and the result decides the 250°C vs. 300°C question with data.
2. **Count real willingness-to-pay (~$5K):** 12–15 structured interviews at IADC/Geothermal Rising/SPE with Erdos Miller/APS/Tolteq/Bench Tree engineering leads + 2 superhot developers: price anchor a 250°C PSU + pulser driver; collect ≥2 written LOIs or treat criterion 2 (§9) as triggered.
3. **Test the DOE bridge at zero cost:** track the $171.5M NOFO's later rounds; join one Topic-4 proposal in 2027 as the named power-electronics task lead (university subaward). If superhot topics don't open or proposals don't want the power task, the bridge is not there.

**Kill criteria:** as §9 — no DOE superhot awards by end-2027; <3 tool-builder buyers at ≥$20K/module; 275°C converter fails on the bench through 2027; or oil capex still contracting *and* geothermal drilling <50 wells/yr entering 2029.
