"""Minimal Policy subclass for PiBehavior models that handles tuple unpacking.

Reference: https://github.com/PhysicalIntelligence/openpi/blob/behavior/src/openpi/policies/policy.py
"""

import time
from typing import Any

import jax
import jax.numpy as jnp
import numpy as np
from typing_extensions import override

from openpi.policies.policy import Policy
from b1k.models.observation import Observation  # Use our custom Observation with FAST fields


class PiBehaviorPolicy(Policy):
    """Policy for PiBehavior models - only difference is unpacking the tuple return.
    
    PiBehavior.sample_actions() returns (actions, subtask_logits) instead of just actions.
    This minimal subclass unpacks the tuple before output transforms are applied.
    """
    
    @override
    def infer(self, obs: dict, *, noise: np.ndarray | None = None, initial_actions: np.ndarray | None = None) -> dict:
        """Infer with PiBehavior-specific tuple unpacking.
        
        Identical to parent Policy.infer() except:
        1. Accepts initial_actions parameter for rolling inpainting
        2. Unpacks (actions, subtask_logits) tuple before output transforms
        """
        inputs, initial_actions = self._prepare_inputs(obs, initial_actions)
        inputs = jax.tree.map(lambda x: jnp.asarray(x)[np.newaxis, ...], inputs)
        self._rng, sample_rng = jax.random.split(self._rng)

        # Prepare sample_kwargs
        sample_kwargs = dict(self._sample_kwargs)
        if noise is not None:
            noise = jnp.asarray(noise)
            if noise.ndim == 2:
                noise = noise[None, ...]
            sample_kwargs["noise"] = noise
        if initial_actions is not None:
            sample_kwargs["initial_actions"] = jnp.asarray(initial_actions)[None, ...]

        observation = Observation.from_dict(inputs)
        start_time = time.monotonic()
        
        # ONLY DIFFERENCE: Unpack tuple return from PiBehavior.sample_actions
        actions, subtask_logits = self._sample_actions(sample_rng, observation, **sample_kwargs)
        
        outputs = {
            "state": inputs["state"],
            "actions": actions,  # Now an array, not a tuple!
            "subtask_logits": subtask_logits,
        }
        
        model_time = time.monotonic() - start_time
        
        # Convert to numpy (same as parent)
        outputs = {
            k: np.asarray(v[0, ...]) if isinstance(v, (jnp.ndarray, np.ndarray)) else v
            for k, v in outputs.items()
        }

        # Apply output transforms (now works because actions is an array)
        outputs = self._output_transform(outputs)
        
        # Add convenience field
        outputs["predicted_stage"] = int(np.argmax(outputs["subtask_logits"]))
        
        outputs["policy_timing"] = {
            "infer_ms": model_time * 1000,
        }
        return outputs

    def _prepare_inputs(self, obs: dict, initial_actions: np.ndarray | None):
        """Per-sample input transforms; returns (model inputs, normalized initial actions or None)."""
        inputs = self._input_transform(jax.tree.map(lambda x: x, obs))
        if initial_actions is None:
            return inputs, None
        # Run the initial actions through the training transforms (delta + normalization) as `actions`
        transformed = self._input_transform({**obs, "actions": np.array(initial_actions, copy=True)})
        # Clip: tiny per-timestep stds can push the re-normalized anchor far out of distribution
        return inputs, np.clip(transformed["actions"], -3.0, 3.0)

    def infer_batch(self, batch: list[tuple[dict, np.ndarray | None]], *, pad_to: int | None = None) -> list[dict]:
        """infer() for several (obs, initial_actions) samples in one model call per inpainting mode.
        The batch is padded to `pad_to` (repeating its last sample) so the jitted function keeps one shape."""
        prepared = [self._prepare_inputs(obs, init) for obs, init in batch]
        outputs = [None] * len(batch)
        for with_init in (False, True):
            idx = [i for i, (_, init) in enumerate(prepared) if (init is not None) == with_init]
            if not idx:
                continue
            rows = [prepared[i] for i in idx]
            rows += [rows[-1]] * max(0, (pad_to or 0) - len(rows))
            inputs = jax.tree.map(lambda *xs: jnp.asarray(np.stack(xs)), *[r[0] for r in rows])
            self._rng, sample_rng = jax.random.split(self._rng)
            sample_kwargs = dict(self._sample_kwargs)
            if with_init:
                sample_kwargs["initial_actions"] = jnp.asarray(np.stack([r[1] for r in rows]))
            actions, subtask_logits = self._sample_actions(sample_rng, Observation.from_dict(inputs), **sample_kwargs)
            actions, subtask_logits, state = np.asarray(actions), np.asarray(subtask_logits), np.asarray(inputs["state"])
            for row, i in enumerate(idx):
                out = self._output_transform(
                    {"state": state[row], "actions": actions[row], "subtask_logits": subtask_logits[row]}
                )
                out["predicted_stage"] = int(np.argmax(out["subtask_logits"]))
                outputs[i] = out
        return outputs

    @property
    def metadata(self) -> dict[str, Any]:
        return self._metadata
