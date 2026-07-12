# START HERE — Round 4: Frontier Idea Research

This is a clean-slate, one-command Claude Code research mission. It accepts at least **600
unique, quality-controlled sources**, creates at least **48 candidate concepts**, and delivers a
diverse final portfolio of **24 startup ideas**. Your EE/Computer Engineering background is kept
as a shallow feasibility prior worth only 5% of the score; it does not choose the search lanes.

## Run from Windows PowerShell

You already have Claude Code installed and logged in. Extract the archive, then:

```powershell
cd <path>\02_Startup\06_Frontier_Idea_Research_2026-07
.\RUN_FRONTIER_RESEARCH.ps1
```

If script execution is blocked:

```powershell
powershell -ExecutionPolicy Bypass -File .\RUN_FRONTIER_RESEARCH.ps1
```

That is the only required interaction. The launcher uses non-interactive mode, verifies Fable 5
and Sonnet 5 availability, writes a raw JSONL transcript, and resumes from on-disk checkpoints.
If Windows sleeps, a usage limit is reached, or the process stops, run:

```powershell
.\RUN_FRONTIER_RESEARCH.ps1 -Resume
```

## What the run produces

- `10_SOURCE_ATLAS/`: 16 independent frontier-lane maps and their source ledgers.
- `20_OPPORTUNITY_POOL/`: 48+ ideas generated from evidence, before founder-fit is considered.
- `30_SCREENING/`: demand checks, competitor maps, physics checks, scoring, and red teams.
- `40_DEEP_DIVES/`: 10 investment/engineering deep dives.
- `50_GEOGRAPHY/`: US, China, Japan, South Korea, Taiwan, India, and Singapore demand/entry map.
- `60_FINAL_PORTFOLIO/`: final 24 ideas, ranked and clustered, plus a validation roadmap.
- `90_BIBLIOGRAPHY/`: canonical 600+ accepted-source ledger and readable bibliography.
- `98_RUN_LOGS/`: raw Claude output, routing decisions, downgrades, failures, and progress.
- `99_AUDIT/`: machine and Fable adjudication reports.

## Model and cost policy

The parent session is fixed to `claude-fable-5` at `xhigh`. Fable performs the critical judgment:
anti-anchoring, idea synthesis, red-team adjudication, deep dives, and final portfolio. Sonnet 5
handles search, source metadata, and repetitive verification at `high` or `medium`. This is an
intentional economy route, not an undisclosed downgrade. Every dispatch is logged in
`98_RUN_LOGS/MODEL_ROUTING_LOG.jsonl`.

No automatic model fallback is permitted. If a configured model is unavailable, the launcher
stops. To intentionally change a model, pass `-CriticalModel` or `-ScoutModel`; the override is
recorded as a user-directed downgrade/upgrade.

Optional controls:

```powershell
.\RUN_FRONTIER_RESEARCH.ps1 -Resume
.\RUN_FRONTIER_RESEARCH.ps1 -CriticalModel claude-fable-5 -ScoutModel claude-sonnet-5
.\RUN_FRONTIER_RESEARCH.ps1 -MaxBudgetUSD 250
.\RUN_FRONTIER_RESEARCH.ps1 -SkipModelProbe
```

`-MaxBudgetUSD` is mainly for API-billed print-mode runs; subscription usage is governed by your
plan limits. A 600-source run is large and may span hours or need several `-Resume` launches.

## Permission boundary

The default uses `dontAsk` plus a project allow-list. Claude can read/write this project, search
the web, run its subagents, and execute the included validation scripts without stopping for
approvals. Unlisted tools are denied. Native Windows Claude Code does not provide an OS-level
folder sandbox for every shell command, so `CLAUDE.md` also imposes a strict project-root rule.
For a hard OS boundary, run the same folder under WSL2 with Claude Code sandboxing enabled.

Do not use `--dangerously-skip-permissions` for this mission: it grants broader machine access
than the folder-only permission you requested.

## Completion test

The run is complete only when `99_AUDIT/FINAL_AUDIT.md` says `PASS` and
`05_STATE/MASTER_STATE.json` contains `"mission": "COMPLETE"`. Source count alone is not enough:
academic sources must have peer-review evidence, demand claims need primary buyer/procurement
evidence, and the final 24 must pass diversity and feasibility gates.

