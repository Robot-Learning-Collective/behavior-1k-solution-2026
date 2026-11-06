// Offline check that every frozen session forks in the pinned Pi (no provider calls).
// PI_PACKAGE_ROOT=<node_modules/@earendil-works/pi-coding-agent> node agent/pi/test_forks.mjs [task]
import {readFileSync, mkdtempSync, createReadStream, rmSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {join, dirname, resolve} from 'node:path';
import {tmpdir} from 'node:os';
import {fileURLToPath, pathToFileURL} from 'node:url';
const root = dirname(fileURLToPath(import.meta.url));
const pkg = process.env.PI_PACKAGE_ROOT;
if (!pkg) throw Error('Set PI_PACKAGE_ROOT to the pinned Pi package directory');
const {SessionManager} = await import(pathToFileURL(join(pkg,'dist/index.js')).href);
const taskRoot = resolve(process.env.BEHAVIOR_TASK_ROOT || join(root,'..','tasks'));
const tasks = JSON.parse(readFileSync(join(taskRoot,'tasks.json'),'utf8')).tasks;
for (const [name, task] of Object.entries(tasks)) {
  if (process.argv[2] && process.argv[2] !== name) continue;
  const dir = mkdtempSync(join(tmpdir(),'behavior-fork-'));
  const session = join(taskRoot, name, 'session.jsonl');
  const manager = SessionManager.forkFrom(session, dir, join(dir,'sessions'));
  const context = manager.buildSessionContext();
  if (manager.getEntries().length < 10 || context.messages.length < 1) throw Error('Empty fork: '+name);
  const digest = createHash('sha256');
  for await (const chunk of createReadStream(session)) digest.update(chunk);
  if (digest.digest('hex') !== task.session.sha256) throw Error('Frozen source changed: '+name);
  console.log(JSON.stringify({task:name, entries:manager.getEntries().length,
    context_messages:context.messages.length, source_unchanged:true, offline_fork:'PASS'}));
  rmSync(dir,{recursive:true,force:true});
}
