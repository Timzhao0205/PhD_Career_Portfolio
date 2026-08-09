# Fable model integrity and fallback log

No runtime model event has occurred. Log each classifier notice, refusal,
availability error, prompt rewrite, retry, quarantine path, and final disposition.
Absence of observable metadata is recorded as `not_exposed`, not as proof of a
model substitution.
