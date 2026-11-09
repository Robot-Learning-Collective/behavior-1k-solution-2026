# Retained panel wrist-branch reorientation — TRAIN10

## Evidence
Second successful reorientation: `practice-restore-carried-door-near-cabinet-36da4748a63e4a33a9e5f3235ce5cd10`, obs18–25, sim92.833→98.100 =5.267sim s for7 inspected arm goals. Door retained throughout and later native attachment succeeded. First successful reorientation used a detour through a stalled Cartesian branch; this improved path omits it. One execution of shorter path, not broad reliability.

## Precondition / clearance
After cabinet tip, raise torso[1.025,-1.45,-.47,0], keep left grip0. Right ready/open. Move right total.7m via inspected.3,.4; then back.18 BEFORE yawing panel (earlier trial needed back.18 to recover environmental blockage). Sideways movement displaced the nearby chair despite achieved base tracking; not a collision-free route claim.
Starting base odom[.385,-.728],yaw-5.989; L TCP[.502,.187,.848], Fdown[0,0,-1], C[.72,-.7,0], grip0, q0 below.

Offline FK sampled approximate retained panel corners using F[-.01,.47]m and hand-X[-.025,.225]m. Four-quarter initial path estimates minX≥.44 and minZ≥.33, above cabinet rim. This is NOT collision checking; each actual endpoint was inspected, and native joint tracking checked. Model-generated solutions can still hit walls/chairs or self-collide.

## Exact verified path
```python
q0 = [-1.03388,.54529,-1.33942,-1.66169,-.48348,.29445,-1.52716]
qu = [-.82004,.76749,-.81012,-1.23156,1.50615,1.0272,.53836]
qh = [.11953,.2051,.06719,-1.19977,1.73911,.13551,-.51735]
qd = [-.23349,-.01685,.28569,-.90476,1.73956,-.43167,-.54124]
# Actual separate inspected calls, seconds2 each:
# q = .75*q0+.25*qu
s.act(left={'q':[-.98042,.60084,-1.207095,-1.5541575,.0139275,.4776375,-1.01078]},seconds=2)
# q = .5*q0+.5*qu
s.act(left={'q':[-.92696,.65639,-1.07477,-1.446625,.511335,.660825,-.4944]},seconds=2)
# q = .25*q0+.75*qu
s.act(left={'q':[-.8735,.71194,-.942445,-1.3390925,1.0087425,.8440125,.02198]},seconds=2)
s.act(left={'q':qu},seconds=2)
s.act(left={'q':[(a+b)/2 for a,b in zip(qu,qh)]},seconds=2)
s.act(left={'q':qh},seconds=2)
s.act(left={'q':qd},seconds=2)
```
Intermediate qu TCP[.652,.404,.850], F[.41,.02,-.91], C[0,1,.02], q6 only.006rad measured upper margin: do NOT command more outward. qh TCP[.55,.351,.801], F[1,0,0],Cdown. Final qd TCP[.599,.451,.797], F[.74,.67,-.01],Cdown; handle side visibly up; finger sum.009m. Final q5lag.020 still within achieved tolerance; never interpret retained grip solely from aperture.

Direct qu→qd offline sweep extended panel forward toX1.224 at wall-side Y~0, so used qh intermediate instead. This avoids a concrete geometrically identified risky sweep, not a global collision guarantee.

Image receipts (same own cache attempt): start obs18 `receipt_01792158490962273000_93046bbc1ab94dc386f2245bde8947a2.json`; qu obs22 `receipt_01792158547299463000_9a7aef0164ce4083a971e4173d49d479.json`; qh obs24 `receipt_01792158594882081000_4b5a7cbb7b274101b977ba7727e85f2e.json`; qd obs25 `receipt_01792158611238648000_c59ef8e93ee642bd8c11f28373cbf4cf.json`.

## Placement following this path
Basic crouch T[1.4505,-2.227,-.818,0] gives L TCP[.568,.450,.581]. Remeasured door nearD[.5555,.4794,.5808],C[.703,.2872,.5832]; cabinet nearB[.7332,.3997,.2532] (only2 rim-filtered samples; lower confidence), nearA[.8995,.2017,.2549] (16samples). Commanded base fwd.19,left-.08 BEFORE deeper crouch, avoiding earlier chair-height obstruction.
Empty right ready arm then showed q2lag.061 from chair-side obstruction. Changed right q[-.65,.14,-.08,-1.1,0,.05,-.1], which raised/adducted hand to[.775,-.232,.803], tracked; no force claim. Then final two coupled torso/left goals and release from aligned-release.md, omitting failed1.8torso goal, succeeded. Door visibly seated during final lowering before release; native feedback was checked only after release, so exact predicate transition tick unknown.
Second continuation finish: attached=true/Q1, step3104, sim103.4667 (restored66.4333, +37.0333sim s), wall564.3025s. `../attachment-continuation-repeat.json`. These are checkpoint-continuation times, not full episode scores.
