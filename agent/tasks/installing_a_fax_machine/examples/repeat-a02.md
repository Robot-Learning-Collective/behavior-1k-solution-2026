# Second full-task practice completion — a02

**201.50 simulated seconds (6045 native30Hz ticks),1505.79 wall seconds**, including all navigation, failed placement approaches, recovery and final backoff. Green-lit fax was released at197.87s, hand withdrawn198.50s, visibly stable for2s at200.50s. Final backoff relieved torso load100Nm→~0 and base rel z+.003→-.001m. This is public-visual evidence, not private BDDL scoring or official certification. Under lead-provided approximate6115-step cap, not under200s. Two consecutive visual task completions now (a01 anda02).

## Reproduction record
[Exact41 public requests, outcomes, images and full compact proprioception at each endpoint](repeat-a02-exact.md). This preserves unsuccessful requests too; do not blindly replay it. All use run-local protocol4 client. [Offline export helper](export_repeat.py) regenerates the record without simulator calls.

## Successful pickup (repeat)
1. Navigate wall-side aisle, turn into cross passage. Base[-3.795,-1.550,-.003],yaw1.958. Raise arms before torso crouch[1.68,-2.54,-1.62,0].
2. Head pixel(485,465) fax[.64566,-.31755,.04584]. Right open hand to[.61,-.32,.15], fingers-down/close+y.
3. Wrist pixel(245,180) surface[.60984,-.32017,.04312], flank samples[.61106,-.29558,.04721] and[.60767,-.34652,.03578]. Descend to[.61,-.32,.035], IK stalls at[.602,-.318,.053] (not contact proof).
4. Replace with measured rightq[-1.17843,-.12874,1.0247,-.03335,-.98038,.4317,.10983],grip0. Then to[.602,-.318,.20]. Visible lift retained object; fingers~.0355/.0345 (not standalone proof).
Images: obs0922 before descent,0951 contact approach,0959 close,0982 lifted; exact paths and all pad positions in linked record.

## Successful switch (repeat; single press)
1. Left grip0; combine right to[.50,-.08,.23],pitch35 with left to[.58,-.06,.36],finger_dir[.220337,-.708506,-.670426],close_dir[-.038811,.680406,-.731807].
2. Left pixel(226,194) red button[.5968628,-.12942728,.28262115]. Approach button+[-.01,.015,.02].
3. Remeasure left(233,245)=[.59805936,-.12942363,.28264806]. Press button+[.003,-.004,-.005],max_steps6. Pose blocked but switch GREEN at139.30s. Withdraw left to[.61,-.04,.36], green persists.
Images: obs1051/1062 precontact,1079 green/contact,1096 withdrawn. Right target remains[.5,-.08,.23]. Exact joints/pads in record.

## Placement and important failed approach
Stand with compact carryq and tall torso. Repeated mistake: entering near desk with fax low traps arm under desk edge; trying folded-elbow targets cannot lift through the surface. Back off enough before lift. In this attempt .30m backoff was insufficient, additional .45 request moved~.36 and allowed straight-arm lift q[-1.8,.05,-.13,-.12,.065,1,-.14] toTCP[.971,-.241,1.138]. Do this while clear *before* approaching on future repeats.

Then fwd.4; lowerq1-1.45; raiseq1-1.65 with fwd.20; lowerq1-1.45 then-1.36. Desk depth before final approach[1.14395,-.29968,.75533], later adjacent support[.85376,-.19352,.74680]. Final rightTCP[.837,-.241,.855], base[-4.158,-.872,.003],yaw-2.324; torso tall. Grip1 released fax on tabletop, shoulderq1-1.65 withdrew,2s hold preserved green light and support. Basefwd-.08 relieved robot/table pressure; final base[-4.104,-.814,-.001],yaw-2.325.

Images: obs1491 approach,1521 before release,1525 release,1530 withdrawn,1543 stable,1551 final backoff. Final receipt `/tmp/fax-run-008_obs/fax-run-008-v4-a02/receipt_01792115477831351000_ec69ca0dc2184cd3bd1fdc1532a34900.json`.

## Next improvement
Lift to high straight-arm carry while still in open cross aisle, then approach desk. Avoid early folded-elbow attempt near/under tabletop, all recovery backoffs and recrossing. This should save substantial simulated time but is not yet verified. No direct chair-pushing sequence needed in a02; incidental contacts still occurred and were recovered, so do not claim collision-free navigation.
