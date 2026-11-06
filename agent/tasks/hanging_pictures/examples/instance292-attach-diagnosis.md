# Public RGBD attachment comparison: TRAIN280-a05 vs TRAIN292-a03

292-a03 acquired/carry retained after correcting the approximately64deg pickup orientation mismatch, but failed hanging. No privileged live geometry used.

- Pre-seating poster plane normals:280 obs22 `[.71953,-.69275,-.04881]`;292 obs37 `[.72271,-.68932,-.05018]`. Orientation transferred closely before the later failed reseating.
- Approximate manually sampled black top-edge midpoint minus nail BODY:280 obs22 `[-.02291,-.02674,.02284]m`;292 obs37 `[-.05300,-.03554,.01789]m`. 280 nail propagated from visible obs15;292 nail back-propagated from visible post-release obs48. These are approximate: pixel selection and integrated planar odometry contribute uncertainty; not calibrated ground truth.
- Independent292 consistency check: visible nail29 propagated to48 predicted `[.96516,-.04808,1.70405]`; measured48 `[.99185,-.04220,1.70583]`. Residual `[.02668,.00587,.00179]m` across route/seating. Thus the one distant calibration plus long base approach is insufficient for millimetre attachment. Sources include odometry and pixel correspondence; causality not established.
- At292 obs46 after additional lowering, approximate top−nail `[-.04777,-.04991,.00150]m`; plane `[.75795,-.64490,-.09808]`, no snap and release dropped. Lowering without re-grounding did not fix attachment.

## Native follow-up a04

Q1/2026steps/67.5333sim s after local re-grounding, with full release/withdraw/lower retention. At close calibration nail `[.99185,.00914,1.70578]`, target top `[.94717,-.00147,1.73583]`; required translation only `[.07013,.03108,.21624]` rather than a03's far-view `[.66219,.30384,.11150]`. Plane correction≈`[-2.13,-3.16,-1.92]deg`. Snap at obs31, immediate release32, retention34. Changes also included clear-floor routing/base-yaw timing; do not claim single-variable proof.

## dev11 public endpoint comparison

Source `pictures-eval-001/actor-receipts` (Astra msg302), local cache `<observation-cache>/pictures-dev11-public`; downloaded public receipts and selected RGBD files individually verified against supplied SHA256 manifest. No actor reasoning/private transcript/scorer read. Lead reports officialQ1/104.5sim s; final public call says episode_ended after9ticks, not a complete hold or released-retention test.

Unlike292, dev11 had a flat poster, failed insertion then recovered a fallen frame with a top pinch. Public actions explicitly changed pinch axes and wrist orientation; its final wrist configuration is not a replayable292 seed. Head frame is partly cropped but wrist nail remains visible. RGBD plane fits: obs3036 normal `[.83380,-.52117,-.18209]`, nail-to-front-plane gap≈127.5mm; obs3127 normal `[.83565,-.52127,-.17311]`, gap≈38.4mm. These are nail-to-fitted-front-plane distances, NOT wall stand-off/contact proof; hand-selected ROI/pixel uncertainty applies. Last act combined≈20mm base normal motion and15mm arm lowering, but termination truncated execution. This supports object/nail visual re-grounding rather than enforcing a single fixed tilt or copied joint target.292-a04 already succeeded with a different grasp and smaller tilt before this comparison.

Next native run: repeat the newly successful local re-grounded procedure; retain oblique pickup; use clear-floor route avoiding known blocked segment; resolve large wall-yaw mismatch with base rather than wrist; approach near target with poster low enough to see nail, then perform fresh local RGBD alignment. Avoid relying on far-view integrated displacement. Re-select actual outer black edge consistently and inspect increments. Score only at finish.
