#!/usr/bin/env python3
"""Pre-quarantine confirmed India-origin records and create the mandatory full-audit queue."""
import argparse, datetime, json, pathlib, re

ROOT=pathlib.Path(__file__).resolve().parents[1]
LEDGER=ROOT/"90_BIBLIOGRAPHY"/"sources.json"

# Confirmed from the existing record's organization/affiliation text. Multinational academic
# papers are deliberately absent: the user permits Indian co-authors when a non-Indian affiliation
# is independently verified.
KNOWN_INDIA_ORIGIN={
 "L01-006","L01-010","L01-026","L02-003","L02-008","L04-024","L04-105",
 "L05-025","L05-051","L08-023", # all-India academic authorships in stored metadata
 "L01-041","L04-037","L06-047","L07-033","L07-048","L09-035","L11-036",
 "L12-043","L13-034","L13-051","L14-052","L16-021", # India-origin organizations/claims
 "L01-042","L01-054","L03-054","L08-028","L11-053" # India-only claims retained as leads
}
PATTERN=re.compile(r"\b(India|Indian|IIT|IISc|BARC|RRCAT|DRDO|ISRO|ITER[- ]India|Bhabha|Raja Ramanna)\b",re.I)

def read(path): return json.loads(path.read_text(encoding="utf-8-sig"))
def write(path,obj): path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def quarantine(s):
    original=s.get("source_type")
    s["accepted"]=False; s["source_type"]="discovery_only"; s["tier"]="discovery"
    s["rejection_reason"]="india_origin_exclusion: confirmed India-origin or India-only underlying technical claim; discovery/search lead only"
    s["india_origin_audit"]={
      "status":"excluded_india_origin","audited_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
      "rule":"Entirely India-origin sources are ineligible; multinational academic coauthorship is allowed when a non-Indian affiliation is verified.",
      "evidence_urls":[x for x in (s.get("url"),s.get("peer_review_evidence_url")) if x],
      "original_source_type":original
    }
    s["notes"]=(str(s.get("notes") or "")+" | Quarantined by 2026-07 India-origin rule; may be used only to discover an independent eligible source.").strip()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--apply-known",action="store_true"); args=ap.parse_args()
    data=read(LEDGER); accepted_before=sum(x.get("accepted") is True for x in data)
    queue=[]; excluded=[]
    for s in data:
        text=" ".join(str(s.get(k) or "") for k in ("title","authors_or_org","url","claim_supported","locator","notes"))
        if s.get("accepted") is True and ("IN" in (s.get("geography") or []) or PATTERN.search(text)):
            queue.append(s.get("id"))
        if args.apply_known and s.get("id") in KNOWN_INDIA_ORIGIN and s.get("accepted") is True:
            quarantine(s); excluded.append(s.get("id"))
    if args.apply_known:
        write(LEDGER,data)
        by_id={x.get("id"):x for x in data}
        for path in sorted((ROOT/"10_SOURCE_ATLAS").glob("L*_verified_sources.json")):
            lane=read(path); changed=False
            for i,s in enumerate(lane):
                if s.get("id") in excluded: lane[i]=by_id[s.get("id")]; changed=True
            if changed: write(path,lane)
    report={"policy":{"exclude":"Entirely India-origin source or India-only underlying technical claim","allow":"Multinational academic paper with at least one verified non-Indian co-author affiliation"},"canonical_records":len(data),"accepted_before":accepted_before,"prequarantined_ids":sorted(excluded),"priority_manual_audit_queue":sorted(set(queue)),"full_audit_required":True}
    write(ROOT/"05_STATE"/"INDIA_SOURCE_ORIGIN_PREFILTER.json",report)
    md=["# India source-origin prefilter","",f"- Canonical records: {len(data)}",f"- Accepted before: {accepted_before}",f"- Confirmed records quarantined now: {len(excluded)}",f"- Priority affiliation/origin queue: {len(set(queue))}","","This is a prefilter, not the P2A completion audit. Every accepted record still requires an origin/affiliation verdict before P3.","","## Prequarantined IDs","",", ".join(f"`{x}`" for x in sorted(excluded))]
    (ROOT/"05_STATE"/"INDIA_SOURCE_ORIGIN_PREFILTER.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(f"INDIA ORIGIN PREFILTER canonical={len(data)} accepted_before={accepted_before} quarantined={len(excluded)} priority_queue={len(set(queue))} applied={args.apply_known}")

if __name__=="__main__": main()
