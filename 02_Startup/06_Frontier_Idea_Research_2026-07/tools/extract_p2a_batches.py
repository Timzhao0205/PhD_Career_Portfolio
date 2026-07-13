"""Extract per-batch record files for the P2A india-origin audit.

Reads the audit queue and canonical ledger, writes one compact records file per
batch to 05_STATE/P2A_BATCHES/ so each auditor agent reads only its own batch.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> None:
    with open(os.path.join(ROOT, '05_STATE/INDIA_SOURCE_ORIGIN_AUDIT_QUEUE.json'), encoding='utf-8') as f:
        queue = json.load(f)
    with open(os.path.join(ROOT, '90_BIBLIOGRAPHY/sources.json'), encoding='utf-8') as f:
        data = json.load(f)
    recs = data['sources'] if isinstance(data, dict) and 'sources' in data else data
    # Duplicate IDs exist: an accepted DOI-keyed canonical record plus rejected
    # URL-keyed duplicates. Always prefer the accepted record for a given ID.
    by_id = {}
    for r in recs:
        cur = by_id.get(r['id'])
        if cur is None or (r.get('accepted') is True and cur.get('accepted') is not True):
            by_id[r['id']] = r

    out_dir = os.path.join(ROOT, '05_STATE/P2A_BATCHES')
    os.makedirs(out_dir, exist_ok=True)

    keep_keys = ['id', 'title', 'authors_or_org', 'year', 'url', 'canonical_key',
                 'source_type', 'tier', 'lane_ids', 'language', 'geography',
                 'peer_review_status', 'peer_review_evidence_url', 'doi',
                 'demand_evidence_type', 'claim_supported', 'notes']

    missing = []
    not_accepted = []
    total = 0
    for b in queue['batches']:
        out = []
        for sid in b['source_ids']:
            total += 1
            r = by_id.get(sid)
            if r is None:
                missing.append(sid)
                continue
            if r.get('accepted') is not True:
                not_accepted.append(sid)
            out.append({k: r.get(k) for k in keep_keys})
        path = os.path.join(out_dir, f"{b['batch_id']}_records.json")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({'batch_id': b['batch_id'], 'count': len(out), 'records': out},
                      f, ensure_ascii=False, indent=1)
        print(b['batch_id'], len(out))

    print('total queued:', total)
    print('missing from ledger:', missing)
    print('queued but not accepted:', len(not_accepted), not_accepted[:10])


if __name__ == '__main__':
    main()
