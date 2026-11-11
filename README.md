# BEHAVIOR Challenge 2026 Solution

**9th Place | Public Leaderboard: 44.6%**

Our solution for the [2026 BEHAVIOR Challenge](https://behavior.stanford.edu/challenge/): a single vision-language-action (VLA) model that runs a Galaxea R1Pro robot on all 100 long-horizon household tasks in the OmniGibson simulator. It builds on [Pi0.5](https://www.physicalintelligence.company/blog/pi05), the [openpi](https://github.com/Physical-Intelligence/openpi) code and our [1st-place 2025 solution](#2025-solution).

**[Checkpoint](https://huggingface.co/IliaLarchenko/BEHAVIOR2026VLA)** | **[Technical report](https://arxiv.org/abs/2611.14432)**

## Results

Local evaluation with the official success criterion and q-score: 100 tasks, 10 episodes per task (instances 301-310), learned policy only.

| Tasks | Count | q-score |
|---|---|---|
| All | 100 | 0.392 |
| Shared with the 2025 challenge | 50 | 0.371 |
| New in 2026 | 50 | 0.412 |

On the 50 shared tasks our 2025 submission scored 0.260. That score comes from the official 2025 evaluation in the 2025 simulator, so the comparison is not exact.

The leaderboard score comes from our challenge submission, which also used an agent-based controller on 14 tasks. The results in this section are for the learned policy alone.

## Agent on 14 tasks

On 14 tasks where the learned policy is weak, the policy server hands the episode to an LLM agent: GPT-6 Astra controls the robot through `observe`, `act` and `xyz` calls and a per-tick controller. Every episode starts from a fork of the agent's own practice session on that task, in which it practised in the simulator, compared itself with the human demonstrations and wrote down what worked. With the agent the public leaderboard score rises from 39.2% to 44.6%.

```
evaluator ── scripts/serve_b1k.py --agent ┬─ agent task (agent/tasks/tasks.json) → fork of the frozen practice session → controller
                                          └─ every other task, and any agent failure → learned policy
```

The practice sessions are not public, so the agent route cannot run from this repository alone; the learned policy on all 100 tasks can. [agent/README.md](agent/README.md) describes the agent, its practice and evaluation loops and the per-task results, [agent/practice/](agent/practice/README.md) is the practice harness, and [agent/research/](agent/research/README.md) covers what we tried before practice.

## Solution

**Model**
- PaliGemma vision-language model plus a smaller Gemma action expert trained with flow matching, 2.9B parameters
- One checkpoint for all 100 tasks: learned task and stage embeddings instead of text prompts
- Correlated flow noise, N(0, 0.5·I + 0.5·C), where C is the empirical correlation of the action chunks
- Each action-expert layer attends to a learnable mix of the keys and values of all VLM layers
- State tokens: each joint's 256-bin token plus a learned per-joint embedding and a projection of sin/cos features of the unclipped value, plus one continuous token of the whole state
- 8 SigLIP register tokens, 8 VLM scratch tokens and 6 action-expert scratch tokens; 2 of the expert tokens follow the actions and carry the task and stage embeddings into the expert
- Attention sink (learnable logit and value) in every Gemma attention layer
- Identity-initialized per-camera projection of the SigLIP tokens
- Gemma token table cut to the 256 state-bin rows

**Data**
- 2026 challenge dataset (LeRobot v3, 100 tasks, 20,000 demonstrations), 224x224 RGB and proprioception; frames after task completion are never sampled as chunk anchors
- 21-dim actions and state: the trunk is represented by the teleoperation's 2 degrees of freedom (translate, tilt) instead of 4 torso joints, exact in both directions for every demonstration (`b1k.shared.trunk2dof`)
- Semantic stages: 413 stages (2-9 per task) built from ordered groups of the demonstrations' skill annotations (`assets/semantic_stages/`). Part of the stage design was post-processed with LLMs: the grouping rules and the reviewed borderline cases
- Observation timing realigned to the evaluator: the demos pair action t with positions of state t-1 and images of state t-2, the evaluator gives positions of t and images of t-1, so each sample takes the action chunk and velocities of the previous row
- State scaled to [-1, 1] by its min/max instead of z-scoring (the z-scored state saturated about a third of the 256 state bins)

**Training**
- YAML recipe (`configs/train_b1k_2026.yaml`), warm start from the 2025 checkpoint (`scripts/convert_2025_checkpoint.py`)
- 10 flow samples per observation with stratified times and antithetic noise pairs
- Auxiliary losses: FAST tokens (weight 0.05) and stage prediction (weight 0.1)
- Per-group learning-rate multipliers: 2x for the action expert, action projections, KV mixing and task/stage embeddings
- Augmentations: head-camera crop and rotation, color jitter, cutout, wrist-camera dropout, state-token dropout; padded chunk steps past the episode end are excluded from the loss
- Flash attention (`jax.nn.dot_product_attention`) for training, EMA 0.995

**Inference**
- 30 predicted actions with 20 denoising steps; the first 26 are executed in 13 environment steps (2x) and each new chunk is snapped to the last executed action with a decaying offset
- Soft inpainting: the 4 kept actions pull the new chunk with strength 0.7 per denoising step, and the correlated correction of the other actions is capped per step
- Stage voting over a 120-step window; a stage is left only after 0.67x its shortest demo duration
- Gripper rule: a fully closed gripper is opened in stages where the demos never close it (`assets/semantic_stages/gripper_close_allowed.json`)
- The server batches several environments and connections per model call

**Evaluation**
- Persistent simulator workers that refill env slots and restore the boot scene between episodes, with per-worker CPU pinning (`scripts/run_parallel_eval.py`)

## Installation

```bash
git clone --recurse-submodules https://github.com/Robot-Learning-Collective/behavior-1k-solution-2026.git
cd behavior-1k-solution-2026
bash setup_remote.sh   # uv env, openpi + local patches, BEHAVIOR-1K, Isaac Sim
```

## Run the checkpoint

The [checkpoint](https://huggingface.co/IliaLarchenko/BEHAVIOR2026VLA) holds the weights, the normalization statistics and the FAST tokenizer.

```bash
uv run hf download IliaLarchenko/BEHAVIOR2026VLA --local-dir models/behavior2026_vla

# Start the policy server
uv run scripts/serve_b1k.py --policy.config configs/train_b1k_2026.yaml --policy.dir models/behavior2026_vla

# In a second terminal, evaluate 4 episodes of one task
uv run scripts/run_parallel_eval.py --task-name turning_on_radio --instance-indices 0 1 2 3 --num-envs 4
```

Instance indices 0-9 are the public instances 301-310 used for the results above. Add `--write-video` to save the episode videos.

## Train

```bash
# 2026 demos (or a subset of chunks)
uv run hf download behavior-1k/2026-challenge-demos --repo-type dataset --local-dir data/2026-challenge-demos

# Warm start: the 2025 checkpoint_2 converted to the 2026 layout
uv run hf download IliaLarchenko/behavior_submission --include "checkpoint_2/*" --local-dir models
JAX_PLATFORMS=cpu uv run scripts/convert_2025_checkpoint.py \
    --src models/checkpoint_2/params --out models/checkpoint_2_2026/params

# Norm stats and FAST tokenizer, then training (8 GPUs, FSDP)
uv run scripts/compute_norm_stats.py --config-name configs/train_b1k_2026.yaml
uv run scripts/train_fast_tokenizer.py --config-name configs/train_b1k_2026.yaml --sample-fraction 0.01
uv run scripts/train.py --yaml configs/train_b1k_2026.yaml   # --resume to continue
```

Checkpoints go to `outputs/checkpoints/pi_behavior_b1k_2026/b1k_2026/<step>/` and are served the same way with `--policy.dir`. On machines with less than ~100 GB of host RAM set `low_memory_checkpointing: true` in the recipe.

The recipe is a single 200k-step run. The released checkpoint came from one 200k-step run that moved between hardware setups and was adjusted while training, so the recipe is not an exact replay of it.

The stage labels in `assets/semantic_stages/` are versioned. To regenerate them from the demos:

```bash
B1K_DEMOS_ROOT=data/2026-challenge-demos bash scripts/prepare_semantic_stages.sh [--grippers]
```

## Repository layout

| Path | Contents |
|---|---|
| `configs/` | Training recipe |
| `src/b1k/` | Model, data pipeline, policy and serving wrapper |
| `scripts/` | Training, conversion, serving and evaluation entry points |
| `assets/semantic_stages/` | Stage definitions, per-frame labels and inference tables |
| `patches/` | Local patches applied to openpi by `setup_remote.sh` |
| `agent/` | LLM agent route: controller, evaluation runtime, practice harness, per-task notes |
| `docs/` | [JoyLo teleoperation rig build guide](docs/joylo_build_guide.md) |
| `openpi/`, `BEHAVIOR-1K/` | Submodules |

## 2025 solution

This work continues our 1st-place solution for the 2025 BEHAVIOR Challenge, which scored 0.26 on 50 tasks.

- [Technical report](https://arxiv.org/abs/2512.06951)
- [Blog post](https://robot-learning-collective.github.io/winning-behavior-1k-challenge)
- [Checkpoints](https://huggingface.co/IliaLarchenko/behavior_submission)

## Acknowledgments

Thanks to [Physical Intelligence](https://www.physicalintelligence.company/) for the open-source work on Pi0.5 and openpi, and to the BEHAVIOR team for the challenge, simulator and dataset.

## References

**BEHAVIOR**
- Challenge: [behavior.stanford.edu/challenge](https://behavior.stanford.edu/challenge/)
- Paper: Li et al., "BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation" (2024), [arXiv:2403.09227](https://arxiv.org/abs/2403.09227)
- Dataset: [behavior-1k/2026-challenge-demos](https://huggingface.co/datasets/behavior-1k/2026-challenge-demos)
- Code: [BEHAVIOR-1K](https://github.com/StanfordVL/BEHAVIOR-1K)

**Pi0.5**
- Blog post: [π0.5: a VLA with Open-World Generalization](https://www.physicalintelligence.company/blog/pi05)
- Paper: [π0.5](https://www.physicalintelligence.company/download/pi05.pdf)
- Code: [openpi](https://github.com/Physical-Intelligence/openpi)

## Citation

```bibtex
@misc{larchenko2026onepolicy,
  title         = {One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge},
  author        = {Ilia Larchenko and Gleb Zarin and Atindra Nair and Keerti Manney and Vitaly Kleban and Mirko Kiefer and Anjana Yodaiken},
  year          = {2026},
  eprint        = {2611.14432},
  archivePrefix = {arXiv},
  primaryClass  = {cs.RO},
  url           = {https://arxiv.org/abs/2611.14432}
}
```

## License

[Apache 2.0](LICENSE)
