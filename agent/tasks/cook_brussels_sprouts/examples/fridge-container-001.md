# Refrigerator opening and high-shelf container pickup — single practice success

TRAIN10, native protocol6. No repeatability or full-task claim. Observations in attempt `practice-restore-fridge_open_first-6d9239691be04e30babed34acde97902`.

## Open door wide before reaching
Partial opening repeatedly caused arm/torso loading and accidental door closing during high-arm transitions. Better: after handle opening, use closed fingers against inner door face, not constrained handle pulling.

At snapshot `fridge_open_first`, torso `[1.025,-1.45,-.47,0]`, base odometry approximately `[1.761,5.113]`, yaw `-5.395` (drifting estimate only):
- A direct Cartesian reorientation to [.43,-.12,1.1] failed at joint limits. Do not reuse.
- Offline IK q `[-.26284,-.21326,.68478,-2.03574,-.33848,.47656,-.81509]`, grip0 put TCP `[.6,-.15,1.05]`, fingers forward, closing left-right.
- Move `[.55,.02,1.0]` around door free edge, then `[.73,-.035,1.0]` inside, then `[.73,-.32,1.0]`, then `[.73,-.58,1.0]`. Door visibly opened wide, negligible final lag/effort.
- Withdraw `[.63,-.15,1.0]`, fold q0/open. Snapshot `fridge_wide_open`.

These are same-scene examples, not collision-safe universal replay. Reinspect door geometry and endpoints each time.

## High-shelf rim pinch
Container rim ~1.56m; shelf ~1.44m. Raise torso `[.45,-.4,-.22,0]`, then right q `[-1.66569,-.08835,.90301,-1.48927,-1.81021,-.88256,-.86839]` reached `[.798,-.08,1.55]` in free space. Advance base .18m with elevated hand.

Forward-up fingers `[.96,0,.29]`, vertical-ish closing `[-.29,0,.96]` repeatedly failed thin-rim pinches and moved container back: lower finger leads into wall. Empty aperture plus failed object-following test rejected these grasps.

Successful correction:
- Withdraw to `[.85,-.11,1.58]`.
- Set `[.85,-.11,1.56]`, `finger_dir=[1,0,0]`, `close_dir=[0,0,1]`, grip1. Horizontal fingers avoid lower-finger leading offset.
- RGBD measured protruding lip ~[.974,-.120,1.559], outer wall ~[.995,-.116,1.547].
- Advance base .05m (actual ~.045), then right TCP `[.933,-.12,1.557]`.
- Close grip0. obs24 measured fingers `[.0162,0]`, pad positions z1.570/1.559; closure stalled on object, not proof alone.
- Lift to `[.91,-.12,1.607]`: obs25 container visibly lifted clear of shelf and followed hand. Snapshot `container_rim_lifted`.
- Base retreat .5m, then lower hand `[.78,-.12,1.30]`: obs27 container remained held and followed; fingers `[.0168,0]`.

Latest obs27 carrying q `[-1.09157,-.21464,.87172,-1.69172,-1.76357,-.87737,-.74855]`, torso unchanged. Contents not yet independently visually verified after extraction. Fridge remains open, knife remains on board. No cutting/cooking yet.
