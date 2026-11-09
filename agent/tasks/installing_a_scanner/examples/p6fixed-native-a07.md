# Fixed protocol6 native a07 — first-acquisition visual completion

Attempt `scanner-run-007-v6fixed-native-a07`, no snapshots/restores. Finished 74.866667sim seconds (~2246 nominal30Hz steps; budget6387), 486.862761wall seconds. Scanner retained on first closure/lift/withdrawal, independently supported beside laptop, green switch persisted after withdrawal. No visible robot tilt. Not privileged scoring. One transport recovery and one rejected torso-schema request mean not an error-free run; consecutive clean target remains unproven.

Evidence `/tmp/scanner-run-007-p6-b311c1/scanner-run-007-v6fixed-native-a07/`; final obs49 receipt `receipt_01792121301963654000_c20817098d264fd99ec07f2b9f04457c.json`. Full actual commands in run control-action-results.jsonl.

Preparation: same a06 navigation and three sweeps. Fresh act images, no routine observe-after-act. Retreat-.60 had truncated JSON; observe26 confirmed completion, no replay. Explicitly reopened both grips afterward.

Acquisition changes: vertical-jaw seed same as a06; stage [.823,-.30,.805] (15mm higher), base+.35. Head pixels (510,460) [.936047,-.203544,.837884], (470,460) [.936326,-.149689,.837233]. Align [.85,-.18,.805], insert [.95,-.18,.805]. Stalled actual [.936,-.175,.790]. Rather than leave unmet target or reject dependent closure, unload at measured q [-.3383,-.42648,.92504,-1.74859,-2.0605,-.89573,.4871] with grip0, accept_partial=True. First closure retained6.1cm finger sum; lift [.936,-.175,.89] elbow-limited actual [.939,-.178,.861], but scanner rose. Withdraw base-.40 with measured q [-.36808,-.48144,.92861,-2.08392,-1.6286,-1.00923,-.13162], accept_partial=True; obs35 confirms unsupported retained scanner. This is first acquisition, not another grasp retry.

Carry yaw-25; fwd+.50 then+.15. Lower [.936,-.175,.79] stalled against support; release at actual q [-.26837,-.3764,.8168,-1.81488,-1.46071,-.85381,.26692], grip1, accept_partial=True. Retreat-.20; independently supported obs41.

Close empty right hand. Torso MUST be {'q':[1.25,-1.76,-.85,0]} (raw list rejected before motion); right seed [-1.95597,-.4024,2.11198,-1.48611,.81688,.03802,.85601]. Raise [.84,-.18,.94], advance+.20. Right pixel(278,22) [.867996,-.168246,.822561]; stage+Z.06. Reacquire right(252,92) [.866786,-.167093,.821450]; press+Z.004. Green obs47, withdraw [.84,-.18,.94], retreat-.20, persistent green obs49.
