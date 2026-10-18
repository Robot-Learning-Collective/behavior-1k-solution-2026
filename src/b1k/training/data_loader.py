"""Data loading for the BEHAVIOR-1K 2026 dataset (LeRobot V3).

`WeightedMultiDataset` puts one or more LeRobot V3 datasets behind one index space and samples frames with
weights: a source gets `weight x (number of sampleable frames)` of the sampling mass, and frames after the
episode's task completion (the idle tail) are never sampled as chunk anchors.

Reference: https://github.com/wensi-ai/openpi/tree/behavior
"""

import dataclasses
import logging
import time

import numpy as np
import torch

from openpi.training.data_loader import (
    Dataset,
    DataLoader,
    TransformedDataset,
    TorchDataLoader,
)

import openpi.training.config as _config

from b1k.models.observation import Observation
from b1k.transforms_normalize import NormalizeWithPerTimestamp


def _install_bounded_video_decoder_cache(max_decoders: int = 32) -> None:
    """LRU-bound lerobot's process-wide video decoder cache: it keeps one decoder per video file forever, and
    random frame sampling over the ~5k concatenated 2026 videos grows it to hundreds of GB per worker.
    Runs at import, so spawned dataloader workers get it too."""
    from collections import OrderedDict

    from lerobot.datasets import video_utils

    class BoundedVideoDecoderCache(video_utils.VideoDecoderCache):
        def __init__(self):
            super().__init__()
            self._cache = OrderedDict()

        def get_decoder(self, video_path: str):
            video_path = str(video_path)
            with self._lock:
                if video_path in self._cache:
                    self._cache.move_to_end(video_path)
                    return self._cache[video_path][0]
                while len(self._cache) >= max_decoders:
                    self._cache.popitem(last=False)[1][1].close()
            return super().get_decoder(video_path)

    if not isinstance(video_utils._default_decoder_cache, BoundedVideoDecoderCache):
        video_utils._default_decoder_cache = BoundedVideoDecoderCache()


_install_bounded_video_decoder_cache()


@dataclasses.dataclass(frozen=True)
class DataSourceConfig:
    """One LeRobot V3 data source."""

    repo_id: str
    # Local dataset root (data/, meta/, videos/)
    root: str | None = None
    # Sampling mass = weight * number of sampleable frames
    weight: float = 1.0
    # Global episode indices to use (for partial local copies); None = all
    episodes: tuple[int, ...] | None = None
    # Never sample frames after the episode's final `next.terminated` run starts (idle tail)
    zero_weight_after_termination: bool = True
    # The official demos pair action t with joint positions of state t-1 and RGB of state t-2, while the
    # evaluator gives positions of state t and RGB of state t-1. True = pair the images and positions of
    # row u with the action chunk and the velocities of row u-1 (the evaluator's timing).
    realign_obs_timing: bool = False
    # csv with per-frame stage labels (episode_index, stage, start, end)
    stage_labels: str | None = None


# Velocity fields of the 61-dim R1Pro proprio vector (omnigibson PROPRIOCEPTION_INDICES["R1Pro"])
PROPRIO_VELOCITY_SLICES = (slice(0, 3), slice(10, 17), slice(26, 28), slice(35, 42), slice(51, 53), slice(57, 61))
STATE_KEY = "observation.state"


def realign_proprio(prev_state: np.ndarray, cur_state: np.ndarray) -> np.ndarray:
    """Positions of `cur_state`, velocities of `prev_state` ([..., 61])."""
    out = np.array(cur_state, copy=True)
    for s in PROPRIO_VELOCITY_SLICES:
        out[..., s] = np.asarray(prev_state)[..., s]
    return out


def episode_arrays(raw_states, raw_actions, terminated, realign: bool):
    """Per-episode (proprio [N, 61], actions [N, 23], last valid anchor index) as training samples them."""
    raw_states, raw_actions = np.asarray(raw_states), np.asarray(raw_actions)
    terminated = None if terminated is None else np.asarray(terminated, dtype=bool)
    if realign:
        # sample i = positions of row i+1, velocities and action of row i
        raw_states = realign_proprio(raw_states[:-1], raw_states[1:])
        raw_actions = raw_actions[:-1]
        terminated = None if terminated is None else terminated[1:]
    last = len(raw_actions) - 1
    if terminated is not None and terminated.any():
        last = int(np.argmax(terminated))
    return raw_states, raw_actions, last


def load_stage_labels(path: str | None) -> dict | None:
    """{episode_index: (run_starts, run_stages)} from a stage-label csv."""
    if not path:
        return None
    import pandas as pd

    df = pd.read_csv(path, usecols=["episode_index", "stage", "start"]).sort_values(["episode_index", "start"])
    return {
        int(ep): (g["start"].to_numpy(np.int64), g["stage"].to_numpy(np.int32)) for ep, g in df.groupby("episode_index")
    }


def valid_before_termination_mask(terminated: np.ndarray, episode_index: np.ndarray) -> np.ndarray:
    """False for frames strictly inside the trailing `terminated=True` run of their episode
    (spurious mid-episode terminations are ignored)."""
    terminated = np.asarray(terminated).reshape(-1).astype(bool)
    episode_index = np.asarray(episode_index).reshape(-1)
    valid = np.ones(len(terminated), dtype=bool)
    bounds = np.concatenate([[0], np.flatnonzero(np.diff(episode_index)) + 1, [len(episode_index)]])
    for start, end in zip(bounds[:-1], bounds[1:]):
        term = terminated[start:end]
        if term[-1]:
            non_term = np.flatnonzero(~term)
            tail_start = int(non_term[-1]) + 1 if non_term.size else 0
            valid[start + tail_start + 1 : end] = False
    return valid


class WeightedMultiDataset:
    """LeRobot V3 datasets behind one global index; items are dicts of numpy arrays."""

    def __init__(self, sources: tuple[DataSourceConfig, ...], action_horizon: int, action_key: str = "action"):
        from lerobot.datasets.lerobot_dataset import LeRobotDataset, LeRobotDatasetMetadata

        self._sources = tuple(sources)
        self._action_key = action_key
        self._datasets, self._stage_labels = [], []
        for src in sources:
            fps = float(LeRobotDatasetMetadata(src.repo_id, root=src.root).fps)
            if src.realign_obs_timing:
                # the chunk starts one row earlier; the previous state is fetched for its velocities
                delta_timestamps = {action_key: [(t - 1) / fps for t in range(action_horizon)], STATE_KEY: [-1 / fps, 0.0]}
            else:
                delta_timestamps = {action_key: [t / fps for t in range(action_horizon)]}
            dataset = LeRobotDataset(
                src.repo_id,
                root=src.root,
                episodes=list(src.episodes) if src.episodes is not None else None,
                delta_timestamps=delta_timestamps,
                # the 2026 videos are long concatenations: float32 timestamps need > 1e-4 s tolerance
                tolerance_s=1e-3,
            )
            # never decode depth streams
            features = dataset.meta.info["features"]
            for key in [k for k, f in features.items() if f.get("dtype") == "video" and ".rgb." not in k]:
                del features[key]
            self._datasets.append(dataset)
            self._stage_labels.append(load_stage_labels(src.stage_labels))
        self._offsets = np.concatenate([[0], np.cumsum([len(ds) for ds in self._datasets])])

    def __len__(self) -> int:
        return int(self._offsets[-1])

    def __getitem__(self, index: int) -> dict:
        src_idx = int(np.searchsorted(self._offsets, index, side="right")) - 1
        src = self._sources[src_idx]
        item = self._datasets[src_idx][int(index - self._offsets[src_idx])]
        out = {k: v.numpy() if isinstance(v, torch.Tensor) else v for k, v in item.items()}
        if src.realign_obs_timing:
            out[STATE_KEY] = realign_proprio(out[STATE_KEY][0], out[STATE_KEY][1])
            out.pop(f"{STATE_KEY}_is_pad", None)
        out.setdefault(f"{self._action_key}_is_pad", np.zeros(len(out[self._action_key]), dtype=bool))
        stage = 0
        labels = self._stage_labels[src_idx]
        if labels is not None:
            starts, stages = labels[int(out["episode_index"])]
            frame = int(np.asarray(out["frame_index"]).reshape(-1)[0])
            stage = stages[max(int(np.searchsorted(starts, frame, side="right")) - 1, 0)]
        out["subtask_state"] = np.int32(stage)
        return out

    def sampling_weights(self) -> np.ndarray:
        """Per-frame sampling probabilities (unnormalized) over the global index."""
        chunks = []
        for src, dataset in zip(self._sources, self._datasets):
            table = dataset._ensure_reader()
            if table.hf_dataset is None:
                table.load_and_activate()
            table = table.hf_dataset
            episode_index = _column(table, "episode_index")
            w = np.ones(len(episode_index))
            if src.zero_weight_after_termination:
                w *= valid_before_termination_mask(_column(table, "next.terminated"), episode_index)
            if src.realign_obs_timing:
                # the first frame of an episode has no previous action
                w[np.concatenate([[True], episode_index[1:] != episode_index[:-1]])] = 0.0
            logging.info(f"{src.repo_id}: {int((w > 0).sum())}/{len(w)} sampleable frames, weight {src.weight}")
            chunks.append(src.weight * w)
        return np.concatenate(chunks)


def _column(hf_dataset, name: str) -> np.ndarray:
    """A whole column as numpy straight from the arrow table (row-wise access takes minutes on 200M frames)."""
    import pyarrow.compute as pc

    col = hf_dataset.data.column(name)
    values = (pc.list_flatten(col) if hasattr(col.type, "value_type") else col).to_numpy(zero_copy_only=False)
    if hf_dataset._indices is not None:
        values = values[hf_dataset._indices.column(0).to_numpy()]
    return np.asarray(values)


class WeightedFrameSampler(torch.utils.data.Sampler[int]):
    """Weighted sampling with replacement (torch.multinomial is limited to 2**24 categories)."""

    def __init__(self, weights, num_samples: int, seed: int):
        cdf = np.cumsum(np.asarray(weights, dtype=np.float64))
        self._cdf = cdf / cdf[-1]
        self._num_samples = num_samples
        self._seed = seed
        self._epoch = 0

    def __len__(self) -> int:
        return self._num_samples

    def __iter__(self):
        rng = np.random.default_rng([self._seed, self._epoch])
        self._epoch += 1
        for start in range(0, self._num_samples, 1 << 16):
            u = rng.random(min(1 << 16, self._num_samples - start))
            yield from np.minimum(np.searchsorted(self._cdf, u, side="right"), len(self._cdf) - 1).tolist()


class DataLoaderImpl(DataLoader):
    """Custom DataLoader using our Observation with fast_tokens."""

    def __init__(self, data_config: _config.DataConfig, data_loader: TorchDataLoader):
        self._data_config = data_config
        self._data_loader = data_loader

    def data_config(self) -> _config.DataConfig:
        return self._data_config

    def __iter__(self):
        for batch in self._data_loader:
            yield Observation.from_dict(batch), batch["actions"]


def transform_dataset(dataset: Dataset, data_config: _config.DataConfig, *, skip_norm_stats: bool = False) -> Dataset:
    """Transform dataset with B1K-specific per-timestamp normalization support.

    CRITICAL: This overrides wensi-ai's transform_dataset to pass use_per_timestamp to Normalize.
    wensi-ai's version doesn't support per-timestamp normalization which causes huge action losses!
    """
    norm_stats = {}
    if data_config.repo_id != "fake" and not skip_norm_stats:
        if data_config.norm_stats is None:
            raise ValueError(
                "Normalization stats not found. "
                "Make sure to run `scripts/compute_norm_stats.py --config-name=<your-config>`."
            )
        norm_stats = data_config.norm_stats

    # Build transform list
    transforms_list = [
        *data_config.repack_transforms.inputs,
        *data_config.data_transforms.inputs,
        # Use custom Normalize with per-timestamp support (wensi-ai's doesn't have it!)
        NormalizeWithPerTimestamp(
            norm_stats,
            use_quantiles=data_config.use_quantile_norm,
            use_per_timestamp=data_config.use_per_timestamp_norm,  # CRITICAL: Per-timestamp normalization!
            state_quantile_norm=data_config.state_quantile_norm,
        ),
        *data_config.model_transforms.inputs,
    ]

    return TransformedDataset(dataset, transforms_list)


def _cpu_only_worker_init_fn(worker_id: int) -> None:
    """Keep JAX (used by the image resize transform) on the CPU in dataloader workers."""
    import os

    os.environ["JAX_PLATFORMS"] = "cpu"
    import jax

    jax.config.update("jax_platforms", "cpu")


def create_behavior_data_loader(
    config: _config.TrainConfig,
    *,
    sharding=None,
    shuffle: bool = False,
    num_batches: int | None = None,
    skip_norm_stats: bool = False,
) -> DataLoader:
    """Create a data loader for BEHAVIOR-1K training."""
    import jax

    data_config = config.data.create(config.assets_dirs, config.model)

    # Use random seed if not provided
    seed = config.seed
    if seed is None:
        seed = int(time.time() * 1000) % (2**32)
        logging.info(f"Using random seed: {seed}")

    dataset = WeightedMultiDataset(data_config.data_sources, action_horizon=config.model.action_horizon)
    sampler = WeightedFrameSampler(dataset.sampling_weights(), num_samples=len(dataset), seed=seed)
    dataset = transform_dataset(dataset, data_config, skip_norm_stats=skip_norm_stats)

    data_loader = TorchDataLoader(
        dataset,
        local_batch_size=config.batch_size // jax.process_count(),
        sharding=sharding,
        sampler=sampler,
        num_batches=num_batches,
        num_workers=config.num_workers,
        seed=seed,
    )
    if config.dataloader_workers_cpu_only and config.num_workers > 0:
        data_loader.torch_loader.worker_init_fn = _cpu_only_worker_init_fn

    return DataLoaderImpl(data_config, data_loader)
