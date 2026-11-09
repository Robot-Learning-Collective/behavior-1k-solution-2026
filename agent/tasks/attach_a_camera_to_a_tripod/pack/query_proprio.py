"""Read one nearest recorded sample; never controls a simulator."""
import json
from pathlib import Path
import sys

def main():
    episode, frame = map(int, sys.argv[1:])
    data = json.loads(Path(__file__).with_name('human-proprio.json').read_text())
    record = next(x for x in data['episodes'] if x['episode_index'] == episode)
    sample = min(record['samples'], key=lambda s: abs(s['rgb_frame']-frame))
    print(json.dumps({'requested_frame':frame,'frame_difference':sample['rgb_frame']-frame,'sample':sample}, indent=2))

if __name__ == '__main__':main()
