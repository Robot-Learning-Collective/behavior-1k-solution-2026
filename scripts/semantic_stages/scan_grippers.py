"""Gripper widths (mean of the 2 finger joint positions, m) and gripper commands of every demo at 10 Hz (every 3rd
frame): one f_<chunk>_<file>.npz per dataset parquet file (input of build_close_allowed.py).

  uv run python scripts/semantic_stages/scan_grippers.py <dataset root> <out dir>
"""
import glob
import os
import sys

import numpy as np
import pyarrow.parquet as pq

root, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for path in sorted(glob.glob(f"{root}/data/chunk-*/file-*.parquet")):
    chunk, fi = int(path.split("chunk-")[1][:3]), int(path.split("file-")[1][:3])
    dst = f"{out}/f_{chunk:03d}_{fi:03d}.npz"
    if os.path.exists(dst):
        continue
    t = pq.read_table(path, columns=["episode_index", "frame_index", "observation.state", "action"])
    ep, fr = t["episode_index"].to_numpy(), t["frame_index"].to_numpy()
    S = np.stack(t["observation.state"].to_numpy(zero_copy_only=False))
    A = np.stack(t["action"].to_numpy(zero_copy_only=False))
    keep = fr % 3 == 0
    np.savez_compressed(dst, ep=ep[keep].astype(np.int32), fr=fr[keep].astype(np.int32),
                        lw=S[keep, 24:26].mean(1).astype(np.float16), rw=S[keep, 49:51].mean(1).astype(np.float16),
                        la=A[keep, 14].astype(np.float16), ra=A[keep, 22].astype(np.float16))
    print(dst, flush=True)
