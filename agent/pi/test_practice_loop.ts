/** Offline checks of the practice loop: npx --yes --package=tsx@4.20.6 tsx agent/pi/test_practice_loop.ts */
import assert from 'node:assert/strict';
import {existsSync, mkdtempSync, readFileSync, rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import loop, {CONTINUE, conciseCompaction, normalTurn, repairHistory} from './extensions/practice-loop';

assert.equal(normalTurn(false, {role: 'assistant', stopReason: 'stop'}), true);
assert.equal(normalTurn(true, {role: 'assistant', stopReason: 'stop'}), false);
assert.equal(normalTurn(false, {role: 'assistant', stopReason: 'error'}), false);

const repaired = repairHistory([
  {role: 'assistant', stopReason: 'stop', content: [{type: 'toolCall', id: 'a|1'}]},
  {role: 'toolResult', toolCallId: 'a|1', toolName: 'bash', content: []},
  {role: 'toolResult', toolCallId: 'b|2', toolName: 'bash', content: [{type: 'text', text: 'old'}]},
]);
assert.deepEqual(repaired.repaired, ['b|2']);
assert.equal(repaired.messages[2].role, 'user');

const summary = {model: 'gpt-6-astra', input: [{role: 'system', content: 'You are a context summarization assistant. ...'}]};
assert.equal(conciseCompaction(summary)!.input.length, 2);
assert.equal(conciseCompaction({model: 'gpt-6-astra', input: [{role: 'user', content: 'hi'}]}), undefined);

// Lifecycle with a fake Pi: continue after a normal turn, never through a hold.
const run = mkdtempSync(join(tmpdir(), 'practice-loop-'));
const saved = {loop: process.env.BEHAVIOR_PRACTICE_LOOP, run: process.env.BEHAVIOR_SIM_RUN_DIR};
process.env.BEHAVIOR_PRACTICE_LOOP = '1';
process.env.BEHAVIOR_SIM_RUN_DIR = run;
const realTimeout = globalThis.setTimeout;
const pending: Function[] = [];
(globalThis as any).setTimeout = (fn: Function) => { pending.push(fn); return pending.length; };
try {
  const handlers = new Map<string, Function>(), sent: string[] = [];
  loop({on: (name: string, fn: Function) => handlers.set(name, fn), registerCommand: () => {},
        sendUserMessage: (text: string) => sent.push(text)} as any);
  const ctx = {isIdle: () => true, hasPendingMessages: () => false};
  const turn = (text: string, stopReason = 'stop', aborted = false) => {
    handlers.get('agent_start')!({});
    handlers.get('message_end')!({message: {role: 'assistant', stopReason, content: [{type: 'text', text}]}});
    handlers.get('agent_settled')!({aborted}, ctx);
  };
  turn('Practised the grasp; notes updated.');
  assert.equal(pending.length, 1); pending.shift()!();
  assert.deepEqual(sent, [CONTINUE]);

  const command = {toolName: 'bash', input: {command: 'python3 x.py'}};
  handlers.get('tool_call')!(command);
  assert.match(command.input.command, /^export BEHAVIOR_SIM_RUN_DIR=/);

  turn('Simulator crashed.\nPRACTICE_HOLD: worker exited with code 74');
  assert.equal(pending.length, 0);
  assert.match(readFileSync(join(run, 'PRACTICE-HOLD'), 'utf8'), /worker exited/);
  turn('Trying again anyway.');
  assert.equal(pending.length, 0);                           // a hold file blocks continuation
  rmSync(join(run, 'PRACTICE-HOLD'));
  turn('', 'error');
  assert.equal(pending.length, 0);                           // failed turns are not continued
  turn('', 'stop', true);
  assert.ok(existsSync(join(run, 'PRACTICE-HOLD')));        // aborted turns hold
  console.log('PRACTICE_LOOP_OFFLINE_PASS');
} finally {
  (globalThis as any).setTimeout = realTimeout;
  process.env.BEHAVIOR_PRACTICE_LOOP = saved.loop;
  process.env.BEHAVIOR_SIM_RUN_DIR = saved.run;
  rmSync(run, {recursive: true, force: true});
}
