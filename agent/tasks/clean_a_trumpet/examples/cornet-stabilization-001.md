# Cornet mouthpiece stabilization — observed success, not reset-repeat mastery

Run trumpet-run-026 / attempt trumpet-practice-001 / TRAIN10 / protocol6.

## Verified renewed top-down pickup (obs204–208)

Torso `[.734,-.755,-.4,0]`; base integrated odom approximately `[1.548,-.525,0]`, yaw1.582. These are episode-specific, not world coordinates. Right retains brush and is raised/clear.

1. Direct Cartesian approach failed at shoulder/wrist limits (obs203). Choose reachable elbow branch rather than repeating the same request:
   `left q=[-1.8,.04322,-1.95724,-.9,.45215,.47436,-.96611]` → measured TCP `[.809,.061,.948]`.
2. From RGBD mouthpiece about `[.739,.092,.846]`, align left TCP `to:[.74,.09,.87]`, `finger_dir:[0,0,-1]`, `close_dir:[1,0,0]`, grip open.
3. Down `.035m` → measured TCP `[.740,.086,.836]`.
4. Close at measured q (`grip:0`); fingers ~`[.0458,0]`.
5. Lift `.11m`; **cornet visibly follows** (obs208). Hold measured q to discard residual target (obs209).

Obs208 receipt: `<observation-cache>/trumpet-run-026-p6-509a09/trumpet-practice-001/receipt_01792159932250627000_af7f33c6662a44098ffce5868a82034c.json`.

Earlier top-down clamp obs67 also retained cornet after a small lift. The later pickup uses a changed object pose/base/torso and is not a clean identical-reset repeat. An earlier side-entry closure obs150 was empty; later side-entry obs157–160 did retain after forward torso lean. Finger asymmetry alone never established retention.

## Presentation and failure lessons

- Unsupported back-loop brushing obs193–199 moved cornet toward desk edge. Stabilize before repeated localized passes.
- Lift brush before rotating cornet. +55° left pitch exposed a black back-loop patch near `[.787,-.139,.952]` atobs214; sampled prior top views hid it.
- Brush heel/fingers and valve buttons can obstruct face contact. Long crossing requests and reversed brush yaw introduced forearm collision/limits.
- To recover crossing approach, release measured q, raise brush, then move cornet forward/up; useful obs228–234, but **goal remained false**.
- Requested pitch is not achieved pitch. Left further positive rotation stalled at wrist upper bound; negative rotation later stalled at shoulder/wrist limits. Accept actual pose with explicitly legal endpoint q before changing approach.
- Black patch was no longer visible from sampled face after obs237, but native feedback atstep8865 remained false/Q0. No complete cleaning claim.
