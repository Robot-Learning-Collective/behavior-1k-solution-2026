# syntax=docker/dockerfile:1.7
# BEHAVIOR Challenge 2026 policy server: the learned policy for every task, and the GPT-6 Astra agent for the
# tasks enabled in agent/tasks/tasks.json (agent/README.md).
#
# Serves the BEHAVIOR-1K websocket protocol on port 8000 (`/healthz` health check). OmniGibson runs outside the
# container (upstream `python -m omnigibson.eval.eval`); this image holds the policy, its checkpoint, the agent and
# the evaluator-side protocol code from BEHAVIOR-1K v3.9.3-post2.
#
# Build with submission/build.sh, which supplies the named contexts:
#   b1k    = BEHAVIOR-1K v3.9.3-post2, git-archived OmniGibson/ and bddl3/ plus the 2026 task table
#   openpi = the pinned openpi submodule commit with patches/openpi-*.patch applied
#   model  = the inference checkpoint directory (params/, assets/, _CHECKPOINT_METADATA, recipe yaml)
# The agent's frozen contexts come from agent/frozen/ (the bundle, see agent/eval/frozen.py).
# The OpenAI key is never part of the image: pass it at `docker run`.

FROM node:22.22.3-bookworm-slim AS agent-pi
RUN npm install --prefix /opt/pi --save-exact '@earendil-works/pi-coding-agent@1.2.0'

# Frozen practice sessions, reassembled from the bundle and checked against tasks.json; only the result is kept.
# AGENT_BUNDLE=optional builds without the bundle: missing tasks are disabled and the learned policy plays them.
FROM python:3.11.13-slim-bookworm AS agent-contexts
ARG AGENT_BUNDLE=required
WORKDIR /opt/b1k
COPY agent ./agent
RUN if [ "$AGENT_BUNDLE" = optional ]; then python -m agent.eval.frozen --disable-missing; \
    else python -m agent.eval.frozen; fi && rm -rf agent/frozen

# Checkpoint-free image: agent tests at build time, agent-only server at run time (no learned policy).
FROM python:3.11.13-slim-bookworm AS agent-check
COPY --from=agent-pi /usr/local/bin/node /usr/local/bin/node
COPY --from=agent-pi /opt/pi /opt/pi
RUN pip install --no-cache-dir numpy==1.26.4 pillow==10.4.0 msgpack==1.1.0 websockets==15.0.1
ENV PATH=/opt/pi/node_modules/.bin:$PATH PI_CODING_AGENT_DIR=/tmp/behavior-agent/auth \
    B1K_AGENT_RUN_ROOT=/tmp/behavior-agent/rollouts
WORKDIR /opt/b1k
COPY --from=agent-contexts /opt/b1k/agent ./agent
COPY src/b1k/policies/agent.py ./src/b1k/policies/agent.py
COPY scripts/serve_b1k.py ./scripts/serve_b1k.py
RUN python -m unittest agent.eval.test_runtime agent.eval.test_route
ENTRYPOINT ["python", "-m", "agent.eval.serve_agent_only", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11.13-slim-bookworm

COPY --from=agent-pi /usr/local/bin/node /usr/local/bin/node
COPY --from=agent-pi /opt/pi /opt/pi
COPY --from=ghcr.io/astral-sh/uv:0.8.13 /uv /uvx /bin/

# git: the lerobot fork is a git dependency in uv.lock; libgl/glib: opencv; procps: debugging;
# g++: OmniGibson torch.compile()s its transform utils at import
RUN apt-get update && apt-get install -y --no-install-recommends \
        git ca-certificates g++ libgl1 libglib2.0-0 libgomp1 procps \
    && rm -rf /var/lib/apt/lists/*

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    UV_HTTP_TIMEOUT=600 \
    GIT_LFS_SKIP_SMUDGE=1 \
    PATH=/opt/venv/bin:$PATH

WORKDIR /opt/b1k

# 1. Locked dependencies (openpi is an editable path dependency, patched by build.sh)
COPY pyproject.toml uv.lock README.md ./
COPY --from=openpi . ./openpi
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# 2. BEHAVIOR-1K evaluation packages (Isaac Sim is not needed: the server only imports the websocket protocol)
COPY --from=b1k OmniGibson /opt/BEHAVIOR-1K/OmniGibson
COPY --from=b1k bddl3 /opt/BEHAVIOR-1K/bddl3
ARG PYPI_INDEX=""
RUN --mount=type=cache,target=/root/.cache/uv \
    if [ -n "$PYPI_INDEX" ]; then export UV_DEFAULT_INDEX="$PYPI_INDEX"; fi \
    && uv pip install --python /opt/venv/bin/python -e /opt/BEHAVIOR-1K/bddl3 -e "/opt/BEHAVIOR-1K/OmniGibson[eval]" \
    && uv pip install --python /opt/venv/bin/python "av>=15,<16" \
    && uv pip install --python /opt/venv/bin/python --no-deps "warp-lang==1.12.0"

# omnigibson.eval.utils.eval_utils reads the 2026 task table at import (the task-name -> id map)
COPY --from=b1k datasets/2026-challenge-task-instances/metadata /opt/BEHAVIOR-1K/datasets/2026-challenge-task-instances/metadata

# 3. Our code
COPY src ./src
COPY scripts ./scripts
COPY assets ./assets
COPY configs ./configs
COPY --from=agent-contexts /opt/b1k/agent ./agent
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --inexact

# 4. Checkpoint (inference files only)
COPY --from=model . /opt/model
COPY submission/entrypoint.sh /opt/entrypoint.sh

ENV XLA_PYTHON_CLIENT_ALLOCATOR=platform \
    XLA_PYTHON_CLIENT_MEM_FRACTION=0.5 \
    POLICY_PORT=8000 \
    OPENPI_DATA_HOME=/opt/openpi_cache \
    HF_HUB_OFFLINE=1 \
    PATH=/opt/pi/node_modules/.bin:/opt/venv/bin:$PATH \
    AGENT_ENABLED=1 \
    PI_CODING_AGENT_DIR=/tmp/behavior-agent/auth \
    B1K_AGENT_RUN_ROOT=/tmp/behavior-agent/rollouts

EXPOSE 8000
ENTRYPOINT ["/opt/entrypoint.sh"]
