# Literature-review policy

Operation B uses a required two-stage evidence block:

1. `B12_lit_search` uses Sonnet 5/high for reproducible searching,
   de-duplication, publisher/DOI checks, peer-review verification, and
   correction/retraction screening.
2. `B15_lit_synth` uses Fable 5/xhigh to independently accept or correct B12,
   weight evidence, resolve contradictions, identify gaps, and determine
   applicability to the PhD and startup questions.

## Method boundary

Use PRISMA-inspired reporting: preserve query strings, dates, result counts,
screening decisions, exclusions, duplicates, and a flow summary. PRISMA 2020
is a reporting guideline with a 27-item checklist and flow diagrams; this
package does not call its targeted engineering evidence map a formal systematic
review or meta-analysis unless the full corresponding methods are performed.

Reference:
https://www.bmj.com/content/372/bmj.n71

## Accepted evidence

Accepted-core evidence consists only of verified peer-reviewed journal research
or review articles with publisher records. Peer-reviewed conference
proceedings may be supplementary when the specific venue process is verified.
Preprints, theses, patents, magazines, vendor documents, and other gray
literature may guide discovery or supply context but cannot satisfy the
accepted-core quota.

For each publication, verify title, year, venue, publication type, DOI when one
exists, publisher URL, peer-review status, correction status, retraction
status, accessibility, topic stream, and evidence role. A DOI, publisher brand,
or professional-looking PDF does not itself prove peer review.

## Measurement evidence

For Hall, coil, HTS, and power-electronics measurements, extract the measurand,
operating conditions, reference/calibration chain, repeatability,
reproducibility, uncertainty components, combined/expanded uncertainty when
reported, controls, sample size, limitations, and transferability. NIST
Technical Note 1297 is the package's general uncertainty-reporting reference;
it does not replace domain-specific standards.

Reference:
https://www.nist.gov/pml/nist-technical-note-1297

## Decision rule

Citation volume is not evidence strength. Fable must judge study design,
measurement quality, agreement across independent groups, applicability,
negative results, and boundary conditions. Retracted work cannot support an
accepted claim. Unresolved corrections, inaccessible evidence, or uncertain
peer-review status must remain limitations. Absence from the search is never
proof that prior art or contradictory evidence does not exist.
