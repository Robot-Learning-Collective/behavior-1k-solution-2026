# Full-scene brown extraction — first verified, not repeated

Active generation d67539/source5fdefd3 only. Attempt `practice-restore-fullscene-trunk-open-stable-624061adfdd84ea0bcff9bd55ff12176`. Exact public actions in ../control-action-results.jsonl, images in matching local cache. Many failed pinches/contact displacements preceded this; do not claim a clean-reset recipe.

## Successful local segment, obs37–53
At base≈[-.762,3.168], yaw−6.302 after reapproach:
- Left historical first-success q[-1.19551,.27002,-.0479,-.79621,.88487,.92732,-.33527], open, initially torso[.849,-1.128,-.45,0].
- Torso pitch−.895 contacted top and deflected elbow; TCP[.928,.219,.883] remained too high. Top depth≈.827m. Cancel measured q.
- Move left +.10m to clear actual side edge BEFORE lowering; then down .08m. Endpoint near[.923,.316,.803], q[-1.47823,.38861,-.3894,-.07367,.77747,.51204,-.98991]. Tiny IK miss cancelled with measured q.
- Move left−.055m into rim. Endpoint[.921,.269,.802], pads[.925,.298,.765] / [.916,.239,.839]. Command timed out with only small residual; cancel using measured q and close.
- obs45 closed fingers .05/.0485, 9.8cm obstruction. This alone was not success.
- Torso−.775 independent10cm lift (obs46), then measured-q unload and torso−.45 (obs48): case visibly rises with hand, black bag stays in trunk. Wrist q5 deflected .407rad; cancel measured q.
- obs50 base−.45m, actual≈.446m, retains case outside trunk. Save `fullscene-brown-extracted-first`.
- Human144→148→150 left q carry route succeeds obs51–53, brown visibly retained. Save `fullscene-brown-carry`.

Important lesson: descend OUTSIDE the edge before sliding inward. Earlier descents above top surface made lower finger press the lid and moved the bag; closing then went empty. Vertical jaws/near-horizontal forward fingers often hit bumper/approached a poor straight-elbow branch. The oblique first-success wrist plus outside-edge descent avoided this.

Final obs53: torso[.849,-1.128,-.45,0], base[-1.206,3.176], yaw−6.303; left q[.1719,.2763,.0375,-1.4632,.6092,-.1003,-.0398], grip0, ~9.8cm obstruction, TCP[.548,.367,.831]. Right remains open/stowed. Black satchel stays in trunk; neither sofa predicate yet satisfied. Plan: attempt single-bag delivery through already-open full-scene doorway, then return for satchel.
