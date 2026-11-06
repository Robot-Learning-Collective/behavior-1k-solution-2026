"""Pin the practice worker's simulator to one GPU and fail closed if it ever allocates on another.

Set ASTRA_GPU_UUID to the GPU to use (default: the first GPU nvidia-smi lists). On a multi-GPU host,
also hide the other GPUs' device nodes from the worker (we used a private mount namespace): Isaac Sim's
Vulkan renderer enumerates devices on its own. Run this file directly for a one-off graphics+physics check.

ASTRA_RUNTIME_ROOT holds isolated Isaac/Kit caches (default: <repo>/.runtime); ASTRA_ISOLATE_CACHES=0 keeps
the host's warm caches instead, which boots the worker in about 2 minutes instead of 10+.
"""
import json
import os
from pathlib import Path
import subprocess
import threading
import time
import xml.etree.ElementTree as ET

def _gpus():
    try:
        return [line.split(', ') for line in subprocess.check_output(
            ['nvidia-smi', '--query-gpu=index,uuid', '--format=csv,noheader'], text=True, timeout=30).splitlines()]
    except (OSError, subprocess.SubprocessError):
        return []  # no GPU (CPU tests); isolate_gpu() refuses to start a simulator


GPUS = _gpus()
UUID = os.environ.get('ASTRA_GPU_UUID') or (GPUS[0][1] if GPUS else None)
INDEX = next((index for index, uuid in GPUS if uuid == UUID), None)
ROOT = Path(os.environ.get('ASTRA_RUNTIME_ROOT', str(Path(__file__).resolve().parents[2] / '.runtime')))
if INDEX is not None:
    os.environ['CUDA_VISIBLE_DEVICES'] = UUID
    os.environ['OMNIGIBSON_GPU_ID'] = INDEX
os.environ['OMNIGIBSON_HEADLESS'] = '1'
os.environ['OMNI_KIT_ACCEPT_EULA'] = 'YES'
if os.environ.get('ASTRA_ISOLATE_CACHES', '1') == '1':
    os.environ['OMNIGIBSON_APPDATA_PATH'] = str(ROOT / 'appdata')
    os.environ['XDG_CACHE_HOME'] = str(ROOT / 'cache')
    os.environ['HOME'] = str(ROOT / 'home')
    for folder in ('appdata', 'cache', 'home'):
        (ROOT / folder).mkdir(parents=True, exist_ok=True)
seen = set()
stop = threading.Event()


def guard():
    while not stop.wait(1):
        try:
            # One transient NVML timeout must not kill a healthy boot: retry the same full census once.
            for attempt in range(2):
                try:
                    data = subprocess.check_output(['nvidia-smi', '-q', '-x'], timeout=8)
                    break
                except subprocess.TimeoutExpired:
                    if attempt:
                        raise
                    print('GPU_GUARD_QUERY_RETRY TimeoutExpired', flush=True)
            tree = ET.fromstring(data)
            for gpu in tree.findall('gpu'):
                for process in gpu.findall('processes/process_info'):
                    if int(process.findtext('pid')) != os.getpid():
                        continue
                    uuid = gpu.findtext('uuid')
                    seen.add(uuid)
                    if uuid != UUID:
                        print('GPU_BOUNDARY_VIOLATION', os.getpid(), uuid, flush=True)
                        os._exit(73)  # stop only this process; never touch other workloads
        except (subprocess.SubprocessError, ET.ParseError, OSError, ValueError, TypeError) as error:
            print('GPU_GUARD_ERROR', type(error).__name__, flush=True)
            os._exit(74)


def isolate_gpu():
    if INDEX is None:
        raise SystemExit(f'GPU {UUID} is not on this host')
    threading.Thread(target=guard, daemon=True).start()
    import isaacsim
    native = isaacsim.SimulationApp

    def simulation_app(config, *args, **kwargs):
        config.update(active_gpu=0, physics_gpu=0, multi_gpu=False)
        print('EXPLICIT_GPU_CONFIG', json.dumps(config), flush=True)
        return native(config, *args, **kwargs)
    isaacsim.SimulationApp = simulation_app


if __name__ == '__main__':
    isolate_gpu()
    import omnigibson as og
    og.gm.RENDER_VIEWER_CAMERA = False
    og.launch(physics_dt=1/120, rendering_dt=1/30, sim_step_dt=1/30, device='cpu')
    for _ in range(30):
        og.sim.step()
    time.sleep(2)  # one bounded allocation sample after real physics
    if seen != {UUID}:
        raise RuntimeError(f'Expected allocation only on {UUID}, got {seen}')
    (ROOT / 'gpu_canary.json').write_text(json.dumps({'pid': os.getpid(), 'uuid': UUID, 'seen': sorted(seen),
                                                       'version': og.__version__}, indent=2) + '\n')
    print('GPU_CANARY_READY', sorted(seen), flush=True)
    stop.set()
    og.shutdown()
