# First real switch activation — protocol4 v4-a01

Visible red→green at obs1387, green retained after withdrawal obs1405. Same-posture repeat contacts: obs1430 toggled green→red, retained red after withdrawal1448; obs1470 toggled red→green, retained green after withdrawal1488. Three consecutive switches, with depth reacquired each time. Ranked switch-contact skill locally repeatable; not reset/generalization mastery or episode completion.

Repeat2 target [.91735,-.16586,.72370], repeat3 [.92866,-.15283,.72741] (XYZ sphere surface +4mm BODY-Z). Scanner shifts slightly from contact, so reacquire depth rather than replay fixed pose. Repeat3 press+withdraw took5.47 simulated seconds and~35wall seconds including tool/transport. No human-time parity claim.

Robot base at final success rel_xyz [.956,-1.105,.040]m, rel_yaw−1.735rad. Base is tilted/raised by nearby furniture; do not transplant BODY heights to a differently situated base. Torso q=[1.25,-1.76,-.85,0]. Left TCP≈[.680,.263,.875], open. Right grip0, finger_dir≈[.707,0,-.707], close_dir=[0,-1,0].

1. Precontact right TCP [.909,-.180,.780] achieved. Read live right camera red sphere pixel(u287,v102): XYZ [.9115065,-.1700502,.7210882].
2. `s.act(right={'to':[.9115065,-.1700502,.7250882]}, max_steps=12)` → obs1387, actual TCP [.915,-.171,.730]. Pose no_progress ~5.6mm residual; visible sphere turns GREEN. Native joint effort increased; this is not a contact-force measurement.
3. `s.act(right={'to':[.84,-.18,.84]},max_steps=12)` → obs1405 achieved [.841,-.180,.840], sphere remains GREEN. Pressure removed by changing goal.

Key lessons: direct straight-down wrist plus high torso exhausted reach around x.75–.82. Angled fingers and explicit torso forward lean [1.25,-1.76,-.85,0] enabled x.91 low target. A returned pose failure need not mean switch failure: inspect actual color, then withdraw. Persistent commands must not be left loaded.

Navigation lesson: initial hands-down approach snagged right hand on chair and loaded elbow against endpoint. Retreat and unload first. Raise both elbows q4−1.95 with tall torso BEFORE passing chair; this cleared furniture. Do not repeat failed hands-down route.
