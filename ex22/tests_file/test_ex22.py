#!/usr/bin/env python3
import os
import sys
import subprocess
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def main():
    header = os.path.join(ROOT, 'ex22', 'ft_abs.h')
    if not os.path.exists(header):
        fail('ft_abs.h not found')
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, 'main.c')
        with open(src, 'w') as f:
            f.write('#include <stdio.h>\n#include "%s"\nint main(void){ printf("%%d %%d\n", ABS(-42), ABS(7)); return 0; }\n' % header)
        p = subprocess.run(['gcc', '-Wall', '-Wextra', '-Werror', 'main.c', '-o', 'a.out'], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=8)
        if p.returncode != 0:
            fail('compile failed: ' + p.stderr)
        r = subprocess.run(['./a.out'], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=4)
        if r.stdout.strip() == '42 7':
            print('ex22: OK')
            return
        fail(f'ex22 output mismatch: {r.stdout!r}')


if __name__ == '__main__':
    main()
