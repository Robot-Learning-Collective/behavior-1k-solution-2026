"""Training-only replacement of openpi's Gemma attention with jax.nn.dot_product_attention.

Same math and parameters as gemma.Attention (including the attention sink slot), but the score matrix is
never materialized in fp32, which cuts memory and step time. Keys can be padded with masked zeros to a
multiple of `key_pad_multiple` for tensor-core friendly shapes. Call install() before building the model.
"""

import logging

import flax.linen as nn
import jax
import jax.numpy as jnp

logger = logging.getLogger(__name__)


def install(key_pad_multiple: int = 1):
    from openpi.models import gemma as _gemma
    from openpi.models.gemma import _apply_rope, _name, lora

    class FlashAttention(_gemma.Attention):
        @nn.compact
        def __call__(self, xs, positions, attn_mask, kv_cache):
            config0 = self.configs[0]
            qkvs = []
            for i, (x, config) in enumerate(zip(xs, self.configs, strict=True)):
                if x is None:
                    continue
                q = lora.Einsum(
                    shape=(config.num_heads, config.width, config.head_dim),
                    name=_name("q_einsum", i),
                    init_fn=nn.initializers.lecun_normal(in_axis=-2, out_axis=-1, batch_axis=(0,)),
                    lora_config=config.lora_configs.get("attn"),
                )("BTD,NDH->BTNH", x)
                k, v = lora.Einsum(
                    shape=(2, config.num_kv_heads, config.width, config.head_dim),
                    name=_name("kv_einsum", i),
                    init_fn=nn.initializers.lecun_normal(in_axis=-2, out_axis=-1, batch_axis=(0, 1)),
                    lora_config=config.lora_configs.get("attn"),
                )("BSD,2KDH->2BSKH", x)
                qkvs.append((q, k, v))
            q, k, v = (jnp.concatenate(y, axis=1) for y in zip(*qkvs, strict=True))
            q = _apply_rope(q, positions=positions)
            k = _apply_rope(k, positions=positions)
            if kv_cache is not None:
                k = jnp.concatenate([kv_cache[0], k], axis=1)
                v = jnp.concatenate([kv_cache[1], v], axis=1)

            k_att, v_att, mask, bias = k, v, attn_mask, None
            if self.sink_slot:
                # virtual key: zero key, logit from a per-head bias, learnable per-KV-head value
                n_kv, n_q = config0.num_kv_heads, config0.num_heads
                sink_logit = self.param("sink_logit", nn.initializers.zeros, (n_kv, n_q // n_kv))
                sink_value = self.param("sink_value", nn.initializers.normal(0.02), (n_kv, config0.head_dim))
                k_att = jnp.concatenate([k, jnp.zeros_like(k[:, :1])], axis=1)
                v_att = jnp.concatenate([v, jnp.broadcast_to(sink_value.astype(v.dtype), v[:, :1].shape)], axis=1)
                mask = jnp.concatenate([mask, jnp.ones_like(mask[..., :1])], axis=-1)
                bias = jnp.zeros((1, n_q, 1, k_att.shape[1]), jnp.float32)
                bias = bias.at[:, :, :, -1].set(sink_logit.reshape(n_q)[None, :, None]).astype(q.dtype)
            pad = (-k_att.shape[1]) % key_pad_multiple
            if pad:
                k_att = jnp.pad(k_att, ((0, 0), (0, pad), (0, 0), (0, 0)))
                v_att = jnp.pad(v_att, ((0, 0), (0, pad), (0, 0), (0, 0)))
                mask = jnp.pad(mask, ((0, 0), (0, 0), (0, 0), (0, pad)))
                if bias is not None:
                    bias = jnp.pad(bias, ((0, 0), (0, 0), (0, 0), (0, pad)))
            encoded = jax.nn.dot_product_attention(
                q, k_att, v_att, bias=bias, mask=mask, scale=config0.head_dim**-0.5, implementation="xla"
            )

            out = []
            start = 0
            for i, (x, config) in enumerate(zip(xs, self.configs, strict=True)):
                if x is None:
                    out.append(None)
                    continue
                end = start + x.shape[1]
                out.append(lora.Einsum(
                    shape=(config.num_heads, config.head_dim, config.width),
                    name=_name("attn_vec_einsum", i),
                    init_fn=nn.initializers.lecun_normal(in_axis=(-3, -2), out_axis=-1),
                    lora_config=config.lora_configs.get("attn"),
                )("BTNH,NHD->BTD", encoded[:, start:end]))
                start = end
            return out, (k, v)

    # Block looks up `Attention` at call time, so every later model construction uses the patch
    _gemma.Attention = FlashAttention
    logger.info(f"Installed flash attention patch (key_pad_multiple={key_pad_multiple})")
