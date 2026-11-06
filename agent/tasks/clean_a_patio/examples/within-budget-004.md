# Independent within-budget repeat — patio-speed-004

Native TRAIN10 full-task practice success **Q1 / fraction1 at 10,086 ticks =336.20 simulated seconds**, obs117. Fresh reset, no restores, original retained left broom grasp. Limit18,106ticks/603.533s; headroom8,020ticks/267.333s. Also below15,000tick/500s target. Prior independent003 succeeded at11,541ticks/384.70s; these establish two consecutive fresh-reset within-budget practice completions of this fixed start, not held-out generalization or official scored evaluation.

Evidence: `../speed-004-success.json`, `../speed-004-finish.json`, `../control-action-results.jsonl`. Audit:116 dispatched motor calls, sum10,086ticks; all116 requested positive finite max_steps through budget_control. Two pre-dispatch rejections preserved (unknown gripper intent after reset; invalid Cartesian field `pos`, corrected to `to`). Endpoint wall4214.0s; admin-finish wall4240.8279s. Wall includes native compaction/runtime repair delay; no wall-speed parity claim. Operator reports repair retained same session936e562a/world/attempt without simulator calls/reset/replay/model change. Worker/controller unchanged.

Final receipt: `<observation-cache>/patio-run-027-p6-3b5a95/patio-speed-004/receipt_01792174640698943000_183c629e858a4372b629a8bd2048bc82.json`. Native false at9147ticks/304.9s; true at10086. No earlier first-success-tick claim. Admin finish succeeded at unchanged10086ticks, leaving no active attempt.

## Reusable policy and changes from003

- Separate OPEN insertion and closure. Failed first pickup was corrected by fresh shaft depth; lift verified010/35.50s. Move left.65 BEFORE turning at pickup; stone contacts/reveals013–016 complete50.33s, avoiding003 foliage collision.
- Cover open center, grill/chair edges and two chair/lamp boundary patches before bench sector. Public RGBD selects each target; numeric coverage labels are not particle counts. Broom stroke TCP is fresh patchXY minus approximately[.33,-.10], z.01, down fingers and close_dir[.31,.95,0], capped2s then known-joint withdrawal. Offset is grasp-dependent, not universal.
- Contact-rich chair routing052–054 stopped on velocity mismatch; changed to straight exit rather than repeating blocked directions. After patch14, straight forward through visible chair gap079–081 worked. Grill blocked direct bench route082; entrance-side bypass083–085 recovered access.
- **Raise torso with unchanged/measured arms first, then compact arms.** Combined low→high plus compact at077 caused leftq4 lag.233; measured release/torso-only078 restored tracking, then compact079. Similar measured torso releases093–094 and right-arm release098–099 normalized preload; they do not identify contact objects.
- Tan marks are not orange targets. Two wasted short strokes088/090 on unchanged tan bench-floor marks did not show removal. Do not count them as cleaned; native success later coexists with tan marks.
- Actual bench-front orange strokes095/100/104 and reveals completed by304.9s, native stillfalse. Lateral reach102 missed height by44mm; withdrawal/lateral alignment103 then104 worked. Improve stance rather than force.
- **No deliberate bench move or grasp required in004.** Raised survey107 revealed three orange patches beyond bench. Right-end bypass108 exposed all three; stage high109, lower/forward110, then strokes111/114/116 and reveals112/115/117. Native Q1. This demonstrates a simpler alternate route for this fixed start, not universal no-furniture-motion necessity; incidental chair contact occurred earlier.

## Exact final contacts (observed TRAIN10 episode, not blind replay)

Use `import budget_control as s` with the assigned run/campaign environment. The full116-request sequence and actual robot goals/states are in control-action-results.jsonl filtered by attempt_id. Final newly visible targets at108 were head(u,v)=(290,390), (105,400), (147,343), respectively BODY[1.5693,.3273,-.0051], [1.5153,1.1711,-.0050], [1.8602,1.1236,-.0049].

```python
lowL = [-.34825,.62665,-1.3462,-1.19364,.82925,-.21662,.68141]
lowR = [.2026,-.14358,-.39082,-1.10861,-.26479,-.60613,.51003]
# At raised, clear obs108, stage arms109, then lower/approach110.
s.act(left={'q':lowL}, right={'q':lowR}, timeout_seconds=3)
s.act(torso={'q':[1.75,-1.75,-1.073,0]}, base={'fwd':.55}, timeout_seconds=4)
# Reacquired111 target from110 head(238,334) [1.0407,.32313,-.01607].
s.act(left={'to':[.7107009,.4231305,.01], 'finger_dir':[0,0,-1],
            'close_dir':[.31,.95,0], 'grip':0}, seconds=2)
s.act(left={'q':lowL}, base={'yaw_deg':40}, timeout_seconds=3)
s.act(base={'fwd':.45}, timeout_seconds=4)
# Fresh113 head(234,331) [1.04619,.32967,-.00515].
s.act(left={'to':[.7161926,.42967412,.01], 'finger_dir':[0,0,-1],
            'close_dir':[.31,.95,0], 'grip':0}, seconds=2)
s.act(left={'q':lowL}, base={'fwd':.3,'left':-.2}, timeout_seconds=3)
# Fresh115 head(254,342) [1.016717,.2756343,-.005156].
s.act(left={'to':[.686717,.3756343,.01], 'finger_dir':[0,0,-1],
            'close_dir':[.31,.95,0], 'grip':0}, seconds=2)
s.act(left={'q':lowL}, timeout_seconds=2)
```

After each motor call inspect endpoint and stop/change approach on a miss; these commands are a record, not an autonomous script. At117 torso[1.75,-1.75,-1.073,0], leftTCP[.4,.3,.16], grip0/gap.0328m; rightTCP[.45,-.4,.25], grip1. Public integrated odometry[-3.207,1.531,0], yaw−2.140 is drifting self-state, not absolute pose.117 practice_feedback returnedQ1, then admin_finish preserved same10086ticks. Before/after/contact images are obs0108–0117 in the cache named above.

## Frozen practical core

Retain budget_control and matching run client; no blind trajectory replay. Fresh RGBD at each contact, whole-broom/empty-arm clearance, move clear before turning, separate high/low posture transitions, release all persistent misses, then change route after guard stops. Finish/record native feedback; judge repeatability from fresh resets only. Source8432188/protocol6/controller26efe4a and TRAIN10 remain binding.
