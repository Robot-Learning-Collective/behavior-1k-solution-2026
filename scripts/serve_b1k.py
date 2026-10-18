import asyncio
import concurrent.futures
import dataclasses
import logging
import os
import socket
from copy import deepcopy

import numpy as np
import tyro
import websockets

# Set JAX memory allocation before importing JAX (can be overridden by env vars)
os.environ.setdefault('XLA_PYTHON_CLIENT_MEM_FRACTION', '0.5')  # Use 50% of GPU memory
os.environ.setdefault('XLA_PYTHON_CLIENT_ALLOCATOR', 'platform')  # Platform allocator

from b1k.shared.cuda_env import ensure_packaged_ptxas

ensure_packaged_ptxas()

from omnigibson.eval.utils import network_utils as _net

# Import B1K-specific modules
from b1k.policies import policy_config as _policy_config  # Use our custom policy_config
from b1k.shared.eval_b1k_wrapper import B1KPolicyWrapper, B1KWrapperConfig, act_batched
from b1k.training.yaml_train_config import resolve_train_config

PROPRIO_KEY = "robot_r1::proprio"


@dataclasses.dataclass
class Checkpoint:
    """Load a policy from a trained checkpoint."""
    config: str  # registered config name or YAML recipe
    dir: str


@dataclasses.dataclass
class Args:
    """Arguments for the serve_policy script."""

    policy: Checkpoint
    # Port to serve the policy on.
    port: int = 8000
    # Flow matching denoising steps
    num_steps: int = 20
    # Rollout parameters
    wrapper: B1KWrapperConfig = dataclasses.field(default_factory=B1KWrapperConfig)


class MultiSessionPolicyServer(_net.WebsocketPolicyServer):
    """Every connection gets its own wrappers (rollout state) around the shared, stateless JAX policy, so
    several evaluators can run against one server. A batched observation ((N, ...) arrays from a
    vectorized evaluator) gets N wrappers. Model calls run on one worker thread."""

    def __init__(self, policy_factory, port: int, metadata: dict):
        super().__init__(policy=None, port=port, metadata=metadata)
        self._policy_factory = policy_factory
        self._worker = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    async def _on_worker(self, fn, *args):
        return await asyncio.get_running_loop().run_in_executor(self._worker, fn, *args)

    async def run(self):
        # No keepalive pings: a long simulator step blocks the client from answering them
        async with _net._server.serve(
            self._handler, self._host, self._port, compression=None, max_size=None,
            process_request=_net._health_check, ping_interval=None,
        ) as server:
            await server.serve_forever()

    async def _handler(self, websocket):
        logging.info(f"Connection from {websocket.remote_address} opened")
        session_policy = self._policy_factory()
        batch_policies = None
        packer = _net.Packer()
        await websocket.send(packer.pack(self._metadata))
        while True:
            try:
                message = _net.unpackb(await websocket.recv(), strict_map_key=False)
                if "reset" in message:
                    # slot-refilling evaluators reset only the reloaded environments
                    env_indices = message.get("env_indices")
                    if env_indices is None:
                        to_reset = [session_policy, *(batch_policies or [])]
                    else:
                        to_reset = [batch_policies[int(i)] for i in env_indices] if batch_policies else []
                    await self._on_worker(lambda: [p.reset() for p in to_reset])
                    continue

                obs = deepcopy(message)
                if np.ndim(obs[PROPRIO_KEY]) == 2:
                    if batch_policies is None:
                        batch_policies = [self._policy_factory() for _ in range(len(obs[PROPRIO_KEY]))]
                    action = await self._on_worker(act_batched, batch_policies, obs)
                else:
                    action = await self._on_worker(session_policy.act, obs)
                await websocket.send(packer.pack({"action": action.cpu().numpy()}))
            except websockets.ConnectionClosed:
                logging.info(f"Connection from {websocket.remote_address} closed")
                break


def main(args: Args) -> None:
    config = resolve_train_config(args.policy.config)
    policy = _policy_config.create_trained_policy(config, args.policy.dir, sample_kwargs={"num_steps": args.num_steps})
    logging.info(f"Wrapper config: {args.wrapper}")

    hostname = socket.gethostname()
    logging.info("Creating server (host: %s, ip: %s)", hostname, socket.gethostbyname(hostname))
    server = MultiSessionPolicyServer(
        lambda: B1KPolicyWrapper(policy, config=args.wrapper), port=args.port, metadata=policy.metadata
    )
    server.serve_forever()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    main(tyro.cli(Args))
