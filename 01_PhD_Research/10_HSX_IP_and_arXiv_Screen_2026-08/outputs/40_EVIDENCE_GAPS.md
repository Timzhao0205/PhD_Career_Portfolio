# Stage 40 — Evidence Gaps That Could Change the Recommendation

Run: HSXIP-20260805T071311Z. Companion to `outputs/40_UHV_PACKAGE_VERDICT.md`.
Scope authority: `IP_SCOPE.md` ("Questions that materially affect the
strongest candidate"), `CLAUDE.md`, `schemas/OUTPUT_GATES.md` §40. Feature IDs
refer to `outputs/10_DISCLOSURE_MAP.csv`; source IDs to
`outputs/20_PRIOR_ART.csv` plus V40-A (defined in the verdict §9.2). This is
a research aid for the inventors/OTL conversation — not legal advice and not
a request the workflow itself may transmit externally (drafts and checklists
only, per `CLAUDE.md`).

## 0. Recommendation under test

Verdict §0: the module is not established as more than routine packaging;
C3 is held conditionally, with the hold resting almost entirely on
inventor-held evidence. Each gap below states what evidence would move that
recommendation, **in which direction**, and how far.

## 1. Gap register (mapped to `IP_SCOPE.md` inventor/OTL questions)

| ID | IP_SCOPE question | Evidence sought | Direction if found | Effect on recommendation | Refs |
|---|---|---|---|---|---|
| G1 | "Was there a documented failure mode or comparison without the shield?" | Arcing incident report, damaged/eroded epoxy on a prior unshielded probe or this module pre-shield; any with/without comparison, photos, shot logs | **Strengthens** (the only realistic unexpected-result / documented problem–solution evidence) | Converts obviousness posture from "predictable assembly" toward a supported non-obviousness argument; would justify presenting C3 to OTL as a substantive narrow candidate | F42; MPEP 2141/2143 (N001) |
| G2 | "Who conceived the grounded graphite shield … and when?" | Lab notebooks, e-mails, CAD/drawings with dates and named originators; whether conceived at Stanford, by UW-Madison HSX staff, or jointly | **Either.** Deliberate, documented conception with rationale strengthens; conception by facility staff applying standard HSX practice weakens toward screen-out and shifts inventorship/institutional control | Controls inventorship, which institution's OTL leads, and whether a filing is even Stanford's to make | F44; S002/S003 |
| G3 | "Are there drawings, photographs, dimensions, current paths…?" | Shield geometry, thickness, apertures, clearances, fastening, grounding route and resistance-to-ground | **Strengthens** (cures the enablement/support deficit; a distinguishing claim is not draftable without it). Note: this detail is *unpublished* — its handling has Stage 50 disclosure-timing consequences | Without G3, even a favorable G1 leaves no claimable specifics; with G3 alone (no G1), the claim is enabled but still obviousness-exposed | F40, F41 |
| G4 | (Implicit in geometry question) | Any design calculation tying shield conductivity/thickness to arc suppression **and** magnetic-field transmission bandwidth (skin-depth trade-off, verdict §4.4) | **Strengthens** — the strongest latent technical delta; would document an engineered, non-arbitrary parameter choice rather than a generic cover | Could support a parameter-limited claim (conductive-yet-field-transparent sacrificial cover) materially narrower but more defensible than the concept-level combination | F40, F45; N017 lead |
| G5 | (GDC exposure, implicit) "GDC exposure data" | GDC exposure logs: cycle count, cumulative hours, discharge current density, gas species; post-campaign inspection of shield and epoxy | **Either.** Documented exposure + intact epoxy strengthens (documented result under quantified stress). Evidence the module was removed/valved off during GDC, or that no GDC ran during the campaign, **weakens sharply** (collapses F17 and the shield's stated purpose to an untested precaution) | Determines whether the shield's protective function was ever actually exercised | F17, F46; V40-A, N008 |
| G6 | "What UHV acceptance criterion did the one-hour bake satisfy?" | HSX vacuum acceptance spec; RGA scans, leak-test, base-pressure records for the module | **Mildly either.** A quantified criterion + records improve enablement of F12; confirmation that the bake was simply the vendor cure performed in a vacuum oven confirms routineness (verdict §3) | Cannot rescue epoxy/bake as an independent candidate; affects only the quality of the record | F43; S022, N007 |
| G7 | (From Stage 30 §4) "float-vs-ground practice verification" | Facility documentation (any fusion lab) prescribing that in-vessel diagnostics be electrically **floated/isolated** during GDC *for their protection* | **Strengthens** (would be genuine teaching-away evidence against grounding a cover). Status: tested this stage and **currently unsupported** — V40-A (PDX 1979, primary) documents grounded-vs-floating GDC coupling physics and frames grounding as the strong-coupling configuration; the N008 float-philosophy snippet remains uncorroborated | Only a documented protective-floating practice would revive the teaching-away argument; absent it, obviousness risk stays high | Verdict §9.2; V40-A, N008 |
| G8 | (From Stage 30 §4) "W7-X panel grounding" | The 2013 companion paper "Thermal analysis of the Mirnov coils of Wendelstein 7-X" (ScienceDirect PII S0920379613005279 — paywalled, unresolved) or IPP engineering documentation stating whether the graphite caps/panels are electrically grounded | **Either.** Panels confirmed grounded → near-complete analog (grounded graphite over an in-vessel magnetic diagnostic in a stellarator) → **weakens toward screen-out**. Panels confirmed deliberately isolated → mild strengthen (field practice differs from F16) | The single cheapest external item that could still flip the novelty picture; verdict §9.1 records the partial resolution (coil center tap grounded; panel status open) | N017; verdict §9.1 |
| G9 | "Was it standard HSX/GDC engineering, adapted from an existing probe, or new?" | HSX internal drawings/photos of *other* in-vessel probes; whether grounded graphite covers pre-date this module at HSX | **Weakens to screen-out if pre-existing** (routine facility practice, likely also prior public use questions); strengthens modestly if demonstrably new to this module | Directly answers the routine-practice question the verdict could not close from the publication | F44; IP_SCOPE.md |
| G10 | "Earliest disclosure to people without confidentiality duties?" | Conference talks, posters, HSX operations reviews, theses, or facility reports showing the shield or module before `submission.pdf` (2026-07-02 working proxy) | **Either — but primarily a Stage 50 timing input.** Earlier public exposure of shield details weakens (prior disclosure); confirmation of no earlier exposure preserves options | Feeds the arXiv-gate timeline; also bears on foreign absolute novelty (S001/S002) | F44; S001, S006 |
| G11 | "Did UW-Madison personnel contribute to any potential claimed element?" | Statement from Goodman/Gallenberger/Geiger on package/shield/deployment contributions; HSX engineering sign-offs | **Either.** Substantive UW contribution changes inventorship and brings UW/DOE facility sponsorship terms into control; no contribution simplifies Stanford-side handling | Controls which OTL acts and under which sponsor terms (DOE DE-AC02-76SF00515, SLAC FWP 101264, NSF ECCS-2026822, TomKat — Acknowledgment, TeX L514) | F44; S003 |

## 2. What would flip the verdict — thresholds, both directions

**Flip toward "present C3 to OTL as a substantive (still narrow) filing
candidate":** at minimum **G1 + G2 + G3** (a documented no-shield
failure/comparison, conception records, and reproducible drawings). G4 or G5
(exposure-quantified survival) would further convert the record from
asserted-purpose to documented-result. Even then, expected claim scope
remains the §6 narrowest combination or narrower, with low design-around
resistance (verdict §7) — OTL should weigh filing cost against that scope.

**Flip toward outright screen-out (no publication-specific package
candidate):** any one of — G9 confirming the shield was pre-existing
HSX/standard facility practice; G8 confirming W7-X panels are grounded; G5
revealing the module was not actually GDC-exposed; or G2 revealing the
design was copied from an existing facility probe. Two or more of these
should end the hold without further inventor effort.

**No change:** inability to obtain inventor records at all leaves the
current posture (conditional hold, high obviousness risk, thin enablement) —
which per verdict §0 already carries the calibrated expectation of no
publication-specific filing case at Stages 60/70.

## 3. Status of externally checkable items after this stage

- **Resolved (primary source):** GDC arcing hazard, floating-potential
  magnitude, grounded-vs-floating coupling — V40-A (Dylla et al., PPPL 1979,
  OSTI 5515925, https://www.osti.gov/servlets/purl/5515925, verified_full
  this session). Teaching-away lead currently unsupported (G7).
- **Partially resolved:** W7-X grounding practice — N017 re-read confirmed
  the coils' center tap is grounded to the vessel
  (https://iopscience.iop.org/article/10.1088/1361-6587/abc395); the
  panels' own status remains open (G8). The open-access W7-X first-phase
  magnetics paper (pure.mpg.de item 2065910) was retrieved and contains no
  panel-grounding statement.
- **Open/blocked:** ScienceDirect PII S0920379613005279 (2013 Mirnov thermal
  analysis) — paywalled at this interface; obtainable via library access or
  an IPP author query. Recorded as an evidence limitation, not a blocker.

## 4. Minimum-evidence bundle for the OTL conversation (the concrete ask)

Request from the inventors, before any arXiv posting decision (Stage 50 sets
that gate): (1) G1 failure/comparison records; (2) G2 conception
who/when/why; (3) G3 drawings + grounding route; (4) G5 GDC exposure logs;
(5) G9 answer on pre-existing HSX practice; (6) G11 UW-Madison contribution
statement; (7) G10 earliest-disclosure inventory. Items (1)–(3) decide
whether C3 is worth OTL's time; items (5)–(7) decide who owns the decision
and how much time remains.
