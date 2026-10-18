"""Build a TrainConfig from a YAML recipe (see configs/train_b1k_2026.yaml).

`base_config` names a registered config; top-level keys override TrainConfig fields, `model` / `data` /
`lr_schedule` / `optimizer` / `lr_multipliers` sections override those dataclasses, `init_checkpoint` sets
the weight loader. Unknown keys raise, so typos never silently train with defaults.
"""

import dataclasses
from typing import Any

import yaml

from b1k.models.observation import TrainAugmentationConfig
from b1k.training import config as _config
from b1k.training import weight_loaders
from b1k.training.data_loader import DataSourceConfig

_SECTIONS = ("model", "data", "lr_schedule", "optimizer", "lr_multipliers")


def _replace(obj: Any, raw: dict, section: str) -> Any:
    known = {f.name for f in dataclasses.fields(obj)}
    if unknown := set(raw) - known:
        raise ValueError(f"Unknown keys in '{section}': {sorted(unknown)}. Known: {sorted(known)}")
    return dataclasses.replace(obj, **{k: tuple(v) if isinstance(v, list) else v for k, v in raw.items()})


def train_config_from_yaml(path: str, overrides: dict[str, Any] | None = None) -> _config.TrainConfig:
    with open(path) as f:
        raw = yaml.safe_load(f) or {}
    cfg = _config.get_config(raw.pop("base_config"))
    kwargs = {}

    if "init_checkpoint" in raw:
        ckpt = raw.pop("init_checkpoint")
        kwargs["weight_loader"] = weight_loaders.PiBehaviorWeightLoader(ckpt) if ckpt else weight_loaders.NoOpWeightLoader()

    model = dict(raw.pop("model", {}))
    if "train_aug" in model:
        model["train_aug"] = _replace(TrainAugmentationConfig(), model.pop("train_aug"), "model.train_aug")
    kwargs["model"] = _replace(cfg.model, model, "model")

    data = dict(raw.pop("data", {}))
    data_cfg = cfg.data
    if "asset_id" in data:
        data_cfg = dataclasses.replace(data_cfg, assets=_config.AssetsConfig(asset_id=data.pop("asset_id")))
    if "use_per_timestamp_norm" in data:
        base = data_cfg.base_config or _config.DataConfig()
        data_cfg = dataclasses.replace(
            data_cfg, base_config=dataclasses.replace(base, use_per_timestamp_norm=data.pop("use_per_timestamp_norm"))
        )
    if "data_sources" in data:
        data["data_sources"] = [_replace(DataSourceConfig(repo_id=""), src, "data.data_sources") for src in data["data_sources"]]
    kwargs["data"] = _replace(data_cfg, data, "data")

    for section in _SECTIONS[2:]:
        kwargs[section] = _replace(getattr(cfg, section), raw.pop(section, {}), section)

    kwargs.update(raw)
    kwargs.update(overrides or {})
    return _replace(cfg, kwargs, "top level")


def resolve_train_config(name_or_yaml: str) -> _config.TrainConfig:
    """A registered config name or a .yaml recipe path."""
    if str(name_or_yaml).endswith((".yaml", ".yml")):
        return train_config_from_yaml(name_or_yaml)
    return _config.get_config(name_or_yaml)
