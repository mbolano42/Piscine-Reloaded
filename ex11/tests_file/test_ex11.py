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
    student = os.path.join('ex11', 'ft_div_mod.c')
    main_src = '#include <stdio.h>\nvoid ft_div_mod(int a, int b, int *div, int *mod);\nint main(void){ int d,m; ft_div_mod(7,3,&d,&m); printf("%d %d\n", d, m); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, timeout=8, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == '2 1':
        print('ex11: OK')
        return
    fail(f'ex11 output mismatch: got {out!r}, expected "2 1"')


if __name__ == '__main__':
    main()
