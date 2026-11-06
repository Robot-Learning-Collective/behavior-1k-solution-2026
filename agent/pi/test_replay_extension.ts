/** Offline lifecycle smoke: npx --yes --package=tsx@4.20.6 tsx agent/pi/test_replay_extension.ts */
import assert from 'node:assert/strict';
import { mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import replay from './extensions/replay';

const directory = mkdtempSync(join(tmpdir(), 'replay-extension-'));
const previous = { root: process.env.BEHAVIOR_EVAL_RUN_DIR, key: process.env.OPENAI_API_KEY };
process.env.BEHAVIOR_EVAL_RUN_DIR = directory;
process.env.OPENAI_API_KEY = 'synthetic-test-secret';
try {
  const callbacks = new Map<string, Function>();
  replay({ on: (name: string, fn: Function) => callbacks.set(name, fn) } as any);
  const emit = (name: string, value: any) => callbacks.get(name)!(value);
  emit('before_provider_request', {payload:{model:'test',reasoning:{summary:'auto'}}});
  emit('message_update', {assistantMessageEvent:{type:'thinking_delta',delta:'A returned summary.',contentIndex:0}});
  const message = {role:'assistant', content:[{type:'thinking',thinking:'A returned summary.',thinkingSignature:'private-continuity'}],usage:{input:10}};
  emit('message_end', {message});
  const args = {note:'synthetic-test-secret', command:'observe()'};
  emit('tool_execution_start', {toolCallId:'child', parentToolCallId:'parent',toolName:'observe',args});
  const result = {content:[{type:'image',mimeType:'image/png',data:Buffer.from('synthetic-image').toString('base64')}]};
  emit('tool_execution_end', {toolCallId:'child',parentToolCallId:'parent',toolName:'observe',result,durationMs:42,isError:false});
  emit('before_provider_request', {payload:{model:'test'}});
  emit('session_shutdown', {});
  const raw = readFileSync(join(directory,'agent-events.jsonl'),'utf8');
  const events = raw.trim().split('\n').map(line=>JSON.parse(line));
  assert(!raw.includes('synthetic-test-secret'));
  assert(!raw.includes('private-continuity'));
  assert.equal(message.content[0].thinkingSignature,'private-continuity');
  assert.equal(args.note,'synthetic-test-secret');
  assert.equal(events[0].request_id,events[2].request_id);
  assert.notEqual(events[0].request_id,events[5].request_id);
  assert.equal(events[4].parent_tool_call_id,'parent');
  assert.equal(events[6].event,'model_interrupted');
  const image = events[4].result.content[0];
  assert.equal(readFileSync(join(directory,image.path),'utf8'),'synthetic-image');
  assert(result.content[0].data);
  emit('session_before_compact', {reason:'threshold'});
  emit('session_compact', {reason:'threshold'});
  const context = readFileSync(join(directory,'agent-events.jsonl'),'utf8').trim().split('\n').slice(-2).map(line=>JSON.parse(line));
  assert.equal(context[0].event,'context_start');
  assert.equal(context[1].event,'context_end');
  assert.equal(context[0].context_id,context[1].context_id);
  console.log('REPLAY_EXTENSION_OFFLINE_PASS');
} finally {
  for (const [name, value] of Object.entries({BEHAVIOR_EVAL_RUN_DIR:previous.root,OPENAI_API_KEY:previous.key})) {
    if (value === undefined) delete process.env[name]; else process.env[name] = value;
  }
  rmSync(directory,{recursive:true,force:true});
}
