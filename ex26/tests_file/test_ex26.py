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
    student = os.path.join('ex26', 'ft_count_if.c')
    main_src = '#include <stdio.h>\nint ft_count_if(char **tab, int (*f)(char*));\nint is_a(char *s){ return s && s[0] == \'a\'; }\nint main(void){ char *tab[] = {"apple", "banana", "avocado", 0}; printf("%d\\n", ft_count_if(tab, &is_a)); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, timeout=6, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == '2':
        print('ex26: OK')
        return
    fail(f'ex26 output mismatch: got {out!r}, expected "2"')


if __name__ == '__main__':
    main()
