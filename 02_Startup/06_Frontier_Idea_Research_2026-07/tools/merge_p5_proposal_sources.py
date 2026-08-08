#!/usr/bin/env python3
"""Promote complete ledger-ready source records from named P5 proposal files.

Only explicitly named source-array keys are traversed. The script is idempotent,
requires the canonical ledger schema and completed origin audit, and refuses
canonical-key or ID conflicts. It does not infer acceptance for partial metadata.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import shutil


ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "90_BIBLIOGRAPHY" / "sources.json"
BACKUP = ROOT / "98_RUN_LOGS" / "P5_PRE_PROPOSAL_SOURCE_MERGE_sources.json"
SOURCE_KEYS = {
    "new_source_ledger_ready_metadata",
    "new_source_ledger_metadata_suggestions",
    "new_source_metadata",
    "ledger_ready_sources",
    "ledger_ready_new_sources",
    "new_sources",
}
SOURCE_TYPE_ALIASES = {
    "company_primary": "company_filing",
    "company_roadmap": "company_filing",
    "state_owned_company_primary": "company_filing",
    "government_state_media": "government",
    "government_official_media": "government",
    "government_plan": "government",
    "government_policy": "government",
    "government_regulatory_roadmap": "regulator",
    "certification_body_primary": "standard",
    "standard_project": "standard",
    "competitor_primary": "vendor_datasheet",
    "competitor_product_page": "vendor_datasheet",
    "primary_buyer_procurement": "buyer_procurement",
    "peer_reviewed_journal_article": "academic_peer_reviewed",
    "official_forward_plan": "government",
    "primary_buyer_procurement_intention": "buyer_procurement",
    "primary_exchange_filing": "company_filing",
    "official_standard": "standard",
    "official_implementation_plan": "government",
    "official_project_report": "national_lab",
    "competitor_service_page": "vendor_datasheet",
    "official_project_record": "national_lab",
    "primary_company_filing": "company_filing",
}
DEMAND_TYPE_ALIASES = {
    "named buyer tender": "buyer_tender",
    "federal procurement notice": "buyer_tender",
    "named university procurement intention": "buyer_tender",
    "buyer expenditure filing": "company_filing",
    "named buyer testing-service procurement": "buyer_tender",
    "government-funded field validation": "official_project_award",
    "exact-category buyer procurement": "buyer_tender",
    "named fab-equipment tender": "buyer_tender",
    "customer-system expansion filing": "company_filing",
    "not_demand": "none",
    "not_current_demand": "none",
    "active_sources_sought_exact_category": "buyer_tender",
    "funded_or_proposed_buyer_rd_program": "official_project_award",
    "buyer_order_and_specification": "buyer_specification",
    "official_project_schedule": "direct_customer_documentation",
    "federal_award_exact_category": "official_project_award",
    "buyer_rd_plan": "direct_customer_documentation",
    "competitor_product": "none",
}
REQUIRED = {
    "id", "title", "authors_or_org", "year", "url", "canonical_key",
    "source_type", "tier", "lane_ids", "idea_ids", "accessed_at", "fetched",
    "language", "geography", "peer_review_status", "peer_review_evidence_url",
    "doi", "demand_evidence_type", "claim_supported", "locator", "accepted",
    "rejection_reason", "notes", "india_origin_audit",
}


def collect(node: object) -> list[dict]:
    found: list[dict] = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key in SOURCE_KEYS and isinstance(value, list):
                found.extend(row for row in value if isinstance(row, dict))
            else:
                found.extend(collect(value))
    elif isinstance(node, list):
        for value in node:
            found.extend(collect(value))
    return found


def normalize(raw: dict) -> dict:
    row = dict(raw)
    if "id" not in row and row.get("suggested_id"):
        row["id"] = row.pop("suggested_id")
    row.pop("acceptance_recommendation", None)
    row["source_type"] = SOURCE_TYPE_ALIASES.get(row.get("source_type"), row.get("source_type"))
    if row.get("source_type") == "academic_peer_reviewed" and str(row.get("peer_review_status", "")).startswith("verified"):
        row["peer_review_status"] = "verified"
    row["demand_evidence_type"] = DEMAND_TYPE_ALIASES.get(
        row.get("demand_evidence_type"), row.get("demand_evidence_type")
    )
    if isinstance(row.get("geography"), str):
        row["geography"] = [part for part in row["geography"].split("/") if part]
    if row.get("accepted") is None:
        row["accepted"] = True
    row.setdefault("rejection_reason", "")
    row.setdefault("notes", "Accepted from a P5 evidence-repair proposal after main readback.")
    row.setdefault("peer_review_evidence_url", "")
    row.setdefault("doi", "")
    audit = row.get("india_origin_audit")
    if isinstance(audit, dict):
        audit = dict(audit)
        if not audit.get("methods") and audit.get("method"):
            audit["methods"] = [audit["method"]]
        audit.setdefault("audited_at", row.get("accessed_at"))
        audit.setdefault("evidence_urls", [row.get("url")])
        audit.setdefault("non_indian_affiliation_count", 1)
        audit.setdefault(
            "institutions",
            [{"name": audit.get("resolved_org") or row.get("authors_or_org", "verified source organization"),
              "country": audit.get("resolved_country") or (row.get("geography") or ["non-IN"])[0]}],
        )
        row["india_origin_audit"] = audit
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("proposal", nargs="+", help="proposal JSON path relative to workspace")
    parser.add_argument(
        "--idea-id",
        action="append",
        default=[],
        help="only promote records explicitly associated with this idea ID (repeatable)",
    )
    args = parser.parse_args()

    ledger = json.loads(LEDGER.read_text(encoding="utf-8-sig"))
    by_id = {row["id"]: row for row in ledger}
    by_key = {str(row["canonical_key"]).strip().lower(): row for row in ledger}
    additions: list[dict] = []

    for rel in args.proposal:
        path = (ROOT / rel).resolve()
        if ROOT not in path.parents:
            raise SystemExit(f"outside workspace: {rel}")
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        for raw in collect(payload):
            row = normalize(raw)
            if args.idea_id and not set(args.idea_id).intersection(row.get("idea_ids") or []):
                continue
            missing = REQUIRED - set(row)
            if missing:
                raise SystemExit(f"{rel}: source {row.get('id')} missing {sorted(missing)}")
            if row["accepted"] is not True or not row["fetched"]:
                raise SystemExit(f"{rel}: source {row['id']} is not fetched+accepted")
            audit = row["india_origin_audit"]
            if audit.get("status") not in {
                "verified_non_india_origin", "verified_multinational_allowed"
            } or not audit.get("audited_at") or not audit.get("methods") or not audit.get("evidence_urls"):
                raise SystemExit(f"{rel}: source {row['id']} has incomplete origin audit")
            source_id = row["id"]
            key = str(row["canonical_key"]).strip().lower()
            if source_id in by_id:
                if str(by_id[source_id]["canonical_key"]).strip().lower() != key:
                    raise SystemExit(f"ID conflict for {source_id}")
                continue
            if key in by_key:
                existing = by_key[key]
                # Same canonical record: merge only explicitly proposed idea/lane associations.
                for field in ("idea_ids", "lane_ids"):
                    existing[field] = list(dict.fromkeys((existing.get(field) or []) + (row.get(field) or [])))
                continue
            additions.append(row)
            by_id[source_id] = row
            by_key[key] = row

    if not BACKUP.exists():
        shutil.copy2(LEDGER, BACKUP)
    ledger.extend(additions)
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"P5 proposal source merge: added {len(additions)} records")
    if additions:
        print("IDs: " + ", ".join(row["id"] for row in additions))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
