"""Run BEHAVIOR evaluations with persistent simulator workers against a running serve_b1k.py.

Each worker boots one simulator once and pulls instance indices from a shared queue; an env slot is refilled
as soon as its episode ends. Simulation is CPU-bound, so every worker gets capped thread pools and its own
exclusive CPUs (measured 1.7x faster than unpinned simulators, same success rates).

    uv run scripts/run_parallel_eval.py --task-name turning_on_radio --instance-indices 0 1 2 3 \
        --num-envs 4 --write-video

--num-envs is the number of episodes running at once; --envs-per-worker packs several of them into one
simulator (one batched policy call per step). Unrecognized arguments are passed to the workers.
"""

import argparse
import json
import os
import queue
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

WORKER_SCRIPT = Path(__file__).resolve().parent / "eval_worker.py"
THREAD_LIMITS = {
    "PXR_WORK_THREAD_LIMIT": "4",
    "OMP_NUM_THREADS": "2",
    "MKL_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
}
MAX_ATTEMPTS = 2


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, allow_abbrev=False)
    parser.add_argument("--task-name", required=True)
    parser.add_argument("--instance-indices", type=int, nargs="+", required=True)
    parser.add_argument("--num-envs", type=int, default=4, help="Episodes running at once, in total")
    parser.add_argument("--envs-per-worker", type=int, default=1)
    parser.add_argument("--cpus-per-env", type=int, default=3, help="Exclusive CPUs per env slot (0 = no pinning)")
    parser.add_argument("--output-dir", default="./eval_logs")
    parser.add_argument("--gpu", default="0", help="CUDA_VISIBLE_DEVICES of the simulators")
    args, worker_args = parser.parse_known_args()

    run_dir = Path(args.output_dir) / f"{datetime.now():%Y%m%d_%H%M%S}_{args.task_name}"
    (run_dir / "logs").mkdir(parents=True)
    total = min(args.num_envs, len(args.instance_indices))
    slots = [min(args.envs_per_worker, total - i) for i in range(0, total, args.envs_per_worker)]
    cpus = sorted(os.sched_getaffinity(0))
    if args.cpus_per_env and sum(slots) * args.cpus_per_env > len(cpus):
        raise ValueError(f"{sum(slots)} env slots x {args.cpus_per_env} CPUs do not fit in {len(cpus)} CPUs")

    pending = queue.Queue()
    for idx in args.instance_indices:
        pending.put(idx)
    attempts = {idx: 0 for idx in args.instance_indices}
    failed, lock = [], threading.Lock()

    def worker(w: int) -> None:
        env = {**os.environ, "CUDA_VISIBLE_DEVICES": args.gpu}
        for key, value in THREAD_LIMITS.items():
            env.setdefault(key, value)
        if args.cpus_per_env:
            start = sum(slots[:w]) * args.cpus_per_env
            env["B1K_EVAL_CPU_AFFINITY"] = ",".join(map(str, cpus[start:start + slots[w] * args.cpus_per_env]))
        while not pending.empty():
            command = [sys.executable, str(WORKER_SCRIPT), "--task-name", args.task_name, "--num-envs", str(slots[w]),
                       "--output-dir", str(run_dir), *worker_args]
            print(f"[worker {w}] booting simulator", flush=True)
            proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    text=True, bufsize=1, env=env)
            running, progressed = set(), False
            with open(run_dir / "logs" / f"worker{w}.log", "a") as log:
                for line in proc.stdout:
                    log.write(line)
                    message = line.strip()
                    if message == "@@WORKER_READY":
                        try:
                            idx = pending.get_nowait()
                        except queue.Empty:
                            proc.stdin.write("EXIT\n")
                        else:
                            running.add(idx)
                            proc.stdin.write(f"{idx}\n")
                            print(f"[start] instance {idx} -> worker {w}", flush=True)
                        proc.stdin.flush()
                    elif message.startswith("@@WORKER_OK"):
                        idx = int(message.split()[1])
                        running.discard(idx)
                        progressed = True
                        print(f"[done] instance {idx}", flush=True)
            proc.wait()
            for idx in running:  # crashed mid-episode: requeue once
                with lock:
                    attempts[idx] += 1
                    (pending.put if attempts[idx] < MAX_ATTEMPTS else failed.append)(idx)
            if not progressed and proc.returncode != 0:
                print(f"[worker {w}] exited {proc.returncode} without progress, stopping", flush=True)
                return

    started = time.monotonic()
    threads = [threading.Thread(target=worker, args=(w,)) for w in range(len(slots))]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    results = [json.loads(p.read_text()) for p in sorted((run_dir / "json").glob("*.json"))]
    q = [r.get("q_score", {}).get("final", 0.0) for r in results]
    summary = {
        "task": args.task_name, "episodes": len(results), "success": sum(bool(r["success"]) for r in results),
        "mean_q_score": sum(q) / len(q) if q else None, "failed_instances": failed,
        "minutes": round((time.monotonic() - started) / 60, 1),
    }
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
