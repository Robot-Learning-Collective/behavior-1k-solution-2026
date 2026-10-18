"""Build assets/semantic_stages/gripper_close_allowed.json (the eval auto-open rule's per-stage allow list) from the 10 Hz gripper scan of all 20k demos + that scheme's per-frame stage labels.

Same definitions as the v2 table (2026-09-13): a demo "closes" a gripper in a stage when the gripper is FULLY closed
(state width < -0.98 normalised = the two finger joints sum below 1 mm) for >= 0.5 s inside the stage, frames past the
task-completion frame excluded. Per (task, stage, side): never = no demo closes; noise = <= 3 % of demos and every close
< 3 s; borderline = 3-15 % of demos (decision inherited from the previous scheme's reviewed table when a reviewed
borderline stage maps into the new stage by frame overlap, else open-back); allowed = > 15 % of demos.

Scan format (scripts in the 2026-09-16 gripper study; one npz per dataset parquet file, every 3rd frame):
  ep, fr int32; lw, rw float16 = mean of the two finger joint positions (m); la, ra = gripper commands.

  GRIPPER_SCAN_DIR=<dir with f_*.npz> uv run --no-sync python scripts/semantic_stages/build_close_allowed.py \
      --stage-dir outputs/semantic_stages/v3 --out assets/semantic_stages/gripper_close_allowed.json
"""
import argparse, collections, csv, datetime, glob, json, os

import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--stage-dir", default="outputs/semantic_stages/v3", help="tasks.csv, stage_defs.json, episode_stage_frames.csv")
ap.add_argument("--scan-dir", default=os.environ.get("GRIPPER_SCAN_DIR", ""))
ap.add_argument("--prev", default="", help="previous scheme's gripper_close_allowed.json (reviewed borderline decisions)")
ap.add_argument("--overlap", default="", help="v2_to_v3_overlap.json (maps the previous scheme's stages onto the new ones)")
ap.add_argument("--out", default="")
a = ap.parse_args()
A = a.stage_dir; out = a.out or "assets/semantic_stages/gripper_close_allowed.json"
CLOSED_W = 0.0005   # mean finger position (m): 2*sum/0.1 - 1 < -0.98  <=>  sum < 0.001
HZ = 10.0
names = {int(r["task"]): r["name"] for r in csv.DictReader(open(f"{A}/tasks.csv"))}
NST = {int(r["task"]): int(r["n_stages"]) for r in csv.DictReader(open(f"{A}/tasks.csv"))}
defs = json.load(open(f"{A}/stage_defs.json"))
runs = collections.defaultdict(list)
for r in csv.DictReader(open(f"{A}/episode_stage_frames.csv")):
    runs[int(r["episode_index"])].append((int(r["start"]), int(r["end"]), int(r["stage"])))
RUNS = {e: (np.array([x[0] for x in sorted(v)]), np.array([x[2] for x in sorted(v)]), max(x[1] for x in v)) for e, v in runs.items()}

# per (task, stage, side): list over episodes of (closed_s, max_run_s)
stat = collections.defaultdict(list)
files = sorted(glob.glob(f"{a.scan_dir}/f_*.npz")); assert files, f"no scan files in {a.scan_dir!r}"
for fi, f in enumerate(files):
    z = np.load(f); ep, fr = z["ep"], z["fr"]; lw, rw = z["lw"].astype(np.float32), z["rw"].astype(np.float32)
    for e in np.unique(ep):
        if int(e) not in RUNS: continue
        starts, stages, end = RUNS[int(e)]; m = ep == e; fe = fr[m]; keep = fe < end
        o = np.argsort(fe[keep]); fe = fe[keep][o]; l = (lw[m][keep][o] < CLOSED_W); r = (rw[m][keep][o] < CLOSED_W)
        sg = stages[np.maximum(np.searchsorted(starts, fe, side="right") - 1, 0)]
        for s in range(NST[int(e) // 200]):
            ms = sg == s
            for side, c in (("left", l[ms]), ("right", r[ms])):
                n = int(c.sum()); mx = 0
                if n:
                    d = np.diff(np.concatenate([[0], c.astype(int), [0]])); mx = int((np.where(d == -1)[0] - np.where(d == 1)[0]).max())
                stat[(int(e) // 200, s, side)].append((n / HZ, mx / HZ))
    if fi % 20 == 0: print(f"{fi}/{len(files)}", flush=True)

prev_allow, prev_border = {}, []
if a.prev:
    P = json.load(open(a.prev)); prev_allow = {int(t): {s: set(v) for s, v in d.items()} for t, d in P["allow"].items()}
    prev_border = [b for b in P.get("borderline", []) if b["decision"] == "allow"]
OV = json.load(open(a.overlap)) if a.overlap else None
def mapped_from_prev(t, j, side):
    """previous-scheme stages (task t) whose frames overlap new stage j (weight > 0.2)"""
    if OV is None: return set()
    W = np.asarray(OV[str(t)]["W"]); return {i for i in range(W.shape[1]) if W[j, i] > 0.2}

allow = collections.defaultdict(lambda: collections.defaultdict(list)); border, noise, table = [], [], []
for (t, s, side), v in sorted(stat.items()):
    n = len(v); closed = [x for x in v if x[0] >= 0.5]; frac = len(closed) / n
    cmax = max((x[0] for x in v), default=0.0); cmed = float(np.median([x[0] for x in closed])) if closed else 0.0
    if not closed: cls = "never"
    elif frac <= 0.03 and cmax <= 3.0: cls = "noise"
    elif frac <= 0.15: cls = "borderline"
    else: cls = "allowed"
    row = dict(task=t, name=names[t], side=side, stage=s, demos=f"{len(closed)}/{n}", frac=round(frac, 3), closed_s_med=round(cmed, 1), closed_s_max=round(cmax, 1),
               stage_name=defs[str(t)][s]["name"][:70], **{"class": cls})
    table.append(row)
    if cls == "allowed": allow[t][side].append(s)
    elif cls == "borderline":
        # inherit a reviewed "allow" of the previous scheme when one of its allowed / reviewed stages maps into this stage
        prev_ok = {b["stage"] for b in prev_border if b["task"] == t and b["side"] == side} | prev_allow.get(t, {}).get(side, set())
        dec = "allow" if (mapped_from_prev(t, s, side) & prev_ok) else "open-back"
        row["decision"] = dec; border.append(row)
        if dec == "allow": allow[t][side].append(s)
    elif cls == "noise": noise.append(row)
doc = {
    "_doc": (f"semantic stages gripper rule (10 Hz scan of all 20k demos, built {datetime.date.today()}): per task and gripper, the stages in which "
             "demos DO fully close that gripper (state width < -0.98 normalised, >= 0.5 s, in > 15% of demos, or a borderline case whose "
             "decision was inherited from the reviewed previous table). At rollout a gripper found fully closed in any OTHER stage is opened "
             "immediately (it closed on air). 'borderline' = 3-15% of demos with the decision taken; 'noise' = <= 3% of demos and < 3 s, "
             "treated as never. Built by scripts/semantic_stages/build_close_allowed.py."),
    "allow": {str(t): {side: sorted(st) for side, st in sorted(d.items())} for t, d in sorted(allow.items())},
    "borderline": border, "noise": noise,
}
json.dump(doc, open(out, "w"), indent=1)
n_allow = sum(len(st) for d in allow.values() for st in d.values())
print(f"{out}: {len(allow)} tasks allow a full close somewhere ({n_allow} task/side/stage entries); borderline {len(border)} "
      f"({sum(b['decision'] == 'allow' for b in border)} allow), noise {len(noise)}")
for b in border: print(f"  borderline task {b['task']:3d} {b['name'][:28]:28s} {b['side']:5s} stage {b['stage']} {b['demos']:>8s} med {b['closed_s_med']}s max {b['closed_s_max']}s -> {b['decision']:9s} | {b['stage_name']}")
