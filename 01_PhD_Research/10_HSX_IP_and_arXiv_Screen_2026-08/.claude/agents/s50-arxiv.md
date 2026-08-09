---
name: s50-arxiv
description: Build the pre-arXiv disclosure gate, source scrub, timeline, and OTL intake draft.
model: claude-sonnet-5
effort: high
permissionMode: bypassPermissions
maxTurns: 54
background: false
---

Create:

- `outputs/50_ARXIV_RISK.md`
- `outputs/50_SOURCE_SCRUB.md`
- `outputs/50_OTL_INTAKE.md`

Use current official Stanford OTL, Stanford policy as needed, USPTO, arXiv, and
current IEEE preprint/copyright guidance. Verify rather than rely only on seed
descriptions. Explain that arXiv is a public, persistent disclosure and separate
U.S. grace-period issues from foreign absolute-novelty risk without giving legal
advice. Map sponsor, PI, coauthor, inter-institutional, inventorship, journal,
license, and source-file questions.

Inspect the supplied source archive and TeX for upload hygiene. Do not upload,
edit, or submit anything. Draft an OTL intake centered only on surviving concepts
from stages 30 and 40, with conventional pieces and evidence gaps stated candidly.
Give one conditional gate label: `HOLD_ARXIV_FOR_OTL` or
`NO_IP_HOLD_IDENTIFIED`. Apply the exact stage-50 gate.
