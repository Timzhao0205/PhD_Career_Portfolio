# V4.1 build-validation record

Build date: 2026-07-28  
Package: `PAP06_INTERACTIVE_PS51` 4.1.0  
Recommended root: `C:\AI\PAP06I_V4_1`

## Completed in the build workspace

| Check | Result |
|---|---|
| Five current uploads versus packaged inputs | PASS, byte-for-byte/SHA-256 |
| Five input manifest records | PASS |
| Four complete source ZIP CRC scans | PASS |
| ZIP traversal/absolute/reserved/symlink/case-collision checks | PASS |
| Source archive totals | PASS, 3,610 entries / 3,182 files |
| Predicted source path at recommended root | PASS, maximum 185 characters |
| Old Folder 06 nested in startup corpus | PASS, 419/419 exact files |
| Blind reconstruction pool | PASS, 126 unique IDs / 3 hash-checked shards |
| Blind ranking/adjudication leakage fields | PASS, absent |
| V2 outer/member preservation ledger | PASS, 69 members |
| Compact V2 reference | PASS, 64 non-input members |
| Retired V3 runtime preservation | PASS, settings/hook/policies/scripts inactive |
| Route order and prerequisites | PASS, 15/15 stages |
| Live-pilot-before-full route | PASS, 15 pilots + 15 full calls |
| Model route | PASS, 12 Fable/xhigh + 3 Sonnet/high stages |
| Main/named-agent YAML frontmatter | PASS |
| Full-permission wiring | PASS, `bypassPermissions` |
| Interactive controller + fresh foreground subagents | PASS, statically wired |
| Active nested/print Claude launch paths | PASS, none |
| Budget/cost/token/turn/time stop controls | PASS, none |
| Automatic fallback-model chain | PASS, none |
| JSON parse | PASS |
| PowerShell grammar parse | PASS, all active/preserved `.ps1` files |
| PS5.1 expandable-variable colon lint | PASS; unbraced `$name:` rejected |
| SessionStart missing-permission fixture | PASS; launch nonce accepted without inventing an observed value |
| Package Windows filename/case-collision checks | PASS |

The final archive is additionally checked for CRC, member count, duplicate and
case-colliding names, per-member SHA-256, outer SHA-256, and clean extraction
equality after `PACKAGE_SHA256.json` is sealed.

## First-command gates on the user's computer

The build workspace is Linux and cannot truthfully execute Windows PowerShell
5.1, use the user's Claude account, or prove provider-side model/effort access.
The one command therefore performs these gates on the target machine:

1. exact Windows PowerShell 5.1 Desktop detection;
2. Claude Code 2.1.219+ and authentication before opening the TUI;
3. native Windows PowerShell parser pass for every package `.ps1`;
4. every package/input/legacy hash and all four ZIP safety scans;
5. all 15 validator branches using offline fixtures;
6. safe source expansion plus a complete expanded-file hash manifest;
7. SessionStart proof that the visible controller is Fable 5, plus either
   direct `bypassPermissions` hook evidence or correlated sealed-launch
   evidence when the hook omits that field;
8. live same-model/same-effort pilot before every full stage;
9. SubagentStop transcript proof for each named stage worker;
10. schema validation and file-hash checkpoint before acceptance.

Operation B remains locked until all three Operation A full checkpoints are
valid. The final release requires 30 valid pilot/full checkpoints and a B80
audit PASS with zero unresolved critical/major issues.

## Reliability boundary

No package can guarantee that an external account, organization allowlist,
effort cap, network, provider safeguard, or service never fails. V4.1 prevents
those conditions from being mistaken for accepted work and lets the same
command resume in a fresh interactive controller context.
