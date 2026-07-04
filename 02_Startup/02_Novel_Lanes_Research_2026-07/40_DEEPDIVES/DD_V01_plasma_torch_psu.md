# DEEP DIVE — V01: WBG retrofit PSU + closed-loop arc control for industrial plasma torches

**Date:** 2026-07-03 · **Launch lens:** 2029/2030 · **Prior scores:** raw 85.2 → RT-adjusted 73.2 (kill-prob 70%) · **Sources:** `DD_V01_sources.json` (28 unique: DD-V01-01..28; 24 verified:"fetched"; 20 fresh / 8 reused-refetched; Tier 1-2 = 15/28)
**POLICY_DELTA.md not yet present — Section 7 is PROVISIONAL own research** (GEN3 POLICY_BRIEF used as background only).

---

## 1. Problem & who has it

The sold problem: MW-class DC arc torches on hazardous-waste vitrification / ash-melting lines are availability-limited by electrode life and arc instability, and their supplies are legacy thyristor rectifiers. Who actually holds that pain, by archetype:

- **A1 — Chinese bolt-on plasma waste operators** (Foshan Huoshen 30 t/d kiln + 15 t/d plasma stage; CITIC Dongguan kiln+plasma; CGN Qingyuan demo; CASC's Jiangmen 30 t/d slag line, operating since 2018) [DD-V01-03][DD-V01-22]. This is the growing pool, but the torch, PSU, and plant arrive as one package from the institute/SOE that owns the technology (CASC 11th Institute/源动力, SWIP, CGN) [DD-V01-03][DD-V01-22]. They are not PSU shoppers.
- **A2 — Western torch-system buyers** (defense primes, aluminum smelters, cement): they buy *complete torch systems* from PyroGenesis — 4.5 MW system, CAD $4.13M, torch + peripherals + power supply delivered as one scope [DD-V01-01]. The PSU is a line item inside an OEM sale, not a separate purchase.
- **A3 — Plasma spray shops** (aerospace/turbine coatings): buy integrated spray platforms (Oerlikon Metco Surface One/MultiCoat class) where gun, gas module, controller, and plasma PSU ship together [DD-V01-04]. Merchant PSU purchases are limited to spares/retrofits — and that seam is already served (see §4, Spang).
- **A4 — Legacy Western retrofit base**: the archetype the one-pager was built on. It is small and broke: Europlasma is financing itself on a €30M OCABSA facility with >99% potential dilution, 529M shares outstanding (May 2026), FY2024 *and* FY2025 statements delayed [DD-V01-14].
- **A5 — Labs/pilots** (universities, institutes, SAF/H2 startups): buy catalog programmable DC (Magna-Power ML: 500 kW/1 MW units, to 6 kV / 5 kA, parallelable to 10 MW) [DD-V01-09] or 30–500 kW Chinese merchant plasma supplies (成都金创立, 60+ models) [DD-V01-11].

**Quantified niche:** the only archetype that matches V01's pitch (A4) is a few dozen operating Western MW torches attached to distressed owners. A1 is real and growing (China's Feb-2025 MEE guidance forces ≥30,000 t/yr new incineration units and <10% landfill share by 2030 — consolidation pressure that favors melting stages [DD-V01-23]) but is procedurally closed to a merchant US PSU vendor. **Resolution of question (a): a merchant torch-PSU seam exists, but it is small, retrofit-shaped, and already occupied** — Spang Power Electronics (Mentor, OH) explicitly sells "upgrades, retrofits, and complete replacements of existing dc plasma power supplies, including legacy systems originally supplied by AO Smith and Macroamp" [DD-V01-16]. V01's business already exists as a service line inside a 60-year-old custom power house.

## 2. Product & extreme edge (specs vs SOTA — corrected)

Proposed: 100 kW–2 MW SiC PSU + FPGA arc-impedance control; sold specs were "2–5x electrode life, 20–30% energy/tonne cut."

**Physics honesty (question c) — what a WBG PSU + fast control actually buys:**

- **Energy:** conversion is already ~95–98% efficient. Trade analysis of the same MW DC class (explicitly benchmarked against "large DC plasma torches (>10 MW)") puts IGBT active-front-end rectification at ~98.5% and SiC at >99%, with SiC devices ~4x Si price [DD-V01-17]; a peer-reviewed 2025 comparison finds thyristor systems >97.5% including transformer, SiC AFE gaining ~1.2 points [DD-V01-27]. **Honest sellable spec: 1.5–4 percentage points of electricity, plus power factor/THD compliance without filter yards — not 20–30%.** The 20–30% figures circulating in Chinese export-promotion material compare plasma *processes* against non-plasma incumbents (e.g., plasma coal-cracking vs. calcium-carbide acetylene), not PSU vs PSU [DD-V01-21].
- **Electrode life:** anode/cathode erosion is dominated by arc current magnitude, arc-root attachment mode and residence time, and gas dynamics — torch-side physics [DD-V01-10][DD-V01-26]. The big documented life lever is *sweeping the arc root magnetically*: Hydro-Québec's 1987 patent claims ~4.5x (400→2,000 h) via time-varying field coils [DD-V01-07]; EDF's 1995 patent drives arc-foot motion with a chopper resonating against cable inductance [DD-V01-08]; Westinghouse ships dual supplies with independently controlled arc and field-coil currents [DD-V01-25]; and the spray industry solved arc instability mechanically with cascaded anodes [DD-V01-10]. PSU-side levers (ripple suppression, restrike detection, soft start/stop, coordinated field-coil modulation) are real but second-order alone. **Credible claim: 1.2–2x on worn thyristor plants (red-team figure stands), possibly more only with field-coil co-control — i.e., partial torch co-design.**
- **What survives as the edge:** ignition reliability and start count (Longyuan advertises 1,500 consecutive starts on its 10 kW marine generator — start-life is a spec buyers already use [DD-V01-24]), turndown depth for load-following, footprint (SiC SMPS vs 12-pulse + filter bank), telemetry/arc-analytics software, and grid-side power quality. These are worth points of uptime and opex — a $100–300K premium story, not a plant-transforming one.

**vs SOTA numbers:** PyroGenesis APT-HP: 200 kW–2 MW (4.5 MW delivered; 20 MW on order since Oct 2024), stated cathode life ≤1,000 h / anode ≤500 h [DD-V01-01, RT-V01-01]. Magna-Power ML: 1 MW in one cabinet, 10 MW paralleled, catalog product [DD-V01-09]. 金创立: 30–500 kW plasma generators + supplies, 60+ models since 2007 [DD-V01-11]. A SiC 500 kW unit with arc analytics would be differentiated on control software and density, not on any spec the buyer currently writes into tenders.

## 3. Feasibility & TRL path to sellable v1 (2029–2031)

Straightforward for this founder — the problem is not feasibility.

- **BOM sketch (500 kW class):** 1,200 V/1,700 V SiC half-bridge modules (12–24), input 12-pulse or AFE stage, MF transformer or interphase chopper, water-cooled cold plates, film-cap bank, HF output inductor, Zynq-class FPGA/SoC controller + isolated sensing (Rogowski + fast V probes), PLC/telemetry layer, cabinet/EMC. Component cost ≈ $60–110K at qty 1–5; sell $250–400K → healthy margin at trivially small volume. (Estimate; SiC device pricing ~4x Si per [DD-V01-17].)
- **Buy vs build:** buy modules, gate drivers, cold plates, transformer; build topology integration, control firmware, arc-dynamics models, telemetry. No cleanroom anywhere (matches founder constraint).
- **TRL path:** TRL4 arc-emulator bench (2027) → TRL6 on a 100 kW university/institute torch (2028) → TRL7-8 first retrofit pilot (2029-2030). Gate: MW-class arc test access is owned by torch OEMs/institutes — the same entities positioned as competitors; without a partner, life-proof data (1,000+ h per point) doesn't exist before 2030.

## 4. Competitive landscape — global and Chinese

**Global:**
- **PyroGenesis (TSX: PYR)** — the healthy Western torch OEM: FY2025 revenue $12.57M (-19.6%), net loss $14.8M, cash $1.1M, backlog $47.8M (84% USD); segments: aluminum (Hydro, Constellium live furnace trials), cement calcination, Ti powder, radioactive waste, battery recycling [DD-V01-12]. **Question (b) resolved:** the red team's claim that PyroGenesis "holds granted IGBT torch-PSU patents US9,950,387 / US12,471,260" is **wrong** — US9,950,387 is Hypertherm's (plasma *cutting* chopper PSU, granted 2018) [DD-V01-05] and US12,471,260 is ESAB's (cutting PSU IGBT thermal management, granted Nov 2025) [DD-V01-06]. PyroGenesis's own portfolio is torches/processes; its 4.5 MW delivery shipped with the power supply arriving as a *separate peripheral component* [DD-V01-01]. No evidence they sell PSUs standalone; no evidence of in-house PSU IP either → **an OEM-supply (partner-not-compete) path is plausible and unproven — the single most valuable validation target.**
- **Spang Power Electronics (US)** — SCR *and* IGBT DC plasma rectifiers (6/12-pulse, chopper, SMPS) with digital current control and ripple filtering, for gasification, melting, spray, tundish, R&D; plus the retrofit service line naming AO Smith/Macroamp legacy fleets [DD-V01-16]. This is V01's product category, shipping today.
- **Magna-Power** (catalog MW DC) [DD-V01-09]; **Westinghouse Plasma** (dual-loop arc + field-coil control in WPCT540 class) [DD-V01-25]; Oerlikon Metco/Linde bundle PSUs inside spray platforms [DD-V01-04]; Tekna (Oslo-listed) integrates its own RF induction-plasma systems — Systems revenue ≈ US$8.1M for all of 2025 [DD-V01-13]; Europlasma distressed [DD-V01-14]; Advanced Energy sits in thin-film plasma, one adjacency away [RT-V01-17].

**Chinese (zh sourcing):**
- **Vertically integrated SOE/institute suppliers:** CASC 6th Academy 11th Institute / 西安航天源动力 (Jiangmen 30 t/d, first slag-treatment engineering application, 2018) [DD-V01-03]; **SWIP/核西物院** (30–300 kW DC torch series, 5 patents, 20 t/d ≈ CNY 50M capex, ~3-yr payback; medical-waste units) [DD-V01-22]; **CGN** (Qingyuan demo, ~40-patent cluster) [DD-V01-28]; **烟台龙源/Longyuan Tech (300105.SZ)** — plasma ignition incumbent now entering plasma solid waste: won China's first ship-based plasma waste project (Jan 2026; 10 kW, 5 kg generator, 1,500-start life, 300 h + 500 h validation) and told investors it is a named new growth lane; also signed an **Eskom (South Africa) plasma ignition demo in 2025 with a registered local subsidiary** — the Belt-and-Road export channel is real and occupied [DD-V01-24][DD-V01-19]. 江苏天楹 sells plasma melting furnaces (MEE catalog) [RT-V01-20].
- **Merchant PSU specialists:** **成都金创立** (2007; 5 product families, 60+ models; laminar generators to 100 kW, turbulent to 500 kW; Sichuan University teaching bases) [DD-V01-11]; **英杰电气 Injet (300820.SZ)** — platform industrial-PSU leader (founded 1996; polysilicon reduction-furnace supplies achieving import substitution since 2008; >70% share of PV power-supply config in 2022; 2023 revenue CNY 1.77B, +38%; GaN/SiC RF plasma supplies for etch/PECVD) [DD-V01-02] — for whom a DC torch supply is a trivial adjacency; 成都通用整流电器研究所 (since 1958) sells merchant rectifiers incl. plasma supplies [DD-V01-18].
- **Pricing signals:** complete 4.5 MW Western system CAD $4.13M [DD-V01-01] → PSU content plausibly $0.5–0.9M; SWIP whole-plant CNY 50M for 20 t/d [DD-V01-22]; Chinese merchant 100–500 kW supplies transact well below Western ASPs (金创立's class typically CNY 0.2–1.5M — estimate, unverified). A US-built SiC PSU at $150–600K faces Chinese units at a fraction of that.

## 5. Market: bottom-up beachhead arithmetic + top-down

**Bottom-up (retrofit beachhead as pitched):**
- West: operating MW waste/metallurgy torches worth retrofitting ≈ 30–80 (Europlasma/Inertam, Kobelco-lineage Japan, scattered defense/demil). Realistic capture 2029–2032: 3–8 units × $250–400K = **$0.75–3.2M cumulative** — not a company.
- China bolt-on new-builds: MEE-driven consolidation [DD-V01-23] supports maybe 10–30 new plasma melting/ash lines per year 2029–2032 (uncertainty high; no national count published). PSU+controls content $200–550K/line → served-market $2–16M/yr, of which a foreign merchant vendor realistically wins ~0 under institute self-supply (§6/§7).
- **Beachhead arithmetic fails: ≤$3M ARR by 2032 in the pitched wedge.**

**Top-down triangulation:** the flagship Western torch OEM books $12.57M/yr revenue *total* [DD-V01-12]; Tekna's systems business is $8.1M/yr [DD-V01-13]; syndicated "plasma torch market" reports scatter across $0.5–2.5B (SEO-grade, conflicting — not load-bearing; even accepting them, the *merchant PSU slice* of thermal-torch systems is plausibly 15–25% of a $100–300M annual system flow = **$15–75M/yr global SAM**, fragmented across cutting/spray/waste). Thermal-spray "market" figures ($8–16B) are coatings-services-dominated; the equipment sub-slice with its bundled PSUs does not open a merchant seam [DD-V01-04].

**Adjacent pivot (question e):** the strongest adjacent socket is **plasma metallurgy / critical-minerals powder and pilot lines** — where torch and PSU are sometimes procured separately, US policy money is flowing (Tekna's $8.1M order from a US critical-minerals customer, June 2026, deliveries 2027 [DD-V01-13]; PyroGenesis Ti powder + aluminum torch trials [DD-V01-12]), and SAF/H2 gasification developers (SGH2/Solena Lancaster: 12,000 kg H2/day from 40,000 t/yr waste; consortium already includes ABB for power; project still without published construction dates years after its 2023 permit [DD-V01-20]) — but summed, this socket is **$10–30M/yr near-term** and largely reachable only as an OEM module supplier, not a standalone product company. Battery-materials graphitization runs Acheson-type resistive furnaces on commodity high-current rectifiers in a brutally oversupplied Chinese anode market — no premium seam for a US startup (assessment; no credible contrary source found). Electrolyzer rectifiers are the real volume market in this converter class — and that is excluded neighbor C39.

## 6. GTM: China-first and US sequences

- **China-first (as pitched): fails.** Buyers are CASC/SWIP/CGN/Longyuan-affiliated programs that self-supply torches *and* supplies under 自主可控 procurement [DD-V01-03][DD-V01-22][DD-V01-24]; the merchant tier below them (金创立, Injet) owns the domestic price ladder [DD-V01-11][DD-V01-02]; and China's own export machine is pitching thermal plasma outbound along Belt-and-Road (Shanghai going-global center, Feb 2025; Longyuan's Eskom beachhead) [DD-V01-21][DD-V01-19]. A US-incorporated vendor selling PSUs *into* this stack inverts the 国产替代 direction. China's role for V01 is component sourcing only.
- **US-first (defensible variant):** lead with **OEM partnership** — PyroGenesis-class torch OEMs and destruction-skid builders who today source PSUs as peripherals [DD-V01-01]; second channel: DoD/DOE demil and critical-minerals pilots (PyroGenesis's own 4.5 MW client is a defense prime innovation hub [DD-V01-01]). Sell the arc-control module + SiC power stage as the OEM's branded supply. This is a components/JDM business: real, but it caps at low-$M/yr per OEM and concedes the customer relationship.
- **Which leads:** US OEM-partner track leads; China is supply chain. If PyroGenesis (or Spang, as acquirer-of-product) declines, there is no channel left — that binary is testable in 2026–2027 for the cost of two meetings (§10).

## 7. Regulatory & geopolitical exposure — **PROVISIONAL** (no POLICY_DELTA.md yet)

- **Export controls:** MW DC supplies are generically EAR99, but precision converters sit near nuclear-adjacent ECCNs (3A225-class frequency changers; GEN3 brief background) — classification review required before any China/BRI shipment; hazardous-waste SOE end-users (CGN = nuclear SOE) raise end-user diligence burdens. Selling *into* Chinese SOE waste projects also collides with procurement localization (首台套/自主可控 posture) — practically foreclosed regardless of law [DD-V01-03][DD-V01-22].
- **Tariffs (fetched, current):** US–China truce holds until **2026-11-10** (10% reciprocal band; China's retaliation suspensions run to 2026-12-31); trade-weighted US tariff on China ≈29.7%; Section 301 machinery lists 7.5–100%; Chinese retaliatory rates 2.5–25% would hit a US-origin PSU entering China [DD-V01-15]. Plan on tariff-driven BOM/China-market asymmetry persisting through 2029.
- **US-person China exposure:** power converters are **not** currently a covered sector under the outbound-investment regime (GEN3 brief) — sourcing SiC modules and subassemblies from China remains the widest legal lane, but the regime is expansion-prone (COINS Act sector-adding authority). Founding a China entity for this product is unnecessary and unwise; export-compliance counsel before any BRI turnkey participation.
- **Demand-side policy:** China MEE Feb-2025 guidance (≥30 kt/yr units, <10% landfill by 2030) pulls plasma melting demand in China [DD-V01-23] — but never names plasma and confers no advantage on foreign suppliers. US side: no federal driver mandates torch retrofits; DoD demil and critical-minerals programs are grant/contract-shaped, favoring integrated system bids.

## 8. Capital & milestones 2029→2032 (if pursued despite verdict)

- **2026–2028 (pre-launch, ≤$150K):** validation experiments (§10); publishable arc-bench data; one OEM LOI or kill.
- **2029 (seed $2–3M):** 100 kW SiC arc-control PSU alpha on institute torch; 1 paid OEM pilot ($150–250K NRE). Team: founder + 2 PE engineers + 1 controls.
- **2030:** 500 kW beta; 1,000 h electrode-life A/B data; OEM design win → $1–2M bookings.
- **2031:** first retrofit or OEM production units; $2–4M revenue; decide platform pivot (electrolyzer-adjacent excluded; metallurgy pilots the only headroom).
- **2032:** $4–8M revenue *best case* — sub-venture-scale; capital efficiency acceptable but outcome shaped like a lifestyle components firm or an acqui-hire by Spang/AE/torch OEM.

## 9. Risks & kill criteria

| # | Risk | Likelihood | Kill criterion (pre-agreed) |
|---|---|---|---|
| 1 | No merchant buyer pool (confirmed shape) | High — Spang occupies US retrofits [DD-V01-16]; China self-supplies [DD-V01-03][DD-V01-22] | <2 of 10 target operators/OEMs will take a paid pilot by mid-2027 → kill |
| 2 | Physics under-delivers | Med-High — life gain ≤1.5x without field-coil co-design [DD-V01-07][DD-V01-10] | Bench A/B shows <30% wear improvement from waveform control alone → kill retrofit claim |
| 3 | OEM partner declines / builds in-house | Med — PyroGenesis PSU sourcing opaque [DD-V01-01] | No OEM LOI by Q2 2027 → kill |
| 4 | China price umbrella collapses ASP | High — 金创立/Injet class pricing [DD-V01-11][DD-V01-02] | Any competitive quote <50% of our BOM-justified ASP in a live deal → exit segment |
| 5 | Trial timelines exceed runway | High — 1,000 h/point life proofs [DD-V01-22] | First pilot slips past 9 months of contract signature → restructure to software-only telemetry |
| 6 | Tariff/localization wall in China | High [DD-V01-15] | (Already assumed — China demoted to sourcing) |

## 10. Verdict

**NO-GO as a standalone company; conviction LOW (concur with red team, sharpened: the buyer-pool objection survives fact-checking even after correcting the red team's patent misattribution in V01's favor).** The seam V01 wants is (i) occupied by Spang/Magna-Power/金创立 at lower price points, (ii) bypassed by vertically integrated Chinese SOEs and bundling OEMs, and (iii) capped by physics at 1.5–4 efficiency points and ~1.2–2x life — below a venture-grade spec wedge. RT-adjusted 73.2 was, if anything, generous; showdown-comparable ≈64e stands. Keep only as a *capability seed* (SiC + FPGA arc control) usable inside stronger candidates (e.g., V02-class purpose-built skids where the PSU is inside a product the startup owns).

**Cheapest 2026–2028 validation experiments:**
1. **Procurement-ledger pull (~$500, 2 wks):** 采招网/千里马/中国政府采购网 records for Foshan Huoshen, CITIC Dongguan, CGN Qingyuan, Jiangmen, Tianying — extract who won the 电源系统 packages and at what CNY prices (my searches found no public PSU award records — direct registry pull required). Confirms/kills the "China buys merchant PSUs" premise with named vendors.
2. **Two OEM conversations (~$3K, 1 mo):** PyroGenesis engineering (does the 4.5 MW PSU come from a third party? would they OEM a SiC arc-control supply? [DD-V01-01]) and Spang (would they license/acquire an arc-analytics control layer? [DD-V01-16]). Either yes → revisit as component/JDM play; both no → hard kill.
3. **50 kW arc-emulator A/B bench (~$40–60K, 6 mo, univ. torch access):** measure electrode wear vs waveform (ripple spectrum, restrike handling, field-coil modulation) to publishable standard — settles the attribution question (§2) for any future plasma-power candidate, including V02.

## 11. NOVELTY DEFENSE — nearest excluded neighbors

- **N08 (industrial pulsed power / PEF processing):** different waveform regime (continuous negative-resistance DC arc vs. µs pulsed fields), different buyer (waste/metallurgy operators vs. food/materials processors), different failure physics (electrode arc-root erosion vs. treatment-chamber field uniformity). Not a re-parameterization.
- **C10 (precision magnet / scientific converters):** C10 sells ppm-class static accuracy to physics facilities; V01 sells kHz-class dynamic stiffness into an arc that *wants* to run away. Spec axis (dynamics vs. precision), buyer, and qualification regime all differ.
- **N05 (solid-state RF/microwave process heat):** different energy-coupling mechanism entirely (electromagnetic radiation into dielectric loads vs. ohmic/thermal DC arc through ionized gas); different frequency domain (MHz/GHz vs. DC-100 kHz); no shared buyer.
- **C35/N02 (accelerator RF):** RF cavities for beams — physics-facility procurement, superconducting-adjacent stack; nothing in common but "power electronics."
- **C39 (electrolyzer power modules) — the truest neighbor (red team, concurred):** same converter family, but electrolyzers are quasi-static loads where thyristor economics win on efficiency/cost [DD-V01-17][DD-V01-27]; arcs demand fast closed-loop control — the product function, load physics, and buyer differ. V01 is genuinely novel at application level; **its problem is not novelty but the absence of a reachable buyer** — novelty verdict NOVEL (narrowly) is reaffirmed, and the kill is commercial, not originality-based.

---
*Conflicting data noted per standards: (1) red team attributed US9,950,387/US12,471,260 to PyroGenesis; Google Patents shows Hypertherm and ESAB respectively [DD-V01-05][DD-V01-06] — red-team objection C7 partially reversed, without changing the verdict. (2) Syndicated torch-market sizes conflict ($0.5B–$2.5B) and are excluded from load-bearing use. (3) Injet 2025 segment figures from a secondary reposting parsed inconsistently and were excluded; 2023 figures from Yicai used instead [DD-V01-02].*
