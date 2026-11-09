#!/usr/bin/env bash
# Start the policy server. Extra arguments go to serve_b1k.py, e.g. `docker run ... <image> --num-steps 10`.
# --offline-only (or AGENT_ENABLED=0): never contact OpenAI; the learned policy plays every task.
set -euo pipefail
cd "${B1K_ROOT:-/opt/b1k}"
MODEL_DIR=${POLICY_MODEL_DIR:-/opt/model}
CONFIG=$(ls "${MODEL_DIR}"/*.yaml | head -1)
OFFLINE=0; [[ ${AGENT_ENABLED:-1} == 1 ]] || OFFLINE=1
ARGS=()
for arg in "$@"; do
    if [[ $arg == --offline-only ]]; then OFFLINE=1; else ARGS+=("$arg"); fi
done
AGENT_ARGS=()
if [[ $OFFLINE == 1 ]]; then
    unset OPENAI_API_KEY
    echo "OFFLINE-ONLY mode: OpenAI is never contacted; the learned policy plays all tasks"
else
    AGENT_ARGS=(--agent)
    [[ -n ${OPENAI_API_KEY:-} ]] || echo "OPENAI_API_KEY is not set: the startup check will stop the server"
fi
exec python -u scripts/serve_b1k.py --port "${POLICY_PORT:-8000}" "${AGENT_ARGS[@]}" "${ARGS[@]}" \
    --policy.config "${CONFIG}" --policy.dir "${MODEL_DIR}"
