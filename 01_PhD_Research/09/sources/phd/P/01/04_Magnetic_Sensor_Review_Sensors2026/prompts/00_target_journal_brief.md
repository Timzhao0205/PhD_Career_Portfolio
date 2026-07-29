# Stage 00 - Target-journal brief (MDPI *Sensors*)

Read `docs/PROJECT_BRIEF.md` first. Then use WebFetch/WebSearch to gather the
CURRENT author requirements for MDPI *Sensors* and distill what actually
constrains our manuscript. Prioritize these official pages (fetch them; do not
work from memory):
- https://www.mdpi.com/journal/sensors/instructions
- https://www.mdpi.com/journal/sensors  (aims & scope; article types incl. Review)
- the MDPI general "Instructions for Authors" and reference-style/template pages
  reachable from those.

Write `outputs/00_target_journal_brief.md` capturing ONLY what matters for us:
1. **Article type** - confirm *Review* is in scope; note any expectations MDPI
   states for reviews (comprehensiveness, structure, systematic vs narrative).
2. **Required structure** - the section order MDPI expects (front matter,
   abstract, keywords, Introduction ... Conclusions) and the mandatory back
   matter (Author Contributions, Funding, Institutional Review/《Data
   Availability》as applicable, Conflicts of Interest, Abbreviations, References).
3. **Abstract & keywords** - length/format norms (e.g. structured, single
   paragraph, self-contained; keyword count).
4. **Reference style** - exact in-text and list format with a worked example for
   a journal article, a conference paper, a book chapter, and a standard;
   bracket placement; DOI expectation; whether one-word journal titles are
   abbreviated. This governs how Stage 70 formats `references.bib`.
5. **Length / figures / tables** - any stated limits or norms for reviews.
6. **Formatting/template** - LaTeX vs Word template availability, line-numbering,
   units (SI), figure resolution.
7. **Ethics / policies** - similarity/plagiarism, data availability, AI-use
   disclosure, ORCID, preprint policy.
8. **Practical** - APC existence (state that a fee applies; do not assert a
   specific number unless the page shows it), typical time-to-first-decision if
   stated, and the special-issue option.

Keep it a tight, skimmable brief with a short "what this means for us" line under
each item. Cite each requirement with the URL you read it from. Log the pages you
used to `refs_raw/00.jsonl` as type "datasheet"/"[VENDOR]"-style publisher pages
(peer_reviewed:false) so we can trace them. Do not pad with generic MDPI
marketing. Finish by writing the file.
