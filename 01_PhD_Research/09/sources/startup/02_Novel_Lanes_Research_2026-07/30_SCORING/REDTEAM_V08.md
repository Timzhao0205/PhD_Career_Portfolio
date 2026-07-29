# RED TEAM — V08 Catalog SWaP-optimized FSM drive + tracking controller card

Date 2026-07-03 · Raw 81.6 · Sources: 30_SCORING/REDTEAM_V08_sources.json (RT-V08-01..14)

## 1. Novelty verification (G7-NOVEL)
Three nearest ledger neighbors: **RID-111** (high-bandwidth piezo nanopositioning actuator),
**C25** (D2W overlay inspection), **CL-09/SEM-06** (CPO fiber-attach assembly cells). C25 and
CL-09/SEM-06 are wafer-level tools — genuinely unrelated. RID-111 is the real neighbor: V08 is
the *electronics half* of RID-111's product space (piezo/VCM actuator vendors always ship
drivers). But the deliverable (FPGA controller card + PAT firmware, no actuator), the buyer
(FSO/directed-energy integrators, not nanopositioning users), and the category differ. Not a
re-parameterization. **Verdict: NOVEL — G7 pass**, with the caveat that RID-111's incumbents
(PI, Cedrat, nPoint) are exactly V08's competitors.

## 2. Strongest bear case
The merchant slot does not exist in the customer's architecture. From below, mirror vendors
already bundle catalog electronics: Cedrat sells the **CCBu20/CCBu40 embedded OEM controller
and a flight-ready CCBu20-NS**, plus demo kits [RT-V08-01, -02] — the one-pager's "Cedrat sells
bespoke, price-on-request" premise is factually wrong at the electronics layer. PI's **E-727**
is explicitly marketed for FSM in free-space optical comms and high-speed tracking [RT-V08-03].
Optotune ships VCM FSMs with **OEM driver boards + reference design**, catalog-priced through
Edmund Optics [RT-V08-04, -05]; Mirrorcle sells MEMS mirrors with PicoAmp OEM drivers and cheap
dev kits — already serving the SWaP-critical small-aperture tier [RT-V08-06, -07]. From above,
terminal primes hold the tracking loop as core IP: Mynaric builds CONDOR electronics in-house
in Hawthorne [RT-V08-09]; CACI's CrossBeam and Tesat's ConLCT80 integrate fine tracking/
beaconless PAT inside the terminal [RT-V08-14]; FSO Instruments (Demcon/VDL/TNO) is
commercializing the merchant FSM itself [RT-V08-08]. V08 is squeezed to the sliver of buyers
sophisticated enough to build a terminal yet willing to outsource its highest-value loop.

## 3. Hidden competition
Named: Cedrat (CCBu20-NS), PI (E-727/E-616), Optotune, Mirrorcle, nPoint, Optics In Motion,
Optical Physics Co., Kaman, GD Mission Systems, L3Harris, Ball [RT-V08-13]; FSO Instruments
[RT-V08-08]. China: CAS institutes (IOE/Changchun lineage) dominate FSM/ATP research
[RT-V08-11]; Tongmao (同茂电机) sells VCM FSM structures domestically [RT-V08-12] — China is
building its own supply, and US export rules gut the sell-to-China angle anyway (tracking/
beam-steering electronics sit on the ECCN 6A004 / USML Cat XII boundary [RT-V08-10]).

## 4. Engineering reality check
The cited gap [G05-08] — nothing spans galvo speed, micro-gimbal compactness, piezo zero-power
holding — is **actuator physics, not electronics**. A controller card cannot give a voice-coil
mirror zero-power holding or a piezo mirror galvo range; V08 repackages a mirror trilemma as a
card product without building the mirror. "Mirror-agnostic" control is also oversold: closed-
loop bandwidth is set by mechanism resonances; notch/compensator tuning, sensor conditioning
(SG vs capacitive vs optical), and HV piezo drive (C·V²·f — kHz drive of large piezo stacks
draws tens–hundreds of watts; E-727 peaks at 270 W) are per-mirror engineering. The <10 W claim
only holds for small mirrors — the tier Mirrorcle/Optotune already serve. A universal card
either underperforms co-designed stacks or becomes per-program NRE, i.e., Cedrat's bespoke model
with less heritage.

## 5. Willingness-to-pay skepticism
$15–60K/card sits above the whole reference class (E-727 ~$10–15K street; Optotune/Mirrorcle
drivers $1–5K class). No named buyer testimony exists for a merchant PAT card; the Navy SBIR
[G05-18] is a funding channel, not proof of a product market. Market sizing spans $0.5B–$12B
across report mills [RT-V08-13] — i.e., unknown, likely instrument-niche at the merchant layer.

## 6. Founder-fit doubts
Not PhD-lane. FPGA control + precision electromechanics is real leverage, but zero optics/
space/defense pedigree in a heritage-gated procurement culture; the winding machine is not a
turbulence-tracking loop with quad-cell sensing. C1=5 overstated.

## 7. Score adjustments (±1, reasons)
| Crit | Raw→Adj | Reason |
|---|---|---|
| C1 | 5→4 | Capability transfers; no optics/space heritage where pedigree gates sales (−2.8) |
| C2 | 4→3 | "Catalog vs bespoke" is procurement friction, not physics; SWaP claim breaks at HV piezo drive (−2.4) |
| C3 | 4→3 | Beachhead primes internalize PAT; no validated merchant WTP (−2.4) |
| C7 | 3→2 | CCBu20-NS, E-727, Optotune/Mirrorcle OEM drivers occupy whitespace from both ends (−1.6) |
| C8 | 3→2 | China sale ≈ license-denial territory (6A004/Cat XII); US-only halves the story (−1.6) |
| C10 | 5→4 | Aerospace/defense design-in cycles 18–36 mo; card BOM ≠ fast revenue (−1.2) |

**Adjusted total: 81.6 − 12.0 = 69.6** (showdown convention: 69.6 − 8.9 = 60.7e).

## 8. Steelman
No existing product combines mirror-agnostic drive, integrated PAT firmware, quaternion
feed-forward, and published tracking specs in one drone-class card — Cedrat/PI drive their own
mirrors and leave the tracking loop to the customer. If proliferated-LEO ground segments and
drone FSO scale 2027–2030, dozens of second-tier integrators without controls teams need
exactly this socket, and one design win (SBIR-funded, ITAR-clean US line) compounds into a
sticky standard.

## Verdict
Kill-probability **70%**. Novelty **NOVEL** (G7 pass). Biggest objection: the "missing merchant
electronics layer" already exists from below (Cedrat CCBu20-NS, PI E-727, Optotune/Mirrorcle OEM
drivers) while primes keep PAT in-house — and the cited performance gap is actuator physics a
card cannot fix, leaving per-mirror NRE services at instrument-niche scale.
