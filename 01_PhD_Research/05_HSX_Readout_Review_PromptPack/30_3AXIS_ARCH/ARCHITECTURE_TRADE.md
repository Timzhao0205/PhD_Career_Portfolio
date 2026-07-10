# ST3 — 3-Axis Readout Board Architecture Trade Study (Q3)

**Status:** DECISION_GATE item — requires user sign-off before ordering PCBs/parts.
**Date:** 2026-07-10 · **Scope:** air-side readout only (ambient, ≤20 kHz demod band; no
high-T or wideband considerations apply per HARDWARE_DATA §4).
**Nature of evidence:** this trade is dominated by **ENGINEERING JUDGMENT** (labeled). The
only fetched numbers are PCB fab prices (cited in Sources). No measured bench amplitudes are
used as evidence anywhere in this file (open ~100× anomaly, HARDWARE_DATA §5).

---

## BLUF

**Recommendation: Option C — three replicated single-axis `hsx_2026_v2` boards, racked on a
common baseplate (weighted score 4.75/5).** This confirms the upstream fixed decision
(rsi plan §2.3, "replicate the 02 board per axis") — it also *wins on the merits*, not just
by incumbency: it is the only option with zero respin risk before the immovable Nov 2026
machine time, it inherits the Aug 2026 bench/campaign heritage unmodified, channel isolation
is structural (three physically separate boards, three floating bias loops, three isolated
DC/DC converters), and a blown channel is fixed by swapping a board, not reworking the flight
assembly.

**Runner-up: Option A** (single larger 2/4-layer board carrying three copies of the channel)
at 3.10/5 — better harness dressing and one-build mechanics, but it is a new layout: it
invalidates bench heritage and adds ~4–8 weeks of layout + fab + re-validation the schedule
does not have.

**Flip condition:** if the ΔV gain-anomaly resolution or Campaign #1 (Aug 2026) findings
**force a schematic/layout respin of the single-axis board anyway**, the heritage argument —
Option C's largest advantage — evaporates, and Option A (one 4-layer board, three replicated
channel blocks, all connectors on one edge) becomes the recommendation. Option B (6-layer)
never wins under this project's constraints.

One amendment to the "tower" mental model: **do not stack the three boards face-to-face into
a literal wired tower.** Rack them side-by-side (or offset-stepped) on standoffs on one
baseplate with all DSUB-9/SMA/power/logic connectors facing the same way. Same electrical
architecture, far better connector access and short-circuit inspectability (feeds ST6).

---

## 1. The three options, concretely

| | Option A — single larger board | Option B — 6-layer multichannel board | Option C — 3× replicated boards, racked |
|---|---|---|---|
| **What it is** | New 2- or 4-layer layout, ~3× area, containing three copies of the full channel (2× ADG1209, ADG5236, AD8429, RS6-2415D, J1 DSUB-9, SMA each) plus one shared logic entry | New 6-layer layout, same three channels, using inner plane layers (per-channel GND islands, shielding layers) to compress area and control coupling | Re-order the existing `hsx_2026_v2` gerbers ×3 (package already exists per rsi plan §2.3); hand-assemble two more copies; mount three boards on a common baseplate/rack |
| **Layout work** | New placement + routing; schematic replicated | New placement + routing + **stackup design** (new discipline for this project) | **Zero** — gerbers exist |
| **Inter-channel wiring** | On-board traces | On-board traces | Only the shared a0/a1/a2/EN fan-out + Pico GND bond (ST4); **no analog signal crosses between boards** |
| **Grounds** | One shared GND1 plane (or split planes — extra layout risk) | Dedicated plane layers; best copper | Three independent GND1s, commoned star-style at scope SMA shields + one Pico bond (rsi plan §2.3) |
| **Bias** | 3 floating 100 µA loops entering one board — creepage/routing care needed to keep them floating | Same, with inner-layer isolation | 3 floating loops, one per board — isolation is physical, by construction |

**Fact reconciliation (flag, not judgment):** rsi plan §2.3 says replicate `hsx_2026_v1`;
HARDWARE_DATA §1 says the current validated design is **v2** (only delta: J1 → Amphenol
D09S33E6GX00LF DSUB-9). Replicate **v2**, not v1 — otherwise boards 2–3 regress to the old
connector and the ST6 harness plan breaks. This should be corrected in the plan document.

---

## 2. Weights (sum = 100) and one-line justifications

| Criterion | Weight | Why this weight (ENGINEERING JUDGMENT) |
|---|---|---|
| Reuse of validated single-axis design | 20 | A respin invalidates the entire bench-validation and Campaign-#1 heritage the RSI paper's credibility rests on. |
| Schedule risk | 20 | Nov 2026 HSX machine time is the immovable object (rsi plan §6); Sep/Oct gates have ~zero slack for a board respin. |
| Channel isolation & crosstalk | 15 | Three 100 µA floating bias loops + three in-amps + shared logic: inter-axis crosstalk directly corrupts the vector claim (off-diagonal M terms). |
| Hand-assembly & rework | 15 | User hand-assembles; a blown channel days before the campaign must be repairable without touching working channels. |
| Mechanical fit / harness dressing | 15 | 3× DSUB-9 + 3× SMA + power + logic must dress cleanly near the flange; congestion is a direct short-circuit risk (Q6, user's #1 worry). |
| Ground integrity | 10 | GND1 ×3 + one Pico bond must not form loops; important but manageable in every option with discipline. |
| Cost | 5 | All options are $100s, negligible against machine time and labor; only a tiebreaker. |

---

## 3. Scoring (1 = poor, 5 = excellent) — all scores ENGINEERING JUDGMENT

### 3.1 Criterion-by-criterion reasoning

| Criterion | A — large 2/4-layer | B — 6-layer | C — 3 replicated boards |
|---|---|---|---|
| **Isolation & crosstalk** | **3.** Three channels share one substrate and one ground plane → shared-return currents and RS6-2415D switching spurs (3 unsynchronized converters, HARDWARE_DATA §2: spurs in the 100s of kHz, plus **beat products** between converters that can land in-band) couple through common copper. Careful plane-splitting can fix it — but that's new, unvalidated layout. | **4.** Inner-layer per-channel islands and shield planes genuinely help; still one substrate, still 3 converters on one board. | **5.** Isolation is structural: separate substrates, separate floating supplies, separate DC/DC converters; the only shared conductors are the CMOS logic lines (≈zero DC current) and the star ground. Converter-to-converter coupling is air-gap, not copper. Residual beats couple only via the harness/scope — mitigable by board spacing. |
| **Ground integrity** | **4.** One continuous GND1 plane is simple and robust — but it *forces* the three channels' returns to share copper (this is the same coin as the isolation penalty above). | **5.** Dedicated plane layers are the textbook-best copper. | **4.** Three GND1s commoned at the scope + one Pico bond is clean *if* the star discipline holds; risk is an accidental second inter-board bond (standoffs/baseplate!) creating a loop. Mitigation: insulating shoulder washers or nylon standoffs, verify with the ST6 pre-power ohmmeter check. |
| **Hand-assembly & rework** | **3.** Same part count (3×) as C, but on one flight board: a soldering error, lifted pad, or blown channel means hot-air rework next to two working channels; a fatal board fault scraps everything. | **2.** 6-layer inner plane thermal relief makes hand soldering/rework measurably harder; inner-layer damage is unrepairable; a blown channel risks the whole flight board. | **5.** Identical to the already-practiced v2 build; a blown channel = unbolt one board and drop in the spare (fab minimums give you spare bare boards for free — see cost row). Rework never endangers working channels. |
| **Cost** | **4.** Assume single-axis board ≈ 6 in² (ASSUMPTION A1 below) → large board ≈ 18 in². 4-layer prototype: $10/in² per set of 3 → ≈ **$180** [OSH Park], of which 2 boards are unused spares. Parts ≈ $120/channel × 3 (rsi plan §8) either way. Plus uncosted layout hours. | **3.** 6-layer prototype: $15/in² per set of 3 → ≈ **$270** [OSH Park] + stackup/layout hours + longer fab (12–21 cal. days) [OSH Park]. | **5.** Existing gerbers; 2-layer prototype ≈ 6 in² → **$30 per set of 3** [OSH Park] — the fab minimum *is* exactly the three channel boards (order twice for spares ≈ $60). Parts $120 × 2 more builds (rsi plan §8). Zero layout hours. (If the existing board is 4-layer, ≈ $60/set — still cheapest. See A1.) |
| **Mechanical fit / dressing** | **4.** One plane, all 3 DSUB-9 + 3 SMA + power + logic on one connector edge — the cleanest harness dressing of the three; single mounting plate. Bigger single footprint near the flange. | **4.** Same as A (smaller footprint possible, same connector story). | **4** *as racked* (side-by-side/stepped on a baseplate, connectors co-facing): each board's J1/J4/J2/J3/J5 stays accessible; footprint ≈ 3× one board. Would be **2 if literally tower-stacked face-to-face**: middle-board connectors buried, cables threading between decks — exactly the chafing/mis-mating congestion ST6 exists to prevent. The rack amendment is part of this recommendation. |
| **Schedule risk** | **2.** New layout (1–2 wk) + fab (9–14 cal. days 4-layer [OSH Park]) + assembly + **re-validation of a new layout** + any respin ≈ 4–8 wk. That consumes the entire September gate ("3 working channels on the bench", rsi plan §6) with zero slack. | **1.** All of A plus stackup design, 12–21-day fab [OSH Park], and the highest respin probability (first 6-layer for this project). | **5.** Order bare boards + parts in July (already in the plan), assemble in September per the existing timeline; no layout, no re-validation of anything but the two new *copies* (emulator check per channel, rsi plan §7). |
| **Reuse of validated design** | **3.** Schematic reused, **layout not** — parasitics, plane returns, converter spur coupling, and EMI behavior all change; Aug Campaign-#1 heritage applies only partially. | **2.** Least resemblance to the validated artifact (new layout *and* new stackup). | **5.** Bit-identical copies of the board that will carry Campaign #1; every bring-up lesson, gotcha list, and calibration procedure transfers 1:1. |

### 3.2 Weighted matrix

| Criterion | Wt | A | B | C | A·Wt | B·Wt | C·Wt |
|---|---|---|---|---|---|---|---|
| Isolation & crosstalk | 15 | 3 | 4 | 5 | 45 | 60 | 75 |
| Ground integrity | 10 | 4 | 5 | 4 | 40 | 50 | 40 |
| Hand-assembly & rework | 15 | 3 | 2 | 5 | 45 | 30 | 75 |
| Cost | 5 | 4 | 3 | 5 | 20 | 15 | 25 |
| Mechanical fit / dressing | 15 | 4 | 4 | 4 | 60 | 60 | 60 |
| Schedule risk | 20 | 2 | 1 | 5 | 40 | 20 | 100 |
| Reuse of validated design | 20 | 3 | 2 | 5 | 60 | 40 | 100 |
| **Total /500 (·/5)** | 100 | | | | **310 (3.10)** | **275 (2.75)** | **475 (4.75)** |

Sensitivity (judgment): C wins under any defensible re-weighting. Even zeroing both
schedule and reuse (i.e., pretending there were no deadline and no heritage), the remaining
criteria (out of 300) still score C 275 vs A 210 (B 215) — the isolation and rework advantages
are intrinsic, not schedule artifacts. A only passes C under the flip condition below (heritage
already void). *(Sentence corrected 2026-07-10 per red-team finding RT-06; totals re-derived
from the matrix above.)*

---

## 4. Recommendation, runner-up, flip condition

| Item | Verdict | Failure mode if wrong |
|---|---|---|
| **Recommendation** | **Option C: replicate `hsx_2026_v2` ×3** (confirms upstream decision — and would win this trade even without incumbency). Order bare boards + 2× parts kits in July; assemble Sept. | If C is wrong (i.e., a multichannel board was actually needed), the symptom is inter-board crosstalk or ground-loop pickup discovered in October bench work — recoverable by shielding/spacing, not a redesign; worst case is a noisier-than-budget channel, not a dead campaign. |
| **Rack amendment** | Mount the 3 boards **side-by-side or offset-stepped on one baseplate** with insulating standoffs, all connectors co-facing the flange; do **not** face-to-face tower-stack. Only inter-board wiring: Pico logic fan-out (ST4) + star ground. | If ignored (true tower): buried middle-deck connectors → forced cable bends/chafing and blind mating — direct feed of the Q6 short-circuit worry; also blocks per-board swap-out. |
| **Runner-up** | **Option A: single larger 4-layer board, three replicated channel blocks, one connector edge, split ground pours per channel.** Park as the natural **rev-B** ("integrated multichannel readout" already named as outlook in rsi plan §5/VI). | If promoted now: 4–8 weeks of layout/fab/re-validation against a September gate with no slack → the plausible outcome is missing the Nov 2026 campaign, the project's immovable object. |
| **Not recommended** | **Option B (6-layer):** its only real edge (plane-layer isolation) solves a problem Option C already solves physically, at maximum cost in schedule, rework, and heritage. | If B were secretly necessary (it isn't at ≤20 kHz / 0.5–0.6 V/T signal levels): symptom would be layout-coupled crosstalk on a single-substrate board — which C avoids entirely, so the risk B addresses doesn't exist in the recommended path. |
| **Flip condition** | **Flip C → A if the single-axis layout must be respun anyway** — i.e., the ΔV gain anomaly (HARDWARE_DATA §5) resolves to a board-level fault requiring layout change, or Campaign #1 forces schematic/layout fixes (rsi plan §7, last risk row). Heritage then protects nothing, and A's one-build + one-connector-edge advantages win. Secondary flip: if the air-side envelope at the HSX port cannot physically host a 3-board rack + harness (UNVERIFIED — port-side space not in pack; goes in the July UW email alongside the feedthrough question). | Failing to flip when triggered: hand-building 3 copies of a known-flawed layout — 3× wasted assembly labor and a compromised campaign. |

**Timing note on the flip condition:** the trigger resolves at exactly the right moment —
the ΔV gain check is pending now and Campaign #1 ends late August, *before* boards 2–3 are
assembled in September (rsi plan §6). So the correct action today is: order parts for C, hold
the two extra bare-board assemblies until the anomaly is closed and Campaign #1 debriefs. That
is already the plan's sequencing ("that's why #1 precedes the board builds", rsi plan §7).

---

## 5. Cross-links to other subtasks

| Interface | What this decision fixes for them |
|---|---|
| ST4 (Pico fan-out) | Shared a0/a1/a2/EN drives 3 separate boards over short jumpers on one baseplate — cable length ≈ 10–20 cm, load = 3× CMOS inputs. |
| ST6 (wiring/shorts) | 3 identical DSUB-9 board connectors → per-axis keyed/labeled harness legs; per-board GND1 star; baseplate standoff insulation is an ST6 checklist item. |
| Synthesis / DECISION_GATES | This page + the flip condition go to `90_SYNTHESIS/DECISION_GATES.md` for sign-off before the July parts order. |

---

## 6. Assumptions made

| # | Assumption | Basis / risk |
|---|---|---|
| A1 | Single-axis board area ≈ 6 in² (≈ 2″ × 3″) and 2-layer, for cost estimates only. **UNVERIFIED** — board outline/stackup not in the pack (would need the KiCad PCB file, only netlist facts are given). If actually 4-layer, C's board cost doubles to ≈ $60/set — ranking unchanged. | Typical for this part count; cost is the 5%-weight criterion, so error cannot flip the matrix. |
| A2 | Air-side space near the HSX port admits a ≈ 3-board baseplate (~20 × 25 cm) plus harness bend radius. **UNVERIFIED** — flagged into the July UW email (with the ST5 feedthrough pin-count question). | If false → secondary flip condition above. |
| A3 | The three RS6-2415D converters are not synchronizable (no sync pin assumed for this fixed part) — beat-spur mitigation is spacing/orientation + the demod's out-of-band rejection (spurs in 100s of kHz vs ≤20 kHz band, HARDWARE_DATA §2), not clock sync. | Judgment; converter is a locked design fact, ST1's scope if it were to change. |
| A4 | "Replicate ×3" means replicate **v2** (Amphenol DSUB-9 J1), superseding rsi plan §2.3's "v1" wording. | Reconciliation per SOURCE_STANDARDS §4; flagged in §1 above. |

---

## Sources

- OSH Park PCB services & pricing (2-layer $5/in² per set of 3, 9–12 cal. days; 4-layer
  $10/in² per set of 3, 9–14 cal. days; 6-layer $15/in² per set of 3, 12–21 cal. days):
  https://docs.oshpark.com/services/ (fetched 2026-07-10)
- JLCPCB rigid-PCB capabilities (1–32 layers offered; no public flat pricing on the
  capabilities page — quote tool required): https://jlcpcb.com/capabilities/pcb-capabilities
  (fetched 2026-07-10)
- All non-price scores and reasoning: **ENGINEERING JUDGMENT**, grounded in the design facts
  of `01_MISSION/HARDWARE_DATA.md` (§1–§5) and the fixed plan in
  `01_MISSION/REFERENCE/rsi_experiment_and_publication_plan.md` (§2.3, §6–§8). No measured
  bench amplitudes were used (open anomaly, HARDWARE_DATA §5).
