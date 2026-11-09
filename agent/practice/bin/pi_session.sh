#!/usr/bin/env bash
# Start (or resume) the practice agent for a run, in the foreground; run it inside tmux.
#   agent/practice/bin/pi_session.sh RUN [MODEL]
# MODEL defaults to openai/gpt-6-astra (needs OPENAI_API_KEY); openai-codex/gpt-6-astra uses a ChatGPT/Codex
# subscription after `/login` in Pi. FORK_FROM=<session.jsonl> starts a new practicer from another task's session
# (we often started a task from the practicer of a related one). PI_COST_LIMIT caps the session's spend (USD).
set -euo pipefail
RUN_NAME=$1; MODEL=${2:-openai/gpt-6-astra}
REPO=$(cd "$(dirname "$0")/../../.." && pwd)
CAMPAIGN=${PRACTICE_HOME:-$REPO/.practice}/campaign
RUN=$CAMPAIGN/runs/$RUN_NAME
[ -f "$RUN/SETUP.json" ] || { echo "no run at $RUN (bin/make_run.py first)" >&2; exit 2; }
EXT=$REPO/agent/pi/extensions
export BEHAVIOR_SIM_RUN_DIR=$RUN BEHAVIOR_PRACTICE_LOOP=1 PI_COST_LIMIT=${PI_COST_LIMIT:-400}
mkdir -p "$RUN/sessions"
ARGS=(--model "$MODEL" --thinking "${THINKING:-medium}" --session-dir "$RUN/sessions"
      --no-extensions -e builtin:codemode -e "$EXT/observation_delivery.ts" -e "$EXT/cost-guard.ts"
      -e "$EXT/auth-isolation.ts" -e "$EXT/practice-loop.ts"
      --skill "$CAMPAIGN/skill/behavior-sim-control/SKILL.md" --tools read,bash,edit,write,codemode)
cd "$CAMPAIGN"
if ls "$RUN"/sessions/*.jsonl >/dev/null 2>&1; then
  exec pi "${ARGS[@]}" --continue
elif [ -n "${FORK_FROM:-}" ]; then
  exec pi "${ARGS[@]}" --fork "$FORK_FROM" "Read $RUN/PRACTICER-KICKOFF.md and follow it."
else
  exec pi "${ARGS[@]}" "Read $RUN/PRACTICER-KICKOFF.md and follow it."
fi
