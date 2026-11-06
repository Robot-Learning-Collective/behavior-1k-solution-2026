#!/usr/bin/env python3
"""The agent's robot API: observe(), act(), xyz(), pixel_to_body(), last_obs().

The same client is used in practice and in evaluation; the run's SETUP.json selects the transport:

  practice  SETUP has "queue": observe/act go to the practice worker's file queue through
            agent/practice/rpc.py, and admin_reset/admin_finish/practice_feedback/snapshot/restore
            through agent/practice/admin.py. Both run locally, or behind SETUP["exec_prefix"]
            (for example ["kubectl", "exec", "-i", POD, "-c", CONTAINER, "--"]).
  eval      SETUP has "evaluation_url" (or BEHAVIOR_EVAL_URL is set): observe/act go to the loopback
            HTTP bridge inside the policy server (agent/control/official_policy_server.py). Resets,
            snapshots and practice feedback are refused.

Control only uses onboard RGB-D and proprioception; simulator truth is never an input.
Bind a run with BEHAVIOR_SIM_RUN_DIR (practice) or BEHAVIOR_EVAL_RUN_DIR (eval).
"""
import base64
import hashlib
import io
import json
import math
import os
import subprocess
import sys
import time
import urllib.request
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import numpy as np

# Bind only an explicitly selected run: its SETUP.json names the worker or evaluation bridge.
RUN_DIR = Path(os.environ.get('BEHAVIOR_EVAL_RUN_DIR', os.environ.get('BEHAVIOR_SIM_RUN_DIR', str(Path.cwd())))).resolve()
SETUP_PATH = Path(os.environ.get('BEHAVIOR_SIM_SETUP_FILE', str(RUN_DIR / 'SETUP.json')))
if not SETUP_PATH.is_file():
    raise RuntimeError("Set BEHAVIOR_SIM_RUN_DIR to the run directory containing SETUP.json")
SETUP = json.loads(SETUP_PATH.read_text())
# Kinematics/diagnostics helpers: agent/control (this file's directory unless the run copies the client).
HELPER_DIR = Path(SETUP.get('client_helpers', str(Path(__file__).resolve().parent)))
sys.path.insert(0, str(HELPER_DIR))
from motion_diagnostics import arm_sample, diagnose, MODEL
from rgbd_geometry import camera_arrays, xyz_from_depth, project_body
EVAL_URL = os.environ.get('BEHAVIOR_EVAL_URL', SETUP.get('evaluation_url', ''))
if EVAL_URL and not EVAL_URL.startswith('http://127.0.0.1:'):
    raise ValueError('The evaluation bridge must be on loopback')
EXEC_PREFIX = list(SETUP.get('exec_prefix', []))
WORKER_PYTHON = SETUP.get('worker_python', 'python3')
REMOTE_WORK_DIR = SETUP.get('queue', '')
__all__ = ["observe", "last_obs", "xyz", "pixel_to_body", "act", "admin_reset", "admin_finish",
           "practice_feedback", "snapshot", "restore"]
REMOTE_RPC = SETUP.get('remote_rpc', '')
REMOTE_ADMIN = SETUP.get('remote_admin', '')

LOCAL_OBS_DIR = Path(SETUP.get('local_observation_root','/tmp')) / SETUP.get('observation_namespace', f'{RUN_DIR.name}_obs')
LOCAL_OBS_DIR.mkdir(parents=True, exist_ok=True)
STATE_CACHE = LOCAL_OBS_DIR / "last_obs.json"


def check_stop():
    if (RUN_DIR / "STOP").exists():
        raise RuntimeError(f"STOP file detected in {RUN_DIR}; aborting immediately.")


def _eval_http(path, data):
    request = urllib.request.Request(EVAL_URL + path, data=json.dumps(data, allow_nan=False).encode(),
                                     headers={'Content-Type': 'application/json', 'X-Behavior-Rollout': SETUP['epoch']})
    with urllib.request.urlopen(request, timeout=600) as response:
        return response.read(48_000_000)


def _worker_cmd(*remote_args):
    """Command that runs one practice RPC next to the worker (locally, or behind exec_prefix)."""
    if EVAL_URL:
        raise RuntimeError('Simulator/admin access is disabled in evaluation')
    return EXEC_PREFIX + ["env", f"ASTRA_WORK_DIR={REMOTE_WORK_DIR}"] + list(remote_args)


def _admin(payload, timeout):
    if EVAL_URL:
        raise RuntimeError('One evaluation attempt: resets, snapshots and practice feedback are refused')
    out = subprocess.check_output(_worker_cmd(WORKER_PYTHON, REMOTE_ADMIN),
                                  input=json.dumps(payload).encode(), timeout=timeout)
    return json.loads(out.decode())


def orient_axes(robot_dict, cameras=None):
    """Computes closing_axis_body (+Y of EEF) and finger_axis_body (+Z of EEF) from onboard eef_quaternion."""
    for arm in ("left", "right"):
        st = robot_dict[arm]
        q = np.asarray(st["eef_quaternion"], dtype=float)
        q = q / np.linalg.norm(q)
        x, y, z, w = q
        c_ax = np.array([
            float(2 * (x * y - z * w)),
            float(1 - 2 * (x * x + z * z)),
            float(2 * (y * z + x * w)),
        ], dtype=float)
        f_ax = np.array([
            float(2 * (x * z + y * w)),
            float(2 * (y * z - x * w)),
            float(1 - 2 * (x * x + y * y)),
        ], dtype=float)
        # Sensor axes include the rigid camera mounting transform, not finger axes.
        st["closing_axis_body"] = c_ax.tolist()
        st["finger_axis_body"] = f_ax.tolist()
        if cameras is not None:
            _, transform=camera_arrays(cameras[arm])
            right,down,depth=transform[:3,0],transform[:3,1],transform[:3,2]
        else:
            _, right, down, depth, _ = wrist_camera_pose_body(st) # Historical receipt compatibility only.
        st["cam_right_body"] = right.tolist()
        st["cam_down_body"] = down.tolist()
        st["cam_depth_body"] = depth.tolist()
    return robot_dict


def _Rx(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]], dtype=float)


def _Ry(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]], dtype=float)


def _Rz(a):
    c, s = math.cos(a), math.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]], dtype=float)


def _T(xyz, R=None):
    M = np.eye(4, dtype=float)
    if R is not None:
        M[:3, :3] = R
    M[:3, 3] = xyz
    return M


def head_camera_pose_body(torso_joints):
    """Asset-derived head camera approximation; not independently calibrated."""
    t1, t2, t3, t4 = [float(x) for x in torso_joints]
    M = (
        _T([-0.079032, 0.0, 0.34265], _Ry(t1))
        @ _T([0.0, 0.0, 0.400], _Ry(t2))
        @ _T([0.0, 0.0001005, 0.300], _Ry(-t3))
        @ _T([0.0, -0.00010015, 0.09962], _Rz(t4))
        @ _T([0.065511, 0.060003, 0.47598], _Rz(-1.5707963) @ _Rx(-1.9199))
        @ _T([0.060, 0.0, 0.010], _Rx(math.pi))
    )
    p_cam = M[:3, 3]
    R_cam = M[:3, :3]
    # USD Camera frame: +X is right (+u), +Y is up (-v), -Z is depth (+d)
    return p_cam, R_cam[:, 0], -R_cam[:, 1], -R_cam[:, 2], 204.0


def wrist_camera_pose_body(arm_dict):
    """Rigid EEF->camera from r1pro.usda 6029617cdd3a...; source-derived, not live calibrated."""
    R_eef = _quat_to_mat(arm_dict["eef_quaternion"])
    t = np.array([-0.05051000043749809, 0.002893388271331787, -0.06513172388076782])
    R_mount = np.array([
        [0.000005366298171, -0.9063159304520745, -0.42260079765659975],
        [-0.9999934526468499, -0.0015341083039915947, 0.003277373207977948],
        [-0.0036186509413855053, 0.422598013152574, -0.9063100047140948],
    ])
    p_camera = np.asarray(arm_dict["eef_position"]) + R_eef @ t
    R_camera = R_eef @ R_mount
    return p_camera, R_camera[:, 0], -R_camera[:, 1], -R_camera[:, 2], 480*17/20.995


def xyz(camera, obs=None):
    """Native pixel-aligned H×W×3 BODY metres. Invalid depth -> NaN; fresh processes work.
    Slice normally: xyz('right')[v0:v1,u0:u1]. No JPEG decoding or simulator calls.
    """
    obs=last_obs() if obs is None else obs
    if 'depth_path' not in obs or camera not in obs.get('cameras',{}):
        raise ValueError('Fresh protocol3 observation required: native float depth/calibration missing')
    with np.load(obs['depth_path'],allow_pickle=False) as arrays:
        return xyz_from_depth(arrays[camera],obs['cameras'][camera])


def pixel_to_body(camera, u, v, obs=None):
    """One nearest native image pixel, equivalent to xyz(camera)[round(v),round(u)]."""
    if not all(math.isfinite(float(x)) for x in (u,v)):raise ValueError('Finite pixels required')
    points=xyz(camera,obs=obs);ui,vi=int(round(u)),int(round(v))
    if not (0<=ui<points.shape[1] and 0<=vi<points.shape[0]):raise ValueError('Pixel outside native camera image')
    return points[vi,ui]


def _annotate_hud(img_bytes, robot, cameras, layout):
    """RGB-only native views. Pad geometry remains in state, never drawn on images."""
    from PIL import Image, ImageDraw
    im=Image.open(io.BytesIO(img_bytes)).convert('RGB')
    rgb_bottom=max(p['rgb_xywh'][1]+p['rgb_xywh'][3] for p in layout['camera_panels'].values())
    im=im.crop((0,0,im.width,rgb_bottom))
    for camera,calibration in cameras.items():
        x0,y0,w,h=layout['camera_panels'][camera]['rgb_xywh']
        panel=im.crop((x0,y0,x0+w,y0+h));draw=ImageDraw.Draw(panel)
        for tick in range(100,w,100):
            draw.text((tick,8),str(tick),fill='white',stroke_width=1,stroke_fill='black')
        for tick in range(100,h,100):
            draw.text((5,tick),str(tick),fill='white',stroke_width=1,stroke_fill='black')
        draw.text((10,h-18),f'{camera.upper()} native pixels',
                  fill='white',stroke_width=1,stroke_fill='black')
        for arm,color in (('left','cyan'),('right','yellow')):
            links=robot[arm]['own_links_body']
            points=[links['ag_start_point_body'],links['ag_end_point_body']]
            uv=project_body(points,calibration)
            inside=np.isfinite(uv).all(axis=1)&(uv[:,0]>=0)&(uv[:,0]<w)&(uv[:,1]>=0)&(uv[:,1]<h)
            robot[arm].setdefault('pad_pixels',{})[camera]={
                'start':uv[0].tolist() if np.isfinite(uv[0]).all() else None,
                'end':uv[1].tolist() if np.isfinite(uv[1]).all() else None,'in_view':inside.tolist()}
        im.paste(panel,(x0,y0))
    out=io.BytesIO();im.save(out,format='JPEG',quality=88)
    return out.getvalue()


def admin_reset(case="episode", attempt_name=None, practice=True, unbounded_practice=True):
    check_stop()
    if attempt_name is None:
        attempt_name = f"attempt_{case}_{int(time.time())}"
    payload = {
        "op": "reset",
        "case": case,
        "attempt": attempt_name,
        "practice": bool(practice),
        "unbounded_practice": bool(practice and unbounded_practice),
    }
    res = _admin(payload, timeout=60)
    STATE_CACHE.unlink(missing_ok=True)  # Reset invalidates pose AND remembered gripper intent.
    print(f"[RESET] case={case} attempt={attempt_name} practice={practice} -> {res}")
    return attempt_name, res


def admin_finish(reason="practice-complete"):
    if EVAL_URL:
        # Ends the agent's planning only; the evaluator owns termination and scoring.
        return json.loads(_eval_http('/finish', {'reason': reason}))
    payload = {"op": "finish", "reason": reason}
    res = _admin(payload, timeout=60)
    public = {"finished": True, "simulated_seconds": res.get("simulated_seconds"), "wall_seconds": res.get("wall_seconds_through_finish_admin")}
    if 'practice_feedback' in res:
        public['practice_feedback']=res['practice_feedback']
        print('[PRACTICE_FEEDBACK] '+json.dumps(res['practice_feedback']))
    print(f"[FINISH] reason={reason} sim_s={public['simulated_seconds']}")
    return public


def practice_feedback():
    """Privileged per-predicate/Q training feedback; never available during evaluation."""
    check_stop()
    if not SETUP.get('practice_feedback'):
        raise RuntimeError('Practice feedback is not installed on this worker')
    result=_admin({'op':'practice_feedback'},timeout=120)
    print('[PRACTICE_FEEDBACK] '+json.dumps(result))
    return result


def _snapshot_admin(op, name, **extra):
    import re
    check_stop()
    if not SETUP.get('snapshot_restore') or SETUP.get('protocol') != 6:
        raise RuntimeError('This worker does not advertise protocol6 practice snapshots')
    if not isinstance(name,str) or re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}',name) is None:
        raise ValueError('Snapshot name must be 1..64 letters, digits, underscores or hyphens')
    payload={'op':op,'name':name,**extra}
    return _admin(payload,timeout=180)


def snapshot(name):
    """Save native scene + whole controller at this completed-RPC boundary; practice only."""
    cache=json.loads(STATE_CACHE.read_text()) if STATE_CACHE.exists() else None
    memory=None if cache is None else {k:cache.get(k) for k in (
        'attempt_id','observation_id','motion_memory','last_commanded_grip','motion_execution_uncertain')}
    return _snapshot_admin('snapshot',name,client_state=memory)


def restore(name):
    """Close the current practice, restore a snapshot as a NEW attempt, and observe it."""
    # Invalidate BEFORE dispatch: a lost restore reply must never leave an old-world pose usable.
    STATE_CACHE.unlink(missing_ok=True)
    reply=_snapshot_admin('restore',name,practice=True)
    memory=reply.pop('client_state') or {}
    if reply.get('previous_attempt_feedback') is not None:
        print('[PRACTICE_FEEDBACK] '+json.dumps(reply['previous_attempt_feedback']))
    # Only public prerequisites/grip intent survive. Never reuse an old image,
    # pose, pending RPC or namespace. Fresh observe starts the new wall clock.
    seed={'attempt_id':reply['attempt_id'],'motion_memory':memory.get('motion_memory') or {},
          'last_commanded_grip':memory.get('last_commanded_grip') or {}}
    STATE_CACHE.write_text(json.dumps(seed))
    obs=observe('Restored practice snapshot '+name)
    return {**reply,'observation':obs}


def _save_and_summarize(reply, intent="", commanded_grip=None):
    if "error" in reply:
        raise RuntimeError(f"RPC error: {reply['error']} (fatal={reply.get('fatal')})")
    if STATE_CACHE.exists():
        cached = json.loads(STATE_CACHE.read_text())
        if cached.get('attempt_id') == reply.get('attempt_id'):
            reply['motion_memory'] = cached.get('motion_memory', {})
            if commanded_grip is None:
                commanded_grip = cached.get('last_commanded_grip')
    reply["last_commanded_grip"] = commanded_grip or {}
    obs_id = reply['observation_id']
    if reply.get('controller_protocol',0)<3:raise ValueError('Protocol3 RGBD worker required')
    attempt=str(reply['attempt_id'])
    if attempt in ('','.','..') or Path(attempt).name!=attempt:raise ValueError('Invalid observation attempt ID')
    directory=LOCAL_OBS_DIR/attempt;directory.mkdir(exist_ok=True)
    # Attempt-qualified filenames retain history even after reset starts observation IDs at one.
    data=base64.b64decode(reply.pop('depth_npz_base64'),validate=True)
    if len(data)>16_000_000 or hashlib.sha256(data).hexdigest()!=reply['depth_sha256']:
        raise ValueError('Float depth size/hash mismatch')
    if set(reply['cameras'])!={'left','head','right'}:raise ValueError('Expected three onboard calibrations')
    with np.load(io.BytesIO(data),allow_pickle=False) as arrays:
        if set(arrays.files)!=set(reply['cameras']):raise ValueError('Unexpected depth channels')
        for camera,calibration in reply['cameras'].items():
            camera_arrays(calibration)
            a=arrays[camera]
            if a.dtype!=np.float32 or list(a.shape)!=calibration['image_size_hw']:
                raise ValueError('Native float32 depth/calibration shape mismatch')
    depth_path=directory/f'obs_{obs_id:04d}_depth.npz';depth_path.write_bytes(data)
    reply['depth_path']=str(depth_path)
    raw_bytes=base64.b64decode(reply['image_base64'],validate=True)
    raw_path=directory/f'obs_{obs_id:04d}_raw.jpg';raw_path.write_bytes(raw_bytes)
    reply['raw_image_path']=str(raw_path)
    reply['robot']=orient_axes(reply['robot'],reply['cameras'])
    img_bytes=_annotate_hud(raw_bytes,reply['robot'],reply['cameras'],reply['image_layout'])
    img_path=directory/f'obs_{obs_id:04d}.jpg'
    latest_path = LOCAL_OBS_DIR / "latest.jpg"
    img_path.write_bytes(img_bytes)
    latest_path.write_bytes(img_bytes)
    del reply["image_base64"]
    reply["local_image_path"] = str(img_path)
    STATE_CACHE.write_text(json.dumps(reply, indent=2))
    return reply


def _compact_state(reply, intent, failure=None):
    obs_id=reply['observation_id']
    r = reply["robot"]
    t = [round(x, 3) for x in r["torso_joints"]]
    t_err = [round(x, 3) for x in r.get("torso_q_tracking_error_rad", [0, 0, 0, 0])]
    odom = r.get('base_odometry', r.get('simulator_base_odom', {}))
    b_rel = [round(x, 3) for x in odom.get("position_rel_start_body", [0, 0, 0])]
    b_yaw = round(odom.get("yaw_rel_start_rad", 0.0), 3)
    b_vel = [round(x, 3) for x in odom.get("body_velocity", [0, 0, 0])]

    lines = [
        f"[obs #{obs_id:03d} | act={str(reply.get('action_id') or '-')[:8]} | sim={reply['simulated_seconds']:6.2f}s | wall={reply.get('wall_seconds',0):6.1f}s | {intent}]",
        f"  base_odom({odom.get('source','unknown')}): rel_xyz={b_rel}m rel_yaw={b_yaw:+.3f}rad vel={b_vel} | torso={t} err={t_err}",
        f"  odom_uncertainty: {odom.get('uncertainty','legacy simulator-derived; not an official sensor')}",
    ]
    if reply.get('controller_protocol',0)>=4:
        lines.append('  COMMANDS persist: relative moves start at COMMAND, not measured pose. Into-surface targets keep pushing until changed. Release via act(left={"q": measured_left_q}) (ordinary slew); q_lag/effort are not contact-force proof.')
        lines.append('  torso_cmd='+str(np.round(r.get('last_torso_q_target',r['torso_joints']),5).tolist())+' effort_Nm='+str(r.get('torso_joint_efforts_nm')))
    for arm, tag in (("left", "L"), ("right", "R")):
        ar = r[arm]
        eef = [round(x, 3) for x in ar["eef_position"]]
        grip = [round(x, 4) for x in ar['finger_positions']]
        links = ar.get('own_links_body', {})
        pads = {k:[round(x,3) for x in links.get(k,[])] for k in ('ag_start_point_body','ag_end_point_body','ag_ray_midpoint_body')}
        q = [round(x, 5) for x in ar["joints"]]
        q_err = [round(x, 3) for x in ar.get("q_tracking_error_rad", [0]*7)]
        margins=ar.get('joint_limit_margins_rad',{})
        min_m=round(margins.get('min_margin_rad',0.),3)
        per_joint_margin=np.round(np.minimum(margins.get('to_lower',[0.]*7),margins.get('to_upper',[0.]*7)),3).tolist()
        c_ax = [round(x, 2) for x in ar["closing_axis_body"]]
        f_ax = [round(x, 2) for x in ar["finger_axis_body"]]
        g_sum_cm = sum(ar["finger_positions"]) * 100.0
        g_tag = f"command={reply['last_commanded_grip'].get(arm, 'unknown')} finger_sum"
        stalls = [f"q{i+1}={ar['q_tracking_error_rad'][i]:+.3f}" for i in range(7) if abs(ar.get("q_tracking_error_rad", [0]*7)[i]) >= 0.018]
        stall_str = f" TRACKING_ERROR({','.join(stalls)})" if stalls else ""
        lines.append(
            f"  {tag}: rigid_TCP(fwd,left,up)={eef}m fingers={grip}m grip={g_tag}({g_sum_cm:.1f}cm){stall_str}\n"
            f"     pad_start={pads['ag_start_point_body']} pad_end={pads['ag_end_point_body']} measured_pinch={pads['ag_ray_midpoint_body']}m\n"
            f"     close_dir={c_ax} fing_dir={f_ax} q={q} q_lag={q_err}rad limit_margins={per_joint_margin}rad min={min_m}rad"
        )
        if reply.get('controller_protocol',0)>=4:
            lines.append(f"     q_cmd={np.round(_command_q(ar),5).tolist()} effort_Nm={ar.get('joint_efforts_nm')} ({ar.get('joint_effort_semantics','unavailable')})")
    result=reply.get('act_result',{}) if failure is None else failure
    diagnosis={a:v.get('diagnosis') for a,v in result.get('arms',{}).items()}
    execution=result.get('execution',reply.get('execution',{})) or {}
    lines.append('  diagnosis='+json.dumps(diagnosis or 'not evaluated on observe/rejection',separators=(',',':')))
    lines.append(f"  status={result.get('reason','observe')} fault={result.get('error',execution.get('fault'))} "
                 f"uncertain={reply.get('motion_execution_uncertain',False)} pending={list(reply.get('motion_memory',{}).get('unresolved_pose_misses',{}))}")
    lines.append(f"  depth saved: {reply.get('depth_path','UNAVAILABLE')} -> s.xyz('left'|'head'|'right')[v,u] BODY metres; invalid NaN")
    if failure is not None:lines.append('  ERROR: image is LAST KNOWN endpoint, not proof of current pose after an uncertain action.')
    return '\n'.join(lines)


def _publish_observation(reply, intent, *, failure=None):
    """Mandatory per-public-call receipt. Durable delivery survives stdout redirection/forks.
    The thin Pi bridge attaches it at the outer tool result (including codemode).
    Python alone cannot convert a Bash text block into a model-visible image block.
    """
    failure=None if failure is None else {k:failure.get(k) for k in (
        'high_level_action_id','reason','error','error_type','steps')}
    text=_compact_state(reply,intent,failure)
    directory=Path(reply['local_image_path']).parent
    # macOS Python3.9 monotonic clocks are process-relative; callers use fresh processes.
    delivery_id=f'{time.time_ns():020d}_{uuid.uuid4().hex}'
    receipt=directory/f'receipt_{delivery_id}.json'
    receipt.write_text(json.dumps({**reply,'observation_contract':1,'compact_state':text,'call_failure':failure}))
    image_path=Path(reply['local_image_path'])
    manifest={'observation_contract':1,'receipt_file':str(receipt),'image_file':str(image_path),
              'image_sha256':hashlib.sha256(image_path.read_bytes()).hexdigest(),'state_text':text,
              'observation_id':reply['observation_id'],'attempt_id':reply['attempt_id']}
    out_dir=Path(os.environ.get('BEHAVIOR_SIM_DELIVERY_DIR',str(LOCAL_OBS_DIR/'deliveries')))
    out_dir.mkdir(parents=True,exist_ok=True)
    tmp=out_dir/f'{delivery_id}.tmp';tmp.write_text(json.dumps(manifest));tmp.replace(out_dir/f'{delivery_id}.json')
    # Ordinary Python redirection must not hide the compact state/receipt marker either.
    print(f'ROBOT_RECEIPT_FILE={receipt}',file=sys.__stdout__,flush=True)
    if os.environ.get('BEHAVIOR_SIM_DELIVERY_ACTIVE')!='1':
        print(text,file=sys.__stdout__)
        print(f'WARNING: image not attached — read {image_path}',file=sys.__stdout__,flush=True)


def observe(intent="Observe scene"):
    check_stop()
    job = {"op": "observe", "action": None, "request_id": str(uuid.uuid4())}
    out = _policy_rpc(job, timeout=90)
    reply = json.loads(out.decode())
    obs=_save_and_summarize(reply,intent=intent)
    _publish_observation(obs,intent)
    return obs


def clamp_arm6(delta):
    """Legacy name: validate finite action bounds; never silently truncate a request."""
    if delta is None or isinstance(delta, str):
        return delta
    if isinstance(delta, dict):
        d = dict(delta)
        d["delta"] = clamp_arm6(d["delta"])
        return d
    arr = list(delta)
    if len(arr) == 7:
        return [float(x) for x in arr]
    dx, dy, dz, rx, ry, rz = [float(x) for x in arr]
    tn = math.hypot(dx, dy, dz)
    rn = math.hypot(rx, ry, rz)
    if not all(math.isfinite(x) for x in (dx, dy, dz, rx, ry, rz)) or tn > 0.28 or rn > 1.15:
        raise ValueError("Finite-action bounds exceeded (0.28m / 1.15rad); use act() for bounded convergence")
    return [dx, dy, dz, rx, ry, rz]


def _send_action(
    intent,
    seconds=1.5,
    left=None,
    right=None,
    left_gripper=None,
    right_gripper=None,
    base=None,
    torso_delta=None,
    torso_target=None,
):
    check_stop()
    # Measured finger separation never determines commanded intent.
    cached = json.loads(STATE_CACHE.read_text()) if STATE_CACHE.exists() else {}
    known = cached.get("last_commanded_grip", {})
    left_gripper = known.get("left") if left_gripper is None else left_gripper
    right_gripper = known.get("right") if right_gripper is None else right_gripper
    if left_gripper is None or right_gripper is None:
        raise ValueError("Unknown gripper intent: explicitly set both grippers after reset/uncertain RPC")
    if any(not math.isfinite(float(g)) or not 0 <= float(g) <= 1 for g in (left_gripper, right_gripper)):
        raise ValueError("Gripper commands must be finite in [0, 1]")

    if not math.isfinite(float(seconds)) or not .1 <= seconds <= 2:
        raise ValueError("seconds must be finite in [.1,2]")
    action = {
        "seconds": float(seconds),
        "left": clamp_arm6(left),
        "right": clamp_arm6(right),
        "left_gripper": float(left_gripper),
        "right_gripper": float(right_gripper),
        "base": [float(x) for x in (base or [0.0, 0.0, 0.0])],
    }
    if torso_target is None:
        action["torso_delta"] = [float(x) for x in (torso_delta or [0.0, 0.0])]
    else:
        target = np.asarray(torso_target, dtype=float)
        delta = np.asarray([0., 0.] if torso_delta is None else torso_delta, dtype=float)
        if (target.shape != (4,) or not np.all(np.isfinite(target))
                or delta.shape != (2,) or np.any(delta != 0)):
            raise ValueError("Absolute torso requires four finite angles and zero torso_delta")
        action["torso_delta"] = [0., 0.]
        action["torso_q"] = target.tolist()
    if cached.get('controller_protocol',0)<4:
        raise ValueError('Persistent-setpoint controller protocol4 required; do not mix with an older worker')
    job = {"op": "act", "action": action, "request_id": str(uuid.uuid4())}
    # An uncertain RPC must not leave stale command intent available for reuse.
    if cached:
        cached['last_commanded_grip'] = {}
        cached['motion_execution_uncertain'] = True
        STATE_CACHE.write_text(json.dumps(cached))
    out = _policy_rpc(job, timeout=120)
    reply = json.loads(out.decode())
    reply["submitted_action"] = action
    execution = reply.get('execution')
    reply['motion_execution_uncertain'] = not execution or bool(execution.get('execution_uncertain'))
    if execution and not execution.get('execution_uncertain'):
        accepted_grip = ({'left':float(left_gripper), 'right':float(right_gripper)}
                         if execution.get('executed_ticks', 0) > 0 else known)
    else:
        accepted_grip = {}  # Missing/uncertain execution must not invent accepted intent.
    return _save_and_summarize(reply, intent=intent, commanded_grip=accepted_grip)


def last_obs():
    if STATE_CACHE.exists():
        obs = json.loads(STATE_CACHE.read_text())
        obs["robot"] = orient_axes(obs["robot"],obs.get('cameras'))
        return obs
    return observe("Initial observation")


def _command_q(st):
    return np.asarray(st.get('last_commanded_q_target',st['joints']),dtype=float)


def _command_pose(arm, obs):
    robot=obs['robot']
    return MODEL.arm(arm,robot.get('last_torso_q_target',robot['torso_joints']),_command_q(robot[arm]))[:2]


def _torso_goal(torso, obs):
    """Resolve shorthand once; retain all four absolute POSITION targets."""
    start = np.asarray(obs['robot'].get('last_torso_q_target',obs['robot']['torso_joints']), dtype=float)
    goal = start.copy()
    if torso is not None:
        if isinstance(torso, dict) and set(torso) == {"q"}:
            goal = np.asarray(torso["q"], dtype=float)
        else:
            if isinstance(torso, str):
                pair = TORSO_PRESETS[torso]
            elif isinstance(torso, dict) and set(torso) == {"to"}:
                pair = TORSO_PRESETS[torso["to"]] if isinstance(torso["to"], str) else torso["to"]
            else:
                raise ValueError("Torso requires preset, to=[joint1,joint3], or q=[four joints]")
            pair = np.asarray(pair, dtype=float)
            if pair.shape != (2,) or not np.all(np.isfinite(pair)):
                raise ValueError("Torso shorthand requires two finite joint angles")
            goal[[0, 2]] = pair
            goal[1] = start[1] - (2.1 / 1.15) * (goal[0] - start[0])
    limits = obs["robot"].get("torso_joint_limits_rad")
    if not limits:
        raise ValueError("Missing runtime torso bounds; observe the absolute4D-capable worker before motion")
    lo, hi = np.asarray(limits["lower"], dtype=float), np.asarray(limits["upper"], dtype=float)
    if (goal.shape != (4,) or lo.shape != (4,) or hi.shape != (4,)
            or not np.all(np.isfinite(np.r_[goal, lo, hi])) or np.any(lo > hi)
            or np.any(goal < lo) or np.any(goal > hi)):
        raise ValueError("Torso goal must be four finite angles within runtime limits; not silently clipped")
    return goal


def _wrap_pi(angle):
    return ((float(angle) + math.pi) % (2.0 * math.pi)) - math.pi


def base_step_toward(rel_x, rel_y, rel_yaw=None, max_v=0.20, max_w=0.40, obs=None):
    """Computes (seconds, [vx, vy, wz], pos_err, yaw_err) in current BODY frame toward start-relative target."""
    if obs is None:
        obs = last_obs()
    odom = obs['robot'].get('base_odometry', obs['robot'].get('simulator_base_odom', {}))
    xc, yc, _ = odom["position_rel_start_body"]
    yawc = float(odom["yaw_rel_start_rad"])
    dxs = float(rel_x) - float(xc)
    dys = float(rel_y) - float(yc)
    dxb = math.cos(yawc) * dxs + math.sin(yawc) * dys
    dyb = -math.sin(yawc) * dxs + math.cos(yawc) * dys
    pos_err = math.hypot(dxb, dyb)
    dyaw = 0.0 if rel_yaw is None else _wrap_pi(float(rel_yaw) - yawc)
    yaw_err = abs(dyaw)
    # Bound the geometric step BEFORE velocity conversion; preserve its direction.
    scale = min(1., .05 / max(pos_err, 1e-12), .10 / max(yaw_err, 1e-12))
    displacement = np.array([dxb, dyb, dyaw]) * scale
    t_need = max(np.linalg.norm(displacement[:2]) / max_v, abs(displacement[2]) / max_w)
    secs = float(np.clip(t_need + 0.12, 0.4, 2.0))
    return secs, (displacement / secs).tolist(), pos_err, yaw_err


TORSO_PRESETS = {
    "tall":   (0.840, -0.420),
    "normal": (1.074, -0.612),
    "mid":    (1.250, -0.750),
    "low":    (1.605, -1.073),
}


def _rotvec_to_mat(rv):
    rv = np.asarray(rv, dtype=float)
    theta = float(np.linalg.norm(rv))
    if theta < 1e-12:
        return np.eye(3)
    k = rv / theta
    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]], dtype=float)
    return np.eye(3) + math.sin(theta) * K + (1.0 - math.cos(theta)) * (K @ K)


def _mat_to_rotvec(R):
    val = float(np.clip((np.trace(R) - 1.0) * 0.5, -1.0, 1.0))
    theta = math.acos(val)
    if theta < 1e-8:
        return np.zeros(3)
    axis = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]], dtype=float)
    norm = float(np.linalg.norm(axis))
    if math.pi - theta < 1e-6:
        # At pi the antisymmetric part vanishes; the +1 eigenvector is the axis.
        _, vectors = np.linalg.eigh((R + R.T) * 0.5)
        direction = vectors[:, -1]
        if norm > 1e-12:
            if np.dot(direction, axis) < 0:
                direction = -direction
        elif direction[np.argmax(np.abs(direction))] < 0:
            direction = -direction  # Deterministic path at the ambiguous exact half-turn.
        return direction * theta
    return (axis / norm) * theta


def _quat_to_mat(q):
    x, y, z, w = [float(v) for v in q]
    n = math.sqrt(x*x + y*y + z*z + w*w)
    x, y, z, w = x/n, y/n, z/n, w/n
    return np.array([
        [1 - 2*(y*y + z*z), 2*(x*y - z*w),     2*(x*z + y*w)],
        [2*(x*y + z*w),     1 - 2*(x*x + z*z), 2*(y*z - x*w)],
        [2*(x*z - y*w),     2*(y*z + x*w),     1 - 2*(x*x + y*y)],
    ], dtype=float)


def _compile_arm_cmd(arm, cmd, obs, bounded=True):
    """
    Compiles a general composable arm spec dict into (worker_spec, gripper_val, needed_seconds).
    Supports:
      - preset='...' or q=[7 floats] or dq=[7 floats]
      - relative body rigid TCP delta: fwd, left, up (meters)
      - absolute body rigid TCP target: to=[fwd, left, up]
      - relative wrist-camera screen delta: cam_right, cam_down, cam_fwd (meters)
      - orientation delta: one BODY rotation vector [roll_deg,-pitch_deg,yaw_deg], pivoting about rigid EEF-origin TCP
      - target gripper axes: finger_dir=[x,y,z], close_dir=[x,y,z]
      - bias: 'current' (posture preference, not a zero-drift guarantee), 'nominal', preset name, or 7D list
      - grip: 1 (open) or 0 (closed)
    """
    st = obs["robot"][arm]
    default_grip = obs.get("last_commanded_grip", {}).get(arm)
    if cmd is None:
        return None, default_grip, 0.4
    if isinstance(cmd, str):
        return cmd, default_grip, 1.5
    if isinstance(cmd, list):
        return cmd, default_grip, 1.2

    allowed = {"preset", "q", "dq", "fwd", "left", "up", "to", "offset", "cam_right", "cam_down", "cam_fwd",
               "roll_deg", "pitch_deg", "yaw_deg", "finger_dir", "close_dir", "bias", "grip"}
    if not isinstance(cmd, dict) or set(cmd) - allowed:
        raise ValueError(f"Unknown arm fields: {set(cmd) - allowed}; use pixel_to_body separately")
    exclusive = [k for k in ("preset", "q", "dq") if k in cmd]
    if len(exclusive) > 1 or (exclusive and set(cmd) - {exclusive[0], "grip"}):
        raise ValueError("Joint/preset command cannot be mixed with Cartesian fields")
    if "to" in cmd and any(k in cmd for k in ("fwd", "left", "up", "cam_right", "cam_down", "cam_fwd")):
        raise ValueError("Absolute and relative translations cannot be mixed")
    if "offset" in cmd and "to" not in cmd:
        raise ValueError("offset requires to")
    if ("finger_dir" in cmd) != ("close_dir" in cmd):
        raise ValueError("Both finger_dir and close_dir are required")
    if "finger_dir" in cmd and any(k in cmd for k in ("roll_deg", "pitch_deg", "yaw_deg")):
        raise ValueError("Target axes cannot be mixed with rotation deltas")
    grip = cmd.get("grip", default_grip)
    if "preset" in cmd:
        import sys
        sys.path.insert(0, str(HELPER_DIR))
        from hybrid_arm_control import PRESETS
        q_goal = PRESETS[arm][cmd["preset"]]
        q_curr = _command_q(st)
        max_dq = float(np.max(np.abs(q_goal - q_curr)))
        secs = float(np.clip(max_dq / 0.65 + 0.2, 0.5, 2.0))
        return cmd["preset"], grip, secs

    if "q" in cmd or "dq" in cmd:
        q_curr = _command_q(st)
        q_goal = np.asarray(cmd["q"], dtype=float) if "q" in cmd else (q_curr + np.asarray(cmd["dq"], dtype=float))
        lo = np.asarray(st["joint_endpoint_metadata"]["endpoint_lower_rad"], dtype=float)
        hi = np.asarray(st["joint_endpoint_metadata"]["endpoint_upper_rad"], dtype=float)
        if q_goal.shape != (7,) or not np.all(np.isfinite(q_goal)) or np.any(q_goal < lo) or np.any(q_goal > hi):
            raise ValueError("Joint goal must be finite and within endpoint bounds; not silently clipped")
        max_dq = float(np.max(np.abs(q_goal - q_curr)))
        secs = float(np.clip(max_dq / 0.65 + 0.2, 0.5, 2.0))
        return q_goal.tolist(), grip, secs

    # Relative moves start at commanded FK, never at a contact-deflected measured pose.
    p_pinch, R_command = _command_pose(arm,obs)

    if "to" in cmd:
        tgt_xyz = np.asarray(cmd["to"], dtype=float)
        offset = np.asarray(cmd.get("offset", [0, 0, 0]), dtype=float)
        if tgt_xyz.shape != (3,) or offset.shape != (3,):
            raise ValueError("to and offset require 3-vectors")
        tgt_xyz = tgt_xyz + offset
        d_pinch = tgt_xyz - p_pinch
    else:
        d_pinch = np.array([
            float(cmd.get("fwd", 0.0)),
            float(cmd.get("left", 0.0)),
            float(cmd.get("up", 0.0)),
        ], dtype=float)

    # Add wrist-camera screen-frame deltas if provided
    if any(k in cmd for k in ("cam_right", "cam_down", "cam_fwd")):
        r_ax = np.asarray(st["cam_right_body"], dtype=float)
        d_ax = np.asarray(st["cam_down_body"], dtype=float)
        f_ax = np.asarray(st["cam_depth_body"], dtype=float)
        d_pinch = (
            d_pinch
            + float(cmd.get("cam_right", 0.0)) * r_ax
            + float(cmd.get("cam_down", 0.0)) * d_ax
            + float(cmd.get("cam_fwd", 0.0)) * f_ax
        )

    # Compute rotation rotvec in BODY frame
    if "finger_dir" in cmd and "close_dir" in cmd:
        f_goal = np.asarray(cmd["finger_dir"], dtype=float)
        if f_goal.shape != (3,) or not np.all(np.isfinite(f_goal)) or np.linalg.norm(f_goal) < 1e-9:
            raise ValueError("finger_dir must be a finite nonzero 3-vector")
        f_goal = f_goal / np.linalg.norm(f_goal)
        c_goal = np.asarray(cmd["close_dir"], dtype=float)
        c_goal = c_goal - np.dot(c_goal, f_goal) * f_goal
        if c_goal.shape != (3,) or not np.all(np.isfinite(c_goal)) or np.linalg.norm(c_goal) < 1e-9:
            raise ValueError("close_dir must be finite and not parallel to finger_dir")
        c_goal = c_goal / np.linalg.norm(c_goal)
        x_goal = np.cross(c_goal, f_goal)
        R_goal = np.column_stack([x_goal, c_goal, f_goal])
        rotvec = _mat_to_rotvec(R_goal @ R_command.T)
    else:
        # roll_deg around +X (fwd), pitch_deg around -Y (so +pitch_deg pitches fingertips UP!), yaw_deg around +Z (up)
        rx = math.radians(float(cmd.get("roll_deg", 0.0)))
        ry = -math.radians(float(cmd.get("pitch_deg", 0.0)))
        rz = math.radians(float(cmd.get("yaw_deg", 0.0)))
        rotvec = np.array([rx, ry, rz], dtype=float)

    # Rigid TCP is the EEF origin: never compensate using deflected finger geometry.
    delta6 = d_pinch.tolist() + rotvec.tolist()
    if not np.all(np.isfinite(delta6)):
        raise ValueError("Cartesian target must be finite")
    if bounded:
        delta6 = clamp_arm6(delta6)
    cartesian_fields = {'to', 'fwd', 'left', 'up', 'cam_right', 'cam_down', 'cam_fwd',
                        'roll_deg', 'pitch_deg', 'yaw_deg', 'finger_dir', 'close_dir'}
    if not np.any(np.abs(delta6) > 1e-6) and not (set(cmd) & cartesian_fields):
        return None, grip, 0.5

    bias_mode = cmd.get("bias", "current")
    if bias_mode == "current":
        lo = np.asarray(st["joint_endpoint_metadata"]["endpoint_lower_rad"], dtype=float)
        hi = np.asarray(st["joint_endpoint_metadata"]["endpoint_upper_rad"], dtype=float)
        q_bias = np.clip(_command_q(st), lo, hi).tolist()
        spec = {"delta": delta6, "bias": q_bias}
    elif bias_mode in (None, "nominal"):
        spec = {'delta': delta6}  # Dict explicitly retains Cartesian zero-error hold.
    else:
        spec = {"delta": delta6, "bias": bias_mode}

    trans_mag = float(np.linalg.norm(d_pinch))
    rot_mag = float(np.linalg.norm(rotvec))
    secs = float(np.clip(max(trans_mag / 0.10, rot_mag / 0.45) + 0.35, 0.5, 2.0))
    return spec, grip, secs


def _move_once(
    intent="Move robot",
    left=None,
    right=None,
    base=None,
    torso=None,
    seconds=None,
    _compensate_base=False,
):
    """Private single-action executor; public act() owns bounded goal convergence."""
    obs = last_obs()
    l_spec, l_grip, l_secs = _compile_arm_cmd("left", left, obs)
    r_spec, r_grip, r_secs = _compile_arm_cmd("right", right, obs)

    torso_goal = _torso_goal(torso, obs)
    t_secs = 1.2 if np.max(np.abs(torso_goal - obs["robot"]["torso_joints"])) > .025 else .4

    # Compile base
    b_cmd = [0.0, 0.0, 0.0]
    b_secs = 0.4
    if base is not None:
        if isinstance(base, list):
            b_cmd = [float(x) for x in base]
            b_secs = 1.0
        elif isinstance(base, dict):
            if "to_rel" in base:
                rx, ry = base["to_rel"][0], base["to_rel"][1]
                ryaw = math.radians(base["to_rel"][2]) if len(base["to_rel"]) > 2 else None
                b_secs, b_cmd, _, _ = base_step_toward(rx, ry, rel_yaw=ryaw, obs=obs)
            else:
                df = float(base.get("fwd", 0.0))
                dl = float(base.get("left", 0.0))
                dyaw = math.radians(float(base.get("yaw_deg", 0.0)))
                dist = math.hypot(df, dl)
                b_secs = float( seconds if seconds is not None else np.clip(max(dist / 0.16, abs(dyaw) / 0.40) + 0.15, 0.5, 2.0) )
                b_cmd = [
                    float(np.clip(df / b_secs, -0.25, 0.25)),
                    float(np.clip(dl / b_secs, -0.25, 0.25)),
                    float(np.clip(dyaw / b_secs, -0.50, 0.50)),
                ]

    dur = float(seconds) if seconds is not None else max(l_secs, r_secs, t_secs, b_secs)
    if not math.isfinite(dur) or not 0.1 <= dur <= 2.0:
        raise ValueError("seconds must be finite and in [0.1, 2.0]")
    dur = round(dur * 30) / 30  # Match actual worker tick duration before computing velocities.
    if isinstance(base, dict):
        # Preserve the bounded displacement when other components extend duration.
        velocity = np.asarray(b_cmd) * b_secs / dur
        velocity /= max(1., float(np.max(np.abs(velocity) / [.2, .2, .4])))
        b_cmd = velocity.tolist()
    if _compensate_base and any(b_cmd):
        # Worker Cartesian ramps are WORLD-fixed. Predict the base endpoint to preserve
        # BASE-relative arm endpoints. Small chunks bound curved-path approximation;
        # measured feedback corrects wheel acceleration/slip, not an exact trajectory claim.
        travel = np.linalg.norm(b_cmd[:2]) * dur
        scale = min(1., .05 / max(travel, 1e-12), .10 / max(abs(b_cmd[2])*dur, 1e-12))
        b_cmd = (np.asarray(b_cmd) * scale).tolist()
        vx, vy, w = b_cmd
        theta = w * dur
        if abs(w) < 1e-9:
            translation = np.array([vx*dur, vy*dur, 0.])
        else:
            translation = np.array([(vx*math.sin(theta)-vy*(1-math.cos(theta)))/w,
                                    (vx*(1-math.cos(theta))+vy*math.sin(theta))/w, 0.])
        Rbase = _Rz(theta)
        def compensate(arm, spec):
            if spec is None or isinstance(spec, str) or (isinstance(spec, list) and len(spec) == 7):
                return spec
            delta = np.asarray(spec['delta'] if isinstance(spec, dict) else spec)
            p,_ = _command_pose(arm,obs)
            corrected = np.r_[Rbase @ (p+delta[:3]) + translation-p,
                              _mat_to_rotvec(Rbase @ _rotvec_to_mat(delta[3:]))].tolist()
            corrected = clamp_arm6(corrected)
            return {**spec, 'delta': corrected} if isinstance(spec, dict) else corrected
        l_spec, r_spec = compensate('left', l_spec), compensate('right', r_spec)
    return _send_action(
        intent,
        seconds=dur,
        left=l_spec,
        right=r_spec,
        left_gripper=l_grip,
        right_gripper=r_grip,
        base=b_cmd,
        torso_target=torso_goal.tolist(),
    )




def _pinch(st):
    # Historical helper name retained internally; this is now a RIGID TCP.
    return np.asarray(st['eef_position'], dtype=float)


def _bounded_vector(v, limit):
    v = np.asarray(v, dtype=float)
    return v * min(1.0, limit / max(float(np.linalg.norm(v)), 1e-12))


def _policy_rpc(job, timeout):
    if EVAL_URL:
        return _eval_http('/rpc', job)
    transport = SETUP.get('rpc_transport', {})
    if transport.get('version') == 'framed-policy-v1':
        # Framed delivery: a lost reply is re-read from the worker, never re-sent as motion.
        from rpc_stream import request
        return request(_worker_cmd(WORKER_PYTHON, transport['remote_rpc']), job, timeout)
    return subprocess.check_output(_worker_cmd(WORKER_PYTHON, REMOTE_RPC),
                                   input=json.dumps(job).encode(), timeout=timeout)


def _cancel_rpc(request_id):
    if EVAL_URL:
        return _eval_http('/cancel', {'request_id': request_id})
    return subprocess.check_output(_worker_cmd(WORKER_PYTHON, REMOTE_RPC, '--cancel', request_id), timeout=15)


def _goal_rpc(job):
    """One motion RPC, with a separate cancellation message only on user STOP."""
    with ThreadPoolExecutor(max_workers=1) as pool:
        future=pool.submit(_policy_rpc,job,timeout=600)
        while not future.done():
            try:check_stop()
            except RuntimeError:
                _cancel_rpc(job['request_id'])
                return future.result() # Preserve the cancelled endpoint/partial receipt.
            time.sleep(.1) # Bounded lifetime of this one in-flight RPC, not a campaign poll.
        return future.result()


def _act(intent="Act", left=None, right=None, base=None, torso=None, seconds=None,
         max_steps=None, position_tol=0.005, rotation_tol=0.035, accept_partial=False,
         timeout_seconds=30., _context=None):
    """One goal, one RPC, per-physics-tick measured feedback; not collision planning.

    Arms: targets in the CURRENT BASE frame, remaining base-attached during base motion.
    Camera offsets use axes captured at call start. Rotation deltas form ONE BODY rotation
    vector (pitch uses -Y), not sequential Euler rotations; magnitude must be <=180deg.
    Base: relative translation expressed in call-start BODY frame, yaw degrees.
    Explicit seconds/max_steps bound the whole move INCLUDING its final hold tick.
    Their default is None; timeout_seconds still bounds otherwise unbounded goals.
    No5cm/20deg client sub-goals or action-chunk replay.
    Returns act_result with per-arm requested/predicted/measured rigid TCP evidence.
    Closing waits for all requested pose/base/torso goals. A prior missed arm goal
    blocks later grip-only closing until a replacement goal is reached, or the caller
    explicitly accepts that partial result with accept_partial=True. Neither means grasp success.
    Stops at reached/stalled/timeout. Check achieved before continuing.
    Torso accepts explicit joint targets/presets only; metric height approximation removed.
    """
    check_stop()
    if type(accept_partial) is not bool:
        raise ValueError('accept_partial must explicitly be boolean')
    if not math.isfinite(float(timeout_seconds)) or not .1 <= timeout_seconds <= 120:
        raise ValueError('timeout_seconds must be finite in [.1,120]')
    caller_limits=[]
    if max_steps is not None:
        if isinstance(max_steps,(bool,np.bool_)) or not isinstance(max_steps,(int,np.integer)) or max_steps<1:
            raise ValueError('max_steps must be a positive integer native tick count')
        caller_limits.append(int(max_steps))
    if seconds is not None:
        if isinstance(seconds,(bool,np.bool_)) or not math.isfinite(float(seconds)) or not 1/30<=float(seconds)<=120:
            raise ValueError('seconds must be finite in [1/30,120]')
        caller_limits.append(math.floor(float(seconds)*30+1e-9))
    caller_limit=min(caller_limits) if caller_limits else None
    if not .001 <= position_tol <= .05 or not .005 <= rotation_tol <= .2:
        raise ValueError("Invalid motion tolerances")
    if not STATE_CACHE.exists():
        raise ValueError('observe() before the first act(); act() never performs an extra observation RPC')
    obs = last_obs()
    if obs.get('controller_protocol', 0) != 6:
        raise ValueError('Fresh observation from per-tick controller protocol6 required before motion')
    if obs.get('ended'):
        raise ValueError('Attempt has ended; no motion dispatched')
    if obs.get('motion_execution_uncertain'):
        raise ValueError('Motion execution uncertain: observe() before planning another action')
    start_id = obs["observation_id"]
    _context = {} if _context is None else _context
    _context.update(start_observation_id=start_id, attempt_id=obs.get('attempt_id'))
    goals, grips = {}, {}
    targeted_grippers = []
    for arm, cmd in (("left", left), ("right", right)):
        if isinstance(cmd, list):
            cmd = {"q": cmd}
        if isinstance(cmd, str):
            cmd = {"preset": cmd}
        if isinstance(cmd, dict):
            rv = np.radians([cmd.get("roll_deg", 0), -cmd.get("pitch_deg", 0), cmd.get("yaw_deg", 0)])
            if np.linalg.norm(rv) > math.pi + 1e-9:
                raise ValueError("Rotation vector >180deg is ambiguous; compose explicit rotations")
        if isinstance(cmd,dict) and 'grip' in cmd:targeted_grippers.append(arm)
        spec, grip, _ = _compile_arm_cmd(arm, cmd, obs, bounded=False)
        grips[arm] = grip
        st = obs["robot"][arm]
        if spec is None:
            continue
        if isinstance(spec, str):
            import sys
            sys.path.insert(0, str(HELPER_DIR))
            from hybrid_arm_control import PRESETS
            spec = PRESETS[arm][spec].tolist()
        if isinstance(spec, list) and len(spec) == 7:
            q = np.asarray(spec, dtype=float)
            meta = st["joint_endpoint_metadata"]
            if not np.all(np.isfinite(q)) or np.any(q < meta["endpoint_lower_rad"]) or np.any(q > meta["endpoint_upper_rad"]):
                raise ValueError("Joint goal outside endpoint bounds")
            goals[arm] = {"q": q}
        else:
            delta = np.asarray(spec["delta"] if isinstance(spec, dict) else spec, dtype=float)
            R = _rotvec_to_mat(delta[3:])
            p_command,R_command = _command_pose(arm,obs)
            goals[arm] = {"p": p_command + delta[:3],
                          "R": R @ R_command,
                          "bias": spec.get('bias') if isinstance(spec,dict) else None}
    if any(g is None for g in grips.values()):
        raise ValueError("Unknown gripper intent: explicitly set both after reset/uncertain RPC")
    base_goal = None
    if base is not None:
        if not isinstance(base, dict) or set(base) - {"fwd", "left", "yaw_deg", "to_rel"}:
            raise ValueError("Base requires displacement dict, not ambiguous raw velocity list")
        if "to_rel" in base:
            if set(base) != {"to_rel"} or len(base["to_rel"]) not in (2, 3):
                raise ValueError("to_rel requires [start_x,start_y,optional_yaw_deg]")
            o = obs['robot']['base_odometry']
            base_goal = np.array([*base["to_rel"][:2], math.radians(base["to_rel"][2]) if len(base["to_rel"]) == 3 else o["yaw_rel_start_rad"]])
        else:
            o = obs['robot']['base_odometry']
            yaw = o["yaw_rel_start_rad"]
            df, dl = float(base.get("fwd", 0)), float(base.get("left", 0))
            base_goal = np.array([o["position_rel_start_body"][0] + math.cos(yaw)*df-math.sin(yaw)*dl,
                                  o["position_rel_start_body"][1] + math.sin(yaw)*df+math.cos(yaw)*dl,
                                  yaw + math.radians(base.get("yaw_deg", 0))])
        if not np.all(np.isfinite(base_goal)):
            raise ValueError("Base goal must be finite")
    torso_goal = _torso_goal(torso, obs)

    resolved={a:{k:v.tolist() if isinstance(v,np.ndarray) else v for k,v in g.items()} for a,g in goals.items()}
    goal={'id':_context.get('high_level_action_id',str(uuid.uuid4())), 'arms':resolved,
          'base':None if base_goal is None else base_goal.tolist(),
          'torso':None if torso is None else torso_goal.tolist(), 'grippers':grips,
          'targeted_grippers':targeted_grippers,'position_tol':position_tol,'rotation_tol':rotation_tol,
          'timeout_seconds':float(timeout_seconds),'accept_partial':accept_partial}
    if caller_limit is not None:goal['max_steps']=caller_limit
    _context.update(resolved_arm_goals=resolved,resolved_base_goal=goal['base'],torso_target_rad=torso_goal.tolist())
    prior_grips=obs.get('last_commanded_grip',{})
    closing={a for a,g in grips.items() if g<prior_grips.get(a,1.)-1e-6}
    memory=dict(obs.get('motion_memory',{}));misses=dict(memory.get('unresolved_pose_misses',{}))
    gated={a:misses[a] for a in closing if a in misses and a not in goals and not accept_partial}
    if closing and not accept_partial:
        for component,replaced in [('base',base_goal is not None),('torso',torso is not None)]:
            if component in misses and not replaced:gated[component]=misses[component]
    if gated:
        samples={a:arm_sample(a,goals.get(a),obs['robot'],torso_goal) for a in ('left','right')}
        result={'interface':'act-v4-per-tick-persistent-goal','achieved':False,'reason':'prerequisite_not_met',
                'steps':0,'errors':{},'trace':[],
                'arms':{a:{**s,'diagnosis':diagnose([s],'prerequisite_not_met',position_tol,rotation_tol)} for a,s in samples.items()},
                'prerequisite_gate':{'blocked_previous_misses':gated,'accepted_previous_miss':False}}
        obs['execution']={'requested_ticks':0,'executed_ticks':0,'stop_reason':'prerequisite_not_met','fault':None,'execution_uncertain':False}
    else:
        pending=dict(misses)
        for component,target in {**resolved,'base':goal['base'],'torso':goal['torso']}.items():
            if target is not None:pending[component]={'action_id':goal['id'],'status':'execution_pending','requested':target}
        pending_obs={**obs,'last_commanded_grip':{},'motion_execution_uncertain':True,
                     'motion_memory':{**memory,'unresolved_pose_misses':pending}}
        STATE_CACHE.write_text(json.dumps(pending_obs))
        _context['dispatch_started']=True
        job={'op':'act','action':goal,'request_id':goal['id']}
        # Exactly ONE RPC per act. No client-side interpolation, repeat dispatch,
        # bounded chunks, per-chunk image renders, or automatic retries.
        raw=_goal_rpc(job)
        reply=json.loads(raw.decode());execution=reply.get('execution')
        reply['motion_execution_uncertain']=not execution or bool(execution.get('execution_uncertain'))
        accepted={} if reply['motion_execution_uncertain'] else reply.get('last_commanded_grip',{})
        obs=_save_and_summarize(reply,intent=intent,commanded_grip=accepted)
        if not execution or 'act_result' not in obs:raise RuntimeError('Missing per-tick execution/diagnostic receipt')
        result=obs['act_result'];errors=result['errors']
        for a in goals:
            if result['arms'][a]['diagnosis']['status']=='reached':misses.pop(a,None)
            else:misses[a]={'action_id':goal['id'],'diagnosis':result['arms'][a]['diagnosis'],'requested':resolved[a]}
        for component,target,error in (
            ('base',goal['base'],max(errors.get('base_position_m',0.)/position_tol,errors.get('base_rotation_rad',0.)/rotation_tol)),
            ('torso',goal['torso'],errors.get('torso_joint_rad',0.)/.025)):
            if target is not None:
                if error<=1:misses.pop(component,None)
                else:misses[component]={'action_id':goal['id'],'normalized_error':error,'requested':target}
        result['prerequisite_gate'].setdefault('blocked_previous_misses',{})
        misses=result.get('unresolved_pose_misses',misses)
    result.update(start_observation_id=start_id,high_level_action_id=goal['id'],
                  execution=obs.get('execution'),ended=obs.get('ended',False),
                  caller_limits={'seconds':seconds,'max_steps':max_steps,
                                 'effective_max_native_steps':min(caller_limit,math.ceil(float(timeout_seconds)*30)+1) if caller_limit is not None else None,
                                 'includes_terminal_hold':True})
    memory['unresolved_pose_misses']=misses
    obs.update(motion_memory=memory,act_result=result)
    _context.update(result,last_observation_id=obs['observation_id'])
    STATE_CACHE.write_text(json.dumps(obs))
    return obs


def act(intent="Act", left=None, right=None, base=None, torso=None, seconds=None,
        max_steps=None, position_tol=0.005, rotation_tol=0.035, accept_partial=False, timeout_seconds=30.):
    """Single-goal, single-RPC per-tick feedback, diagnosis and missed-pose closing gate."""
    requested = dict(intent=intent, left=left, right=right, base=base, torso=torso,
                     seconds=seconds, max_steps=max_steps, position_tol=position_tol,
                     rotation_tol=rotation_tol, accept_partial=accept_partial, timeout_seconds=timeout_seconds)
    context = {'high_level_action_id':str(uuid.uuid4()), 'requested':requested, 'trace':[]}
    motion_complete=False
    try:
        obs = _act(**requested, _context=context)
        context.update(obs['act_result'])
        motion_complete=True
        _publish_observation(obs,intent)
        return obs
    except Exception as error:
        context.update(achieved=False, reason=('observation_delivery_error' if motion_complete else
                       'transport_or_execution_error' if context.get('dispatch_started') else 'request_rejected'),
                       error_type=type(error).__name__, error=str(error), steps=len(context['trace']))
        if STATE_CACHE.exists():
            prior=json.loads(STATE_CACHE.read_text())
            if prior.get('local_image_path'):
                try:_publish_observation(prior,intent,failure=context)
                except Exception as delivery_error:
                    print('ENDPOINT_DELIVERY_FAILED: '+str(delivery_error),file=sys.__stderr__)
        raise
    finally:
        with (RUN_DIR / 'control-action-results.jsonl').open('a') as output:
            output.write(json.dumps({'intent':intent, **context}, default=str) + '\n')


def main():
    """CLI adapter; every motor command goes through the same public act()."""
    import argparse
    parser = argparse.ArgumentParser(description="Authorized BEHAVIOR simulator: observe, pixel measurement, or bounded act")
    commands = parser.add_subparsers(dest="command", required=True)
    observing = commands.add_parser("observe", help="Capture RGBD/self-state without advancing physics")
    observing.add_argument("--intent", default="Observe scene")
    acting = commands.add_parser("act", help="JSON arguments to the sole public motion interface")
    acting.add_argument("json", help='e.g. {"right":{"up":0.02}}')
    pixel = commands.add_parser("pixel", help="Native float-depth pixel-to-BODY measurement; no motion")
    pixel.add_argument("camera", choices=["left", "head", "right"])
    pixel.add_argument("u", type=float)
    pixel.add_argument("v", type=float)
    args = parser.parse_args()
    if args.command == "observe":
        observe(args.intent)
    elif args.command == "pixel":
        print(json.dumps([float(x) if np.isfinite(x) else None for x in pixel_to_body(args.camera,args.u,args.v)]))
    else:
        params = json.loads(args.json)
        if not isinstance(params, dict):
            parser.error("act JSON must be an object")
        act(**params)


if __name__ == "__main__":
    main()
