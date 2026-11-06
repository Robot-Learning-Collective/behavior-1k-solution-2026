#!/usr/bin/env bash
# Build the submission image.
#   B1K_DATA=<BEHAVIOR datasets root> submission/build.sh <checkpoint step dir> [image tag]
# The checkpoint dir must hold params/, assets/, _CHECKPOINT_METADATA and exactly one recipe .yaml.
# BEHAVIOR-1K and openpi sources are staged from their pinned commits with `git archive`, so local edits in a
# working tree never reach the image. Agent contexts come from agent/frozen/ (see agent/eval/frozen.py);
# AGENT_BUNDLE=optional builds without it, and then the image serves the learned policy for every task.
# PYPI_INDEX=<simple index url> routes the one unlocked install (OmniGibson deps) through a mirror.
set -euo pipefail
REPO=$(cd "$(dirname "$0")/.." && pwd)
CKPT=$(readlink -f "${1:?usage: build.sh <checkpoint step dir> [tag]}")
TAG=${2:-rlc-behavior2026-policy:latest}
B1K_REV=${B1K_REV:-v3.9.3-post2}

for f in params assets _CHECKPOINT_METADATA; do
  [ -e "$CKPT/$f" ] || { echo "checkpoint is missing $f: $CKPT" >&2; exit 1; }
done
[ "$(ls "$CKPT"/*.yaml | wc -l)" = 1 ] || { echo "need exactly one recipe .yaml in $CKPT" >&2; exit 1; }
[ -e "$REPO/openpi/.git" ] || { echo "openpi submodule missing (git submodule update --init openpi)" >&2; exit 1; }

B1K_GIT=${B1K_GIT:-$REPO/BEHAVIOR-1K}
STAGE=$(mktemp -d "${TMPDIR:-/tmp}/b1k_ctx.XXXXXX"); trap 'rm -rf "$STAGE"' EXIT
git -C "$B1K_GIT" archive "$B1K_REV" OmniGibson bddl3 | tar -x -C "$STAGE"
B1K_META=${B1K_DATA:-$B1K_GIT/datasets}/2026-challenge-task-instances/metadata
[ -f "$B1K_META/B100_task_misc.csv" ] || { echo "missing $B1K_META/B100_task_misc.csv (set B1K_DATA)" >&2; exit 1; }
mkdir -p "$STAGE/datasets/2026-challenge-task-instances" && cp -a "$B1K_META" "$STAGE/datasets/2026-challenge-task-instances/"
echo "BEHAVIOR-1K $B1K_REV = $(git -C "$B1K_GIT" rev-parse "$B1K_REV^{commit}")"

OPENPI_REV=$(git -C "$REPO" ls-tree HEAD openpi | awk '{print $3}')
OPENPI_CTX="$STAGE/.openpi"; mkdir -p "$OPENPI_CTX"
git -C "$REPO/openpi" archive "$OPENPI_REV" | tar -x -C "$OPENPI_CTX"
for p in "$REPO"/patches/openpi-*.patch; do   # same patches, same order as setup_remote.sh
  (cd "$OPENPI_CTX" && git apply "$p") || { echo "failed to apply $p" >&2; exit 1; }
done
echo "openpi $OPENPI_REV + patches"

MODEL_CTX="$STAGE/.model"; mkdir -p "$MODEL_CTX"
for f in params assets _CHECKPOINT_METADATA; do cp -al "$CKPT/$f" "$MODEL_CTX/" 2>/dev/null || cp -a "$CKPT/$f" "$MODEL_CTX/"; done
cp "$CKPT"/*.yaml "$MODEL_CTX/"

DOCKER_BUILDKIT=1 docker build \
  --build-context b1k="$STAGE" \
  --build-context model="$MODEL_CTX" \
  --build-context openpi="$OPENPI_CTX" \
  --build-arg PYPI_INDEX="${PYPI_INDEX:-}" \
  --build-arg AGENT_BUNDLE="${AGENT_BUNDLE:-required}" \
  -f "$REPO/submission/Dockerfile" -t "$TAG" "$REPO"
