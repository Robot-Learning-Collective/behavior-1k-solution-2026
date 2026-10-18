"""PI_BEHAVIOR Model Configuration

Configuration for PI_BEHAVIOR model on BEHAVIOR-1K challenge.
"""

import dataclasses
import json
import pathlib
from typing import TYPE_CHECKING

import flax.nnx as nnx
import jax
import jax.numpy as jnp
from typing_extensions import override

from openpi.models import model as _model
from openpi.models import gemma as _gemma
from openpi.shared import array_typing as at
import openpi.shared.nnx_utils as nnx_utils

from b1k.models.observation import Observation, TrainAugmentationConfig

if TYPE_CHECKING:
    from b1k.models.pi_behavior import PiBehavior


# Per-task stage counts of the semantic stages (assets/semantic_stages/stages.csv): ordered groups of the
# skill annotations of the 2026 demos; per-frame labels in assets/semantic_stages/episode_stage_frames.csv.
# Use tuple for immutability and to avoid JAX device allocation at import time
TASK_NUM_STAGES = (
    2, 2, 3, 4, 4, 2, 2, 5, 4, 5,  # Tasks 0-9
    2, 5, 3, 6, 9, 4, 4, 3, 3, 4,  # Tasks 10-19
    4, 5, 3, 6, 6, 5, 6, 6, 4, 5,  # Tasks 20-29
    5, 4, 3, 4, 2, 2, 3, 2, 3, 3,  # Tasks 30-39
    4, 7, 2, 6, 4, 7, 7, 3, 9, 5,  # Tasks 40-49
    3, 6, 3, 3, 3, 3, 3, 2, 4, 3,  # Tasks 50-59
    2, 6, 5, 2, 8, 4, 6, 5, 4, 3,  # Tasks 60-69
    5, 5, 7, 6, 4, 4, 2, 2, 2, 3,  # Tasks 70-79
    2, 3, 5, 5, 5, 8, 3, 3, 4, 3,  # Tasks 80-89
    2, 5, 2, 3, 5, 8, 4, 5, 5, 4,  # Tasks 90-99
)

MAX_NUM_STAGES = max(TASK_NUM_STAGES)  # 9
TOTAL_TASK_STAGE_EMBEDDINGS = sum(TASK_NUM_STAGES)  # 413 total embeddings

# Cumulative offsets for indexing into task_stage_embeddings (as tuple)
TASK_STAGE_OFFSETS = tuple([0] + [sum(TASK_NUM_STAGES[:i+1]) for i in range(len(TASK_NUM_STAGES) - 1)])


@dataclasses.dataclass(frozen=True)
class PiBehaviorConfig(_model.BaseModelConfig):
    dtype: str = "bfloat16"
    paligemma_variant: _gemma.Variant = "gemma_2b"
    action_expert_variant: _gemma.Variant = "gemma_300m"

    # Set the model specific defaults.
    # 21 = [base 3][trunk translate, tilt][left arm 7][left grip][right arm 7][right grip] (b1k.shared.trunk2dof)
    action_dim: int = 21
    action_horizon: int = 30
    max_token_len: int = 200  # Only used for compatibility, not for actual tokenization
    
    # Number of tasks in the behavior dataset
    num_tasks: int = 100
    # Task embedding dimension - will match the paligemma width
    task_embedding_dim: int = None  # type: ignore
    # Maximum number of subtask states across all tasks
    max_num_subtask_states: int = MAX_NUM_STAGES
    
    # Path to task data JSON file for initialization
    task_data_path: str = "b1k/BEHAVIOR-1K/docs/challenge/task_data.json"
    
    # Whether to use correlated noise matching action covariance structure
    # Requires correlation matrix in norm_stats (computed by compute_norm_stats.py)
    use_correlated_noise: bool = True
    
    # Shrinkage parameter for correlation regularization
    # Applied as: S_regularized = beta * S + (1-beta) * I
    # beta=1.0 means full correlation (no shrinkage)
    # beta=0.7 means 70% correlation + 30% independence (recommended for robustness)
    # beta=0.0 means independence (no correlation)
    correlation_beta: float = 0.5
    
    # FAST auxiliary training configuration
    use_fast_auxiliary: bool = False  # Enable FAST during training
    fast_loss_weight: float = 0.1  # Weight for FAST loss (vs flow loss)
    
    # Action dimensions to encode with FAST (default: 0:6, 7:23 = 22 dims)
    # Format: "0:6,7:23" or list of tuples [(0, 6), (7, 23)]
    fast_encoded_dims: str | list[tuple[int, int]] = "0:6,7:23"
    
    # FAST tokenizer vocab size
    fast_vocab_size: int = 1024
    
    # Max FAST tokens to predict (truncate if exceeded)
    max_fast_tokens: int = 32
    
    # FAST tokenizer path (set during initialization, relative to assets_dir/asset_id)
    fast_tokenizer_path: str | None = None
    
    # KV cache transformation for cross-layer attention between VLM and action expert
    # Allows each action expert layer to attend to a learned combination of all VLM layers
    use_kv_transform: bool = True
    
    # Knowledge insulation: stop action expert gradients from flowing to VLM backbone
    # VLM trains on FAST tokens only, action expert on flow matching with frozen VLM features
    # Implements approach from https://www.physicalintelligence.company/research/knowledge_insulation
    use_knowledge_insulation: bool = True
    
    # Subtask/stage prediction auxiliary loss weight (relative to action loss)
    # Higher values emphasize stage prediction accuracy at the expense of action quality
    subtask_loss_weight: float = 0.1
    
    # Time threshold for inpainting during inference
    # Stop enforcing inpainting constraint when t < threshold (let model be free in final steps)
    time_threshold_inpaint: float = 0.3
    # Soft inpainting: per flow step the inpainted coords move this fraction toward the anchor path,
    # and the correlated correction of the free coords is scaled to at most this size (normalized units)
    inpaint_pin_alpha: float = 0.7
    inpaint_correction_step_cap: float = 0.1
    
    # Vision backbone finetuning control
    freeze_vision_backbone: bool = True

    # Learnable tokens: SigLIP registers (their outputs join the prefix), VLM scratch tokens after the
    # images, and action-expert scratch tokens; the last `num_action_scratch_tokens_tail` of them follow
    # the actions and carry the task / task-stage embeddings into the expert.
    num_siglip_registers: int = 8
    num_vlm_scratch_tokens: int = 8
    num_action_scratch_tokens: int = 6
    num_action_scratch_tokens_tail: int = 2
    # Rows kept in Gemma's token embedding table: only the 256 state bins are ever embedded
    llm_vocab_size: int = 256

    # Training only: pad attention keys to a multiple of this in the flash attention patch
    attn_key_pad_multiple: int = 1
    # Training only: image / state augmentations
    train_aug: TrainAugmentationConfig = dataclasses.field(default_factory=TrainAugmentationConfig)

    def __post_init__(self):
        if self.task_embedding_dim is None:
            paligemma_config = _gemma.get_config(self.paligemma_variant)
            object.__setattr__(self, "task_embedding_dim", paligemma_config.width)
    
    def get_fast_dim_ranges(self) -> list[tuple[int, int]]:
        """Parse fast_encoded_dims into list of ranges."""
        if isinstance(self.fast_encoded_dims, str):
            ranges = []
            for range_str in self.fast_encoded_dims.split(','):
                start, end = map(int, range_str.strip().split(':'))
                ranges.append((start, end))
            return ranges
        return self.fast_encoded_dims
    
    def get_total_fast_dims(self) -> int:
        """Get total number of dimensions encoded by FAST."""
        return sum(end - start for start, end in self.get_fast_dim_ranges())

    @property
    @override
    def model_type(self):
        return "pi_behavior"

    @override
    def create(self, rng: at.KeyArrayLike) -> "PiBehavior":
        from b1k.models.pi_behavior import PiBehavior

        return PiBehavior(self, rngs=nnx.Rngs(rng))

    @override
    def inputs_spec(self, *, batch_size: int = 1) -> tuple["Observation", _model.Actions]:
        image_spec = jax.ShapeDtypeStruct([batch_size, *_model.IMAGE_RESOLUTION, 3], jnp.float32)
        image_mask_spec = jax.ShapeDtypeStruct([batch_size], jnp.bool_)

        with at.disable_typechecking():
            obs_kwargs = {
                "images": {
                    "base_0_rgb": image_spec,
                    "left_wrist_0_rgb": image_spec,
                    "right_wrist_0_rgb": image_spec,
                },
                "image_masks": {
                    "base_0_rgb": image_mask_spec,
                    "left_wrist_0_rgb": image_mask_spec,
                    "right_wrist_0_rgb": image_mask_spec,
                },
                "state": jax.ShapeDtypeStruct([batch_size, self.action_dim], jnp.float32),
                "tokenized_prompt": jax.ShapeDtypeStruct([batch_size, 2], jnp.int32),
                "tokenized_prompt_mask": jax.ShapeDtypeStruct([batch_size, 2], bool),
            }
            
            if self.use_fast_auxiliary:
                obs_kwargs["fast_tokens"] = jax.ShapeDtypeStruct([batch_size, self.max_fast_tokens], jnp.int32)
                obs_kwargs["fast_token_mask"] = jax.ShapeDtypeStruct([batch_size, self.max_fast_tokens], bool)
            
            observation_spec = Observation(**obs_kwargs)
        
        action_spec = jax.ShapeDtypeStruct([batch_size, self.action_horizon, self.action_dim], jnp.float32)
        return observation_spec, action_spec