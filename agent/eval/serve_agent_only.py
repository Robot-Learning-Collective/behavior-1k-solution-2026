"""Agent-only policy server: the real serve_b1k.py connection handler and agent route, no learned policy.

Lets you run agent episodes (agent/eval/run_episode.py) on a machine without JAX or the VLA checkpoint.
The handler class is compiled from scripts/serve_b1k.py unchanged, with its JAX worker replaced by a stub;
a non-agent task on this server fails loudly instead of playing the learned policy.

    python -m agent.eval.serve_agent_only --port 8000 [--host 0.0.0.0]

Without the frozen-context bundle every task is disabled and the server refuses to start (agent/README.md).
"""
import argparse
import ast
import asyncio
import json
import os
from pathlib import Path
import signal
import sys
import threading
from types import SimpleNamespace

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / 'agent/control'))
from official_policy_server import pack, unpack  # noqa: E402


class _Parent:
    """Stand-in for omnigibson's WebsocketPolicyServer base class."""
    def __init__(self, policy=None, port=8000, metadata=None):
        self._host, self._port, self._metadata = '127.0.0.1', port, metadata or {}


def load_agent_route():
    """src/b1k/policies/agent.py as b1k.policies.agent, without importing the b1k package (openpi, JAX)."""
    import importlib.util
    if 'b1k.policies.agent' not in sys.modules:
        spec = importlib.util.spec_from_file_location('b1k.policies.agent', REPO / 'src/b1k/policies/agent.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules['b1k.policies.agent'] = module
    return sys.modules['b1k.policies.agent']


def load_server_class(act_batched=None):
    """MultiSessionPolicyServer from scripts/serve_b1k.py, without importing JAX or omnigibson."""
    tree = ast.parse((REPO / 'scripts/serve_b1k.py').read_text())
    node = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'MultiSessionPolicyServer')
    net = SimpleNamespace(WebsocketPolicyServer=_Parent, Packer=lambda: SimpleNamespace(pack=pack),
                          unpackb=lambda data, **kw: unpack(data))
    import concurrent.futures
    import logging
    import time
    from copy import deepcopy
    import numpy as np
    import websockets
    scope = dict(asyncio=asyncio, concurrent=concurrent, logging=logging, time=time, deepcopy=deepcopy, np=np,
                 websockets=websockets, _net=net, act_batched=act_batched, PROPRIO_KEY='robot_r1::proprio')
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(REPO / 'scripts/serve_b1k.py'), 'exec'), scope)
    return scope[node.name]


class UnavailableBase:
    def reset(self):
        pass

    def act(self, obs):
        raise RuntimeError('No learned policy on the agent-only server; this task is not routed to the agent')


async def handle_connection(server, websocket, stopped, exit_on_disconnect):
    """Serve one evaluator connection; with exit_on_disconnect (full runs) stop the server afterwards."""
    try:
        await server._handler(websocket)
    finally:
        if exit_on_disconnect:
            stopped.set()


def tracked_runtime(original, active, shutting_down):
    """FrozenRuntime subclass that registers each episode runtime for shutdown, and never outlives a shutdown:
    a runtime that finishes starting after shutdown began is closed at once."""
    class TrackedRuntime(original):
        def __init__(self, entry, epoch, config):
            if shutting_down.is_set():
                raise RuntimeError('Agent-only server is shutting down')
            if os.environ.get('B1K_AGENT_SMOKE') == '1':
                config = {**config, 'qualification_only': True}
            super().__init__(entry, epoch, config)
            active.append(self)
            if shutting_down.is_set():
                self.close()
                raise RuntimeError('Agent-only server is shutting down')
    return TrackedRuntime


def close_all(active, shutting_down):
    shutting_down.set()
    for instance in list(active):
        instance.close()


async def main(port, host='127.0.0.1'):
    from websockets.asyncio.server import serve
    sys.path.insert(0, str(REPO))
    route = load_agent_route()
    from agent.eval import runtime
    active, shutting_down = [], threading.Event()
    runtime.FrozenRuntime = tracked_runtime(runtime.FrozenRuntime, active, shutting_down)
    tasks = route.load_enabled_tasks()
    if not tasks:
        raise SystemExit('No agent tasks are enabled (no frozen contexts); this server has nothing to serve')
    if not route.startup_check(tasks):
        raise SystemExit(1)
    server = load_server_class()(UnavailableBase, port=port, metadata={'server': 'agent-only'}, agent_tasks=tasks)
    stopped = asyncio.Event()
    for sig in (signal.SIGTERM, signal.SIGINT):
        asyncio.get_running_loop().add_signal_handler(sig, stopped.set)

    def health(connection, request):
        if request.path == '/healthz':
            return connection.respond(200, 'agent route ready\n')

    async def handler(websocket):
        await handle_connection(server, websocket, stopped, os.environ.get('B1K_AGENT_EXIT_ON_DISCONNECT') == '1')

    try:
        async with serve(handler, host, port, compression=None, max_size=None,
                         ping_interval=20, ping_timeout=600, process_request=health):
            print('AGENT_ROUTE_READY', port, json.dumps(sorted(e['task_name'] for e in tasks.values())), flush=True)
            try:
                await stopped.wait()
            finally:
                # Close runtimes before leaving the server context, also on cancellation: the context waits for
                # handlers that may be blocked on an in-flight agent query, which returns once its runtime closes.
                await asyncio.to_thread(close_all, active, shutting_down)
    finally:
        await asyncio.to_thread(close_all, active, shutting_down)
        server._worker.shutdown(wait=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--port', type=int, required=True)
    parser.add_argument('--host', default='127.0.0.1', help='0.0.0.0 inside a container')
    args = parser.parse_args()
    asyncio.run(main(args.port, args.host))
