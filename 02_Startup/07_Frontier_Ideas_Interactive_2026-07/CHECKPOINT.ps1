#requires -Version 5.1
[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet(
        '10_refresh','20_p4','30_redteam','40_select',
        '45_packs','50_deep','60_synth','70_audit'
    )]
    [string]$Stage,
    [switch]$Pilot,
    [switch]$Verify
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$Root = $PSScriptRoot
$target = if ($Pilot) {
    Join-Path $Root "pilot\$Stage"
} else {
    Join-Path $Root "outputs\$Stage"
}
$marker = if ($Pilot) {
    Join-Path $target 'PILOT_COMPLETE.json'
} else {
    Join-Path $Root "state\stages\$Stage.json"
}

function Write-Utf8NoBom {
    param([string]$Path, [string]$Text)
    $encoding = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Text, $encoding)
}

function Read-Json {
    param([string]$Path)
    return ([System.IO.File]::ReadAllText($Path) | ConvertFrom-Json)
}

function Get-LatestStatus {
    $path = Join-Path $Root 'logs\status.jsonl'
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw 'Missing logs\status.jsonl.'
    }
    $last = $null
    foreach ($line in [System.IO.File]::ReadAllLines($path)) {
        if (-not [string]::IsNullOrWhiteSpace($line)) {
            $last = $line | ConvertFrom-Json
        }
    }
    if ($null -eq $last) {
        throw 'No status telemetry was recorded.'
    }
    return $last
}

function Get-FileRecords {
    param([string]$Directory, [string]$ExcludedPath)
    $records = @()
    foreach ($file in @(Get-ChildItem -LiteralPath $Directory -File `
        -Recurse | Sort-Object FullName)) {
        if ($file.FullName -eq $ExcludedPath -or $file.Name -eq '.keep') {
            continue
        }
        $relative = $file.FullName.Substring($Root.Length)
        $relative = $relative.TrimStart([char[]]"\/")
        $records += [ordered]@{
            path = $relative
            bytes = [long]$file.Length
            sha256 = (Get-FileHash -LiteralPath $file.FullName `
                -Algorithm SHA256).Hash.ToUpperInvariant()
        }
    }
    return @($records)
}

function Invoke-Validator {
    $arguments = @(
        '-NoProfile','-ExecutionPolicy','Bypass',
        '-File',(Join-Path $Root 'VALIDATE.ps1'),
        '-Stage',$Stage
    )
    if ($Pilot) {
        $arguments += '-Pilot'
    }
    & powershell.exe @arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Validation failed for $Stage."
    }
}

if ($Verify) {
    if (-not (Test-Path -LiteralPath $marker -PathType Leaf)) {
        Write-Host "FAIL: Missing checkpoint $marker" -ForegroundColor Red
        exit 1
    }
    try {
        Invoke-Validator
        $saved = Read-Json $marker
        if ([string]$saved.stage -ne $Stage -or
            [string]$saved.status -ne 'COMPLETE') {
            throw 'Checkpoint stage or status is invalid.'
        }
        $savedEffort = [string]$saved.effort_observed
        if ([string]$saved.model_observed -notmatch '(?i)fable' -or
            [string]$saved.model_observed -notmatch '5' -or
            @('xhigh','not_exposed') -notcontains $savedEffort -or
            [string]$saved.effort_requested -ne 'xhigh') {
            throw (
                'Checkpoint model/effort evidence is invalid. The model must ' +
                'be Fable 5; effort must be xhigh or honestly NOT_EXPOSED ' +
                'with requested xhigh.'
            )
        }
        foreach ($entry in @($saved.output_files)) {
            $path = [string]$entry.path
            if ([System.IO.Path]::IsPathRooted($path) -or
                $path -match '(^|[\\/])\.\.([\\/]|$)') {
                throw "Unsafe checkpoint path: $path"
            }
            $full = Join-Path $Root $path
            if (-not (Test-Path -LiteralPath $full -PathType Leaf)) {
                throw "Missing checkpoint file: $path"
            }
            $actual = (Get-FileHash -LiteralPath $full `
                -Algorithm SHA256).Hash.ToUpperInvariant()
            if ($actual -ne ([string]$entry.sha256).ToUpperInvariant()) {
                throw "Checkpoint hash mismatch: $path"
            }
        }
        Write-Host "PASS: $Stage checkpoint is valid." -ForegroundColor Green
        exit 0
    } catch {
        Write-Host ("FAIL: {0}" -f $_.Exception.Message) -ForegroundColor Red
        exit 1
    }
}

try {
    Invoke-Validator
    if (-not (Test-Path -LiteralPath $target -PathType Container)) {
        throw "Missing checkpoint target: $target"
    }
    $status = Get-LatestStatus
    $model = [string]$status.model_id
    $effort = [string]$status.effort
    if ($model -notmatch '(?i)fable' -or $model -notmatch '5') {
        throw "Observed model is not verifiably Fable 5: $model"
    }
    if (@('xhigh','not_exposed') -notcontains $effort) {
        throw "Observed effort explicitly conflicts with xhigh: $effort"
    }

    $sessionId = ''
    $activePath = Join-Path $Root 'state\ACTIVE_SESSION.json'
    if (Test-Path -LiteralPath $activePath -PathType Leaf) {
        $active = Read-Json $activePath
        $sessionId = [string]$active.session_id
    }
    $files = @(Get-FileRecords -Directory $target `
        -ExcludedPath $marker)
    if ($files.Count -lt 1) {
        throw 'Checkpoint target has no files.'
    }
    $record = [ordered]@{
        stage = $Stage
        kind = if ($Pilot) { 'PILOT' } else { 'FULL' }
        status = 'COMPLETE'
        validated_at_utc = [DateTime]::UtcNow.ToString('o')
        session_id = $sessionId
        model_observed = $model
        effort_observed = $effort
        effort_requested = 'xhigh'
        claude_code_version = [string]$status.claude_code_version
        total_cost_usd_telemetry = [double]$status.total_cost_usd_telemetry
        total_duration_ms = [long]$status.total_duration_ms
        total_input_tokens = [long]$status.total_input_tokens
        total_output_tokens = [long]$status.total_output_tokens
        output_files = $files
    }
    $parent = Split-Path -Parent $marker
    if (-not (Test-Path -LiteralPath $parent -PathType Container)) {
        [void](New-Item -ItemType Directory -Force -Path $parent)
    }
    Write-Utf8NoBom -Path $marker -Text (
        ($record | ConvertTo-Json -Depth 30) + [Environment]::NewLine
    )
    Write-Host "PASS: $Stage checkpoint created." -ForegroundColor Green
    exit 0
} catch {
    Write-Host ("FAIL: {0}" -f $_.Exception.Message) -ForegroundColor Red
    exit 1
}
