# RED TEAM — V06 Qualified PTO-to-grid conversion module for wave/tidal OEMs

Verdict up front: **NOVEL / KILL-RECOMMEND (on merits, not gate). Kill probability 90%.**
Sources: `30_SCORING/REDTEAM_V06_sources.json` (RT-V06-01…16).

## 1. Novelty verification (G7-NOVEL)
Three nearest ledger neighbors: (1) **N04** subsea inductive power/docking — power INTO resident
AUV/ROV via couplers; V06 is harvest-to-grid conversion. Different direction, buyer, category.
Clean. (2) **C01/C03** MW SiC marine power bricks / marine inverters — the real neighbor. Same
hardware class (marine-hardened AC-DC-AC PEBB); V06 survives only on buyer segment (WEC/tidal
OEMs, grid-interconnect duty) vs. propulsion integrators. Bluntly: a marine power brick pointed
at the grid — declaration holds, but on buyer, not physics. (3) **C10** (magnet/science
converters) and **C38/RID-019/PWR-15** (GFM PCS/controls for compute/LDES) — GFL/GFM content
overlaps, buyers/environments materially differ. **Verdict: NOVEL, gate passes.** Not a disguised
duplicate; it dies on the market instead.

## 2. Strongest bear case
The merchant TAM is ~$5M/yr and the solvent buyers signed away their conversion sockets in
2024–25, before this company could exist. Named 2027–2030 pipeline: MeyGen 2 — 28 MW CfD, 2027
target [RT-V06-04] — locked via the Nov-2024 Proteus/SKF/**GE Vernova** MOU in which GE Vernova
Power Conversion explicitly takes "power conversion from generator to grid" for ≥59 MW
[RT-V06-03]. CorPower (15 MW of arrays) — locked to **Equipmake** under a multi-year April-2025
development agreement [RT-V06-01], phase 1 priced at **£650K** [RT-V06-02] — the revealed value
of the sector leader's entire conversion program. Orbital — SKF integrated powertrains
[RT-V06-05]. Carnegie CETO — PTO assembled at SKF [RT-V06-06]. Nova — in-house direct drive.
PacWave 2026–30 is single devices (CalWave x200 = 200 kW) [RT-V06-15]. Generous math: ~100 MW
cumulative at $100–250/kW conversion content = $10–25M over four years, >80% pre-allocated.
Remainder: low-single-digit modules/yr.

## 3. Hidden competition (missed by the one-pager)
**GE Vernova Power Conversion** (ex-Converteam; also built OpenHydro's subsea converter),
**SKF** (occupying the "qualified integrated PTO" slot at Orbital, Carnegie, Proteus), **Ingeteam**
(offshore converter range to 18 MW, marine-proven [RT-V06-13]), **Yaskawa/The Switch** (catalog
MW-class PM-generator + full-power converter packages for marine OEMs [RT-V06-14]), and the
EU-funded **MEGA PTO WAVE** consortium building exactly "modular power electronics" for WECs with
grant money [RT-V06-07]. China: LHD Zhoushan is fully self-developed (自主研发), 4th-gen 1.6 MW,
LCOE driven 106→1.1 CNY/kWh — a closed domestic SOE chain with zero import slot [RT-V06-12].

## 4. Engineering reality check (crest-factor claim)
5–10x peak-to-average is real for point-absorber WECs — but a module "handling" it must rate
silicon, magnetics, and cooling at PEAK, so a "250 kW" module is a ~1–2 MW-peak converter sold at
average-power price. Smoothing 8–12 s wave periods across a 5:1 swing needs MJ-class buffering
(supercap/battery hybrid), not DC-link caps. Leaders already solve crest factor upstream —
CorPower mechanically (WaveSpring), hydraulics via accumulators — and wave-by-wave force/MPPT
control IS the OEM's crown-jewel IP; they will buy silicon, never the control loop. Tidal, the
only revenue-grade sub-sector, is smooth — no crest-factor problem — which is precisely why
GE/Ingeteam/The Switch serve it from wind-class catalogs. The extreme edge exists only where the
market doesn't, and four PTO architectures (linear, hydraulic, air-turbine, rotary) defeat the
"one catalog module" premise.

## 5. Willingness-to-pay skepticism
No OEM has publicly asked for a merchant module; WTP is grant-cycle money (TEAMER $6.3M across
39 projects; EU funds) spent with bankable nameplates — a £200M EPC's lenders want GE/SKF/ABB,
not a seed startup. Buyer solvency is the sector's defining datum: Pelamis (2014, £15M debts,
assets £836K) [RT-V06-11], Aquamarine (2015), OpenHydro (2018), Wello (2023) [RT-V06-10],
Sustainable Marine (2023, killed by permitting) [RT-V06-08], Sabella (liquidated Jan 2024)
[RT-V06-09]. Customers die faster than a marine sales cycle. UL 1741 SB/IEEE 1547.1 NRTL +
IEC 62600 + class approval per SKU [RT-V06-16] is routine amortized over 10^4 solar units,
fatal over ~10.

## 6. Founder-fit doubts
Not PhD-lane. But CorPower chose Equipmake — an automotive electrification shop — proving generic
power-conversion competence is abundant; the scarce assets are class-society/grid-code
certification experience and a balance sheet, which the founder lacks. No ocean-engineering or
DNV track record.

## 7. Score adjustments (raw 74.0)
- C1 4→3: conversion skill generic (Equipmake precedent); zero marine-cert domain. C2 4→3:
  crest-factor solved upstream/mechanically; absent in tidal. C3 3→2: buyers locked or insolvent;
  TAM <$10M/yr. C4 3→3 (0). C5 4→3: conversion sockets awarded 2024–25 — window closed pre-2029.
  C6 4→4 (0). C7 4→3: GE Vernova/SKF/Ingeteam/Yaskawa + EU-funded modular-PTO consortium. C8 3→2:
  LHD chain closed; US = grant demos. C9 4→3: triple certification burden on tiny volume. C10 4→3:
  EMEC/PacWave qualification slots grant-gated, slow. C11 4→4 (0).
- **Adjusted: C1=3,C2=3,C3=2,C4=3,C5=3,C6=4,C7=3,C8=2,C9=3,C10=3,C11=4 → 294/5 = 58.8**
  (−15.2; showdown convention 58.8 − 8.9 = 49.9e).

## 8. Steelman
If wave energy reaches true array scale in the 2030s, the first EMEC/PacWave-qualified merchant
module becomes the sector standard for the ~30-developer long tail that cannot afford
Equipmake-style bespoke programs, with TEAMER/EU grants paying the entire qualification bill.
MeyGen's £178.54/MWh CfD gives tidal revenue-grade economics for the first time, and a
crest-factor-rated buffer-converter genuinely does not exist as a catalog SKU. If that thesis is
right, V06 is early, not wrong — but "early" against six customer bankruptcies is the same trade.

**RETURN: V06 · kill-probability 90% · biggest objection: merchant conversion TAM ≈$3–6M/yr with
every solvent volume buyer (MeyGen→GE Vernova, CorPower→Equipmake, Orbital/Carnegie→SKF,
Nova→in-house) already contractually locked in 2024–25 · novelty verdict: NOVEL.**
