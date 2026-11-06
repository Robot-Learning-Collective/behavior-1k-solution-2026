import asyncio
import concurrent.futures
import dataclasses
import logging
import os
import socket
import sys
import time
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
    # Route the tasks enabled in agent/tasks/tasks.json to the GPT-6 Astra agent (agent/README.md);
    # every other task, and any agent episode that fails, is played by the learned policy.
    agent: bool = False
    # Flow matching denoising steps
    num_steps: int = 20
    # Rollout parameters
    wrapper: B1KWrapperConfig = dataclasses.field(default_factory=B1KWrapperConfig)


class MultiSessionPolicyServer(_net.WebsocketPolicyServer):
    """Every connection gets its own wrappers (rollout state) around the shared, stateless JAX policy, so
    several evaluators can run against one server. A batched observation ((N, ...) arrays from a
    vectorized evaluator) gets N wrappers. Model calls run on one worker thread.
    With agent tasks, each connection also gets an AgentRoute that answers routed episodes itself."""

    def __init__(self, policy_factory, port: int, metadata: dict, agent_tasks=None):
        super().__init__(policy=None, port=port, metadata=metadata)
        self._policy_factory = policy_factory
        self._agent_tasks = agent_tasks
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
        agent = None
        if self._agent_tasks:
            from b1k.policies.agent import AgentRoute
            agent = AgentRoute(self._agent_tasks)
        try:
            await self._serve(websocket, agent)
        finally:
            if agent is not None:
                await asyncio.to_thread(agent.shutdown)

    async def _serve(self, websocket, agent):
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
                    if agent is not None:
                        await agent.call(agent.reset, env_indices)
                    if env_indices is None:
                        to_reset = [session_policy, *(batch_policies or [])]
                    else:
                        to_reset = [batch_policies[int(i)] for i in env_indices] if batch_policies else []
                    await self._on_worker(lambda: [p.reset() for p in to_reset])
                    continue

                obs = deepcopy(message)
                if agent is not None:
                    # Runs on the route's own thread (not the JAX worker) while the agent plans.
                    # None means the learned policy plays this step (other task, or fallback).
                    start = time.monotonic()
                    action = await agent.call(agent.step, obs)
                    if action is not None:
                        await websocket.send(packer.pack({
                            "action": action,
                            "server_timing": {"infer_ms": (time.monotonic() - start) * 1000},
                            "action_owner": "agent",
                        }))
                        continue
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


def load_agent_tasks() -> dict:
    """Enabled agent tasks from agent/tasks/tasks.json, keyed by official task id. Stops the server if the
    OpenAI check fails or a frozen context is missing, before the policy loads."""
    from b1k.policies.agent import load_enabled_tasks, startup_check

    tasks = load_enabled_tasks()
    logging.info("Agent routes for %s; those tasks need RGBDFullResWrapper", sorted(e["task_name"] for e in tasks.values()))
    if not startup_check(tasks):
        sys.exit(1)
    return tasks


def main(args: Args) -> None:
    agent_tasks = load_agent_tasks() if args.agent else {}
    config = resolve_train_config(args.policy.config)
    policy = _policy_config.create_trained_policy(config, args.policy.dir, sample_kwargs={"num_steps": args.num_steps})
    logging.info(f"Wrapper config: {args.wrapper}")

    hostname = socket.gethostname()
    logging.info("Creating server (host: %s, ip: %s)", hostname, socket.gethostbyname(hostname))
    server = MultiSessionPolicyServer(
        lambda: B1KPolicyWrapper(policy, config=args.wrapper), port=args.port, metadata=policy.metadata,
        agent_tasks=agent_tasks,
    )
    server.serve_forever()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    main(tyro.cli(Args))
