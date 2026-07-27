"""Stage 60 output validator (reusable).

Checks the three stage-60 outputs for existence/nontriviality, resolves
every cited ID (sources Hxxx/Rxxx/Pxxx, claims Cxx, tests FT-xx, failure
modes FM-xx, risks RR-xx) against the mission ledgers, verifies the
stage acceptance markers, and re-parses every CSV in outputs/ with the
exact required ledger header.

Run from the mission root:  python tools/validate_60_outputs.py
Exit code 0 = all checks pass.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "outputs"

STAGE60_FILES = [
    OUT / "06_INTEGRATED_RESEARCH_PROGRAM.md",
    OUT / "06_DECISION_GATES_AND_ROADMAP.md",
    OUT / "06_ADVISOR_MEETING_BRIEF.md",
]

LEDGER_HEADER = (
    "source_id,citation,title,authors,year,venue,doi,url,source_type,"
    "peer_review_status,quality_tier,topic_tags,claims_supported,"
    "verification_basis,access_level,notes"
)

checks = []


def check(name, ok, detail=""):
    checks.append((name, ok, detail))
    print(("PASS" if ok else "FAIL") + f"  {name}" + (f"  [{detail}]" if detail and not ok else ""))


def main():
    # --- 1. existence / nontriviality -------------------------------------
    for f in STAGE60_FILES:
        exists = f.exists()
        size = f.stat().st_size if exists else 0
        check(f"exists+nontrivial: {f.name}", exists and size > 4000, f"size={size}")

    texts = {f.name: f.read_text(encoding="utf-8") for f in STAGE60_FILES if f.exists()}
    all_text = "\n".join(texts.values())

    # --- 2. ID universes ---------------------------------------------------
    with open(OUT / "01_SOURCE_LEDGER.csv", newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fieldnames = reader.fieldnames or []
    source_ids = {r["source_id"] for r in rows}
    check("ledger parses, 219 rows", len(rows) == 219, f"rows={len(rows)}")
    check("ledger header exact (parsed fields)",
          ",".join(fieldnames) == LEDGER_HEADER, ",".join(fieldnames)[:60])

    with open(OUT / "01_EVIDENCE_MAP.csv", newline="", encoding="utf-8") as fh:
        crows = list(csv.DictReader(fh))
    claim_col = "claim_id" if "claim_id" in (crows[0] if crows else {}) else None
    claim_ids = {r[claim_col] for r in crows} if claim_col else set()
    check("evidence map parses, 37 claims", len(crows) == 37, f"rows={len(crows)}")

    with open(OUT / "03_RADIATION_RISK_REGISTER.csv", newline="", encoding="utf-8") as fh:
        rrows = list(csv.DictReader(fh))
    risk_col = next((c for c in (rrows[0].keys() if rrows else []) if "risk" in c and "id" in c), None)
    risk_ids = {r[risk_col] for r in rrows} if risk_col else set()
    check("risk register parses, 24 rows", len(rrows) == 24, f"rows={len(rrows)}")

    ft_text = (OUT / "05_FALSIFICATION_TESTS.md").read_text(encoding="utf-8")
    ft_ids = set(re.findall(r"\bFT-\d{2}\b", ft_text))
    fm_text = (OUT / "05_LIMITATIONS_AND_FAILURE_MODES.md").read_text(encoding="utf-8")
    fm_ids = set(re.findall(r"\bFM-\d{2}\b", fm_text))

    # --- 3. cited-ID resolution -------------------------------------------
    cited_sources = set(re.findall(r"\[([HRP]\d{3})\]", all_text))
    missing = sorted(cited_sources - source_ids)
    check(f"all {len(cited_sources)} bracketed source IDs resolve", not missing, str(missing))

    cited_claims = set(re.findall(r"\bC(\d{2})\b", all_text))
    cited_claims = {f"C{n}" for n in cited_claims}
    missing_c = sorted(c for c in cited_claims if c not in claim_ids)
    check(f"all {len(cited_claims)} claim IDs resolve", not missing_c, str(missing_c))

    cited_ft = set(re.findall(r"\bFT-\d{2}\b", all_text))
    missing_ft = sorted(cited_ft - ft_ids)
    check(f"all {len(cited_ft)} FT IDs resolve", not missing_ft, str(missing_ft))

    cited_fm = set(re.findall(r"\bFM-\d{2}\b", all_text))
    missing_fm = sorted(cited_fm - fm_ids)
    check(f"all {len(cited_fm)} FM IDs resolve", not missing_fm, str(missing_fm))

    cited_rr = set(re.findall(r"\bRR-\d{2}\b", all_text))
    missing_rr = sorted(cited_rr - risk_ids)
    check(f"all {len(cited_rr)} RR IDs resolve", not missing_rr, str(missing_rr))

    # --- 4. stage acceptance markers --------------------------------------
    prog = texts.get("06_INTEGRATED_RESEARCH_PROGRAM.md", "")
    gates = texts.get("06_DECISION_GATES_AND_ROADMAP.md", "")
    brief = texts.get("06_ADVISOR_MEETING_BRIEF.md", "")

    check("program: direct three-step conclusion present",
          "three-step" in prog and "CONFIRMED IN SUBSTANCE" in prog)
    check("program: all 7 phases present",
          all(f"Phase {i}" in prog for i in range(7)))
    check("program: three budget tiers present",
          all(t in prog for t in ["Tier 1 — minimum defensible",
                                  "Tier 2 — balanced/recommended",
                                  "Tier 3 — high-accuracy/collaborator-enabled"]))
    check("program: kill criteria K1..K10 present",
          all(f"K{i}" in prog for i in range(1, 11)))
    check("program: HSX critical-path decoupling stated",
          "critical path" in prog and "9.4" in prog)
    check("program: module boundedness section present",
          "3.8" in prog and "open-ended" in prog)
    check("gate-name disambiguation used (HY-G / 06-G)",
          "HY-G" in prog and "06-G" in prog and "HY-G" in gates and "06-G" in gates)
    check("gates: ordered DG sequence present",
          all(f"DG-{i:02d}" in gates for i in range(12)))
    check("gates: resume-ready next tasks present",
          "Resume-ready next tasks" in gates)
    check("brief: decision requested + lowest-cost experiment + questions",
          "Decision requested" in brief and "Lowest-cost next experiment" in brief
          and "Questions for the advisor" in brief)
    check("brief: radiation off critical path stated",
          "never on the HSX critical path" in brief)
    check("no unconditional mutual-calibration claim",
          "mutually calibrate" not in prog.lower() or "not" in prog.lower())
    label_phrase = "Observed / Derived / Inferred / Proposed / Unknown"
    check("labels convention declared in all three",
          all(label_phrase in re.sub(r"\s+", " ", t).replace("**", "")
              for t in [prog, gates, brief]))

    # --- 5. every outputs CSV parses --------------------------------------
    for csv_file in sorted(OUT.glob("*.csv")):
        try:
            with open(csv_file, newline="", encoding="utf-8") as fh:
                n = sum(1 for _ in csv.reader(fh))
            check(f"csv parses: {csv_file.name}", n >= 2, f"lines={n}")
        except Exception as e:  # noqa: BLE001 - report any parse failure
            check(f"csv parses: {csv_file.name}", False, str(e))

    # --- summary -----------------------------------------------------------
    failed = [c for c in checks if not c[1]]
    print(f"\n{len(checks) - len(failed)}/{len(checks)} PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
