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
    script = os.path.join(ROOT, 'ex03', 'find_sh.sh')
    if not os.path.exists(script):
        fail('find_sh.sh not found in ex03')
    # Expected: list of basenames without .sh for all .sh files under ex03
    expected = []
    for root, dirs, files in os.walk(os.path.join(ROOT, 'ex03')):
        for f in files:
            if f.endswith('.sh'):
                expected.append(os.path.splitext(f)[0])
    expected = sorted(set(expected))
    try:
        p = subprocess.run(['sh', script], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=8)
    except subprocess.TimeoutExpired:
        fail('find_sh.sh timed out')
    out = p.stdout.splitlines()
    out = [line.strip() for line in out if line.strip()]
    if sorted(out) == expected:
        print('ex03: OK')
        return
    fail(f'output mismatch. expected {expected!r}, got {out!r}')


if __name__ == '__main__':
    main()
