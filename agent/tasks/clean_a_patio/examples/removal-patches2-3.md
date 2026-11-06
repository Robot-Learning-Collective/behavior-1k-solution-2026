# Two additional visible patch removals

Same attempt/grasp/torso as removal-probe.md. These are independent sub-step outcomes within one episode, not reset repeatability.

## Patch2 obs47→49
Base odom[.095,-.397,8.236rad]; target depth head(280,431)=[.78955,.19896,-.00515]. Pre left TCP[.497,.423,.159], fingers[.0344,0], q[-.10739,.73911,-.48584,-1.30023,-.08864,.17505,.03017].
- `s.act(left={'to':[.57,.44,.005]},timeout_seconds=4)` contact stroke obs48:2.167sim s, stalled with11mm residual, TCP[.572,.435,.014].
- `s.act(left={'to':[.50,.55,.16]},timeout_seconds=4)` reveal obs49:1.133sim s, TCP[.499,.551,.159], q[-.19786,.813,-.34744,-.88427,-.09362,-.22897,-.15641]. Previously orange patch absent. Q0 at3779ticks.

## Patch3 obs51→53
Navigate depth-checked base right.4, then forward.45; base odom[.296,.163,8.236rad]. Patch head(308,428)=[.79689,.12907,-.00516]. Pre left TCP[.500,.421,.159], fingers[.0344,0].
- `s.act(left={'to':[.58,.36,.005]},timeout_seconds=4)` obs52:1.20sim s, reached TCP[.582,.357,.008], q[-.71771,.28630,-.43671,-.47010,-.42947,-.01537,-.09673].
- `s.act(left={'to':[.50,.55,.16]},timeout_seconds=4)` obs53:.767sim s. Patch absent after reveal, broom retained. TCP[.500,.551,.159], q[-.16725,.72080,-.10013,-.88916,-.28304,-.24709,-.27154], fingers[.0345,0].

Torso[1.75,-1.75,-1.073,0], gripL0/R1 throughout. Evidence full images/depth/receipts obs47–53 in same cache namespace. Exact actions in control-action-results.jsonl. No global success claim.
