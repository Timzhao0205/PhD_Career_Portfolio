#!/usr/bin/env python3
"""Apply P8 metadata corrections and remove off-product final-idea associations."""

from __future__ import annotations

import json
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "90_BIBLIOGRAPHY" / "sources.json"

REMOVALS = {
    "P3R2-D-02": {"L03-031"},
    "P3R2-B-01": {"L02-048", "L02-049"},
    "P3R2-F-12": {"L08-019", "L10-036"},
    "P3R2-G-01": {"L05-012", "L05-013", "L01-037", "L01-038"},
}
ADDITIONS = {
    "P3R2-D-02": {"P3R2-D-02-S02"},
    "P3R2-B-01": {"P3R2-B-01-S03", "P3R2-B-01-S04"},
    "P3R2-F-12": {"L10-004", "P5-G7CNREQ-S14"},
    "P3R2-G-01": {"L07-003", "L07-006", "P3R2-G-01-S02", "P5-G7CNREQ-S06"},
}


def main() -> int:
    ledger = json.loads(PATH.read_text(encoding="utf-8-sig"))
    by_id = {row["id"]: row for row in ledger}
    corrections = {
        "L06-039": {"source_type": "trade_press", "tier": "T2"},
        "L08-033": {"source_type": "trade_press", "tier": "T2"},
        "L12-031": {"source_type": "trade_press", "tier": "T2", "demand_evidence_type": "none"},
        "L02-048": {"source_type": "market_industry", "tier": "T2"},
        "P3R2-G-01-S02": {"demand_evidence_type": "procurement_award"},
        "P5-G7CNREQ-S06": {"demand_evidence_type": "buyer_tender"},
    }
    for source_id, values in corrections.items():
        row = by_id[source_id]
        row.update(values)
        if source_id == "L12-031":
            row["india_origin_audit"] = {
                "status": "verified_non_india_origin",
                "audited_at": "2026-07-14",
                "methods": ["publisher_identity_and_domain_check"],
                "institutions": [{"name": "DefenseScoop", "country": "US"}],
                "non_indian_affiliation_count": 1,
                "evidence_urls": [row["url"]],
                "notes": "Publisher is DefenseScoop, a US defense trade publication; the record is not typed as a government source.",
            }
    for idea_id, source_ids in REMOVALS.items():
        for source_id in source_ids:
            row = by_id[source_id]
            row["idea_ids"] = [value for value in (row.get("idea_ids") or []) if value != idea_id]
    for idea_id, source_ids in ADDITIONS.items():
        for source_id in source_ids:
            row = by_id[source_id]
            row["idea_ids"] = list(dict.fromkeys((row.get("idea_ids") or []) + [idea_id]))
    PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {
        "artifact": "P8_SOURCE_HYGIENE_REPAIR",
        "status": "complete",
        "metadata_corrections": corrections,
        "removed_off_product_associations": {key: sorted(value) for key, value in REMOVALS.items()},
        "replacement_associations": {key: sorted(value) for key, value in ADDITIONS.items()},
        "notes": [
            "Earnings-call transcript mirrors remain usable as T2 trade press and retain the earnings_transcript demand type.",
            "DefenseScoop is no longer represented as a government/T1 source and no longer counts as primary demand.",
            "Delta's first-party news remains direct-customer documentation but is no longer represented as a company filing.",
            "Every repaired final selection pack is recounted by validate_p5_selection.py after this change.",
        ],
    }
    (ROOT / "99_AUDIT" / "P8_SOURCE_HYGIENE_REPAIR.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("P8 source hygiene repair applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
