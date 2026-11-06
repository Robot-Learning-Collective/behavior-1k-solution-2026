# Knife return to board — first successful placement

From `knife_held_first` (see knife-grasp-001.md), own TRAIN10 only. Exact continuation:
```python
s.act(right={'to':[.81,-.21,1.02]},intent='Return held knife above its observed board patch before setting down',seconds=5,position_tol=.01)
s.act(right={'to':[.82,-.21,.911]},intent='Lower held knife onto board at measured support height',seconds=5,position_tol=.01)
s.act(right={'q':s.last_obs()['robot']['right']['joints'],'grip':1},intent='Release supported knife on board without persistent preload',seconds=3)
s.act(right={'up':.15,'fwd':-.10},intent='Withdraw empty hand from placed knife before navigating',seconds=5,position_tol=.01)
```
Board depth .8831m; handle surface .905m. Pre-release obs39 TCP[.815,-.206,.913], q[-1.39124,-.19098,1.65796,-.51305,-1.4854,.7079,-.02752], pads [.810,-.191,.911]/[.817,-.211,.914], grip0. Torso[1.025,-1.45,-.47,0], base odom[.143,.624],yaw-5.390. Obs40 explicitly open both fingers .05m; obs41 empty hand TCP[.720,-.212,1.063], knife remains visibly supported on board. Cache brussels-knife-001 obs0038–0041 images/depth/receipts. One success, not repeatability or task completion.
