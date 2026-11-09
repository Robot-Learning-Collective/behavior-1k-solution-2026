// The practice loop: keeps one practice session working on its task, turn after turn, in the same session.
//
// Active only when BEHAVIOR_PRACTICE_LOOP=1 and BEHAVIOR_SIM_RUN_DIR names the run (agent/practice/bin/pi_session.sh).
// After a normal turn ends, it waits 60 s and, if nobody typed anything, sends CONTINUE. It never continues
// through a hold: a STOP or PRACTICE-HOLD file in the run, a "PRACTICE_HOLD: <reason>" line in the agent's reply,
// an aborted or failed turn, or the user typing stop/pause/hold. Holds are cleared by a person, never by the loop.
//
// It also asks Astra for concise compaction summaries, repairs tool outputs orphaned by context-length recovery
// (kept as labelled evidence, never re-executed) and appends a content-free event log to practicer-events.jsonl.
import {appendFileSync, existsSync, writeFileSync} from 'node:fs';
import {join} from 'node:path';
import type {ExtensionAPI} from '@earendil-works/pi-coding-agent';

export const CONTINUE = 'Continue practising in this same session and world, unless a user stop or a genuine runtime/safety blocker remains; never force simulator calls through a hold. When stuck (a few failed tries at the same segment), go back to the human proprio + RGB across DIFFERENT annotations in DIFFERENT episodes: compare the same fine-annotation segment across 2-3 demos, plus neighbouring segments, step through them densely (approach / pre-contact / contact / object-changing move / release), tabulate the human-vs-own differences in NOTES.md, change those, and retry. Guard/controller stops (stalled, timeout, base_velocity_tracking_mismatch, pose miss) that return with execution_uncertain=false are feedback for you to handle, not holds. Write PRACTICE-HOLD for a real runtime/safety blocker (uncertain execution, simulator/transport error, unexpected attempt end) or an explicit user STOP/WAIT_NEXT_INSTANCE; prose alone does not stop the loop. New attempts: admin_reset(..., practice=True, unbounded_practice=True); keep the official native step budget as your own target. Keep routine progress in NOTES.md and examples/.';

export const COMPACTION_FOCUS = 'Keep the entire summary concise, at most 1200 words. Preserve the current task/world binding, current attempt state and unresolved commands, user stops/holds, transferable lessons and exact NOTES/examples/artifact paths. Prefer file references over copied contents; summarize older failed iterations briefly. Raw history remains available. Memory compaction only: no reset, action replay, new actor or task change.';

const DELAY_MS = 60_000;

export function normalTurn(aborted: boolean, last: any) {
  return aborted === false && last?.role === 'assistant' && last.stopReason === 'stop';
}

/** Add the compaction focus to Astra's native summarization request (and nothing else). */
export function conciseCompaction(payload: any) {
  if (payload?.model !== 'gpt-6-astra' || !Array.isArray(payload.input) || payload.tools?.length) return;
  const summary = payload.input.some((item: any) => {
    if (!['system', 'developer'].includes(item.role)) return false;
    const text = typeof item.content === 'string' ? item.content : (item.content ?? []).map((c: any) => c.text ?? '').join('');
    return text.startsWith('You are a context summarization assistant.');
  });
  if (summary) return {...payload, input: [...payload.input, {role: 'user', content: [{type: 'input_text', text: 'Additional compaction focus: ' + COMPACTION_FOCUS}]}]};
}

/** Context-length recovery can drop an assistant message but keep its tool results; the API then rejects them.
 * Keep those results as labelled historical evidence instead. Never invent or replay a tool call. */
export function repairHistory(messages: any[]) {
  const calls = new Set<string>(), repaired: string[] = [];
  const key = (id: string) => id.split('|')[0];
  const output = messages.map(message => {
    if (message.role === 'assistant' && !['error', 'aborted'].includes(message.stopReason)) {
      for (const block of message.content ?? []) if (block.type === 'toolCall') calls.add(key(block.id));
    }
    if (message.role !== 'toolResult' || calls.has(key(message.toolCallId))) return message;
    repaired.push(message.toolCallId);
    return {role: 'user', timestamp: message.timestamp, content: [
      {type: 'text', text: `Recorded historical ${message.toolName} result; its assistant call is absent from the current context after recovery. Evidence only, NOT a request to execute or replay anything.`},
      ...message.content]};
  });
  return {messages: output, repaired};
}

/** A fixed classification of a provider error; the raw message (which may echo request content) is never logged. */
export function errorSummary(message: any) {
  if (message.stopReason !== 'error') return undefined;
  const text = String(message.errorMessage ?? '');
  const status = text.match(/(?:API error\s*\(|\bstatus[=: ]+)([45]\d\d)/i);
  const category = /No tool call found for function call output/i.test(text) ? 'orphaned_tool_output' :
    /context.{0,20}(length|window)|too many tokens/i.test(text) ? 'context_limit' :
    /rate.?limit|quota/i.test(text) ? 'rate_or_quota_limit' :
    /timed?\s*out|timeout/i.test(text) ? 'timeout' :
    /unauthorized|invalid.{0,8}api.{0,8}key|authentication/i.test(text) ? 'authentication' : 'provider_error';
  return {category, ...(status ? {http_status: Number(status[1])} : {})};
}

export default function (pi: ExtensionAPI) {
  const run = process.env.BEHAVIOR_SIM_RUN_DIR;
  if (process.env.BEHAVIOR_PRACTICE_LOOP !== '1' || !run) return;
  const hold = join(run, 'PRACTICE-HOLD');
  const stopped = () => existsSync(hold) || existsSync(join(run, 'STOP'));
  const event = (name: string, data: any = {}) =>
    appendFileSync(join(run, 'practicer-events.jsonl'), JSON.stringify({time: Date.now() / 1000, event: name, pid: process.pid, ...data}) + '\n');
  let timer: ReturnType<typeof setTimeout> | undefined, last: any;
  const reported = new Set<string>();
  const cancel = () => { if (timer) clearTimeout(timer); timer = undefined; };
  const holdFor = (reason: string) => { cancel(); if (!existsSync(hold)) writeFileSync(hold, reason + '\n'); event('held', {reason}); };

  pi.on('before_provider_request', e => conciseCompaction(e.payload));
  pi.on('session_start', () => event('wired', {state: stopped() ? 'held' : 'ready'}));
  pi.on('session_compact', e => event('compacted', {reason: e.reason, tokens_before: e.compactionEntry.tokensBefore}));
  pi.on('session_compact_failed', e => event('compaction_error', {reason: e.reason, error: errorSummary({stopReason: 'error', errorMessage: e.errorMessage})}));
  pi.on('before_agent_start', (_e, ctx) => { if (stopped()) ctx.abort(); });
  pi.on('context', e => {
    const result = repairHistory(e.messages);
    const fresh = result.repaired.filter(id => !reported.has(id));
    if (fresh.length) { fresh.forEach(id => reported.add(id)); event('history_repair', {call_ids: fresh}); }
    return result.repaired.length ? {messages: result.messages} : undefined;
  });
  pi.on('input', e => {
    cancel();
    if (e.source !== 'extension' && /^(stop|pause|hold)\b/i.test(e.text.trim())) holdFor('User stop: ' + e.text);
  });
  pi.on('agent_start', () => { cancel(); last = undefined; event('turn_started'); });
  pi.on('message_end', e => {
    if (e.message.role !== 'assistant') return;
    last = e.message;
    event('model_response', {stop_reason: e.message.stopReason, output_tokens: e.message.usage?.output, error: errorSummary(e.message)});
  });
  pi.on('tool_call', e => {
    // Every bash call is bound to this run, so a stray script cannot drive another run's robot.
    if (e.toolName === 'bash' && typeof e.input.command === 'string')
      e.input.command = `export BEHAVIOR_SIM_RUN_DIR='${run.replaceAll("'", "'\\''")}';\n` + e.input.command;
  });
  pi.on('tool_result', e => event(e.isError ? 'tool_error' : 'tool_result', {tool: e.toolName}));
  pi.on('agent_settled', (e, ctx) => {
    cancel();
    if (e.aborted) { holdFor('Turn aborted (user, cost guard or runtime); a person must release the hold'); return; }
    const text = Array.isArray(last?.content) ? last.content.filter((b: any) => b.type === 'text').map((b: any) => b.text).join('\n') : '';
    const explicit = text.match(/(?:^|\n)\s*PRACTICE_HOLD:\s*(.+)/i);
    if (explicit) { holdFor(explicit[1]); return; }
    if (!normalTurn(e.aborted, last) || stopped()) { event('held', {stop_reason: last?.stopReason, error: last ? errorSummary(last) : undefined}); return; }
    event('waiting', {delay_seconds: DELAY_MS / 1000});
    timer = setTimeout(() => {
      timer = undefined;
      if (stopped() || !ctx.isIdle() || ctx.hasPendingMessages()) return;
      pi.sendUserMessage(CONTINUE);
    }, DELAY_MS);
  });
  pi.on('session_shutdown', () => { cancel(); event('closed'); });
  pi.registerCommand('practice-hold', {description: 'Hold this practice session without touching its world',
    handler: async reason => holdFor(reason || 'Operator hold')});
}
