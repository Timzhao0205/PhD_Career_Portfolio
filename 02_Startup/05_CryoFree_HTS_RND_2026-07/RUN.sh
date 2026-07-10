#!/usr/bin/env bash
# =============================================================================
# ONE-COMMAND AUTONOMOUS RUNNER (macOS / Linux)
# Usage:  ./RUN.sh            # default 2,000,000-token budget ceiling
#         ./RUN.sh 5000000    # custom ceiling
# Runs the full cryogen-free discovery pipeline hands-off, auto-resuming across
# budget/interruption checkpoints until W5 completes. Logs to run_console.log.
# =============================================================================
set -uo pipefail
cd "$(dirname "$0")"
CEIL="${1:-2000000}"
LOG="run_console.log"
MAXPASS=12   # safety cap on resume loops

echo "[RUN] $(date) starting autonomous pipeline, budget ceiling=$CEIL" | tee -a "$LOG"

if ! command -v claude >/dev/null 2>&1; then
  echo "[RUN] ERROR: 'claude' CLI not found on PATH. Install Claude Code first." | tee -a "$LOG"; exit 1
fi

pass=0
while [ "$pass" -lt "$MAXPASS" ]; do
  pass=$((pass+1))
  echo "[RUN] pass $pass $(date)" | tee -a "$LOG"
  # Headless, non-interactive, permissions pre-granted via settings.json bypass.
  claude -p "/autorun $CEIL" \
         --permission-mode bypassPermissions \
         --dangerously-skip-permissions \
         >> "$LOG" 2>&1
  # Completion check: RUN_STATE phase reaching W5_done ends the loop.
  phase="$(python3 -c "import json;print(json.load(open('80_STATE/RUN_STATE.json')).get('phase',''))" 2>/dev/null || echo '')"
  echo "[RUN] pass $pass finished; phase=$phase" | tee -a "$LOG"
  case "$phase" in
    *W5_done*|*COMPLETE*|*complete*) echo "[RUN] pipeline complete." | tee -a "$LOG"; break;;
  esac
  # If it stopped for budget, RUN_STATE.notes carries RESUME_HERE; loop resumes.
  sleep 2
done

echo "[RUN] done after $pass pass(es). See 10_MISSION/RND_STRATEGY_CryoFree.md and 98_CLAUDE_METRICS/RUN_REPORT.md" | tee -a "$LOG"
