# Scrubbing bathroom floor — fresh full success validated

Goal: use brush until NOT covered(floor,dirt). Official budget 4730 native ticks (~157.7 sim s).

## Ranked hard bits
1. Maintain bristle/floor contact while sweeping enough dirty surface; verify with practice feedback after attempts, not TCP completion.
2. Floor brush pickup with useful wiping orientation, retention on lift.
3. Reorient/hand over only if necessary; human TRAIN20 hands over at frames750–990.
4. Safe low-posture repositioning to remaining dirt.

Human TRAIN20 annotations: approach0–420, pickup420–750, handover750–990, approach990–1230, wipe1230–1650, reposition1650–2220, wipe2220–2580. Local demo directory currently contains annotations and metadata only, no dense RGB/proprio.

## Current evidence and failures
Pickup succeeded once (not yet repeated), see [exact staged descent and retention](examples/01-thin-brush-pickup.md). From aligned top: torso1.78/-2.54/-1.62/0, right raised clear, left z.07→.05→.03→.015 close. Lift to.12 and6cm carry retained brush.4.1sim seconds. Snapshot `brush_held`. No wiping bit mastered. a01 ended by restore after81.1sim s; feedback Q0, covered remains true. Current restored attempt continues; snapshots `before_brush_pickup` and `aligned_top` available in practice only.

Brush initially lies bristles-up, red thin oval near door. At first approach center ~[.525,.13,.01], floor z=-.0052. Align base right.10 puts brush y~.22. The visible bristles are not reliable solid grasp geometry: top closes at TCP z.04 and .05 gave zero aperture and brush stayed on floor after lift. Low descents .014/.020 can collide with floor, shift brush and deflect TCP laterally4–5cm; immediately withdraw, remeasure brush. Closing after a pose alone is not enough.

Torso `low` from start expands to [1.605,-2.509,-1.073,0] but stalls q2=-1.743 with folded arms. Release to measured torso q. A working bent-elbow preparation is left q[-.52695,.35921,-.79382,-.97008,1.51884,1.036,.79466], right mirror signs at q2/q3/q5/q7. THEN torso q[1.68,-2.54,-1.62,0] with arms omitted reached cleanly, hands [.253,+/-.27,.123]. Cartesian left [.525,.215,.07], fingers down, closing Y reached in .67s. Do not simultaneously solve large torso+Cartesian changes: it jumped into joint-limit branches.

q1=1.78 permits lower reach; q1=1.80 produced torso100Nm and right hand floor interference. Raising unused right to [.35,-.25,.22] and backing torso q1 to1.78 removed load. Horizontal orientations at this reach hit wrist limits; avoid insisting on them. Use timeout_seconds3–5 during exploratory contacts, not default30.

Large in-place yaw requests30/60 stopped after~14deg despite negligible tracking load.15deg requests reached (~13deg actual), .8–1s each. Initial survey turned left~135deg to brush. This is instance-specific, not a navigation route for evaluation.

Dense human reference unavailable locally: only annotations and metadata parquet. `pyarrow` import also unavailable. Human detailed pickup/hand-over comparison remains outstanding.

Update: restored brush retained through transit and many motions. Pitch45 at normal torso succeeds; pitch90 hits wrist limits. Flipping may be UNNECESSARY: first dark patch visibly disappeared after bristles-up brush approached floor (obs0032–0035 in practice-restore-brush_held-952d4c4e686f4d6cba8234ac0552a273). Dirt measured [.608,.190,-.00513] before descent. Torso [1.68,-2.54,-1.62,0], left [.51,.20,.03] then target z.012 (measured .019, IK_stalled), sweep [.54,.20,.02] (measured .538,.198,.027), lift [.46,.28,.15]: patch absent, brush retained. Whole goal still false/Q0 at pre-sweep check; further patch visible [1.231,-.673,-.005]. Snapshot first_patch_cleared. Local cleaning promising, not repeated/mastered yet.

Navigation near cabinet was difficult: normal torso, six yaw-15 steps from brush_held transit, left.10, fwd.20+.15 brought dirt ~[.724,.138]. Right arm forward blocked near cabinet; park at [-.05,-.30,.50] in crouch. Parking near center [.2,-.1,.3] caused self interference and torso100Nm; moving right outside cleared. Crouch1.78 near cabinet blocked at1.689;1.62 released,1.68 subsequently worked. Upright reposition then crouch preferable; crouched yaw-8 induced torso interference. Base has small residual drift near cabinet, always remeasure. Left floor reach .70 impossible; .51–.54 works at torso1.68. Do not waste time flipping until testing brush removal in original orientation.

## Completed restored episode
Attempt `practice-restore-brush_held-b25a5c6fa43a457eb47e39f022bdcf0e`: success=true, Q=1, predicate not-covered satisfied at step2864/sim95.47s (obs0051). Both patches cleared; brush still retained. First-patch cleaning repeated, then second patch cleaned. No flip or handover required. This is NOT yet a fresh full success.

Working second-patch drill: torso [1.68,-2.54,-1.62,0], fingers down/close +Y; left [.51,.18,.12] → [.53,.18,.025] → [.57,.18,.025] → lift [.43,.25,.15]. Sweep measured [.565,.179,.038] and IK stalled but patch disappeared and feedback succeeded. Right parked [-.05,-.30,.50], then held measured joints (q1 at limit). Original bristles-up brush removes dirt despite counterintuitive orientation.

Navigation lessons: zero all seven joints of both arms for narrow travel, left grip0/right1. Retention verified visually. Cartesian tucked arms interfered. Determine passage axis from depth wall planes, NOT perspective. In obs0044 leftwall points [.819,.605,.836] and [1.101,.563,1.101] imply passage yaw correction -8.5deg. Rightwall y intercept -.21 was too close for chassis; left.15 plus yaw-8 centered it, then forward.20 reached cleanly. Earlier repeated forward stalls and torso saturation were avoidable partition collisions. Release torso to measured q, shift left clear before advancing. Passage floor dirt became [.53,.18,-.005]. Snapshot clean_patch_stable holds first-patch-clear state.

## Ranked-bit completion
1. Cleaning: repeated first-patch removal and both-patch native success, including fresh reset.
2. Thin brush pickup/retention: independently repeated from fresh reset; lift, travel, and final retention verified.
3. Flip/handover: unnecessary, not an outstanding requirement; original orientation achieved native success twice.
4. Repositioning: completed both transitions in fresh attempt. Narrow-passage corner recovery works, though inefficient; use depth wall alignment earlier.
All required bits validated. The independent fresh attempt below already satisfies the no-restores, under-budget full validation requirement; no additional reset is needed merely to collect timing.

## Independent fresh full validation — SUCCESS
`admin_reset` attempt `independent-full-01`, no restore: native success=true, Q=1, satisfied_fraction=1 at step2809 / 93.63sim seconds, obs0074. This is within4730 ticks by1921 ticks (~64.0s). Finished after feedback. Pickup and both patches independently repeated; brush visibly retained after final lift. Earlier provisional statements above are historical.

### Per-phase timing (reconstructed from saved endpoint receipts)
Ticks = rounded simulated_seconds ×30. Wall durations are differences of cumulative receipt wall_seconds, including perception, reasoning, tool latency and pauses—not motor-only execution. Boundaries include the named endpoint. Initial wall origin is attempt start.

| Phase | Ending observation | Phase ticks | Sim seconds | Wall seconds | Cumulative ticks |
|---|---:|---:|---:|---:|---:|
| Initial survey / brush localization | 11 | 269 | 8.967 | 38.418 | 269 |
| Approach, crouch, staged pickup and lift verification | 23 | 393 | 13.100 | 99.722 | 662 |
| Stand, fold, carry and approach first patch | 37 | 608 | 20.267 | 94.806 | 1270 |
| Prepare, crouch, wipe first patch and lift | 42 | 328 | 10.933 | 50.414 | 1598 |
| Stand, fold, passage navigation/recovery and final approach | 68 | 900 | 30.000 | 268.729 | 2498 |
| Prepare, crouch, wipe second patch and final lift | 74 | 311 | 10.367 | 46.146 | 2809 |
| **Through final observation** | **74** | **2809** | **93.633** | **598.236** | **2809** |

`admin_finish` confirmed success at the same2809 ticks, wall622.388s (24.152s additional feedback/documentation/finish overhead; zero additional simulation ticks). Budget margin1921 ticks. Full lifecycle wall time10m22.388s. Evidence directory: `/home/b1k/practice/obs/scrub-run-01_obs/independent-full-01/`; phase boundaries are receipt observations11,23,37,42,68,74. Native feedback success/Q1 was checked after final lift and again by finish.

Fresh pickup: torso[1.78,-2.54,-1.62,0], displaced brush remeasured [.526,.344,.01354], closing axis[.84,.55,0]. Staged TCP z.07→.05→.03→.015/close then lift.12. Elevated brush depth [.561136,.332452,.122691] verified retention. Stand and zero-joint fold both arms for travel. First patch at [.5535,.1879,-.00516] cleared with y.17 short wipe.

Fresh passage navigation required several short sidesteps/advances to clear the corner; small turns sometimes stalled and caused torso load. A diagonal fwd.10/left.10 released corner interference. Do not copy odometry as a route: use fresh wall depth earlier than this attempt did. At obs0064 leftwall [.895,.384,.925] and [1.426,.226,.990] gave yaw correction~-17deg. After turn, dirt [.7535,.2001,-.00512]. Advance.22/left.02 stalled after~.16; left.06 then forward.06 succeeded. Last dirt remeasured in left wrist [245,90] at [.54717,.14954,-.00516].

Final wipe: bent left elbow preparation, right park[-.05,-.30,.50]; torso[1.68,-2.54,-1.62,0], left[.51,.15,.12] → [.53,.14,.025] → [.57,.14,.025]. Actual final TCP [.564,.155,.042], joint-limit stop; dirt disappeared. Lift[.43,.25,.15], then feedback confirmed success. No flip/handover needed. Receipt: independent-full-01/receipt_01792189576573275707_4e7ee04f149540bb9443756113848e6b.json under run observation directory.
