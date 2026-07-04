# PHASE 3 — SELECTION: Deep-Dive Slate (top 5 of 15)

## Post-red-team standings (all 15 red-teamed; adjustments per REDTEAM_Vxx.md)

| Rank | ID | Candidate | Raw | RT-adj | Δ | Kill% | Novelty verdict |
|---|---|---|---|---|---|---|---|
| 1 | V09 | Field-hardened White-Rabbit timing appliance | 86.8 | **74.0** | −12.8 | 65% | NOVEL |
| 2 | V01 | WBG plasma-torch retrofit PSU + arc control | 85.2 | **73.2** | −12.0 | 70% | NOVEL |
| 3 | V11 | Robotic magnet-harvesting disassembly cell | 86.8 | **72.0** | −14.8 | 60% | NOVEL |
| 4 | V12 | Heavy-REE magnetic-signature triage sensor (PhD-lane) | 83.2 | **70.8** | −12.4 | 75% | NOVEL |
| 5 | V08 | FSM drive + tracking controller card | 81.6 | **69.6** | −12.0 | 70% | NOVEL |
| 6 | V02 | Pulsed-arc PFAS destruction skid | 82.0 | 68.4 | −13.6 | 75% | NOVEL |
| 7= | V03 | Thermal-battery discharge power stage | 81.2 | 67.6 | −13.6 | 85% | **VARIANT — G7-NOVEL FAIL → reserve** |
| 7= | V13 | Bolt-on weld-QC sensor head | 79.6 | 67.6 | −12.0 | 80% | NOVEL |
| 9 | V04 | MV >1000 °C resistive kiln controller | 79.6 | 66.8 | −12.8 | 75% | NOVEL |
| 10= | V07 | Laser-power-beaming receiver module | 84.4 | 66.4 | −18.0 | 80% | NOVEL |
| 10= | V10 | Real-time QEC decoder appliance | 80.4 | 66.4 | −14.0 | 85% | NOVEL |
| 12 | V05 | Berthed-load shore-tie converter | 83.2 | 66.0 | −17.2 | 85% | NOVEL |
| 13 | V15 | RTG battery-buffer retrofit kit | 76.0 | 60.0 | −16.0 | 90% | NOVEL |
| 14= | V06 | PTO-to-grid conversion module | 74.0 | 58.8 | −15.2 | 90% | NOVEL |
| 14= | V14 | Trolley-assist retrofit interface | 76.8 | 58.8 | −18.0 | 90% | NOVEL |

Mean red-team adjustment: **−13.9 points** (steeper than Round 1's −7.0 — the 2026 evidence
base closes whitespaces fast; the modal kill remains "the product already ships": Konecranes
multi-brand RTG retrofits, BluVein, NVQLink decoders, PowerLight receivers, Precitec/OCT weld
monitors, PowerCon shore converters, Chromalox MV controllers).

## Selected for deep dives (waves of 3 then 2)

**Wave 1: V09, V01, V11 · Wave 2: V12, V08**

Selection rule: straight top-5 by RT-adjusted score; no diversity override needed.

Diversity confirmation: 4/5 standalone products (80% ≥50% ✓); 1/5 instrument (V12; portfolio
instrument count 2 ≤3 ✓); 1/5 PhD-lane (V12, ≤2 ✓; carries anti-anchoring note into the deep
dive); lanes G06/G02/G07/G07/G05 — G07 appears twice but V11 (capital equipment for
disassembly) and V12 (routing instrument) have different buyers-stage and product categories;
0 HTS ✓; no Magnefy conflict ✓; V03 (VARIANT) excluded from selection per G7 rule.

Rationale notes:
- **V09**: highest surviving score; red team found hardened-WR prior art (LHAASO, WR
  Collaboration roadmap) but left a real question — whether a telecom-grade productized node
  for unattended quantum/VLBI infrastructure is a business or a Safran feature. Deep dive
  must resolve buyer count and the Safran/GMV/OPNT timeline.
- **V01**: plasma is a user-named sector and this is its strongest expression; deep dive must
  test whether ANY reachable buyer pool exists outside SOE self-supply (Western waste
  operators, torch OEM partnerships, Belt-and-Road channel) and whether the PSU can win as
  retrofit vs PyroGenesis turnkey.
- **V11**: lowest kill probability (60%) of the slate; the HPMS-doesn't-need-disassembly
  objection is the load-bearing question — deep dive must map which recycling routes DO pay
  for intact extraction (reuse/short-loop, Noveon-style) and whether Molg's traction proves or
  crowds the category.
- **V12**: PhD-lane candidate; red team's Dy-coercivity physics objection gutted the headline
  claim — deep dive must either find a physically honest re-scope (alloy-family + magnetized-
  state triage, applied-field probing add-on) with real WTP, or confirm the kill. C33
  precedent: Round-1 deep dives overturned red-team physics/patent claims twice.
- **V08**: cheapest v1, strongest founder-fit; deep dive must test whether merchant tracking
  electronics can win sockets against Cedrat/PI OEM boards and in-house prime IP, and size the
  honest TAM (instrument-scale?).

Not selected (reasons): V02 premise weakened by EPA slip + wrong-bottleneck physics; V13
whitespace premise false (OCT incumbents); V04 whitespace occupied (Chromalox/Yingjie); V07
receiver slot foreclosed (PowerLight/Teravec) + claim self-contradiction; V10 NVQLink closed
the category; V05 crowded 12-vendor field + non-hardware root cause; V15/V06/V14 premise-level
kills (whitespace closed 2024-2026). V03 G7-fail. All remain in the merged ranking with
RT-adj − 8.9e expected scores.
