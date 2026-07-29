# Windows PowerShell 5.1 validator hotfix — 2026-07-24

## Observed result

The preceding package successfully connected to Claude Sonnet 5 and Fable 5,
then stopped during package preflight with these two messages:

- `Fable final-result first/second downgrade transition policy is missing.`
- `The event logger does not distinguish temporary/auxiliary models from the
  Fable final result.`

No research stage started.

## Root cause

The policy implementation and event fields were present. Two source-validation
regular expressions were written with double backslashes before literal
parentheses:

```text
\\(\\?i\\)
```

PowerShell does not use backslash as its string escape character. The regular
expression therefore searched for literal backslashes that were not present in
the runner source.

## Correction

Both checks now use PowerShell-native regular-expression escaping:

```text
\(\?i\)
```

The repaired assertions verify these actual source expressions:

```powershell
[string]$ExpectedModel -match '(?i)fable'
[string]$RequestedModel -match '(?i)fable'
```

No model routing, downgrade behavior, prompt, input, or research acceptance
gate was weakened. The validator now recognizes the policy that was already
implemented.

## Restart state

This corrected package is still a clean full restart:

- 0 of 12 stages complete;
- next stage `00_inventory`;
- no active completion marker or research session;
- historical records retained under `_history\r0` for audit only.
