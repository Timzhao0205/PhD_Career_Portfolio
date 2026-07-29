#requires -Version 5.1
<#
  run.ps1 - one-command automation for the "Magnetic Sensors" review paper.

  Usage (from anywhere; the script anchors to its own folder):
      powershell -ExecutionPolicy Bypass -File .\run.ps1

  Common variants:
      .\run.ps1                         # run every stage not already done
      .\run.ps1 -OnlyStage 10,20        # just titles + outlines (the Friday deliverable)
      .\run.ps1 -FromStage 30           # resume from the sensor-taxonomy stage onward
      .\run.ps1 -OnlyStage 30 -Force    # re-run one stage to produce a patch
      .\run.ps1 -DryRun                 # print the plan + model/effort per stage, do nothing
      .\run.ps1 -Safe                   # scoped permissions instead of skip-permissions
      .\run.ps1 -SkipHtml               # don't regenerate the .html mirrors

  Prereqs: Claude Code installed and logged in (you said it already is).
           Optional for HTML mirrors:  pip install markdown
#>
[CmdletBinding()]
param(
    [string[]]$OnlyStage,          # run only these stages (match by number or full key)
    [string]  $FromStage,          # run this stage and everything after it
    [switch]  $Force,              # re-run stages even if marked done (use for patches)
    [switch]  $DryRun,             # show the plan and exit
    [switch]  $ContinueOnError,    # keep going past a failed stage (default: stop)
    [switch]  $Safe,               # scoped permission mode instead of --dangerously-skip-permissions
    [switch]  $SkipHtml            # skip the python HTML-mirror step
)

# 'Continue' (not 'Stop'): claude may write benign progress/warnings to stderr,
# which under 'Stop' + capture can throw and false-fail a good stage. We judge
# success by exit code + JSON subtype instead. Fatal preflight uses explicit throw.
$ErrorActionPreference = 'Continue'
Set-Location -LiteralPath $PSScriptRoot   # everything below is relative to this folder

# Force UTF-8 across the native-process boundary (prompts and results contain
# unicode; PS 5.1 defaults would mangle it). This governs bytes we pipe into
# claude's stdin and how we decode its stdout.
$utf8 = New-Object System.Text.UTF8Encoding $false
$OutputEncoding = $utf8
try { [Console]::OutputEncoding = $utf8 } catch {}

# ---------------------------------------------------------------------------
# 1. BUDGET CONFIG  --  edit freely. This is your cost/quality control panel.
#    Model  : 'FABLE' (-> $FableModel), or an alias 'opus'/'sonnet'/'haiku',
#             or a full id like 'claude-opus-4-8'.
#    Effort : low | medium | high | xhigh | max   (sets CLAUDE_CODE_EFFORT_LEVEL)
#    MaxTurns: hard ceiling on agentic tool calls for that stage (safety valve).
# ---------------------------------------------------------------------------
$FableModel       = 'claude-fable-5'   # change here if your account exposes a different id
$FallbackForFable = 'opus'             # used automatically if the Fable preflight fails

$Stages = [ordered]@{
  '00_target_journal_brief'    = @{ Prompt='prompts/00_target_journal_brief.md';    Model='sonnet'; Effort='low';    MaxTurns=30; Desc='Fetch + digest MDPI Sensors author requirements' }
  '10_titles'                  = @{ Prompt='prompts/10_titles.md';                  Model='FABLE';  Effort='high';   MaxTurns=20; Desc='15 title options' }
  '20_outlines'                = @{ Prompt='prompts/20_outlines.md';                Model='FABLE';  Effort='high';   MaxTurns=25; Desc='3-4 full outlines with subtopics' }
  '30_litreview_sensor_types'  = @{ Prompt='prompts/30_litreview_sensor_types.md';  Model='FABLE';  Effort='high';   MaxTurns=90; Desc='Sensor taxonomy: commercial + pioneering, strengths/weaknesses' }
  '40_litreview_applications'  = @{ Prompt='prompts/40_litreview_applications.md';  Model='opus';   Effort='high';   MaxTurns=90; Desc='Applications: energy, transportation, industrial, biomed' }
  '50_litreview_future_methods'= @{ Prompt='prompts/50_litreview_future_methods.md';Model='FABLE';  Effort='high';   MaxTurns=90; Desc='Data-driven modeling, ML control, multimodal digital twin' }
  '60_standards_and_business'  = @{ Prompt='prompts/60_standards_and_business.md';  Model='opus';   Effort='high';   MaxTurns=70; Desc='Standards + business/investor potential' }
  '70_bibliography'            = @{ Prompt='prompts/70_bibliography.md';            Model='sonnet'; Effort='medium'; MaxTurns=80; Desc='Verify DOIs, flag non-peer-reviewed, build .bib + registry' }
  '80_assemble_deliverable'    = @{ Prompt='prompts/80_assemble_deliverable.md';    Model='FABLE';  Effort='high';   MaxTurns=40; Desc='Merge into the deliverable pack + coverage/gap matrix' }
  '90_patch_notes'             = @{ Prompt='prompts/90_patch_notes.md';             Model='haiku';  Effort='low';    MaxTurns=15; Desc='Run digest + patch notes + NOTES.md update' }
}

# ---------------------------------------------------------------------------
# 2. Setup: run folder, logging, permission args
# ---------------------------------------------------------------------------
$stamp   = Get-Date -Format 'yyyy-MM-dd_HHmmss'
$logRoot = Join-Path 'logs' "run_$stamp"
New-Item -ItemType Directory -Force -Path $logRoot,'outputs','refs_raw','.state' | Out-Null
$costLog  = Join-Path $logRoot 'costs.jsonl'
$meLog    = Join-Path $logRoot 'MODEL_EFFORT_LOG.md'
$sharedSys = Get-Content -Raw -Encoding UTF8 -LiteralPath 'prompts/_shared_system.md'

"# Model & effort log - run $stamp`n" | Set-Content -Encoding utf8 $meLog
"| stage | model | effort | max-turns | status | cost (USD) | seconds |" | Add-Content $meLog
"|---|---|---|---|---|---|---|" | Add-Content $meLog

if ($Safe) {
    $PermArgs = @('--permission-mode','acceptEdits','--allowedTools','Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,TodoWrite')
} else {
    $PermArgs = @('--dangerously-skip-permissions')
}

function Write-Head($msg){ Write-Host ""; Write-Host "==== $msg ====" -ForegroundColor Cyan }

# ---------------------------------------------------------------------------
# 3. Preflight: claude present? logged in? is Fable reachable?
# ---------------------------------------------------------------------------
Write-Head "Preflight"
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    throw "Claude Code CLI ('claude') not found on PATH. Install it and log in, then re-run."
}
Write-Host ("claude: " + ((claude --version) 2>&1 | Select-Object -First 1))

function Test-Model($model){
    try {
        $raw = ('reply with the single word READY and nothing else' |
                 & claude -p --model $model --max-turns 2 --output-format json 2>$null) | Out-String
        if ($LASTEXITCODE -ne 0) { return $false }
        $j = $raw | ConvertFrom-Json
        return ("$($j.result)" -match 'READY')
    } catch { return $false }
}

$useFable = $true
Write-Host "Checking Fable 5 availability ($FableModel) ..." -NoNewline
if (Test-Model $FableModel) { Write-Host " OK" -ForegroundColor Green }
else {
    $useFable = $false
    Write-Host " NOT AVAILABLE" -ForegroundColor Yellow
    Write-Warning "Fable 5 ('$FableModel') did not respond. FABLE stages will fall back to '$FallbackForFable'."
    Write-Warning "If you believe you have access, check the id in `$FableModel at the top of run.ps1 and your plan, then re-run."
}
function Resolve-Model($m){ if ($m -eq 'FABLE'){ if($useFable){$FableModel}else{$FallbackForFable} } else { $m } }

# ---------------------------------------------------------------------------
# 4. Decide which stages to run
# ---------------------------------------------------------------------------
$allKeys = @($Stages.Keys)
function Match-Stage($token){ $allKeys | Where-Object { $_ -eq $token -or $_ -like "$token*" -or ($_ -split '_')[0] -eq $token } }

$selected = $allKeys
if ($OnlyStage) {
    $selected = @(); foreach($t in $OnlyStage){ $selected += Match-Stage $t }
    $selected = $selected | Select-Object -Unique
}
elseif ($FromStage) {
    $start = @(Match-Stage $FromStage)[0]
    if (-not $start) { throw "FromStage '$FromStage' matched no stage." }
    $i = [array]::IndexOf($allKeys,$start)
    $selected = $allKeys[$i..($allKeys.Count-1)]
}

Write-Head "Plan"
$idx=0
foreach($k in $allKeys){
    $run = $selected -contains $k
    $done = Test-Path (Join-Path '.state' "$k.done")
    $willRun = $run -and ($Force -or -not $done)
    $cfg = $Stages[$k]
    $mdl = Resolve-Model $cfg.Model
    $tag = if(-not $run){'skip (not selected)'} elseif($done -and -not $Force){'skip (already done)'} else {'RUN'}
    $idx++
    Write-Host ("  [{0,2}] {1,-30} {2,-16} effort={3,-6} {4}" -f $idx,$k,$mdl,$cfg.Effort,$tag)
}
if ($DryRun) { Write-Host "`n(dry run - nothing executed)`n" -ForegroundColor Yellow; return }

# ---------------------------------------------------------------------------
# 5. Run stages
# ---------------------------------------------------------------------------
$grandTotal = 0.0
foreach($key in $allKeys){
    if ($selected -notcontains $key) { continue }
    $marker = Join-Path '.state' "$key.done"
    if ((Test-Path $marker) -and -not $Force) { continue }

    $cfg    = $Stages[$key]
    $model  = Resolve-Model $cfg.Model
    $effort = $cfg.Effort
    $prompt = $cfg.Prompt
    if (-not (Test-Path $prompt)) { Write-Warning "Missing prompt $prompt - skipping $key"; continue }

    Write-Head "$key  ($($cfg.Desc))"
    Write-Host ("model={0}  effort={1}  max-turns={2}" -f $model,$effort,$cfg.MaxTurns)

    $env:CLAUDE_CODE_EFFORT_LEVEL = $effort     # per-stage effort (picked up by the CLI)
    $jsonFile = Join-Path $logRoot "$key.json"
    $errFile  = Join-Path $logRoot "$key.err.txt"
    $outFile  = Join-Path $logRoot "$key.result.md"

    # We fold the shared rules into the piped prompt (stdin) rather than passing
    # them via --append-system-prompt: the shared prompt is quote-heavy and PS 5.1
    # mangles quote-heavy native arguments. stdin is raw and safe.
    $stagePrompt = Get-Content -Raw -Encoding UTF8 -LiteralPath $prompt
    $fullPrompt  = $sharedSys + "`n`n===== STAGE INSTRUCTIONS =====`n`n" + $stagePrompt

    $claudeArgs = @('-p','--model',$model,'--max-turns',$cfg.MaxTurns,'--output-format','json') + $PermArgs

    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    $exit = 0; $raw = ''
    try {
        $raw = ($fullPrompt | & claude @claudeArgs 2>$errFile) | Out-String
        $exit = $LASTEXITCODE
    } catch { $exit = 1; ($_ | Out-String) | Set-Content -Encoding UTF8 $errFile }
    $sw.Stop(); $secs = [math]::Round($sw.Elapsed.TotalSeconds,1)
    $raw | Set-Content -Encoding UTF8 -LiteralPath $jsonFile   # keep the raw JSON for audit

    $cost = 0.0; $subtype=''; $sid=''
    try {
        $res = $raw | ConvertFrom-Json
        if ($res.total_cost_usd) { $cost = [double]$res.total_cost_usd }
        $subtype = "$($res.subtype)"; $sid = "$($res.session_id)"
        if ($res.result) { "$($res.result)" | Set-Content -Encoding UTF8 $outFile }
    } catch { }

    $ok = ($exit -eq 0 -and $subtype -ne 'error_max_turns' -and $subtype -ne 'error_during_execution')
    $status = if($ok){'ok'}else{'FAIL'}
    $grandTotal += $cost

    # structured cost line + human table row
    ([pscustomobject]@{ stage=$key; model=$model; effort=$effort; status=$status;
                        cost_usd=$cost; seconds=$secs; session_id=$sid; subtype=$subtype
    } | ConvertTo-Json -Compress) | Add-Content $costLog
    "| $key | $model | $effort | $($cfg.MaxTurns) | $status | $([math]::Round($cost,4)) | $secs |" | Add-Content $meLog

    if ($ok) {
        "done $stamp model=$model effort=$effort cost=$cost secs=$secs" | Set-Content $marker
        Write-Host ("  -> {0}   `$ {1}   {2}s" -f $status,[math]::Round($cost,4),$secs) -ForegroundColor Green
    } else {
        Write-Host ("  -> {0}  (exit={1} subtype={2})  see {3}" -f $status,$exit,$subtype,$errFile) -ForegroundColor Red
        if (-not $ContinueOnError) {
            Write-Warning "Stopping. Fix the issue, then resume with:  .\run.ps1 -FromStage $($key.Split('_')[0])"
            break
        }
    }
}

Remove-Item Env:CLAUDE_CODE_EFFORT_LEVEL -ErrorAction SilentlyContinue

# ---------------------------------------------------------------------------
# 6. HTML mirrors (optional, on-convention with your other reports)
# ---------------------------------------------------------------------------
if (-not $SkipHtml) {
    Write-Head "HTML mirrors"
    $py = Get-Command python -ErrorAction SilentlyContinue
    if (-not $py) { $py = Get-Command py -ErrorAction SilentlyContinue }
    if ($py) {
        try { & $py.Source 'tools/build_html.py'; if($LASTEXITCODE -ne 0){ Write-Warning "build_html.py exited $LASTEXITCODE (mirrors skipped; markdown is still the source of truth)." } }
        catch { Write-Warning "HTML mirror step failed: $($_.Exception.Message)" }
    } else { Write-Warning "python not found - skipping HTML mirrors. (Markdown outputs are unaffected.)" }
}

# ---------------------------------------------------------------------------
# 7. Summary
# ---------------------------------------------------------------------------
Write-Head "Summary"
Write-Host ("Total spend this run: `$ {0}" -f [math]::Round($grandTotal,4)) -ForegroundColor Cyan
Write-Host "Per-stage log:  $meLog"
Write-Host "Cost detail:    $costLog"
Write-Host "Deliverables:   .\outputs\   (start with 00_DELIVERABLE_paper_plan.md, 10_titles.md, 20_outlines.md)"
Write-Host "Patch notes:    .\outputs\PATCH_NOTES.md   and   .\NOTES.md"
Write-Host ""
Write-Host "To patch/refine one part later, e.g. the future-methods section:" -ForegroundColor Gray
Write-Host "    .\run.ps1 -OnlyStage 50 -Force" -ForegroundColor Gray
