# Broom pickup: successful local correction, not reset replay

Attempt patio-probe-001. Starting obs32 after several misses and shifted broom. Base odom [1.580,-4.108,5.158rad]. Torso[1.75,-1.75,-1.073,0]. Left finger direction down, closing direction [.81,.59,0]. Both grippers initially open. Right arm idle command [-.34947,.05008,-.08019,.33,-.00062,.05,-.1]; was loaded while crouched, resolved on torso raise.

1. Wrist depth obs32 shaft pixel(110,250)=[.4349,.3135,.0240]; pixel(140,300)=[.4215,.3226,.0231].
2. `s.act(left={'to':[.467,.30,.04]},timeout_seconds=4)` horizontal insertion, obs33. New shaft pixel(270,220)=[.4713,.2849,.0256].
3. `s.act(left={'to':[.45,.30,.03],'grip':0},timeout_seconds=3)` obs34. Measured TCP[.450,.300,.032], q[-.51578,.17714,-.52793,-.40036,-.40423,-.09044,.18979], fingers[.0344,0]. Pads[.476,.318,.032]/[.452,.301,.032].
4. `s.act(left={'up':.15},timeout_seconds=4)` obs35. Entire broom rises against fixed stone; TCP[.451,.300,.182], fingers[.0345,0]. q[-.03427,.56551,-.66534,-1.46593,-.15378,.41560,.26410].
5. `s.act(torso={'q':[1.025,-1.45,-.47,0]},timeout_seconds=5)` obs36. Broom retained TCP[.539,.300,.746].
6. Two separate `s.act(base={'yaw_deg':90},timeout_seconds=8)` obs37/38. Broom retained. Depth-checked clear grass around turn; not universal safe route.

Images/depth: obs_0032 through obs_0038 in `<observation-cache>/patio-run-027-p6-3b5a95/patio-probe-001/`. Exact full receipt paths and action IDs in control-action-results.jsonl.
