#!/usr/bin/env python3
"""Scan decoded input fields; scanner failure never passes unexamined content."""
import argparse
import json
from pathlib import Path
import subprocess
import sys


def strings(value):
    if isinstance(value,str):yield value
    elif isinstance(value,list):
        for item in value:yield from strings(item)
    elif isinstance(value,dict):
        for key,item in value.items():yield key;yield from strings(item)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for flag in ['json','strict','silent','report']:p.add_argument('--'+flag,action='store_true')
    p.add_argument('text',nargs='?')
    args=p.parse_args()
    try:
        raw=args.text if args.text is not None else sys.stdin.read(2_000_001)
        if len(raw)>2_000_000:raise ValueError('input exceeds scan limit')
        text='\n'.join(strings(json.loads(raw))) if args.json else raw
        r=subprocess.run(['bash',str(Path(__file__).with_name('clawdefender.sh')),'--check-prompt','true'],input=text,capture_output=True,text=True,timeout=20)
        result=json.loads(r.stdout)
        if r.returncode not in (0,1) or not isinstance(result,dict) or not isinstance(result.get('clean'),bool):
            raise ValueError('scanner unavailable or invalid result')
        if (r.returncode==0) != result['clean']:raise ValueError('scanner status mismatch')
        if args.report:print(json.dumps(result));return 0 if result['clean'] else 1
        if result['clean']:print(raw);return 0
        if args.strict:
            if not args.silent:print('BLOCKED: suspicious input',file=sys.stderr)
            return 1
        print('[FLAGGED UNTRUSTED INPUT]\n'+raw+'\n[END FLAGGED INPUT]')
        return 1
    except (OSError,ValueError,subprocess.SubprocessError):
        if not args.silent:print('BLOCKED: input could not be checked',file=sys.stderr)
        return 2


if __name__=='__main__':sys.exit(main())
