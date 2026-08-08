# ALIGNMENT — B20_align (PILOT SAMPLE — NOT FINAL)

Stage: `B20_align` | Mode: `PILOT` | Attempt: `1`
Named worker: `pap06-fable-xhigh` | Requested model/effort: Fable 5 / xhigh

Bidirectional PhD/startup impact analysis, pilot-scoped to exactly SIX ideas.
The user's expectation that the PhD (incl. the Opt2 continuation) and the
startup directions reinforce each other is treated as a HYPOTHESIS under test,
not a conclusion. Every material technical claim maps to B15 evidence rows
(EVxx), B15-adjudicated papers (Pxxxx), B10 claims (Cxx), A30-verified opened
primaries (A30:*), or sources opened this run (S-B20-xx in SOURCES.csv).
Idea IDs are verbatim from the A30-established universe.

## 1. Selection rationale (six of 41)

Chosen to span (a) all four alignment classes, (b) final-set members vs
killed ideas, (c) technical domains near and far from the PhD, and (d) the
corpora's own agreement/disagreement structure:

| idea_id | Why selected |
|---|---|
| P3R2-D-02 | Triple-final member (BLIND 5 / OLD 1 / NEW 1); the corpus's own #1 both runs; the only idea whose core sensing element is literally a Hall array — the best candidate for STRONG, so the strong end is tested on its best case, not a strawman. |
| P3R2-D-01 | Triple-final member (3/3/7); HTS-magnet diagnostics — thematically nearest to "fusion instrumentation," which makes it the sharpest test of the no-causation-from-theme rule. |
| P3R2-A-14 | Triple-final member (6/9/6); harsh-environment instrumentation — probes whether the PhD's most-demonstrated skill (harsh-environment packaging, C46) transfers when the environment axis (300 °C) differs. |
| P3R2-C-13 | In all three finals but low-blind (24/10/9); maximal "GaN" vocabulary overlap with near-zero mechanism — the designated thematic-similarity trap. |
| P3R2-D-10 | The verified OLD-kill/NEW-select split decision (A30 DIS-D10); defense-prime domain far from the PhD with an idea-specific interference mechanism — the ADVERSE candidate. |
| P3R2-C-07 | A killed idea (OLD G7 kill; NEW cut; A30 DIS-C07 verified the kill facts) — ensures the sample includes the killed stratum and a far domain with no interference mechanism, separating WEAK from ADVERSE. |

Records actually read this run: new06 FINAL/DEEP D01, D04, D06, D07; old06
DD_P3R2_D_02, DD_P3R2_D_01, DD_P3R2_C_13; old06 30_SCREENING/EVIDENCE/
P3R2-C-07.md; new06 FINAL/SELECTION.json (all 24 concept entries). D04 and
D06 were read through their mechanism/feasibility/edge sections (not their
full roadmap tails); old06 DD_P3R2_A_14.md was not read (the new06 deep dive
was used as A-14's record). Disclosed, not concealed.

## 2. Rubric

Direction classes (per direction): **direct leverage** = a demonstrated PhD
asset (B10 "demonstrated") maps onto a core, differentiating element of the
venture (or vice versa) through a stated mechanism; **adjacent leverage** =
a real mechanism exists but maps demonstrated assets onto non-core elements,
or proposed assets onto core elements; **speculative transfer** = a
plausible channel exists but is unplanned, unevidenced, or contingent on
work nobody has scheduled; **negative interference** = the direction
actively costs the other side (idea-specific conflict, or opportunity-cost
dominant with zero return channel).

Overall classes: STRONG / MEDIUM / WEAK / ADVERSE, judged on the pair of
directions. ADVERSE is reserved for ideas with an **idea-specific**
interference mechanism (not just the generic opportunity cost that any
non-PhD activity carries — otherwise every far idea would be adverse and the
class would carry no information).

## 3. Verdicts (pilot sample)

| idea_id | PhD→startup | startup→PhD | Overall |
|---|---|---|---|
| P3R2-D-02 | direct leverage | adjacent leverage | **STRONG** |
| P3R2-D-01 | adjacent leverage | speculative transfer | **MEDIUM** |
| P3R2-A-14 | adjacent leverage | speculative transfer | **MEDIUM** (medium/weak boundary) |
| P3R2-C-13 | speculative transfer | speculative transfer | **WEAK** |
| P3R2-C-07 | speculative transfer | negative interference (opportunity-cost only) | **WEAK** (weak/adverse boundary — no idea-specific conflict) |
| P3R2-D-10 | negative interference | negative interference | **ADVERSE** |

## 4. Strongest link

**P3R2-D-02** is the only sampled idea where a *demonstrated* PhD asset sits
on the venture's *core* element: the product's sensing head is a Hall array
(merchant incumbent class verified live this run — TapeStar, non-contact
reel-to-reel Ic inspection at 77 K, up to 1 T on the XL-HF, with no
delamination/thermal channel listed on the vendor page; S-B20-01), and the
PhD demonstrably owns Hall readout-chain design and Hall-die packaging
(C03/C13/C46/C01). Critically, the venture's *decisive risk* — proving
non-contact maps predict transport Ic within 5% under a defensible
uncertainty budget — is the PhD's proposed WP-C methodology (C06) in a
different costume, and B15 shows traceable Hall calibration is a real,
under-published niche (EV01/EV35, template P0008). Even here, honesty limits
apply: (a) the calibration credential is **proposed, not demonstrated**, and
is gated behind the open ~109x anomaly (C04); (b) array instrumentation,
line-speed DAQ, and lock-in thermography are not in B10's demonstrated
ledger — new06 D01 §14's "strongest founder-to-product mapping" claim is
partially overstated against B10 and is corrected here; (c) nothing in D-02
needs GaN, radiation hardness, stellarators, or the hybrid coil direction —
the most-aligned startup uses the least thesis-specific parts of the PhD.

## 5. Weakest links

**P3R2-D-10** (ADVERSE): zero mechanism in either direction plus two
idea-specific interference mechanisms — (i) controlled/classified
defense-prime work vs the PhD's open-publication gate structure (G5 requires
an accepted first-author paper; C49 records zero; OTL gate C33/C34), and
(ii) the A30-verified 2026-2028 decision concentration (JLWS awards executed
2026-07-09; JBCS from Q4-2026; awardee holds the phase-control layer as
proprietary vertically-integrated technology) sitting exactly across the
remaining PhD years. **P3R2-C-07** (WEAK, killed): no mechanism, no return
channel, and the venture itself is impaired on A30-verified primary facts
(45V deadline; shipping AFE incumbent) — it is retired rather than scored.

## 6. Asymmetries between the two directions

1. **Forward > reverse, systematically.** In all six ideas the PhD→startup
   direction is at least as strong as startup→PhD. The reverse direction is
   weak for a structural reason: the PhD's binding constraints are internal
   and hardware-specific — the C04 anomaly, the C45 lost-module question,
   and the publication gate — and no sampled venture supplies any of them.
   A startup can donate money, collaborators, and datasets, but none of the
   six donates the specific unblockers the thesis needs.
2. **The synergy is front-loaded on unexecuted work.** The demonstrated
   assets (bench readout, packaging, deployment experience) transfer
   narrowly; most of the *claimed* synergy rides on proposed Opt2 elements
   (WP-C calibration C06, estimator/identifiability C23/C31, package C10).
   Per B10's discipline a proposed capability transfers less than a
   demonstrated one — so the user's synergy expectation is really a bet
   that Opt2 gets executed. (See IMPACT_MAP counterfactuals.)
3. **Method layer transfers; thesis claims do not.** Across D-02, D-01, and
   A-14 the transferable material is calibration/uncertainty practice,
   EMI-robust measurement, packaging, and estimator methodology — never the
   thesis-specific claims (GaN radiation response is Unknown per C29/EV09;
   the coil→Hall reverse direction is unsupported per EV32; stellarator
   novelty per EV33). The PhD's most distinctive scientific claims are
   exactly the parts with the least startup value in this sample, and vice
   versa: the startup-valuable parts are the least novel scientifically.
4. **Reverse-direction publication risk is low in this sample except where
   it is total.** D-02/D-01/A-14/C-22-class instrumentation work is
   publishable; D-10 flips discontinuously to a structural conflict. The
   spectrum is not smooth — one defense-prime idea class carries almost all
   the publication risk.

## 7. Hypothesis verdict (pilot-scoped)

The mutual-reinforcement hypothesis is **supported in full for at most one
of six sampled ideas (D-02), partially for two (D-01, A-14), and refuted
for three (C-13, C-07, D-10)** — where "refuted" means no concrete
mechanism survives the causation test, or the interference term dominates.
Synergy is idea-specific, not portfolio-general: thematic proximity
("fusion," "GaN," "instrumentation," "control") predicted alignment poorly
(C-13 and D-10 are thematically close on vocabulary and weak/adverse on
mechanism), while mechanism proximity (Hall array + calibration for D-02)
predicted it well. This is a pilot finding on a deliberately spectrum-
spanning sample; the full run must test whether it generalizes.

## 8. Caveats

- Pilot sample of 6 from a 41-idea universe, deliberately chosen to span
  the spectrum — class proportions here are NOT an estimate of portfolio
  proportions.
- All Opt2-derived mechanisms inherit folder-08's pre-redteam status (C40)
  and B10's provenance caveat (C50: strategy/ledger content produced by
  commissioned AI missions, hardware work researcher-attributed).
- Market-timing facts (REBCO ramp, SPARC schedule, JLWS window, superhot
  2030 projects) are corpus-dated and refresh-sensitive; only the TapeStar
  incumbent page and the CFS/Realta release were re-verified live this run
  (S-B20-01/S-B20-02); JLWS and 45V facts rest on A30's opened primaries,
  not reopened here.
- TapeStar's detailed specifications (sensor count, accuracy, speed) remain
  corpus-record claims [NP45-001]; the vendor datasheet PDF fetched this
  run was password-protected and could not be read — disclosed in
  SOURCES.csv.
- Direction classes are mechanism judgments made personally by this worker;
  each row carries a falsifier so the full run and B40 can overturn them on
  evidence.
