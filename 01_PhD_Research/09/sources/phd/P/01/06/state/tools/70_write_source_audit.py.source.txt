"""Stage 70: generate outputs/07_SOURCE_AUDIT.csv from the sample report
plus the manual/deterministic audit rows."""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

rep = json.load(open(ROOT / "state/tools/70_sample_report.json", encoding="utf-8"))
led = {r["source_id"]: r for r in csv.DictReader(
    open(ROOT / "outputs/01_SOURCE_LEDGER.csv", encoding="utf-8-sig"))}

rows = []
counter = 0


def rid():
    global counter
    counter += 1
    return f"AUD{counter:03d}"


BENIGN = {
    "S0054": "em-dash vs '--' transliteration only",
    "S0055": "venue abbreviation 'J. Mater. Chem. C' = 'Journal of Materials Chemistry C'",
    "S0169": "em-dash vs '--' transliteration only",
    "S0192": "en-dash vs hyphen in 'Grad-Shafranov' only",
}

for i in rep:
    sid = i["source_id"]
    r = led[sid]
    claimed = (f"title='{r['title'][:80]}'; year={r['year']}; "
               f"venue={r['venue']}; first_author={i['led_first_author']}")
    if "cr_title" in i:
        verified = (f"title='{i['cr_title'][:80]}'; years={i['cr_years']}; "
                    f"venue={i['cr_venue']}; first_author_family={i['cr_first_author']}; "
                    f"type={i['cr_type']}")
    else:
        verified = "FETCH FAILED"
    if not i["flags"]:
        res, note = "match", f"stratum={i['stratum']}; tier={i['tier']}; access={i['access']}"
    else:
        res = "match_after_adjudication"
        note = (f"stratum={i['stratum']}; tier={i['tier']}; access={i['access']}; "
                f"flag {i['flags']} adjudicated benign: {BENIGN.get(sid, '')}")
    rows.append([rid(), sid, "bibliographic_identity",
                 "title/year/venue/first_author/doi", claimed, verified,
                 f"https://api.crossref.org/works/{r['doi']}", res, "none",
                 "none", note])

EXTRA = [
    ("S0068", "content_fulltext",
     "notes: 15,473 useful pulses; +/-0.07% cal. stability std dev (compensated)",
     "15,473 useful pulses; +/-0.07% compensated / +/-0.1% uncompensated std dev",
     "https://iopscience.iop.org/article/10.1088/1741-4326/ac8aad",
     "match", "none", "none",
     "Open-access IOP full text confirms both; ledger note correctly reflects the "
     "compensated figure. Abstract also confirms Oct 2009 - Mar 2021 (11+ yr), "
     ">19,000 pulses, hybrid coil+Hall Luenberger-Kalman proposal. Most "
     "load-bearing precedent in the ledger."),
    ("S0128", "verbatim_quote",
     "notes verbatim quote: 'HSX is the first and only stellarator experiment "
     "optimized for quasi-helical symmetry (QHS)'",
     "identical sentence present in the article introduction (IOP page fetched 2026-07-25)",
     "https://iopscience.iop.org/article/10.1088/1361-6587/adb179",
     "match", "none", "none",
     "Load-bearing for the stage-30 QHS-wording recommendation; independently "
     "confirmed this stage."),
    ("S0002", "content_secondary",
     "notes: tolerance to 1e13 cm-2 at 380 keV proton dose; 400C operation",
     "phys.org and ScienceDaily (2012) report the same numbers; publisher "
     "abstract remains elided/blocked",
     "https://phys.org/news/2012-03-hall-effect-magnetic-field-sensors.html",
     "consistent_secondary_only", "none", "none",
     "Ledger verification_basis honestly records snippet-level basis. Do not "
     "quote these numbers in a manuscript table without primary-PDF "
     "confirmation (existing stage-10D rule already covers this)."),
    ("", "prior_art_patent",
     "PA-P01 US9389284B2: Active, anticipated expiration 2029-04-09, Infineon",
     "Google Patents 2026-07-25: status Active; expiration 2029-04-09; "
     "assignee Infineon Technologies AG",
     "https://patents.google.com/patent/US9389284B2/en",
     "match", "none", "none", "Spot-check of stage-50 patent-row accuracy."),
    ("", "external_policy",
     "03 route decision 4.1: SENSL 4-page max incl. reference column; "
     "'Submission-to-ePublication = 4.8 weeks, median'; sensor-centric scope",
     "live page 2026-07-25 quotes all three verbatim",
     "https://ieee-sensorsletters.org/information-for-authors/",
     "match", "none", "none", "Stage-30 policy claim re-verified live."),
    ("", "external_policy",
     "03 route decision 4.3: RSI refuses papers covering material previously "
     "published in any peer-reviewed journal; considers material previously "
     "published but not yet peer-reviewed",
     "both sentences verbatim in Internet Archive snapshot (2025-11-15) of the "
     "official page; live page Cloudflare-403",
     "https://web.archive.org/web/20251115144142/https://pubs.aip.org/aip/rsi/pages/policies",
     "match", "none",
     "annotation added to 03_PUBLICATION_ROUTE_DECISION.md 4.3 (correction F-7)",
     "Open gate from stage 30 closed. Snapshot also adds: 'A previously "
     "published instrument is not considered to be novel' - sharpens the "
     "Route-C novelty requirement; recorded in the same annotation. Re-check "
     "the live page before actual submission."),
    ("", "external_policy",
     "06 roadmap [EE]: Stanford EE reading committee in year 3; University "
     "Oral Exam in year 4",
     "official EE degree-progress pages confirm both",
     "https://ee.stanford.edu/academics/graduate-degree-progress",
     "match", "low",
     "links added to 06_24_MONTH_PHD_ROADMAP.md header (correction F-4)",
     "Claims were correct but cited no URL anywhere in stage-60 outputs. "
     "Second URL: https://ee.stanford.edu/academics/graduate-degree-progress/oral-exam"),
    ("", "deterministic_schema",
     "01_SOURCE_LEDGER.csv: 231 rows; exact 16-col header; unique sequential "
     "IDs; unique normalized DOIs/titles; all verified_peer_reviewed; no "
     "disallowed types; enums/years valid",
     "independent script state/tools/70_audit_ledger.py: PASS on all checks",
     "", "PASS", "none", "none",
     "Fresh audit script; does not reuse 10d_validate.py logic."),
    ("", "deterministic_crossref",
     "All inline [S####](doi) citation links across outputs match ledger "
     "DOIs; all output CSVs parse; all relative links resolve",
     "276/276 links match; 9/9 CSVs single-width; 97/97 links resolve "
     "(state/tools/70_audit_crossrefs.py)",
     "", "PASS", "none", "none",
     "Two scanner false-positive classes documented (Elsevier PII DOIs; PFR "
     "article number S2054 inside row S0090's citation string)."),
    ("", "sampling_coverage",
     "Stratified sample design: >=30 rows across topic groups, years, tiers, "
     "access levels",
     "36 rows; 9/9 lane-x-access cells; 7/7 year bands (1971-2026); tiers "
     "A21/B12/C3; 7/7 SOURCE_POLICY topic groups; deterministic md5 rule "
     "(state/tools/70_sample_verify.py)",
     "", "PASS", "none", "none",
     "Sampling rule independent of the stage-10D 32-DOI sample; 36/36 "
     "identity-verified."),
]

for sid, at, claim, ver, url, res, sev, corr, note in EXTRA:
    rows.append([rid(), sid, at, at, claim, ver, url, res, sev, corr, note])

out = ROOT / "outputs/07_SOURCE_AUDIT.csv"
with open(out, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow("audit_id,source_id,audit_type,field_checked,claimed_value,"
               "verified_value,verification_url,result,severity,"
               "required_correction,notes".split(","))
    w.writerows(rows)
print(f"wrote {out.name} with {len(rows)} data rows")

with open(out, encoding="utf-8", newline="") as f:
    rr = list(csv.reader(f))
print("widths:", dict(Counter(len(x) for x in rr)))
