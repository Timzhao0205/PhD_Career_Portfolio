# Target-journal brief — MDPI *Sensors* (ISSN 1424-8220)

Distilled from live MDPI pages, for the magnetic-field-sensors review. Only
what constrains this manuscript; skip generic marketing. Submission target:
before 30 Oct 2026.

## 1. Article type
*Review* is a standard MDPI article type across its journals and is listed
among *Sensors*' article types; the Instructions for Authors page does not
carve out extra structural mandates specific to reviews beyond "concise and
comprehensive" and full reproducibility of any reported methodology [MDPI
Sensors IfA; MDPI Sensors publguid]. No explicit systematic-review protocol
(e.g., PRISMA) is demanded — this can remain a narrative, vendor-neutral
review, not a systematic one.
**For us:** proceed with the narrative-review skeleton in `PROJECT_BRIEF.md`;
no PRISMA flow diagram needed.

## 2. Required structure
MDPI's standard template order is: title/author/affiliation front matter →
Abstract → Keywords → main body (Introduction ... Conclusions, numbered
headings, up to 3 levels) → back matter. Back matter for a review-type
paper (no primary human/animal data) is lighter than for a research article:
**Author Contributions, Acknowledgments (incl. any AI-tool disclosure per
§7), Conflicts of Interest, Abbreviations, References** — omit Institutional
Review Board/Informed Consent/Data Availability Statement unless we report
new experimental data of our own (we do not) [MDPI publguid; MDPI ethics
policy pages].
**For us:** end the manuscript with Author Contributions → Funding →
Acknowledgments (AI-tool line if applicable) → Conflicts of Interest →
Abbreviations → References. No IRB/data-availability boilerplate needed.

## 3. Abstract & keywords
- Keywords: **3–5**, placed immediately after the abstract [MDPI Sensors
  publguid].
- Abstract: single self-contained paragraph (MDPI does not mandate a
  structured/subheaded abstract for *Sensors*); should state
  problem/scope/method-of-review/key findings/implication in one block.
**For us:** write one ~200-250 word abstract paragraph, 4-5 keywords
(e.g., magnetic sensors; Hall effect; magnetoresistance; SQUID; sensor
fusion).

## 4. Reference style
- **In-text:** numbered, square brackets, placed **before** punctuation,
  e.g. `... noise floor [4].` or a range `[1–3]` [MDPI Sensors publguid].
- **Reference list**, MDPI/ACS numeric style (worked examples):
  - *Journal article:* `1. Surname, A.B.; Surname2, C.D. Title of article.
    Abbrev. J. Name Year, Volume, page-page or article no.
    https://doi.org/xx.xxxx/xxxxx.`
    Journal names are abbreviated per **ISO 4** — *but* one-word titles
    (e.g., *Sensors*, *Molecules*) are left unabbreviated [MDPI reference
    style guide v10].
  - *Conference paper:* `Surname, A.B. Title of Presentation. In
    Proceedings of the Name of the Conference, Location, Country, Day Month
    Year; Abstract/Paper No.` [MDPI reference style guide].
  - *Book chapter:* `Surname, A.B. Title of contribution. In Title of the
    Book, Edition; Editor1, E.; Editor2, E., Eds.; Publisher: City, Country,
    Year; Volume, pp. page-page; ISBN.` [MDPI reference style guide].
  - *Standard:* cite as a corporate-author reference, e.g. `International
    Organization for Standardization. ISO 26262-1:2018, Road Vehicles —
    Functional Safety — Part 1; ISO: Geneva, Switzerland, 2018.` (no
    established MDPI worked example for standards; this follows the
    book/report template MDPI recommends for institutional documents).
  - **DOI:** not mandatory but "highly encouraged" — include wherever it
    resolves [MDPI Sensors publguid].
**For us:** Stage 70 (bibliography formatting) must (a) keep one-word
journal titles unabbreviated, (b) abbreviate multi-word titles per ISO 4,
(c) always attach a verified DOI when one exists, (d) bracket + pre-
punctuation citation placement throughout all drafted sections.

## 5. Length / figures / tables
No stated maximum length — "no restrictions... provided the text is
concise and comprehensive" [MDPI Sensors IfA]. Figures: legend as a
separate paragraph before the figure; color figures published at no extra
cost. Tables: embedded in text with numbers/titles supplied [MDPI Sensors
publguid].
**For us:** a comparison table per §3 of the brief (sensor-family
range/resolution/bandwidth/cost/maturity) is normal MDPI review practice;
size the piece to the content (broad four-domain, three-section-thirds
plan implies a long review, which is acceptable here).

## 6. Formatting / template
MS Word (.dot template) is the primary route; a LaTeX class also exists in
MDPI's general author toolkit. SI units expected as standard scientific
convention (not itself stated as a Sensors-specific rule, but house style
across MDPI journals) [MDPI Sensors IfA].
**For us:** draft in Markdown/plain prose during Stages 30–80; convert to
the Word template only at final manuscript assembly (out of scope for this
run).

## 7. Ethics / policies
- **AI-assisted writing disclosure:** if generative AI (e.g., an LLM) is
  used to draft or edit any manuscript text, MDPI requires disclosure in
  the **Acknowledgments** section (tool name/version + purpose) and, where
  substantive, a description of use; authors retain full responsibility and
  the tool cannot be listed as an author [MDPI "Updated Guidelines on
  Artificial Intelligence and Authorship," mdpi.com/about/announcements/5687].
  Suggested wording: *"During the preparation of this manuscript, the
  author(s) used [tool, version] for [purpose]. The authors have reviewed
  and edited the output and take full responsibility for the content of
  this publication."*
- **Plagiarism/similarity:** MDPI screens all submissions (standard MDPI-
  wide policy; not *Sensors*-specific text retrieved this run, but binding
  regardless).
- **ORCID:** MDPI's submission system requests corresponding-author ORCID
  as standard practice across journals.
- **Preprint policy:** MDPI journals generally permit prior preprint
  posting (does not count as prior publication); consistent with this
  project's own preprint-then-cite-version-of-record rule.
**For us:** since this review will likely use an AI-assisted drafting
workflow, the final manuscript's Acknowledgments section MUST carry an
AI-disclosure line per the template above — flag this for the final
assembly stage (not this stage's job to write it, but note it now so it
isn't missed).

## 8. Practical
- **APC:** an article processing charge applies. Reported current 2026
  figure for *Sensors* is **CHF 2600** per accepted paper (open access);
  older/instructions-page figures citing CHF 1050 (+250 CHF English-editing
  surcharge) appear to be stale relative to the 2026 APC schedule — treat
  CHF 2600 as the operative number and re-verify at submission time, since
  APC pages update yearly [MDPI Sensors APC page; MDPI apc-2026 page].
- **Time to first decision:** median ~17.8 days to first decision, ~2.8
  days acceptance-to-publication, per *Sensors* first-half-2026 published
  figures [MDPI Sensors journal page metrics].
- **Special issues:** *Sensors* runs numerous open Special Issues
  (including recurring "Sensors in <year>" issues); submitting to a
  relevant Special Issue is optional and does not change the structural
  requirements above.
**For us:** no blocker to the 30 Oct 2026 target — turnaround is fast
relative to our timeline; APC budget should assume ~CHF 2600, confirm
before submission.

## Sources used (logged to refs_raw/00.jsonl)
- https://www.mdpi.com/journal/sensors/instructions
- https://mdpi.org/sensors/publguid.htm
- https://www.mdpi-res.com/data/mdpi-acs-references-guide-v10.pdf (via search)
- https://www.mdpi.com/about/announcements/5687
- https://www.mdpi.com/journal/sensors/apc
- https://www.mdpi.com/about/apc-2026
- https://www.mdpi.com/journal/sensors (metrics/scope, via search)
