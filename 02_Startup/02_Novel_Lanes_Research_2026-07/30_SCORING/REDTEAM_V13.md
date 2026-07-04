# RED TEAM — V13: Bolt-on multi-modal weld-QC sensor head for battery module/pack lines

Reviewer stance: kill it if possible. Sources: `REDTEAM_V13_sources.json` (RT-V13-01..21). Raw 79.6.

## 1. Novelty verification (G7-NOVEL)

Nearest ledger neighbors. **IND-08** (silver-sinter die-attach cell, inline void metrology): power-module packaging cell for die-attach — different process, product (cell vs. sensor head), buyer. **CL-13** (battery/solid-state manufacturing lines, dry-electrode/sulfide film): V13 never touches cell/electrode processes; it inspects finished interconnect welds. **C22** (PD/insulation EOL rigs): insulation, not welds. **C30** (fast current sensors): component sensing, unrelated. Swept further: **IND-10** (on-machine adaptive-metrology retrofit — machine tools, dimensional compensation), **CL-16** (precision-mfg in-process QC cells — generic cells, not battery-weld heads), **C40/RID-016** (second-life grading — untouched). No re-parameterization found. **Verdict: NOVEL vs. the ledger.** But as with V10, the one-pager's whitespace premise ("nobody sells this un-bundled" [G01-10]) fails verification below — G7 passes; the market claim does not.

## 2. Strongest bear case

The un-bundled retrofit weld-QC category already exists and is crowded from three directions. (1) Merchant monitoring vendors: Precitec's LWM is battery-specific (foil-to-tab, cap-to-can, cell-to-busbar), AI-classified — predicting weld strength AND electrical conductivity — and explicitly "adapted retroactively to already existing laser systems or... foreign processing heads" [RT-V13-01/02/03]; plasmo (nLIGHT) processobserver + plasmoeye deep learning targets battery welding at 250 kHz [RT-V13-06/07]; 4D WeldWatcher and VITRONIC advertise line-agnostic retrofit [RT-V13-18/19]; Xiris holds weld vision [RT-V13-21]. (2) OCT depth measurement is the standard answer on battery welds: IPG LDD-700 measures actual keyhole depth in-process, replacing destructive testing [RT-V13-04/05]; Trumpf VisionLine OCT Check names busbar welding in battery production [RT-V13-08/09]; Lessmueller closes the loop on busbar depth [RT-V13-10]. (3) Chinese welder OEMs bundle it at the source: United Winners' RWD FD-OCT real-time depth detection was certified "international leading" Dec 2024 (25 patents, 3 standards) [RT-V13-11]; Hymson PACK lines ship online depth detection closed-loop [RT-V13-12]; Han's Laser lines carry CCD NG-judgment at every station plus hipot test [RT-V13-13]. V13 arrives 2027 selling inference where incumbents sell measurement.

## 3. Hidden competition missed

Beyond the above: **Therness** (Turin, EU-co-financed) — thermal-AI tab/busbar weld monitoring, "100% inline QA" [RT-V13-16]; **EVident Battery** ($3.2M seed Apr 2025) — 2-minute NDT pack inspection [RT-V13-17]; **Hioki** documents 4-wire weld contact-resistance checking of tab/busbar joints as standard cheap post-weld practice [RT-V13-14/15]; multi-sensor fusion (spectrum+vision predicting strength and resistance) is already published academic method, not proprietary IP [RT-V13-20]; eddy-current weld NDT is commodity instrumentation (Foerster/Eddysun class).

## 4. Engineering reality check

Is plume+vision+eddy fusion additive over OCT? Mostly no. OCT measures penetration depth — the actual spec — geometrically; V13 fuses three indirect proxies to infer it. Off-axis modalities a third party can bolt on cannot see the keyhole; the high-value coaxial path requires welder-OEM optical integration V13 doesn't control. Eddy current on Al/Cu dissimilar welds confounds lift-off, texture, and intermetallics — research-grade inline, not solved. The >99.7%/<2% target extrapolates from one 1,268-image academic baseline [G01-04]; validation requires destructive ground-truth campaigns per material/format, and incumbents own years of 24/7 production data. Worse, the cited 500Ah+ tailwind [G01-11] cuts the other way: fewer, fatter joints make 100% EOL 4-wire resistance screening MORE tractable — strengthening the cheap alternative.

## 5. Market/WTP skepticism

The named US beachhead is the G01 brief's own casualty list (KORE cancelled, FREYR cancelled, iM3NY bankrupt) — capital-constrained lines don't buy $60–120K QC heads. Serious integrators buy monitoring from, and keep weld-quality liability with, the welder OEM; a third-party head in the weld cell triggers warranty finger-pointing. In China, selling against United Winners' bundled RWD at Chinese prices is not a strategy. No quoted buyer anywhere validates the ASP.

## 6. Founder fit

Not PhD-lane. "Instrumentation + edge AI" is generic; the moat here is welding-process physics and production weld datasets — the founder has neither, and the data cold-start against Precitec/IPG/United Winners installed bases is structural.

## 7. Score adjustments (raw 79.6)

| Crit | Raw→Adj | Reason |
|---|---|---|
| C1 | 4→3 | No welding-domain capital; moat is training data he can't access (−2.8) |
| C2 | 3→2 | Fused proxies vs. incumbent direct OCT depth measurement = parity at best (−2.4) |
| C3 | 4→3 | Beachhead cohort is cancelled/bankrupt per G01-14 itself (−2.4) |
| C7 | 3→2 | Retrofit whitespace occupied (Precitec/plasmo/VITRONIC) + OEM bundling + EOL resistance (−1.6) |
| C8 | 4→3 | China channel blocked by welder-OEM bundling [RT-V13-11..13] (−1.6) |
| C10 | 5→4 | Destructive-validation campaigns per format stretch time-to-revenue (−1.2) |

**Adjusted total: 67.6** (showdown comparability: 58.7e).

## 8. Steelman

An independent, welder-agnostic QC + IATF serialization layer that OEM-bundled monitors don't provide (cross-line traceability, Cpk evidence) could win second-tier retrofits where OCT was never installed; multi-modal post-weld sensing needs no beam-path access; and BESS onshoring creates new lines faster than Precitec localizes support. But that is a software-led traceability company wearing a sensor-head costume — and the sensor claim is the weak part.

---
**Candidate:** V13 · **Kill-probability: 80%** · **Biggest objection:** the whitespace premise is false — merchant retrofit weld monitors (Precitec LWM on foreign heads, plasmo, VITRONIC) and OCT true-depth measurement (IPG LDD-700, Trumpf, Lessmueller, United Winners RWD) already own this layer, and cheap 4-wire EOL resistance testing covers the rest, leaving V13 inferring what incumbents measure · **Novelty verdict: NOVEL** (ledger-clean; kill is competition/false premise, not duplication)
