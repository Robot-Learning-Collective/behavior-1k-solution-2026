"""Exact-key scan before pushing a branch or publishing an image; the key stays in memory, never printed.

python -m agent.eval.check_secret --env-file /private/openai.env --base origin/main --image <built-image>

Scans the complete PR diff, changed/untracked file contents (including decompressed
session gzip members), and Docker image config/history/layers via streaming save.
It does not scan runtime containers, which intentionally receive runtime auth.
"""
import argparse
import gzip
import io
from pathlib import Path
import shlex
import subprocess
import tarfile


def scan(stream,key):
    tail=b''
    while chunk:=stream.read(1024*1024):
        joined=tail+chunk
        if key in joined:raise RuntimeError('SECRET DETECTED; refusing qualification/publication')
        tail=joined[-len(key):]


class Prefixed(io.RawIOBase):
    def __init__(self,prefix,stream):self.prefix=prefix;self.stream=stream
    def readable(self):return True
    def readinto(self,buffer):
        data=self.prefix[:len(buffer)]
        self.prefix=self.prefix[len(data):]
        if not data:data=self.stream.read(len(buffer))
        buffer[:len(data)]=data
        return len(data)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--env-file',type=Path,required=True)
    parser.add_argument('--base',default='origin/main')
    parser.add_argument('--image')
    args=parser.parse_args()
    if args.env_file.stat().st_mode & 0o077:raise ValueError('Env file must be private (0600)')
    key=next(shlex.split(line.split('=',1)[1])[0].encode() for line in args.env_file.read_text().splitlines()
             if line.startswith('OPENAI_API_KEY='))
    if not key:raise ValueError('Missing model key')
    root=Path(__file__).resolve().parents[2]
    def git(*command):return subprocess.check_output(['git','-C',str(root),*command])
    scan(io.BytesIO(git('diff','--binary',args.base)),key)
    paths=set(git('diff','--name-only','-z',args.base).split(b'\0'))
    paths.update(git('ls-files','--others','--exclude-standard','-z').split(b'\0'))
    count=0
    for name in paths:
        if not name:continue
        path=root/name.decode()
        if not path.is_file():continue
        with path.open('rb') as stream:scan(stream,key)
        if path.suffix=='.gz':
            with gzip.open(path,'rb') as stream:scan(stream,key)
        count+=1
    print('PR_DIFF_AND_CONTENT_KEY_SCAN_PASS',count)
    if not args.image:
        print('IMAGE_KEY_SCAN_NOT_RUN');return
    for command in [['inspect',args.image],['history','--no-trunc',args.image]]:
        scan(io.BytesIO(subprocess.check_output(['docker','image',*command])),key)
    process=subprocess.Popen(['docker','image','save',args.image],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    try:
        with tarfile.open(fileobj=process.stdout,mode='r|*') as archive:
            for member in archive:
                if not member.isfile():continue
                stream=archive.extractfile(member);prefix=stream.read(2)
                reader=io.BufferedReader(Prefixed(prefix,stream))
                if prefix==b'\x1f\x8b':
                    with gzip.GzipFile(fileobj=reader) as decoded:scan(decoded,key)
                else:scan(reader,key)
        if process.wait()!=0:raise RuntimeError('Docker image save failed')
        print('IMAGE_CONFIG_HISTORY_AND_LAYERS_KEY_SCAN_PASS')
    finally:
        if process.poll() is None:process.kill();process.wait()


if __name__=='__main__':main()
