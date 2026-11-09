# TRAIN199 first unseen-layout attempt — native success

Attempt `scanner-heldout-199-first`, scene `office_cubicles_right`, assigned protocol6 slot969c99. First full reset on this instance, no demo study, snapshots/restores or intermediate practice feedback. Public RGBD/proprioception used; feedback first requested at finish.

**Result:** native success/Q1, toggled_on=true and nextto=true, **1975/6387 physics steps =65.8333333333sim seconds**, finish wall580.935969397s. Reset setup excluded; not recovered here. First closure retained scanner through lift/withdrawal/turn; first switch press green. Not wall-time parity or final frozen evaluation: this is a first-attempt practice checkpoint on a previously unseen layout, now used for learning.

## Grounded approach and recoveries
- Initial route's left translation hit base_velocity_tracking_mismatch after16ticks. Inspected safety report, changed route via forward clearance rather than replaying blocked motion. No uncertain execution reported.
- Measured scanner front/true desk edge. BASE-only preparation draws were .12m then .05m, much shorter than TRAIN237; these are examples, NOT a future route.
- Withdrew .30m before opening/rotating jaws, returned and freshly sampled rim. Front samples around [.918,-.166,.813], low region/underside partly occluded. Shallow target [.932,-.17,.785] stalled at [.925,-.17,.780], padsZ.827/.733. No visible insertion displacement. Replaced persistent target with measured q, closed at achieved pose.
- Initial vertical lift hit elbow limit: achievedZ.839 instead of.95. Scanner front visibly followed, but full clearance was not established. Changed lift geometry by extending slightly forward to[1.07,-.17,.96]; achieved[1.072,-.168,.958], scanner visibly clear. Withdraw-.18 then yaw-30 verified retention. Do not interpret a joint-limit stop as failed retention or continue pushing the same goal.
- Laptop/held-scanner edges measured anew after turn. Base+.12 and raised arm[1.15,0,.96] approached laptop's left side; lateral goal stopped near joint limit at[1.152,-.007,.955]. Replaced with measured q and used small base-left.05 correction grounded in edge gap. Scanner right edge≈-.15, laptop left edge≈-.16 before correction. These are not transferable coordinates.
- Lowered toward supportZ.765; targetTCP.82 achieved.828 with lag. Unloaded measured q, opened, level-backout to[.97,-.008,.828]. Scanner attitude changed on settling/release but remained supported, close alongside laptop with longitudinal overlap. No zero-displacement claim.
- Cross-camera button samples: head[355,395]≈[1.13455,-.06388,.83033]; wrist[45,245]≈[1.13121,-.06378,.82460]. Cleared jaws before changing to high press orientation. Compound pose+close left grip open, so explicitly closed empty hand and verified command0 before pressing. Stage[1.133,-.064,.90], press.817 stopped at.831 with visible green. Prompt high withdrawal[1.10,-.20,1.02] cleared preload; green and supported adjacency persisted.

## Evidence
Public receipt/cache root:
`<observation-cache>/scanner-run-007-p6-969c99/scanner-heldout-199-first/`

- First retained full lift: `receipt_01792176664765891000_4b018acceaca4e888dc4cd2032b0e53d.json`.
- Supported lowering: `receipt_01792176857509978000_b99e71ff3859424e94bf568454addd36.json`.
- Level release clearance: `receipt_01792176872001140000_a50a066936794000a23db64c0dc117d8.json`.
- First green press: `receipt_01792176900349540000_164f960db39246a3a6e3dec317c26325.json`.
- Final public endpoint: `receipt_01792176909966919000_92b0ff1adbc54bcf9ca569f451929b17.json`.
- Finish reason: `heldout199-first-zero-shot-first-retention-first-green-press-supported-adjacency`.

Finished at the authorized rotation boundary; no same-instance reset. Await next matched READY instance via switching shim. Top NOTES procedure updated with endpoint-based grip verification and joint-limit-aware lift/placement recovery. One new-layout success is not reliability proof.
