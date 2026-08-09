#requires -Version 5.1
Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

function Write-Utf8NoBom {
    param([string]$Path, [string]$Text, [switch]$Append)
    $encoding = New-Object System.Text.UTF8Encoding($false)
    if ($Append) {
        [System.IO.File]::AppendAllText($Path, $Text, $encoding)
    } else {
        [System.IO.File]::WriteAllText($Path, $Text, $encoding)
    }
}

try {
    $root = [System.IO.Path]::GetFullPath(
        (Join-Path $PSScriptRoot '..\..')
    )
    $stateDir = Join-Path $root 'state'
    $logDir = Join-Path $root 'logs'
    foreach ($dir in @($stateDir, $logDir)) {
        if (-not (Test-Path -LiteralPath $dir -PathType Container)) {
            [void](New-Item -ItemType Directory -Force -Path $dir)
        }
    }

    $raw = [Console]::In.ReadToEnd()
    $event = $raw | ConvertFrom-Json
    $model = [string]$event.model
    $sessionId = [string]$event.session_id
    $source = [string]$event.source
    $record = [ordered]@{
        captured_at_utc = [DateTime]::UtcNow.ToString('o')
        event = 'SessionStart'
        source = $source
        session_id = $sessionId
        model_observed = $model
        effort_requested = 'xhigh'
        permission_mode_requested = 'bypassPermissions'
        transcript_path = [string]$event.transcript_path
        cwd = [string]$event.cwd
    }
    $json = $record | ConvertTo-Json -Depth 20
    Write-Utf8NoBom -Path (Join-Path $stateDir 'ACTIVE_SESSION.json') `
        -Text ($json + [Environment]::NewLine)
    $line = $record | ConvertTo-Json -Depth 20 -Compress
    Write-Utf8NoBom -Path (Join-Path $logDir 'events.jsonl') `
        -Text ($line + [Environment]::NewLine) -Append

    $isFable5 = (
        $model -match '(?i)fable' -and
        $model -match '5'
    )
    if (-not $isFable5) {
        $eventPath = Join-Path $stateDir 'FABLE_EVENTS.json'
        $events = @()
        if (Test-Path -LiteralPath $eventPath -PathType Leaf) {
            try {
                $savedEvents = [System.IO.File]::ReadAllText($eventPath) |
                    ConvertFrom-Json
                $events = @($savedEvents.events)
            } catch {
                $events = @()
            }
        }
        $alreadyRecorded = @($events | Where-Object {
            [string]$_.session_id -eq $sessionId
        }).Count -gt 0
        if (-not $alreadyRecorded) {
            $events += [ordered]@{
                captured_at_utc = [DateTime]::UtcNow.ToString('o')
                session_id = $sessionId
                model_observed = $model
                effort_observed = 'not_exposed_at_session_start'
            }
        }
        $eventRecord = [ordered]@{
            count = @($events).Count
            policy = 'first_retry_second_pause'
            events = @($events)
        }
        Write-Utf8NoBom -Path $eventPath -Text (
            ($eventRecord | ConvertTo-Json -Depth 30) +
            [Environment]::NewLine
        )
        $modelEvent = [ordered]@{
            created_at_utc = [DateTime]::UtcNow.ToString('o')
            reason = 'MAIN_MODEL_NOT_VERIFIED_AS_FABLE_5'
            observed_model = $model
            requested_model = 'fable'
            requested_effort = 'xhigh'
            session_id = $sessionId
            event_count = @($events).Count
        }
        if (@($events).Count -le 1) {
            Write-Utf8NoBom -Path (Join-Path $stateDir 'MODEL_RETRY.json') `
                -Text (($modelEvent | ConvertTo-Json -Depth 20) +
                    [Environment]::NewLine)
            Write-Output (
                'FIRST MODEL-INTEGRITY EVENT: do not perform substantive ' +
                'work. Stop this response. The launcher will archive this ' +
                'attempt and automatically retry one fresh Fable session.'
            )
        } else {
            $retryPath = Join-Path $stateDir 'MODEL_RETRY.json'
            if (Test-Path -LiteralPath $retryPath -PathType Leaf) {
                Remove-Item -LiteralPath $retryPath -Force
            }
            Write-Utf8NoBom -Path (Join-Path $stateDir 'MODEL_PAUSE.json') `
                -Text (($modelEvent | ConvertTo-Json -Depth 20) +
                    [Environment]::NewLine)
            Write-Output (
                'SECOND MODEL-INTEGRITY EVENT: do not perform substantive ' +
                'work. Preserve state/MODEL_PAUSE.json and stop for review.'
            )
        }
    } else {
        $retryPath = Join-Path $stateDir 'MODEL_RETRY.json'
        if (Test-Path -LiteralPath $retryPath -PathType Leaf) {
            Remove-Item -LiteralPath $retryPath -Force
        }
        $pausePath = Join-Path $stateDir 'MODEL_PAUSE.json'
        if (Test-Path -LiteralPath $pausePath -PathType Leaf) {
            Write-Output (
                'A protected second-strike MODEL_PAUSE still exists. Do not ' +
                'perform substantive work until the user explicitly starts ' +
                'with -RetryFableAfterReview.'
            )
        } else {
            Write-Output (
                'Main session verified as Fable 5. Requested effort is xhigh. ' +
                'Read RUNBOOK.md, inspect durable state, and continue the next ' +
                'unfinished pilot or stage without waiting.'
            )
        }
    }
} catch {
    try {
        $fallback = Join-Path $PSScriptRoot 'hook_errors.log'
        $message = ('{0} SESSION_START {1}{2}' -f
            [DateTime]::UtcNow.ToString('o'),
            $_.Exception.Message,
            [Environment]::NewLine)
        Write-Utf8NoBom -Path $fallback -Text $message -Append
    } catch {
    }
    Write-Output (
        'SESSION HOOK ERROR: do not begin substantive work until the ' +
        'project logging setup is repaired.'
    )
}
exit 0
