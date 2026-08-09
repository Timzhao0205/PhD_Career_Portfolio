#requires -Version 5.1
[CmdletBinding()]
param()

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot

$Root = $PSScriptRoot
$Stages = @(
    '10_refresh','20_p4','30_redteam','40_select',
    '45_packs','50_deep','60_synth','70_audit'
)

function Write-Utf8NoBom {
    param([string]$Path, [string]$Text)
    $encoding = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Text, $encoding)
}

function Read-Json {
    param([string]$Path)
    return ([System.IO.File]::ReadAllText($Path) | ConvertFrom-Json)
}

& powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File (Join-Path $Root 'VALIDATE.ps1') -All
if ($LASTEXITCODE -ne 0) {
    Write-Host (
        'FAIL: final validation did not pass; RUN_COMPLETE was not written.'
    ) -ForegroundColor Red
    exit 1
}

$statusPath = Join-Path $Root 'logs\status.jsonl'
$status = $null
foreach ($line in [System.IO.File]::ReadAllLines($statusPath)) {
    if (-not [string]::IsNullOrWhiteSpace($line)) {
        $status = $line | ConvertFrom-Json
    }
}
if ($null -eq $status) {
    Write-Host 'FAIL: no status telemetry.' -ForegroundColor Red
    exit 1
}

$active = Read-Json (Join-Path $Root 'state\ACTIVE_SESSION.json')
$audit = Read-Json (Join-Path $Root 'outputs\70_audit\AUDIT.json')
$markers = @()
foreach ($stage in $Stages) {
    $path = Join-Path $Root "state\stages\$stage.json"
    $markers += [ordered]@{
        stage = $stage
        path = "state\stages\$stage.json"
        sha256 = (Get-FileHash -LiteralPath $path `
            -Algorithm SHA256).Hash.ToUpperInvariant()
    }
}

$record = [ordered]@{
    status = 'COMPLETE'
    completed_at_utc = [DateTime]::UtcNow.ToString('o')
    route_id = 'F06_INTERACTIVE_NOCAP_PS51_V1'
    session_id = [string]$active.session_id
    model_observed = [string]$status.model_id
    effort_observed = [string]$status.effort
    audit_verdict = [string]$audit.verdict
    final_output = 'outputs\70_audit\FINAL'
    package_defined_budget_stop = $false
    stage_markers = $markers
}
$path = Join-Path $Root 'state\RUN_COMPLETE.json'
Write-Utf8NoBom -Path $path -Text (
    ($record | ConvertTo-Json -Depth 30) + [Environment]::NewLine
)

& powershell.exe -NoProfile -ExecutionPolicy Bypass `
    -File (Join-Path $Root 'VALIDATE.ps1') -All
if ($LASTEXITCODE -ne 0) {
    Remove-Item -LiteralPath $path -Force
    Write-Host (
        'FAIL: post-write validation failed; RUN_COMPLETE was removed.'
    ) -ForegroundColor Red
    exit 1
}

Write-Host (
    'PASS: RUN_COMPLETE written; canonical release is ' +
    'outputs\70_audit\FINAL.'
) -ForegroundColor Green
exit 0

