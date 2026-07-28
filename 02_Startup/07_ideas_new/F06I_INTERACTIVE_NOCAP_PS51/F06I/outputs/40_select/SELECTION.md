# P5 portfolio selection (2026-07-28)

The main Fable 5/xhigh agent selected 24 of the 30 red-teamed survivors and
ten deep dives, reconciling P4 scores with red-team evidence by judgment
rather than averaging.

## Ranking logic

Ranks 1-7 are the clean-survive ideas whose wedges were fresh-verified during
red-team (D-02, C-01, C-05, D-10, E-14, A-14, D-01). C-05 outranks D-10
despite a 0.4-point score gap because its demand is live now and its
whitespace verification was the strongest in the review, while D-10 carries a
design-win-window timing tension. Ranks 8-10 are the three highest-scoring
repair ideas (A-10, C-13, F-01) — each demoted below equal-scored clean
survivors because their CN chapters require mandatory counterparty
restructuring. Ranks 11-18 follow reconciled strength (A-05, C-09, C-22,
C-08, G-03, E-04, D-09, A-22); G-03 moves above the higher-scoring E-04
because G-03's whitespace was verified at the strongest level while E-04's
density wedge was lost to the shipping Delft/Bluefors roadmap. Ranks 19-24
(C-04, D-19, F-16, F-19, F-23, D-16) are the portfolio's option tier.

## Tradeoffs and replacements at the cut line

- **F-23 in, D-18 out.** D-18 scored 3.3 points higher but its demand is one
  SBIR topic with no award across two visible cycles; F-23 brings dual-market
  breadth (reduced-but-real hub cost-share plus CN retrofit audits) under the
  binding US/China geography scope, with its repairs recorded as binding.
- **C-04 in, B-01 out.** One two-phase-loop thesis, one slot: C-04's
  chemistry-forced US/EU legs plus dual-market shape beat B-01's CN-only,
  now-decomposed mechanism (Sugon two-phase cold plates; Chuanrun
  negative-pressure CDUs).
- **L14 cap (3):** C-05, C-04, F-19 kept; D-12 (research-only EHD with an
  empty fluid intersection) and D-13 (GA/ACT incumbency at lower tiers)
  dropped alongside B-01.
- **A-02 out:** the DC cluster is represented by C-01/E-14/G-03; A-02's $1.5M
  experiment misfits the capital path and DG Matrix-class SST entrants are
  capturing its customer line.
- **F-10 out:** lowest-ranked survivor with the POD-at-speed make-or-break
  unproven and a documented US H2-pipeline delay.

## Deep-dive choices (10)

Ranks 1-8 (D-02, C-01, C-05, D-10, E-14, A-14, D-01, A-10) plus C-09 (12) and
C-22 (13). C-13 (9) and F-01 (10) were passed over for deep dives — not from
weakness but because each duplicates a lane already carried by a higher-ranked
deep dive (L12 by D-10, L06 by A-10) while both carry the same
CN-counterparty repair class as A-10, which the A-10 dive will treat in
depth. C-09 and C-22 extend deep-dive coverage to L05 and L11, giving the ten
dives nine distinct lanes, seven dual-market theses, and all three verified-
whitespace instrument plays.

## Constraint adjudications

Two frozen portfolio constraints are unsatisfiable by construction from the
frozen longlist (documented with true observed counts in
PORTFOLIO_CHECKS.json): no sub-$100k experiment exists among all 65 frozen
ideas (minimum $120k), and only 17 gate-clean survivors carry a China
beachhead against an 18-idea target — a deficit created by CN-heavy ideas
failing their own binding evidence conditions at P4. The selection preserves
capital-lightness (14 ideas at or under $300k) and China primacy (14 CN
beachheads, 13 dual-market, China analyzed as a primary market throughout)
without resurrecting evidence-failed ideas or fabricating counts.

## Near misses

Recorded in SELECTION.json with reasons: D-18, A-02, D-12, B-01, D-13, F-10.
F-10 is the strongest revisit candidate if a battery-line defect-escape
datapoint emerges; D-18 revives on an A254-049 award plus a second anchor.
