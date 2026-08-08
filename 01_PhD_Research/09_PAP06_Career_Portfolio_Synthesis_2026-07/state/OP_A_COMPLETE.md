# Operation A complete

Date: 2026-07-28

All three Operation A stages have accepted pilots, accepted full outputs, and
independent Fable 5/xhigh verification reports ending `VERDICT: PASS`:

| Stage | Pilot | Full candidate | Verification report |
|---|---|---|---|
| A10_blind | pilot/A10_blind/attempt-1 | outputs/A10_blind/attempt-1 | verification/A10_blind/FULL_attempt-1.md (PASS) |
| A20_prov | pilot/A20_prov/attempt-1 | outputs/A20_prov/attempt-1 | verification/A20_prov/FULL_attempt-1.md (PASS) |
| A30_verify | pilot/A30_verify/attempt-1 | outputs/A30_verify/attempt-1 | verification/A30_verify/FULL_attempt-1.md (PASS) |

## Findings of record

- A10 (blind reconstruction): fresh 24-idea shortlist and top 10 from the 126
  blind candidates, 126/126 coverage independently recounted.
- A20 (provenance): core old-corpus idea generation and Claude-side
  adjudication ran on runtime-logged claude-fable-5 (effort request-only,
  never runtime-recorded → PARTIAL_PROVENANCE); the old final-24 selection,
  P4 calibration, P5 red teams, and all later artifacts (deep dives,
  geography, synthesis, audits) were ChatGPT-continuation work with actual
  model unknown → CONTRADICTED. Zero CONFIRMED rows (honest evidence limit).
- A30 (comparison, unblinded): exact-ID overlap at 24 — blind∩old 12,
  blind∩new 16, old∩new 14 (triple intersection 11, union 41); at 10 —
  blind∩old 4, blind∩new 6 (rank-order ten) / 7 (deep-dive ten). Strong
  blind↔new convergence; the old decision layer is the outlier, driven by its
  G7 timing gate and P5 kill severity. Four decision-critical disagreements
  web-verified with opened primary sources (C-05, D-10, C-09, C-07 — C-07 is
  the clearest blind error). Old-corpus overlap is agreement evidence only;
  per A20, no Fable-vs-Fable historical claim is possible.

## Conditions carried into Operation B

- Priority rerun list from A30 VERDICT.md: C-05/C-01 cluster, C-07, D-10,
  C-09, the seven unverified old→new reversals (D-09, F-16, F-19, A-05,
  A-22, D-19, D-16), G-03/F-23, out-of-longlist blind picks, and the three
  P5 supplementals.
- Unresolved: OCP conformance-program status (opencompute.org 403-blocks all
  fetches); Navy JBCS line verified via trade press only.
- All historical effort claims remain request-side only; runtime effort was
  never recorded in the old corpus.

Operation B may now begin per workflow/ROUTE.json.
