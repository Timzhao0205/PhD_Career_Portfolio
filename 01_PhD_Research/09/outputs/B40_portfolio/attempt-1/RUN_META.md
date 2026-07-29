# RUN_META — B40_portfolio FULL attempt-1

- Stage: `B40_portfolio` | Mode: `FULL` | Attempt: `1`
- Target directory: `outputs/B40_portfolio/attempt-1/`
- Named agent (task card): `pap06-fable-xhigh`
- Requested model: `Fable 5`
- Requested effort: `xhigh`
- Observed runtime model: `claude-fable-5` (exposed in this session's system
  context as the exact model ID; recorded as observed evidence, kept separate
  from the request above)
- Observed runtime effort: `NOT_EXPOSED` (no runtime effort indicator exists
  in this session)
- Start time: `NOT_EXPOSED` (no runtime clock available; session date
  2026-07-28 per environment context)
- End time: `NOT_EXPOSED` (same basis)

## Sources consulted (read this run)

Task and policy layer:
- `state/CURRENT_TASK.md` (task card, hard gates)
- `workflow/stages/B40_portfolio.md` (stage specification)

Accepted pilot (method carried forward):
- `pilot/B40_portfolio/attempt-1/RANKING.csv`
- `pilot/B40_portfolio/attempt-1/DECISION.json`
- `pilot/B40_portfolio/attempt-1/PORTFOLIO.md`
- `pilot/B40_portfolio/attempt-1/SOURCES.csv`

Accepted prerequisite outputs (full evidence base):
- `outputs/B20_align/attempt-1/ALIGNMENT.csv` (all 39 rows, read in full)
- `outputs/B25_power/attempt-1/POWER_MAP.csv` (all 31 rows, read in full)
- `outputs/B25_power/attempt-1/POWER.md` (read in full)
- `outputs/B30_skills/attempt-1/BRIDGES.json` (read in full)
- `outputs/B30_skills/attempt-1/PREP_PLAN.md` (read in full)
- `outputs/B15_lit_synth/attempt-1/GAPS.md` (read in full)
- `outputs/B15_lit_synth/attempt-1/LIT_REVIEW.md` (read to §2.1; the
  sections this stage leans on — audit chain, stream adjudication basis —
  plus GAPS.md in full; EV-row content otherwise consumed via B20/B25's
  accepted carrying, disclosed in SOURCES.csv rows B40-22..25)
- `outputs/A30_verify/attempt-1/COMPARE.json` (read in full)
- `outputs/A30_verify/attempt-1/VERDICT.md` (read in full)
- `outputs/A30_verify/attempt-1/SOURCES.csv` (rows C09-DIS-02/03 opened to
  transcribe exact URLs for reuse rows)
- `outputs/B20_align/attempt-1/SOURCES.csv` (rows S-B20-01/02/03, same
  purpose)
- `outputs/B25_power/attempt-1/SOURCES.csv` (rows S-B25-15..18, same
  purpose)
- `outputs/B10_phd/attempt-1/OPT2.md` (read in full)

## Web activity (all logged in SOURCES.csv)

1. WebFetch `new.abb.com/...sace-infinitus-solid-state-circuit-breaker` —
   FAILED (60s timeout; the third failed attempt across the pilot and this
   run). Logged as B40-01; the ABB shipping claim stays discovery-level.
2. WebSearch "SAES Getters NEG coating US capacity accelerator vacuum
   chambers 2025 2026" — discovery-level only; no US-capacity announcement
   found (A-05's kill trigger not visibly fired); logged as B40-02; no page
   opened.
3. WebSearch "OCP liquid cooling CDU conformance program test methodology
   reference hardware 2026" — discovery-level only; corroborates OCP
   test-methodology/qualification white papers, no complete conformance
   program with reference hardware surfaced; opencompute.org not re-fetched
   (known 403 pattern per A30); logged as B40-03; no page opened.

No other fetches or searches were made. All other current-market claims are
reused opened primaries (original claim IDs and non-re-opening disclosed per
row) or internal prerequisite-output evidence.

## Limitations

- The ABB SACE Infinitus shipping claim (pressing C-01/A-02) could not be
  verified after three fetch attempts; scoring treats merchant-SSCB pressure
  as window-pressure, not window-collapse.
- Eight OLD→NEW decision reversals (A-05, A-22, D-19, D-16, D-09, F-16,
  F-19, plus the C-12 gate flip) remain unverified at primary level (A30);
  affected ranks carry 1.0 bands and the affected rejections say so.
- The two searches this run are discovery aids only; no searched page was
  opened, and search-level absence is never treated as proof of absence.
- The base ranking contains two exact score ties resolved by stated
  judgment; sensitivity analysis shows the C-05/D-09 pair flips under two
  weight variants — the full flip record is in DECISION.json.
- Old06 decision-layer provenance is CONTRADICTED (A20); new06 runtime is
  unaudited; all agreement statistics are content agreement, not provenance
  evidence.
- Folder-08-derived estimator claims are pre-redteam (C40); every score
  touching them inherits that status.
- This stage is research planning and strategic screening, not legal,
  safety, export, or certification advice (SOURCE_POLICY).

## Model/effort evidence note

Requested model/effort come from the task card and are recorded above
verbatim. The only runtime-observed identity evidence available to this
session is the system-context model ID (`claude-fable-5`); no runtime effort
evidence exists (`NOT_EXPOSED`). The two kinds of evidence are kept separate
per MODEL_POLICY discipline.
