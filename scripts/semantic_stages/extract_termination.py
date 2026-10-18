"""Per-episode effective end (first frame of the trailing terminated=True run) for all 20k demos."""
import glob, os, sys
import numpy as np, pandas as pd, pyarrow.parquet as pq
ROOT = os.environ.get("B1K_DEMOS_ROOT", "data/2026-challenge-demos")
out = {}
files = sorted(glob.glob(f"{ROOT}/data/chunk-*/file-*.parquet"))
for i, f in enumerate(files):
    t = pq.read_table(f, columns=["episode_index", "frame_index", "next.terminated"]).to_pandas()
    t["term"] = t["next.terminated"].apply(lambda v: bool(np.asarray(v).reshape(-1)[0]))
    for ep, g in t.groupby("episode_index", sort=False):
        g = g.sort_values("frame_index")
        term = g["term"].to_numpy()
        n = len(term)
        if term[-1]:
            non = np.where(~term)[0]
            tail_start = int(non[-1]) + 1 if non.size else 0
        else:
            tail_start = n  # never terminated at the end
        # any mid-episode blips?
        blips = int(np.sum(np.diff(term.astype(int)) == 1)) - (1 if term[-1] else 0)
        prev = out.get(ep)
        if prev is None:
            out[ep] = dict(n=n, completion_frame=tail_start, ends_terminated=bool(term[-1]), blips=blips,
                           first_term=int(np.argmax(term)) if term.any() else -1, nterm=int(term.sum()))
        else:  # episode split across files: merge conservatively
            prev["n"] += n; prev["nterm"] += int(term.sum()); prev["split"] = True
    if i % 50 == 0:
        print(i, len(files), len(out), flush=True)
df = pd.DataFrame.from_dict(out, orient="index").rename_axis("episode_index").reset_index()
df.to_csv(os.path.join(os.environ.get("STAGE_OUT", "outputs/semantic_stages/v2"), "termination.csv"))
print("done", len(df))
