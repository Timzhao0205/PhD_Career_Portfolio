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

try {
    $root = [System.IO.Path]::GetFullPath(
        (Join-Path $PSScriptRoot '..\..')
    )
    $logDir = Join-Path $root 'logs'
    if (-not (Test-Path -LiteralPath $logDir -PathType Container)) {
        [void](New-Item -ItemType Directory -Force -Path $logDir)
    }
    $raw = [Console]::In.ReadToEnd()
    $record = [ordered]@{
        captured_at_utc = [DateTime]::UtcNow.ToString('o')
        payload = $null
        raw = $null
    }
    try {
        $record.payload = $raw | ConvertFrom-Json
    } catch {
        $record.raw = $raw
    }
    $line = $record | ConvertTo-Json -Depth 60 -Compress
    Write-Utf8NoBom -Path (Join-Path $logDir 'events.jsonl') `
        -Text ($line + [Environment]::NewLine) -Append
} catch {
    try {
        $fallback = Join-Path $PSScriptRoot 'hook_errors.log'
        $message = ('{0} EVENT_LOG {1}{2}' -f
            [DateTime]::UtcNow.ToString('o'),
            $_.Exception.Message,
            [Environment]::NewLine)
        Write-Utf8NoBom -Path $fallback -Text $message -Append
    } catch {
    }
}
exit 0

