# Stage 70 - Bibliography: verify, dedupe, format

Read every `refs_raw/*.jsonl` file (00_seed plus each stage's log). Your job is to
turn the accumulated raw references into a clean, verified bibliography. Do NOT
add new topical claims; work only with references already collected (you MAY do
targeted WebFetch/lookups to VERIFY or complete an existing reference's metadata).

Steps:
1. **Load & dedupe** - merge all entries; collapse duplicates (same DOI, or same
   title+year). Keep the richest record; unify to one citation key per work
   (AuthorYYYYkeyword). Track which stage(s)/section(s) each is used in.
2. **Verify** - for entries with `verify_doi:true` or a missing DOI, resolve via
   Crossref (https://api.crossref.org/works?query.bibliographic=...) or the
   publisher page. Confirm authors, year, venue, volume, pages/article-number,
   and DOI. Fix mistakes. If a DOI cannot be confirmed, leave it blank and set a
   note - never insert an unverified DOI.
3. **Classify peer-review status** - mark each: peer-reviewed journal / peer-
   reviewed conference / edited book / **standard** / **preprint** / **vendor /
   grey**. For any preprint, try once more to find the peer-reviewed version of
   record and prefer it; if none exists, keep the preprint flagged.
4. **Write outputs**:
   - `outputs/references.bib` - BibTeX for all confirmed entries, formatted for
     MDPI *Sensors* (follow the reference-style notes in
     `outputs/00_target_journal_brief.md`; include DOI fields; standards as
     @misc/@techreport with the issuing body). Sort by citation key.
   - `outputs/reference_registry.csv` - columns: key, authors, year, title,
     venue, type, doi, url, peer_reviewed, status, sections_used, confidence,
     notes. One row per work.
   - `outputs/70_bibliography_report.md` - a short QA report: total count; counts
     by status; a **flagged list** of everything NOT peer-reviewed (preprints,
     vendor, grey, standards) with a one-line note on how it's used and whether a
     peer-reviewed substitute is needed; any entries whose DOI/metadata could not
     be confirmed; and any duplicates you merged.

Accuracy over completeness: a smaller, fully-verified bibliography beats a larger
one with guessed DOIs. Finish by writing all three files.
