"""Per task and stage: demo stage durations in frames (30 fps) over the demos, empty (skipped) stages excluded
-> assets/semantic_stages/stage_len_stats.json (the minimum-stage-time rule of B1KPolicyWrapper)."""
import json
import sys

import numpy as np
import pandas as pd

labels = sys.argv[1] if len(sys.argv) > 1 else "assets/semantic_stages/episode_stage_frames.csv"
out = sys.argv[2] if len(sys.argv) > 2 else "assets/semantic_stages/stage_len_stats.json"
df = pd.read_csv(labels)
df["task"], df["len"] = df.episode_index // 200, df.end - df.start
lengths = df[df.len > 0].groupby(["task", "episode_index", "stage"]).len.sum().reset_index()
stats = {}
for t, g in lengths.groupby("task"):
    rows = []
    for s in range(df[df.task == t].stage.max() + 1):
        x = g[g.stage == s].len.to_numpy()
        q = [int(v) for v in np.percentile(x, [5, 10, 50, 90, 95])] if len(x) else [0] * 5
        rows.append({"n": len(x), "min": int(x.min()) if len(x) else 0, "p05": q[0], "p10": q[1], "p50": q[2],
                     "p90": q[3], "p95": q[4], "max": int(x.max()) if len(x) else 0})
    stats[str(t)] = rows
json.dump({"_doc": __doc__.strip(), "fps": 30, "stats": stats}, open(out, "w"))
