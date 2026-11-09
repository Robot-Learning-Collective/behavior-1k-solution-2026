# One left knife acquisition and blade orientation — TRAIN10

**Evidence: one observed success, NOT repeatability or a safe blind-replay recipe.** Native cutting subsequently errored; no slice/dice success claimed. Match READY run-local source8c7cca8/protocol6, current images and depth before each movement. All positions BODY metres. `act()` only; await and inspect each result. No automatic trajectory replay.

## Initial conditions
Practice restore of `cabbage-on-board-001`, attempt `practice-restore-cabbage-on-board-001-3bcda51a0e0e47509ca5120b3c9dcbc4`. Cabbage on board, chili staged on other counter. Knife beside microwave. Right approach previously interfered and damaged scene; preserved and restored. Left first closure also missed; this success followed a5cm closer base adjustment and lower handle-middle alignment.

At obs012: base odom[.061,-1.151],yaw3.266 (drift-prone); torso command[.7293,-.9093,-.3357,-.0003]; right empty/home/open. Left empty/open and elevated. Knife handle fresh geometry near[.80,.20,.897] after approach. Do not use this pose on another base/scene state.

## Acquisition
1. Left q `[-1.14,0,-.1559,-.3009,.2932,.8093,-.044]`,seconds4, open retained. Obs013 reached TCP[.797,.205,.904].
2. Replace left target with current measured q and close `grip:0`,accept_partialtrue,seconds2. Obs014 fingers1.7cm; closure alone is not proof.
3. Left q `[-.637,.25,-.0309,-1.3973,.2585,.8512,-.2432]`,seconds3. Obs015 reached[.765,.279,1.035]; knife visibly followed and remained between fingers. Save `knife-held-left-001` (saved).
4. Measured left q0−.25,seconds2. Obs016 reached[.821,.279,1.185], knife retained clear above surface.

## Orientation from RGBD, not guessed mirrored roll
On obs015 wrist view, handle pixel(u210,v300), blade(u170,v50); blade edge(u140,v50), spine(u230,v50). Obtain each from `s.xyz('left')[v,u]`. Normalize length `a=blade-handle`; orthogonalize edge `b=edge-spine-a*dot(a,edge-spine)`, normalize. Current blade frame `C=[a,b,cross(a,b)]`. Desired frame `D=[+Y,-Z,-X]` gives `Q=D@C.T`. Apply Q to measured hand finger and closure axes to obtain desired axes. This uses only public observed surfaces and rigid self-state; no hidden object pose.

Target left `to=[.72,.26,1.20]`, `finger_dir=[.81348,.57874,-.05753]`, `close_dir=[-.19035,.17146,-.96663]`,seconds4. Obs017 TCP[.720,.265,1.200], shoulder-limit stall5mm off; knife retained. Fresh wrist depth verifies blade axis[-.007,1,.010], edge[.002,.010,-1]. Simply mirroring demonstrated right roll would have pointed edge upward.

## Precut and failure boundary
- Head depth cabbage top[.5485,.3576,1.0384]. Left to[.55,.25,1.12],seconds4 reached obs018; saved `knife-precut-cabbage-001`.
- Left to[.55,.23,1.055],seconds2 reached obs019; q5 at lower limit.
- Further to[.55,.23,.995],seconds2 returned unrecoverable `simulator_error` after0.1sim seconds at obs020/sim296.30. Cabbage absent in final RGB; no claim about cause or completed cut. **Stop here; do not retry.** See NOTES for exact receipt and operator blocker.

Saved native attempt receipts contain every endpoint. Recovery snapshots preserve pre-cut states, but restore requires operator resolution of the current unrecoverable runtime fault.
