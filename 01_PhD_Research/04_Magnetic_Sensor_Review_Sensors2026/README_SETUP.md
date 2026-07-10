# Magnetic-sensor review paper — automated pipeline (setup & run)

This folder runs your whole "titles + outlines + literature review" job on Claude
Code with **one command**, using a different model and effort level per stage so
the budget goes where it matters. It writes every deliverable, logs every source,
and records what it did so you can patch specific parts later.

Target: a review for **MDPI *Sensors*** on magnetic-field sensors, their
applications (energy, transportation, industrial & manufacturing, biomedicine),
future directions (data-driven modeling, ML control, multi-modality / digital
twin), and standards/potential for a business+investor audience — submission
before **30 Oct 2026**.

---

## 1. Put it in place
Extract so this folder sits inside your research root, alongside `02_...` / `03_...`:

    01_PhD_Research\
      04_Magnetic_Sensor_Review_Sensors2026\   <-- this folder

## 2. Prerequisites
- **Claude Code, logged in** — you said it already is. Check: `claude --version`.
- **Python + the `markdown` package** — only for the reader-friendly `.html`
  mirrors (same as your other reports). One-time: `pip install markdown`.
  If you skip this, everything else still works; run with `-SkipHtml`.

## 3. Run it (the one command)
From PowerShell, inside this folder:

    powershell -ExecutionPolicy Bypass -File .\run.ps1

That's the whole job. It preflights Claude Code, checks Fable 5 is reachable,
runs all stages in order, regenerates the HTML mirrors, and prints a cost summary.

Useful variants:

    .\run.ps1 -DryRun               # show the plan + model/effort per stage, run nothing
    .\run.ps1 -OnlyStage 10,20      # just the Friday deliverable: titles + outlines
    .\run.ps1 -FromStage 30         # resume from the sensor-taxonomy stage onward
    .\run.ps1 -OnlyStage 50 -Force  # re-run one stage to produce a patch
    .\run.ps1 -Safe                 # scoped permissions instead of skip-permissions
    .\run.ps1 -SkipHtml             # don't build the .html mirrors

Stages that finish are marked done in `.state\`, so a plain re-run only does
what's left. Use `-Force` to redo a stage.

---

## 4. What runs, and where Fable 5 goes (my recommendation)

You asked me to put **Fable 5 on the most critical parts**. My read: the parts
where a wrong judgment or an invented citation does the most damage are the
**sensor taxonomy**, the **future-methods synthesis** (buzzword-adjacent, highest
hallucination risk), and the **paper architecture** (titles, outlines, final
integration). Those run on Fable 5 at high effort. Broad-but-bounded enumeration
(applications, standards) runs on Opus; careful mechanical work (journal brief,
bibliography) on Sonnet; bookkeeping on Haiku.

| # | Stage | Model | Effort | Why this tier |
|---|-------|-------|--------|---------------|
| 00 | Journal requirements brief | Sonnet | low | Fetch + digest MDPI pages; careful, not creative |
| 10 | 15 titles | **Fable 5** | high | Headline deliverable; framing quality matters |
| 20 | 3–4 full outlines | **Fable 5** | high | Architecture of the whole paper |
| 30 | Sensor taxonomy (commercial + pioneering) | **Fable 5** | high | Intellectual core; strengths/weakness judgments |
| 40 | Applications (4 domains) | Opus | high | Broad but enumerative |
| 50 | Future methods (data/ML/digital-twin) | **Fable 5** | high | Highest hallucination risk; strongest reasoning |
| 60 | Standards + business/investor | Opus | high | Well-bounded; needs care, not novelty |
| 70 | Bibliography: verify DOIs, dedupe, format | Sonnet | medium | Mechanical + careful; Crossref checks |
| 80 | Assemble deliverable + gap matrix | **Fable 5** | high | Final integration and honest gap analysis |
| 90 | Patch notes / run digest | Haiku | low | Cheap bookkeeping |

Effort is set per stage via the `CLAUDE_CODE_EFFORT_LEVEL` env var. The Fable
stages also carry a `think hard` / `ultrathink` directive in their prompt so
reasoning depth holds regardless of how the effort knob maps for a given model.

**Change any of this in one place:** the `$Stages` table at the top of `run.ps1`.
Swap a model (`FABLE`, `opus`, `sonnet`, `haiku`, or a full id like
`claude-opus-4-8`), change `Effort`, or lower `MaxTurns` to cap spend. If your
Fable model id differs, edit `$FableModel` at the top too.

---

## 5. Permissions & safety
Default is `--dangerously-skip-permissions` so the run never stops to ask — this
matches your "full read/write, least interaction, one command" ask, and it's your
own machine and folder. If you'd rather scope it, run with **`-Safe`**, which
switches to `acceptEdits` permission mode plus an allow-list of exactly
`Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, TodoWrite` — enough for this
job, nothing else, and no arbitrary shell. The pipeline does not need Bash: the
HTML mirrors are built by PowerShell calling `tools\build_html.py` after the model
stages, not by the agent.

## 6. Source quality — how it stays honest
The rules live in `prompts\_shared_system.md` (appended to every stage) and
`CLAUDE.md`. In short: never fabricate a reference, DOI, or quote; every non-
obvious claim traces to a real source retrieved that run or in the seed;
peer-reviewed preferred; **preprints (arXiv, etc.) only to discover work, then
cite the version of record** — and any that stay preprints are tagged. Vendor
datasheets are tagged and used only for device facts. Every source used is logged
to `refs_raw\*.jsonl`; Stage 70 verifies DOIs via Crossref, dedupes, and produces
`references.bib`, `reference_registry.csv`, and a QA report that flags anything
not peer-reviewed. A verified seed of real anchor references is in
`refs_raw\00_seed.jsonl` / `seed\seed_references.md`.

---

## 7. Outputs
Everything lands in `outputs\` (open the `.html` mirror of each, or the `.md`):

- `00_DELIVERABLE_paper_plan.md` — **start here**: recommended title + shortlist,
  recommended outline, section-by-section annotated briefs with citations, and a
  coverage/gap matrix.
- `10_titles.md`, `20_outlines.md` — the finalize-by-Friday deliverables.
- `30_…`, `40_…`, `50_…`, `60_…` — the sourced section briefs.
- `references.bib`, `reference_registry.csv`, `70_bibliography_report.md`.
- `00_target_journal_brief.md` — digested *Sensors* requirements.
- `PATCH_NOTES.md` (+ `NOTES.md`) — what ran, models/effort/cost, and what to
  improve next.

## 8. Logs & producing patches
Each run writes `logs\run_<timestamp>\` with per-stage `*.json` / `*.result.md` /
`*.err.txt`, a `costs.jsonl`, and a human `MODEL_EFFORT_LOG.md` (the table of
model/effort/status/cost/seconds you asked to keep for patching). To improve one
part later, re-run just that stage, e.g. to deepen the digital-twin evidence:

    .\run.ps1 -OnlyStage 50 -Force

Then re-run Stages 70 and 80 to fold the new sources into the bibliography and the
deliverable:

    .\run.ps1 -OnlyStage 70,80 -Force

## 9. If a stage fails
The run stops and tells you the resume command (`-FromStage <n>`). Look at
`logs\run_<timestamp>\<stage>.err.txt`. Common causes: a stage hit `MaxTurns`
(raise it in `$Stages`), or a transient network/search issue (just re-run it).
Add `-ContinueOnError` if you'd rather it push through failures.

## 10. Notes & troubleshooting
- **Fable availability:** the preflight pings Fable 5; if your account can't reach
  it, Fable stages automatically fall back to Opus and a warning is logged — the
  run still completes. Fix the id in `$FableModel` or your plan, then re-run those
  stages with `-Force`.
- **Safeguards routing:** some Fable 5 requests may be served by Opus 4.8 via
  Anthropic's safeguards routing. If a log shows that, it's expected, not a bug.
- **Execution policy:** if PowerShell blocks the script, either use the
  `-ExecutionPolicy Bypass` form above, or `Set-ExecutionPolicy -Scope Process
  Bypass` once in your session.
- **`python` not found:** the HTML step is skipped with a warning; your markdown
  outputs are unaffected. Install Python or run with `-SkipHtml`.
- **Time/cost:** titles + outlines (stages 10–20) are quick and cheap — run those
  first for your Friday deadline (`.\run.ps1 -OnlyStage 10,20`), review, then let
  the full literature review run.
