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
    student = os.path.join('ex15', 'ft_putstr.c')
    helpers = {'ft_putchar.c': '#include <unistd.h>\nvoid ft_putchar(char c){write(1,&c,1);}\n'}
    main_src = 'void ft_putstr(char *str);\nint main(void){ ft_putstr("Hello"); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, helpers=helpers, timeout=6, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == 'Hello':
        print('ex15: OK')
        return
    fail(f'ex15 output mismatch: got {out!r}, expected "Hello"')


if __name__ == '__main__':
    main()
