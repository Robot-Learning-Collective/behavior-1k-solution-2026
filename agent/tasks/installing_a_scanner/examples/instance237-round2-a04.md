# TRAIN237 round2-a04 — Q1, closer placement

Fresh native reset on e361cf/a47213f, no restores. Reset setup343.016458176s separately. Native finish2257steps /75.233333sim /517.071619070wall, both toggled_on and nextto true. Round2 completed denominator2/4 (Q1,Q0,Q0.5,Q1). First acquisition retained through lift/withdrawal/carry; first press green. Familiar TRAIN237 only, not held-out reliability.

## Geometry-gated acquisition
BASE-only draws-.25/-.16; front head[395,500]=[1.0754,-.2488,.7901], true desk samples[380,370]=[1.1282,-.0204,.7649],[425,630]=[1.0300,-.4692,.7649]. Chose final-.06 from apparent near-zero overhang, not a universal recipe. Withdrew-.30 before rotation/opening, returned+.30. Align[1.015,-.24,.785], shallow insert[1.092,-.24,.785], close achieved joints, lift[1.089,-.236,.94], withdraw-.25/yaw-30. Retained visibly.

## Closer placement
Fresh laptop near edge head[215,590]=[1.8064,-.7730,.7877], support[230,550]=[1.7469,-.6250,.7650]. Scanner right visible edge head[300,650]=[1.0980,-.3921,.9811] while TCP≈[1.09,-.236,.935]. Base+.43; carry[1.19,-.59,.94] (more lateral overlap than a03-.54), lower[1.19,-.59,.835]. IK stalled at TCP[1.181,-.579,.839], no unresolved transport. Replaced target with measured q[-1.31934,-.63482,.48709,-.04732,-2.03157,.59843,.82511]. Open, level backout[.98,-.579,.839], raise[.98,-.579,.98]. Scanner changed attitude/slid slightly during settling/backout, then appeared stable beside laptop. No zero-displacement claim. Yaw-20 and base+.18 for switch.

## Switch and endpoint
Fresh right[154,55]=[1.2995,-.3388,.8231]; after high stage, right[110,235]=[1.2984,-.3416,.8227]. Close empty hand, stage[1.299,-.339,.89], press.815; green on first press, blocked at measuredZ.838. Immediately clear[1.15,-.20,1.02]. Final supported pose visually unchanged through press/clear. No robot tilt observed; odometry cannot prove tilt.

Final receipt: `<observation-cache>/scanner-run-007-p6-e361cf/scanner-run-007-instance237-round2-a04/receipt_01792156169666198000_f0b49c0b30a6424b829b9c2d96e05458.json`.

Next: repeat fresh geometry-gated acquisition and smaller-gap placement; do not turn successful TCP into a blind template. Placement rotation remains a weakness even when native nextto succeeds.
