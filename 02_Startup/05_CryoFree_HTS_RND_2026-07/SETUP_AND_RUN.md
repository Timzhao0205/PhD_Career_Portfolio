# SETUP_AND_RUN — Cryogen-Free HTS Discovery Engine

> **Research aid — not legal advice.** Nothing here authorizes a filing. A registered
> patent attorney reviews before any disclosure or reliance.

This folder is a self-contained Claude Code project. Drop it into your portfolio and run.

## 0. What you're getting
An autonomous engine that: brainstorms cryogen-free HTS component inventions →
harvests prior art in US/CN/JP/KR/EU → simulates the core physics cheaply →
runs three **Fable-5** critical gates (physics, novelty, claim-shaping) →
drafts disclosures for survivors → reports every model/effort/budget choice.
Pre-loaded with 7 candidates (CF-1 flagship = the Rc-vs-thermal-drain conflict,
already physics-seeded) and a working coupled electro-thermal simulation.

## 1. Place the folder
Unzip so it lands at:
```
…/PhD_Career_Portfolio/02_Startup/05_CryoFree_HTS_RND_2026-07/
```
It sits beside `03_C12_C10_Strategy_IP_2026-07` and `04_Cocktail_Dilution_Sensor_2026-07`
and reuses their conventions.

## 2. Prerequisites
- **Claude Code** installed and authenticated (`claude` on your PATH). Verify: `claude --version`.
- **Python 3.10+** with numpy/scipy/matplotlib (the sims): `pip install numpy scipy matplotlib`.
- Model access on your account for **Haiku, Sonnet, Opus, and Fable 5** (the routing
  uses all four). If you lack Fable 5 access, the run still works — see step 6.
- Personal machine/repo only (ownership protocol). `git init` here if you want dated commits.

## 3. Confirm the wiring (once)
From inside the folder:
```
python tools/check_runlog.py          # expect: RUN-LOG CHECK: green
python 20_SIM/thermal_network.py      # expect: the 4-row interface table + a KNOWN-ISSUES note
```
The thermal starter INTENTIONALLY ships with a tau↔Rc coupling-direction bug recorded
in `20_SIM/out/cf1_starter.json` → it's the first thing the physics gate (G-PHYS)
must catch. Don't "fix" it by hand; let the pipeline exercise the gate.

## 4. How model routing works
- `.claude/settings.json` sets the **default** (`opusplan` / effort `medium`).
- Per-stage models come from the **subagent frontmatter** in `.claude/agents/`:
  `cryo-ideator`=sonnet, `prior-art-scout`=sonnet, `fable-adjudicator`=**fable-5**.
- The routing TABLE the orchestrator follows is in `CLAUDE.md`. It logs intended
  model per stage as `models=role:model` in `80_STATE/PROGRESS_LOG.md`.
- **Fable-5 is pinned to the three gates only** (physics / novelty / claim-shaping) —
  the least-reversible calls — so you spend the premium model where it changes outcomes.

## 5. Set your budget (do this before the first real wave)
Open `80_STATE/RUN_STATE.json` → `budget_tokens.ceiling`: set an integer token
ceiling for the run (e.g. 2_000_000). The orchestrator checks spend at each wave
checkpoint and halts into resume if >90% consumed. Leave 0 to run uncapped (not
recommended).

## 6. If you don't have Fable 5 access
Edit `.claude/agents/fable-adjudicator.md` frontmatter `model: fable-5` → `model: opus`
and set effort high. You lose the mandated premium adjudication but the pipeline is
otherwise identical. (Note: even with access, Anthropic safeguards may transparently
route some Fable-5 queries to Opus 4.8; the engine logs this uncertainty rather than
hiding it — see CLAUDE.md.)

## 7. Launch — ONE COMMAND, HANDS-OFF (the default)
This build runs fully autonomously: full read/write inside the folder, no
per-step approvals, auto-resume across budget/interruption checkpoints until the
pipeline finishes. From the folder:

**macOS / Linux**
```
cd …/02_Startup/05_CryoFree_HTS_RND_2026-07
./RUN.sh                 # default 2,000,000-token budget ceiling
./RUN.sh 5000000         # or set your own ceiling
```
**Windows PowerShell**
```
cd …\02_Startup\05_CryoFree_HTS_RND_2026-07
.\RUN.ps1                # or:  .\RUN.ps1 -Ceiling 5000000
```
That's it. The launcher invokes Claude Code headless with `/autorun`, which drives
W0→W5 without stopping, then exits. Progress streams to `run_console.log`; results
land in `10_MISSION/RND_STRATEGY_CryoFree.md` and `98_CLAUDE_METRICS/RUN_REPORT.md`.
If it pauses at a budget checkpoint, just run the same command again — it resumes
from `RUN_STATE.json`, never restarts.

### Permissions model (what "full permission" means here)
`.claude/settings.json` sets `defaultMode: bypassPermissions` scoped to THIS folder
(`additionalDirectories: ["."]`), so no approval prompts. Guardrails still apply via
a `deny` list: **no writes/reads outside the folder** (`../**` denied — protects the
rest of your portfolio), and `rm`, `curl`, `ssh`, `scp` are blocked. The launcher
passes `--dangerously-skip-permissions` so a long unattended run never stalls on a
prompt; the deny list is what keeps that safe. If you'd rather approve tool calls,
delete that flag from RUN.sh/RUN.ps1 and set `defaultMode` back to `acceptEdits`.

### Interactive alternative (optional, if you want to watch/steer)
```
claude
/autorun            # same autonomous run, inside an interactive session
# or drive it manually, one checkpoint at a time:
/status  ·  /runwave 1  ·  /runwave 2  ·  /gates CF-1  ·  /runwave 4  ·  /runwave 5  ·  /metrics --transcripts
```
To rerun one weak stage later on a stronger model, edit the agent frontmatter (or
ask in-session) and re-issue that wave/gate — the run-log lets you target a single
stage without redoing the rest.

## 8. Where things land
- Ideas → `30_IDEATION/` · Prior art + gate verdicts → `60_PRIOR_ART/<CF>/`
- Sims → `20_SIM/…/out/` · Disclosures → `70_DISCLOSURES/ID_##_*.md`
- Strategy + ranking → `10_MISSION/RND_STRATEGY_CryoFree.md` (W5)
- Model/effort/budget audit → `98_CLAUDE_METRICS/RUN_REPORT.md` + `logs/*.jsonl`

## 9. Hard rules the engine obeys (full text in CLAUDE.md)
No GaN; no "stellarator" in patent text; any candidate touching the funded lane
(HSX plasma diagnostics, GaN Hall device dev, battery imaging) is stubbed
BLOCKED-PENDING-COUNSEL; China's no-grace-period means the engine writes to the
private repo only and never posts/emails; duty of candor (all found art → IDS_pool);
simulations labeled prophetic, never blended with measured data; no filings — it
proposes, you and counsel dispose.

## 10. First thing to actually do
`/status`, then `/runwave 1`, then read the harvest. If CF-1's prior-art comes back
clean-ish, it's the one to push through the gates first — the physics seed is already
in hand and it composes with Patent A.
