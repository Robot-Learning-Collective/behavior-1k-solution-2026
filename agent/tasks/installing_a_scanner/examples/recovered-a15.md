# Recovered a15 — consecutive native Q1 pair with a14

TRAIN instance10, protocol6 recovery1054ef. Full native reset; no restores, regrasp, transport/schema errors or observed robot tilt. First acquisition retained through lift, withdrawal and carry. Training-only native feedback confirms toggled_on and nextto true at2675steps (budget6387),89.16666666666667sim seconds; endpoint551.1wall seconds, finish566.1796325510004wall seconds (reset setup excluded).

Evidence root `<observation-cache>/scanner-run-007-p6-1054ef/scanner-run-007-recovered-a15/`; terminal `receipt_01792130259635461000_560773b6f752449ab85ef6c7f9af46b6.json`. Finish reason `native-Q1-clean-full-run-consecutive-pair-a14-a15` reconfirmed Q1.

## Adaptive differences from a14
- Initial rear draws−.35/−.25/−.08/−.10 at1.27; recentered+.20/left−.12, extended1.34 draw−.10 then inspected and added−.05. At head(500,387), scanner rim[1.0886,-.2507,.79594]; edge/fascia head(470,402)[1.1175,-.229,.704]. Stop drawing rather than blindly copying longer sequences.
- Withdraw−.30, open, vertical-jaw seed, stage[.823,-.30,.805], approach+.40. Rim head(540,430)[.98873,-.27099,.82355]. Initial insertion1.015/Z.805 blocked and deflected to[.978,-.281,.766] **before any closure**. Unloaded measured joints, raised open jaws at[.96,-.28,.83], inserted[1.015,-.28,.83] successfully. This is pregrasp adjustment, not failed acquisition/regrasp.
- First close measuredq[-.44888,-.68336,.68902,-1.85543,-2.23302,-.70981,.26164];5.2cm gap. Lift1.014/Z.92 elbow-limited actual[1.022,-.30,.891], visibly retained; base−.30 retained.
- Carry yaw−25/fwd.60; lower[1.022,-.30,.79]; release measuredq[-.46762,-.65662,.69484,-1.70991,-2.21788,-.69888,.31358]; retreat−.20. Independent support visible.
- High switch posture as a14, base+.20/left−.22, close high. Fresh button head(417,317)[1.26669,-.12333,.80593], right(310,99)[1.26260,-.12690,.80391]. Stage[1.264,-.126,.87], pressZ.80, clear[1.20,-.126,.96]: activation true/nextto false at2529.
- Fresh flank head(360,420)[1.01058,-.00078,.81526]; laptop head(530,410)[1.07258,-.31964,.74520]. Closed-hand stage[1.045,.06,.91], descendZ.79, slide[1.045,-.09,.79], clearZ.96: native Q1 at2675.

## Pair acceptance
Consecutive independent full native practice attempts **a14:2516steps/Q1** and **a15:2675steps/Q1**, both first-closure acquisition, no restores/regrasp or observed robot tilt. a12 also Q1 but a13 failed between a12/a14 and is not erased. This is trained instance10 repeatability, not held-out generalization, official scored evaluation, fixed-script reliability or teleop-wall parity. Both runs used privileged training-only predicate feedback for placement correction.
