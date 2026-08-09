# PAP06 Native Claude Code package

This is the clean, native replacement for the PowerShell-orchestrated PAP06
packages. PowerShell 5.1 may host the terminal, but no research, validation,
checkpoint, hook, extraction, or release step calls a PowerShell script.

The package contains:

- the old Folder 06 research;
- the completed recent Folder 06 rerun and its final outputs;
- the PhD corpus and future Option 2 material;
- the complete prior startup corpus, with the duplicate old Folder 06 tree
  represented once;
- prior chat/history;
- the score-free 126-idea blind pool;
- retained source/model/literature policies and prior package documentation;
- a native project skill, a visible Fable/xhigh controller, model-locked fresh
  workers, a fresh Fable/xhigh full-stage verifier, durable state, pilots, and
  a final independent audit.

## Requirements

- Windows 10/11.
- Claude Code 2.1.219 or later.
- An organization/account where the model picker exposes Fable 5 and Sonnet 5.
- Internet access for WebSearch/WebFetch.
- At least 1.5 GB free disk space for extraction, outputs, and logs.

Your known environment—Windows PowerShell 5.1.26100.8875 Desktop—is compatible
because it only launches the native `claude` executable.

## Safe setup

1. In the old V4.1 interface, choose its safe-pause option and close it. Do not
   patch or continue the old package.
2. Extract this ZIP with Windows Explorer to a short dedicated path, preferably
   `C:\AI\PAP06N`.
3. Confirm that the opened folder directly contains `CLAUDE.md`, `README.md`,
   `workflow`, `sources`, and `.claude`. Avoid a doubled `PAP06N\PAP06N` path.
4. Right-click the folder and choose **Open in Terminal**, or open Windows
   Terminal there.
5. Run the one command below.

## One command

```text
claude --agent pap06-controller --model fable --effort xhigh --permission-mode bypassPermissions --strict-mcp-config --no-chrome --name PAP06-NATIVE --debug-file "logs/claude-native-debug.log"
```

The agent's `initialPrompt` invokes `/pap06-native` automatically. This is an
interactive session, not `claude -p`; you will see the controller and each
foreground stage agent work.

Claude Code may show its normal first-use workspace-trust and dangerous-mode
confirmation. Review and accept them only because this is a dedicated folder.
Project settings cannot and should not suppress those product safeguards.

## Watching progress

- Press `Ctrl+T` to show/hide the persistent task checklist.
- Use `/tasks` to inspect the active foreground subagent.
- Read `state/PROGRESS.md` for durable accepted progress.
- Read `state/MODEL_LEDGER.md` for requested/observed model and effort notes.
- Read `state/ERROR_LOG.md` for retries, provider events, and limitations.

Workers always write a `RUN_META.md` and `SELF_CHECK.md`. Every full stage then
receives a fresh Fable 5/xhigh report under `verification/`.

## Resume

If Windows closes, a provider limit is reached, or context compaction fails,
close the session and rerun the exact same one command from this folder. The
controller verifies files and resumes at the first unaccepted item. Do not use
the old session transcript as the progress source.

## Permission warning

`bypassPermissions` grants broad read/write authority inside the Claude Code
environment. Use this package only in its dedicated extracted directory. Keep
unrelated private files, credentials, and repositories outside that directory.
The package disables command shells, project hooks, Chrome integration, MCP
servers, and artifact publishing to reduce unnecessary exposure.

## Expected final reading order

After B80 passes, read the accepted B80 candidate:

1. `FINAL/PLAIN.md`
2. `FINAL/RANKING.csv`
3. `FINAL/DETAILED.md`
4. `FINAL/SOURCE_INDEX.csv`
5. `FINAL/MODEL_REPORT.md`
6. `AUDIT.md` and `FINAL/RELEASE.json`

`state/RUN_COMPLETE.md` will contain the exact accepted paths.
