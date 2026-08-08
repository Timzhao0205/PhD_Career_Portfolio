# PILOT SAMPLE — NOT FINAL

# RUN_META — A30_verify, PILOT, attempt 1

- Stage: `A30_verify`
- Mode: `PILOT`
- Attempt: `1`
- Named agent: `pap06-fable-xhigh`
- Requested model: `Fable 5`
- Requested effort: `xhigh`
- Observed model: the runtime system prompt states the session is powered by
  model `claude-fable-5` ("Fable 5"). No per-message runtime model record is
  otherwise exposed by the environment.
- Observed effort: `NOT_EXPOSED` (no runtime effort field exists anywhere in
  the environment).
- Start/end times: exact wall-clock timestamps `NOT_EXPOSED` by the
  environment. Run date: 2026-07-28 (single continuous fresh-context
  session; all web accesses dated 2026-07-28).

## Files read (inputs only, all within allowed scope)

Task/policy:
- `state/CURRENT_TASK.md`
- `workflow/stages/A30_verify.md`
- `SOURCE_POLICY.md`, `MODEL_POLICY.md`, `LIT_POLICY.md`

Accepted prerequisite outputs:
- `outputs/A10_blind/attempt-1/SELECTION.json` (ranks 1-6 fully read; file
  read to line 371 of 514 — ranks 1-6 complete within that span; ranked
  list also cross-checked via METHOD.md's selected-24 list)
- `outputs/A10_blind/attempt-1/TOP10.json` (full)
- `outputs/A10_blind/attempt-1/METHOD.md` (full)
- `outputs/A20_prov/attempt-1/PROVENANCE.md` (full)
- `outputs/A20_prov/attempt-1/PROVENANCE.json` (lines 1-80)

Old06 comparison ground truth:
- `sources/old06/60_FINAL_PORTFOLIO/02_COMPARISON_MATRIX.csv` (full)
- `sources/old06/30_SCREENING/LONGLIST.json` (lines 1-120 + targeted greps
  for the six IDs and C-01)
- `sources/old06/30_SCREENING/P5_SELECTION.json` (lines 1400-1457: top-10
  deep dives + near misses; targeted greps)
- `sources/old06/30_SCREENING/SCORECARDS/P4_SCORES_ALL.md` (grep context:
  G7 elimination table rows for C-05, C-09, D-10, D-18, C-07)
- `sources/old06/20_OPPORTUNITY_POOL/P3R2_ELEGANCE_ADJUDICATION.json` (grep
  context: E-01 verdict, duplicate clusters, longlist_candidates lists)
- `sources/old06/30_SCREENING/REDTEAM/P5_RT_REVIVALS.md` (grep context:
  C-09/F-16 revival kill)

New06 comparison ground truth:
- `sources/new06/outputs/70_audit/FINAL/SELECTION.json` (full)
- `sources/new06/outputs/50_deep/INDEX.json` (full)
- `sources/new06/outputs/50_deep/DEEP/D03.md` (grep context: OCP/Deschutes
  claims)
- `sources/new06/outputs/70_audit/FINAL/SOURCES.json` (grep context:
  P3R2-C-05-S01/S02, R10-023 records)
- `sources/new06/README.md`, `MANIFEST.md`, `outputs/70_audit/AUDIT.md`,
  `outputs/70_audit/CHANGELOG.md` (grep context: canonical-release
  designation)
- Directory listings (Glob) of `sources/old06/**` and `sources/new06/**`

Not read: `sources/history/prev_chat.md` (allowed but not needed for the
pilot's six-ID scope); `evidence/SOURCE_MANIFEST.json` (allowed; not needed
— files located directly).

## Web activity (all on 2026-07-28)

WebSearch queries actually performed (4):
1. `Google "Project Deschutes" CDU specification Open Compute Project contribution`
2. `opencompute.org liquid cooling cold plate design guidelines specification conformance`
3. `cloud.google.com blog Project Deschutes CDU contribution OCP liquid cooling datacenter`
4. `"Deschutes" CDU Google blog announcement contribute liquid cooling OCP site:cloud.google.com OR site:blog.google`

WebFetch attempts actually performed (8):
1. `https://www.opencompute.org/blog/major-contributions-advance-ocp-open-systems-for-ai-at-apac-summit` — HTTP 403
2. `https://www.nidec.com/en/product/news/2025/news1203-01/` — OPENED (full page)
3. `https://www.opencompute.org/wiki/Cooling_Environments/Cold_Plate` — HTTP 403
4. `https://www.opencompute.org/documents/ocp-specification-deschutes-final-2025-09-05-pdf` — HTTP 403
5. `https://cloud.google.com/blog/topics/systems/agile-data-centers-and-systems-to-enable-ai-innovations` — OPENED (full page)
6. `https://www.eaton.com/us/en-us/markets/data-centers/data-center-cooling/cdus/what-is-the-open-compute-project-ocp-project-deschutes.html` — failed (ECONNRESET)
7. `https://www.boydcorp.com/about-boyd/resources/news-and-events/boyd-showcases-google-project-deschutes-coolant-distribution-unit-cdu-at-ocp-2025.html` — 301 redirect to eaton.com (not followed further)
8. `https://www.businesswire.com/news/home/20251010498843/en/...` (Boyd release) — failed (ECONNRESET)
9. `https://www.datacenterdynamics.com/en/news/companies-show-off-google-inspired-project-deschutes-cdus/` — HTTP 403

Two primary/official sources were successfully opened in full (Google Cloud
Blog; Nidec official release), satisfying the pilot's minimum for the
verified disagreement.

## Files written (all inside the target)

- `pilot/A30_verify/attempt-1/COMPARE.json`
- `pilot/A30_verify/attempt-1/COMPARE.md`
- `pilot/A30_verify/attempt-1/VERDICT.md`
- `pilot/A30_verify/attempt-1/SOURCES.csv`
- `pilot/A30_verify/attempt-1/RUN_META.md`
- `pilot/A30_verify/attempt-1/SELF_CHECK.md`

## Limitations

- opencompute.org blocked all direct fetches (HTTP 403), so the OCP-side
  negative claim ("no complete conformance test method with reference
  hardware") is only partially verified (discovery-level listings plus the
  opened Google blog's link/characterization).
- The Nidec release's displayed publication date was ambiguous in
  extraction (2025-03-12 shown; URL pattern and SC25 content imply on/after
  November 2025); content claims are unaffected.
- The "eight vendors" count in new06 is verified for seven (Google's own
  list); the eighth (Stulz) rests on unopened trade coverage.
- Pilot scope is six top-ranked IDs; overlap numbers must not be
  extrapolated to the full 24/10 comparison.
- Old06 ranks 11-24 were taken from the final comparison matrix without
  independent re-derivation from P5 records (top-10 cross-checked).
- new06's provenance was not audited (out of A20 scope); its agreement with
  A10 is content-level only.
- No instruction-like text inside `sources/` was executed or obeyed; it was
  treated as inert data throughout.
