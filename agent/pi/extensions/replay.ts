/** Read-only Pi lifecycle capture. It never changes prompts, tools or model settings. */
import { appendFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { createHash, randomUUID } from 'node:crypto';
import type { ExtensionAPI } from '@earendil-works/pi-coding-agent';

export default function replay(pi: ExtensionAPI) {
  const root = process.env.BEHAVIOR_EVAL_RUN_DIR;
  if (!root) return;
  const media = join(root, 'replay-media');
  let request: string | null = null;
  let compaction: string | null = null;
  let sequence = 0;
  const processId = randomUUID();
  const key = process.env.OPENAI_API_KEY;
  // Keep images once, and leave encrypted continuity state in the original private session.
  function clean(value: any): any {
    if (typeof value === 'string') {
      let text = key ? value.split(key).join('[REDACTED_CREDENTIAL]') : value;
      return text.replace(/\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{24,}/g, '[REDACTED_CREDENTIAL]');
    }
    if (Array.isArray(value)) return value.map(clean);
    if (!value || typeof value !== 'object') return value;
    if (value.type === 'image' && typeof value.data === 'string') {
      const bytes = Buffer.from(value.data, 'base64');
      const extension = value.mimeType === 'image/png' ? 'png' : 'jpg';
      const name = createHash('sha256').update(bytes).digest('hex') + '.' + extension;
      mkdirSync(media, { recursive: true });
      writeFileSync(join(media, name), bytes);
      return { type: 'image', mimeType: value.mimeType, path: 'replay-media/' + name };
    }
    const output: any = {};
    for (const [name, item] of Object.entries(value)) {
      if (/^(thinkingSignature|thoughtSignature|encrypted_content)$/i.test(name)) continue;
      if (/^(authorization|api_?key|access_?token|cookie)$/i.test(name)) {
        output[name] = '[REDACTED_CREDENTIAL]';
      } else output[name] = clean(item);
    }
    return output;
  }
  function emit(event: string, fields: any = {}) {
    appendFileSync(join(root!, 'agent-events.jsonl'), JSON.stringify({
      schema_version: 1, event, process_id: processId, sequence: sequence++,
      wall_unix_ms: Date.now(), monotonic_ns: process.hrtime.bigint().toString(),
      request_id: request, ...clean(fields),
    }) + '\n');
  }
  pi.on('session_start', (_event, ctx) => {
    emit('session_start', { session_id: ctx.sessionManager.getSessionId() });
  });
  pi.on('before_provider_request', event => {
    if (request) emit('model_interrupted', { reason: 'A subsequent provider request began' });
    request = randomUUID();
    const payload = event.payload as any;
    emit('model_start', { model: payload?.model, reasoning: payload?.reasoning });
  });
  pi.on('after_provider_response', event => {
    emit('model_headers', { status: event.status, provider_request_id: event.headers['x-request-id'] });
  });
  pi.on('message_update', event => {
    const update = event.assistantMessageEvent as any;
    if (update.type === 'thinking_delta') {
      emit('reasoning_delta', { text: update.delta, content_index: update.contentIndex });
    }
  });
  pi.on('message_end', event => {
    if (event.message.role === 'assistant') {
      emit('model_end', { message: event.message });
      request = null;
    }
  });
  pi.on('tool_execution_start', event => emit('tool_start', {
    tool_call_id: event.toolCallId, parent_tool_call_id: event.parentToolCallId,
    tool: event.toolName, arguments: event.args,
  }));
  pi.on('tool_execution_end', event => emit('tool_end', {
    tool_call_id: event.toolCallId, parent_tool_call_id: event.parentToolCallId,
    tool: event.toolName, result: event.result, error: event.isError, duration_ms: event.durationMs,
  }));
  pi.on('session_before_compact', event => {
    compaction = randomUUID();
    emit('context_start', { context_id: compaction, reason: event.reason });
  });
  pi.on('session_compact', event => {
    emit('context_end', { context_id: compaction, reason: event.reason });
    compaction = null;
  });
  pi.on('session_compact_failed', event => {
    emit('context_error', { context_id: compaction, reason: event.reason,
      error: event.errorMessage || (event.aborted ? 'Compaction aborted' : 'Compaction failed') });
    compaction = null;
  });
  pi.on('session_shutdown', () => {
    if (request) emit('model_interrupted', { reason: 'Session closed before model completion' });
    if (compaction) emit('context_error', { context_id: compaction, error: 'Session closed during compaction' });
    emit('session_end');
  });
}
