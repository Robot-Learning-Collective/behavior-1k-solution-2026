# fax-run-008-v4-a01: first public-visual episode completion

Follow pickup/switch example in `pickup-switch-v4.md`. Single exploratory completion, NOT repeatable mastery or official evaluation certification.

## Outcome
obs2671: opened right gripper to1. obs2676: withdrew open hand; green switch visible, fax keypad-up on carrel. obs2689: remained supported and green after2 additional simulated seconds. Finished honestly via admin_finish,357.533333sim s /2885.994712wall s. No hidden state queried.

Final receipt `/tmp/fax-run-008_obs/fax-run-008-v4-a01/receipt_01792113901789528000_1eefb81b41524a3bb40b068b1813fe95.json`. Full requests/results remain in run control-action-results.jsonl.

## Useful placement trajectory (scene-specific, remeasure on replay)
- Chair moved with left hand, but forward base motions repeatedly stalled/tilted robot. Backoff.15m restored base height once. Final robot still tilted/base z+.041m; not good navigation mastery.
- Human joint branch avoids near-body high Cartesian target's wrong elbow-folded IK branch. At torso tall, right q[-1.55,.05,-.13,-.12,.065,1.,-.14] gives TCP approximately[.911,-.241,.970], fax retained.
- Raised fax, advanced .25m request (only~.15 achieved), turned left40deg, advanced .2m request (only~.13 achieved). Leftward alignment was more useful than attempting to cross right arm's inner shoulder limit.
- Lower shoulder q1 from-1.55 to-1.43; attempted right to[.92,.03,.84] hit shoulder joint2 limit, reaching[.852,-.182,.873]. Turned base left18deg so fax was above desktop rather than curved chair cutout.
- Used exact head xyz: surrounding tabletop points[.862,-.084,.640],[.824,-.133,.657] BODY. Tilt means tabletop is not constant body-z; do not reuse nominal .755m desktop height.
- Command right to[.87,-.18,.75] ended IK_stalled at TCP[.811,-.191,.788], q[-1.26016,.1469,-.12066,-.01132,-.06968,.69151,-.33455]. RGB showed fax at tabletop. Release grip1 (opening not prerequisite-gated). After release command q[-1.55,.14692,-.1223,-.01142,-.07119,.69083,-.33458] withdrew upward. Two-second hold confirmed visible stability and green switch.

## Transport recovery
One JSONDecodeError (unterminated string~3.7MB) during bounded joint move. Did NOT blindly retry motion. Fresh observe showed actual terminal target reached. Grip command became unknown in local state; restored close-only with top-level accept_partial=True (NOT arm-local field), then continued. No backend edits.
