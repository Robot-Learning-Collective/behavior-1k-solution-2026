"""Semantic subtask (skill annotation) vs time-based System-2 stage analysis, all 100 tasks.
Episodes are truncated at the completion frame (first frame of the trailing terminated run), as in training.
"""
import glob, json, os, re, sys, collections, itertools
import numpy as np, pandas as pd
# time-based stage counts of the 2025 solution (tasks 0-49) and the same rule for tasks 50-99 (comparison only)
NST = (
    5, 6, 15, 15, 14, 12, 9, 15, 10, 15, 7, 13, 10, 15, 15, 15, 15, 11, 13, 12, 14, 15, 9, 15, 15,
    15, 15, 15, 15, 15, 11, 10, 10, 13, 5, 5, 14, 6, 8, 10, 5, 15, 8, 15, 12, 11, 9, 14, 15, 15,
    11, 8, 10, 11, 15, 9, 5, 5, 15, 8, 5, 11, 7, 5, 15, 13, 11, 8, 14, 5, 12, 15, 11, 14, 12,
    15, 8, 5, 5, 12, 10, 10, 11, 6, 15, 11, 8, 11, 15, 5, 5, 11, 5, 5, 15, 15, 5, 12, 15, 7,
)
ROOT = os.environ.get("B1K_DEMOS_ROOT", "data/2026-challenge-demos")  # needs meta/ + annotations/ for all 100 tasks
OUT = os.environ.get("STAGE_OUT", "outputs/semantic_stages/v2")
FPS = 30.0
VOTE_WIN_S = 2.0  # stage_vote_window_steps=60 env steps

meta = pd.concat([pd.read_parquet(f) for f in sorted(glob.glob(f"{ROOT}/meta/episodes/*/*.parquet"))])
meta = meta.set_index("episode_index")
tasks = pd.read_parquet(f"{ROOT}/meta/tasks.parquet").reset_index().set_index("task_index")["task"].to_dict()
term = pd.read_csv(f"{OUT}/termination.csv").set_index("episode_index") if os.path.exists(f"{OUT}/termination.csv") else None

def flat(x):
    if isinstance(x, (list, tuple)):
        for y in x: yield from flat(y)
    else: yield x

def obj_cat(o):  # "coffee_table_koagbh_0" -> "coffee_table"; "radio_89" -> "radio"
    o = re.sub(r"_\d+$", "", o); o = re.sub(r"_[a-z]{6}$", "", o); return o

try:
    from rapidfuzz.distance import Levenshtein as _L
except ImportError:  # not in the project env: set PYTHONPATH to a dir holding rapidfuzz
    class _L:  # only lev()/align_to_canonical() need it; design_stages_v3.py imports this module without them
        @staticmethod
        def distance(*a): raise SystemExit("rapidfuzz missing: PYTHONPATH=<dir with rapidfuzz> or uv pip install rapidfuzz")
        opcodes = distance
_VOC = {}
def _enc(seq): return "".join(chr(0x100 + _VOC.setdefault(t, len(_VOC))) for t in seq)
def lev(a, b): return _L.distance(_enc(a), _enc(b))

def align_to_canonical(seq, canon):
    """Map each element of seq to an index in canon via Levenshtein alignment.
    Inserted (extra) elements inherit the index of the last matched canonical element (>=0)."""
    ops = _L.opcodes(_enc(seq), _enc(canon))
    idx = [-1] * len(seq)
    for tag, i0, i1, j0, j1 in ops:
        if tag in ("equal", "replace"):
            for k in range(i1 - i0): idx[i0 + k] = j0 + min(k, j1 - j0 - 1)
    last = 0
    for i in range(len(idx)):
        if idx[i] < 0: idx[i] = last
        else: last = idx[i]
    return idx

def canonical_alignment_stats(eps, canon, nst, key="g2", use_effective=True):
    """Time-stage <-> canonical semantic-stage cross-tabulation (frame weighted)."""
    K = len(canon); M = np.zeros((nst, K))
    spread = []  # per-episode: how many time stages does a canonical stage span
    for e in eps:
        seq = [s[key] for s in e["segs"]]
        idx = align_to_canonical(seq, canon)
        Lref = e["comp"] if use_effective else e["L"]
        for s, ci in zip(e["segs"], idx):
            for f0 in range(s["s0"], s["s1"], 5):  # subsample frames
                k = min(int(f0 / (Lref / nst)), nst - 1); M[k, ci] += 5
    tot = M.sum()
    # purity of time stage wrt canonical stage; purity of canonical stage wrt time stage
    ts_pur = (M.max(1).sum() / tot) if tot else np.nan
    cs_pur = (M.max(0).sum() / tot) if tot else np.nan
    # mutual information normalized
    P = M / tot; pi = P.sum(1, keepdims=True); pj = P.sum(0, keepdims=True)
    nz = P > 0; mi = (P[nz] * np.log(P[nz] / (pi @ pj)[nz])).sum()
    hi = -(pi[pi > 0] * np.log(pi[pi > 0])).sum(); hj = -(pj[pj > 0] * np.log(pj[pj > 0])).sum()
    nmi = mi / max(np.sqrt(hi * hj), 1e-9)
    return dict(ts_purity=float(ts_pur), cs_purity=float(cs_pur), nmi=float(nmi), M=M)

def load_task(ti):
    d = f"{ROOT}/annotations/task-{ti:04d}"
    fs = sorted(glob.glob(f"{d}/episode_*.json"))
    eps = []
    for f in fs:
        a = json.load(open(f))
        raw = int(re.search(r"episode_(\d+)\.json", f).group(1))
        m = meta[(meta.task_index == ti) & (meta.raw_episode_id == raw)]
        if len(m) != 1: continue
        ep = int(m.index[0]); L = int(m.length.iloc[0])
        comp = int(term.loc[ep, "completion_frame"]) if term is not None and ep in term.index else L
        blips = int(term.loc[ep, "blips"]) if term is not None and ep in term.index else 0
        segs = []
        def ranges(fd):
            v = list(flat(fd)); v = [int(x) for x in v]
            if len(v) % 2: v = [min(v), max(v)]
            return sorted((v[i], v[i + 1]) for i in range(0, len(v), 2))
        for s in a["skill_annotation"]:
          for s0, s1 in ranges(s["frame_duration"]):
            if s0 >= comp: continue
            s1 = min(s1, comp)
            desc = "+".join(s["skill_description"]); objs = list(flat(s["object_id"]))
            segs.append(dict(desc=desc, g2=desc + "(" + ",".join(dict.fromkeys(obj_cat(o) for o in objs)) + ")",
                             g3=desc + "(" + ",".join(objs) + ")", s0=s0, s1=s1, type="+".join(str(x) for x in s["skill_type"])))
        prims = []
        for p in a["primitive_annotation"]:
          for s0, s1 in ranges(p["frame_duration"]):
            if s0 >= comp: continue
            objs = list(flat(p["object_id"]))
            prims.append(dict(g2="+".join(p["primitive_description"]) + "(" + ",".join(dict.fromkeys(obj_cat(o) for o in objs)) + ")", s0=s0, s1=min(s1, comp)))
        eps.append(dict(ep=ep, L=L, comp=comp, blips=blips, segs=segs, prims=prims,
                        ann_end=max(r[1] for s in a["skill_annotation"] for r in ranges(s["frame_duration"])), n_after=sum(r[0] >= comp for s in a["skill_annotation"] for r in ranges(s["frame_duration"]))))
        eps[-1]["segs"].sort(key=lambda s: s["s0"]); eps[-1]["prims"].sort(key=lambda s: s["s0"])
    return eps

def seq_stats(seqs):
    """Consistency of a list of token sequences."""
    cnt = collections.Counter(tuple(s) for s in seqs)
    mode, mode_n = cnt.most_common(1)[0]
    uniq = list(cnt)
    # medoid among unique sequences (weighted)
    best, bestd = None, 1e18
    for u in uniq:
        d = sum(c * lev(u, v) for v, c in cnt.items())
        if d < bestd: best, bestd = u, d
    dists = np.array([lev(best, s) for s in seqs], float)
    ndist = dists / np.maximum(len(best), [len(s) for s in seqs])
    ms = [collections.Counter(s) == collections.Counter(best) and tuple(s) != best for s in seqs]
    lens = np.array([len(s) for s in seqs])
    return dict(n_unique=len(uniq), mode_share=mode_n / len(seqs), exact_medoid_share=float(np.mean(dists == 0)),
                within1_share=float(np.mean(dists <= 1)), within10pct_share=float(np.mean(ndist <= 0.1)),
                mean_edit=float(dists.mean()), mean_nedit=float(ndist.mean()), p90_nedit=float(np.percentile(ndist, 90)),
                pure_reorder_share=float(np.mean(ms)), longer_share=float(np.mean(lens > len(best))), shorter_share=float(np.mean(lens < len(best))),
                medoid=best, medoid_len=len(best))

def time_stage_alignment(eps, nst, key="g2", use_effective=False):
    """Purity/consistency of time stages vs semantic labels."""
    per_stage_labels = [collections.Counter() for _ in range(nst)]  # weighted by frames
    misaligned_frames = 0; total_frames = 0
    bdist = []  # semantic boundary -> nearest time border (s)
    tdist = []  # time border -> nearest semantic boundary (s)
    ep_purity = []
    for e in eps:
        Lref = e["comp"] if use_effective else e["L"]
        borders = np.array([k * Lref / nst for k in range(1, nst)])
        borders_in = borders[borders < e["comp"]]
        sb = np.array([s["s0"] for s in e["segs"][1:]])  # internal semantic boundaries
        if len(sb) and len(borders_in):
            bdist += list(np.min(np.abs(sb[:, None] - borders_in[None, :]), 1) / FPS)
            tdist += list(np.min(np.abs(borders_in[:, None] - sb[None, :]), 1) / FPS)
        lab = np.full(e["comp"], -1); labels = []
        for i, s in enumerate(e["segs"]): lab[s["s0"]:s["s1"]] = i; labels.append(s[key])
        pur = []
        for k in range(nst):
            a, b = int(k * Lref / nst), int(min((k + 1) * Lref / nst, e["comp"]))
            if b <= a: continue
            seg = lab[a:b]; seg = seg[seg >= 0]
            if len(seg) == 0: continue
            c = collections.Counter(labels[i] for i in seg)
            for l, n in c.items(): per_stage_labels[k][l] += n
            pur.append(c.most_common(1)[0][1] / len(seg))
        ep_purity.append(np.mean(pur) if pur else np.nan)
    # cross-episode consistency: for each stage, share of frames carrying that stage's majority label
    cons = []; 
    for k in range(nst):
        c = per_stage_labels[k]; tot = sum(c.values())
        if tot == 0: continue
        top = c.most_common(1)[0][1]; cons.append(top / tot); misaligned_frames += tot - top; total_frames += tot
    return dict(stage_consistency=float(np.mean(cons)), misaligned_frac=misaligned_frames / max(total_frames, 1),
                within_ep_purity=float(np.nanmean(ep_purity)),
                sem_to_time_border_med_s=float(np.median(bdist)) if bdist else np.nan,
                time_to_sem_border_med_s=float(np.median(tdist)) if tdist else np.nan,
                stage_majority=[per_stage_labels[k].most_common(1)[0][0] if per_stage_labels[k] else None for k in range(nst)])

def boundary_position_spread(eps, medoid, key="g2"):
    """Among episodes exactly matching the medoid sequence: std of normalized boundary positions."""
    pos = []
    for e in eps:
        if tuple(s[key] for s in e["segs"]) != medoid: continue
        pos.append([s["s0"] / e["comp"] for s in e["segs"][1:]])
    if len(pos) < 3: return np.nan, np.nan
    pos = np.array(pos); return float(pos.std(0).mean()), float(pos.std(0).max())

rows = []; details = {}
ONLY = [int(x) for x in os.environ.get("ONLY", "").split(",") if x]
for ti in sorted(tasks):
    if ONLY and ti not in ONLY: continue
    if len(glob.glob(f"{ROOT}/annotations/task-{ti:04d}/*.json")) < 200: continue
    eps = load_task(ti)
    if not eps: continue
    nst = NST[ti]
    L = np.array([e["L"] for e in eps]) / FPS; C = np.array([e["comp"] for e in eps]) / FPS
    segdur = np.array([(s["s1"] - s["s0"]) / FPS for e in eps for s in e["segs"]])
    r = dict(task=ti, name=tasks[ti], n_ep=len(eps), nst=nst,
             len_full_mean_s=L.mean(), len_eff_mean_s=C.mean(), len_eff_std_s=C.std(), len_eff_cv=C.std() / C.mean(),
             len_eff_min_s=C.min(), len_eff_p10_s=np.percentile(C, 10), len_eff_med_s=np.median(C), len_eff_p90_s=np.percentile(C, 90), len_eff_max_s=C.max(),
             tail_cut_frac=1 - C.sum() / L.sum(), skills_after_comp_mean=np.mean([e["n_after"] for e in eps]),
             blip_eps_frac=np.mean([e["blips"] > 0 for e in eps]),
             n_skills_mean=np.mean([len(e["segs"]) for e in eps]), n_skills_std=np.std([len(e["segs"]) for e in eps]),
             n_skills_min=min(len(e["segs"]) for e in eps), n_skills_max=max(len(e["segs"]) for e in eps),
             n_prims_mean=np.mean([len(e["prims"]) for e in eps]),
             seg_dur_med_s=np.median(segdur), seg_dur_p10_s=np.percentile(segdur, 10), seg_short2s_frac=np.mean(segdur < VOTE_WIN_S),
             seg_short5s_frac=np.mean(segdur < 5), stage_len_s=C.mean() / nst)
    for key in ("desc", "g2", "g3"):
        st = seq_stats([[s[key] for s in e["segs"]] for e in eps])
        for k, v in st.items():
            if k != "medoid": r[f"{key}_{k}"] = v
        details.setdefault(ti, {})[f"medoid_{key}"] = st["medoid"]
    st = seq_stats([[p["g2"] for p in e["prims"]] for e in eps])
    for k, v in st.items():
        if k != "medoid": r[f"prim_{k}"] = v
    details[ti]["medoid_prim"] = st["medoid"]
    al = time_stage_alignment(eps, nst, "g2", False)
    for k, v in al.items():
        if k != "stage_majority": r[f"al_{k}"] = v
    details[ti]["stage_majority_g2"] = al["stage_majority"]
    al2 = time_stage_alignment(eps, nst, "g2", True)
    r["al_eff_stage_consistency"] = al2["stage_consistency"]; r["al_eff_misaligned_frac"] = al2["misaligned_frac"]
    # with a semantic-count number of stages, computed on effective length
    al3 = time_stage_alignment(eps, max(2, int(round(r["n_skills_mean"]))), "g2", True)
    r["al_nsem_stage_consistency"] = al3["stage_consistency"]
    r["bpos_std_mean"], r["bpos_std_max"] = boundary_position_spread(eps, details[ti]["medoid_g2"])
    ca = canonical_alignment_stats(eps, details[ti]["medoid_g2"], nst, "g2", True)
    r["ca_time_purity"], r["ca_sem_purity"], r["ca_nmi"] = ca["ts_purity"], ca["cs_purity"], ca["nmi"]
    ca_full = canonical_alignment_stats(eps, details[ti]["medoid_g2"], nst, "g2", False)
    r["ca_time_purity_fullL"], r["ca_nmi_fullL"] = ca_full["ts_purity"], ca_full["nmi"]
    cap = canonical_alignment_stats(eps, details[ti]["medoid_prim"], nst, "g2", True) if False else None
    details[ti]["crosstab_time_x_sem"] = np.round(ca["M"] / ca["M"].sum(1, keepdims=True).clip(1), 2).tolist()
    # per-canonical-stage normalized position stats (all episodes, via alignment)
    pos = collections.defaultdict(list)
    for e in eps:
        idx = align_to_canonical([s["g2"] for s in e["segs"]], details[ti]["medoid_g2"])
        for s, ci in zip(e["segs"], idx): pos[ci].append(((s["s0"] + s["s1"]) / 2) / e["comp"])
    details[ti]["canon_stage_mid_pos_mean_std"] = [[float(np.mean(pos[c])), float(np.std(pos[c]))] if pos[c] else None for c in range(len(details[ti]["medoid_g2"]))]
    r["canon_pos_std_mean"] = float(np.mean([np.std(pos[c]) for c in pos if len(pos[c]) > 2]))
    rows.append(r); print(ti, tasks[ti], f"eff {C.mean():.0f}s nst {nst} skills {r['n_skills_mean']:.1f} mode {r['g2_mode_share']:.2f} nedit {r['g2_mean_nedit']:.2f} cons {r['al_stage_consistency']:.2f}", flush=True)
SUF = "_test" if ONLY else ""
df = pd.DataFrame(rows); df.to_csv(f"{OUT}/per_task{SUF}.csv", index=False)
json.dump({str(k): v for k, v in details.items()}, open(f"{OUT}/details{SUF}.json", "w"), indent=1)
print("saved", len(df))
