# Corrected knife acquisition, cabbage and partial chili dicing — public-observation example

## Scope
One TRAIN10 practice sequence, source a32648a, obs024–070 of the restored both-ingredients-held attempt. Knife retained and cabbage visually became halves then diced clusters on board. Chili was first unintentionally split; later ONE supported half was deliberately diced via a torso-assisted cut. The other half remained unrecovered on adjacent counter, with some cabbage spilled. No cooking, transfer, full-task success or repeatability. This is NOT an evaluator script. Never import its practice binding/checkpoints or replay numeric coordinates in a fresh world.

## Geometry-based procedure
1. Inspect current handle-middle in wrist/head RGBD. Raise the arm outside the counter lip, then approach with joint-limit margin. A steep Cartesian approach reached a bad wrist branch; a human-informed alternative joint branch worked after clearance. At the final measured pose, close and then lift; closure alone is not retention evidence.
2. Preserve object orientation while lifting clear. In this run a torso-only rise avoided changing the near-contact arm branch. Static FK predicted a direct subsequent folding slew would dip TCP to z=.857m, below the counter; an intermediate elbow bend raised it first. FK has no scene collision model—inspect actual endpoints and surrounding housing clearance.
3. Estimate blade longitudinal axis `a` from two visible points on the blade/handle and edge-facing axis `b` from blade width. Orthogonalize `b` against `a`, normalize both, form `C=[a,b,a×b]`. Choose a convenient horizontal target blade heading `a_goal`, edge `b_goal=[0,0,-1]`; form `D=[a_goal,b_goal,a_goal×b_goal]`. Apply `Q=D @ C.T` to the measured gripper finger/closing directions. Confirm the resulting BLADE orientation with new RGBD, not just the requested tool axes.
4. This grasp used target heading60° in BODY XY with higher torso, rather than historical +Y heading/low torso that left wrist index5 near its lower bound. Fresh depth confirmed blade approximately[.501,.865,.006], edge[.0045,.0048,−.99998]. These vectors were measured for this grasp, not universally correct gripper commands.
5. Ground the vegetable surface and blade offset independently. Position blade over it, descend boundedly, then lift and inspect the actual material after clearance. Retain knife and joint margin; do not keep pushing because a target was not reached.

## Observed action/result sequence (historical BODY metres)
- Knife pre-cut TCP[.61,.31,1.12]; cabbage surface samples near[.678,.425,1.027].
- Targetz1.055 reached; targetz1.00 stalled at[.617,.314,1.043] with elbow lag+.104. No simulator fault.
- Lift to[.617,.314,1.13] reached; obs039 visibly showed two cabbage halves.
- Intended rear-half alignment[.73,.30,1.06], cut target[.73,.30,.97] stalled at[.709,.304,1.057]. Lift[.71,.304,1.15] then a small shoulder-sideways motion exposed the board.
- Obs043 showed multiple diced cabbage clusters, no visible cabbage halves, and two chili halves. Thus the intended isolated cut was NOT isolated. Exact intermediate contact paths/transition ticks are unresolved; do not infer each target touched only its intended object or that lag proves knife contact.

## Deliberate supported chili-half dicing (obs065–070)
- After failed counter-half recovery, changed to the supported half instead of another obstructed pinch. Fresh head depth measured its body around[.697,.261,.935] before a lateral base alignment; moved to give the left blade lateral margin, then restored the previously verified edge-down blade orientation.
- Pre-cut targetTCP[.64,.33,1.05] reached at[.641,.330,1.047]. Cut target[.64,.33,.93] **IK-stalled** at[.620,.325,.971], elbow q3≈−.013 and maximum tracking lag≈.007rad. This was a nearly straight-arm reach limitation, not evidence of cutting force. No visible dicing yet.
- Rather than repeat that Cartesian descent, used public FK to select a lower torso with unchanged chest pitch and fixed measured arm q. On this model `q0+q1−q2` stayed≈.119; torso[.44929,−.39939,−.069,−.0003]→[.65,−.77,−.2391,−.0003] predictedTCP[.637,.325,.927] while preserving blade direction. This numeric posture is historical evidence, NOT a transferable recipe.
- Actual obs069 showed the supported chili half replaced by diced material on the board. Raised knife to[.63,.33,1.13]; obs070 showed knife retained and diced chili remained. Measured fingers closed to0 although visible knife followed the hand—again aperture alone is not retention evidence.
- This is a deliberate partial-chili dicing result, not merely the incidental whole→halves transition atobs043. It does not establish repeatability, recovery/dicing of the other half, complete particle retention or cooking.
- For new geometry: remeasure blade and target; distinguish tracking/contact limitation from IK reach; adapt posture while preserving intended edge/frame; inspect the **entire intermediate slew** and clearance of elbow/forearm/camera, then lift and inspect. Subsequent pan work exposed that independent torso joint slew can dip below its endpoint height and that a high TCP does not guarantee a clear elbow. Static FK is a kinematic check, not collision certification.

## Transferable cautions
- Stage ingredients separately and keep full footprints inside the board; chili overhang and incidental splitting complicated recovery.
- Inspect after lifting/withdrawal before deciding a cut failed. A stalled endpoint can precede visible transition.
- Knife edge-down is the invariant; gripper wrist signs depend on actual grasp. Two studied human episodes held reversed knife orientations.
- Measured joint commands release persistent preload. `accept_partial` acknowledges a pose miss; it does not disable limits or certify contact.
- Right-hand counter approaches twice interfered with microwave despite apparently reachable TCP. Hand/forearm housing and actual scene clearance matter, not just fingertip endpoint.

See [human comparison](human-placement-knife-comparison-002.md) and the top EVAL PROCEDURE in [NOTES](../NOTES.md). Historical snapshots were used only for practice and are excluded from the evaluation procedure.
