# RED TEAM — V01: WBG retrofit PSU + closed-loop arc control for industrial plasma torches

Reviewer stance: kill it if possible. Sources: `REDTEAM_V01_sources.json` (RT-V01-01..20).

## 1. Novelty verification (G7-NOVEL)

Three nearest ledger neighbors: **N08** (industrial pulsed power/PEF), **C10** (precision magnet/scientific converters), **C39** (electrolyzer power modules); also checked **N05** (RF/microwave process heat) and **C35/N02** (accelerator RF). N08: pulsed-field food/materials processing — different waveform regime (pulse vs continuous negative-resistance arc), different buyer. C10: ppm-class static precision for physics facilities — different spec axis and buyer. C39 is the truest neighbor the declaration omitted: both are "industrial MW DC rectifier re-aimed at a new load"; but electrolyzers are quasi-static loads, arcs are dynamic negative-resistance loads needing kHz-class control — product function and buyer (waste/metallurgy operators) both differ. N05/C35: different physical mechanism entirely. No ledger entry covers plasma-torch power. **Verdict: NOVEL — narrowly.** It is a new lane, not a disguised duplicate, but it sits in the same capability family as C10/C39; the novelty is the application, not the converter.

## 2. Strongest bear case

The addressable retrofit pool barely exists. West: the legacy installed base V01 targets is tiny and broke — Europlasma trades at ~$1.4M market cap on >99%-dilution OCABSA financing (RT-V01-18/19); Tees Valley/Plasco class plants are dead, so there are perhaps dozens of operating MW waste torches worth retrofitting. China: the growing base is vertically integrated SOE/institute programs — CGN (~40-patent plasma cluster, Qingyuan demo, RT-V01-13), SWIP industrialization (RT-V01-14), Yantai Longyuan (RT-V01-11/12), Tianying (RT-V01-20) — which build their own torches AND supplies under 自主可控 procurement. The one healthy Western torch OEM, PyroGenesis, already ships turnkey systems with its own patented IGBT power circuits (RT-V01-03/04/05). Squeezed on all three sides, V01 dies by 2031 with two pilots and no repeat buyer.

## 3. Hidden competition the one-pager missed

- **PyroGenesis** (RT-V01-01..05): 5 torch lines, 200 kW–2 MW APT-HP, 4.5 MW delivered 2025; granted IGBT torch-PSU patents US9,950,387 and US12,471,260. A plasma-torch company that IS a power-supply company.
- **Westinghouse Plasma** (RT-V01-06): WPCT540 runs two supplies with independently controlled arc and field-coil currents — closed-loop arc management already shipping.
- **烟台龙源 Yantai Longyuan** (RT-V01-11/12): plasma ignition industrialized since ~2004 (national S&T prize), modular DC switching PSUs, thousands of boiler units; Jan 2026 won China's first ship-based plasma solid-waste project.
- **中广核 CGN / 核西物院 SWIP / 江苏天楹** (RT-V01-13/14/20): vertically integrated Chinese plasma-waste suppliers.
- **Merchant PSUs**: Magna-Power ML 500 kW–1 MW catalog DC, scalable 10 MW (RT-V01-15); Injet 英杰电气 already sells plasma supplies (RT-V01-16); Advanced Energy (RT-V01-17).

## 4. Physics reality check

Closed-loop arc control is not novel: erosion-control PSUs are 1987/1995 prior art (RT-V01-07/08); Westinghouse ships dual-loop control. Electrode erosion is dominated by arc-current magnitude, arc-root attachment mode/residence time, gas chemistry, and electrode material/cooling (RT-V01-10) — torch-side variables. PSU-controllable levers (ripple zeros/peaks, soft start/stop, restrike detection) are real (RT-V01-09) but second-order: credible gain ~1.2–2x on worn thyristor plants, not 2–5x, without torch-head co-design — which makes you a torch OEM. The 20–30% energy-per-tonne cut is worse: thyristor rectifiers already run ~95% efficient; SiC buys ~3–4 points of conversion. Any bigger number is process-coupling speculation, unproven.

## 5. Market/WTP skepticism

Nobody quoted actually says they'd pay $150–600K for a PSU alone; the CNY 50M/3-yr-payback datum (G02-18) is for whole plants, sold by the institute that builds them. Proving electrode-life ROI against a 1,000–1,500 h baseline takes months of continuous burn per data point — sales cycles beyond seed runway. And a 100 kW–2 MW arc test facility must be rented from... a competitor.

## 6. Founder fit

Conversion + FPGA match is real, but zero torch/furnace process experience, no hazardous-waste site credibility, and every natural channel partner (torch OEM) is a rival selling its own PSU. C1=5 was anchored on component-level match, ignoring channel/domain.

## 7. Score adjustments (raw 85.2)

| Crit | Raw→Adj | Reason |
|---|---|---|
| C1 | 5→4 | Domain/channel gap: torch OEMs are rivals, no MW arc test access (−2.8) |
| C2 | 4→3 | 2–5x life and 20–30% energy not PSU-attributable; credible edge 1.2–2x (−2.4) |
| C3 | 4→3 | Western buyers few/distressed; Chinese buyers vertically integrated (−2.4) |
| C7 | 4→3 | PyroGenesis IGBT patents + Westinghouse dual-loop + Magna-Power catalog (−1.6) |
| C8 | 5→4 | China channel implausible into SOE/institute self-supply (−1.6) |
| C10 | 4→3 | Months-long life-proof trials delay revenue (−1.2) |

**Adjusted total: 73.2** (showdown comparability: 64.3e).

## 8. Steelman

The wedge is not distressed Western retrofits but new-build bolt-on plasma stages and plasma-metallurgy pilots (Ti powder, H2-plasma) where torch and PSU are procured separately and no merchant supplier offers arc-dynamics software; PyroGenesis's own IGBT patents prove the PSU is where value concentrates. Even a demonstrated 1.5x electrode life plus a few points of energy on availability-critical lines can clear a $300K ASP. If one credible torch partner outside the OEM oligopoly signs, the squeeze argument weakens materially.

---
**Candidate:** V01 · **Kill-probability: 70%** · **Biggest objection:** no reachable buyer pool — West is tiny/insolvent, China is vertically integrated SOE self-supply, and the healthy torch OEM already bundles patented modern PSUs · **Novelty verdict: NOVEL** (narrowly; application-level, not converter-level)
