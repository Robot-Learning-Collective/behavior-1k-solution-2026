# Initial trunk lift — partial success, not mastered

TRAIN10, car-practice-001 obs31–37; replay from own immutable `frontal-trunk` snapshot after restoring and observing. No full-open or repeatability claim. Original RGB+self-state receipts in `<observation-cache>/car-run-024-p6-8dae5a/car-practice-001/obs_0031..0037*` and corresponding receipt JSON; exact targets/results also in `control-action-results.jsonl`.

Base odom approximately[-1.049,2.692], yaw0.312rad; torso[1.025,-1.45,-.47,0]. Both grips open. Trunk upper lip from head RGBD: pixel(290,460) BODY[.733,.140,.967].

From stowed: first left q human72=[.445,-.027,.163,-1.323,.238,-.560,-.063], grip1. Do not jump straight to74 (self-collision observed).
1. left q[-.042,-.112,-.098,-1.549,1.01,.127,-.555], grip1. Measured TCP[.592,.101,1.006].
2. left q[-.2822,-.0997,.0322,-1.2625,1.0953,.1274,-.4893], grip1. TCP[.686,.161,.981], pads[.705,.173,.939]/[.666,.148,1.023]. Finger dir[.90,-.27,.33], close[.40,.26,-.88].
3. left fwd .035, left -.015, seconds1. TCP[.719,.145,.983], pads[.739,.157,.941]/[.700,.132,1.024]. No gripping: hook with open finger.
4. left to[.703,.14,1.07], finger_dir[.8,-.31,.52], close_dir[.6,.26,-.76], seconds2. Stalled at TCP[.693,.139,1.038]; lid visibly begins rising. This is intentional contact, not a pose success.
5. left to[.66,.13,1.16], finger_dir[.67,-.38,.64], close_dir[.73,.19,-.65], seconds2. Reached TCP[.661,.129,1.159], visible black opening below lid. Saved snapshot `trunk-initial-lift` here.

Human13003 source study: open grip throughout. 77.5s→79s hand goes up .089m/back .018m and curls fingers upwards. Our +35mm geometric correction was necessary for observed coupling. Subsequent horizontal two-hand support/torso raise did NOT fully open: lid fell closed. Do not treat that continuation as recipe.
