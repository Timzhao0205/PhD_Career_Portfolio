#requires -Version 5.1
Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

function Write-Utf8NoBom {
    param([string]$Path, [string]$Text, [switch]$Append)
    $encoding = New-Object System.Text.UTF8Encoding($false)
    for ($attempt = 1; $attempt -le 10; $attempt++) {
        try {
            if ($Append) {
                [System.IO.File]::AppendAllText($Path, $Text, $encoding)
            } else {
                [System.IO.File]::WriteAllText($Path, $Text, $encoding)
            }
            return
        } catch [System.IO.IOException] {
            if ($attempt -ge 10) {
                throw
            }
            Start-Sleep -Milliseconds 120
        }
    }
}

function Get-Value {
    param($Object, [string]$Name, $Default)
    if ($null -eq $Object) {
        return $Default
    }
    $property = $Object.PSObject.Properties[$Name]
    if ($null -eq $property -or $null -eq $property.Value) {
        return $Default
    }
    return $property.Value
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
    $event = $null
    try {
        $event = $raw | ConvertFrom-Json
    } catch {
        $event = $null
    }
    $model = [string](Get-Value -Object $event -Name 'model' -Default '')
    $sessionId = [string](Get-Value -Object $event -Name 'session_id' `
        -Default '')
    $source = [string](Get-Value -Object $event -Name 'source' -Default '')
    $modelExposed = -not [string]::IsNullOrWhiteSpace($model)
    $record = [ordered]@{
        captured_at_utc = [DateTime]::UtcNow.ToString('o')
        event = 'SessionStart'
        source = $source
        session_id = $sessionId
        model_observed = $(if ($modelExposed) {
            $model
        } else {
            'not_exposed_at_session_start'
        })
        effort_requested = 'xhigh'
        permission_mode_requested = 'bypassPermissions'
        transcript_path = [string](Get-Value -Object $event `
            -Name 'transcript_path' -Default '')
        cwd = [string](Get-Value -Object $event -Name 'cwd' -Default '')
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
    $retryPath = Join-Path $stateDir 'MODEL_RETRY.json'
    $pausePath = Join-Path $stateDir 'MODEL_PAUSE.json'
    if (-not $modelExposed) {
        # Absence of a model identifier is never converted into a false
        # verification or a false downgrade (MODEL_POLICY.md). Record
        # honestly, change no integrity state, and defer to status telemetry.
        if (Test-Path -LiteralPath $pausePath -PathType Leaf) {
            Write-Output (
                'A protected second-strike MODEL_PAUSE still exists. Do not ' +
                'perform substantive work until the user explicitly starts ' +
                'with -RetryFableAfterReview.'
            )
        } elseif (Test-Path -LiteralPath $retryPath -PathType Leaf) {
            Write-Output (
                'SessionStart did not expose a model identifier and ' +
                'state/MODEL_RETRY.json exists from a prior event. Verify ' +
                'the newest logs/status.jsonl telemetry shows Fable 5 at ' +
                'xhigh and adjudicate per MODEL_POLICY.md before ' +
                'substantive work.'
            )
        } else {
            Write-Output (
                'SessionStart did not expose a model identifier. Requested ' +
                'model fable, effort xhigh. Verify the newest ' +
                'logs/status.jsonl telemetry before accepting any stage ' +
                'result; prompt text is not model evidence.'
            )
        }
    } elseif (-not $isFable5) {
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
            [string](Get-Value -Object $_ -Name 'session_id' -Default '') `
                -eq $sessionId
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
            Write-Utf8NoBom -Path $retryPath `
                -Text (($modelEvent | ConvertTo-Json -Depth 20) +
                    [Environment]::NewLine)
            Write-Output (
                'FIRST MODEL-INTEGRITY EVENT: do not perform substantive ' +
                'work. Stop this response. The launcher will archive this ' +
                'attempt and automatically retry one fresh Fable session.'
            )
        } else {
            if (Test-Path -LiteralPath $retryPath -PathType Leaf) {
                Remove-Item -LiteralPath $retryPath -Force
            }
            Write-Utf8NoBom -Path $pausePath `
                -Text (($modelEvent | ConvertTo-Json -Depth 20) +
                    [Environment]::NewLine)
            Write-Output (
                'SECOND MODEL-INTEGRITY EVENT: do not perform substantive ' +
                'work. Preserve state/MODEL_PAUSE.json and stop for review.'
            )
        }
    } else {
        if (Test-Path -LiteralPath $retryPath -PathType Leaf) {
            Remove-Item -LiteralPath $retryPath -Force
        }
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
