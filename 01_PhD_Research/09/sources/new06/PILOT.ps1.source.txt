#requires -Version 5.1
[CmdletBinding()]
param(
    [switch]$AllowCompatiblePS51
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$Root = $PSScriptRoot
$Failures = New-Object System.Collections.Generic.List[string]
$Stages = @(
    '10_refresh','20_p4','30_redteam','40_select',
    '45_packs','50_deep','60_synth','70_audit'
)

function Add-Failure {
    param([string]$Message)
    [void]$script:Failures.Add($Message)
    Write-Host ("FAIL: {0}" -f $Message) -ForegroundColor Red
}

function Write-Pass {
    param([string]$Message)
    Write-Host ("PASS: {0}" -f $Message) -ForegroundColor Green
}

function Invoke-Validator {
    param([string]$StageName, [switch]$PilotMode)
    $arguments = @(
        '-NoProfile','-ExecutionPolicy','Bypass',
        '-File',(Join-Path $Root 'VALIDATE.ps1'),
        '-Stage',$StageName,
        '-BasePath',(Join-Path $Root 'tests\fixtures'),
        '-Quiet'
    )
    if ($PilotMode) {
        $arguments += '-Pilot'
    }
    & powershell.exe @arguments
    return [int]$LASTEXITCODE
}

function Invoke-Hook {
    param([string]$Script, [string]$InputJson)
    $output = @(
        $InputJson | & powershell.exe -NoProfile -ExecutionPolicy Bypass `
            -File $Script 2>&1
    )
    return [ordered]@{
        code = [int]$LASTEXITCODE
        output = @($output | ForEach-Object { [string]$_ })
    }
}

Write-Host ''
Write-Host '---- All-stage contract fixtures ----' -ForegroundColor Cyan
foreach ($stage in $Stages) {
    $pilotCode = Invoke-Validator -StageName $stage -PilotMode
    if ($pilotCode -ne 0) {
        Add-Failure "$stage pilot fixture failed."
        continue
    }
    $stageCode = Invoke-Validator -StageName $stage
    if ($stageCode -ne 0) {
        Add-Failure "$stage full-stage fixture failed."
        continue
    }
    Write-Pass "$stage pilot and full-stage fixtures."
}

Write-Host ''
Write-Host '---- Hook and telemetry fixtures ----' -ForegroundColor Cyan
$hookRoot = Join-Path $Root 'pilot\hook_selftest'
if (Test-Path -LiteralPath $hookRoot) {
    Remove-Item -LiteralPath $hookRoot -Recurse -Force
}
$hookDir = Join-Path $hookRoot '.claude\hooks'
[void](New-Item -ItemType Directory -Force -Path $hookDir)
foreach ($name in @(
    'EVENT_LOG.ps1','SESSION_START.ps1','STATUS.ps1','STOP_GUARD.ps1'
)) {
    Copy-Item -LiteralPath (Join-Path $Root ".claude\hooks\$name") `
        -Destination (Join-Path $hookDir $name)
}

$sessionInput = @{
    session_id = 'fixture-session'
    transcript_path = 'fixture-transcript.jsonl'
    cwd = $hookRoot
    permission_mode = 'bypassPermissions'
    hook_event_name = 'SessionStart'
    source = 'startup'
    model = 'claude-fable-5'
} | ConvertTo-Json -Compress
$sessionRun = Invoke-Hook -Script (Join-Path $hookDir `
    'SESSION_START.ps1') -InputJson $sessionInput
if ($sessionRun.code -ne 0 -or
    -not (Test-Path -LiteralPath (Join-Path $hookRoot `
        'state\ACTIVE_SESSION.json') -PathType Leaf) -or
    (Test-Path -LiteralPath (Join-Path $hookRoot `
        'state\MODEL_PAUSE.json') -PathType Leaf)) {
    Add-Failure 'Fable SessionStart hook fixture failed.'
} else {
    Write-Pass 'Fable SessionStart hook and active-session persistence.'
}

$statusInput = @{
    cwd = $hookRoot
    session_id = 'fixture-session'
    version = '2.1.219'
    model = @{
        id = 'claude-fable-5'
        display_name = 'Fable 5'
    }
    cost = @{
        total_cost_usd = 1.25
        total_duration_ms = 60000
        total_api_duration_ms = 30000
        total_lines_added = 10
        total_lines_removed = 0
    }
    context_window = @{
        total_input_tokens = 100
        total_output_tokens = 50
        context_window_size = 200000
        used_percentage = 1
        remaining_percentage = 99
    }
    effort = @{ level = 'xhigh' }
    rate_limits = @{}
} | ConvertTo-Json -Depth 20 -Compress
$statusRun = Invoke-Hook -Script (Join-Path $hookDir 'STATUS.ps1') `
    -InputJson $statusInput
$statusPath = Join-Path $hookRoot 'logs\status.jsonl'
if ($statusRun.code -ne 0 -or
    -not (Test-Path -LiteralPath $statusPath -PathType Leaf) -or
    ($statusRun.output -join ' ') -notmatch 'Fable 5') {
    Add-Failure 'Status-line telemetry fixture failed.'
} else {
    $statusLines = [System.IO.File]::ReadAllLines($statusPath)
    $record = $statusLines[$statusLines.Length - 1] | ConvertFrom-Json
    if ([string]$record.model_id -ne 'claude-fable-5' -or
        [string]$record.effort -ne 'xhigh' -or
        [double]$record.total_cost_usd_telemetry -ne 1.25) {
        Add-Failure 'Status-line fields were not recorded correctly.'
    } else {
        Write-Pass 'Model, effort, token, duration, and cost telemetry hook.'
    }
}

$eventInput = @{
    session_id = 'fixture-session'
    hook_event_name = 'PostToolUseFailure'
    tool_name = 'Fixture'
    error = 'fixture error'
} | ConvertTo-Json -Compress
$eventRun = Invoke-Hook -Script (Join-Path $hookDir 'EVENT_LOG.ps1') `
    -InputJson $eventInput
if ($eventRun.code -ne 0 -or
    -not (Test-Path -LiteralPath (Join-Path $hookRoot `
        'logs\events.jsonl') -PathType Leaf)) {
    Add-Failure 'Event logging fixture failed.'
} else {
    Write-Pass 'Failure/event logging hook.'
}

$stopInput = @{
    session_id = 'fixture-session'
    transcript_path = 'fixture-transcript.jsonl'
    cwd = $hookRoot
    permission_mode = 'bypassPermissions'
    hook_event_name = 'Stop'
    stop_hook_active = $false
    last_assistant_message = 'fixture'
} | ConvertTo-Json -Compress
$stopRun = Invoke-Hook -Script (Join-Path $hookDir 'STOP_GUARD.ps1') `
    -InputJson $stopInput
try {
    $stopDecision = ($stopRun.output -join [Environment]::NewLine) |
        ConvertFrom-Json
    if ($stopRun.code -ne 0 -or
        [string]$stopDecision.decision -ne 'block') {
        Add-Failure 'Incomplete-run Stop hook did not continue work.'
    } else {
        Write-Pass 'Stop guard continues an incomplete run.'
    }
} catch {
    Add-Failure 'Stop-hook fixture did not return valid decision JSON.'
}

$mismatchRoot = Join-Path $Root 'pilot\model_mismatch_selftest'
if (Test-Path -LiteralPath $mismatchRoot) {
    Remove-Item -LiteralPath $mismatchRoot -Recurse -Force
}
$mismatchHookDir = Join-Path $mismatchRoot '.claude\hooks'
[void](New-Item -ItemType Directory -Force -Path $mismatchHookDir)
Copy-Item -LiteralPath (Join-Path $Root `
    '.claude\hooks\SESSION_START.ps1') `
    -Destination (Join-Path $mismatchHookDir 'SESSION_START.ps1')
$badInputObject = $sessionInput | ConvertFrom-Json
$badInputObject.model = 'claude-opus-5'
$badInputObject.cwd = $mismatchRoot
$badRun = Invoke-Hook -Script (Join-Path $mismatchHookDir `
    'SESSION_START.ps1') -InputJson (
        $badInputObject | ConvertTo-Json -Compress
    )
if ($badRun.code -ne 0 -or
    -not (Test-Path -LiteralPath (Join-Path $mismatchRoot `
        'state\MODEL_RETRY.json') -PathType Leaf)) {
    Add-Failure 'First non-Fable automatic-retry fixture failed.'
} else {
    Write-Pass 'First non-Fable SessionStart creates one retry marker.'
}

$badInputObject.session_id = 'fixture-session-2'
$secondBadRun = Invoke-Hook -Script (Join-Path $mismatchHookDir `
    'SESSION_START.ps1') -InputJson (
        $badInputObject | ConvertTo-Json -Compress
    )
if ($secondBadRun.code -ne 0 -or
    -not (Test-Path -LiteralPath (Join-Path $mismatchRoot `
        'state\MODEL_PAUSE.json') -PathType Leaf)) {
    Add-Failure 'Second non-Fable protected-pause fixture failed.'
} else {
    Write-Pass 'Second non-Fable SessionStart creates a protected pause.'
}

Write-Host ''
if ($Failures.Count -gt 0) {
    Write-Host (
        "OFFLINE PILOT FAILED ({0} issue(s))." -f $Failures.Count
    ) -ForegroundColor Red
    exit 1
}
Write-Host (
    'OFFLINE PILOT PASSED: all eight pilot/full contracts, hooks, telemetry, ' +
    'resume state, Stop guard, and model-integrity pause.'
) -ForegroundColor Green
exit 0
