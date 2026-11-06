# First knife grasp — one observed success, not mastery

Practice `brussels-knife-001`, TRAIN10. Matching run client only. Snapshot `knife_aligned_high` resumes just before this sequence (stored native state, do not inspect files). Knife held endpoint snapshot `knife_held_first` after obs37. No cutting yet.

## Evidence and geometry
Cache `<observation-cache>/brussels-run-031-p6-7d6605/brussels-knife-001/`: obs0030 pregrasp, obs0034 preclose, obs0035 pinch, obs0036 lift, obs0037 retreat; corresponding receipt JSON and depth NPZ retained. Blade visibly rises and follows hand across both lift and retreat, stays fixed in wrist view while board moves. Aperture alone was not accepted as evidence.

At obs30 wrist handle selected pixels: (273,210) BODY[.879,-.207,.909]; (280,280)[.854,-.219,.9055]; near bolster (280,315)[.8415,-.2244,.9035]. Board .8831m. Pad midpoint obs30[.837,-.205,.976], fingers down-oblique[.53,.11,-.84], close[-.34,.93,-.09].

## Exact successful continuation
Import run-local sim_client as s. Run serially; inspect each returned image. Earlier stalled pose is deliberately replaced by measured q, not blindly repeated.
```python
s.act(right={'to':[.843,-.205,.925]},intent='Descend toward handle stopping above board',seconds=3,position_tol=.01) # stalled, measured [.830,-.206,.928]
s.act(right={'q':s.last_obs()['robot']['right']['joints']},intent='Release residual reach before final approach',seconds=2)
s.act(base={'fwd':.04},intent='Four centimetre measured approach to place handle inside reachable workspace',seconds=3)
s.act(right={'to':[.833,-.207,.905]},intent='Set pad midpoint to handle-side height above .883m board',seconds=3,position_tol=.01)
s.act(right={'grip':0},intent='Pinch near knife handle bolster at measured pad height',seconds=3) # grip stalls against object; not failure/success proof alone
s.act(right={'up':.10,'fwd':-.04},intent='Lift pinched knife clear of board and verify visible retention',seconds=5,position_tol=.01)
s.act(right={'to':[.69,-.22,1.09]},intent='Retract lifted knife into free space and verify blade remains with hand',seconds=5,position_tol=.01)
```

At obs34 preclose right q[-1.35675,.02323,.54666,-.05597,-.1276,.72614,.36242], TCP[.825,-.207,.907], open pads[.809,-.163,.902]/[.842,-.252,.911]. At obs35 closed fingers[.0189,.0076], TCP[.826,-.210,.908]. Obs36 TCP[.791,-.206,1.011]; obs37[.693,-.223,1.090], fingers[.019,.0076]. Torso throughout[1.025,-1.45,-.47,0]. Base before final4cm: odom[.120,.596], yaw-5.389; afterward[.142,.624],yaw-5.390. Left q zeros/open.

## Approach lessons / not yet a repeatable full-reset recipe
Initial robot faces away. Board turn survey used -35,-70,-75,-75,-45deg (shorter route possible). Ready preset collided with lower shelf on approach; retract/turn45deg into aisle, ready, direct high joint q[-.7,0,-.08,-1.1,0,.05,-.1], then turn back-45deg avoided shelf. Exact downward-axis target saturated wrist; human156s q[-1.1459,-.3544,.5983,-.5185,-.109,.844,.5875] provided workable branch but touched board, corrected by up.08 before lateral alignment. Keep high withdrawal before changing branch. This grasp is near bolster and blade points back toward robot; reorient only in free space before cutting.
