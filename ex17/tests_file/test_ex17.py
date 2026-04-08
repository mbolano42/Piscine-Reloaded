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
    student = os.path.join('ex17', 'ft_strcmp.c')
    main_src = '#include <stdio.h>\nint ft_strcmp(char *s1, char *s2);\nint main(void){ printf("%d %d %d\\n", ft_strcmp("abc","abc"), ft_strcmp("abc","abd") < 0, ft_strcmp("abd","abc") > 0); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, timeout=6, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip().split()
    if len(out) == 3 and out[0] == '0' and out[1] == '1' and out[2] == '1':
        print('ex17: OK')
        return
    fail(f'ex17 output mismatch: got {out!r}')


if __name__ == '__main__':
    main()
