# Seen207 staged-handle006 — upright miss, floor recovery, no attachment

`cabinet-train207-staged-handle-006` finished **false/Q0,1911ticks/63.7sim s/1668.3655388629923task-wall s**. Unbounded seen-instance practice, no snapshot/restore, not evaluation. [Native finish](../train207-staged-handle-006-finish.json). Reset RPC independently measured1.685428625s; repeated backend setup metadata is not reset latency. All commands/receipts remain in `../control-action-results.jsonl` and own cache namespace `cabinet-run-023-p6-d689c6`.

## Initial handle hypothesis failed

Unlike005, staged deep torso/arm while distant, then translated toward the upright handle. Close returned effectively zero aperture; a2cm lift did not retain the door and it fell face-up. Before close, TCP~[.652,.254,.240] versus sampled bar~[.669,.245,.243]: approximate19mm horizontal offset remained. This is a possible registration error, not proven sole cause. No direct upright-handle success. Human15600/15601/15602 all initially grasp the exposed panel edge, so direct handle remains an unsupported optimization hypothesis.

## Useful floor-recovery component

- Exposed bar lay~14–18mm high. Torso first joint target1.8 stopped~1.741 both before and after raising empty right. Canceled measured torso preload; do not keep requesting deeper crouch.
- Base+11cm forward/−3cm left brought bar nearer. With actual measured torso `[1.74133885,-2.75999045,-1.69999981,-.00000206]`, fresh handle target~[.515,.285,.015] became reachable.
- Obs016 pregrasp TCP.06m, Fdown,C[.55,.835,0]: Lq `[-.70902,.25448,-.42857,-.93608,-.20765,.80763,-.39643]`.
- Obs017 nominal.016m insertion: Lq `[-.83859,.16293,-.42353,-.53466,-.20897,.56508,-.32849]`; actual~.020m with lag. Canceled at measured q before close.
- Obs018 close left one finger fully open, other nearly closed; not retention proof. Obs019 upward12mm unloaded contact and both fingers closed around visible bar. Obs020 separate4cm lift, followed by25/55/80cm lifts, visibly carried the panel.
-25cm: torso `[1.744,-2.75,-1.3,0]`, Lq `[-.38814,.44265,-.36033,-1.29156,-.09825,.84701,-.56757]` (modest tilt).
-55cm: torso `[1.4505,-2.227,-.818,0]`, Lq `[-.16278,.55508,-.25334,-1.5723,.01589,.92949,-.64679]`, F~[.4175,-.275,-.866],C[.55,.835,0]. Minimum measured margin~.10rad.
-80cm: torso `[1.025,-1.45,-.47,0]`, Lq `[-.03958,.3991,.03628,-1.77749,-.51065,.97949,-1.11604]`; measured torso residual was canceled before navigation. Panel retained through travel.
- Later torso change to `[1.2,-1.8,-1.1,0]` without compensating world orientation produced left lag. World-oriented55cm carry Lq `[.03288,.49685,-.09808,-1.70983,-.00144,.51955,-.42894]` resolved it.
- New forward approach deflected left wrist near furniture. Measured-q cancellation/8cm retreat, then inboard target[.5,.15,.55], Lq `[-.04834,.20921,-.39475,-1.77236,-.16004,.74248,-.18233]` changed clearance; subsequent approach tracked. No collision-free claim or exact obstruction identification.

All numeric poses are historical measured-practice examples, not a new-world macro. Offline IK/FK is not collision checking.

## Tipping failure and corrected observations

First four backward draws from a mislabeled rim did not tip: cabinet top stayed flat~.452m despite changing perspective. Second geometry-grounded approach briefly increased top-plane slope~.04 then~.10, but it slipped back. No stronger pushing was used; missed targets were canceled at measured q.

After comparing tipping plus neighbors across three demos, empty-right withdrawal `fwd=-.30,up=.06` at obs047 unexpectedly changed the cabinet orientation. A no-goal `act(seconds=.5)` advanced only1tick, NOT a.5s hold. A10cm base retreat gave separation and additional physics. Final largest solid face was horizontal~.2587m; desired open-face-up was NOT established. The exact wrong-face orientation remains unresolved; do not label it successful tipping. Finished rather than treating this as a completed full chain or continuing uncertain visual assumptions.

Three-demo comparison and exact sampling/alignment are in `../NOTES.md`; artifacts under `<demo-samples>/make_cabinet_doors/tipping-study/`. Humans visibly engage the opening, keep the gripper open, tip away with arm/base/torso changes and withdraw. Own overhead sliding/pulling was not equivalent. New work should identify the opening from a clear view before contact, not infer a mating face from a rectangular top.

## Boundaries

0032757Q1 and0042817Q1 remain separate successful studied full chains.005321Q0 and0061911Q0 are later failed optimization attempts, not an ongoing2/2 reliability claim. First held-out207 remains5277Q0/overbudget. No native feedback was requested in006 before finish, no attachment success claimed, and historical TRAIN10 crash was not touched or repaired.
