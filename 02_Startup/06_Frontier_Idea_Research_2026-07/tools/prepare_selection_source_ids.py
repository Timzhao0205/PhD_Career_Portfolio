#!/usr/bin/env python3
"""Populate P5 selection rows with their explicit canonical longlist source IDs.

The script does not invent same-lane substitutions. It reports any remaining quota
deficits so a human/agent can add concept-specific sources deliberately.
"""

from __future__ import annotations

import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
SELECTION = ROOT / "30_SCREENING" / "P5_SELECTION.json"
LONGLIST = ROOT / "20_OPPORTUNITY_POOL" / "ideas.json"
SOURCES = ROOT / "90_BIBLIOGRAPHY" / "sources.json"
PRIMARY_DEMAND = {
    "buyer_tender", "buyer_specification", "procurement_award", "company_filing",
    "earnings_transcript", "official_project_award", "direct_customer_documentation",
}


def main() -> int:
    if not SELECTION.exists():
        print(f"missing {SELECTION.relative_to(ROOT).as_posix()}")
        return 1
    payload = json.loads(SELECTION.read_text(encoding="utf-8-sig"))
    longlist = {
        row["idea_id"]: row
        for row in json.loads(LONGLIST.read_text(encoding="utf-8-sig"))
    }
    source_by_id = {
        row["id"]: row
        for row in json.loads(SOURCES.read_text(encoding="utf-8-sig"))
        if row.get("accepted")
    }
    deficits: list[str] = []
    for row in payload.get("final_24", []):
        iid = row["idea_id"]
        idea = longlist.get(iid)
        if not idea:
            deficits.append(f"{iid}: absent from canonical longlist")
            continue
        explicit: list[str] = []
        for key in ("demand_source_ids", "technical_source_ids", "competitor_source_ids"):
            explicit.extend(idea.get(key) or [])
        existing = row.get("source_ids") or []
        row["source_ids"] = [
            source_id
            for source_id in dict.fromkeys([*existing, *explicit])
            if source_id in source_by_id
        ]
        refs = [source_by_id[source_id] for source_id in row["source_ids"]]
        peer = sum(source.get("source_type") == "academic_peer_reviewed" for source in refs)
        demand = sum(source.get("demand_evidence_type") in PRIMARY_DEMAND for source in refs)
        if len(refs) < 12 or peer < 5 or demand < 3:
            deficits.append(f"{iid}: total={len(refs)} peer={peer} demand={demand}")

    SELECTION.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"updated {SELECTION.relative_to(ROOT).as_posix()}")
    if deficits:
        print("CONCEPT-SPECIFIC SOURCE DEFICITS")
        for deficit in deficits:
            print(f"- {deficit}")
        return 2
    print("all final-24 explicit source quotas pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
