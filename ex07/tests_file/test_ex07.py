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
    student = os.path.join('ex07', 'ft_print_numbers.c')
    helpers = {'ft_putchar.c': '#include <unistd.h>\nvoid ft_putchar(char c){write(1,&c,1);}\n'}
    main_src = 'void ft_print_numbers(void);\nint main(void){ ft_print_numbers(); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, helpers=helpers, timeout=8, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == '0123456789':
        print('ex07: OK')
        return
    fail(f'ex07 output mismatch: got {out!r}, expected digits 0-9')


if __name__ == '__main__':
    main()
