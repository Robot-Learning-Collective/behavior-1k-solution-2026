# Observed pickup + switch sequence, protocol4 a01
Not a blind replay recipe. Live images/depth guided coordinates. One success, repeatability/fast mastery not yet established.

## Approach
Reset initial facing wall. Base: yaw-90, fwd1.0, fwd.8, yaw-90, left.35, fwd1.2 twice, yaw-70, left.9, left.2, fwd.95, fwd.25. This exploratory path has avoidable turns. Final base rel[-3.825,-1.537], yaw1.952. Fax visible on floor in middle cross aisle, long direction BODY-X, width~.08m. Setup10 specific.

## Reach and pickup
Raise hands before crouch: right to[.50,-.27,.65], left to[.45,.28,.75]; torso low then deeper q[1.68,-2.54,-1.62,0]. Default low insufficient for floor reach: right IK stalled ~.52,-.31,.26. Deep torso resolved reach.
Right to[.59,-.33,.15], finger_dir[0,0,-1], close_dir[0,1,0]. Wrist depth confirmed fax surface~.04m, lateral bounds roughly-.30..-.38.
Descend right to[.59,-.35,.035]: stalled at[.584,-.346,.050]. Replace with measured q[-1.14578,-.18576,1.09515,-.0436,-1.04176,.39989,.15983] + grip0, achieved. Right to[.584,-.347,.20]: object visibly followed .15m lift, wrist view retained fax. Then to[.53,-.15,.23], later[.50,-.08,.23]; retained throughout.

## Switch
Naive downward left orientation cross-body hit joint2 limit. Human86s orientation quaternion[-.062,.912,-.395,.094] solved left reach: finger_dir[.220337,-.708506,-.670426], close_dir[-.038811,.680406,-.731807]. Close left hand before press.
Flat fax attempted presses at observed button [.635,-.191,.222] then [.606,-.128,.222] were blocked; red remained. Withdraw and release pressure before changes.
Key improvement: tilt retained right wrist pitch_deg35 (right TCP~[.501,-.081,.231], finger_dir[.57,0,-.82]). This raises/presents button toward left fingertip, analogous human held-fax rotation.
Measure red button with left camera: [.5937,-.1195,.28385]. Left to button+[-.01,.015,.02] achieved precontact [.583,-.104,.304]. Remeasure red button [.59583,-.12041,.28449]; left to button+[.003,-.004,-.005] max_steps8. Returned no_progress/blocked at TCP[.593,-.132,.291], but RGB shows GREEN. Thus pose failure is not task-effect failure. Withdraw left to[.61,-.04,.36], achieved and green remained.

Evidence: /tmp/fax-run-008_obs/fax-run-008-v4-a01/ obs1055 lift,1084 retention,1465 red→green,1481 withdrawn/green; full action records run control-action-results.jsonl. Current sim193.97s, right still holds tilted fax, left safely withdrawn, no pending prerequisites. Need place and repeat pickup/switch efficiently, no mastery claim yet.
