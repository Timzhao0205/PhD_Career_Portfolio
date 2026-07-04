# DD_C01 — MW-class Ruggedized SiC Power-Electronics Building Blocks (marine / off-highway / defense)

Candidate: C01 · Phase 3 score 75.2 (rank 15), red-teamed to ~80% kill probability · This deep dive **explicitly resolves the three REDTEAM_C01 objections** (marked ▶RT-1…▶RT-3 inline) and answers the orchestrator's question: *is the strongest surviving version actually C03's thesis — aviation-class kW/kg conversion for electric marine/UxV?* (Answer: yes; §2, §5, §10.) Sources: `DD_C01_sources.json` (25 unique; 13 Tier 1–2; 9 Chinese-language). Section 7 draws on `50_PHASE5_POLICY/POLICY_BRIEF.md` [P-##].

---

## 1. Problem & who has it

The original C01 framing ("integrators buy a qualified MW brick instead of an 18-month in-house design") describes a real procurement pattern — but the buyers it named are already served (§4). The customers who are *demonstrably not* served, and for whom conversion density is mission capability rather than cabinet convenience, are:

- **The propulsion lead at a US uncrewed-vessel builder.** The Navy merged LUSV/MUSV into the **Modular Attack Surface Craft (MASC)** program in 2025; FY2026 is an industry prototyping phase, with variants specified by payload (2–4 × 40-ft containers, 2,500+ nm range, 25+ kt in Sea State 4) and the FY2026 NDAA §130 requiring "purpose-built unmanned vessels engineered to operate without human support systems" [DD-C01-02]. Below MASC, attritable small ASVs are already in series production: Saronic's 24-ft Corsair (1,000 nm, 35+ kt) went "prototype to production in under 12 months" and took a Navy production contract with **$200M obligated immediately** in Dec 2025 [DD-C01-12]. These builders move at startup speed, hold venture-scale budgets, and have no legacy marine-drive supply relationships. Long-range/loiter USV missions force diesel-electric or hybrid architectures — on a 24–90-ft hull, every kg and liter of the power chain trades against payload, fuel, and range.
- **The electrical architect of a fast electric or foiling craft** (crew-transfer vessels, hydrofoil ferries, patrol/harbor craft). At the fleet level, electrification is no longer speculative: DNV's AFI counted **1,794 alternative-fuel-capable vessels in operation and 1,544 on order as of Aug 2025** [DD-C01-13]; Incat's Hull 096 carries a **40 MWh** battery — 4× any prior ship — toward late-2025 sea trials, and Norway alone runs ~80 electric ferries [DD-C01-15]. IMO's 2023 strategy (5–10% zero/near-zero energy by 2030, net-zero ~2050) keeps the regulatory floor rising [DD-C01-14]. Displacement ferries tolerate cabinet drives; *planing and foiling* craft do not — they need automotive/aviation-class density with marine ruggedization, which no catalog vendor ships today (§4).
- **The defense test-infrastructure engineer** feeding directed-energy and sensor loads: ONR's own converter push explicitly targets power for "laser weapons, RF weapons, and radar systems" [DD-C01-01], and ONR Code 331 funds power-density/MVDC component research as a standing thrust [DD-C01-03]. Navy STTR topic N21A-T012 quantifies the ask: WBG converter modules "approaching 100 kW/L" with >500 W/cm² device heat flux [DD-C01-10]. Tens of buyers, deep budgets, lumpy orders.

**Who does NOT have the problem:** crewed-combatant programs (GE Vernova/Leonardo DRS territory, ▶RT-1), displacement ferries/tugs/workboats (Danfoss/ABB cabinet territory), and Chinese yards (CSSC-captive, §4/§7).

## 2. Product definition & the extreme-performance edge (▶RT-1 resolved; C03 merge adopted)

**▶RT-1 (the whitespace is occupied) — the red team is right about the category as chartered, and the one-pager's beachhead is retired.** ONR's PEBB productization went to GE Vernova: a **$10.4M Phase 3 rapid-prototyping order (June 2025, complete June 2027)** for the SiC-MOSFET hybrid modular multilevel converter for Navy propulsion [DD-C01-01]; GE holds granted patents on the hybrid-PEBB architecture itself (US 11,831,250, SiC-MOSFET low-voltage + Si-IGBT high-voltage stages for "military and commercial marine applications") [DD-C01-04]. The commercial "brick to integrators" tier is Danfoss (iC7-Marine liquid-cooled modules, 170–6,400 A, engineered-to-order) [DD-C01-06] and ABB's Onboard DC Grid platform [DD-C01-25]. A generic "MW SiC PEBB catalog" startup enters fifth. **Kill the original framing.**

**What verifiably remains open — and it is C03's thesis wearing C01's ruggedization:** a *weight/volume-critical, marine-ruggedized* 50–500 kW conversion tier that neither the cabinet vendors nor the automotive-COTS vendors serve:

| Benchmark (verified) | Density | Environment | Gap it leaves |
|---|---|---|---|
| Danfoss iC7-Marine [DD-C01-06] | Cabinet-class ("40% less space than closest competitor" — still switchboard-room hardware) | Marine, class-approved | Useless on a 24-ft USV or foiler; engineered-to-order lead times |
| Cascadia CM350SiC [DD-C01-07] | 500 kW *peak* in 14 kg (~36 kW/kg peak; continuous 500 Arms, far lower) | Automotive; no marine class, no naval shock | Density without qualification or marine I/O |
| H3X IMDs [DD-C01-08] | up to 12 kW/kg *continuous*, 30 kW–1 MW+ | Aero/defense/marine incl. USVs | **Motor-integrated** drives only — not standalone DC-DC / rectifier / bus bricks |
| NASA 250 kW EAP converter [DD-C01-09] | 10.6 kW/kg, 99.3%, 1 kV bus | Aviation lab/altitude | Proves the physics envelope; not a marine product |
| Navy STTR target [DD-C01-10] | modules "approaching 100 kW/L" | Naval shock/vibe/EMI | States the demand; no shipping product |
| PEBB 1000 research line (1.7 kV SiC H-bridge, 100 kHz) [DD-C01-05] | lab prototype | Navy-sponsored | Never commercialized below prime tier |

**Product (v1, 2029–2031): "attritable-fleet power bricks."** A family of standalone, liquid/seawater-cooled, IP67, shock-rated SiC conversion modules for uncrewed and fast electric craft: (a) **250 kW bidirectional DC-DC / battery-interface brick**, 800–1,000 V bus (the DC-1000V bus is already the emerging norm — even China's new electric tugs run DC 1000 V integrated power [DD-C01-23]); (b) **150–350 kW propulsion inverter** at ≥10 kW/kg *continuous* and ≥20 kW/L — i.e., NASA-class specific power [DD-C01-09] held under marine shock/vibe/salt, versus peak-rated automotive COTS [DD-C01-07]; (c) **genset active-rectifier brick** for hybrid loiter architectures; plus the HW+SW layer the founder wants: gate-drive/protection firmware, health monitoring, fleet-level power-management API for autonomy stacks. The 10× is not raw density (Cascadia's peak number already looks spectacular); it is **continuous, qualified density in salt water** — a packaging/thermal/reliability claim squarely on the founder's Rivas-collaboration + harsh-environment-packaging axis.

Honesty note: this is a **2–4× system-level edge over what integrators can actually buy qualified today**, not 10× over physics; and H3X can flank into standalone bricks at any time (§9).

## 3. Technical feasibility & TRL path

- **Buy:** SiC modules (1,200 V automotive/industrial grade; 1.7 kV for the MVDC-stack variant later), gate drivers, film caps, cold plates, DSP/FPGA control. **Build:** the thermal stack (the Navy's own topic says heat flux is the binding constraint [DD-C01-10]), busbar/EMI design at 50–100 kHz (Chinese military-marine literature confirms 50 kHz+ SiC operation is where filter mass collapses [DD-C01-20]), potting/enclosure for salt-fog and shock, protection firmware. **Cleanroom dependence: none.**
- **Bench-provable during the PhD:** a 100–250 kW, ≥20 kW/L liquid-cooled brick with continuous-power thermal proof is a <$60K, 1–2-person-year artifact; salt-fog (ASTM B117) and MIL-STD-810/167-1 vibration screening are commercial-lab services; MIL-DTL-901 *lightweight* machine tests run in 1–3 days at commercial labs [DD-C01-11].
- **Hard parts:** (i) continuous-rating honesty — automotive peak ratings hide 30-s limits [DD-C01-07]; the differentiator is a coolant-to-junction design that holds nameplate indefinitely; (ii) class/qualification paperwork (DNV/ABS type approval for the commercial line; see §9 for the defense qual path); (iii) MW-level test loads are NOT needed for v1 — the product tops out at 500 kW/brick, and a 250 kW regenerative back-to-back test rig is ~$150–400K, not the red team's $2–5M (that figure belongs to the retired MVDC-system framing, ▶RT-2 partially conceded on the original scope).
- **TRL path:** TRL4 bench 2027 → TRL6 sea-trial units on a partner USV/foiler 2030 → TRL7–8 qualified family 2031. First *paid* prototypes plausibly 2030; catalog revenue 2031+.

## 4. Competitive landscape — global and Chinese

**Global (all positions verified this mission):**
- **GE Vernova Naval Systems** — owns the Navy PEBB/HMMC productization through at least June 2027 [DD-C01-01] and the hybrid-PEBB patent estate [DD-C01-04]. Do not compete; potential eventual channel/acquirer.
- **Danfoss** (iC7-Marine modules 170–6,400 A, engineered-to-order [DD-C01-06]) and **ABB** (Onboard DC Grid modular platform [DD-C01-25]) — own crewed-vessel cabinet conversion. Their catalogs stop where weight-critical platforms begin.
- **H3X** — the most dangerous neighbor: 12 kW/kg continuous integrated motor drives, 30 kW–1 MW+, explicitly marketing to USVs, submarines, workboats, NASA/USAF/AFRL/Lockheed logos [DD-C01-08]. Today it sells *motor-integrated* units; a standalone-converter line would collide head-on.
- **Cascadia Motion (BorgWarner)** — automotive-grade SiC inverters (CM350SiC: 500 kW peak/14 kg, 200–850 VDC) reachable by any integrator willing to self-marinize [DD-C01-07]. The startup's pitch must beat "Cascadia + in-house ruggedization" on total cost and risk.
- **Epirus/DEW primes** — solid-state HPM at production scale shows defense willingness to fund compact power (context; test-bench sales are adjacent, lumpy).

**China (Chinese-language sourcing) — ▶RT-3 resolved: the red team is confirmed and extended.** The Chinese marine-electrification chain is CSSC-captive end to end:
- **中国船舶712所** is the state-designated marine electric-propulsion integrator; its new-energy subsidiary 威迈动力 is expanding shore-based integration-test infrastructure as of June 2026 (tender on CSSC's own bidding platform) [DD-C01-24] — integration capability is being *built in-house*, not procured.
- **中船赛思亿 (CSSC-SETH)** — series deliveries of complete propulsion sets (e.g., 7 vessel sets in one 2022 batch, including a *hybrid unmanned twin-hull* with 2×200 kW thrusters — note: China's USV power chain is also captive) [DD-C01-22]; in Feb 2025 it committed a **~¥1B** new-energy marine electro-control manufacturing base in Wuxi, backed by CSSC's Fenxi Heavy Industry [DD-C01-21].
- **中船动力研究院/704所-系** delivered China's largest pure-electric tugs (5,400 HP, 6,700 kWh, **DC 1000 V integrated propulsion**, 2 MW PM motors at 97.5% efficiency) with all electrics sourced inside the group [DD-C01-23].
- **SiC in marine is already a Chinese military-institute research topic:** 武汉第二船舶设计研究所 published SiC marine-converter work (30 kVA, 50 kHz, ~1 W/cm³, 96%) in 舰船科学技术 back in 2020 [DD-C01-20] — the naval institutes intend to make, not buy.
- **Demand is real but closed:** China's electric-vessel market grew to ¥14.8B (2024) with EVTank projecting **¥36.75B by 2026** and 11.2 GWh of marine battery demand; ~700 battery-equipped vessels were operating domestically by Aug 2024 [DD-C01-19]. The demand pull is state policy — the five-ministry inland-vessel Implementation Opinion (battery-electric priority segments, swap-standardization pilots across nine provinces) [DD-C01-16], the scrappage-renewal subsidy running to end-2028 (inland newbuild subsidies capped at ¥40M/vessel) [DD-C01-17], and CCS's 2025 battery-power rules effective 2026-01-01 [DD-C01-18]. Every one of those instruments channels orders to domestic (overwhelmingly CSSC-affiliated or A-share) suppliers.

**Pricing signals:** Chinese complete small-vessel propulsion sets (tens-of-kW class, per CSSC-SETH deliveries [DD-C01-22]) imply system prices well under Western defense ASPs; Western USV builders, by contrast, operate under $200M+ production contracts [DD-C01-12] where a $50–150K power chain is a rounding error — supporting high-end niche pricing in the US and none in China.

## 5. Market: beachhead sizing (bottom-up), then triangulation

**Beachhead = US/allied uncrewed + fast electric craft, 2030–2032. Explicit arithmetic (units × ASP):**

1. **MASC-class hybrids.** CRS documents the program but no production quantities yet (prototyping FY2026) [DD-C01-02]. Assume 15–40 hulls/yr by 2031–32 (uncertainty stated; Replicator-style intent supports the high end), hybrid-electric share 25–50%. Conversion content per hybrid hull: 2 propulsion inverters (300–400 kW) + 2 active rectifiers + DC-DC + controls ≈ **$250–500K**. → (4–20 hulls) × ($250–500K) = **$1–10M/yr**.
2. **Small attritable ASVs.** Corsair-class production is real ($200M obligated to one vendor in Dec 2025 [DD-C01-12]); fleet ambitions imply high hundreds to thousands of units/yr across vendors by ~2031. Most are pure-ICE today; assume 10–20% adopt 50–150 kW hybrid/quiet-loiter chains at **$20–60K content**: (75–300 units) × ($20–60K) = **$1.5–18M/yr**.
3. **Fast/foiling electric craft (ex-China).** Global electric-vessel momentum [DD-C01-13][DD-C01-15] but weight-critical builds are dozens/yr; content $60–150K; winnable share ~20–30 units → **$1.5–4M/yr**.
4. **Defense/DEW test infrastructure + mobile MW charging bricks.** Tens of buyers, $80–500K systems [DD-C01-03][DD-C01-10]; lumpy → **$1–3M/yr**.

**Bottom-up SOM 2032: ~$5–35M/yr; central estimate $10–15M/yr** at 40–60% hardware gross margin. Honest reading: viable seed-stage niche, venture-scale *only if* USV electrification penetrates faster than assumed or the MW-charging/off-highway adjacency opens.

**Top-down triangulation:** China's electric-vessel market alone is projected ¥36.75B (~$5B) in 2026 [DD-C01-19]; power-conversion content of vessel electrification typically ~10–20% of powertrain value → order **$0.5–1B China + a comparable rest-of-world = $1–2B global SAM-superset**, of which the ruggedized weight-critical tier (the startup's actual SAM, US/allied-addressable) is plausibly **$150–400M by 2031**. Bottom-up SOM of $10–15M ≈ 3–7% of SAM — internally consistent. Conflict noted: Chinese sources give both "440+ pure-battery vessels built/building (June 2024)" and "~700 battery-equipped vessels (Aug 2024)" [DD-C01-19]; both retained, definitions differ (pure vs. equipped).

**Expansion:** off-highway/mining retrofit inverters → mobile megawatt charging power stages → MVDC stackable bricks for defense primes (the GE-adjacent tier) → certified-aviation supply once volumes justify (the reverse of the usual path; NASA benchmarks show the spec continuity [DD-C01-09]).

## 6. Go-to-market

**US-first, unambiguous.** Sequence: (1) 2027–2028, during PhD: bench brick + two design-partner relationships (one USV builder, one foiling-craft OEM) won on spec sheets and fast iteration; (2) 2029–2030: paid prototype programs (NRE-funded, $200–500K each) + Navy SBIR/STTR entries against standing power-density topics [DD-C01-10][DD-C01-03]; (3) 2031: DNV/ABS type approval of the commercial line to unlock crew-transfer/ferry OEMs; sell defense variants only via platform builders (Saronic-class) and primes, never direct-to-NAVSEA. Reference-customer strategy: one named USV design win matters more than any trade-show catalog — attritable-fleet builders copy each other's supplier lists.

**China sequence: none for this candidate.** The buyer chain is CSSC-captive [DD-C01-21][DD-C01-22][DD-C01-24], procurement policy pays domestic [DD-C01-17], and any US defense-marine positioning makes Chinese entity involvement disqualifying (§7). The founder's China asset degrades to supply-chain literacy (component sourcing for the *commercial* line only, and even that carries defense-supply-chain content restrictions).

## 7. Regulatory & geopolitical exposure (per POLICY_BRIEF.md)

- **Item level:** generic SiC converter bricks are EAR99-class; power converters are "not currently covered sectors" under the outbound-investment regime [P-01][P-02] — but the moment the product is *designed for* a military vessel/USV, it migrates toward USML/600-series naval-equipment controls, and the company becomes a defense article producer with ITAR registration duties (POLICY_BRIEF §1.2, archetype-h logic). Plan classification review before the first defense deliverable.
- **China-first is structurally foreclosed, not merely hard.** A US-person founder building a China-facing marine-power company would (a) face the CSSC-captive market of §4 with a 20% government-procurement evaluation handicap as an importer, or mandatory China manufacturing to qualify as "domestic product" [P-32]; (b) forfeit US defense customers — FOCI/CFIUS screens treat an active Chinese sibling in a naval-adjacent domain as disqualifying [P-20]; and (c) sit under COINS-era sector-expansion risk through 2029 [P-03]. Parallel structure: ⛔ for this candidate (mirrors archetype h in the brief's framework).
- **Hiring:** defense-track work restricts PRC-national engineers (deemed exports/ITAR) [P-08][P-09] — a real constraint on the founder's China-network hiring advantage.
- **Supply chain:** Chinese SiC content into US defense platforms faces tightening DFARS-type sourcing restrictions; design the BOM dual-sourced (US/EU/Japan die) from day one. China's own materials controls (gallium etc., truce expiring Nov-2026) are a secondary watch item [P-36].

## 8. Capital & milestones (2029 → 2032)

- **2029 (found; seed $2.5–4M):** 2 engineers + founder; v1 brick family (250 kW DC-DC, 200 kW inverter); regenerative test rig ($150–400K); MIL-STD-810/167 + 901-lightweight screening ($100–200K) [DD-C01-11]; 1–2 SBIR Phase I ($150–300K non-dilutive).
- **2030:** two paid design-partner programs ($400–800K NRE revenue); sea trials on partner hulls; SBIR Phase II ($1–2M); headcount 6–8. Burn ~$2.5M/yr.
- **2031 (Series A gate, $8–15M):** DNV/ABS type approval on commercial line; first production PO from a USV builder (target $1.5–3M bookings); catalog launch.
- **2032:** $5–12M revenue if beachhead math (§5) holds. **First meaningful product revenue lands 2031 — two years post-founding, not the red team's 2032+, but only because the design targets uncrewed/commercial platforms that do not require Grade-A heavyweight qualification first (§9).**

## 9. Risks & kill criteria (▶RT-2 resolved: the qual path for a solo founder)

**▶RT-2 (MIL-DTL-901E + QVL reality):** the red team is right that Grade-A *heavyweight* barge qualification (floating shock platforms, 100,000+ lb class [DD-C01-11]) is a multi-$M, prime-scale undertaking no seed startup should self-fund. The resolution is sequencing, not denial: (a) **target platforms that don't impose it** — attritable USVs are procured outside the crewed-combatant qual stack (NDAA §130 explicitly frames them as engineered without human support systems [DD-C01-02]); (b) qualify at the achievable tier — 901 *lightweight/mediumweight* machine tests run in 1–3 days at commercial labs, and the DSSM covers Class II items to 2,400 lb without a barge [DD-C01-11]; (c) enter crewed-platform programs only as a **sub to a prime that owns system-level qualification**, with SBIR/STTR money paying for the module-level evidence [DD-C01-10]. Heavyweight barge testing happens if and only if an anchor program funds it.

**Residual risks, ranked:**
1. **USV electrification doesn't happen on schedule** — attritable boats stay pure-ICE (outboards win on cost/simplicity); the beachhead's largest tranche (§5 lines 1–2) evaporates.
2. **H3X flanks into standalone bricks** — it has the density, the defense logos, and the funding trajectory [DD-C01-08]; the startup would be a late second.
3. **Integrators self-marinize automotive COTS** (Cascadia + potting) at half the price [DD-C01-07].
4. **Solo-founder channel gap** in defense: no prime relationships; mitigated only partially by SBIR and the non-traditional USV builders.
5. **China: zero option value** (§4/§7) — the founder's strongest personal asset is unused in this candidate.

**Kill criteria (explicit):**
- By **end-2028**: no USV/fast-craft builder LOI or paid design-partner commitment after ≥15 structured customer conversations → kill.
- By **end-2028**: H3X or Cascadia/BorgWarner announces a marine-classed *standalone* converter line ≥10 kW/kg continuous → kill (whitespace gone).
- By **2030**: MASC production decisions show all-mechanical propulsion with no hybrid variants AND small-ASV hybrid share still <5% → kill or pivot the brick family to mobile-MW-charging/off-highway.
- Any point: entering a crewed-platform program requires >$1.5M self-funded qualification before first PO → decline that market, don't kill the company.

## 10. Verdict

**Conviction: LOW for C01 as chartered; MEDIUM-LOW for the surviving pivot.** The red team's core finding stands: the named beachhead (Navy PEBB, marine-integrator bricks) is occupied by GE Vernova above and Danfoss/ABB beside [DD-C01-01][DD-C01-06][DD-C01-25], and the China angle is CSSC-captive [DD-C01-21][DD-C01-24]. **The strongest surviving version is exactly the C03 merger the orchestrator hypothesized: aviation-class kW/kg, marine-ruggedized 50–500 kW conversion bricks for uncrewed and fast electric craft, US-first** — a real, quantified, but modest niche (~$10–15M/yr SOM by 2032, §5) with H3X already adjacent. C01 should not be pursued as an independent thesis; its surviving content should be folded into the C03 deep-dive lane and re-ranked there.

**Cheapest validation experiments (2026–2028, during PhD):**
1. **Customer-discovery sprint (~$5K + time):** 15–20 structured interviews across USV builders (Saronic, BlackSea-class, Blue Water Autonomy tier), foiling-craft OEMs, and two defense primes' power groups. Single question that decides everything: *do you buy third-party power stages, and at what spec/price/qual level?* Outcome: ≥2 LOIs or kill.
2. **SBIR/STTR probe ($0 cash):** track Navy/DIU power-conversion topics through FY2027–28 [DD-C01-10][DD-C01-03] and submit with a small-business partner; one Phase I award = $150–250K of non-dilutive validation that the density/shock spec is procurable by a newcomer. Two cycles with no award = negative signal on the defense channel.
3. **Density demonstrator (<$60K):** 100–250 kW SiC brick at ≥20 kW/L with *continuous* thermal proof and a lightweight-shock/vibe screening report [DD-C01-11] — the artifact that converts interviews into design-partner agreements, built on the founder's Rivas-collaboration bench skills without any MW infrastructure.

---
*Sources: `DD_C01_sources.json` (DD-C01-01…25). Policy citations [P-##] refer to `50_PHASE5_POLICY/policy_sources.json` via POLICY_BRIEF.md. Research synthesis, not investment or legal advice.*
