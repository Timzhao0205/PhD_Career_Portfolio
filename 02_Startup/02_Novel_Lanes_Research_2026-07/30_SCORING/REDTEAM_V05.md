# RED TEAM — V05 Compact berthed-load shore-tie frequency/voltage converter (lane G03)

Date 2026-07-03 · Raw 83.2 · Sources: `30_SCORING/REDTEAM_V05_sources.json` (RT-V05-01..21)

## 1. Novelty verification (G7-NOVEL)

Nearest ledger neighbors checked: **C01/C03** (MW SiC PEBB / marine propulsion inverters), **C04** (+PWR-12, W-HERON: MCS/SST road charging), **C09** (datacenter SST blocks), **C38** (GFM PCS compute microgrids), **N04** (subsea inductive). None sells stationary 50/60 Hz hotel-load interconnect to port authorities/shipowners: C01/C03 are drivetrain/USV propulsion (engines ON, integrator buyer); C04-family is road-vehicle DC charging (different connector, cert, buyer); C09/C38 are datacenter-segment. Not a re-parameterized variant of any entry — the guts overlap (AC-DC-AC PCS) but buyer segment AND category differ. **Verdict: NOVEL — G7 passes.** Caveat: the "workboat DC charging dispenser" expansion plank re-enters C04-adjacent territory and should be struck. The fatal problem is novelty vs. the *commercial market*, not the ledger.

## 2. Strongest bear case

The load-bearing claim — "nothing compact and catalog-priced exists below the ABB/Siemens EPC tier" — is false on both continents. By 2031 V05 is the 12th entrant in a bid-priced integration market, with no spec anyone asked for, arriving *after* the AFIR procurement wave (contracts for the 31 Dec 2029 deadline are being let 2026–2028; Skagen's 16 MW plant was awarded for the 2028 season [RT-V05-02]).

## 3. Hidden competition (the one-pager missed an entire industry)

West, compact/containerized tier: **PowerCon** (20-ft building blocks, "largest cruise ships … to smaller fishing vessels and ferries") [RT-V05-01/02]; **Danfoss iC7-Hybrid** catalog grid converters, 100+ units in Stockholm/Ålesund/Haugesund; PSW/FAYARD portable 2×20-ft units at 440/690 V [RT-V05-03/04]; **EnSmart** (containerized IP65 to 8 MW) [RT-V05-05]; **Sinepower**, **ElectroAir**, **FCX Systems**, **Ingeteam**, **Hitachi Energy ACS6080-SFC** ("pre-fabricated, pre-tested, minimum time on site"), **NIDEC ASI** [RT-V05-06..10,12]. Vessel-side: **Cavotec PowerFit** 40-ft containerized HVSC retrofit, USD 5M multi-unit order (Evergreen/Seaspan/Capital) [RT-V05-11]. China: **青岛创统 Qingdao Chuangtong** — lead drafter of GB/T 25316, CCS-certified, ~300 units at major ports [RT-V05-13]; plus **江门安利** SVF and **山东精久** JJCY catalog lines [RT-V05-14/15]. China procurement flows through MOT + State Grid/CSG action-plan channels [RT-V05-21] — de facto domestic-locked against a US-flag startup.

## 4. Engineering reality check

At 50/60 Hz output, volume/mass are set by the isolation transformer and LC output filter, not switch technology — 2–3x "power density" from GaN-SiC is mostly unharvestable, and 650 V GaN cannot natively serve 690 Vac anyway (multilevel gymnastics or SiC-only, like everyone else). Density is not the binding constraint on a quay; cost/kW, IEC/IEEE 80005 compliance, grid code, and tender terms are. "Days-not-months install" is already Hitachi/PowerCon's shipping pitch. Benchmarking against RMB 800k/MW is a category error: that figure is the Chinese *vessel-side retrofit* cost — no US GaN-SiC BOM undercuts Chuangtong's cost base.

## 5. Willingness-to-pay skepticism

The 17%-utilization gap is a *tariff* problem, not hardware: two-part pricing pushes effective shore power to ~6.9 CNY/kWh (Shanghai) / 3.56 (Shenzhen) vs. cheaper aux-engine fuel [RT-V05-16/17]; China's fix is policy (capacity-charge exemption end-2025 [RT-V05-18]). A converter changes none of that math. EU vessel-side WTP is penalty-backed (FuelEU: EUR 1.5 × power demand × non-compliant hours from 2030) but only for container/passenger ships >5000 GT — exactly the ships served by incumbent HV berths, not V05's compact tier [RT-V05-19]. Tugs/bulkers/river craft — the compact segment — face no penalty and hold no budget.

## 6. Founder-fit doubts (not PhD-lane, still overscored)

Winning here means BOM cost engineering, 80005/class certification management, and public-tender navigation — none of the founder's extreme-edge capabilities (density, kHz+ FPGA control, harsh-env packaging) is monetized at 50/60 Hz quay duty. "Any competent power-electronics team could do it" — and a dozen already do.

## 7. Score adjustments (±1, reasons)

| C | Raw→Adj | Reason |
|---|---|---|
| 1 | 4→3 | Commodity conversion; capability graph unused |
| 2 | 3→2 | Density claim unharvestable at 50/60 Hz; no 10x |
| 3 | 4→3 | AFIR buyers already contracting incumbents 2026–28 |
| 4 | 4→3 | Expansion plank collides with C04-adjacent MCS space |
| 5 | 5→4 | 2029 launch lands after the procurement crunch |
| 6 | 5→5 | Genuinely buildable (that's the problem) |
| 7 | 3→2 | Middle tier occupied by ~12 named vendors |
| 8 | 4→3 | China tender channel domestic-locked; US tier served |
| 9 | 5→4 | Regulation routes demand into incumbent-favoring public tenders |
| 10 | 5→4 | MVA marine/grid-code type tests + slow port sales cycles |
| 11 | 5→5 | Standalone value real |

**Adjusted total: 66.0** (was 83.2; −17.2 — worst-in-class stress delta).

## 8. Steelman

The pain is real somewhere: Shanghai logged an 18% connection-failure rate in 2023 from voltage mismatch, and MOT Order 2025 No.2 makes compliance/utilization disclosure mandatory — a software-led universal-adapter + billing/compliance instrumentation play into Chinese port groups could work as a niche. Small non-TEN-T ports may eventually want sub-MVA catalog boxes the EPC giants ignore. But that is a services/software thesis, not the scored hardware thesis.

**Recommendation: KILL (market-crowding, not novelty). Kill-probability 85%. Do not advance to deep dive; pull a reserve seed.**
