# P3 US/China weighting patch — 2026-07-12

## Binding decision

The United States and China are the primary markets. They dominate idea generation, demand
validation, scoring, and the final portfolio. Japan, Taiwan, and South Korea are optional side
markets only. India and Singapore remain excluded markets. Technical publications may originate
anywhere, but market claims must be country-specific.

## Progress at patch time

- Mission remains `IN_PROGRESS`, phase P3.
- P0, P1, and P2 are complete and must not be repeated.
- 1,125 canonical sources were reviewed; 860 accepted; 484 peer reviewed.
- The source validator and Fable P2 atlas adjudication passed.
- Prior seed batches A-D exist, but the longlist has not been written (`longlist_ideas: 0`).

## Authoritative P3 round 2

Keep `SEEDS_A-D` as an audit trail, but do not directly promote them. Generate at least 80 new
`P3R2_*` seeds in five independent Fable 5/xhigh batches: US, China, dual US-China, frontier
energy/physics wildcards, and optional JP/TW/KR side markets. Then run the independent
`idea-elegance-judge` at Fable 5/xhigh. It must write its adjudication before longlist freeze.

Longlist minimums: 48 ideas, 14 lanes, 36 credible US cases, 36 credible China cases, 24 credible
dual US-China cases, and at most 8 primarily reliant on JP/TW/KR. Final-24 minimums: 18 US, 18
China, 12 dual, and at most 4 primarily reliant on JP/TW/KR.

## Model/effort decision

No downgrade. All P3 generation and the independent elegance adjudication use Fable 5/xhigh.
Claude Code exposes `max` only on models that support it; the package therefore uses Anthropic's
recommended capability-sensitive Fable setting (`xhigh`) and adds a second independent critical
pass as the quality upgrade. Never silently fall back or claim an unverified effort level.

## Resume

From Windows PowerShell in this folder:

```powershell
.\RUN_FRONTIER_RESEARCH.ps1 -Resume -SkipModelProbe
```

Omit `-SkipModelProbe` if you want to re-check model availability before spending the next usage
window. The launcher waits indefinitely for background tasks and retains its retry watchdog.
