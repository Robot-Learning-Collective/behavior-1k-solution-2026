#!/usr/bin/env python3
"""Live view of what the practice agent sees: the newest endpoint image, refreshed every second.

    agent/practice/bin/live_view.py 8765 [OBS_ROOT]     (default <PRACTICE_HOME>/obs; binds 127.0.0.1)
"""
import json, os, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = int(sys.argv[1])
if len(sys.argv) > 2:
    ROOT = Path(sys.argv[2])
else:
    ROOT = Path(os.environ.get('PRACTICE_HOME', Path(__file__).resolve().parents[3] / '.practice')) / 'obs'
PAGE = b"""<!doctype html><meta charset=utf-8><title>Practice live view</title>
<style>body{margin:0;background:#111;color:#ddd;font:14px system-ui}#m{padding:8px 12px}img{width:100%;display:block}
#s{display:flex;gap:4px;overflow-x:auto;padding:4px}#s img{width:240px;flex:none;cursor:pointer}</style>
<div id=m>waiting for the first observation...</div><img id=i><div id=s></div>
<script>let last='';async function tick(){try{const r=await (await fetch('/state')).json();
if(r.latest&&r.latest!==last){last=r.latest;i.src='/img?p='+encodeURIComponent(r.latest);
m.textContent=r.attempt+' | '+r.name+' | '+r.count+' endpoints in this attempt | '+r.mtime;
s.innerHTML=r.recent.map(p=>'<img src="/img?p='+encodeURIComponent(p)+'" onclick="i.src=this.src">').join('')}}catch(e){}
setTimeout(tick,1000)}tick()</script>"""


def images():
    return sorted(ROOT.rglob('obs_*.jpg'), key=lambda p: p.stat().st_mtime)


class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def send(self, body, kind):
        self.send_response(200); self.send_header('Content-Type', kind)
        self.send_header('Cache-Control', 'no-store'); self.send_header('Content-Length', str(len(body)))
        self.end_headers(); self.wfile.write(body)

    def do_GET(self):
        if self.path == '/':
            return self.send(PAGE, 'text/html')
        if self.path == '/state':
            imgs = images(); latest = imgs[-1] if imgs else None
            same = [p for p in imgs if latest and p.parent == latest.parent]
            import time
            return self.send(json.dumps({'latest': str(latest) if latest else None,
                'attempt': latest.parent.name if latest else '', 'name': latest.name if latest else '',
                'count': len(same), 'mtime': time.strftime('%H:%M:%S', time.localtime(latest.stat().st_mtime)) if latest else '',
                'recent': [str(p) for p in same[-12:][::-1]]}).encode(), 'application/json')
        if self.path.startswith('/img?p='):
            from urllib.parse import unquote
            p = Path(unquote(self.path[7:])).resolve()
            if ROOT.resolve() in p.parents and p.suffix == '.jpg' and p.is_file():
                return self.send(p.read_bytes(), 'image/jpeg')
        self.send_error(404)


ThreadingHTTPServer(('127.0.0.1', PORT), H).serve_forever()
