"""Convert the 2025 checkpoint (50 tasks, time-based stages, actions padded to 32) into the 2026 warm start.

- action projections: 32-dim padded layout -> 21-dim layout (base / arm / gripper rows copied, trunk translate /
  tilt rows zero: no linear map from the torso joints exists through the per-timestep normalization)
- token embedding table: first 256 rows (the state bins)
- task embeddings: tasks 0-49 copied; tasks 50-99 a weighted mean of matched 2025 tasks
- task-stage rows: for tasks 0-49 the overlap-weighted mean of the task's 2025 time-stage rows (weights = share
  of the semantic stage's training frames that fell in each time stage); for tasks 50-99 a weighted mean of
  matched converted rows; stage head columns from the same overlaps. Means are rescaled to the mean source norm.
- 2026-only parameters (registers, scratch tokens, sink, state / camera projections) are not written and keep
  their fresh init when training starts from the result.

  JAX_PLATFORMS=cpu uv run scripts/convert_2025_checkpoint.py \
      --src models/checkpoint_2/params --out models/checkpoint_2_2026/params --meta data/2026-challenge-demos/meta
"""

import argparse
import glob
import json
import os

import flax.traverse_util
import jax
import numpy as np
import orbax.checkpoint as ocp
import pandas as pd

from b1k.models.pi_behavior_config import TASK_NUM_STAGES
from b1k.shared.trunk2dof import MODEL_TO_ENV_INDEX

STAGES_2025 = (
    5, 6, 15, 15, 14, 12, 9, 15, 10, 15, 7, 13, 10, 15, 15, 15, 15, 11, 13, 12, 14, 15, 9, 15, 15,
    15, 15, 15, 15, 15, 11, 10, 10, 13, 5, 5, 14, 6, 8, 10, 5, 15, 8, 15, 12, 11, 9, 14, 15, 15,
)


def offsets(counts):
    return np.concatenate([[0], np.cumsum(counts)[:-1]]).astype(int)


def wavg(rows, weights):
    """Weighted mean of rows, rescaled to the weighted mean norm of the rows."""
    rows, w = np.asarray(rows, np.float64), np.asarray(weights, np.float64) / np.sum(weights)
    v = w @ rows
    return (v * (w @ np.linalg.norm(rows, axis=1)) / max(np.linalg.norm(v), 1e-9)).astype(np.float32)


def convert_tables(task_emb, stage_emb, head_k, head_b, labels_csv, meta_dir, matches_json, seed=0):
    old_off, new_off = offsets(STAGES_2025), offsets(TASK_NUM_STAGES)
    labels = pd.read_csv(labels_csv)
    lengths = pd.concat(
        [pd.read_parquet(f, columns=["episode_index", "length"]) for f in sorted(glob.glob(f"{meta_dir}/episodes/*/*.parquet"))]
    ).set_index("episode_index")["length"]
    matches = json.load(open(matches_json))
    rng = np.random.default_rng(seed)

    new_stage = np.zeros((sum(TASK_NUM_STAGES), stage_emb.shape[1]), np.float32)
    head_cols = [[] for _ in range(max(TASK_NUM_STAGES))]
    head_bias = [[] for _ in range(max(TASK_NUM_STAGES))]
    for t, n_old in enumerate(STAGES_2025):
        # frames of semantic stage j x 2025 time stage k (time stage = int(frame / (episode length / n_old)))
        overlap = np.zeros((TASK_NUM_STAGES[t], n_old))
        for r in labels[labels.episode_index // 200 == t].itertuples():
            k = np.minimum((np.arange(r.start, r.end) / (lengths[r.episode_index] / n_old)).astype(int), n_old - 1)
            overlap[r.stage] += np.bincount(k, minlength=n_old)
        overlap /= np.maximum(overlap.sum(1, keepdims=True), 1e-9)
        for j, w in enumerate(overlap):
            new_stage[new_off[t] + j] = wavg(stage_emb[old_off[t]:old_off[t] + n_old], w)
            head_cols[j].append(head_k[:, :n_old] @ w)
            head_bias[j].append(head_b[:n_old] @ w)
    old_col_norm = np.linalg.norm(head_k, axis=0).mean()
    new_k = np.stack([np.mean(c, 0) for c in head_cols], axis=1)
    new_k *= old_col_norm / np.linalg.norm(new_k, axis=0, keepdims=True)
    new_b = np.array([np.mean(b) for b in head_bias], np.float32)

    old_tasks = task_emb[: len(STAGES_2025)]
    new_task = np.concatenate([old_tasks, np.zeros((len(TASK_NUM_STAGES) - len(STAGES_2025), task_emb.shape[1]), np.float32)])
    converted = new_stage[: sum(TASK_NUM_STAGES[: len(STAGES_2025)])]
    for t in range(len(STAGES_2025), len(TASK_NUM_STAGES)):
        cand = matches["tasks"][str(t)]
        new_task[t] = (wavg([old_tasks[o] for o, _ in cand], [w for _, w in cand]) if cand != "random"
                       else rng.normal(old_tasks.mean(0), old_tasks.std(0)))
        for j in range(TASK_NUM_STAGES[t]):
            cand = matches["stages"][f"{t}:{j}"]
            if cand == "random":
                new_stage[new_off[t] + j] = rng.normal(converted.mean(0), converted.std(0))
                continue
            rows = [new_stage[new_off[int(o.split(":")[0])] + int(o.split(":")[1])] for o, _ in cand]
            new_stage[new_off[t] + j] = wavg(rows, [w for _, w in cand])
    return new_task, new_stage, new_k.astype(np.float32), new_b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="params dir of the 2025 checkpoint")
    ap.add_argument("--out", required=True)
    ap.add_argument("--meta", default="data/2026-challenge-demos/meta", help="2026 dataset meta dir (episode lengths)")
    ap.add_argument("--labels", default="assets/semantic_stages/episode_stage_frames.csv")
    ap.add_argument("--matches", default="assets/semantic_stages/init_from_2025.json")
    a = ap.parse_args()

    with ocp.PyTreeCheckpointer() as ckptr:
        src = os.path.abspath(a.src)
        metadata = ckptr.metadata(src)
        restore_args = jax.tree.map(lambda _: ocp.ArrayRestoreArgs(restore_type=np.ndarray), metadata)
        tree = ckptr.restore(src, ocp.args.PyTreeRestore(item=metadata, restore_args=restore_args))
    tree = tree.get("params", tree)
    flat = {k[:-1] if k[-1] == "value" else k: np.asarray(v) for k, v in flax.traverse_util.flatten_dict(tree).items()}

    def remap(x, axis):  # 32-dim padded action axis -> 21-dim model layout
        x = np.moveaxis(x, axis, 0)
        out = np.stack([x[i] if i is not None else np.zeros_like(x[0]) for i in MODEL_TO_ENV_INDEX])
        return np.moveaxis(out, 0, axis)

    flat[("action_in_proj", "kernel")] = remap(flat[("action_in_proj", "kernel")], 0)
    flat[("action_out_proj", "kernel")] = remap(flat[("action_out_proj", "kernel")], 1)
    flat[("action_out_proj", "bias")] = remap(flat[("action_out_proj", "bias")], 0)
    key = next(k for k in flat if k[-2:] == ("embedder", "input_embedding"))
    flat[key] = flat[key][:256]
    tables = convert_tables(
        flat[("task_embeddings", "embedding")], flat[("task_stage_embeddings", "embedding")],
        flat[("stage_pred_from_vlm", "kernel")], flat[("stage_pred_from_vlm", "bias")], a.labels, a.meta, a.matches,
    )
    for k, v in zip(
        [("task_embeddings", "embedding"), ("task_stage_embeddings", "embedding"), ("stage_pred_from_vlm", "kernel"), ("stage_pred_from_vlm", "bias")],
        tables,
    ):
        print(f"{'/'.join(k)}: {flat[k].shape} -> {v.shape}")
        flat[k] = v

    with ocp.PyTreeCheckpointer() as ckptr:
        ckptr.save(os.path.abspath(a.out), {"params": flax.traverse_util.unflatten_dict(flat)})
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
