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
    student = os.path.join('ex10', 'ft_swap.c')
    main_src = '#include <stdio.h>\nvoid ft_swap(int *a, int *b);\nint main(void){ int a = 1, b = 2; ft_swap(&a,&b); printf("%d %d\\n", a, b); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, timeout=8, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == '2 1':
        print('ex10: OK')
        return
    fail(f'ex10 output mismatch: got {out!r}, expected "2 1"')


if __name__ == '__main__':
    main()
