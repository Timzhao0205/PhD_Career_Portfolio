#requires -Version 5.1
[CmdletBinding()]
param(
    [switch]$CheckOnly,
    [switch]$NewSession,
    [switch]$AllowCompatiblePS51,
    [switch]$RetryFableAfterReview
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$Root = $PSScriptRoot
$powerShellCommand = Get-Command powershell.exe -ErrorAction Stop

foreach ($name in @(
    'CLAUDE_CODE_EFFORT_LEVEL','CLAUDE_CODE_SUBAGENT_MODEL',
    'ANTHROPIC_MODEL','ANTHROPIC_DEFAULT_FABLE_MODEL'
)) {
    [Environment]::SetEnvironmentVariable($name, $null, 'Process')
}

Write-Host ''
Write-Host '==== Package and input validation ====' -ForegroundColor Cyan
$checkArguments = @()
if ($AllowCompatiblePS51) {
    $checkArguments += '-AllowCompatiblePS51'
}
& $powerShellCommand.Source -NoProfile -ExecutionPolicy Bypass `
    -File (Join-Path $Root 'CHECK.ps1') @checkArguments
$code = [int]$LASTEXITCODE
if ($code -ne 0) {
    Write-Host (
        'START stopped before Claude launch. Repair the visible validation ' +
        'failure and rerun this same command.'
    ) -ForegroundColor Red
    exit $code
}

Write-Host ''
Write-Host '==== Offline all-stage and hook pilot ====' -ForegroundColor Cyan
$pilotArguments = @()
if ($AllowCompatiblePS51) {
    $pilotArguments += '-AllowCompatiblePS51'
}
& $powerShellCommand.Source -NoProfile -ExecutionPolicy Bypass `
    -File (Join-Path $Root 'PILOT.ps1') @pilotArguments
$code = [int]$LASTEXITCODE
if ($code -ne 0) {
    Write-Host (
        'START stopped before Claude launch. Repair the visible pilot ' +
        'failure and rerun this same command.'
    ) -ForegroundColor Red
    exit $code
}

if ($CheckOnly) {
    Write-Host (
        'CHECK-ONLY COMPLETE: no Claude model call was made.'
    ) -ForegroundColor Green
    exit 0
}

$modelPausePath = Join-Path $Root 'state\MODEL_PAUSE.json'
$modelRetryPath = Join-Path $Root 'state\MODEL_RETRY.json'
$sessionPath = Join-Path $Root 'state\ACTIVE_SESSION.json'
$quarantineDir = Join-Path $Root 'quarantine'
if (-not (Test-Path -LiteralPath $quarantineDir -PathType Container)) {
    [void](New-Item -ItemType Directory -Force -Path $quarantineDir)
}

if ($RetryFableAfterReview) {
    if (Test-Path -LiteralPath $modelPausePath -PathType Leaf) {
        $stamp = [DateTime]::UtcNow.ToString('yyyyMMdd_HHmmss')
        Copy-Item -LiteralPath $modelPausePath -Destination (
            Join-Path $quarantineDir "reviewed_model_pause_$stamp.json"
        )
        Remove-Item -LiteralPath $modelPausePath -Force
    }
    if (Test-Path -LiteralPath $sessionPath -PathType Leaf) {
        Remove-Item -LiteralPath $sessionPath -Force
    }
    $NewSession = $true
}

if (Test-Path -LiteralPath $modelPausePath -PathType Leaf) {
    Write-Host (
        'Protected second Fable/model event is preserved in ' +
        'state\MODEL_PAUSE.json. Review it, then explicitly run START.ps1 ' +
        'with -RetryFableAfterReview.'
    ) -ForegroundColor Red
    exit 2
}

$automaticRetryUsed = $false
if (Test-Path -LiteralPath $modelRetryPath -PathType Leaf) {
    $stamp = [DateTime]::UtcNow.ToString('yyyyMMdd_HHmmss')
    Copy-Item -LiteralPath $modelRetryPath -Destination (
        Join-Path $quarantineDir "model_retry_$stamp.json"
    )
    Remove-Item -LiteralPath $modelRetryPath -Force
    if (Test-Path -LiteralPath $sessionPath -PathType Leaf) {
        Copy-Item -LiteralPath $sessionPath -Destination (
            Join-Path $quarantineDir "model_retry_session_$stamp.json"
        )
        Remove-Item -LiteralPath $sessionPath -Force
    }
    $NewSession = $true
    $automaticRetryUsed = $true
}

$claudeCommand = Get-Command claude -ErrorAction SilentlyContinue
if ($null -eq $claudeCommand) {
    Write-Host (
        'Claude Code was not found on PATH. Install/sign in to Claude Code, ' +
        'close and reopen Windows PowerShell, then rerun the same command.'
    ) -ForegroundColor Red
    exit 1
}

Write-Host ''
Write-Host '==== Claude Code version ====' -ForegroundColor Cyan
& $claudeCommand.Source --version
if ($LASTEXITCODE -ne 0) {
    Write-Host (
        'Claude Code did not start correctly. Repair its installation or ' +
        'authentication, then rerun the same command.'
    ) -ForegroundColor Red
    exit 1
}

$resumeId = ''
if (-not $NewSession -and
    (Test-Path -LiteralPath $sessionPath -PathType Leaf)) {
    try {
        $active = [System.IO.File]::ReadAllText($sessionPath) |
            ConvertFrom-Json
        $resumeId = [string]$active.session_id
    } catch {
        Write-Host (
            'The saved session marker is invalid. Use -NewSession once; ' +
            'durable stage files will still be retained.'
        ) -ForegroundColor Red
        exit 1
    }
}

$common = @(
    '--model','fable',
    '--effort','xhigh',
    '--permission-mode','bypassPermissions',
    '--no-chrome',
    '--append-system-prompt-file',(Join-Path $Root 'SESSION_POLICY.md')
)

Write-Host (
    'Main route: Fable 5/xhigh; full permissions; persistent interactive ' +
    'session; no package-defined budget/turn/token/time stop.'
) -ForegroundColor Green
Write-Host (
    'Press Ctrl+C only if you intentionally want to pause. Rerun this same ' +
    'START.ps1 command to resume.'
) -ForegroundColor Yellow

$claudeExit = 0
while ($true) {
    if ([string]::IsNullOrWhiteSpace($resumeId)) {
        $sessionName = 'f06i-' + (
            [Guid]::NewGuid().ToString('N').Substring(0,12)
        )
        $prompt = (
            'Open CLAUDE.md and RUNBOOK.md now. Verify the session model and ' +
            'effort telemetry, inspect durable state, then perform every ' +
            'required stage pilot and full stage through the final audited ' +
            'release. Work autonomously and do not stop for routine progress ' +
            'summaries.'
        )
        if ($automaticRetryUsed) {
            $prompt = (
                'This is the single automatic retry after a first model-' +
                'integrity event. Verify Fable 5/xhigh before any substantive ' +
                'work, then read RUNBOOK.md and continue from durable files.'
            )
        }
        $claudeArguments = $common + @(
            '--name',$sessionName,$prompt
        )
        Write-Host ''
        Write-Host '==== Starting interactive Fable session ====' `
            -ForegroundColor Cyan
    } else {
        $prompt = (
            'Resume the Folder 06 run. Read RUNBOOK.md and durable state, ' +
            'verify every saved checkpoint, and continue the next unfinished ' +
            'pilot or stage autonomously through the audited final release.'
        )
        $claudeArguments = $common + @(
            '--resume',$resumeId,$prompt
        )
        Write-Host ''
        Write-Host "==== Resuming interactive session $resumeId ====" `
            -ForegroundColor Cyan
    }

    & $claudeCommand.Source @claudeArguments
    $claudeExit = [int]$LASTEXITCODE

    if (Test-Path -LiteralPath (Join-Path $Root `
        'state\RUN_COMPLETE.json') -PathType Leaf) {
        break
    }
    if ((Test-Path -LiteralPath $modelRetryPath -PathType Leaf) -and
        -not $automaticRetryUsed -and
        -not (Test-Path -LiteralPath $modelPausePath -PathType Leaf)) {
        $stamp = [DateTime]::UtcNow.ToString('yyyyMMdd_HHmmss')
        Copy-Item -LiteralPath $modelRetryPath -Destination (
            Join-Path $quarantineDir "model_retry_$stamp.json"
        )
        Remove-Item -LiteralPath $modelRetryPath -Force
        if (Test-Path -LiteralPath $sessionPath -PathType Leaf) {
            Copy-Item -LiteralPath $sessionPath -Destination (
                Join-Path $quarantineDir "model_retry_session_$stamp.json"
            )
            Remove-Item -LiteralPath $sessionPath -Force
        }
        $resumeId = ''
        $automaticRetryUsed = $true
        Write-Host (
            'First model-integrity event archived. Starting the one allowed ' +
            'fresh Fable retry now.'
        ) -ForegroundColor Yellow
        continue
    }
    break
}

Write-Host ''
$completePath = Join-Path $Root 'state\RUN_COMPLETE.json'
if (Test-Path -LiteralPath $completePath -PathType Leaf) {
    Write-Host '==== Final local verification ====' -ForegroundColor Cyan
    & $powerShellCommand.Source -NoProfile -ExecutionPolicy Bypass `
        -File (Join-Path $Root 'VALIDATE.ps1') -All
    $finalCode = [int]$LASTEXITCODE
    if ($finalCode -eq 0) {
        Write-Host (
            'RUN COMPLETE: audited release is under ' +
            'outputs\70_audit\FINAL.'
        ) -ForegroundColor Green
        exit 0
    }
    Write-Host (
        'Claude created a completion marker, but final validation failed. ' +
        'Rerun the same START.ps1 command so Claude can repair it.'
    ) -ForegroundColor Red
    exit 1
}

Write-Host (
    "Claude session ended with code $claudeExit before RUN_COMPLETE. " +
    'All durable work is retained. Rerun the same START.ps1 command to resume.'
) -ForegroundColor Yellow
exit $claudeExit
