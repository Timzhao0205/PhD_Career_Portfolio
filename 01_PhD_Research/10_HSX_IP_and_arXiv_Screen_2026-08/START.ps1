[CmdletBinding()]
param()

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

$Root = $PSScriptRoot
Set-Location -LiteralPath $Root

Write-Host ''
Write-Host '==== HSX publication-only IP and arXiv review ====' -ForegroundColor Cyan
Write-Host 'Running deterministic package validation before Claude Code starts.'

$Preflight = Join-Path $Root 'PREFLIGHT.ps1'
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File $Preflight
if ($LASTEXITCODE -ne 0) {
    Write-Host ''
    Write-Host 'START STOPPED: preflight reported a real prerequisite error.' -ForegroundColor Red
    Write-Host 'Nothing was sent to Claude Code. Correct the named item and run the same command.' -ForegroundColor Yellow
    exit $LASTEXITCODE
}

$StatePath = Join-Path $Root 'state\STATE.json'
$State = Get-Content -Raw -LiteralPath $StatePath | ConvertFrom-Json
$SessionName = 'hsx-ip-arxiv-review'
$DebugFile = Join-Path $Root 'state\claude_debug.log'
$SystemPrompt = Join-Path $Root 'SYSTEM_PROMPT.md'
$LaunchLog = Join-Path $Root 'state\LAUNCH_LOG.csv'
$Now = [DateTime]::UtcNow.ToString('o')

if (-not (Test-Path -LiteralPath $LaunchLog)) {
    'utc,mode,requested_model,requested_effort,permission_mode' |
        Set-Content -LiteralPath $LaunchLog -Encoding UTF8
}

$Common = @(
    '--model', 'fable',
    '--effort', 'xhigh',
    '--dangerously-skip-permissions',
    '--debug-file', $DebugFile,
    '--append-system-prompt-file', $SystemPrompt
)

if ([bool]$State.session_started) {
    Add-Content -LiteralPath $LaunchLog -Encoding UTF8 -Value (
        '"{0}",resume,fable,xhigh,bypassPermissions' -f $Now
    )
    Write-Host ''
    Write-Host 'Resuming the named Claude Code session in this folder.' -ForegroundColor Green
    $Prompt = @'
Resume the publication-only HSX IP/arXiv review. Read state/STATE.json,
state/WORKLOG.md, and the newest checkpoint before acting. Continue from the
first incomplete stage. Preserve every valid prior result. Do not broaden scope.
'@
    $ClaudeArgs = $Common + @('--resume', $SessionName, $Prompt)
} else {
    Add-Content -LiteralPath $LaunchLog -Encoding UTF8 -Value (
        '"{0}",new,fable,xhigh,bypassPermissions' -f $Now
    )
    Write-Host ''
    Write-Host 'Starting a new named Claude Code session.' -ForegroundColor Green
    $Prompt = @'
Begin the publication-only HSX IP/arXiv review. Your first action must be to
read START_HERE.md and follow it exactly. Keep the work inside this folder.
The accepted critical analyses and final synthesis must be produced by Fable 5
at xhigh effort under MODEL_PLAN.md.
'@
    $ClaudeArgs = $Common + @('--name', $SessionName, $Prompt)
}

Write-Host 'Requested parent: Claude Fable 5 / xhigh.'
Write-Host 'Permission mode: bypassPermissions (full read/write in the native CLI).'
Write-Host 'Model switching on a safety flag is disabled; a flag pauses visibly.'
Write-Host ''

& claude @ClaudeArgs
$ClaudeExit = $LASTEXITCODE

Write-Host ''
if ($ClaudeExit -eq 0) {
    Write-Host 'Claude Code closed normally. The same START.ps1 command resumes.' -ForegroundColor Green
} else {
    Write-Host ('Claude Code exited with code {0}.' -f $ClaudeExit) -ForegroundColor Yellow
    Write-Host 'State and checkpoints remain in this folder. Run the same command to resume.'
}
exit $ClaudeExit
