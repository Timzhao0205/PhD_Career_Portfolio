# RED TEAM — V02 Containerized pulsed-arc PFAS destruction skid (lane G02)

Date 2026-07-03 · Raw 82.0 · Sources: `REDTEAM_V02_sources.json` (RT-V02-01..25)

## 1. Novelty verification (G7-NOVEL)

Three nearest ledger neighbors: **N08** (industrial pulsed power / PEF), **C36** (GaN medical
ablation OEM), **CL-25** (energy-based intervention engines: PFA/histotripsy/FUS). C36/CL-25 are
tissue-intervention generators — different physics target, buyer, and regulatory universe; no
overlap beyond "energy engine." N08 is the real test: V02 is unambiguously "industrial pulsed
power," but N08's gist is pulsed-electric-field food/extraction processing — electroporation,
food-plant buyers. V02 sells a plasma-discharge destruction skid + compliance software to
water-utility/DoD environmental buyers. Different buyer segment, product category, and mechanism
(discharge chemistry vs. electroporation). **Verdict: NOVEL** — but note the capability thesis
("our pulsed PSU is the moat") is the same one the Round-1 saturation report already retired
with N08; the novelty is real, the moat logic is recycled.

## 2. Strongest bear case

The demand clock the one-pager scored on has already slipped. The "spring-2026 final extension
rule" did not land as final: on 2026-05-18 EPA issued *proposals* to (a) rescind MCLs for
PFHxS/PFNA/GenX/PFBS — 4 of 6 regulated compounds — and (b) extend PFOA/PFOS compliance from
2029 to an opt-in 2031 (comments close 2026-07-20; final intended late 2026, litigation certain)
[RT-V02-01..05]. By 2031 the residual PFOA/PFOS market is served by GAC/IX removal plus
haul-away disposal; destruction stays a discretionary polishing purchase in a field where SCWO
(Revive at 160k gal/day >99.99% [RT-V02-12]; 374Water/GA/Arcadis in DoD full-scale demos
[RT-V02-07]), HALT (Aquagga), electro-oxidation (Aclarity $15.9M, Oxyle $16M, Gradiant
ForeverGone at Munich Airport [RT-V02-14..17]) are all further along — and plasma's own DoD slot
is already Onvector's (AFWERX Phase II + STRATFI + Phase III OT, 2x ESTCP) [RT-V02-09,10]. A
2029-launch power-electronics entrant arrives fifth to a knife fight that may have no umpire.

## 3. Hidden competition the one-pager missed

- **Gradiant "ForeverGone"** — unicorn-scale; integrated foam fractionation + electro-oxidation
  (concentrates AND destroys); claims 100x Destruction-Engine footprint cut; AFFF deployment at
  Munich Airport [RT-V02-17]. Occupies exactly V02's "polishing after concentration" slot.
- **Revive Environmental/Battelle, 374Water, General Atomics iSCWO, Aquagga** — the four teams in
  DoD's flagship large-scale destruction demos [RT-V02-07]; plasma not in that lineup.
- **Merchant pulsed-power vendors**: Eagle Harbor Technologies (lists water treatment) and
  Transient Plasma Systems sell precision ns-pulsed supplies today [RT-V02-23,24] — DMAX/Onvector
  can buy the claimed differentiator.
- **China**: no commercial plasma-PFAS vendor surfaced (consistent with one-pager), but USTC's
  Nature-published 40–60 °C catalytic total defluorination [RT-V02-25] is a substitution threat.

## 4. Physics reality check

Plasma PFAS destruction is interface-limited: PFAS are surfactants that concentrate at
gas–liquid interfaces; rate scales with interfacial area, bubbling, and reactor geometry
— the 2025 plasma-liquid review names reactor design/mass transfer, not electrical delivery,
as the critical limiter [RT-V02-18..20]. Published energy-per-volume spans 20–330 kWh/m³
*across reactor architectures* [RT-V02-19]. Adaptive impedance matching buys tens of percent in
coupled power, not the claimed 2–4x destruction throughput per kW. The extreme-edge claim
attacks the wrong bottleneck.

## 5. Market WTP skepticism

Utilities are mandated to *comply* (remove), not to *destroy*; spent media is overwhelmingly
hauled to incineration/landfill. The cleanest WTP datum: 374Water, a NASDAQ-listed SCWO pure
play, booked $215K FY2025 revenue (−52% YoY) and ran cash to $0.9M [RT-V02-13]. DoD money is
real but demo-gated and CERCLA-slow (PA/SI 1–3 yrs; AFFF waiver pushed to Oct 2026)
[RT-V02-21,22]. $300K–1M capital skids also fight a service-model market (Revive/Gradiant sell
destruction-as-a-service).

## 6. Founder-fit doubts

Not PhD-lane, but the fit is capability-projected, not buyer-verified: zero water/wastewater
domain history, no municipal procurement or consulting-engineer (Arcadis/CDM) channel, no
analytical-chemistry capability for the LC-MS/MS destruction-verification and byproduct (HF,
short-chain) work that closes every sale. C1=4 was generous.

## 7. Score adjustments (±1, reasons)

| C | Raw→Adj | Reason |
|---|---------|--------|
| C1 | 4→3 | No water-domain credibility or channel; chemistry validation gap |
| C2 | 4→3 | PSU edge misaligned with mass-transfer bottleneck; merchant pulsed PSUs purchasable |
| C3 | 5→4 | Funded DoD slots occupied (Onvector); utility destruction demand discretionary |
| C4 | 4 | Leachate/fab expansion real — unchanged |
| C5 | 5→4 | Deadline 2029→2031 opt-in; 4/6 MCLs proposed rescinded; driver diluted + litigated |
| C6 | 4 | Skid is buildable — unchanged |
| C7 | 3→2 | Field worse than scored: Gradiant + electro-ox wave + SCWO commercial execution |
| C8 | 3 | Unchanged (US-only demand, China watch) |
| C9 | 4→3 | Entire beachhead rests on a rule being partially rescinded — fragility, not robustness |
| C10 | 4→3 | 3–5 yr municipal/DoD cycles; 374Water burn is the object lesson |
| C11 | 5 | Genuinely standalone — unchanged |

**Adjusted total: 68.4** (raw 82.0, −13.6).

## 8. Steelman

If PFOA/PFOS MCLs survive (EPA says they will) plus CERCLA liability, thousands of utilities
must handle PFAS-laden concentrate somewhere, and incineration keeps losing social license —
destruction demand then compounds through the 2030s. Plasma is the only non-pressurized,
ambient-condition destruction route, and every incumbent plasma player is chemistry-led with
weak power engineering; a reliability-first skid could win on uptime economics where pilots die
today. The founder could also de-risk by selling the pulsed-PSU layer to all plasma/electro-ox
players (V01-pattern) instead of the skid.

**Recommendation: KILL (fails on moat + timing, not on gates). G7-NOVEL: pass.**
