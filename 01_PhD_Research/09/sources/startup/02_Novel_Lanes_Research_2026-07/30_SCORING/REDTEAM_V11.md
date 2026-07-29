# RED TEAM — V11 Robotic magnet-harvesting disassembly cell (lane G07)

Date: 2026-07-03 · Raw 86.8 · RT-adjusted **72.0** · Kill-probability **60%** · Novelty: **NOVEL**

## 1. Novelty verification (G7-NOVEL)

Three nearest ledger neighbors: **IND-09** (autonomous machining cell — subtractive manufacturing for defense castings; buyer = machine shops), **IND-23** (tactile micro-assembly cell — builds devices; buyer = electronics manufacturers), **CL-14** (robot/surgical actuation engines — sells actuators, not cells). V11 inverts the process direction (disassembly for material recovery) and the buyer segment (recyclers/dismantlers). **C40/RID-016** (second-life battery grading/repurposing) untouched: V11 never grades packs. No G01 role (no manufacturing-line function). Not a re-parameterized variant of any ledger entry; the G07 lane is charter-virgin. **Verdict: NOVEL — G7-NOVEL passes.** Novelty of the *category*, however, does not mean the market is empty (below).

## 2. Strongest bear case

The two dominant recycling routes don't need intact magnets. HyProMag's HPMS removes magnets from **full rotor assemblies including on-shaft, glued EDU magnets — no prior disassembly — 96–100% separation in ~6-hour cycles** [RT-V11-01]; hydromet/chromatography routes (ReElement, Cyclic's REEPure) digest shredded feed. Of V11's named buyers, the ones that do remove magnets already built captive removal: Cyclic's **Mag-Xtract, running 2,200 lb/hr since Sept 2023** [RT-V11-04]; GEM ran a national 863 program on 电机拆解装备 and operates robotic auto-disassembly lines in Wuhan [RT-V11-12]. The merchant TAM collapses to short-loop magnet-to-magnet players (Noveon-style, which genuinely needs harvested magnets ≥ HDD size [RT-V11-13]) plus reuse dismantlers — a handful of accounts by 2029, each tempted to build in-house like everyone before them.

## 3. Hidden competition (missed by one-pager)

- **Molg** — $5.5M seed (Oct 2024; Closed Loop, Amazon, ABB Ventures), robotic disassembly microfactories already installed at Sims Lifecycle Services and rolling into hyperscaler ITADs [RT-V11-02][RT-V11-03]. Same product category, 4-year head start on recipes.
- **Fraunhofer iDEAR** (IFF) — the ADIR successor the one-pager's "never commercialized" framing hides: active AI/robotic e-waste disassembly, Feb 2025 push [RT-V11-07][RT-V11-08]; **DeMoBat** (IPA/KUKA) built Europe's largest battery-and-motor disassembly test facility [RT-V11-09]; **REASSERT** (Schaeffler-led) covers motor disassembly + demag + reman [RT-V11-10]. Free/licensable public IP for any integrator.
- **Apple Daisy/Dave/Taz** — 1.2M iPhones/yr, magnet-bearing module recovery, **patents offered license-free with zero takers** [RT-V11-05] — a market signal that recyclers won't adopt even free disassembly IP.
- **Hitachi** solved automated HDD magnet recovery at ~100 units/hr (8x manual) in **2010** and it still never became a merchant equipment business [RT-V11-06].
- **Chinese equipment vendors**: Zhejiang Weibo's Giant-2000 stator recycling line, Henan Suyuan 电机拆解设备 — shred-and-separate motor lines at commodity prices that cap what a US cell can charge [RT-V11-11].

## 4. Engineering reality check

"10–60x manual throughput" across "motors, HDDs & turbine generators" is three machines pretending to be one. EV rotors vary wildly (surface vs. buried IPM magnets, epoxy potting, on-shaft interference fits); each SKU = new fixturing + recipe; peer-reviewed work calls magnet-intact extraction "very challenging" and disassembly workshops SKU-limited [RT-V11-16]. Direct-drive wind generators carry up to ~4 t of magnets in 70 t assemblies handled with cranes at hub height [RT-V11-14] — not a robotic-cell workpiece at all. Realistic v1 = HDD + 2–3 motor families; Hitachi's drum-shaker beat exactly that scope 15 years ago.

## 5. Willingness-to-pay skepticism

Who pays $400K–1.2M/cell? Recyclers running thin margins on volatile REE prices, whose alternative is $18/hr labor or whole-assembly HPMS/shredding. Manual dismantling is documented as cost-prohibitive per unit in the West [RT-V11-16] — but that argues volumes go to no-disassembly routes, not to capex robots. No named buyer has published a capex line for merchant disassembly cells; DoW's $1.4B funds chemistry and magnet-making capacity, not cells.

## 6. Founder-fit doubts

Not PhD-lane, but discount anyway: one automated winding machine ≠ production robotics-integration pedigree. Vision + force control + fixturing is bread-and-butter for ABB/KUKA integrator networks (ABB literally backs Molg). The rare-combo premium behind C1=5 doesn't survive contact with the integrator ecosystem.

## 7. Score adjustments (±1, reasons)

| C | Raw→Adj | Reason |
|---|---|---|
| 1 | 5→4 | Integrator-commodity capability; ABB-backed Molg proves it |
| 2 | 4→3 | HPMS removes magnets from whole rotors — the 10–60x edge only matters on the short-loop route |
| 3 | 5→4 | Named buyers need no cell (HyProMag) or built captive lines (Cyclic, GEM); Noveon-class remainder |
| 4 | 4 | Expansion breadth real (boards, packs-as-equipment) — concede |
| 5 | 5→4 | Capacity equipment is being bought 2026–2028, before a 2029 entrant ships |
| 6 | 4→3 | SKU heterogeneity + wind-scale mismatch; recipe scalability unproven |
| 7 | 4→3 | Molg/iDEAR/DeMoBat/Apple-free-IP/Chinese lines — whitespace was stale |
| 8 | 4→3 | GEM is a 57-patent competitor, not a customer; Chinese vendors clone mechanical cells on price |
| 9,10,11 | 4/3/5 | Unchanged |

**Adjusted total: 72.0** (sum 360/5; was 86.8).

## 8. Steelman

Noveon-style short-loop recycling — the highest-margin, DoW-favored route — physically requires intact harvested magnets, and 600 kt of EOL magnet stock exists with <1% recycled today; nobody sells a merchant harvesting cell for motors specifically. If HPMS licensing stalls (one 5 t/batch vessel, 9.2 t cumulative output to date) and reuse/reman mandates (EU CRMA, REASSERT-style OEM programs) reward intact magnets, a recipe-library cell vendor could become the pick-and-shovel standard the way Molg is for servers.

---
**RETURN: V11 · kill-probability 60% · biggest objection: the dominant recycling routes (hydrogen decrepitation on whole rotors, hydromet on shred) don't need intact-magnet extraction, and the buyers who do extract already built captive lines — leaving a Noveon-sized niche, not an equipment market · novelty verdict: NOVEL**
