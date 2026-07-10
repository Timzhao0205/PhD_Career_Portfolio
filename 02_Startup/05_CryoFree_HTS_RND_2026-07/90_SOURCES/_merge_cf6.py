import json

with open('90_SOURCES/sources.json', encoding='utf-8') as f:
    shared = json.load(f)

with open('60_PRIOR_ART/CF-6/sources.json', encoding='utf-8') as f:
    cf6 = json.load(f)

def conv(e):
    out = {
        "candidate": "CF-6",
        "id": e["id"],
        "tier": e["tier"],
        "jurisdiction": e["jurisdiction"],
        "type": e["source_type"],
    }
    if e.get("number"):
        out["number"] = e["number"]
    if e.get("title_original") and e.get("title_original") != e.get("title_translated"):
        out["title_original"] = e["title_original"]
        if e.get("title_translated"):
            out["title_translation"] = e["title_translated"]
    else:
        out["title"] = e.get("title_original")
    if e.get("assignee"):
        out["assignee"] = e["assignee"]
    if e.get("priority_date"):
        out["priority_date"] = e["priority_date"]
    if e.get("status"):
        out["status"] = e["status"]
    out["relevance_sentence"] = e["relevance_sentence"]
    if e.get("abstract_snippet_original"):
        out["abstract_original"] = e["abstract_snippet_original"]
    if e.get("abstract_snippet_translated"):
        out["abstract_translation"] = e["abstract_snippet_translated"]
    out["query_terms_that_found_it"] = e["query_terms_that_found_it"]
    return out

new_entries = [conv(e) for e in cf6]
shared["sources"].extend(new_entries)

with open('90_SOURCES/sources.json', 'w', encoding='utf-8') as f:
    json.dump(shared, f, ensure_ascii=False, indent=2)

print("appended", len(new_entries), "new total", len(shared["sources"]))
