"""Checkpoint management with FAST tokenizer saving.

Reference: https://github.com/Physical-Intelligence/openpi
"""

from __future__ import annotations

import asyncio
import concurrent.futures as futures
import dataclasses
import logging
import shutil
from typing import Protocol

from etils import epath
import flax.traverse_util
import jax
import flax.nnx as nnx

import orbax.checkpoint as ocp
import orbax.checkpoint.future as future

from openpi.shared import array_typing as at
import openpi.training.data_loader as _data_loader
import openpi.training.utils as training_utils

# Use our custom normalize (has per_timestamp fields and can save/load them)
from b1k.shared import normalize as _normalize


class _DrainingPyTreeCheckpointHandler(ocp.PyTreeCheckpointHandler):
    """Writes each item to disk before the next one is staged, so host RAM holds one item at a time
    (low-memory machines; the save then blocks training while it runs)."""

    _lock = None

    async def async_save(self, directory, args):
        if type(self)._lock is None:
            type(self)._lock = asyncio.Lock()
        # stage through pinned host buffers: the default path caches a host copy on every live array
        if hasattr(args, "enable_pinned_host_transfer"):
            args = dataclasses.replace(args, enable_pinned_host_transfer=True)
        async with type(self)._lock:
            for f in await super().async_save(directory, args=args) or []:
                f.result()
        return []


@ocp.args.register_with_handler(_DrainingPyTreeCheckpointHandler, for_save=True)
class _DrainingSaveArgs(ocp.args.PyTreeSave): ...


@ocp.args.register_with_handler(_DrainingPyTreeCheckpointHandler, for_restore=True)
class _DrainingRestoreArgs(ocp.args.PyTreeRestore): ...


# The train state is saved as params-sized items (orbax stages each item in host RAM as a whole)
ITEMS = ("train_state", "params", "train_params", "opt_mu", "opt_nu")


def initialize_checkpoint_dir(
    checkpoint_dir: epath.Path | str, *, keep_period: int | None, overwrite: bool, resume: bool, low_memory: bool = False
) -> tuple[ocp.CheckpointManager, bool]:
    checkpoint_dir = epath.Path(checkpoint_dir).resolve()
    resuming = False
    if checkpoint_dir.exists():
        if overwrite:
            checkpoint_dir.rmtree()
            checkpoint_dir.mkdir(parents=True, exist_ok=True)
            logging.info(f"Wiped checkpoint directory {checkpoint_dir}")
        elif resume:
            resuming = True
        else:
            raise FileExistsError(
                f"Checkpoint directory {checkpoint_dir} already exists. Use --overwrite or --resume "
                "to indicate how to handle it."
            )

    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    mngr = ocp.CheckpointManager(
        checkpoint_dir,
        item_handlers={
            "assets": CallbackHandler(),
            **{
                name: (_DrainingPyTreeCheckpointHandler(save_concurrent_gb=8, restore_concurrent_gb=8) if low_memory
                       else ocp.PyTreeCheckpointHandler())
                for name in ITEMS
            },
        },
        options=ocp.CheckpointManagerOptions(
            max_to_keep=1,
            keep_period=keep_period,
            create=False,
            async_options=ocp.AsyncOptions(timeout_secs=7200),
        ),
    )

    # Special case: the checkpoint directory exists and the user requests to resume training, but the training run did
    # not get to the first checkpoint saved. In this case, we don't actually want the train script to try and restore a
    # checkpoint, since it will fail.
    if resuming and tuple(mngr.all_steps()) in [(), (0,)]:
        logging.info("Checkpoint directory exists, but does not contain any checkpoints. Aborting resume.")
        resuming = False

    return mngr, resuming


def save_state(
    checkpoint_manager: ocp.CheckpointManager,
    state: training_utils.TrainState,
    data_loader: _data_loader.DataLoader,
    step: int,
):
    def save_assets(directory: epath.Path):
        # Save the normalization stats.
        data_config = data_loader.data_config()
        norm_stats = data_config.norm_stats
        if norm_stats is not None and data_config.asset_id is not None:
            _normalize.save(directory / data_config.asset_id, norm_stats)
        
        # Save FAST tokenizer if it exists
        model = nnx.merge(state.model_def, state.params)
        # Check if model has FAST enabled (indicated by having fast_token_embedding)
        if hasattr(model, 'fast_token_embedding'):
            # Get the checkpoint directory to determine assets base dir
            # Directory structure: checkpoint_dir/step/assets/asset_id/fast_tokenizer
            # We need to copy from: assets_base_dir/asset_id/fast_tokenizer
            # The assets_base_dir is stored in the config, but we can infer it from checkpoint_dir
            checkpoint_dir = checkpoint_manager.directory
            
            # Infer assets_base_dir from checkpoint structure
            # checkpoint_dir is like: ./outputs/checkpoints/config_name/exp_name
            # assets_base_dir is like: ./outputs/assets/config_name
            parts = checkpoint_dir.parts
            if 'checkpoints' in parts:
                idx = parts.index('checkpoints')
                assets_base_parts = parts[:idx] + ('assets',) + (parts[idx + 1],)  # Keep config_name
                assets_base_dir = epath.Path(*assets_base_parts)
            else:
                # Fallback: try relative to checkpoint dir
                assets_base_dir = checkpoint_dir.parent.parent / 'assets' / checkpoint_dir.parent.name
            
            fast_tokenizer_source = assets_base_dir / data_config.asset_id / "fast_tokenizer"
            fast_tokenizer_dest = directory / data_config.asset_id / "fast_tokenizer"
            
            if fast_tokenizer_source.exists():
                # Create parent directory
                fast_tokenizer_dest.parent.mkdir(parents=True, exist_ok=True)
                # Copy tokenizer directory
                shutil.copytree(fast_tokenizer_source, fast_tokenizer_dest, dirs_exist_ok=True)
                logging.info(f"Saved FAST tokenizer to checkpoint: {fast_tokenizer_dest}")

    # Split params that can be used for inference into a separate item.
    with at.disable_typechecking():
        items = _split_items(state)
    checkpoint_manager.save(step, {"assets": save_assets, **items})


def restore_state(
    checkpoint_manager: ocp.CheckpointManager,
    state: training_utils.TrainState,
    data_loader: _data_loader.DataLoader,
    step: int | None = None,
) -> training_utils.TrainState:
    del data_loader

    with at.disable_typechecking():
        restored = checkpoint_manager.restore(step, items=_split_items(state))
        return _join_items(restored)


def load_norm_stats(assets_dir: epath.Path | str, asset_id: str) -> dict[str, _normalize.NormStats] | None:
    norm_stats_dir = epath.Path(assets_dir) / asset_id
    norm_stats = _normalize.load(norm_stats_dir)
    logging.info(f"Loaded norm stats from {norm_stats_dir}")
    return norm_stats


class Callback(Protocol):
    def __call__(self, directory: epath.Path) -> None: ...


class CallbackHandler(ocp.AsyncCheckpointHandler):
    """A CheckpointHandler for calling an arbitrary function asynchronously. Only for saving, not for restoring."""

    def save(self, directory: epath.Path, args: CallbackSave):
        if jax.process_index() == 0:
            args.callback(directory)

    async def async_save(self, directory: epath.Path, args: CallbackSave) -> list[futures.Future]:
        return [future.CommitFutureAwaitingContractedSignals(asyncio.to_thread(self.save, directory, args))]

    def restore(self, *args, **kwargs):
        raise NotImplementedError("CallbackHandler does not support restore")


@ocp.args.register_with_handler(CallbackHandler, for_save=True)
@dataclasses.dataclass
class CallbackSave(ocp.args.CheckpointArgs):
    callback: Callback


@ocp.args.register_with_handler(CallbackHandler, for_restore=True)
class CallbackRestore(ocp.args.CheckpointArgs): ...


def _split_params(state: training_utils.TrainState) -> tuple[training_utils.TrainState, at.Params]:
    if state.ema_params is not None:
        params = state.ema_params
        train_state = dataclasses.replace(state, ema_params=None)
    else:
        params = state.params
        train_state = dataclasses.replace(state, params={})
    return train_state, params


def _merge_params(train_state: training_utils.TrainState, params: dict[str, at.Params]) -> training_utils.TrainState:
    # Revert the logic inside `_split_params`.
    # If the restored train_state has an empty `params` dict, it means we're in the non-EMA case
    # and we should restore the main training params.
    if not train_state.params:
        # Non-EMA case: The saved 'params' are the training weights.
        return dataclasses.replace(train_state, params=params["params"])
    else:
        # EMA case: The saved 'params' are the ema_params, and train_state already has the training params.
        return dataclasses.replace(train_state, ema_params=params["params"])


def _moment_paths(tree, path=()):
    """Paths of the optax states holding Adam moments (fields mu and nu)."""
    if hasattr(tree, "_fields") and "mu" in tree._fields:
        return [path]
    if isinstance(tree, (tuple, list)):
        return [p for i, child in enumerate(tree) for p in _moment_paths(child, path + (i,))]
    return []


def _replace_at(tree, path, fn):
    if not path:
        return fn(tree)
    children = [_replace_at(c, path[1:], fn) if j == path[0] else c for j, c in enumerate(tree)]
    return type(tree)(*children) if hasattr(tree, "_fields") else type(tree)(children)


def _get_at(tree, path):
    for i in path:
        tree = tree[i]
    return tree


def _split_items(state: training_utils.TrainState) -> dict:
    """{train_state (step + optimizer skeleton), params (servable / EMA), train_params, opt_mu, opt_nu}."""
    train_state, params = _split_params(state)
    paths = _moment_paths(train_state.opt_state)
    mu = {str(i): _get_at(train_state.opt_state, p).mu for i, p in enumerate(paths)}
    nu = {str(i): _get_at(train_state.opt_state, p).nu for i, p in enumerate(paths)}
    opt = train_state.opt_state
    for p in paths:
        opt = _replace_at(opt, p, lambda node: node._replace(mu=None, nu=None))
    items = {
        "train_state": dataclasses.replace(train_state, params={}, opt_state=opt),
        "params": {"params": params},
        "opt_mu": {"mu": mu},
        "opt_nu": {"nu": nu},
    }
    if state.ema_params is not None:
        items["train_params"] = {"params": train_state.params}
    return items


def _join_items(items: dict) -> training_utils.TrainState:
    opt = items["train_state"].opt_state
    for i, p in enumerate(_moment_paths(opt)):
        opt = _replace_at(opt, p, lambda node: node._replace(mu=items["opt_mu"]["mu"][str(i)], nu=items["opt_nu"]["nu"][str(i)]))
    train_state = dataclasses.replace(items["train_state"], opt_state=opt, params=items.get("train_params", {"params": {}})["params"])
    return _merge_params(train_state, items["params"])
