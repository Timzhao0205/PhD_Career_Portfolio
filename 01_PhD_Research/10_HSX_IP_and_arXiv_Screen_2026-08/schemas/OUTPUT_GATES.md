# Stage acceptance gates

These gates prevent silent schema mismatch and scope drift. They contain no
arbitrary source-row quota.

## Global gates

- Every required file exists and is nonempty.
- All conclusions distinguish fact, inference, uncertainty, and action.
- Material factual and legal propositions have a direct URL/identifier.
- Excluded concepts from `IP_SCOPE.md` are not evaluated as manuscript IP.
- No output claims to be legal advice, an exhaustive search, or an FTO opinion.
- Model and performance fields are logged without invented telemetry.

## 00 scope

Files: `00_SCOPE_AUDIT.md`.

Must list all controlling artifacts, exact included technical groups, exclusions,
and any input-integrity issue. It must say whether unrelated archives were
absent/excluded and identify any publication source-file disclosure hazard.

## 10 disclosure

Files: `10_PUBLICATION_TECH.md`, `10_DISCLOSURE_MAP.csv`.

CSV columns:

`feature_id,manuscript_location,feature,disclosure_level,implemented,validated,authors_claim_novel,known_group_work,missing_enablement,commercial_use,notes`

Every device, package, readout, deployment, validation, and future-work feature
must be mapped. `disclosure_level` is one of `explicit`, `implicit`, `future`,
or `absent`.

## 20 prior art

Files: `20_PRIOR_ART.csv`, `20_SEARCH_LOG.md`.

The CSV must use `SOURCE_POLICY.md` exactly. Search log must show queries,
databases/sites, dates, family consolidation, coverage disposition, and a
saturation statement. `lead_only` rows cannot support final conclusions.

## 30 IP screen

Files: `30_IP_SCREEN.md`, `30_CLAIM_CHART.csv`.

The screen must separately answer:

1. Existing AlGaN/GaN Hall element/fabrication.
2. New use as an in-vessel fusion/stellarator diagnostic.
3. UHV/GDC module combination.
4. Readout chain.
5. Deployment/validation method.

For each: closest references, feature delta, novelty risk, obviousness risk,
enablement/support, practical claim value, inventorship questions, confidence,
and action. The claim chart is a research aid, not drafted legal claims.

CSV columns:

`candidate_id,concept,element_no,element,manuscript_support,closest_source,source_support,delta,novelty_risk,obviousness_risk,evidence_gap,disposition`

## 40 UHV/GDC package

Files: `40_UHV_PACKAGE_VERDICT.md`, `40_EVIDENCE_GAPS.md`.

Must distinguish conventional pieces from the asserted combination; test
whether epoxy plus bake alone is routine; evaluate whether the grounded graphite
shield contributes a non-obvious, documented result; examine magnetic,
electrical, thermal, GDC, vacuum, serviceability, and commercial value; and state
what evidence could change the recommendation.

## 50 arXiv/OTL gate

Files: `50_ARXIV_RISK.md`, `50_SOURCE_SCRUB.md`, `50_OTL_INTAKE.md`.

Must include a disclosure timeline, U.S./foreign distinction, sponsor/coauthor/
inventor questions, exact material exposed by PDF and TeX sources, source ZIP
hygiene, journal/copyright/license checks, and a binary `HOLD_ARXIV_FOR_OTL` or
`NO_IP_HOLD_IDENTIFIED` recommendation with conditions. It may not upload or
modify anything externally.

## 60 red team

File: `60_RED_TEAM.md`.

Must argue the best examiner/competitor case against each surviving candidate,
identify unsupported assumptions, propose the narrowest plausible surviving
combination, and say whether its commercial scope justifies filing expense.

## 70 final

Files: `70_FINAL_OTL_BRIEF.md`, `70_EXEC_SUMMARY.md`, `70_MODEL_REPORT.md`.

The Fable 5/xhigh final must lead with one of:

- `OTL_REVIEW_BEFORE_ARXIV`
- `NO_PUBLICATION_SPECIFIC_FILING_CASE_IDENTIFIED`
- `INSUFFICIENT_EVIDENCE_PAUSE`

It must answer the user's three questions about the Hall device, fusion use, and
UHV/GDC package; give a prioritized 48-hour/one-week action list; identify
inventorship/sponsor questions; separate strong, weak, and excluded concepts;
and state limitations. The model report reconciles requested versus observed
model/effort and all fallback events.
