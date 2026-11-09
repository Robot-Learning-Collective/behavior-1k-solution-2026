# Thin brush pickup — one successful drill, not yet repeated

Evidence attempt: `practice-restore-aligned_top-338d40cd711b4580bad3dc5c78e7693a` under `/home/b1k/practice/obs/scrub-run-01_obs/`. Images/receipts obs0001–0007. Practice snapshots `aligned_top` (pregrasp), `brush_held` (after retention).

Precondition: brush bristles-up on floor, measured center about [.525,.215,.015], long axis X; floor z=-.0052. Base odom[-.077,.183], yaw2.355. Left initially at [.523,.215,.071], finger down, close Y; torso[1.68,-2.54,-1.62,0]. Right open at [.253,-.27,.123]. Both grips already explicitly open. Reground all coordinates on new instance.

Exact successful sequence:
```python
s.act(intent='Clear right and increase floor reach while retaining left pregrasp',torso={'q':[1.78,-2.54,-1.62,0]},left={'to':[.525,.215,.07]},right={'to':[.35,-.25,.22],'finger_dir':[0,0,-1],'close_dir':[0,1,0]},timeout_seconds=4)
s.act(intent='Controlled vertical descent first 2cm',left={'to':[.525,.215,.05]},timeout_seconds=2)
s.act(intent='Controlled descent to 3cm',left={'to':[.525,.215,.03]},position_tol=.002,timeout_seconds=2)
s.act(intent='Final short descent to 15mm rim height and close',left={'to':[.525,.215,.015],'grip':0},position_tol=.002,timeout_seconds=2)
s.act(intent='Test thin-rim grasp with vertical lift',left={'to':[.525,.215,.12]},timeout_seconds=3)
s.act(intent='Verify retained brush during 6cm lateral carry',left={'left':.06},timeout_seconds=3)
```

Measure wrist brush before each descent. obs0004 left xyz[280,240]=[.52657,.21742,.01527]. Close endpoint obs0005 reported stalled (2.45mm residual vs2mm tolerance), but close HAD executed and aperture became asymmetric [.0466,.0035]. No need to reclose: lift succeeded and brush visibly followed. Brush depth after lift xyz(left)[260,150]=[.54283,.23144,.12226], confirming ~10cm lift, then6cm lateral carry retained it.

Key obs0005: TCP[.525,.213,.016], pads[.524,.256,.015]/[.525,.211,.016], left q[-.84161,.23018,-.87642,-.8495,1.0666,.48324,.46909], grip0. obs0006 TCP[.525,.213,.119], q[-.62635,.34442,-.65116,-1.49373,1.18256,.78103,.86379], same aperture. obs0007 TCP[.525,.272,.119], q[-.61019,.48971,-.6127,-1.49996,1.18815,.78439,.7229], pads[.525,.316,.118]/[.525,.271,.119]. Torso unchanged1.78/-2.54/-1.62/0; right q[-.11687,-.70024,.82048,-2.01805,-1.13691,.39969,-1.01808], grip1. Base[-.076,.183], yaw2.354.

Duration4.1sim seconds from aligned snapshot, including torso adjustment, pickup and lateral retention test. Crucial difference from failures: correct deeper torso with right hand cleared; small staged vertical descent, NOT large descent from far away. Top closes at z.04–.05 were empty. Brush still bristles-UP: wiping orientation remains unsolved.
