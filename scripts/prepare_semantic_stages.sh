#!/usr/bin/env bash
# Regenerates the semantic stage assets in assets/semantic_stages/ from the 2026 demos (skill annotations, meta/
# and data/ of all 100 tasks): per-frame stage labels, stage spec, stage length stats and, with --grippers, the
# gripper allow list. Intermediate files go to outputs/semantic_stages/. ~15 min CPU (+ ~1 h for --grippers).
#
#   B1K_DEMOS_ROOT=data/2026-challenge-demos bash scripts/prepare_semantic_stages.sh [--grippers]
#
# The stage design rules in design_stages.py / design_stages_v3.py (and the reviewed borderline gripper decisions in
# reviewed_gripper_close_v2.json) were derived with LLM-assisted analysis and review of the annotations.
set -euo pipefail
cd "$(dirname "$0")/.."
export B1K_DEMOS_ROOT="${B1K_DEMOS_ROOT:-data/2026-challenge-demos}"
export STAGE_OUT=outputs/semantic_stages/v2 STAGE_OUT_V3=outputs/semantic_stages/v3 JAX_PLATFORMS=cpu
S=scripts/semantic_stages; A=assets/semantic_stages
mkdir -p "$STAGE_OUT" "$STAGE_OUT_V3"

echo "== 1/5 completion frame per episode"
uv run python $S/extract_termination.py
echo "== 2/5 skill-annotation analysis (medoid skill sequences)"
uv run python $S/analyze.py
echo "== 3/5 v2 stage design (consistent cuts, unordered / class blocks)"
uv run python $S/design_stages.py > "$STAGE_OUT/design_stages.log"
for f in stage_defs.json structure.json episode_stage_frames.csv stages.csv tasks.csv; do mv -f "$STAGE_OUT/v2_$f" "$STAGE_OUT/$f"; done
echo "== 4/5 v3 stages (regrouped v2 atoms) -> $A"
uv run python $S/design_stages_v3.py > "$STAGE_OUT_V3/design_stages_v3.log"
cmp -s "$STAGE_OUT_V3/stages.csv" $A/stages.csv || { echo "ERROR: regenerated stages.csv differs from $A/stages.csv (TASK_NUM_STAGES)"; exit 1; }
cp "$STAGE_OUT_V3/episode_stage_frames.csv" $A/
echo "== 5/5 stage length stats"
uv run python $S/stage_length_stats.py $A/episode_stage_frames.csv $A/stage_len_stats.json
if [ "${1:-}" = "--grippers" ]; then
  uv run python $S/scan_grippers.py "$B1K_DEMOS_ROOT" outputs/semantic_stages/gripper_scan
  GRIPPER_SCAN_DIR=outputs/semantic_stages/gripper_scan uv run python $S/build_close_allowed.py --stage-dir "$STAGE_OUT_V3" \
    --prev $S/reviewed_gripper_close_v2.json --overlap "$STAGE_OUT_V3/v2_to_v3_overlap.json" --out $A/gripper_close_allowed.json
fi
echo done
