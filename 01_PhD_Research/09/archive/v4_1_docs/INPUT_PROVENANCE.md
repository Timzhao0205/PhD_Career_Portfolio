# Input provenance

The clean package embeds the latest attachments supplied for this rebuild.
Their content hashes exactly match the corresponding inputs embedded in the
previous V2 package.

| Runtime file | User attachment | Bytes | SHA-256 |
|---|---|---:|---|
| `inputs/06_old.zip` | `06_ideas(8).zip` | 36,261,562 | `62f4111018161d58db36d7beb0e7153743f2f00c05482759c349f6fc4d3e8912` |
| `inputs/06_new.zip` | `06_ideas_new(2).zip` | 37,214,754 | `2c05dd6c145b01e9b39dcbaf9867d6c0fe8770fb99ef305208f21f61036b9db6` |
| `inputs/phd.zip` | `01_phd_work(3).zip` | 68,461,374 | `764243843698b1ff555e8dac8abcafcfcca5ce881c2c51d31a98df9a0d8a003d` |
| `inputs/startup.zip` | `02_Startup(5).zip` | 77,893,566 | `8eec7492bf849d44c9ba9c80b34841c1f9a296d4b24e9583e7540c5186f1fb87` |
| `inputs/history.md` | `prev_chat(2).md` | 29,939 | `6bef537791f862850ba417736530ea4efd01c006e77c4ac699942ecb69ec28b3` |

All four archives passed complete ZIP CRC checks before release. Their
contents include the prior research results, source ledgers, model logs, and
supporting documents. The old Folder 06 tree also exists inside the startup
archive; the standalone old ZIP is authoritative for Operation A and the
nested copy must not be double-counted.

`blind` is the preserved deterministic, score-free projection of 126 unique
raw P3R2 ideas in three hash-checked shards. It excludes ranking,
adjudication, and confidence fields so A10 can perform a genuinely independent
reconstruction.

During extraction, source files named `.claude`, `CLAUDE.md`,
`CLAUDE.local.md`, or `AGENTS.md` are renamed only in the working copy so
historical instructions cannot control the new run. Original ZIP bytes remain
unchanged. `state\SOURCE_RENAMES.json` records each mapping and hash.
