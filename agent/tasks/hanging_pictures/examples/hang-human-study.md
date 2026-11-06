# Eight random human hang segments — motion paused, proposals NOT executed

## Scope and provenance

Requested correction followed: **8 random episodes beyond 6800/6806**, not all200. Uniform sample without replacement over6800–6999 excluding6800/6806, Python `random.Random(9017)`: **6846,6854,6863,6878,6935,6958,6974,6984**. These are TRAIN demonstrations on instances71,88,110,127,197,223,247,271. No evaluator worlds were opened. Supplementary matched-instance6806 check identifies an important error in my earlier interpretation.

Pinned HF `behavior-1k/2026-challenge-demos@4f50b44796641a4d526a19d9aeadc8aa51e2f2c2`. Metadata joins global episode→raw annotation→data/video shard. Fine `hang` intervals used, clipped to actual frame count. Full measured61D state and native23D commands analysed; no reward or scorer fields consulted. Public head RGB sampled at hang start, release−4s,−1s,+.067s,+.567s,+1.567s. **48 sampled original RGB frames reviewed, not continuous viewing.** Public depth range-seeked at start, release−1s and+1.567s for each episode (24frames), plus6806 frames1499/1532. No simulator motion/observe/reset since the study instruction; a06 remains finished.

Source/replication:
- `analyse_hang.py`: joins, all arm/torso/EEF/finger samples, opening events, approximate base integration and model pad rays.
- `hang_contact_sheets.py`, `hang_depth_frames.py`, `hang_geometry.py`: original video/depth sampling and geometric analysis.
- `hang-study-measurements.json`: exact left/right joints, torso, EEF xyzw, finger measurements, model pad endpoints, commanded opening, approximate base/world motion at8 key samples/episode.
- `hang-study-geometry.json`: selected pixels, fitted planes, measured gaps and estimated nail-relative positions.
- Large original shards, frames and contact sheets: `<demo-samples>/hanging_pictures/`; sheets named `hang-6846.jpg` etc. Not copied into Workbench.
- Exact proposed calls: **`hang-variations-proposed.json`**. This is a plan, not a replay success or permission to execute.

## Main correction: a visible 6cm wall gap is NORMAL after successful hanging

My earlier inference “front surface8cm from wall means not seated; push closer” was too strong. Across all8, **after opening/withdrawal the retained poster's visible front is5.8–6.2cm from the fitted wall**. Before opening it is5.3–8.0cm away. We see the *front*, not the back/mount; front-to-wall distance is NOT free clearance behind the object. A zero-gap target is wrong.

Our a06 front gap8cm is only~2cm larger than the demonstrated final stand-off, not evidence that8cm of additional pushing is available. Base tilt during approach remains a real warning. The touching link/object is unidentified.

Second correction: frame1499 in6806 is **pre-release approach**, not the final hanging posture. Right opening command occurs1536. At1499 the poster plane normal is[.7756,−.6312,−.0071] while wall normal[.88375,−.46796,.00153] (about11degrees apart), front gap7.49cm. At1532, four frames BEFORE opening, poster normal becomes[.88616,−.46338,.00177], essentially wall-parallel, and front gap5.93cm. Meanwhile EEF-to-wall gap grows9.00→11.66cm. **The frame appears to seat/reorient before opening; opening does not cause attachment.** This is a geometric/visual interpretation, not privileged attachment-state proof.

Our a06 wall normal at yaw31deg was[.777,−.629,−.004], unlike6806's[.884,−.468,.002]. From our recorded yaw and measured wall normal, matching6806 requires **base yaw≈20deg**, not the30–39deg I introduced. This is the strongest concrete next variation. Base yaw refers to our own reset frame; it is derived from public geometry, not copied across human world coordinates.

## Measurement contract and limits

- Right joints28:35; right EEF42:45/quat45:49; fingers49:51; torso53:57; left3:10. Actions right grip22: native−1closed,+1open. All joint values radians; EEF/pads metres.
- Recorded EEF is configured EEF origin, not an independently calibrated force/contact point. Shipped static FK matches sampled recorded EEF at~0.8–1.9micrometres; this validates indexing/kinematic convention, not collision geometry.
- Pad-ray points reconstructed from static finger geometry, calibrated using our earlier PUBLIC self-state receipt. They are **model-derived pad references**, not measured deformable contacts. Exact endpoints are in JSON.
- Depth: raw gray12le codes, inverse documented logarithmic encoding `exp(log(3.51)+q/4095*(log(13.5)-log(3.51)))-3.5` metres. No grayscale-as-metric shortcut. Head720 static calibration fx=fy306,cx=cy360 and recorded robot-relative camera poses; optical-axis conversion explicit. Wall-only patches have RMS0.6–0.8mm. Front sample patches selected from RGB.
- Source-reported alignment: RGB/depth frameN with position/camera rowN−1; command/velocity source lag distinguished in report. Opening command row is NOT instantaneous physical jaw opening. Opening-event state tables use raw state row so timing has~1–2frame uncertainty.
- Nail selected manually in the initial visible RGB/depth. Later EEF−nail uses integrated measured BODY velocity (no absolute world pose in61D), so XY is approximate and cannot support millimetre alignment. Height and same-frame wall gaps are substantially better grounded. Viewpoint, depth quantization and patch selection remain errors. No contact force, hidden mounting site or goal truth inferred.
- Source runtime emitted NumPy matmul warnings on this machine; reported results were finite and wall-fit residuals small. Treat last decimals as bookkeeping, not accuracy. Do not use these as precise physical contact coordinates.

## Per-episode results

Release is **commanded opening frame**. “Lower” is drop from last4s maximum EEF height, not necessarily a deliberate hook stroke. Gap is summed measured fingers0.5s before opening. Height is BODY EEF z, not nail height or poster centre.

|Episode / instance|Fine hang frames|Release / full-open frame|Gap mm|Raise over hang m|Release z m|Last4s peak→release drop mm|Front gap pre→post mm|Pad→wall pre mm|
|---|---|---|---:|---:|---:|---:|---|---|
|6846 /71|1576–2100|2012 /2020|16.8|.376|1.439|19|55→59|80,69|
|6854 /88|1410–1949|1844 /1849|12.1|.255|1.444|12|80→62|108,101|
|6863 /110|1234–2099|1951 /1956|11.1|.254|1.397|30|65→60|94,88|
|6878 /127|1548–2645|2568 /2573|16.6|.293|1.286|16|64→59|118,108|
|6935 /197|1192–1770|1661 /1693|11.9|.319|1.376|19|72→62|105,98|
|6958 /223|1675–2218|2163 /2186|12.0|.373|1.393|0|68→59|100,94|
|6974 /247|1499–2160|2068 /2088|13.4|.359|1.466|19|79→58|121,113|
|6984 /271|1408–2100|2022 /2048|12.2|.216|1.368|1|53→61|90,83|

### What the RGB and proprio show in each

- **6846:** prior left→right hand-over; right grips the right edge below centre but above the bottom corner. Raise38cm, finish with17mm downward EEF movement and5.4deg orientation change in last1s. Last4s estimated wall-tangent correction+93mm; almost no net wall-normal push. Poster stays after fingers separate; hand withdraws/backoffs and lowers8cm in1.5s.
- **6854:** right-edge lower-quarter grip, no hand-over. Raise26cm. Last1s EEF BODY forward−53mm, height−10mm, orientation12.6deg. Last4s approximate normal motion−86mm (away), tangent+82mm. Thus “push continuously until opening” is not the common mechanism. Poster settles from80mm front stand-off to62mm and stays while hand separates.
- **6863:** right lower-edge/near-corner grip; raise25cm, then clear~26mm lowering in last1s (30mm from recent peak). Large17.3deg orientation change and−59mm BODY forward retraction. Rightq3 rises~.41rad andq5 falls~.34rad during that second; torso nearly fixed. Poster remains upright against wall after opening; hand stays near briefly rather than an immediate large retreat.
- **6878:** prior hand-over, visibly near bottom-right corner grasp (lower than others). EEF release height1.286m,~42cm below estimated nail, yet poster stays hung. This is direct evidence against a universal EEF-at-nail/centre-height target. Last1s height changes only−4mm while wrist orientation changes13deg and hand retracts51mm BODY-forward. Hand later moves away; left is idle/open.
- **6935:** right lower-side grip; raise32cm, then16mm lowering and15.7deg wrist change in last1s. Torso fixed near[.45,−.399,.104,0]. Opening reaches>8cm only~1.07s after command. Poster remains while fingers open; early small gap is not a command-failure diagnosis.
- **6958:** lower-right side grasp. Raise37cm; EEF rises11mm in final1s, no peak→release lowering. Wall-tangent correction~157mm over4s; final normal retreat~45mm. Poster still seats successfully: a lift-then-lower stroke is **not necessary in every episode**. Open completes~.77s after command, then hand lowers17cm over1.5s.
- **6974:** right edge closer to lower-middle, not bottom corner; highest release EEF1.466m (~22cm below nail). Recent peak drop19mm; final1s rotation17.8deg, wrist7+.351rad, BODY forward−62mm, torso stable. Base movement offsets much of arm retraction, so BODY delta alone misdescribes world motion. Opening takes~.67s; after opening, hand lowers24cm and leaves poster supported.
- **6984:** right lower edge. Last1s arm orientation changes only.11deg and EEF BODY pose essentially fixed; base advances~18mm. Last4s approximately+35mm wall-normal motion, no tangent correction. Poster survives opening/withdrawal without a distinct lowering or wrist-tilt manoeuvre. This supports a small base-only seating alternative, not mandatory arm overmanipulation.

### Common vs variable

**Common:** right-hand edge grip; raise object into alignment before releasing; arm posture/torso mostly stabilized near final contact; front stand-off settles near6cm; poster remains after fingers open and withdrawal; opening and withdrawal are distinct phases. No hard push-through/robot tilt is required by these examples.

**Variable:** hand-over or direct grasp; grasp height along right edge; EEF release z1.286–1.466; 0–30mm recent lowering; last-second orientation0–18deg; lateral corrections on either side; base motion vs arm motion; opening completion. These are not five independent proofs of one identical trajectory.

All8 random examples are more frontal than our a06:7 wall normals within~4.3deg of BODY+X, one6863 at~−16.6deg. Matched6806 is the useful exception at~−28deg; oura06 was~−39deg. A frontal compact posture is a defensible alternative, but not required by6806.

Exact release q/torso/EEF/pads and earlier/later states are retained in the JSON, avoiding a misleading single “mean joint posture.” Joint endpoints must be validated: e.g.6935 wrist7≈1.570 approaches/exceeds our1.5608 command endpoint; do NOT blindly replay every measured human q or clip it silently.

## Five proposed variations — require lead reply before ANY motion

Each starts with an independent own reset, previously verified pickup/lift/carry to[.35,.45,20]. That prefix is in the successful examples. Use ONE variation, not a sweep in one episode. Every `act()` endpoint is inspected; calls are not run blindly. **Exact numeric calls and guards are in `hang-variations-proposed.json`.** Placeholder `MEASURED_RIGHT_Q` means read current seven measured joints immediately before that call, validate limits, then submit; it is not a fixed historical q.

Common matched prefix: frame1499 rightq+torso in free space, grip0; then `base.to_rel=[1.00,.75,20]` (conservative geometry-derived waypoint). This predicts wall-relative heading like6806; remeasure wall, poster and nail before further movement. If geometry disagrees, stop/revise rather than pushing. Common seating increment is only BODY[+.01326,−.00702] (15mm along measured expected wall normal). Hold measuredq; open without translation; inspect retention; only then withdraw BODY[−.0884,+.0468]. Stop for unexpected motion, newly rising base>3mm, non-achievement or escalating lag; cancel preload with measuredq. Front-gap target is NOT zero.

1. **Matched heading + genuinely late approach (first choice).** Keep yaw20, not30–39. After common prefix use6806frame1520 q `[-1.165885,-.061282,-.014067,-1.151664,.012701,.800061,.933163]`, grip0,max_steps8; then common15mm seating/hold/open/withdraw. Evidence: matched6806 wall normal,1532 pre-opening seating,1499 mislabel correction. No human1532 deflected/snap posture is treated as the cause of attachment.
2. **20mm downward settling, not150mm centre-height raising.** Same prefix; `right={up:-.02}`,max_steps4, then common seating/hold/open/withdraw. Evidence:6846/6863/6935/6974 lower~16–30mm before opening; human corner grip can leave EEF42cm below nail. Hypothesis: our retained poster's attachment region is a few centimetres too high, not15cm too low. Abort if RGBD instead shows it below target.
3. **+20mm wall-tangent correction.** Same prefix; `base={fwd:.00936,left:.01768}`,max_steps3, then common sequence. Evidence:6846/6854/6878/6935/6958 show positive tangent adjustment before release; use a much smaller bounded probe. Tests lateral alignment without changing grasp/height/orientation simultaneously.
4. **−20mm wall-tangent correction.** Same prefix; `base={fwd:-.00936,left:-.01768}`,max_steps3, then common sequence. Evidence:6863's estimated final4s tangent adjustment is−21mm;6806 late approach moves rightwards in BODY. This is an alternative hypothesis, NOT another movement appended after variation3. Fresh RGBD must justify the side.
5. **Frontal compact human approach (different posture family).** In free space use6863frame1921 q `[-1.295561,.104380,-.009032,-.842254,.085212,.662514,1.020350]`, torso `[.449495,-.399180,.019511,.000069]`,grip0,max_steps16. Then conservative `base.to_rel=[1.08,1.00,-8]`,max_steps24; recheck retained poster orientation and clearance, then at most `base.fwd=.015`,max_steps3. Hold measuredq/open; if retained, `base.fwd=-.10`. Evidence:7/8 are approximately frontal,6863 provides an in-limits near-contact human configuration; a06's oblique long reach repeatedly tilted base. Predicted waypoint is not guaranteed collision-free, so stop earlier if visuals disagree. This intentionally changes posture family, unlike variants2–4.

**Acceptance:** visible poster stays at nail after open and a separate withdrawal/hold, level base, no hand support. A pose/effort spike, held silhouette, annotation name or first moment after opening is insufficient. Preserve failed variants, not just successes. Awaiting lead selection/authorization; none of these has run.
