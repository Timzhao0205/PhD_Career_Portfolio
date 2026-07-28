import json, collections, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
recs = json.load(open('90_BIBLIOGRAPHY/sources.json', encoding='utf-8'))
pos = collections.defaultdict(list)
for idx, r in enumerate(recs):
    pos[r['id']].append(idx)
dups = {k: v for k, v in pos.items() if len(v) > 1}

# 1. How do dup copies differ?
same = 0
diffs = collections.Counter()
acc_pattern = collections.Counter()
for k, idxs in dups.items():
    a, b = recs[idxs[0]], recs[idxs[1]]
    acc_pattern[(bool(a.get('accepted')), bool(b.get('accepted')))] += 1
    if json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True):
        same += 1
        continue
    fields = tuple(sorted(f for f in set(a) | set(b) if a.get(f) != b.get(f)))
    diffs[fields] += 1
print('dup pairs:', len(dups), 'identical:', same)
print('accepted pattern (first,second):', dict(acc_pattern))
for f, n in diffs.most_common(12):
    print(n, f)

# 2. Example dup pair inspection
for ex in ['L05-001', 'L14-011', 'L01-030']:
    idxs = pos[ex]
    if len(idxs) < 2: continue
    a, b = recs[idxs[0]], recs[idxs[1]]
    print('\n---', ex, 'copy1 idx', idxs[0], 'copy2 idx', idxs[1])
    for tag, r in (('copy1', a), ('copy2', b)):
        ia = r.get('india_origin_audit') or {}
        print(tag, '| accepted=', r.get('accepted'), '| type=', r.get('source_type'),
              '| ia_status=', ia.get('status'), '| rej=', (r.get('rejection_reason') or '')[:80])

# 3. True state of all 42 excluded IDs using best copy (prefer copy with india_origin_audit, else first)
prefx = ['L01-006','L01-010','L01-026','L01-041','L01-042','L01-054','L02-003','L02-008','L03-054','L04-024','L04-037','L04-105','L05-025','L05-051','L06-047','L07-033','L07-048','L08-023','L08-028','L09-035','L11-036','L11-053','L12-043','L13-034','L13-051','L14-052','L16-021']
fullq = ['L01-051','L01-052','L03-047','L03-049','L05-001','L06-053','L07-038','L07-039','L13-050','L14-011','L14-017','L14-023','L15-045','L16-008','L16-012']
excl = prefx + fullq
print('\n=== 42 excluded: per-copy state ===')
problems = []
for i in excl:
    idxs = pos.get(i, [])
    states = []
    for idx in idxs:
        r = recs[idx]
        ia = r.get('india_origin_audit') or {}
        states.append({
            'idx': idx,
            'accepted': r.get('accepted'),
            'type': r.get('source_type'),
            'ia': ia.get('status'),
            'rej': bool((r.get('rejection_reason') or '').strip()),
        })
    ok_copies = [s for s in states if s['accepted'] is False and s['type'] == 'discovery_only'
                 and s['ia'] == 'excluded_india_origin' and s['rej']]
    flag = 'OK' if ok_copies and all(not s['accepted'] for s in states) else 'PROBLEM'
    if flag == 'PROBLEM':
        problems.append(i)
    print(i, flag, states)
print('\nproblem IDs:', problems)

# 4. Recheck sample80 with best-copy semantics: does any sampled ID have divergent audit between copies?
sample = json.load(open('99_AUDIT/_adjudication_workdir/sample80.json', encoding='utf-8'))
diverge = []
for sid in sample:
    idxs = pos.get(sid, [])
    if len(idxs) > 1:
        a, b = recs[idxs[0]], recs[idxs[1]]
        ia_a = (a.get('india_origin_audit') or {}).get('status')
        ia_b = (b.get('india_origin_audit') or {}).get('status')
        if (bool(a.get('accepted')), ia_a) != (bool(b.get('accepted')), ia_b):
            diverge.append((sid, a.get('accepted'), ia_a, b.get('accepted'), ia_b))
print('\nsampled IDs with divergent copies:', diverge if diverge else 'NONE (all dup copies agree on accepted+status)')

# 5. Are second copies stale pre-audit versions? Check global pattern.
second_acc = sum(1 for k, v in dups.items() if recs[v[1]].get('accepted'))
first_acc = sum(1 for k, v in dups.items() if recs[v[0]].get('accepted'))
print('\ndup pairs where first copy accepted:', first_acc, '| second copy accepted:', second_acc)
# which copy has india_origin_audit?
pat = collections.Counter()
for k, v in dups.items():
    a, b = recs[v[0]], recs[v[1]]
    pat[(a.get('india_origin_audit') is not None, b.get('india_origin_audit') is not None)] += 1
print('ia-object presence pattern (first,second):', dict(pat))
