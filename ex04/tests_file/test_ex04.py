#!/usr/bin/env python3
import os
import sys
import subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)
import tests_lib as tl


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def main():
    script = os.path.join(ROOT, 'ex04', 'MAC.sh')
    if not os.path.exists(script):
        fail('MAC.sh not found in ex04')
    try:
        p = subprocess.run(['sh', script], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=8)
    except subprocess.TimeoutExpired:
        fail('MAC.sh timed out')
    out = p.stdout + p.stderr
    if tl.looks_like_mac(out):
        print('ex04: OK')
        return
    fail('MAC.sh output does not contain any MAC-like address')


if __name__ == '__main__':
    main()
