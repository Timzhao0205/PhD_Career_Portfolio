#!/usr/bin/env python3
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "90_BIBLIOGRAPHY" / "sources.json"
REQUIRED = {
    "id","title","authors_or_org","year","url","canonical_key","source_type","tier",
    "lane_ids","idea_ids","accessed_at","fetched","language","geography",
    "peer_review_status","peer_review_evidence_url","doi","demand_evidence_type",
    "claim_supported","locator","accepted","rejection_reason","notes"
}

def fail(msgs):
    print("SOURCE VALIDATION FAIL")
    for m in msgs: print(f"- {m}")
    return 1

def main():
    if not LEDGER.exists(): return fail([f"missing {LEDGER.relative_to(ROOT)}"])
    try: data = json.loads(LEDGER.read_text(encoding="utf-8-sig"))
    except Exception as e: return fail([f"invalid JSON: {e}"])
    if not isinstance(data, list): return fail(["ledger root must be a JSON array"])
    errors, seen, accepted = [], {}, []
    valid_types = {"academic_peer_reviewed","buyer_procurement","company_filing","government","national_lab","standard","regulator","market_industry","vendor_datasheet","trade_press","patent","discovery_only"}
    if len(data) < 720: errors.append(f"reviewed canonical records {len(data)} < 720")
    for i, s in enumerate(data):
        if not isinstance(s, dict): errors.append(f"row {i} is not object"); continue
        missing = REQUIRED - set(s)
        if missing: errors.append(f"row {i} missing {sorted(missing)}")
        key = str(s.get("canonical_key", "")).strip().lower()
        if not key: errors.append(f"row {i} empty canonical_key")
        elif key in seen and s.get("accepted"): errors.append(f"duplicate accepted key {key}: rows {seen[key]},{i}")
        else: seen[key] = i
        if s.get("accepted") is True:
            accepted.append(s)
            for field in ("lane_ids","idea_ids","geography"):
                if not isinstance(s.get(field), list): errors.append(f"accepted {s.get('id')} {field} must be array")
            if not s.get("fetched"): errors.append(f"accepted {s.get('id')} not fetched")
            if s.get("tier") not in ("T1","T2","T3"): errors.append(f"accepted {s.get('id')} invalid tier")
            if s.get("source_type") not in valid_types: errors.append(f"accepted {s.get('id')} invalid source_type")
            url=str(s.get("url","")).lower()
            if any(host in url for host in ("arxiv.org","ssrn.com","biorxiv.org","medrxiv.org")):
                errors.append(f"accepted {s.get('id')} uses preprint URL")
            if s.get("source_type") == "academic_peer_reviewed":
                if s.get("peer_review_status") != "verified": errors.append(f"{s.get('id')} peer review unverified")
                if not s.get("peer_review_evidence_url"): errors.append(f"{s.get('id')} lacks peer-review evidence URL")
                if not (s.get("doi") or s.get("url")): errors.append(f"{s.get('id')} lacks DOI/publisher URL")
    n = len(accepted)
    peer = sum(s.get("source_type") == "academic_peer_reviewed" and s.get("peer_review_status") == "verified" for s in accepted)
    primary_demand_types = {"buyer_tender","buyer_specification","procurement_award","company_filing","earnings_transcript","official_project_award","direct_customer_documentation"}
    demand = sum(s.get("demand_evidence_type") in primary_demand_types for s in accepted)
    gov = sum(s.get("source_type") in ("government","national_lab","standard","regulator") for s in accepted)
    industry = sum(s.get("source_type") in ("market_industry","vendor_datasheet","trade_press") for s in accepted)
    asia = sum(any(g in (s.get("geography") or []) for g in ("CN","JP","KR","TW","IN","SG")) for s in accepted)
    local = sum(any(g in (s.get("geography") or []) for g in ("CN","JP","KR","TW","IN")) and s.get("language") not in ("en","English",None,"") for s in accepted)
    t1 = sum(s.get("tier") == "T1" for s in accepted); t12 = sum(s.get("tier") in ("T1","T2") for s in accepted)
    thresholds = [(n,600,"accepted"),(peer,360,"peer-reviewed"),(demand,120,"primary demand"),(gov,60,"government/standards"),(industry,60,"market/industry"),(asia,80,"Asia"),(local,40,"local-language Asia")]
    for val, req, label in thresholds:
        if val < req: errors.append(f"{label} {val} < {req}")
    if n and t1/n < .70: errors.append(f"T1 share {t1/n:.1%} < 70%")
    if n and t12/n < .90: errors.append(f"T1+T2 share {t12/n:.1%} < 90%")
    if errors: return fail(errors[:100])
    print(f"SOURCE VALIDATION PASS reviewed={len(data)} accepted={n} peer={peer} demand={demand} gov={gov} industry={industry} asia={asia} local_asia={local} T1={t1}")
    return 0

if __name__ == "__main__": sys.exit(main())
