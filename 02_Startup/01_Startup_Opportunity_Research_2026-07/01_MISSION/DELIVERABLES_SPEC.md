# DELIVERABLES SPEC & ACCEPTANCE CHECKLIST

Final tree (auditor verifies every box):

```
01_Startup_Opportunity_Research_2026-07/
├── 05_STATE/
│   ├── MASTER_STATE.json          [ ] mission == "COMPLETE", all phases "complete"
│   ├── PROGRESS_LOG.md            [ ] timestamped entry per phase & wave
│   └── ASSUMPTIONS.md             [ ] exists (even if short)
├── 10_PHASE1_LANDSCAPE/           [ ] 10 domain briefs D01–D10 + 10 *_sources.json
├── 20_PHASE2_CANDIDATES/
│   ├── CANDIDATES.md              [ ] ≥ 36 candidates, template-complete
│   └── candidates.json            [ ] parses; matches CANDIDATES.md
├── 30_PHASE3_SCORING/
│   ├── SCORING_MATRIX.md / .csv   [ ] every candidate scored on all 11 criteria + gates
│   ├── REDTEAM_Cxx.md × 15        [ ] bear case per top-15 idea
│   └── SELECTION.md               [ ] top 12 + diversity-rule confirmation
├── 40_PHASE4_DEEPDIVES/           [ ] 12 reports, all 10 sections, ≥14 sources each
├── 50_PHASE5_POLICY/POLICY_BRIEF.md [ ] ≥25 sources, current-dated, both-language sourcing
├── 60_PHASE6_SYNTHESIS/
│   ├── 00_EXECUTIVE_SUMMARY.md    [ ] Top-7 ranking + comparison table + recommendation logic
│   ├── 01_ROADMAP_2026_2030.md    [ ] quarterly plan with decision gates
│   └── 02_FULL_RANKING.md         [ ] all candidates, final scores
├── 90_BIBLIOGRAPHY/
│   ├── sources.json               [ ] ≥200 unique; schema-valid; tier mix per SOURCE_STANDARDS
│   └── BIBLIOGRAPHY.md            [ ] human-readable, grouped by tier, zh titles bilingual
└── 99_AUDIT/FINAL_AUDIT.md        [ ] all checks pass incl. 20-link re-fetch verification
```

Style: direct, math-forward, precise; numbers with units and dates; no filler. Markdown tables
where they clarify. Every file self-contained enough to read alone.
