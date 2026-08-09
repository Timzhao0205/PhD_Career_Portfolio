# ALIGNMENT — B20_align (FULL)

Stage: `B20_align` | Mode: `FULL` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Bidirectional PhD/startup impact analysis over the COMPLETE set of serious
directions. The user's expectation that the PhD (including the Opt2
continuation) and the startup directions reinforce each other is treated as a
HYPOTHESIS under test, not a conclusion. Every material technical claim maps
to B15 evidence rows (EVxx), B15-adjudicated papers (Pxxxx), B15 gap/bridge
IDs (G/M/BT), B10 claims (Cxx), A30-verified opened primaries (A30:*), or
sources opened by this stage (S-B20-xx in SOURCES.csv). Idea IDs are verbatim
from the A30-established universe. No portfolio ranking appears here (that is
B40); classification only.

## 1. Inclusion boundary (stated and defended)

**Universe: exactly the A30 union of 41 ideas** — every member of BLIND24,
OLD24, and NEW24 per `outputs/A30_verify/attempt-1/COMPARE.json`
(inclusion-exclusion check 72 − 12 − 16 − 14 + 11 = 41), including the three
P5 supplementals (P5-USSCI2-S01, P5R2-CN-01, P5R2-CN-03).

**No additions beyond the 41.** The task permits adding further serious
directions only if they carry substantive deep-dive-class records. I checked:
old06's ten deep dives cover only OLD top-10 members; new06's ten DEEP files
cover only NEW24 members (ranks 1–8 plus C-09, C-22). Every non-union
candidate (e.g. near-misses D-18, D-13, F-10, A-02-adjacent variants, and the
longlist canonicals A-13/A-21) has at most screening/pool-record depth AND was
rejected by both baselines; the two canonicals are additionally already
represented in the universe through their documented blind-side duplicates
(E-10, C-15). Adding such rows would inflate the universe without deep-dive
support, against the task's no-padding instruction. Boundary: 41 IDs, no more,
no fewer.

## 2. Consolidation ledger (semantic dedup — one row per underlying direction)

Consolidations use ONLY A30's documented semantic ledger, never name
similarity:

| Ledger | Consolidation | Basis | Effect |
|---|---|---|---|
| SEM-01 | **P3R2-E-01 → row P3R2-C-01** | Old06's own elegance adjudication: E-01 REJECT, duplicate_of C-01, same "800VDC rack-inlet protection" cluster; A10 chose the opposite representative of the same documented cluster | One row (C-01) analyzes the underlying 800VDC-protection direction; E-01's pool record was read and its blind rank 1 is carried in the row |
| SEM-02 | **P3R2-B-01 → row P3R2-C-04** | New06's own near-miss note ("the same two-phase-loop thesis as C-04 — its own merge notes say so") and A10's absorption decision | One row (C-04) analyzes the two-phase-loop direction; B-01's evidence record header was read and its old rank 12 is carried in the row |
| SEM-03 | E-10 kept as its OWN row | Its documented canonical (A-13) is in NO final set, so no in-universe consolidation target exists | E-10 represents the rad-tolerant-GaN-PPU direction itself |
| SEM-04 | C-15 kept as its OWN row | Same structure: canonical A-21 in no final set | C-15 represents the heavy-fleet-charging direction itself |
| NON-MATCH-C14 | C-14 and A-22 kept as SEPARATE rows | A30 explicitly adjudicates them as different products (plasma power supplies vs destruction equipment); merging would be theme-based, which the ledger rules forbid | Two rows |

**Row count: 39 = 41 − 2.** Reconciliation: every one of the 41 union IDs
appears verbatim either as a row `idea_id` (39) or inside the consolidated
row's name/source_version cells with its SEM ledger ID (E-01 in C-01; B-01 in
C-04). No ID is dropped, renamed, or silently merged.

## 3. Rubric (carried unchanged from the accepted pilot)

Direction classes (per direction): **direct leverage** = a demonstrated PhD
asset (B10 "demonstrated") maps onto a core, differentiating element of the
venture (or vice versa) through a stated mechanism; **adjacent leverage** = a
real mechanism exists but maps demonstrated assets onto non-core elements, or
proposed assets onto core elements; **speculative transfer** = a plausible
channel exists but is unplanned, unevidenced, or contingent on work nobody has
scheduled; **negative interference** = the direction actively costs the other
side (idea-specific conflict, or opportunity-cost dominant with zero return
channel).

Overall classes: STRONG / MEDIUM / WEAK / ADVERSE, judged on the pair of
directions. ADVERSE is reserved for ideas with an **idea-specific**
interference mechanism (not the generic opportunity cost every non-PhD
activity carries — otherwise every far idea would be adverse and the class
would carry no information). Mechanism is required throughout; thematic
similarity ("fusion", "GaN", "plasma", "instrumentation", "DC") is never
accepted as causation, and several rows explicitly test and reject such
chains.

## 4. Alignment-class distribution (39 rows)

| Overall class | Count | Ideas |
|---|---|---|
| **STRONG** | 1 | D-02 |
| **MEDIUM** | 7 | D-01, A-14 (boundary), A-10, C-05 (boundary), D-09 (boundary), E-04 (boundary), F-06 (boundary) |
| **WEAK** | 30 | C-01, E-14, C-13, F-01, C-09, C-22, C-08, C-04, F-02, F-12, G-01, G-03 (boundary), D-12, F-23, F-03, S01, CN-01, CN-03, C-07 (boundary), C-12, A-02, A-05, A-22, D-19, F-16, F-19, D-16, E-10, C-14, C-15 |
| **ADVERSE** | 1 | D-10 |

Per-direction usage: direct leverage appears once (D-02 forward); adjacent
leverage eight times (D-02 reverse; seven forwards); negative interference
four times (D-10 both directions; C-07 and CN-03 reverse, opportunity-cost-only
at the weak/adverse boundary); speculative transfer fills the remainder. All
four classes are used where genuinely present; no class was forced.

## 5. Overall patterns

1. **Alignment concentrates in a single mechanism family: measurement
   authority.** Every non-WEAK forward direction runs through one of two
   channels: (a) the *demonstrated* hardware channel — Hall readout chains,
   harsh-environment packaging, EMI-disciplined bench measurement
   (C01/C03/C13/C46) — carrying D-02, A-10, A-14, E-04; or (b) the *proposed*
   traceable-calibration/uncertainty-budget methodology channel — WP-C's
   GUM/Monte-Carlo discipline (C06) plus estimator honesty (C23/C31) —
   carrying D-02's decisive leg, C-05, D-09, F-06, and D-01's estimator leg.
   Nothing else in the PhD transfers anywhere in the 39-idea universe.
2. **Consensus strength and alignment are independent axes.** The corpus's
   top consensus idea (C-01: BLIND 1 via SEM-01 / NEW 2 / OLD 5) is WEAK;
   old06's #2 (C-22) is WEAK; blind's #4 (C-09) is WEAK. Conversely two of the
   revived NEW-only ideas (D-09) and one both-baselines-cut idea (F-06) carry
   genuine MEDIUM mechanisms. B40 must not read cross-run agreement as
   founder-fit evidence.
3. **Thematic proximity still predicts alignment poorly — now on 39 ideas,
   not 6.** The full run adds three more explicit vocabulary traps to the
   pilot's C-13: E-10 (GaN+radiation, disjoint failure physics per
   C29/EV09/M1), A-22/C-14/F-16 (plasma-as-host vs plasma-as-process), and
   D-19/F-03 ("magnetic" machines vs field metrology). Every one fails the
   mechanism test. Meanwhile the least fusion-flavored ideas (C-05 thermal
   benches, D-09 medical-beam ammeter) carry real mechanisms through the
   traceability methodology.
4. **The "neutral qualification authority" business theme recurs (C-05, E-14,
   C-22, G-03, F-23, D-09) but theme is not mechanism.** Only where the
   authority position is built on *traceable measurement uncertainty* (C-05,
   D-09, marginally G-03) does the PhD's methodology map onto the core; where
   it is built on domain attribution (C-22 electrochemistry, E-14 protection
   algorithms) the link stays speculative.
5. **Killed/cut status barely correlates with alignment.** The kill/cut
   stratum (14 rows) contains both the sleeper MEDIUM cases (D-09, F-06) and
   pure mechanism-absence rows — alignment is orthogonal to the corpora's
   commercial verdicts in both directions.

## 6. Strongest link

**P3R2-D-02** remains the only idea in the full universe where a
*demonstrated* PhD asset sits on the venture's *core* element (Hall-array
sensing head; incumbent class verified live: S-B20-01), with the decisive
risk (transport-calibrated Ic within 5% under a defensible uncertainty
budget) being the proposed WP-C methodology (C06) in a different costume
(EV01/EV35/G3/M3, template P0008). The full run confirms the pilot's honesty
limits: the calibration credential is proposed-only and gated by C04; array
instrumentation, line-speed DAQ, and lock-in thermography are not in B10's
demonstrated ledger (new06 D01 §14 correction carried); and the most-aligned
startup uses the least thesis-specific parts of the PhD.

The strongest **new** finding of the full run is the second tier: **A-10**
(demonstrated in-plasma packaging + EMI readout onto the production-hardened
sensing core; merchant metrology incumbent verified measurement-only live,
S-B20-03) and **D-09** (proposed traceable-current-metrology methodology onto
a buyer-mandated NIST-traceability core, in the magnetic-sensing family).
Neither reaches STRONG: A-10's control engine and process-domain depth are
unevidenced, D-09's methodology is proposed-only and its market is small.

## 7. Weakest links

**P3R2-D-10** (ADVERSE — carried, unchanged): zero mechanism either way plus
two idea-specific interference mechanisms (classification vs the open-
publication gate structure G5/C49/C33/C34; the A30-verified 2026-2028
decision window sitting across the remaining PhD years). No other idea earned
ADVERSE on the full sweep: E-04's deemed-export friction (BIS quantum/cryo
rule vs an international-student founder, C42) is a real idea-specific
conflict flag but its mechanism balance stays positive-adjacent, so it is
MEDIUM-with-conflict, not ADVERSE — the distinction is disclosed in its row.
**C-07** and **CN-03** sit at the weak/adverse boundary (reverse = negative,
opportunity-cost-only, no idea-specific conflict) exactly as the rubric
requires.

## 8. Asymmetries between the two directions

1. **Forward > reverse in every one of the 39 rows.** The pilot's structural
   explanation survives the full sweep: the PhD's binding constraints are
   internal and hardware-specific (C04 anomaly, C45 lost module, publication
   gate C49), and no venture in the universe supplies any of them. The
   reverse direction's best cases are collaborator/dataset channels (D-01,
   A-10, D-09) and three concrete-but-unplanned piggyback channels: A-14's
   high-T ovens closing the P0017 data gap, E-10/D-16-class irradiation
   campaigns closing M1 (BT-5), and F-06/F-02's trusted current references
   serving FT-05/BT-3.
2. **The synergy is front-loaded on unexecuted work — now quantified.** Of
   the 8 non-WEAK forward directions, 5 lean on proposed Opt2 elements
   (C-05, D-09, F-06 on WP-C methodology; D-01 on estimator honesty; D-02's
   decisive leg on C06) and inherit folder-08/pre-redteam and C40 caveats;
   only 3 (A-10, A-14, E-04) ride mostly on demonstrated assets. The user's
   synergy expectation is, concretely, a bet that Opt2 Element 1 (and its
   FT-02 honesty gate) gets executed — see IMPACT_MAP counterfactuals.
3. **Method layer transfers; thesis claims do not — universe-wide.** Nowhere
   in 39 ideas does the stellarator deployment claim, the GaN radiation
   question (C29, Unknown), or the hybrid coil→Hall direction (EV32, G1)
   carry commercial value. The PhD's most distinctive scientific claims have
   the least startup value, and the startup-valuable parts (calibration
   discipline, packaging, EMI measurement) are the least novel scientifically
   (EV11, EV12).
4. **Publication risk is bimodal.** 38 of 39 ideas carry low or ordinary
   publication risk; D-10 alone flips to structural conflict. E-04 adds an
   export-control (not publication) discontinuity. The spectrum is not
   smooth, confirming the pilot on the full universe.

## 9. Changes from the accepted pilot (disclosed)

- **All six pilot analyses carried.** D-02, D-01, C-13, C-07, D-10 rows are
  substantively unchanged (pilot-label text removed; B15 gap IDs G3/M3/M7
  added to evidence chains where they resolve).
- **A-14: the pilot's disclosed gap is closed** — old06 DD_P3R2_A_14.md was
  read this run. It confirms the pilot classification (packaging is the
  gating asset; CISSOID last-time-buy; DARPA THERMAL context) and changes
  nothing. Class unchanged: MEDIUM (boundary).
- **Founder-fit corrections extended.** The pilot corrected new06 D01 §14
  (D-02) and D04 ("founder's home ground", D-10). This run adds three more,
  each checked against B10's demonstrated-vs-proposed ledger: D02 §14
  (C-01: "power-electronics engineering, the founder's core stack" — no
  power-electronics work is in B10's demonstrated ledger), D03 (C-05:
  "controls-and-DAQ problem squarely in the founder's stack" — bench DAQ
  demonstrated, multi-kW calorimetric/thermal metrology not), and D08 §14
  (A-10: "system identification and deterministic closed-loop control are
  the founder's core" — those are proposed Opt2 elements C23/C31, pre-redteam
  C40, not demonstrated).
- **New classifications beyond the pilot's six**: 33 rows, of which five are
  non-WEAK (A-10, C-05, D-09, E-04, F-06) — each with the mechanism stated
  and bounded in its row.

## 10. Hypothesis verdict (full universe)

The mutual-reinforcement hypothesis is **supported in full for exactly one of
39 directions (D-02), partially for seven (D-01, A-14, A-10, C-05, D-09,
E-04, F-06 — several at the medium/weak boundary), and unsupported or refuted
for thirty-one** (30 WEAK + 1 ADVERSE). Synergy is idea-specific and
mechanism-borne, not portfolio-general: roughly four-fifths of the serious
direction universe neither helps nor is helped by the PhD beyond generic
engineering competence, and one direction actively conflicts. The pilot's
spectrum-spanning finding generalizes: mechanism proximity (Hall arrays,
traceable calibration, in-plasma packaging, precision current metrology)
predicts alignment; thematic proximity does not.

## 11. Caveats

- All Opt2-derived mechanisms inherit folder-08's pre-redteam status (C40)
  and B10's provenance caveat (C50: strategy/ledger content produced by
  commissioned AI missions; hardware work researcher-attributed).
- Old06 record-layer provenance: per A30, the old06 decision layer is
  CONTRADICTED-provenance; old06 deep-dive/evidence content is used here as
  record evidence with primary citations, never as authority. New06's runtime
  provenance is unaudited (A30 note). Where the two conflict on an idea's
  facts, the row says which record was used.
- Market-timing facts are corpus-dated unless marked A30-verified
  (C05/C07/C09/D10 registers) or opened this stage (S-B20-01/02/03); the
  F-19 reversal carries A30's explicit unverified flag.
- Record-depth varies by design: deep-dive tier (14 rows), screening-evidence
  tier (18), selection-entry/pool tier (7, disclosed per row — CN-03 is the
  thinnest). Far-idea rows are deliberately tight per the task's efficiency
  rule; tightness is not evidence of shallow consideration — each records a
  tested mechanism absence.
- Direction classes are mechanism judgments made personally by this worker
  (not delegated); each row carries a falsifier so B25/B30/B40 and the
  verifier can overturn them on evidence.
