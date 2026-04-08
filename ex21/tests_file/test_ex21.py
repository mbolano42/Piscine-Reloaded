#!/usr/bin/env python3
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)
import tests_lib as tl


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def main():
    student = os.path.join('ex21', 'ft_range.c')
    main_src = '#include <stdio.h>\n#include <stdlib.h>\nint *ft_range(int min, int max);\nint main(void){ int *p = ft_range(2, 6); if(!p) return 1; for(int i = 0; i < 4; i++) printf("%d ", p[i]); free(p); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, timeout=6, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == '2 3 4 5':
        print('ex21: OK')
        return
    fail(f'ex21 output mismatch: got {out!r}, expected "2 3 4 5"')


if __name__ == '__main__':
    main()
