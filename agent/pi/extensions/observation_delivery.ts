// Attaches each robot endpoint image + state receipt (written by sim_client) to the tool result the model
// sees, including bash calls nested inside codemode. Loaded by every practice and evaluation session.
// Transport only: no motion API and no history pruning.
import {createHash} from 'node:crypto';
import {existsSync,readdirSync,readFileSync,realpathSync,statSync} from 'node:fs';
import {basename,dirname,join} from 'node:path';
import type {ExtensionAPI} from '@earendil-works/pi-coding-agent';

export function deliveryDirectory(sessionId:string,rootCallId:string){
 return join('/tmp/behavior-sim-delivery',createHash('sha256').update(sessionId+'\0'+rootCallId).digest('hex'));
}

export function attachReceipts(event:any,directory:string){
 if(!existsSync(directory))return;
 const content=[...event.content];let count=0;
 for(const name of readdirSync(directory).filter(n=>n.endsWith('.json')).sort()){
  try{
   const manifestPath=join(directory,name);
   if(statSync(manifestPath).size>256_000)throw Error('Oversize delivery manifest');
   const m=JSON.parse(readFileSync(manifestPath,'utf8'));
   if(m.observation_contract!==1)throw Error('Unknown observation contract');
   const receipt=realpathSync(m.receipt_file),imagePath=realpathSync(m.image_file);
   if(dirname(receipt)!==dirname(imagePath)||!/^obs_\d+\.jpg$/.test(basename(imagePath))
      ||statSync(receipt).size>2_000_000||statSync(imagePath).size>4_000_000)
    throw Error('Invalid endpoint receipt/image path or size');
   const r=JSON.parse(readFileSync(receipt,'utf8')),image=readFileSync(imagePath);
   if(r.observation_contract!==1||r.observation_id!==m.observation_id||r.attempt_id!==m.attempt_id
      ||realpathSync(r.local_image_path)!==imagePath||r.compact_state!==m.state_text
      ||createHash('sha256').update(image).digest('hex')!==m.image_sha256)
    throw Error('Endpoint receipt/image identity mismatch');
   if(image[0]!==0xff||image[1]!==0xd8)throw Error('Expected JPEG endpoint');
   content.push({type:'text',text:'Automatic simulator endpoint (saved, not a live stream):\n'+m.state_text+'\nReceipt: '+receipt},
                {type:'image',data:image.toString('base64'),mimeType:'image/jpeg'});
   count++;
  }catch(error){
   content.push({type:'text',text:'WARNING: image not attached — receipt '+join(directory,name)+' failed: '+String(error)});
  }
 }
 if(content.length===event.content.length)return;
 return {content,structuredContent:event.structuredContent,
         details:{...event.details,simulatorEndpointImages:count}};
}

export default function(pi:ExtensionAPI){
 const roots=new Map<string,string>();
 pi.on('tool_call',(event,ctx)=>{
  const root=event.parentToolCallId?(roots.get(event.parentToolCallId)??event.parentToolCallId):event.toolCallId;
  roots.set(event.toolCallId,root);
  if(event.toolName!=='bash'||typeof event.input.command!=='string')return;
  const directory=deliveryDirectory(ctx.sessionManager.getSessionId(),root);
  // Scoped to this shell and its ordinary child processes, never mutable process-global env.
  event.input.command=`export BEHAVIOR_SIM_DELIVERY_ACTIVE=1 BEHAVIOR_SIM_DELIVERY_DIR='${directory}';\n`+event.input.command;
 });
 pi.on('tool_result',(event,ctx)=>{
  if(event.parentToolCallId)return; // Nested codemode results are intentionally filterable.
  const result=attachReceipts(event,deliveryDirectory(ctx.sessionManager.getSessionId(),event.toolCallId));
  for(const [id,root] of roots)if(root===event.toolCallId)roots.delete(id);
  return result; // Attach at the outer, model-visible boundary even if stdout was discarded.
 });
}
