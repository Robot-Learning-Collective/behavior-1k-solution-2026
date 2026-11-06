# One empty-sheet grasp/carry/release — TRAIN10, after frozen package capture

Same corrected-sourcea32648a attempt; public RGBD/self-state only. Human comparison: [tray study](tray-human-study-004.md). No loaded-sheet/oven success or independent repeat.

## Approach failures and changed geometry
- Obs148: requested backward.4 from board stance stopped after≈.218m: `base_velocity_tracking_mismatch`, triggered=true. Did NOT retry. Counter behind became visible after changed heading. This is velocity mismatch evidence, not calibrated collision/tilt proof.
- Direct arm-fold interpolation would sweep below steel while still over table. Instead raised shoulders along inspected upward arcs (leftq0−4/rightq0−2), turned into aisle, folded. Public model sampled TCP path does not certify full-arm swept clearance. No uncertainty/fault; folded byobs152.
- Moved along visible aisle and faced sheet. Torso[.45,−.4,−.15,0]; own IK, not human joint replay. Elbow-first raising avoided low table-edge sweep: leftq[0,0,0,−1.42,0,0,0], then own stagingq[−.76489,.12113,−.06406,−1.41895,1.40502,1.02974,1.35070], measuredTCP[.701,.300,1.049], finger[.50,.10,−.86], close[−.44,.89,−.15]. Wrist margin only7mm-equivalent0.007rad, so not robust/universal preset.
- After stance alignment, short rim measured in left depth: topz.8856 vs steel.8616. Near short-edge segment ran approximately[.787,.332]→[.859,.370]. Farther overhead target[.845,.365,1.02] IK-stalled at[.830,.363,1.025] without large lag; canceled target, moved stance forward.065, remeasured.
- Near-rim alignment[.780,.357,.970] reached; lower[.780,.357,.891] IK-stalled at[.769,.355,.898], q4≈−.046 (almost straight), not physical contact proof. Did not force farther. Explicit measured-q close tested current observed rim engagement.

## Verified empty-sheet retention and placement
- Obs163 close: fingers[.0196,0], measuredTCP[.770,.352,.900]. Aperture alone not proof.
- Obs164 lift[.74,.357,1.10] measured[.741,.357,1.099], sheet visibly lifted and retained. Obs165 raise[.78,.357,1.22] measured1.219, q7 margin.04rad. Sheet bottom cleared bowl for carry.
- Obs166 lateral base carry fwd−.05,left−.90; actual baseodom[−.220,1.268], yaw+.047. Sheet visibly retained through carry, not a transient lift. Further base−.10/−.10 positioned above clear steel left of board; timeout was caller_step_limit/baseguardfalse, residual base goal replaced with zero displacement.
- Obs168 lower[.74,.357,.920] reached[.738,.358,.921]. Obs169 targetz.891 blocked at[.744,.346,.900], q4lag+.026, torsoeffort59Nm (not force calibration). Released downward preload with actual measuredq and grip1, no repeat/deeper forcing.
- Obs170 open; obs171 withdraw[.74,.357,1.10] reached[.741,.358,1.099]. Sheet remains flat on steel immediately left of board, no bowl/food overlap visible. Both hands empty/open. Knife remains right steel. Seven halves board (overlap), one steel beside board; no halves transferred yet.

## Exact receipts
Cache namespacebrussels-run-031-p6-efb2d9, attemptpractice-restore-recovery_container_carry-fd61d378358448deba8fd30124c4e475:
- guard148: receipt_01792175024730012000_e960831715994cec924d4e1ac5f181f3.json
- close163: receipt_01792175544272176000_cacd4b649cfe40eb93872f66da447f9a.json
- lift164: receipt_01792175555971316000_5f0bd706bfd740ed95620d894574c84a.json
- carry166: receipt_01792175592587171000_ce4dcfa2c8914cda8a5c037eedc22f03.json
- release170: receipt_01792175654868580000_4d2004f3ceff4352aac4305ca03856e6.json
- withdraw171: receipt_01792175664604482000_454af1d4de01483d81c488a336cfc1ea.json

Currentobs171/sim312.73, baseodom[−.311,1.168],yaw+.047; torso[.45,−.4,−.15,0]. Lq[−1.19606,.66598,−.92880,−1.25537,2.08956,.55869,1.14485], rightfoldedq0. All numerical targets are historical evidence, not portable macros. Main transferable mechanism: local rim-normal pinch with slight down-forward fingers; verify lift AND carry, clearance above obstacles, supported release AND withdrawal. Thin-rim success here does not erase earlier shallow-container slips or prove loaded-tray handling.
