"""Observation class and preprocessing with FAST auxiliary fields support.

Based on openpi with FAST fields added for PI_BEHAVIOR model.

Reference: https://github.com/wensi-ai/openpi/blob/behavior/src/openpi/models/model.py
"""

from collections.abc import Sequence
from typing import Generic, TypeVar
import dataclasses

import augmax
from flax import struct
import jax
import jax.numpy as jnp
import numpy as np
import torch

from openpi.shared import image_tools
from openpi.shared import array_typing as at

ArrayT = TypeVar("ArrayT", bound=jax.Array | torch.Tensor | np.ndarray)

IMAGE_KEYS = (
    "base_0_rgb",
    "left_wrist_0_rgb",
    "right_wrist_0_rgb",
)
IMAGE_RESOLUTION = (224, 224)


@dataclasses.dataclass(frozen=True)
class TrainAugmentationConfig:
    """Training-only augmentations: crop + rotate (head camera), color jitter and cutout (every camera),
    whole wrist-camera dropout, and state-token dropout (applied in the attention mask by the model)."""
    brightness: float = 0.3
    contrast: float = 0.4
    saturation: float = 0.5
    head_crop_frac: float = 0.98
    head_rotate_deg: float = 2.0
    cutout_prob: float = 0.3
    cutout_max_area: float = 0.1
    cam_dropout_prob: float = 0.05
    state_dropout_prob: float = 0.02


@at.typecheck
@struct.dataclass
class Observation(Generic[ArrayT]):
    """Observation with FAST auxiliary fields."""
    
    images: dict[str, at.Float[ArrayT, "*b h w c"]]
    image_masks: dict[str, at.Bool[ArrayT, "*b"]]
    state: at.Float[ArrayT, "*b s"]
    tokenized_prompt: at.Int[ArrayT, "*b l"] | None = None
    tokenized_prompt_mask: at.Bool[ArrayT, "*b l"] | None = None
    token_ar_mask: at.Int[ArrayT, "*b l"] | None = None
    token_loss_mask: at.Bool[ArrayT, "*b l"] | None = None
    
    fast_tokens: at.Int[ArrayT, "*b t"] | None = None
    fast_token_mask: at.Bool[ArrayT, "*b t"] | None = None

    # True for action-chunk steps past the episode end (excluded from the action loss)
    action_is_pad: at.Bool[ArrayT, "*b ah"] | None = None

    @classmethod
    def from_dict(cls, data: at.PyTree[ArrayT]) -> "Observation[ArrayT]":
        """Convert dict to Observation."""
        if ("tokenized_prompt" in data) != ("tokenized_prompt_mask" in data):
            raise ValueError("tokenized_prompt and tokenized_prompt_mask must be provided together.")
        
        # Convert uint8 images to float32 [-1, 1]
        for key in data["image"]:
            if data["image"][key].dtype == np.uint8:
                data["image"][key] = data["image"][key].astype(np.float32) / 255.0 * 2.0 - 1.0
            elif hasattr(data["image"][key], "dtype") and data["image"][key].dtype == torch.uint8:
                data["image"][key] = data["image"][key].to(torch.float32).permute(0, 3, 1, 2) / 255.0 * 2.0 - 1.0
        
        return cls(
            images=data["image"],
            image_masks=data["image_mask"],
            state=data["state"],
            tokenized_prompt=data.get("tokenized_prompt"),
            tokenized_prompt_mask=data.get("tokenized_prompt_mask"),
            token_ar_mask=data.get("token_ar_mask"),
            token_loss_mask=data.get("token_loss_mask"),
            fast_tokens=data.get("fast_tokens"),
            fast_token_mask=data.get("fast_token_mask"),
            action_is_pad=data.get("action_is_pad"),
        )

    def to_dict(self) -> at.PyTree[ArrayT]:
        """Convert Observation to dict."""
        result = dataclasses.asdict(self)
        result["image"] = result.pop("images")
        result["image_mask"] = result.pop("image_masks")
        return result


def _cutout(rng, image, prob: float, max_area: float):
    """One grey rectangle (area <= max_area of the image, aspect 0.3-3) with probability `prob`."""
    rng_apply, rng_area, rng_aspect, rng_cy, rng_cx = jax.random.split(rng, 5)
    height, width, _ = image.shape
    area = jax.random.uniform(rng_area, (), maxval=max_area) * height * width
    aspect = jax.random.uniform(rng_aspect, (), minval=0.3, maxval=3.0)
    h, w = jnp.sqrt(area * aspect), jnp.sqrt(area / aspect)
    cy = jax.random.uniform(rng_cy, (), maxval=float(height))
    cx = jax.random.uniform(rng_cx, (), maxval=float(width))
    ys = jnp.arange(height)[:, None]
    xs = jnp.arange(width)[None, :]
    inside = (jnp.abs(ys - cy) < h / 2) & (jnp.abs(xs - cx) < w / 2) & jax.random.bernoulli(rng_apply, prob)
    return jnp.where(inside[..., None], jnp.array(0.5, image.dtype), image)


def preprocess_observation(
    rng: at.KeyArrayLike | None,
    observation: Observation,
    *,
    train: bool = False,
    image_keys: Sequence[str] = IMAGE_KEYS,
    image_resolution: tuple[int, int] = IMAGE_RESOLUTION,
    aug: TrainAugmentationConfig | None = None,
) -> Observation:
    """Preprocess observations with image augmentation and FAST fields preservation."""
    if not set(image_keys).issubset(observation.images):
        raise ValueError(f"images dict missing keys: expected {image_keys}, got {list(observation.images)}")

    batch_shape = observation.state.shape[:-1]
    if train:
        aug = aug or TrainAugmentationConfig()
        rng_color, rng_cutout, rng_drop = jax.random.split(rng, 3)

    out_images = {}
    for key in image_keys:
        image = observation.images[key]
        if image.shape[1:3] != image_resolution:
            image = image_tools.resize_with_pad(image, *image_resolution)

        if train:
            # Convert from [-1, 1] to [0, 1] for augmax
            image = image / 2.0 + 0.5

            transforms = []
            if "wrist" not in key:
                height, width = image.shape[1:3]
                transforms += [
                    augmax.RandomCrop(int(width * aug.head_crop_frac), int(height * aug.head_crop_frac)),
                    augmax.Resize(width, height),
                    augmax.Rotate((-aug.head_rotate_deg, aug.head_rotate_deg)),
                ]
            transforms += [
                augmax.ColorJitter(brightness=aug.brightness, contrast=aug.contrast, saturation=aug.saturation),
            ]
            sub_rngs = jax.random.split(rng_color, image.shape[0])
            image = jax.vmap(augmax.Chain(*transforms))(sub_rngs, image)
            cutout_rngs = jax.random.split(jax.random.fold_in(rng_cutout, len(out_images)), image.shape[0])
            image = jax.vmap(_cutout, in_axes=(0, 0, None, None))(cutout_rngs, image, aug.cutout_prob, aug.cutout_max_area)

            # Back to [-1, 1]
            image = jnp.clip(image, 0.0, 1.0) * 2.0 - 1.0

        out_images[key] = image

    # Obtain masks
    out_masks = {}
    for key in out_images:
        if key not in observation.image_masks:
            out_masks[key] = jnp.ones(batch_shape, dtype=jnp.bool)
        else:
            out_masks[key] = jnp.asarray(observation.image_masks[key])

    # Wrist-camera dropout: zero image and mask=False, so the model learns to act without it
    if train:
        for i, key in enumerate(image_keys):
            if "wrist" in key:
                drop = jax.random.bernoulli(jax.random.fold_in(rng_drop, i), aug.cam_dropout_prob, batch_shape)
                out_images[key] = jnp.where(drop[:, None, None, None], 0.0, out_images[key])
                out_masks[key] = out_masks[key] & ~drop

    return Observation(
        images=out_images,
        image_masks=out_masks,
        state=observation.state,
        tokenized_prompt=observation.tokenized_prompt,
        tokenized_prompt_mask=observation.tokenized_prompt_mask,
        token_ar_mask=observation.token_ar_mask,
        token_loss_mask=observation.token_loss_mask,
        fast_tokens=getattr(observation, 'fast_tokens', None),
        fast_token_mask=getattr(observation, 'fast_token_mask', None),
        action_is_pad=getattr(observation, 'action_is_pad', None),
    )
