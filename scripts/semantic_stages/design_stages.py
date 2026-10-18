"""Design ordered semantic stages per task (research). See REPORT_v2.md for the rules."""
import sys, os, json, collections, re
os.environ["ONLY"] = "999"
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "analyze.py")).read().split("rows = []; details = {}")[0]
exec(src)
import numpy as np, pandas as pd
det = json.load(open(f"{OUT}/details.json"))
per = pd.read_csv(f"{OUT}/per_task.csv").set_index("task")
LONGEST = set(per.len_eff_mean_s.sort_values(ascending=False).index[:20])
CUT_OK0 = 0.55
CUT_OK = 0.70      # share of episodes with <=1 misplaced token for a cut to count as ordered
TARGET_MIN, TARGET_MAX, SHORT = 30.0, 60.0, 15.0   # user 2026-09-12: no stage under 15 s on average
MIN_STAGE_S = 15.0
MERGE_REPEATS = os.environ.get("MERGE_REPEATS", "1") == "1"  # consecutive identical stages -> one stage (x n)

def skill_kind(t): return t.split("(")[0]
def skill_obj(t): 
    m = re.match(r".+?\((.*)\)", t); return m.group(1).split(",")[0] if m and m.group(1) else ""

def cut_split(seq, A, B):
    """Best split index s for episode token list `seq` given the medoid prefix A (before cut) and suffix B.
    cost(s) = missing A-tokens in prefix + excess prefix tokens whose label also occurs in B (i.e. later work done early).
    Retries of labels exclusive to A are free. Ties -> s closest to len(A). Returns (s, cost)."""
    cA = collections.Counter(A); inB = set(B); k = len(A)
    labels = set(cA) | set(seq); lab_idx = {l: i for i, l in enumerate(labels)}
    n = len(seq); before = np.zeros(len(labels), int); costs = np.empty(n + 1, int)
    def cost():
        c = 0
        for l, i in lab_idx.items():
            a = cA.get(l, 0); b = before[i]
            if b < a: c += a - b
            elif b > a and l in inB: c += b - a
        return c
    costs[0] = cost()
    for s in range(1, n + 1):
        before[lab_idx[seq[s - 1]]] += 1; costs[s] = cost()
    best = costs.min(); cands = np.where(costs == best)[0]
    s = int(cands[np.argmin(np.abs(cands - k))]); return s, int(best)

PROGRESS = os.environ.get("PROGRESS", "units")
_EV = None
def milestones(ep, comp):
    """Frames where the net satisfied-goal-predicate count reaches k for good (never drops below k before completion)."""
    global _EV
    if _EV is None:
        ev = pd.read_parquet(f"{OUT}/predicate_events.parquet"); _EV = {k: g[["frame", "delta"]].to_numpy() for k, g in ev.groupby("episode_index")}
    e = _EV.get(ep)
    if e is None: return []
    e = e[e[:, 0] < comp]; e = e[np.argsort(e[:, 0])]
    if len(e) == 0: return []
    unit = np.abs(e[:, 1]).min(); cnt = np.round(np.cumsum(e[:, 1]) / unit).astype(int)
    out = []; final = cnt[-1] if len(cnt) else 0
    for k in range(1, final + 1):
        idx = [i for i in range(len(cnt)) if cnt[i] >= k and (cnt[i:] >= k).all()]
        if idx: out.append(int(e[idx[0], 0]))
    return out

CLASS_CONTIG = 0.80
# progress-part overrides per (task, region block): keeps the stage COUNT of the previous spec for the tasks whose
# minority-order class stages were replaced by progress stages (user 2026-09-13), so trained checkpoints keep
# their table layout; the parts are also closer to the 30-60 s target than the 5-part cap allowed.
PROGRESS_M_OVERRIDE = {(2, 0, 27): 10, (10, 6, 19): 4, (21, 18, 28): 4, (24, 3, 36): 12}
CLASS_DOM_MIN = 0.70   # user 2026-09-13: class stages only when the dominant class order covers >= 70% of demos;
                       # otherwise the region gets ordered PROGRESS stages (completed sub-tasks), never minority-order class labels
MANIP = ("pick up", "place", "pour", "insert", "hang", "push to", "chop", "tip over", "hand over", "attach")
def _objs(t): return [x for x in t[len(skill_kind(t)) + 1:-1].split(",") if x]
def class_info(eps, reg, splits, a, b):
    """Sub-goal classes = manipulated object categories of the region's canonical skills.
    Returns classes (list), per-episode per-segment class index (or None), contiguity share, dominant order, its share."""
    manip = [_objs(t)[0] for t in reg if skill_kind(t).startswith(MANIP) and _objs(t)]
    classes = list(dict.fromkeys(manip)); cid = {c: i for i, c in enumerate(classes)}
    if len(classes) < 2: return classes, None, 0.0, (), 0.0
    seglab = []; contig = []; orders = []
    for ei, e in enumerate(eps):
        i0, i1 = splits[ei, a], splits[ei, b]
        lab = [None] * len(e["segs"])
        for i in range(i0, i1):
            t = e["segs"][i]["g2"]; o = _objs(t)
            if o and skill_kind(t).startswith(MANIP) and o[0] in cid: lab[i] = cid[o[0]]
        nxt = None
        for i in range(i1 - 1, i0 - 1, -1):  # move-to / open-door etc. inherit the next class
            if lab[i] is not None: nxt = lab[i]
            elif nxt is not None: lab[i] = nxt
        prv = None
        for i in range(i0, i1):  # trailing unlabeled -> previous class
            if lab[i] is not None: prv = lab[i]
            elif prv is not None: lab[i] = prv
        seq = [k for k in lab[i0:i1] if k is not None]
        runs = [k for i, k in enumerate(seq) if i == 0 or seq[i - 1] != k]
        contig.append(len(runs) == len(set(runs))); orders.append(tuple(dict.fromkeys(runs))); seglab.append(lab)
    oc = collections.Counter(orders); top = oc.most_common(1)[0]
    return classes, seglab, float(np.mean(contig)), top[0], top[1] / len(orders)

def design(ti, verbose=False, m_cap=None):
    m_cap = m_cap or {}
    eps = load_task(ti); med = det[str(ti)]["medoid_g2"]; K = len(med)
    class_regions = {}
    if PROGRESS == "predicate":
        for e in eps: e["ms"] = milestones(e["ep"], e["comp"])
    def region_units(e, i0, i1, f0, f1):
        if PROGRESS == "predicate":
            ms = [f for f in e["ms"] if f0 < f < f1]
            if ms: return [dict(s1=f) for f in ms]
        return [sg for sg in e["segs"][i0:i1] if skill_kind(sg["g2"]) != "move to"]
    seqs = [[s["g2"] for s in e["segs"]] for e in eps]
    # 1) cut consistency + per-episode split positions (monotone)
    cut_ok = []; splits = np.zeros((len(eps), K + 1), int); splits[:, K] = [len(s) for s in seqs]
    for k in range(1, K):
        A, B = med[:k], med[k:]; ok0 = ok1 = 0
        for ei, seq in enumerate(seqs):
            s, mis = cut_split(seq, A, B); s = max(s, splits[ei, k - 1]); splits[ei, k] = s; ok1 += mis <= 1; ok0 += mis == 0
        cut_ok.append(ok1 / len(eps) >= CUT_OK and ok0 / len(eps) >= CUT_OK0)
    # 2) blocks = maximal runs between consistent cuts
    blocks = []; start = 0
    for k in range(1, K):
        if cut_ok[k - 1]: blocks.append((start, k)); start = k
    blocks.append((start, K))
    # per-episode block frame ranges
    def block_frames(ei, a, b):
        segs = eps[ei]["segs"]; i0, i1 = splits[ei, a], splits[ei, b]
        if i1 <= i0: return None
        return segs[i0]["s0"], segs[i1 - 1]["s1"], i0, i1
    # 3) atoms: ordered block -> 1 atom; unordered block (len>1) -> m progress atoms by completed non-nav units
    atoms = []  # dict(name, kind, block, sub=(j,m), dur list)
    thresholds = {}  # block -> list of unit-fraction thresholds p_1..p_{m-1}
    for (a, b) in blocks:
        durs = [];
        for ei in range(len(eps)):
            bf = block_frames(ei, a, b); durs.append((bf[1] - bf[0]) / FPS if bf else 0.0)
        mean = float(np.mean(durs))
        if b - a == 1:
            atoms.append(dict(name=med[a], kind="ordered", block=(a, b), sub=(0, 1), mean=mean))
            continue
        if mean <= 65:  # short unordered group -> one stage, fine as is
            atoms.append(dict(name=f"unordered group[{a}:{b}] ({b-a} skills, one stage)", kind="unordered", block=(a, b), sub=(0, 1), mean=mean, region_m=1)); continue
        classes, seglab, contig, dom_order, dom_share = class_info(eps, med[a:b], splits, a, b)
        cdur = {}
        if seglab is not None:
            cdur = {c: [] for c in range(len(classes))}
            for ei, e in enumerate(eps):
                for c in cdur: cdur[c].append(sum((sg["s1"] - sg["s0"]) for sg, l in zip(e["segs"], seglab[ei]) if l == c) / FPS)
        if seglab is not None and contig >= CLASS_CONTIG and dom_share >= CLASS_DOM_MIN and len(dom_order) == len(classes) and mean >= 30 and min(np.mean(v) for v in cdur.values()) >= 12:
            # sub-goal class stages in dominant order; each class -> 1..5 progress parts by completed units of that class
            class_regions[(a, b)] = dict(classes=classes, seglab=seglab, contig=contig, dom_order=[classes[c] for c in dom_order], dom_share=dom_share, th={})
            for c in dom_order:
                mc = float(np.mean(cdur[c])); m = int(np.clip(round(mc / 45.0), 1, 5)) if mc >= 15 else 1
                m = min(m, m_cap.get((a, b, c), 5))
                if m > 1:  # corpus-balanced unit-fraction thresholds so the parts are even in time
                    P, T = [], []
                    for ei, e in enumerate(eps):
                        segs = [sg for sg, l in zip(e["segs"], seglab[ei]) if l == c]
                        units = [sg for sg in segs if skill_kind(sg["g2"]) != "move to"] or segs
                        if not segs: continue
                        f0, f1 = segs[0]["s0"], segs[-1]["s1"]
                        for ui, sg in enumerate(units): P.append((ui + 1) / len(units)); T.append((sg["s1"] - f0) / max(f1 - f0, 1))
                    P, T = np.array(P), np.array(T); grid = np.linspace(0, 1, 101)
                    tp = np.array([T[np.abs(P - g) <= 0.06].mean() if (np.abs(P - g) <= 0.06).any() else np.nan for g in grid])
                    tp = pd.Series(tp).interpolate(limit_direction="both").to_numpy(); tp = np.maximum.accumulate(tp); tp[0] = 0.0; tp[-1] = 1.0
                    class_regions[(a, b)]["th"][c] = [float(np.interp(j / m, tp, grid)) for j in range(1, m)]
                for j in range(m):
                    atoms.append(dict(name=f"class {classes[c]}" + (f" part {j+1}/{m}" if m > 1 else ""), kind="class", block=(a, b), cls=c, sub=(j, m), mean=mc / m, dom=dom_share))
            continue
        if True:
            m = int(np.clip(round(mean / 45.0), 1, 5)) if mean >= 15 else 1
            m = PROGRESS_M_OVERRIDE.get((ti, a, b), m); protected = (ti, a, b) in PROGRESS_M_OVERRIDE
            # progress axis = completed non-nav units. Thresholds in unit-fraction space chosen so mean stage durations balance.
            P, T = [], []
            for ei, e in enumerate(eps):
                bf = block_frames(ei, a, b)
                if not bf or bf[1] <= bf[0]: continue
                f0, f1, i0, i1 = bf; units = region_units(e, i0, i1, f0, f1)
                for ui, sg in enumerate(units): P.append((ui + 1) / len(units)); T.append((sg["s1"] - f0) / (f1 - f0))
            th = []
            if m > 1 and P:
                P, T = np.array(P), np.array(T); grid = np.linspace(0, 1, 101)
                tp = np.array([np.interp(g, np.sort(P), T[np.argsort(P)]) for g in grid])  # crude monotone-ish curve
                # smooth by binning
                tp = np.array([T[np.abs(P - g) <= 0.06].mean() if (np.abs(P - g) <= 0.06).any() else np.nan for g in grid])
                tp = pd.Series(tp).interpolate(limit_direction="both").to_numpy(); tp = np.maximum.accumulate(tp); tp[0] = 0.0; tp[-1] = 1.0
                th = [float(np.interp(j / m, tp, grid)) for j in range(1, m)]
            thresholds[(a, b)] = th
            for j in range(m):
                atoms.append(dict(name=f"unordered[{a}:{b}] progress {j+1}/{m}", kind="unordered", block=(a, b), sub=(j, m), mean=mean / m, region_m=m, protected=protected))
    # 4) merging. A stage = list of consecutive atoms. Duration = sum of means (atoms are contiguous in time).
    stages = [[x] for x in atoms]
    def dur(st): return sum(x["mean"] for x in st)
    def logical_pref(st_prev, st, st_next):
        """which neighbour to merge into: 'prev' or 'next'."""
        first = st[0]; last = st[-1]
        if st_next is not None and skill_kind(first["name"]) == "move to" and first["kind"] == "ordered": return "next"
        if st_prev is not None and last["kind"] == "ordered" and st_prev[-1]["kind"] == "ordered" and skill_obj(last["name"]) == skill_obj(st_prev[-1]["name"]): return "prev"
        if st_next is not None and first["kind"] == "ordered" and st_next[0]["kind"] == "ordered" and skill_obj(first["name"]) == skill_obj(st_next[0]["name"]): return "next"
        if st_prev is None: return "next"
        if st_next is None: return "prev"
        return "prev" if dur(st_prev) <= dur(st_next) else "next"
    def is_class(st): return any(x["kind"] == "class" or x.get("protected") for x in st)   # class parts and count-matched progress parts are never merged
    def merge_at(i, side):
        j = i - 1 if side == "prev" else i + 1
        a, b = min(i, j), max(i, j); stages[a:b + 1] = [stages[a] + stages[b]]
    # pass 1: short atoms (<10 s) -> logically closest neighbour
    changed = True
    while changed and len(stages) > 2:
        changed = False
        for i, st in enumerate(stages):
            if dur(st) < SHORT and not is_class(st):
                side = logical_pref(stages[i - 1] if i > 0 else None, st, stages[i + 1] if i + 1 < len(stages) else None)
                other = "next" if side == "prev" else "prev"
                j = i - 1 if side == "prev" else i + 1; jo = i - 1 if other == "prev" else i + 1
                if 0 <= jo < len(stages) and dur(st) + dur(stages[j]) > TARGET_MAX and dur(st) + dur(stages[jo]) <= TARGET_MAX: side = other
                jj = i - 1 if side == "prev" else i + 1
                if is_class(stages[jj]):
                    side = other; jj = jo
                    if not (0 <= jj < len(stages)) or is_class(stages[jj]): continue
                merge_at(i, side); changed = True; break
    # pass 2: bring stages to >= 30 s where the merge stays <= 60 s (shortest first); keep >= 2 stages
    accepted = set()
    while len(stages) > 2:
        cand = [i for i, st in enumerate(stages) if dur(st) < TARGET_MIN and id(st) not in accepted and not is_class(st)]
        if not cand: break
        i = min(cand, key=lambda i: dur(stages[i]))
        opts = []
        if i > 0 and not is_class(stages[i - 1]): opts.append(("prev", dur(stages[i - 1])))
        if i + 1 < len(stages) and not is_class(stages[i + 1]): opts.append(("next", dur(stages[i + 1])))
        pref = logical_pref(stages[i - 1] if i > 0 else None, stages[i], stages[i + 1] if i + 1 < len(stages) else None)
        opts.sort(key=lambda c: (c[0] != pref, c[1]))
        for side, nd in opts:
            if dur(stages[i]) + nd <= TARGET_MAX: merge_at(i, side); break
        else:
            accepted.add(id(stages[i]))
    # pass 3: cap on count
    cap_n = 25 if ti in LONGEST else 15
    while len(stages) > cap_n:
        sums = [dur(stages[i]) + dur(stages[i + 1]) + (1e6 if is_class(stages[i]) or is_class(stages[i + 1]) else 0) for i in range(len(stages) - 1)]
        i = int(np.argmin(sums)); stages[i:i + 2] = [stages[i] + stages[i + 1]]
    # pass 4 (user 2026-09-12): HARD minimum — any non-class stage under MIN_STAGE_S merges into its
    # logically preferred neighbour whatever the resulting length (keep >= 2 stages)
    changed = True
    while changed and len(stages) > 2:
        changed = False
        for i, st in enumerate(stages):
            if dur(st) < MIN_STAGE_S and not is_class(st):
                side = logical_pref(stages[i - 1] if i > 0 else None, st, stages[i + 1] if i + 1 < len(stages) else None)
                j = i - 1 if side == "prev" else i + 1
                if not (0 <= j < len(stages)) or is_class(stages[j]):
                    side = "next" if side == "prev" else "prev"; j = i - 1 if side == "prev" else i + 1
                    if not (0 <= j < len(stages)) or is_class(stages[j]): continue
                merge_at(i, side); changed = True; break
    # pass 5 (user 2026-09-12): consecutive stages with IDENTICAL skill content (e.g. "fetch a can,
    # drop it in the trash" x3) collapse into one repeated stage — the stage embedding conditions the
    # behaviour and the behaviour is the same; the head cannot tell repeat 2 from repeat 3 anyway.
    def atom_names(st): return tuple(x["name"] for x in st)
    if MERGE_REPEATS:
        i = 0
        while i + 1 < len(stages):
            if not is_class(stages[i]) and not is_class(stages[i + 1]) and atom_names(stages[i]) == atom_names(stages[i + 1]):
                rep_n = stages[i][0].get("_repeat", 1) + 1
                merged = [dict(x) for x in stages[i]]
                for x in merged: x["_repeat"] = rep_n
                merged[0]["_extra_blocks"] = merged[0].get("_extra_blocks", []) + [x["block"] for x in stages[i + 1]]
                merged[0]["mean"] = sum(x["mean"] for x in stages[i]) + sum(x["mean"] for x in stages[i + 1]) - sum(x["mean"] for x in merged[1:])
                stages[i:i + 2] = [merged]
            else:
                i += 1
    # 4b) long ORDERED stages (single skills like a 120 s push/walk) -> time sub-split into ~45 s pieces, snapped to skill ends
    LONG = 75.0 if ti in LONGEST else 65.0
    def stage_mean(st):
        d = []
        for ei in range(len(eps)):
            f = [block_frames(ei, *x["block"]) for x in st]; f = [x for x in f if x]
            d.append((max(x[1] for x in f) - min(x[0] for x in f)) / FPS if f else 0.0)
        return float(np.mean(d))
    final = []  # (stage atoms, j, q)
    for st in stages:
        m_ = stage_mean(st); q = 1
        # user rule (2026-08-29): a long single skill is always ONE stage -> no time split
        for j in range(q): final.append((st, j, q))
    # 5) per-episode frame labels
    labels = []  # (ep, stage, start_frame, end_frame)
    for ei, e in enumerate(eps):
        bounds = []
        for st, j, q in final:
            first = st[0]; a, b = first["block"]; jj, m = first["sub"]
            if first["kind"] == "class": bounds.append(None); continue
            if q > 1:
                # time split of the whole (merged) stage span
                f = [block_frames(ei, *x["block"]) for x in st]; f = [x for x in f if x]
                if not f: bounds.append(None); continue
                f0, f1 = min(x[0] for x in f), max(x[1] for x in f); i0, i1 = min(x[2] for x in f), max(x[3] for x in f)
                target = f0 + (f1 - f0) * j / q; ends = np.array([sg["s1"] for sg in e["segs"][i0:i1] if f0 < sg["s1"] < f1])
                if len(ends):
                    near = ends[np.argmin(np.abs(ends - target))]
                    if abs(near - target) <= 0.25 * (f1 - f0) / q: target = near
                bounds.append(int(target)); continue
            bf = block_frames(ei, a, b)
            if bf is None: bounds.append(None); continue
            f0, f1, i0, i1 = bf
            if m == 1: bounds.append(f0); continue
            # progress parts inside an unordered block are EQUAL TIME slices of that block in every
            # episode (block length / m, like the 2025 time stages but confined to the block; user 2026-09-13)
            bounds.append(int(f0 + (f1 - f0) * jj / m))
        nxt = e["comp"]
        for i in range(len(bounds) - 1, -1, -1):
            if bounds[i] is None: bounds[i] = nxt
            else: nxt = bounds[i]
        bounds[0] = 0
        for i in range(1, len(bounds)): bounds[i] = max(bounds[i], bounds[i - 1])
        frame = np.zeros(max(e["comp"], 1), int)
        for i in range(len(final)):
            s0 = bounds[i]; s1 = bounds[i + 1] if i + 1 < len(final) else e["comp"]; frame[s0:s1] = i
        # class stages: override by the class actually being executed (labels follow the demo's own order)
        for i, (st, j, q) in enumerate(final):
            x = st[0]
            if x["kind"] != "class": continue
            cr = class_regions[x["block"]]; lab = cr["seglab"][ei]; c = x["cls"]; jj, m = x["sub"]
            segs = [sg for sg, l in zip(e["segs"], lab) if l == c]
            if not segs: continue
            units = [sg for sg in segs if skill_kind(sg["g2"]) != "move to"] or segs
            th = [0.0] + cr["th"].get(c, []) + [1.0]
            k0 = int(round(len(units) * th[jj])); k1 = int(round(len(units) * th[jj + 1])); k0 = min(max(k0, 0), len(units)); k1 = min(max(k1, k0), len(units))
            if jj > 0 and k0 == 0: k0 = 1
            if jj < m - 1 and k1 == 0: k1 = 1
            lo = segs[0]["s0"] if jj == 0 else units[k0 - 1]["s1"]; hi = segs[-1]["s1"] if jj == m - 1 else (units[k1 - 1]["s1"] if k1 > 0 else lo)
            for sg in segs:
                f0, f1 = max(sg["s0"], lo), min(sg["s1"], hi)
                if f1 > f0: frame[f0:f1] = i
        # emit runs
        ch = np.concatenate([[0], np.where(np.diff(frame) != 0)[0] + 1, [len(frame)]])
        for r0, r1 in zip(ch[:-1], ch[1:]): labels.append((e["ep"], int(frame[r0]), int(r0), int(r1)))
    stages = [dict(atoms=st, sub=(j, q)) for st, j, q in final]
    lab = pd.DataFrame(labels, columns=["episode_index", "stage", "start", "end"]); lab["dur_s"] = (lab.end - lab.start) / FPS
    lab_ep = lab.groupby(["episode_index", "stage"]).dur_s.sum().reset_index()
    lab_ep = lab_ep.set_index(["episode_index", "stage"]).reindex(pd.MultiIndex.from_product([[e["ep"] for e in eps], range(len(stages))], names=["episode_index", "stage"]), fill_value=0.0).reset_index()
    st_rows = []
    for i, st in enumerate(stages):
        g = lab_ep[lab_ep.stage == i].dur_s; j, q = st["sub"]
        rep_n = st["atoms"][0].get("_repeat", 1)
        nm = " | ".join(x["name"] for x in st["atoms"]) + (f"  x{rep_n}" if rep_n > 1 else "") + (f"  [time part {j+1}/{q}]" if q > 1 else "")
        kind = "+".join(sorted(set(x["kind"] for x in st["atoms"]))) + ("+timesplit" if q > 1 else "")
        x0 = st["atoms"][0]; cr = class_regions.get(x0["block"]) if x0["kind"] == "class" else None
        red = any((x["kind"] == "unordered" and x.get("region_m", 1) > 1) or (x["kind"] == "class" and x["dom"] < 0.7) for x in st["atoms"])
        color = "red" if red else ("green" if any(x["kind"] in ("unordered", "class") for x in st["atoms"]) else "blue")
        st_rows.append(dict(task=ti, stage=i, name=nm, kind=kind + ("+repeat" if rep_n > 1 else ""), repeat=rep_n, n_atoms=len(st["atoms"]), dom_share=cr["dom_share"] if cr else None, dom_order=" > ".join(cr["dom_order"]) if cr else None, color=color, mean_s=g.mean(), std_s=g.std(), p10_s=g.quantile(.1), p90_s=g.quantile(.9), empty_frac=float((g <= 0).mean()),
                            first_skill=st["atoms"][0]["name"], skills=[x["name"] for x in st["atoms"]], _atom0=st["atoms"][0], objects=sorted(set(skill_obj(x["name"]) for x in st["atoms"] if x["kind"] == "ordered"))))
    n_unordered_blocks = sum(1 for a, b in blocks if b - a > 1)
    info = dict(task=ti, name=tasks[ti], K=K, n_cuts_ok=int(sum(cut_ok)), n_blocks=len(blocks), n_unordered_blocks=n_unordered_blocks,
                unordered_frac=float(sum(x["mean"] for x in atoms if x["kind"] == "unordered") / max(sum(x["mean"] for x in atoms), 1e-9)),
            n_timesplit=0, n_class_regions=len(class_regions), class_regions=[dict(block=[a, b], classes=v["classes"], contig=round(v["contig"], 2), dom_order=v["dom_order"], dom_share=round(v["dom_share"], 2)) for (a, b), v in class_regions.items()], unordered_regions=[dict(block=[a, b], mean_s=float(sum(x["mean"] for x in atoms if x["block"] == (a, b))), m=max(x["sub"][1] for x in atoms if x["block"] == (a, b))) for a, b in blocks if b - a > 1],
                n_atoms=len(atoms), n_stages=len(stages), old_nst=NST[ti], len_s=per.loc[ti, "len_eff_mean_s"], longest20=ti in LONGEST,
                cut_ok=cut_ok, blocks=blocks)
    if verbose:
        print(f"\n### {ti} {tasks[ti]} len {info['len_s']:.0f}s old nst {NST[ti]} -> new {len(stages)} | cuts ok {sum(cut_ok)}/{K-1} | unordered blocks {n_unordered_blocks} ({info['unordered_frac']:.0%} of time)")
        for r in st_rows: print(f"  {r['stage']:2d} {r['mean_s']:5.1f}s ±{r['std_s']:4.1f} [{r['kind'][:9]:9s}] {r['name'][:150]}")
    return info, st_rows, lab

def design_min15(ti, verbose=False):
    """design() with class parts re-cut until no class part averages under MIN_STAGE_S."""
    m_cap = {}
    for _ in range(8):
        info, sr, lab = design(ti, verbose=False, m_cap=m_cap)
        bad = [r for r in sr if "class" in r["kind"] and r["mean_s"] < MIN_STAGE_S]
        if not bad: break
        for r in bad:
            x = r["_atom0"]; key = (x["block"][0], x["block"][1], x["cls"]); m_cap[key] = max(1, x["sub"][1] - 1)
    if verbose:
        print(f"\n### {ti} {tasks[ti]} old nst {NST[ti]} -> new {len(sr)} | class caps {m_cap}")
        for r in sr: print(f"  {r['stage']:2d} {r['mean_s']:5.1f}s ±{r['std_s']:4.1f} [{r['kind'][:14]:14s}] {r['name'][:150]}")
    for r in sr: r.pop("_atom0", None)
    return info, sr, lab

if __name__ == "__main__":
    only = [int(x) for x in sys.argv[1:]]
    infos, srows, labs = [], [], []
    for ti in (only or sorted(tasks)):
        info, sr, lab = design_min15(ti, verbose=True)
        infos.append(info); srows += sr; lab["task"] = ti; labs.append(lab)
    SUF2 = "_pred" if PROGRESS == "predicate" else ""
    if not only:
        pd.DataFrame(infos).drop(columns=["cut_ok", "blocks", "unordered_regions", "class_regions"]).to_csv(f"{OUT}/v2_tasks{SUF2}.csv", index=False)
        pd.DataFrame(srows).drop(columns=["skills", "objects"], errors="ignore").to_csv(f"{OUT}/v2_stages{SUF2}.csv", index=False)
        pd.concat(labs)[["episode_index", "stage", "start", "end"]].astype(int).sort_values(["episode_index", "start"]).to_csv(f"{OUT}/v2_episode_stage_frames{SUF2}.csv", index=False)
        json.dump({str(i["task"]): dict(cut_ok=[bool(c) for c in i["cut_ok"]], blocks=[list(b) for b in i["blocks"]], unordered_regions=i["unordered_regions"], class_regions=i["class_regions"]) for i in infos}, open(f"{OUT}/v2_structure{SUF2}.json", "w"))
        json.dump({str(i["task"]): [dict(name=r["name"], kind=r["kind"], repeat=r["repeat"], mean_s=round(float(r["mean_s"]), 1), std_s=round(float(r["std_s"]), 1), skills=r["skills"], dom_share=r["dom_share"], dom_order=r["dom_order"], color=r["color"]) for r in srows if r["task"] == i["task"]] for i in infos}, open(f"{OUT}/v2_stage_defs{SUF2}.json", "w"), indent=1)
        print("saved")
