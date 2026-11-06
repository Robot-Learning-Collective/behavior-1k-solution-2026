"""Practice-only feedback shape/gating; native Q implementation is used live."""
from pathlib import Path
from types import SimpleNamespace
from practice_feedback import feedback
from practice_snapshots import SnapshotRejected

calls=[]
conditions=[SimpleNamespace(body=['toggled_on','scanner.n.01_1']),SimpleNamespace(body=['nextto','scanner.n.01_1','laptop.n.01_1'])]
task=SimpleNamespace(activity_goal_conditions=conditions,ground_goal_state_options=[conditions],
    compiled_task=SimpleNamespace(check_goal=lambda fn:(calls.append('goal') or False,{'satisfied':[1],'unsatisfied':[0]})),
    get_goal_option_satisfaction=lambda index:[[False,True]],_evaluate_predicate=lambda *args:False)
session={'root':Path('/private/practice'),'practice':True,'step':12,'practice_feedback_initial':[[False,False]]}
for bad in (None,dict(session,practice=False)):
    try:feedback(task,bad,lambda *args:1.)
    except SnapshotRejected:pass
    else:raise AssertionError('Evaluation feedback leaked')
assert calls==[], 'Evaluation guard ran after privileged evaluation'
seen=[]
out=feedback(task,session,lambda success,now,initial:(seen.append((success,now,initial)) or .5))
assert out['q_score']==.5 and out['satisfied_fraction']==.5
assert [p['satisfied'] for p in out['predicates']]==[False,True]
assert out['predicates'][0]['predicate']=='(toggled_on scanner.n.01_1)'
assert seen==[(False,[[False,True]],[[False,False]])]
print('PRACTICE_FEEDBACK_EVALUATION_EARLY_GUARD_PREDICATES_NATIVE_Q_INPUTS_PASS')
