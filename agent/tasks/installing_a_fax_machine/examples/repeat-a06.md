# a06 overhead-route repeat

FINISHED `fax-run-008-v4-a06`: **159.90sim s /4797ticks /1026.0865wall s**. [28 exact public requests/states/images](repeat-a06-exact.md). Same fresh TRAIN instance10 reset and a05 recipe, no snapshots. Green127.13s, release157.27s, withdrawal157.90s, stable159.90s. No visible divider brush/base tilt, no blocked navigation/carry, no recovery actions. Final base[-4.140,-.862,-.001], yaw-2.337. Torso effort~8Nm during turn,~.14Nm final hold.

Together a05(159.2667s) and a06(159.90s) are two consecutive endpoint-visually clean, sub170s completions using overhead carry and direct diagonal placement approach. Not official scorer results; no roll/pitch or continuous transient-tilt certification. Initial navigation z follows floor from0 to-.008 then-.003; no observed base lifting against furniture in either repeat. Brief high torso effort during arm acceleration/deceleration is not contact proof.

Recipe: use a05 instructions. Direct overhead q[-2.6,.05,-.13,-.12,.065,1,-.14] after standing torso[.84,-1.00609,-.42,0], left qzeros. Move fwd.77,left.06, yaw115; lower right shoulder-1.45 then-1.36, release, withdraw-1.65, hold seconds=2. Recheck actual RGB/depth before contacts, not blind replay.

Measured switch left[194,226]=[.596911,-.129087,.282954], near left[245,233]=[.598145,-.128971,.283085]. Table head[420,450]=[1.053260,-.277583,.755319]; head[475,430]=[.860935,-.179768,.755297]. Final receipt /tmp/fax-run-008_obs/fax-run-008-v4-a06/receipt_01792120481591972000_85dd3cc10363440eb27f711d1b0a5a85.json.

Stopped all simulator calls after admin_finish at lead-requested protocol6 handover boundary. No next reset; protocol4 recipe timings are historical and must be revalidated after swap.
