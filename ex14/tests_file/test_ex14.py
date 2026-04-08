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
    student = os.path.join('ex14', 'ft_sqrt.c')
    main_src = '#include <stdio.h>\nint ft_sqrt(int nb);\nint main(void){ printf("%d %d %d\\n", ft_sqrt(4), ft_sqrt(5), ft_sqrt(9)); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, timeout=6, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == '2 0 3':
        print('ex14: OK')
        return
    fail(f'ex14 output mismatch: got {out!r}, expected "2 0 3"')


if __name__ == '__main__':
    main()
