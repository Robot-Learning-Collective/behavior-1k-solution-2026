#!/usr/bin/env bash
# Start the persistent practice simulator for one training instance.
#   agent/practice/bin/worker.sh TASK INSTANCE RUN      e.g. worker.sh clean_a_trumpet 20 trumpet-01
# Needs: SIM_PY (Python of the Isaac Sim 5.1 + OmniGibson environment), OMNIGIBSON_DATA_PATH (with
# 2026-challenge-task-instances) and optionally SIM_PYTHONPATH, ASTRA_GPU_UUID, PRACTICE_HOME (default <repo>/.practice).
# The worker writes <PRACTICE_HOME>/runtime/RUN/queue/ready.json when it is READY (about 2-10 min).
set -euo pipefail
TASK=$1; INST=$2; RUN=$3
(( INST >= 10 && INST <= 300 )) || { echo "training instance 10..300 only" >&2; exit 2; }
: "${SIM_PY:?set SIM_PY to the simulator environment python}" "${OMNIGIBSON_DATA_PATH:?set OMNIGIBSON_DATA_PATH}"
REPO=$(cd "$(dirname "$0")/../../.." && pwd)
RT=${PRACTICE_HOME:-$REPO/.practice}/runtime/$RUN
SCENE=$(ls "$OMNIGIBSON_DATA_PATH"/2026-challenge-task-instances/scenes/*/json/*_task_"${TASK}"_0_0_template.json 2>/dev/null \
        | head -1 | awk -F/ '{print $(NF-2)}')
[ -n "$SCENE" ] || { echo "no scene template for $TASK under $OMNIGIBSON_DATA_PATH" >&2; exit 2; }
if [ -f "$RT/worker.pid" ] && kill -0 "$(cat "$RT/worker.pid")" 2>/dev/null; then
  echo "worker already running: pid $(cat "$RT/worker.pid")"; exit 0
fi
mkdir -p "$RT/queue" "$RT/artifacts"
unset OPENAI_API_KEY ANTHROPIC_API_KEY GEMINI_API_KEY   # the simulator never needs model credentials
rm -f "$RT/queue/ready.json" "$RT/queue/QUIT"
ASTRA_WORK_DIR=$RT/queue ASTRA_RUNTIME_ROOT=$RT ASTRA_ISOLATE_CACHES=${ASTRA_ISOLATE_CACHES:-0} \
  OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=1 PXR_WORK_THREAD_LIMIT=4 OMNIGIBSON_HEADLESS=1 \
  PYTHONPATH="${SIM_PYTHONPATH:-}" \
  setsid nohup "$SIM_PY" -u "$REPO/agent/practice/worker.py" --task "$TASK" --scene "$SCENE" --instance "$INST" \
    --artifacts "$RT/artifacts" > "$RT/worker.log" 2>&1 < /dev/null &
echo $! > "$RT/worker.pid"
echo "worker pid $(cat "$RT/worker.pid"): $TASK scene=$SCENE instance=$INST log=$RT/worker.log"
