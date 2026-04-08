#!/usr/bin/env python3
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
helpers = os.path.join(ROOT, '.test')
if helpers not in sys.path:
    sys.path.insert(0, helpers)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
import tests_lib as tl


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def main():
    student = os.path.join('ex09', 'ft_ft.c')
    main_src = '#include <stdio.h>\nvoid ft_ft(int *nbr);\nint main(void){ int n = 0; ft_ft(&n); printf("%d\\n", n); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, timeout=8, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == '42':
        print('ex09: OK')
        return
    fail(f'ex09 output mismatch: got {out!r}, expected "42"')


if __name__ == '__main__':
    main()
