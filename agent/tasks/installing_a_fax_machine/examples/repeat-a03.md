# a03 — high carry improvement, third consecutive visual completion

**158.3667 simulated seconds /4751 native30Hz ticks;1262.8658 wall seconds through finish.** 43.13s faster than a02 (21.4%), below requested170s target and approximate6115-tick cap. Fresh-reset same TRAIN10 scene; not official scoring. Green fax released155.73s, hand withdrawn156.37s, independent tabletop support stable through158.37s. One faster repeat does not establish reliable ≤170s across repeated runs. Incidental rail/base contacts remain, not collision-free certification.

[Exact32 public requests and endpoint proprioception/images](repeat-a03-exact.md); includes two pre-motor validation rejections (rounded wrist limit and mistaken `pos` rather than `to`). Regenerate offline with `python3 examples/export_repeat.py a03`.

## Pickup and switch
Same aisle route as a02. Combined final.78m approach with raised hand joint goals, then deep torso[1.68,-2.54,-1.62,0]. Right wrist goal1.036 rather than rounded1.0372, which exceeds exact bound. Head(485,465) fax[.645667,-.317557,.045819]; right(245,180) casing[.609827,-.320173,.043073]. Right to[.61,-.32,.15] fingers down/closing+y, then[.61,-.32,.035]; IK plateau at[.602,-.318,.053]. Replace target with measuredq[-1.17843,-.12875,1.02494,-.03335,-.98062,.4317,.10983] and close both hands. Lift right to[.602,-.318,.20]; retained fax visually follows113.8s. Aperture.0355/.0329 is corroboration, not proof.

Tilt right to[.50,-.08,.23],pitch35 and left to[.58,-.06,.36] with previous angled finger/close axes. Left(226,194) switch[.596880,-.129315,.282731], approach+[-.01,.015,.02]. Remeasure(233,245)[.598118,-.129198,.282866], press+[.003,-.004,-.005]. GREEN126.63s despite no-progress result; withdraw[.61,-.04,.36]129s.

Before/contact/after images: obs0833/0862/0870/0893 pickup;0958/0969/0986/1004 switch, all under `/tmp/fax-run-008_obs/fax-run-008-v4-a03/` (exact filenames in export).

## Faster placement
1. **Before moving toward furniture**, stand torso[.84,-1.00609,-.42,0] while holding arm joints; then rightq[-1.8,.05,-.13,-.12,.065,1,-.14], leftzeros. High TCP[.972,-.241,1.138] achieved134s, base[-3.795,-1.552,-.003],yaw1.958. Retention remained visible.
2. Base fwd.45 then yaw115. At149.5s rail interaction caused right joint lag; do not lower through divider. Head table(520,410)[1.099855,-.513797,.752035], rail(420,435)[.609947,-.065020,1.187563].
3. Base left-.32 moves toward open tabletop edge; base becomes[-4.197,-.918,.010], indicating tilt. Back fwd-.08 BEFORE descent, releasing foot pressure: base[-4.143,-.861,-.001],yaw-2.322. No long failed low-carry or folded-elbow sequence.
4. Lower right shoulder to-1.45 (other joints unchanged). Remeasure table head(430,475)=[.860950,-.179773,.755293]. Then shoulder-1.36; TCP[.838,-.241,.854], pad references[.839,-.210,.852] and[.837,-.273,.856], fingers.0346/.0338.
5. Grip1; raise shoulder-1.65; hold2s. Fax is keypad-up, green, supported by tabletop, no hand contact. Final TCP[.940,-.242,1.035], base remains[-4.143,-.861,-.001]; torso effort settles~0.3Nm. `admin_finish`158.3667s.

Images:1038 high carry;1162 rail-facing;1190 lateral;1198 backed clear;1203 above surface;1207 before release;1211 release;1216 withdrawn;1229 stable.
Final receipt `/tmp/fax-run-008_obs/fax-run-008-v4-a03/receipt_01792116834862731000_cd101e4801b0437a8bcfd63600e5c184.json`.

## Remaining reliability risk
High carry removed the severe under-desk trap, but the115° turn still brushed a divider and lateral move produced transient base tilt. Improve swept-path clearance rather than claiming clean mastery. Three consecutive visual task completions; only a03 is under170s.
