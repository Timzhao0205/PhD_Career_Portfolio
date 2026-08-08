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
    $logDir = Join-Path $root 'logs'
    $stateDir = Join-Path $root 'state'
    $raw = [Console]::In.ReadToEnd()
    $event = $raw | ConvertFrom-Json
    $record = [ordered]@{
        captured_at_utc = [DateTime]::UtcNow.ToString('o')
        event = 'Stop'
        session_id = [string]$event.session_id
        stop_hook_active = [bool]$event.stop_hook_active
        last_assistant_message = [string]$event.last_assistant_message
    }
    $line = $record | ConvertTo-Json -Depth 20 -Compress
    Write-Utf8NoBom -Path (Join-Path $logDir 'events.jsonl') `
        -Text ($line + [Environment]::NewLine) -Append

    foreach ($pauseName in @(
        'MODEL_RETRY.json','MODEL_PAUSE.json','PAUSE.json'
    )) {
        if (Test-Path -LiteralPath (Join-Path $stateDir $pauseName) `
            -PathType Leaf) {
            exit 0
        }
    }

    $complete = Join-Path $stateDir 'RUN_COMPLETE.json'
    if (Test-Path -LiteralPath $complete -PathType Leaf) {
        $validator = Join-Path $root 'VALIDATE.ps1'
        & powershell.exe -NoProfile -ExecutionPolicy Bypass `
            -File $validator -All -Quiet *> $null
        if ($LASTEXITCODE -eq 0) {
            exit 0
        }
        $response = [ordered]@{
            decision = 'block'
            reason = (
                'RUN_COMPLETE exists but final validation failed. Read the ' +
                'visible validator output by running: powershell -NoProfile ' +
                '-ExecutionPolicy Bypass -File .\VALIDATE.ps1 -All. Repair ' +
                'the exact failures and revalidate before stopping.'
            )
        }
        Write-Output ($response | ConvertTo-Json -Compress)
        exit 0
    }

    $response = [ordered]@{
        decision = 'block'
        reason = (
            'The Folder 06 run is not complete. Continue autonomously. Read ' +
            'RUNBOOK.md and state/stages, perform the next required pilot or ' +
            'stage, validate it, checkpoint it, and proceed. Do not stop to ' +
            'summarize progress. If a genuine external blocker requires a ' +
            'protected pause, write state/PAUSE.json with evidence first.'
        )
    }
    Write-Output ($response | ConvertTo-Json -Compress)
} catch {
    $response = [ordered]@{
        decision = 'block'
        reason = (
            'The completion guard encountered an error. Repair project ' +
            'logging/validation before stopping: ' + $_.Exception.Message
        )
    }
    Write-Output ($response | ConvertTo-Json -Compress)
}
exit 0
