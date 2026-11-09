// CPU-only check of the pinned extension's actual outer-tool image attachment.
import assert from 'node:assert/strict';
import {createHash, randomUUID} from 'node:crypto';
import {mkdtempSync, mkdirSync, writeFileSync, rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join, resolve} from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';

const root=fileURLToPath(new URL('.',import.meta.url));
if(!process.env.PI_PACKAGE_ROOT)throw Error('Set PI_PACKAGE_ROOT to the pinned installed Pi package directory');
const require=createRequire(join(resolve(process.env.PI_PACKAGE_ROOT),'package.json'));
const {createJiti}=require('jiti');
const jiti=createJiti(import.meta.url);
const extension=await jiti.import(join(root,'extensions/observation_delivery.ts'));
const session=randomUUID(), call=randomUUID();
const delivery=extension.deliveryDirectory(session,call);
const temp=mkdtempSync(join(tmpdir(),'behavior-delivery-test-'));
try{
 mkdirSync(delivery,{recursive:true});
 const imagePath=join(temp,'obs_0001.jpg'), receipt=join(temp,'receipt.json');
 // Small opaque JPEG-framed fixture; attachment test, not an image decoder.
 const image=Buffer.from([0xff,0xd8,0xff,0xd9]);writeFileSync(imagePath,image);
 const state='CPU-only public state';
 writeFileSync(receipt,JSON.stringify({observation_contract:1,observation_id:1,attempt_id:'cpu',local_image_path:imagePath,compact_state:state}));
 const manifest={observation_contract:1,observation_id:1,attempt_id:'cpu',receipt_file:receipt,image_file:imagePath,state_text:state,image_sha256:createHash('sha256').update(image).digest('hex')};
 const manifestPath=join(delivery,'endpoint.json');writeFileSync(manifestPath,JSON.stringify(manifest));
 const handlers={};extension.default({on:(name,handler)=>{handlers[name]=handler;}});
 const ctx={sessionManager:{getSessionId:()=>session}};
 handlers.tool_call({toolName:'codemode',toolCallId:call,input:{}},ctx);
 const child={toolName:'bash',toolCallId:call+'/0',parentToolCallId:call,input:{command:'python3 example.py'}};
 handlers.tool_call(child,ctx);assert.ok(child.input.command.includes(delivery));
 assert.equal(handlers.tool_result({...child,content:[]},ctx),undefined);
 const result=handlers.tool_result({toolCallId:call,content:[]},ctx);
 assert.equal(result.details.simulatorEndpointImages,1);
 assert.equal(result.content[1].data,image.toString('base64'));
 writeFileSync(manifestPath,JSON.stringify({...manifest,image_sha256:'0'.repeat(64)}));
 const rejected=extension.attachReceipts({content:[]},delivery);
 assert.equal(rejected.details.simulatorEndpointImages,0);
 assert.ok(rejected.content[0].text.includes('WARNING: image not attached'));
 const auth=await jiti.import(join(root,'extensions/auth-isolation.ts'));
 let authHook;auth.default({on:(name,handler)=>{if(name==='tool_call')authHook=handler;}});
 const check={toolName:'bash',input:{command:'test -z "${OPENAI_API_KEY:-}"'}};
 authHook(check);
 const shell=spawnSync('/bin/bash',['-c',check.input.command],{env:{...process.env,OPENAI_API_KEY:'synthetic-fixture'}});
 assert.equal(shell.status,0,'tool subprocess must not receive the model key');
 for(const input of [{command:'cat /proc/$PPID/environ'},{path:'/proc/123/environ'}])
  assert.equal(authHook({toolName:input.path?'read':'bash',input})?.block,true,'process environment must be refused');
 assert.equal(authHook({toolName:'bash',input:{command:'ls /proc/self/status'}}),undefined);
 console.log('PASS pinned image/state delivery, hash warning, model-key tool isolation, environ refused');
}finally{
 rmSync(temp,{recursive:true,force:true});rmSync(delivery,{recursive:true,force:true});
}
