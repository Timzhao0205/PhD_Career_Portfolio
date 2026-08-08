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
    $logDir = Join-Path $root 'logs'
    $stateDir = Join-Path $root 'state'
    foreach ($dir in @($logDir, $stateDir)) {
        if (-not (Test-Path -LiteralPath $dir -PathType Container)) {
            [void](New-Item -ItemType Directory -Force -Path $dir)
        }
    }

    $raw = [Console]::In.ReadToEnd()
    $data = $raw | ConvertFrom-Json
    $modelObject = Get-Value -Object $data -Name 'model' -Default $null
    $modelId = [string](Get-Value -Object $modelObject -Name 'id' -Default '')
    $modelName = [string](Get-Value -Object $modelObject `
        -Name 'display_name' -Default $modelId)
    $effortObject = Get-Value -Object $data -Name 'effort' -Default $null
    $effort = [string](Get-Value -Object $effortObject `
        -Name 'level' -Default 'not_exposed')
    $costObject = Get-Value -Object $data -Name 'cost' -Default $null
    $cost = [double](Get-Value -Object $costObject `
        -Name 'total_cost_usd' -Default 0)
    $duration = [long](Get-Value -Object $costObject `
        -Name 'total_duration_ms' -Default 0)
    $context = Get-Value -Object $data -Name 'context_window' -Default $null
    $used = [double](Get-Value -Object $context `
        -Name 'used_percentage' -Default 0)
    $inputTokens = [long](Get-Value -Object $context `
        -Name 'total_input_tokens' -Default 0)
    $outputTokens = [long](Get-Value -Object $context `
        -Name 'total_output_tokens' -Default 0)

    $record = [ordered]@{
        captured_at_utc = [DateTime]::UtcNow.ToString('o')
        session_id = [string](Get-Value -Object $data `
            -Name 'session_id' -Default '')
        claude_code_version = [string](Get-Value -Object $data `
            -Name 'version' -Default '')
        model_id = $modelId
        model_display = $modelName
        effort = $effort
        total_cost_usd_telemetry = $cost
        total_duration_ms = $duration
        context_used_percent = $used
        total_input_tokens = $inputTokens
        total_output_tokens = $outputTokens
        rate_limits = Get-Value -Object $data -Name 'rate_limits' `
            -Default $null
    }
    $signature = ('{0}|{1}|{2}|{3}|{4}|{5}' -f
        $modelId,$effort,$cost,$duration,$inputTokens,$outputTokens)
    $lastPath = Join-Path $logDir 'status.last'
    $last = ''
    if (Test-Path -LiteralPath $lastPath -PathType Leaf) {
        $last = [System.IO.File]::ReadAllText($lastPath)
    }
    if ($signature -ne $last) {
        $line = $record | ConvertTo-Json -Depth 40 -Compress
        Write-Utf8NoBom -Path (Join-Path $logDir 'status.jsonl') `
            -Text ($line + [Environment]::NewLine) -Append
        Write-Utf8NoBom -Path $lastPath -Text $signature
    }

    $modelExposed = -not [string]::IsNullOrWhiteSpace($modelId)
    $modelVerified = (
        $modelId -match '(?i)fable' -and
        $modelId -match '5'
    )
    $modelMismatch = ($modelExposed -and -not $modelVerified)
    $effortExposed = (
        -not [string]::IsNullOrWhiteSpace($effort) -and
        $effort -ne 'not_exposed'
    )
    $effortMismatch = ($effortExposed -and $effort -ne 'xhigh')
    $verified = (-not $modelMismatch -and -not $effortMismatch)
    if (-not $verified) {
        $sessionId = [string](Get-Value -Object $data `
            -Name 'session_id' -Default '')
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
                model_observed = $modelId
                effort_observed = $effort
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
            reason = 'STATUS_MODEL_OR_EFFORT_MISMATCH'
            observed_model = $modelId
            observed_effort = $effort
            required_model = 'Fable 5'
            required_effort = 'xhigh'
            session_id = $sessionId
            event_count = @($events).Count
        }
        if (@($events).Count -le 1) {
            Write-Utf8NoBom -Path (Join-Path $stateDir 'MODEL_RETRY.json') `
                -Text (($modelEvent | ConvertTo-Json -Depth 20) +
                    [Environment]::NewLine)
            Write-Output (
                'RETRY REQUIRED model={0} effort={1}' -f $modelName,$effort
            )
        } else {
            $retryPath = Join-Path $stateDir 'MODEL_RETRY.json'
            if (Test-Path -LiteralPath $retryPath -PathType Leaf) {
                Remove-Item -LiteralPath $retryPath -Force
            }
            Write-Utf8NoBom -Path (Join-Path $stateDir 'MODEL_PAUSE.json') `
                -Text (($modelEvent | ConvertTo-Json -Depth 20) +
                    [Environment]::NewLine)
            Write-Output ('PAUSED model={0} effort={1}' -f
                $modelName,$effort)
        }
    } else {
        if ($effortExposed) {
            Write-Output (
                '{0} | effort {1} | context {2:N0}% | telemetry ${3:N2} | {4:N0}s' -f
                $modelName,$effort,$used,$cost,($duration / 1000)
            )
        } else {
            Write-Output (
                '{0} | effort NOT_EXPOSED (requested xhigh) | context {1:N0}% | telemetry ${2:N2} | {3:N0}s' -f
                $modelName,$used,$cost,($duration / 1000)
            )
        }
    }
} catch {
    Write-Output 'F06 telemetry unavailable; inspect .claude/hooks/hook_errors.log'
}
exit 0
