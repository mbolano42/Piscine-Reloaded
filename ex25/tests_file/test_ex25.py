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
    student = os.path.join('ex25', 'ft_foreach.c')
    main_src = '#include <stdio.h>\nvoid ft_foreach(int *tab, int length, void (*f)(int));\nvoid print_int(int n){ printf("%d ", n); }\nint main(void){ int tab[] = {1,2,3}; ft_foreach(tab, 3, &print_int); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, timeout=6, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == '1 2 3':
        print('ex25: OK')
        return
    fail(f'ex25 output mismatch: got {out!r}, expected "1 2 3"')


if __name__ == '__main__':
    main()
