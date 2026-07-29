# Checkpoint — Stage 40 (`40_applications_collaboration`)

- Date: 2026-07-27
- Model/effort: Sonnet 5 / xhigh (per `MODEL_POLICY.md` — "applications/
  collaboration scoring: substantial judgment, but bounded by the
  Fable-reviewed technical analysis")
- Attempt: 1 (confirmed live via `state\attempts\40_applications_collaboration.json`;
  no prior partial attempt existed to resume — the generated effective
  prompt matched `prompts\40_applications_collaboration.md` verbatim)

## Gate status

- **PASS** — all 6 named/required application classes evaluated with
  evidence-based judgments: tokamak long-pulse, stellarator mapping,
  z-pinch/pulsed-power, MIF/plasma-jet, superconducting/HTS magnets &
  motors/generators, and accelerator magnets (the required 6th
  evidence-supported application, drawn from the stage-10C evidence base
  already showing mature Hall+coil+NMR prior art there, C29).
- **PASS** — scores do not override technical vetoes: z-pinch (C30),
  SC/HTS (C28), and accelerator magnets (C29 novelty) are hard-vetoed
  regardless of any strategic-score component; MIF carries a partial veto
  (C35, core region only). Validator confirms every `do-not-prioritize`
  row states a non-empty veto.
- **PASS** — candidate status current and linked to official pages: 10
  candidates across all 6 lanes, each with an `official_url` independently
  fetched/verified live on 2026-07-27 via 4 parallel research subagents
  plus one direct follow-up fetch I ran myself. Two exceptions honestly
  flagged rather than asserted: CERN's `te-msc-mm.web.cern.ch` (DNS
  resolution failure from this environment on every attempt, including my
  own direct WebFetch retry; search-engine-indexed as live) and the
  canonical `www.pppl.gov` domain (site-wide HTTP 403; mitigated with a
  live Google Sites NSTX-U mirror, independently verified).
- **PASS** — every approach-type recommendation (stellarator internal;
  tokamak external) carries a concrete, non-sent scientific ask and a
  named prerequisite (stage-30 gate G0/G1). Monitor/do-not-prioritize rows
  explicitly state no ask is recommended, which is the correct behavior
  for a vetoed or lower-priority lane, not an omission.
- **PASS** — no contact, submission, or external write occurred. Every
  `proposed_scientific_ask` cell is labeled "PROPOSED, NOT SENT"
  (validator-enforced); zero email addresses or phone-shaped strings in
  any of the 3 outputs (validator-enforced); all subagent research was
  explicitly briefed as read-only/discovery-only with no outreach.

## Completed outputs and row counts

- `outputs\04_APPLICATION_SCORECARD.csv` — 6 data rows, exact stage
  header (18 columns), parse-verified, rank is a clean 1..6 permutation.
- `outputs\04_COLLABORATION_STRATEGY.md` — scoring rubric/weights (§2),
  ranked recommendation table (§3), 6 per-application detail sections
  with prerequisites/asks/risks (§4), cross-cutting risks (§5), fallback
  path (§6), consistency statement (§7).
- `outputs\04_COLLABORATOR_CANDIDATES.csv` — 10 data rows, exact stage
  header (14 columns), parse-verified, rank is a clean 1..10 permutation,
  `group_or_facility` values unique.

## Searches/analyses completed

- Reused stage 10C/10D application evidence (`01_APPLICATIONS_ALTERNATIVES_REVIEW.md`,
  `evidence\10C_APPLICATION_SYNTHESIS.md`, evidence-map claims C27–C36)
  and stage 20/30 vetoes/architecture (Theorem 1, CASE A/F, tiers T0–T3,
  gates G0–G5, §9.4 HSX-decoupling) without repeating any prior search.
- 4 parallel general-purpose subagents (web search + web fetch, explicitly
  briefed read-only/discovery-only, no outreach) verified current official
  pages for 10 candidate groups across all 6 lanes. One follow-up direct
  WebFetch (by me, not a subagent) attempted to independently confirm the
  CERN group micro-site after the subagent reported DNS failure; confirmed
  the same failure, so the finding is recorded as unreachable-this-session,
  not silently dropped or guessed.
- Built and ran two deterministic CSV builder scripts and one output
  validator (all kept as reusable tools per `tools\`).

## Exact unresolved questions / limitations

1. CERN's TE-MSC Magnetic Measurements group micro-site
   (`te-msc-mm.web.cern.ch`) could not be independently fetched this
   session (DNS resolution failure on every URL variant tried, confirmed
   twice); its existence and mission are inferred from search-engine
   indexing and third-party (arXiv) citations, not directly read. No
   approach is recommended for this lane regardless (C29 novelty veto),
   so this limitation does not affect any actionable recommendation.
2. `www.pppl.gov` returned HTTP 403 to automated fetch for every page
   tried; the live NSTX-U Google Sites mirror was used instead. PPPL's
   historical stellarator-specific work (W7-X trim-coil contributions,
   NCSX/QUASAR) could not be matched to a currently active, independently
   verified PPPL stellarator program this session — NSTX-U (a spherical
   tokamak) was the most current verifiably active program found and is
   recorded under the tokamak lane, not mislabeled as stellarator.
3. LANL's specific Plasma Liner Experiment (PLX) page returned HTTP 404;
   a secondary-source signal (unconfirmed on an official page) suggests
   the program is mid-transition (commercialization/relocation call,
   September 2025). Recorded as an access-uncertainty factor, not asserted
   as fact.
4. No dedicated, named "WEST magnetic diagnostics team" page could be
   found at CEA/IRFM this session (a candidate service sub-page returned
   HTTP 500); this candidate is ranked lowest among the tokamak-lane
   entries specifically for that reason.
5. Numeric figures inherited from stage 10C remain unconfirmed at full
   text (JT-60SA 200°C/9 MGy, P006; Rogacki et al. ppm/mrad precision,
   P054) — flagged again here so they are not quoted as hard numbers in
   any stage-50/60/70/80 downstream synthesis without re-verification.

## Files safe to reuse

- `outputs\04_APPLICATION_SCORECARD.csv`, `outputs\04_COLLABORATION_STRATEGY.md`,
  `outputs\04_COLLABORATOR_CANDIDATES.csv` are final for this stage.
- `tools\build_04_application_scorecard.py`, `tools\build_04_collaborator_candidates.py`,
  `tools\validate_40_outputs.py` are reusable builders/validators (edit
  `ROWS`/checks and re-run rather than hand-editing CSV quoting).
- No scratch files were left outside `tools\`.

## Next action

Run/resume the parent launcher into `50_limitations_comparison` (model/
effort per `MODEL_POLICY.md`) — architecture limitations, failure modes,
prior-art constraints, and technology-comparison baseline, consuming the
10D evidence base, the stage-20 identifiability verdicts, the stage-30
architecture/tiers, and this stage's application/collaboration priorities
(notably: stellarator/HSX is the primary near-term venue; tokamak is the
strongest external-validation target once bench-proven; z-pinch, MIF,
SC/HTS-persistent-mode, and accelerator-magnet architecture-level novelty
are all vetoed and should not resurface as "market size" arguments in
later synthesis stages).
