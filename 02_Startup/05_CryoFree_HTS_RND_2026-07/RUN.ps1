# =============================================================================
# ONE-COMMAND AUTONOMOUS RUNNER (Windows PowerShell)
# Usage:  .\RUN.ps1                # default 2,000,000-token ceiling
#         .\RUN.ps1 -Ceiling 5000000
# Runs the full pipeline hands-off with auto-resume. Logs to run_console.log.
# =============================================================================
param([int]$Ceiling = 2000000, [int]$MaxPass = 12)
Set-Location -Path $PSScriptRoot
$log = "run_console.log"
"[RUN] $(Get-Date) starting autonomous pipeline, budget ceiling=$Ceiling" | Tee-Object -FilePath $log -Append

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
  "[RUN] ERROR: 'claude' CLI not found on PATH. Install Claude Code first." | Tee-Object -FilePath $log -Append
  exit 1
}

for ($pass = 1; $pass -le $MaxPass; $pass++) {
  "[RUN] pass $pass $(Get-Date)" | Tee-Object -FilePath $log -Append
  claude -p "/autorun $Ceiling" --permission-mode bypassPermissions --dangerously-skip-permissions *>> $log
  $phase = ""
  try { $phase = (python -c "import json;print(json.load(open('80_STATE/RUN_STATE.json')).get('phase',''))") } catch {}
  "[RUN] pass $pass finished; phase=$phase" | Tee-Object -FilePath $log -Append
  if ($phase -match "W5_done|COMPLETE|complete") { "[RUN] pipeline complete." | Tee-Object -FilePath $log -Append; break }
  Start-Sleep -Seconds 2
}
"[RUN] done. See 10_MISSION/RND_STRATEGY_CryoFree.md and 98_CLAUDE_METRICS/RUN_REPORT.md" | Tee-Object -FilePath $log -Append
