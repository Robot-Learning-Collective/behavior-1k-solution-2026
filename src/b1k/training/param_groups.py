"""Per-parameter-group LR multipliers.

Applied as a stateless scaling of the optimizer's final updates, so the optimizer state layout does not
depend on the multipliers. Groups are matched on "/"-joined parameter paths, first rule wins.
"""

import dataclasses
import re

import jax
import optax


@dataclasses.dataclass(frozen=True)
class LRMultipliers:
    vision: float = 1.0  # SigLIP tower
    llm: float = 1.0  # Gemma VLM + token embedder
    expert: float = 1.0  # action expert (Gemma modules with the _1 suffix)
    action_proj: float = 1.0  # action / time projections and the expert conditioning projections
    kv_transform: float = 1.0  # VLM -> expert KV mixing
    embeddings: float = 1.0  # task / stage tables and their fusion layers
    fast: float = 1.0  # FAST auxiliary head
    subtask_head: float = 1.0  # stage prediction head
    pe: float = 1.0  # scratch tokens, camera projections, state embeddings
    sink: float = 1.0  # attention sink logit and value
    siglip_registers: float = 1.0  # SigLIP register tokens


_GROUP_RULES = (
    ("sink", r"(?:^|/)sink_(?:logit|value)(?:/|$)"),
    ("siglip_registers", r"(?:^|/)registers(?:/|$)"),
    ("vision", r"^PaliGemma/img/"),
    ("expert", r"_1(?:/|$)"),  # after vision: SigLIP also has *_1 layer names
    ("llm", r"^PaliGemma/llm/"),
    ("action_proj", r"^(?:action_in_proj|action_out_proj|time_mlp_in|time_mlp_out|expert_cond_proj_task|expert_cond_proj_stage)/"),
    ("kv_transform", r"^kv_transform/"),
    ("embeddings", r"^(?:task_embeddings|task_stage_embeddings|fusion_layer\d*|gate_sincos|gate_task|stage_projection)"),
    ("fast", r"^(?:fast_token_embedding|fast_token_proj)/"),
    ("subtask_head", r"^stage_pred_from_vlm/"),
    ("pe", r"^(?:vlm_scratch|action_scratch|camera_proj|state_continuous_proj|state_dim_embedding|state_value_proj)(?:/|$)"),
)


def group_of(path: str) -> str:
    for name, pattern in _GROUP_RULES:
        if re.search(pattern, path):
            return name
    raise ValueError(f"parameter {path} matches no LR group")


def _path_string(key_path) -> str:
    return "/".join(str(getattr(k, "key", getattr(k, "name", getattr(k, "idx", k)))) for k in key_path)


def with_lr_multipliers(base_tx: optax.GradientTransformation, multipliers: LRMultipliers) -> optax.GradientTransformation:
    mults = dataclasses.asdict(multipliers)

    def update(updates, state, params=None):
        updates, new_state = base_tx.update(updates, state, params)
        flat, treedef = jax.tree_util.tree_flatten_with_path(updates)
        scaled = [leaf * mults[group_of(_path_string(kp))] for kp, leaf in flat]
        return jax.tree_util.tree_unflatten(treedef, scaled), new_state

    return optax.GradientTransformation(base_tx.init, update)
