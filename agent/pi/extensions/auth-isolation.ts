// The model process needs the API key; robot/tool subprocesses do not. Every bash call runs with model keys unset,
// and reading another process's environment (/proc/<pid>/environ) is refused. This keeps the key out of tool output
// and transcripts by accident; it is not a sandbox against deliberately malicious code.
import type {ExtensionAPI} from '@earendil-works/pi-coding-agent';

const ENVIRON = /\/proc\/[^\s'"]*environ/;

export default function(pi: ExtensionAPI) {
  pi.on('tool_call', (event) => {
    const input = event.input as Record<string, unknown>;
    const text = [input.command, input.path, input.script, input.code].filter(v => typeof v === 'string').join('\n');
    if (ENVIRON.test(text)) return {block: true, reason: 'Process environments are not readable from tools'};
    if (event.toolName === 'bash' && typeof input.command === 'string') {
      input.command = 'unset OPENAI_API_KEY ANTHROPIC_API_KEY GEMINI_API_KEY;\n' + input.command;
    }
  });
}
