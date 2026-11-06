"""Single-rollout official WebSocket policy + endpoint-only HTTP sim_client bridge.

CPU only. No simulator imports. Native protocol matches pinned3.9.3 network_utils;
NumPy/msgpack only (never pickle). Agent sees allowlisted observations, no scores.
"""
import argparse
import asyncio
import base64
import copy
import hashlib
import http
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import io
import json
from pathlib import Path
import threading
import time
import urllib.request
import uuid
import msgpack
import numpy as np
from PIL import Image
from official_controller import OfficialControllerPolicy


def pack_data(obj):
    if isinstance(obj,np.ndarray):
        if obj.dtype.kind in ('V','O','c'):raise ValueError('Unsupported dtype')
        return {b'__ndarray__':True,b'data':obj.tobytes(),b'dtype':obj.dtype.str,b'shape':obj.shape}
    if isinstance(obj,np.generic):return {b'__npgeneric__':True,b'data':obj.item(),b'dtype':obj.dtype.str}
    raise TypeError(type(obj).__name__)


def unpack_data(obj):
    if b'__ndarray__' in obj:
        dtype=np.dtype(obj[b'dtype'])
        if dtype.kind in ('V','O','c'):raise ValueError('Unsupported dtype')
        return np.ndarray(buffer=obj[b'data'],dtype=dtype,shape=obj[b'shape'])
    if b'__npgeneric__' in obj:return np.dtype(obj[b'dtype']).type(obj[b'data'])
    return obj


def pack(obj):return msgpack.packb(obj,default=pack_data)
def unpack(raw):return msgpack.unpackb(raw,object_hook=unpack_data,strict_map_key=False)


def post(url,data):
    request=urllib.request.Request(url,data=json.dumps(data).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(request,timeout=30) as response:return json.load(response)


def endpoint(packet,epoch,result=None,ended=False):
    """Same canonical image/depth/state wire shape as practice, without simulator IO."""
    depth=io.BytesIO();np.savez_compressed(depth,**packet['depth']);depth=depth.getvalue()
    canvas=Image.new('RGB',(1680,720));panels={};x=0
    for name in ('left','head','right'):
        image=Image.fromarray(packet['rgb'][name]);w,h=image.size
        canvas.paste(image,(x,0));panels[name]={'rgb_xywh':[x,0,w,h]};x+=w
    image=io.BytesIO();canvas.save(image,format='JPEG',quality=88)
    out={key:packet[key] for key in ('robot','cameras','controller_protocol','observation_id','simulated_seconds','wall_seconds','action_id','last_commanded_grip')}
    out.update(attempt_id='official-'+epoch,capture_monotonic_ns=time.monotonic_ns(),ended=ended,
               image_layout={'dimensions':[1680,720],'camera_panels':panels,'layout':'Native LEFT|HEAD|RIGHT RGB'},
               image_base64=base64.b64encode(image.getvalue()).decode(),
               depth_npz_base64=base64.b64encode(depth).decode(),depth_sha256=hashlib.sha256(depth).hexdigest())
    if result is not None:
        execution={'requested_ticks':None,'executed_ticks':result['steps'],'timeout_ticks':result.get('timeout_ticks'),
                   'stop_reason':result['reason'],'fault':None,'execution_uncertain':False}
        out.update(act_result={**result,'execution':execution},execution=execution)
    return out


class AgentBridge:
    def __init__(self):
        self.cv=threading.Condition();self.policy=None;self.epoch='';self.reset()

    def reset(self):
        with self.cv:
            self.packet=None;self.pending=None;self.active=None;self.responses={};self.waiting=False
            self.finished=False;self.ended=False;self.cancelled=set();self.seen_ids=set();self.error=None;self.cv.notify_all()

    def __call__(self,packet,previous):
        with self.cv:
            self.packet=packet
            if self.active:
                self.responses[self.active]=endpoint(packet,self.epoch,previous,self.ended)
                self.active=None
            self.waiting=True;self.cv.notify_all()
            deadline=min(self.policy.started+self.policy.max_steps,time.monotonic()+599)
            while self.pending is None and not self.finished and not self.ended and not self.error:
                remaining=deadline-time.monotonic()
                if remaining<=0:raise TimeoutError('Waiting for agent exceeded query/episode wall budget')
                self.cv.wait(remaining)
            if self.error:raise RuntimeError(self.error)
            if self.finished or self.ended:return None
            goal=self.pending;self.pending=None;self.active=goal['id'];self.waiting=False
            return goal

    def rpc(self,job):
        if set(job)!={'op','action','request_id'} or job['op'] not in ('observe','act'):raise ValueError('Only observe/act')
        request_id=str(uuid.UUID(job['request_id']))
        with self.cv:
            epoch=self.epoch
            if job['op']=='act' and (self.pending is not None or self.active is not None):raise RuntimeError('Concurrent motion forbidden')
            def wait(predicate):
                deadline=time.monotonic()+599
                while not predicate():
                    if self.error:raise RuntimeError(self.error)
                    if epoch!=self.epoch:raise RuntimeError('Rollout changed; old requests cannot resume')
                    remaining=deadline-time.monotonic()
                    if remaining<=0:raise TimeoutError('Agent RPC deadline exceeded')
                    self.cv.wait(remaining)
            wait(lambda:self.packet is not None and (self.waiting or self.ended))
            if job['op']=='observe':return endpoint({**self.packet,'wall_seconds':time.monotonic()-self.policy.started},self.epoch,ended=self.ended)
            if self.ended or self.finished:raise RuntimeError('Evaluation ended; no more motion')
            if self.pending is not None or self.active is not None:raise RuntimeError('Concurrent motion forbidden')
            if request_id in self.seen_ids:raise RuntimeError('Replayed motion forbidden')
            goal=job['action']
            if goal['id']!=request_id:raise ValueError('Goal/request ID mismatch')
            copy.deepcopy(self.policy.controller).step(self.packet,goal) # Validate without changing commands.
            self.seen_ids.add(request_id);self.pending=goal;self.cv.notify_all()
            wait(lambda:request_id in self.responses)
            return self.responses.pop(request_id)

    def end(self,flat):
        with self.cv:
            self.ended=True;self.waiting=True
            if self.policy.started is not None:self.packet=self.policy.observation(flat)
            if self.active and self.packet is not None:
                result={**self.policy.controller.result,'reason':'episode_ended','achieved':False}
                self.responses[self.active]=endpoint(self.packet,self.epoch,result,True);self.active=None
            self.cv.notify_all()
            if hasattr(self,'output'):self.output.write_text(json.dumps(self.report(),indent=2)+'\n')

    def report(self):
        p=self.policy
        return {'native_actions':p.tick,'reset_count':p.reset_count,'completed_goals':p.completed_goals,
                'last_goal':p.controller.result,'max_query_seconds':max(p.query_seconds,default=0),
                'wall_seconds':time.monotonic()-p.started if p.started else None,'epoch':self.epoch,'error':self.error}


def handler_for(bridge):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args):pass
        def do_GET(self):
            if self.path!='/healthz':self.send_error(404);return
            self.send_response(200);self.end_headers();self.wfile.write(b'OK')
        def do_POST(self):
            try:
                size=int(self.headers.get('Content-Length',0))
                if not 0<size<40_000_000:raise ValueError('Request size')
                raw=self.rfile.read(size)
                if self.path=='/end':bridge.end(unpack(raw));result={'ended':True}
                else:
                    if self.headers.get('X-Behavior-Rollout')!=bridge.epoch:raise ValueError('Wrong/stale rollout binding')
                    data=json.loads(raw)
                    if self.path=='/rpc':result=bridge.rpc(data)
                    elif self.path=='/cancel':
                        with bridge.cv:bridge.cancelled.add(str(uuid.UUID(data['request_id'])));bridge.cv.notify_all()
                        result={'cancel_requested':True}
                    elif self.path=='/finish':
                        with bridge.cv:
                            bridge.finished=True
                            if bridge.active:bridge.cancelled.add(bridge.active)
                            bridge.cv.notify_all()
                        result={'finished':True,'semantics':'agent finished; evaluator owns termination/scoring'}
                    else:raise ValueError('Unknown operation; reset/snapshot/truth unavailable')
                payload=json.dumps(result,allow_nan=False).encode()
            except Exception as error:payload=json.dumps({'error':str(error),'fatal':True}).encode()
            self.send_response(200);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(payload)));self.end_headers()
            try:self.wfile.write(payload)
            except (BrokenPipeError,ConnectionResetError):pass
    return Handler


async def serve(args):
    from websockets.asyncio.server import serve as ws_serve
    bridge=AgentBridge();profile=json.loads(args.profile.read_text())
    policy=OfficialControllerPolicy(profile,bridge,args.max_steps);bridge.policy=policy;bridge.output=args.output
    http_server=ThreadingHTTPServer(('127.0.0.1',args.http_port),handler_for(bridge))
    threading.Thread(target=http_server.serve_forever,daemon=True).start()
    connected=False
    async def health(connection,request):
        if request.path=='/healthz':return connection.respond(http.HTTPStatus.OK,'OK\n')
    async def connection(ws):
        nonlocal connected
        if connected:await ws.close(code=1013,reason='Single evaluator only');return
        connected=True
        await ws.send(pack({'controller_protocol':6,'action_chunks':False,'wrapper':'RGBDFullResWrapper'}))
        try:
            async for raw in ws:
                data=unpack(raw)
                if data=={'reset':True}:
                    bridge.epoch=uuid.uuid4().hex;policy.reset()
                    receipt=await asyncio.to_thread(post,args.launcher_url+'/reset',{'epoch':bridge.epoch,'max_steps':args.max_steps})
                    if receipt.get('error'):raise RuntimeError(receipt['error'])
                    print('AGENT_FORK_STARTED',json.dumps(receipt),flush=True);continue
                if '__action_chunk_size__' in data:raise ValueError('Action chunks forbidden')
                if policy.goal and policy.goal['id'] in bridge.cancelled:policy.controller.reason='cancelled'
                action=await asyncio.to_thread(policy.act,data) # Event loop stays alive for ping/pong while agent thinks.
                await ws.send(pack({'action':action}))
                if policy.tick%300==0:print('NATIVE_PROGRESS',policy.tick,round(time.monotonic()-policy.started,2),flush=True)
        except Exception as error:
            with bridge.cv:bridge.error=repr(error);bridge.cv.notify_all()
            print('POLICY_SERVER_FAILED',repr(error),flush=True)
            raise
        finally:
            connected=False
            report={'native_actions':policy.tick,'reset_count':policy.reset_count,'completed_goals':policy.completed_goals,
                    'last_goal':policy.controller.result,'max_query_seconds':max(policy.query_seconds,default=0),
                    'wall_seconds':time.monotonic()-policy.started if policy.started else None,'epoch':bridge.epoch,'error':bridge.error}
            args.output.write_text(json.dumps(report,indent=2)+'\n')
    async with ws_serve(connection,'127.0.0.1',args.ws_port,compression=None,max_size=40_000_000,process_request=health):
        print('POLICY_SERVER_READY',flush=True)
        await asyncio.Future()


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--profile',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--max-steps',type=int,required=True);p.add_argument('--ws-port',type=int,default=48731);p.add_argument('--http-port',type=int,default=48732)
    p.add_argument('--launcher-url',default='http://127.0.0.1:48733');asyncio.run(serve(p.parse_args()))
