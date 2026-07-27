"""Stage-30 output validator (reusable; mirrors tools/validate_10d_outputs.py).

Checks:
  1. All three stage-30 outputs exist and are nontrivial.
  2. Risk register parses, has the exact required header, unique risk_ids.
  3. Every evidence_id in the register resolves to a ledger source_id or an
     evidence-map claim_id.
  4. Every bracketed [Hxxx]/[Rxxx]/[Pxxx] source ID and every Cxx claim ID
     cited in the two stage-30 markdown files resolves likewise.
  5. Register enumerations (likelihood/impact/decision_gate) use the allowed
     vocabularies.
"""
import csv
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "outputs")

REQUIRED_HEADER = [
    "risk_id", "component", "mechanism", "radiation_or_environment",
    "observable_effect", "detectability", "compensation_possible",
    "reference_required", "likelihood", "impact", "evidence_ids",
    "mitigation", "validation_test", "residual_risk", "decision_gate",
]

FILES = {
    "arch": os.path.join(OUT, "03_RADIATION_COMPENSATION_ARCHITECTURE.md"),
    "plan": os.path.join(OUT, "03_SIMULATION_AND_VALIDATION_PLAN.md"),
    "risk": os.path.join(OUT, "03_RADIATION_RISK_REGISTER.csv"),
}

LIKELIHOOD_VOCAB_PREFIX = ("low", "medium", "high", "unknown")
IMPACT_VOCAB_PREFIX = ("low", "medium", "high", "unknown")
GATE_RE = re.compile(r"^G[0-7]$")

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


def main():
    valid_ids = load_valid_ids()
    print(f"loaded {len(valid_ids)} valid source+claim IDs")

    # 1. existence / nontriviality
    for key, path in FILES.items():
        exists = os.path.isfile(path)
        size = os.path.getsize(path) if exists else 0
        check(f"{key} exists and nontrivial", exists and size > 2000,
              f"{os.path.basename(path)} size={size}")

    # 2. register parse + header + uniqueness
    with open(FILES["risk"], encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    check("register header exact", header == REQUIRED_HEADER,
          "match" if header == REQUIRED_HEADER else f"got {header}")
    check("register row count", len(rows) >= 15, f"{len(rows)} rows")
    ids = [r[0] for r in rows]
    check("risk_id unique", len(ids) == len(set(ids)))
    check("all rows full-width", all(len(r) == len(REQUIRED_HEADER) for r in rows))

    # 3. evidence_ids resolve
    idx = REQUIRED_HEADER.index("evidence_ids")
    bad = []
    for r in rows:
        for eid in r[idx].split(";"):
            eid = eid.strip()
            if eid and eid not in valid_ids:
                bad.append((r[0], eid))
    check("register evidence_ids resolve", not bad, f"unresolved: {bad}" if bad else "all resolve")

    # 4. enum vocab + gates
    li = REQUIRED_HEADER.index("likelihood")
    im = REQUIRED_HEADER.index("impact")
    dg = REQUIRED_HEADER.index("decision_gate")
    bad_enum = [r[0] for r in rows
                if not r[li].startswith(LIKELIHOOD_VOCAB_PREFIX)
                or not r[im].startswith(IMPACT_VOCAB_PREFIX)
                or not GATE_RE.match(r[dg])]
    check("register enums/gates valid", not bad_enum, str(bad_enum) if bad_enum else "ok")

    # 5. markdown citations resolve
    id_re = re.compile(r"\[([HRP]\d{3})\]")
    claim_re = re.compile(r"\bC\d{2}\b")
    for key in ("arch", "plan"):
        text = open(FILES[key], encoding="utf-8").read()
        cited = set(id_re.findall(text))
        claims = set(c for c in claim_re.findall(text))
        bad_src = sorted(c for c in cited if c not in valid_ids)
        bad_claim = sorted(c for c in claims if c not in valid_ids)
        check(f"{key} source IDs resolve ({len(cited)} cited)", not bad_src,
              f"unresolved: {bad_src}" if bad_src else "all resolve")
        check(f"{key} claim IDs resolve ({len(claims)} cited)", not bad_claim,
              f"unresolved: {bad_claim}" if bad_claim else "all resolve")

    print(f"\n{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES:", failures)
        sys.exit(1)


if __name__ == "__main__":
    main()
