"""Privileged training-only BDDL feedback. Never called by act/observe."""
from practice_snapshots import SnapshotRejected


def feedback(task, session, compute_q_score):
    if session is None or session.get('practice') is not True:
        raise SnapshotRejected('Goal feedback requires an active practice attempt; evaluation is forbidden')
    done, status = task.compiled_task.check_goal(lambda name, *entities: task._evaluate_predicate(0, name, *entities))
    masks = task.get_goal_option_satisfaction(0)
    initial = session['practice_feedback_initial']
    def expression(node):
        body = node.body
        def render(value):
            return '('+' '.join(render(x) for x in value)+')' if isinstance(value,(list,tuple)) else str(value)
        return render(body)
    satisfied = set(status['satisfied'])
    return {
        'practice_only': True, 'privileged_training_feedback': True,
        'attempt_id': session['root'].name, 'step': session['step'],
        'success': bool(done),
        'predicates': [{'index': i, 'predicate': expression(condition), 'satisfied': i in satisfied}
                       for i,condition in enumerate(task.activity_goal_conditions)],
        'goal_options': [[{'index': i, 'predicate': expression(condition), 'satisfied': bool(mask[i])}
                          for i,condition in enumerate(option)]
                         for option,mask in zip(task.ground_goal_state_options,masks)],
        'q_score': float(compute_q_score(bool(done), masks, initial)),
        'satisfied_fraction': max((sum(mask)/len(mask) if mask else 0. for mask in masks),default=0.),
        'q_definition': 'Native compute_q_score: success=1; otherwise newly satisfied since this practice start / predicates per option, maximized over alternatives',
        'satisfied_fraction_definition': 'Current satisfied predicates / predicates per option, maximized over alternatives; not baseline-adjusted Q',
        'source': 'BehaviorTask.compiled_task.check_goal + get_goal_option_satisfaction; native TaskMetric.compute_q_score',
    }
