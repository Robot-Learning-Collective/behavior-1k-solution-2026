# TRAIN207 settled-handle010 — full chain attached after release

`cabinet-train207-settled-handle-010` is CLOSED. Native reset, studied/seen207, unbounded practice; no snapshot/restore or backend change.

- Finish: **attached=true/Q1,3103ticks/103.43333333333334sim s/2072.868077881998task-wall s**.
- 2060ticks below5163 practice meter, NOT native-budget evaluation.
- Independently measured reset RPC **3.049556875s**, not repeated setup metadata.
- Audit: **85 sequential execution-certain/fault-null motor actions**,71reached/11ordinary stalled/3bounded timeouts;86RGB endpoints. One additional local zero-tick torso-schema rejection. Summed native ticks3103. No uncertain transport, base guard, automatic replay or unexpected termination.
- First seating feedback3023=false; corrected seating3083=false; after release/withdrawal3103=true. Exact attachment transition tick within3084–3103 is unknown.
- Preserves original held-out2075277tickQ0 and all005–007 failures. Fifth studied207 native-reset full-chain success003/004/008/009/010, not5/5 reliability or unseen generalization. Historical TRAIN10 crash remains unresolved.

## Chain and changes

1. **Exposed edge:** distant ready/open arms, crouch, fresh top.451m; near-corner shallow insertion missed~7mm, canceled measured joints/accepted partial, closed. Independent14cm lift visibly carried panel. Retained compact aisle carry.
2. **Tip/opening verification:** right open pad line placed beyond fresh far rim, descended to[.682,−.310,.436]; canceled deeper miss. Q-refreshed bounded draws produced visible plane slopes(.0578,.0274),(.1635,.0838),(.2655,.1570). Withdrawal15cm revealed opening-up.
3. **Relocate before horizontal panel:** fresh long rim~[.588,−.231,.2477], insertion~.239; canceled/closed and separate4cm lift visibly moved cabinet. Backward40+20cm with measured-q refresh, floor-supported release. Empty-right withdrawal/clear posture had two bounded timeouts(obs032/033); achieved clear posture accepted rather than retrying exhausted wrist orientation.
4. **Alternate wrist/support:** raised six-stage retained rotation, horizontal handle-face-up panel. Fresh ottoman plane.373–.377;15cm right shift, shallow descent~.461→.389, canceled/opened.
5. **Improved empty-hand withdrawal:**−12cm/+15cm reachedTCP[.404,.153,.538], elbow−2.02168 with.063rad margin. This avoided009's+18cm elbow-bound detour. Raised torso/A/B orientation kept supported panel visibly stationary, then lowered already-oriented hand to50cm. Neither FK clearance nor stable panel proves whole-hand collision freedom.
6. **First lower registration failed:** fresh bar[.6075,.4337,.4062], panel.3905, target.398. Insertion displaced panel before closure. Canceled/closed;12mm unloading took2ticks; explicit close settling5ticks ended atzero aperture with panel stationary. Opened/raised4cm; no retention claim.
7. **Fresh registration met wrist limit:** displaced bar~[.594,.483,.40586],panel.39178. Changed target/axis hit wrist−1.0402 with commanded−1.0372 and bounded60tick timeout. Canceled/inset wrist−1.0; withdrew10cm, moved base15cm left to change workspace rather than force insertion. This was a failed registration, not a second verified grip.
8. **Recovered supported handle grasp:** fresh bar~[.602,.345,.406–.4074], plane.3918.49cm pregrasp had.264rad minimum joint margin; shallow.398 target reachedTCP~.399 with.424rad wrist margin. Canceled measured q/closed;12mm unloading2ticks, explicit closure settling20ticks to~6.5mm aperture. Separate4cm lift visibly raised panel, then torso lift confirmed retention. Base placement, registration and settling changed together; not isolated proof of one factor.
9. **Raised carry/alignment:** preserved mating-end relation through90cm posture and two inspected raised wrist yaw stages. Base−20cm/+5cm accounted for prior+15cm left recovery.60/40cm inspection exposed rim. Initial two-point long-edge estimate implied short46° vs panel55.6°, so−9.5° correction and fresh corner translation[+.0445,+.1762].35/28cm seating returned **false3023**.
10. **Corrected edge estimate, not more pressure:** canceled measured goal/lifted10cm.168 visible rim-top XYZ points in head rectangleu270:312,v535:582,z.247–.2485 fit short-edge51.01° (PCA singular spread.4367/.0206), while panel corner vector was44.8°. Corrected+6.2° while raised and compensated−17/−18mm base translation to approximately preserve far-corner registration. Bounded10cm descent returned **false3083** despite flush appearance.
11. **Release and settle:** rechecked same attach phase plus withdrawal in15600/15602 dense113–115.5s RGB and aligned108–118s proprio. Both have fingers~.05/.05 open during final attachment-phase positioning; pose/height differ and are not copied targets. Canceled measured q/opened at3090, withdrew8cm at3103. Native feedback then **true/Q1**, confirmed at finish. No postrelease pressing or door opening/closing. Release, settling and withdrawal are not individually isolated causes; true arose after this20tick sequence.

## Important distinctions

- Raised orientation preserved panel position; the subsequent first lower insertion did NOT. Do not call the entire approach nondisturbing.
- Explicit settling cannot rescue an empty grip: first5tick settling ended empty; changed-base recovery20tick settling preceded a real lift.
- Good gripper midpoint tracking is not full-hand collision clearance; first insertion displaced panel despite tight target tracking.
- Sparse rim pixels can bias axis estimates. Use several same-surface points, visible edges and correspondence checks, not just a rectangle's apparent parallelism. The168point fit uses public depth and a visually selected region, not privileged geometry.
- Native false while still holding a flush panel does not justify more downward force. Supported release/withdrawal can allow attachment; only native result establishes it.
- Local rejected `torso=[...]` was corrected to `torso={'q':[...]}` before dispatch. It used0ticks and was not a transport fault or uncertain-action replay.

## Evidence

Run-relative files:
- `train207-settled-handle-010-reset.json`
- `train207-settled-handle-010-seating-feedback.json` (false3023)
- `train207-settled-handle-010-corrected-seating-feedback.json` (false3083)
- `train207-settled-handle-010-release-feedback.json` (true3103)
- `train207-settled-handle-010-finish.json`
- `control-action-results.jsonl`, filtered by exact lifecycle

Final obs086 receipt: `<observation-cache>/cabinet-run-023-p6-d689c6/cabinet-train207-settled-handle-010/receipt_01792193852303584000_dc30e7cd6aed4192bb4982ada58a8435.json`.

Next useful refinement: move the base into a measured, better-margin supported-handle workspace BEFORE insertion, retaining raised empty-hand orientation and independent closure/lift verification; fit multiple rim points before final yaw correction. No stale numeric waypoint or guarantee of success on another world.
