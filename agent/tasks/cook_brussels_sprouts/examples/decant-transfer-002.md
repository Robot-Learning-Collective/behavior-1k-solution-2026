# Corrected-source decant and sprout transfer

TRAIN10 sourcea32648a; attempt `practice-restore-recovery_container_carry-fd61d378358448deba8fd30124c4e475`. Same-source snapshot restore only. Torso `[.45,-.4,-.22,0]` throughout. Scene-specific inspected motions, not replay macros.

## Failed Cartesian pour preserved
In preceding `brussels-cut-recovery-001`, pitch45 exhausted wrist range. Direct Cartesian orientation `[.75,-.22,1.08]`, finger+X/close+Y diverged to TCP `[.566,-.235,1.861]`, q3lag3.206rad and torso deflection/effort. Endpoint IK feasibility did not ensure controller convergence. Explicit nearest-valid measured-q release needed >3.3s slew, not an instantaneous reset; then same-source `recovery_container_carry` restore closed this failed branch. No cut occurred there.

## Revised retained-rim pour
From `recovery_container_carry`, right grip0/fingers~.0167/0:
1. Midpoint q `[-.59246,-.43656,.58660,-1.53120,-1.23842,-.42974,-.36689]`.
2. Sideways q `[-.40583,-.51150,.58150,-1.42482,-.52329,-.27942,-.43254]` → TCP `[.699,-.300,1.051]`, fingers+X/close+Y.
3. roll−20 then−15; returned through midpoint then upright q `[-.77915,-.3616,.5916,-1.63773,-1.95166,-.5794,-.30117]`.
4. **All four sprouts visibly on steel, empty container retained** at obs8. Move `[.85,-.45,1.10]`; lowering goal z.999 saturated at TCP `[.823,-.437,1.026]`. Accepted measured-q and opened, releasing empty container a few cm above steel. Withdrew .20 and folded; container stayed upright, four whole sprouts on steel.

## Sprout grasp and transfer
- Two early pinches closed empty/rolled food; transient green near fingers and one depth sample were not retention proof. A subsequent clear lift showed all four still on steel. Preserve these failures.
- Stance correction put selected sprout near `[.702,.191,.908]` top; final left target `[.704,.202,.895]` reached TCP `[.702,.202,.896]`. Finger-down, closing−Y. Close0 gave fingers~.0316/.0307, total6.2cm.
- Lift `[.704,.202,1.12]` retained; base back.10/left−.35 carry retained; board fresh depth z.883, clear placement `[.606,.116,.930]`; open and lift1.10. Obs35 showed sprout remaining on board and three whole sprouts on steel.
- Left q0 fold after only .15 retreat hit table edge (TCP~.561,.251,.874; q4lag1.369). Measured-q release2.5s; base retreat requested.25, achieved~.203 then base_velocity_tracking_mismatch guard. Did not retry retreat. Hand was visibly clear; left fold completed without base motion. Guard is velocity evidence, not collision/tilt truth.
- Snapshot `recovery_sprout_on_board` at obs40/sim163.33, arms folded. Knife subsequently reacquired and cut: see `knife-cutting-002.md`.

## Transferable points
Use bounded inspected joint-space orientation waypoints when a large Cartesian reorientation demonstrably diverges. Verify retained pour by both empty bowl and all food positions. Require carry, not transient lift/green pixels/aperture. Confirm low-grasp x alignment after descent; 1cm error can eject a round sprout. Fold only with the complete swept hand path clear of table edge, not just its high start pose.
