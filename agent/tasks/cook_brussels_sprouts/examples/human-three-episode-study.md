# Three human episodes: cutting, grasp, release and withdrawal

Study prompted by lead msg000707. No live controls during study; own world remains obs102/sim226.07 with knife elevated above third whole sprout. Public TRAIN demos only, no simulator object/scorer truth. This is sampled inspection, NOT a claim of continuous full-episode viewing or flawless human execution.

## Provenance and alignment
HF `behavior-1k/2026-challenge-demos` revision `4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`, task95. Metadata-joined rows:
- global19000/raw950010/instance1, study RGB frames10020–11009 (334–367s).
- global19001/raw950050/instance5, frames8610–9419 (287–314s).
- global19002/raw950070/instance7, frames5580–6619 (186–220.667s).
All three share frame-data shard `data/chunk-095/file-000.parquet`; head/left/right RGB file000, episode offsets respectively0,686.6,1212.6s (confirmed separately per camera).

Original three-camera clips, six contact sheets and named numeric records are outside Workbench:
`<demo-samples>/cook_brussels_sprouts/three-episode-study/`.
`manifest.json` records URLs/ranges; `19000/19001/19002-aligned.json` contains0.5s measured state+actions; `selected-aligned-records.json` contains every displayed sample's full left/right/torso measured and commanded joint vectors, gripper state and public-model TCP/axes. Scripts `study_human.py`, `study_sheets.py` reproduce extraction. Each camera is decoded from its own metadata offset, then local exact-time seek; source30FPS. No hidden transition data or private diagnostics.

Mapping follows existing source-reviewed `human_proprio.py`: RGB row n uses position groups from n−1, actions from n−2; measured61D and requested23D remain distinct. Torso/arm requests are absolute POSITION radians; native grip−1closed/+1open, equivalent live0/1. Base normalized fractions scale[.75,.75,1]. Human EEF is not jaw/TCP: table below uses current public rigid robot model on measured joints, not the native EEF directly. Source-reported render lag is not simultaneous shutter/contact proof.

## Matching fine annotations inspected
- 19000: container placement9780–10080; sprout pickup10080–10350; chop10350–10558; half placement10558–10729; half pickup10729–10846; placement10846–10950; next pickup10950–11384. Study includes placement tail, grasp, cutting and both post-release withdrawals.
- 19001: container placement8310–8670; sprout pickup8670–8850; chop8850–9063; half pickup9063–9134; placement9134–9177; next pickup9177–9263; placement9263–9365. Both halves required regrasp in this example.
- 19002: container placement5400–5640; sprout pickup5640–5850; chop5850–6258; half placement6258–6302; pickup6302–6444; placement6444–6560; next pickup6560 onward.

Head+both wrist RGB inspected at nine selected frames per episode (five grasp/cut, four transfer/release/withdrawal), plus measured/commanded sequences every0.5s throughout chop windows. Three-camera sheets retain frame numbers and distinct measured/requested labels.

## Concrete observations and state/action comparisons
### 1. Human does not release the whole sprout before cutting
All three keep left native grip−1 through approach and cut. Measured whole-sprout finger sums are56mm,61–62mm and48–49mm. RGB shows the sprout remains between left pads near board while right knife descends. Our first three transfers instead release the whole onto board, allowing it to roll (third moved to board edge); this introduces alignment/regrasp work the human avoids.

Human left fingers are **oblique**, not a fixed exact vertical orientation: at cut10500 finger[.420,−.640,−.644], close[.771,.626,−.120];8970 finger[.653,−.600,−.462], close[.624,.772,−.122];6180 finger[.231,−.840,−.491], close[.916,.358,−.182]. Their left shoulder/elbow branches are far from ours: e.g10500 measured q[−.423,.052,−.181,−1.367,−.351,.526,−.872], requested[−.423,.051,−.181,−1.367,−.353,.523,−.870]. Our vertical-finger branch often q1≈−2, q3≈−2.3, close to limits. Axis relaxation and geometric grasp adaptation are better hypotheses than another exact-axis endpoint push.

### 2. One principal downward crossing, with lateral/rotation corrections—not prolonged sawing
Measured/model TCP sequences (m), sampled0.5s; requests track these to a few mm around contact:
- 19000 R z1.174@10425→1.040@10500→.998@10530→1.024@10545; at10545 left aperture changed56→46mm and RGB shows retained half. Right x/y also changed substantially(.755,−.293→.604,−.132), so this is not a pure vertical prerecorded chop.
- 19001 R z1.119@8895→.986@8955→.992@8970→1.017@8985. Left61mm→47mm@8985→0@9015 despite command remaining−1; RGB then shows empty closed pads and pieces on board. Human did not assume retention; opened/regrasped both halves.
- 19002 R z1.155@5985→1.088 plateau@6060→.958@6180→.948@6195→1.051@6210. Left49→46–47mm and RGB shows half retained.
These samples support one principal downward excursion in each first annotated chop, with micro-adjustments; exact physics-contact count/success timing is not asserted from sparse RGB. Our corrected first split needed two downward approaches (first level failed, second tip-down worked); second split used one downward pass in two bounded RPCs, no lift/restrike between them.

### 3. Transfer tool-relative geometry, not human wrist coordinates
Human right fingers generally+X but closing direction near−Z at contact, whereas our successful grasp has closing direction approximately[−.11,.48,+.87] after tip-down roll. Opposite closing sign reflects different held-knife orientation; blindly adopting human joints/axes could turn our cutting edge up. At human10500 Rq[−.462,−.379,1.017,−1.631,.935,.876,−.168] versus requested[−.462,−.377,1.019,−1.631,.937,.876,−.169]; our second-cut Rq near[−.293,−.281,.816,−1.652,−1.200,−.751,−.277]. Use visible blade edge, target and current grasp, not vector replay.

### 4. Workspace preparation eliminates repeated base transfers
All three human head views show board centered, baking sheet immediately LEFT, empty bowl RIGHT, whole food poured onto board. Human half transfers are short left-arm motions: e.g19000 left TCP[.618,.087,.928] near cut→[.723,.243,.963] over tray. Our bowl beside food on steel blocked one descent; tray remains farther away; whole-food transfers needed multiple base changes. Hypothesis: finish current cut, then bring empty baking sheet beside board and move empty bowl clear of last whole before repeatedly regrasping/transporting halves.

### 5. Release followed by visible retained placement, not command-only success
- 19000 left half retained46mm@10680; native grip changes−1→+1 by10695, measured100mm. At10710 TCP rises to1.069 and half remains on sheet;10905/10950 show both halves on sheet after second release/withdrawal.
- 19001 first half30mm@9150→open100mm@9180, TCP rises. First half is still on sheet at9330; second release by9345 and9360 shows it resting after withdrawal. Initial cut had dropped the half: the corrective regrasp is preserved, not erased.
- 19002 retained47mm@6270; opens by6300,6315 empty hand withdrawn;6480/6525 show two halves remaining on sheet after second placement.
Right knife grip stays−1 with measured31–35mm throughout. Human fingers may close asymmetrically; actual sustained lift/placement RGB is stronger than aperture.

## Next hypothesis / practice adaptation
1. Current third sprout is already released at board edge: remeasure and complete bounded visible-edge cut; do not introduce a new bimanual crossing blindly next to left fingers.
2. Before eight half transfers, stage sheet adjacent to board and empty bowl away from last whole. Prefer shorter left-only motions and inspect release AND withdrawal with both wrist/head.
3. For future whole pickup, adapt oblique finger axes and closer workspace instead of forcing exact-down at joint limits. A controlled left-held cut could reduce rolling, but requires current knife/left-finger clearance from RGBD; no blind human-joint replay.
4. Maintain separate stroke/RPC/event counts; release persistent cutting preload on visible split and verify halves after lifting. No full-task, repeatability or native evaluation success claim from this study.
