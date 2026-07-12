# Geography scope patch — 2026-07-12

> Superseded later on 2026-07-12 by `P3_US_CHINA_WEIGHTING_PATCH_2026-07-12.md`. Retained as an
> audit record; do not use its South Korea exclusion for resumed work.

## Binding user decision

Target markets for this round are the United States, China, Japan, and Taiwan. India, South Korea,
and Singapore are excluded from buyer examples, demand scoring, market sizing, beachheads,
competitive/entry analysis, geography reports, and final recommendations.

Existing publications from excluded countries are retained in the source archive when they are
useful technical evidence. They do not count toward the target-market quota and cannot support a
market case.

## Progress when applied

- Mission: IN_PROGRESS, P3.
- P1 and P2 complete.
- 1,125 canonical sources reviewed; 860 accepted; 484 verified peer-reviewed.
- Fable P2 atlas adjudication PASS.
- P3 seed batches A–D exist; longlist not yet written.

## Reconciliation performed

- Patched binding mission, scoring, source, agent, deliverable, and audit rules.
- Recomputed the target-Asia gate using only CN/JP/TW: 228 accepted (requirement 80).
- Recomputed local-language gate using Chinese/Japanese: 79 accepted (requirement 40).
- Removed excluded-market demand IDs and buyer examples from P3 seed batches A–D.
- Reframed D11 from a Singapore regulation-specific product to a Chinese inland/coastal workboat
  battery-swap product supported by China vessel-operation and classification evidence.
- Added machine checks that reject excluded-market references in the longlist, geography brief,
  and final portfolio.
- Made background-agent indefinite waiting and 429/529 retry watchdog settings permanent in the
  PowerShell launcher.

## Resume instruction

After the Claude usage window resets, run from this folder:

```powershell
.\RUN_FRONTIER_RESEARCH.ps1 -Resume -SkipModelProbe
```

The launcher now applies the wait/retry environment variables automatically.
