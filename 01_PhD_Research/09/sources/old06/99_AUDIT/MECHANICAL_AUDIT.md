# Mechanical audit

**Result: PASS**

Run date: 2026-07-14

This audit is non-circular: it validates sources, P4, P5 red-team coverage, the exact P5 selection, exact deep dives, and the P7 portfolio structure before the final mission-state check.

## validate_sources.py — PASS

```text
SOURCE VALIDATION PASS reviewed=1289 accepted=1182 peer=482 demand=298 gov=217 industry=323 US=478 CN=284 side=130 asia=401 local_asia=183 T1=737
  atlas cohort: n=887 T1=648 (73.1%) T1+T2=99.4%
  P4 evidence cohort: n=295 T1+T2=92.2% T3=7.8%
```

## validate_p4.py — PASS

```text
P4 VALIDATION PASS: mode=authoritative ideas=65 survivors=30 eliminated=35
```

## validate_p5_redteams.py — PASS

```text
P5 RED-TEAM VALIDATION PASS
- packets=6 ideas=30
```

## validate_p5_selection.py — PASS

```text
P5 SELECTION VALIDATION PASS
- final=24 top10=10 lanes=12 cheap=11 us=20 cn=18 dual=14 direct=19
```

## validate_deep_dives.py — PASS

```text
DEEP-DIVE VALIDATION PASS exact=10 words=2500-4000 sources>=20/7/5
```

## validate_final_portfolio.py — PASS

```text
FINAL PORTFOLIO VALIDATION PASS exact24 full cards roadmap2026-2034 geography dual-primary
```

## Constraint readback

- Exact 24 final ideas and exact 10 top-ranked deep dives are machine-checked.
- Every selected idea has at least 12 accepted sources, five peer-reviewed records, and three primary-demand records.
- Every deep dive has 2,500-4,000 words and at least 20 accepted sources, seven peer-reviewed records, and five primary records.
- Lane, role, archetype, geography, timing, decisive-experiment, and excluded-market constraints are machine-checked.
- Final mission completion remains blocked until the independent source/claim adjudication passes and `FINAL_AUDIT.md` is written.
