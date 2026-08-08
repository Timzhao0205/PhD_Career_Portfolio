[CmdletBinding()]
param()

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
$Root = $PSScriptRoot
Set-Location -LiteralPath $Root

function Assert-True {
    param(
        [Parameter(Mandatory = $true)][bool]$Condition,
        [Parameter(Mandatory = $true)][string]$Message
    )
    if (-not $Condition) { throw $Message }
}

try {
    $Required = @(
        'START.ps1',
        'PREFLIGHT.ps1',
        'START_HERE.md',
        'SYSTEM_PROMPT.md',
        'CLAUDE.md',
        'MODEL_PLAN.md',
        'IP_SCOPE.md',
        'SOURCE_POLICY.md',
        '.claude\settings.json',
        'inputs\HASHES.sha256',
        'inputs\prior_art_seeds.csv',
        'inputs\manuscript\source_original.zip',
        'inputs\manuscript\submission.pdf',
        'inputs\manuscript\source\regular_lsens\regular_lsens.tex',
        'state\STATE.json',
        'state\MODEL_LOG.csv',
        'schemas\OUTPUT_GATES.md'
    )
    foreach ($Relative in $Required) {
        $Path = Join-Path $Root $Relative
        Assert-True (Test-Path -LiteralPath $Path -PathType Leaf) (
            'Missing required file: {0}' -f $Relative
        )
    }

    foreach ($Relative in @('START.ps1', 'PREFLIGHT.ps1')) {
        $ScriptPath = Join-Path $Root $Relative
        $Tokens = $null
        $ParseErrors = $null
        $null = [System.Management.Automation.Language.Parser]::ParseFile(
            $ScriptPath,
            [ref]$Tokens,
            [ref]$ParseErrors
        )
        $ErrorList = @($ParseErrors)
        Assert-True ($ErrorList.Count -eq 0) (
            'PowerShell syntax error in {0}: {1}' -f
            $Relative, (($ErrorList | ForEach-Object { $_.Message }) -join '; ')
        )
    }

    $JsonFiles = @('.claude\settings.json', 'state\STATE.json')
    foreach ($Relative in $JsonFiles) {
        $Path = Join-Path $Root $Relative
        $null = Get-Content -Raw -LiteralPath $Path | ConvertFrom-Json
    }

    $Settings = Get-Content -Raw -LiteralPath (
        Join-Path $Root '.claude\settings.json'
    ) | ConvertFrom-Json
    Assert-True ($Settings.model -eq 'fable') 'settings.json must request fable.'
    Assert-True ($Settings.effortLevel -eq 'xhigh') 'settings.json must request xhigh.'
    Assert-True (-not [bool]$Settings.switchModelsOnFlag) (
        'switchModelsOnFlag must be false.'
    )
    Assert-True ($Settings.permissions.defaultMode -eq 'bypassPermissions') (
        'Default permission mode must be bypassPermissions.'
    )

    $AgentPolicy = @(
        @('s00-scope.md', 'claude-sonnet-5', 'medium'),
        @('s10-disclosure.md', 'claude-sonnet-5', 'high'),
        @('s20-prior-art.md', 'claude-sonnet-5', 'xhigh'),
        @('s30-ip-screen.md', 'fable', 'xhigh'),
        @('s40-uhv.md', 'fable', 'xhigh'),
        @('s50-arxiv.md', 'claude-sonnet-5', 'high'),
        @('s60-red-team.md', 'fable', 'xhigh'),
        @('s70-final.md', 'fable', 'xhigh')
    )
    foreach ($Rule in $AgentPolicy) {
        $AgentPath = Join-Path $Root ('.claude\agents\{0}' -f $Rule[0])
        Assert-True (Test-Path -LiteralPath $AgentPath -PathType Leaf) (
            'Missing stage agent: {0}' -f $Rule[0]
        )
        $AgentText = Get-Content -Raw -LiteralPath $AgentPath
        $ModelPattern = '(?m)^model:\s*{0}\s*$' -f [Regex]::Escape($Rule[1])
        $EffortPattern = '(?m)^effort:\s*{0}\s*$' -f [Regex]::Escape($Rule[2])
        Assert-True ($AgentText -match $ModelPattern) (
            'Model mismatch in agent {0}' -f $Rule[0]
        )
        Assert-True ($AgentText -match $EffortPattern) (
            'Effort mismatch in agent {0}' -f $Rule[0]
        )
        Assert-True ($AgentText -match '(?m)^permissionMode:\s*bypassPermissions\s*$') (
            'Permission mismatch in agent {0}' -f $Rule[0]
        )
    }

    $SeedPath = Join-Path $Root 'inputs\prior_art_seeds.csv'
    $SeedRows = @(Import-Csv -LiteralPath $SeedPath)
    Assert-True ($SeedRows.Count -gt 0) 'prior_art_seeds.csv has no data rows.'
    $SeedHeaders = @($SeedRows[0].PSObject.Properties.Name)
    foreach ($Header in @(
        'seed_id', 'kind', 'title', 'authority', 'year', 'identifier', 'url',
        'coverage_area', 'why_seeded', 'status'
    )) {
        Assert-True ($SeedHeaders -contains $Header) (
            'prior_art_seeds.csv is missing column: {0}' -f $Header
        )
    }
    $Coverage = @($SeedRows | Select-Object -ExpandProperty coverage_area -Unique)
    foreach ($Area in @(
        'gan_hall', 'fusion_hall', 'uhv_package', 'group_prior_work',
        'new_use', 'disclosure', 'arxiv', 'source_hygiene'
    )) {
        Assert-True ($Coverage -contains $Area) (
            'Prior-art seed coverage is missing: {0}' -f $Area
        )
    }

    $Claude = Get-Command claude -ErrorAction SilentlyContinue
    Assert-True ($null -ne $Claude) (
        'Claude Code is not installed or is not on PATH. See README.md.'
    )

    $VersionText = ((& claude --version 2>&1) | Out-String).Trim()
    Assert-True ($LASTEXITCODE -eq 0) 'claude --version failed.'
    Assert-True ($VersionText -match '(\d+\.\d+\.\d+)') (
        'Could not parse Claude Code version: {0}' -f $VersionText
    )
    $CurrentVersion = [Version]$Matches[1]
    $MinimumVersion = [Version]'2.1.219'
    Assert-True ($CurrentVersion -ge $MinimumVersion) (
        'Claude Code {0} is too old. Version 2.1.219 or newer is required.' -f
        $CurrentVersion
    )

    & claude auth status *> $null
    Assert-True ($LASTEXITCODE -eq 0) (
        'Claude authentication is not ready. Run claude once and sign in.'
    )

    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $SourceZip = Join-Path $Root 'inputs\manuscript\source_original.zip'
    $Archive = [IO.Compression.ZipFile]::OpenRead($SourceZip)
    try {
        Assert-True ($Archive.Entries.Count -eq 17) (
            'Unexpected manuscript source ZIP entry count.'
        )
        $TexEntries = @($Archive.Entries | Where-Object {
            $_.FullName -eq 'regular_lsens/regular_lsens.tex'
        })
        Assert-True ($TexEntries.Count -eq 1) (
            'regular_lsens.tex is missing from source ZIP.'
        )
    } finally {
        $Archive.Dispose()
    }

    $Pdf = Join-Path $Root 'inputs\manuscript\submission.pdf'
    $PdfStream = [IO.File]::OpenRead($Pdf)
    try {
        $Header = New-Object byte[] 4
        $Read = $PdfStream.Read($Header, 0, 4)
        $Magic = [Text.Encoding]::ASCII.GetString($Header)
        Assert-True ($Read -eq 4 -and $Magic -eq '%PDF') (
            'submission.pdf is not a valid PDF header.'
        )
    } finally {
        $PdfStream.Dispose()
    }

    $TexPath = Join-Path $Root (
        'inputs\manuscript\source\regular_lsens\regular_lsens.tex'
    )
    $Tex = Get-Content -Raw -LiteralPath $TexPath
    Assert-True ($Tex -match 'AlGaN/GaN Hall-Effect Sensor') (
        'Expected manuscript title was not found in regular_lsens.tex.'
    )
    Assert-True ($Tex -match 'grounded graphite shield') (
        'Expected publication packaging disclosure was not found.'
    )

    $HashFile = Join-Path $Root 'inputs\HASHES.sha256'
    foreach ($Line in Get-Content -LiteralPath $HashFile) {
        if ([string]::IsNullOrWhiteSpace($Line)) { continue }
        $Parts = $Line -split '\s{2,}', 2
        Assert-True ($Parts.Count -eq 2) ('Malformed hash line: {0}' -f $Line)
        $Expected = $Parts[0].Trim().ToLowerInvariant()
        $Relative = $Parts[1].Trim().Replace('/', '\')
        $Path = Join-Path $Root $Relative
        Assert-True (Test-Path -LiteralPath $Path -PathType Leaf) (
            'Hash target is missing: {0}' -f $Relative
        )
        $Actual = (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToLowerInvariant()
        Assert-True ($Actual -eq $Expected) ('Hash mismatch: {0}' -f $Relative)
    }

    $AllItems = @(Get-ChildItem -LiteralPath $Root -Recurse -Force)
    $TooLong = @($AllItems | Where-Object { $_.FullName.Length -ge 240 })
    Assert-True ($TooLong.Count -eq 0) (
        'A full path is 240 characters or longer. Move the package to C:\HSX_IP.'
    )
    $BadNames = @($AllItems | Where-Object {
        $_.Name -match '[<>:"/\\|?*]' -or $_.Name.EndsWith('.') -or
        $_.Name.EndsWith(' ')
    })
    Assert-True ($BadNames.Count -eq 0) 'A file has a Windows-incompatible name.'

    Write-Host 'PASS: required files, PowerShell AST syntax, JSON, agents, and source schema.' -ForegroundColor Green
    Write-Host 'PASS: manuscript ZIP/PDF, immutable hashes, and Windows paths.' -ForegroundColor Green
    Write-Host ('PASS: Claude Code {0}; authentication OK.' -f $CurrentVersion) -ForegroundColor Green
    Write-Host 'PASS: Fable/xhigh request, no silent safety fallback, and full-permission mode.' -ForegroundColor Green
    Write-Host 'PASS: no numeric source-count gate; evidence is judged by coverage and traceability.' -ForegroundColor Green
    exit 0
} catch {
    Write-Host ('PREFLIGHT FAILED: {0}' -f $_.Exception.Message) -ForegroundColor Red
    exit 1
}
