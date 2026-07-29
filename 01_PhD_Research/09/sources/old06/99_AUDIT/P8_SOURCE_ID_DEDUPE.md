# P8 source-ID deduplication

Collapsed 198 historical duplicate IDs and removed 198 extra rows. Every duplicate group had at most one accepted record, so the authoritative accepted row was retained; groups containing only rejected records retained the richest fetched/audited row. The pre-repair ledger is preserved in `98_RUN_LOGS/P8_PRE_SOURCE_ID_DEDUPE_sources.json`.
