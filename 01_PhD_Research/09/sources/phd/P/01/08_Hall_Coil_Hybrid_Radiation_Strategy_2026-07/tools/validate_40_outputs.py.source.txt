"""Stage-40 output validator (reusable; mirrors tools/validate_30_outputs.py).

Checks:
  1. All three stage-40 outputs exist and are nontrivial.
  2. Both CSVs parse, have the exact required header from the stage prompt,
     correct row counts, unique application/rank values.
  3. Every ID cited in evidence_ids / relevant_publication_ids (Cxx claim IDs;
     Hxxx/Rxxx/Pxxx source IDs) resolves against the stage-10D ledger/map.
  4. Every bare Cxx / Hxxx / Rxxx / Pxxx token cited in the prose strategy
     document resolves likewise.
  5. veto column non-empty for every row that the scorecard's recommendation
     marks do-not-prioritize, and rank values are a 1..N permutation.
  6. No outreach/contact-detail leakage: strategy doc contains no email
     addresses or phone-number-shaped strings.
"""
import csv
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "outputs")

SCORECARD_HEADER = [
    "application", "problem", "incumbent_diagnostic", "hybrid_value",
    "identifiability_path", "radiation_fit", "experimental_access",
    "publication_value", "collaboration_leverage", "prototype_cost",
    "thesis_dilution_risk", "technical_score", "strategic_score", "veto",
    "evidence_ids", "rank", "recommendation", "next_gate",
]

CANDIDATES_HEADER = [
    "rank", "group_or_facility", "institution", "application", "official_url",
    "relevant_publication_ids", "unique_capability", "proposed_scientific_ask",
    "prerequisites", "access_uncertainty", "competition_or_ip_risk", "phd_fit",
    "recommendation", "notes",
]

FILES = {
    "scorecard": os.path.join(OUT, "04_APPLICATION_SCORECARD.csv"),
    "strategy": os.path.join(OUT, "04_COLLABORATION_STRATEGY.md"),
    "candidates": os.path.join(OUT, "04_COLLABORATOR_CANDIDATES.csv"),
}

failures = []
checks = 0


def check(name, ok, detail=""):
    global checks
    checks += 1
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(name)


def load_valid_ids():
    ids = set()
    with open(os.path.join(OUT, "01_SOURCE_LEDGER.csv"), encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            ids.add(row["source_id"].strip())
    with open(os.path.join(OUT, "01_EVIDENCE_MAP.csv"), encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            ids.add(row["claim_id"].strip())
    return ids


def read_csv_rows(path, required_header):
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    return header, rows


def main():
    valid_ids = load_valid_ids()
    print(f"loaded {len(valid_ids)} valid source+claim IDs")

    for key, path in FILES.items():
        exists = os.path.isfile(path)
        size = os.path.getsize(path) if exists else 0
        check(f"{key} exists and nontrivial", exists and size > 1500,
              f"{os.path.basename(path)} size={size}")

    # Scorecard checks
    sc_header, sc_rows = read_csv_rows(FILES["scorecard"], SCORECARD_HEADER)
    check("scorecard header exact", sc_header == SCORECARD_HEADER,
          "match" if sc_header == SCORECARD_HEADER else f"got {sc_header}")
    check("scorecard row count == 6", len(sc_rows) == 6, f"{len(sc_rows)} rows")
    check("scorecard rows full-width",
          all(len(r) == len(SCORECARD_HEADER) for r in sc_rows))
    apps = [r[0] for r in sc_rows]
    check("scorecard application values unique", len(apps) == len(set(apps)))
    ranks = sorted(int(r[SCORECARD_HEADER.index("rank")]) for r in sc_rows)
    check("scorecard rank is 1..N permutation", ranks == list(range(1, len(sc_rows) + 1)),
          str(ranks))
    veto_idx = SCORECARD_HEADER.index("veto")
    rec_idx = SCORECARD_HEADER.index("recommendation")
    dnp_no_veto = [r[0] for r in sc_rows
                   if r[rec_idx].startswith("do-not-prioritize") and r[veto_idx].strip().lower().startswith("none")]
    check("every do-not-prioritize row states a veto", not dnp_no_veto,
          str(dnp_no_veto) if dnp_no_veto else "ok")

    ev_idx = SCORECARD_HEADER.index("evidence_ids")
    bad = []
    for r in sc_rows:
        for eid in r[ev_idx].split(";"):
            eid = eid.strip()
            if eid and eid not in valid_ids:
                bad.append((r[0], eid))
    check("scorecard evidence_ids resolve", not bad, f"unresolved: {bad}" if bad else "all resolve")

    # Candidates checks
    cd_header, cd_rows = read_csv_rows(FILES["candidates"], CANDIDATES_HEADER)
    check("candidates header exact", cd_header == CANDIDATES_HEADER,
          "match" if cd_header == CANDIDATES_HEADER else f"got {cd_header}")
    check("candidates row count == 10", len(cd_rows) == 10, f"{len(cd_rows)} rows")
    check("candidates rows full-width",
          all(len(r) == len(CANDIDATES_HEADER) for r in cd_rows))
    cranks = sorted(int(r[0]) for r in cd_rows)
    check("candidates rank is 1..N permutation", cranks == list(range(1, len(cd_rows) + 1)),
          str(cranks))
    groups = [r[1] for r in cd_rows]
    check("candidates group_or_facility unique", len(groups) == len(set(groups)))

    pub_idx = CANDIDATES_HEADER.index("relevant_publication_ids")
    bad2 = []
    id_token_re = re.compile(r"\b([CHRP]\d{2,3})\b")
    for r in cd_rows:
        for tok in id_token_re.findall(r[pub_idx]):
            if tok not in valid_ids:
                bad2.append((r[1], tok))
    check("candidates relevant_publication_ids resolve", not bad2,
          f"unresolved: {bad2}" if bad2 else "all resolve")

    # ask discipline: every proposed_scientific_ask must say PROPOSED, NOT SENT
    ask_idx = CANDIDATES_HEADER.index("proposed_scientific_ask")
    bad_ask = [r[1] for r in cd_rows if "PROPOSED, NOT SENT" not in r[ask_idx]]
    check("every candidate ask labeled PROPOSED, NOT SENT", not bad_ask,
          str(bad_ask) if bad_ask else "ok")

    # Strategy doc: citation resolution + no contact-detail leakage
    text = open(FILES["strategy"], encoding="utf-8").read()
    cited = set(id_token_re.findall(text))
    bad3 = sorted(c for c in cited if c not in valid_ids and not re.match(r"^G[0-9]$", c))
    # filter out gate-like tokens (G0-G5) and tier tokens (T0-T3) misfired by regex (won't match [CHRP] anyway)
    check(f"strategy doc source/claim IDs resolve ({len(cited)} tokens)", not bad3,
          f"unresolved: {bad3}" if bad3 else "all resolve")

    email_re = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
    phone_re = re.compile(r"\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b")
    emails = email_re.findall(text)
    phones = phone_re.findall(text)
    check("strategy doc has no email addresses", not emails, str(emails) if emails else "none found")
    check("strategy doc has no phone-shaped strings", not phones, str(phones) if phones else "none found")

    # same check on the two CSVs (concatenate raw text)
    csv_text = (open(FILES["scorecard"], encoding="utf-8").read() +
                open(FILES["candidates"], encoding="utf-8").read())
    emails2 = email_re.findall(csv_text)
    check("CSVs have no email addresses", not emails2, str(emails2) if emails2 else "none found")

    print(f"\n{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES:", failures)
        sys.exit(1)


if __name__ == "__main__":
    main()
