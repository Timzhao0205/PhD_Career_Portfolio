#!/usr/bin/env python3
"""Create relevance-first, quota-complete source packs for the frozen top 10."""

from __future__ import annotations

import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
PRIMARY = {
    "buyer_tender", "buyer_specification", "procurement_award", "company_filing",
    "earnings_transcript", "official_project_award", "direct_customer_documentation",
}


def main() -> int:
    selection = json.loads((ROOT / "30_SCREENING" / "P5_SELECTION.json").read_text(encoding="utf-8-sig"))
    final = {row["idea_id"]: row for row in selection["final_24"]}
    ledger = [
        row for row in json.loads((ROOT / "90_BIBLIOGRAPHY" / "sources.json").read_text(encoding="utf-8-sig"))
        if row.get("accepted")
    ]
    by_id = {row["id"]: row for row in ledger}
    packs: list[dict] = []
    for iid in selection["top_10_deep_dives"]:
        idea = final[iid]
        chosen = list(dict.fromkeys(idea["source_ids"]))
        candidates = [
            row for row in ledger
            if row["id"] not in chosen and (
                iid in (row.get("idea_ids") or [])
                or idea["primary_lane"] in (row.get("lane_ids") or [])
            )
        ]
        candidates.sort(key=lambda row: (
            0 if iid in (row.get("idea_ids") or []) else 1,
            0 if row.get("source_type") == "academic_peer_reviewed" else 1,
            0 if row.get("demand_evidence_type") in PRIMARY else 1,
            0 if row.get("tier") == "T1" else 1,
            row["id"],
        ))

        def counts() -> tuple[int, int, int]:
            refs = [by_id[source_id] for source_id in chosen]
            return (
                len(refs),
                sum(row.get("source_type") == "academic_peer_reviewed" for row in refs),
                sum(row.get("demand_evidence_type") in PRIMARY for row in refs),
            )

        for need in ("peer", "demand", "total"):
            for row in candidates:
                if row["id"] in chosen:
                    continue
                total, peer, demand = counts()
                if need == "peer" and peer >= 7:
                    break
                if need == "demand" and demand >= 5:
                    break
                if need == "total" and total >= 20:
                    break
                if need == "peer" and row.get("source_type") != "academic_peer_reviewed":
                    continue
                if need == "demand" and row.get("demand_evidence_type") not in PRIMARY:
                    continue
                chosen.append(row["id"])
        total, peer, demand = counts()
        if total < 20 or peer < 7 or demand < 5:
            raise SystemExit(f"source-pack deficit {iid}: total={total} peer={peer} demand={demand}")
        packs.append({
            "idea_id": iid,
            "concept": idea["concept"],
            "primary_lane": idea["primary_lane"],
            "source_ids": chosen,
            "counts": {"total": total, "peer_reviewed": peer, "primary": demand},
            "sources": [
                {
                    key: by_id[source_id].get(key)
                    for key in ("id", "title", "authors_or_org", "year", "url", "source_type", "tier", "demand_evidence_type", "claim_supported", "locator")
                }
                for source_id in chosen
            ],
        })
    output = {
        "artifact": "P6_SOURCE_PACKS",
        "status": "curated_starting_packs",
        "policy": "Agents must use at least 20 accepted records, seven peer-reviewed technical records, and five primary buyer/competitor/geography records; they may add or replace records only from the accepted ledger.",
        "packs": packs,
    }
    path = ROOT / "40_DEEP_DIVES" / "P6_SOURCE_PACKS.json"
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"P6 source packs built: {len(packs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
