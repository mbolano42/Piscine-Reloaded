#!/usr/bin/env python3
import os
import sys
import subprocess
import tempfile
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def main():
    header = os.path.join(ROOT, 'ex23', 'ft_point.h')
    if not os.path.exists(header):
        fail('ft_point.h not found')
    with tempfile.TemporaryDirectory() as td:
        shutil.copy2(header, os.path.join(td, 'ft_point.h'))
        with open(os.path.join(td, 'main.c'), 'w') as f:
            f.write('#include "ft_point.h"\nint main(void){ t_point p; p.x = 1; p.y = 2; return (p.x + p.y != 3); }\n')
        p = subprocess.run(['gcc', '-Wall', '-Wextra', '-Werror', 'main.c', '-o', 'a.out'], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=8)
        if p.returncode != 0:
            fail('compile failed: ' + p.stderr)
        r = subprocess.run(['./a.out'], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=4)
        if r.returncode == 0:
            print('ex23: OK')
            return
        fail('program returned non-zero')


if __name__ == '__main__':
    main()
