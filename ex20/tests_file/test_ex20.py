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
    student = os.path.join('ex20', 'ft_strdup.c')
    main_src = '#include <stdio.h>\n#include <stdlib.h>\nchar *ft_strdup(char *src);\nint main(void){ char *p = ft_strdup("hello"); if(!p) return 1; printf("%s\\n", p); free(p); return 0; }\n'
    res = tl.compile_and_run_c_test([student], main_src, timeout=6, test_cwd=ROOT)
    if not res['ok']:
        fail(f"compile/run failed: {res.get('reason')}\ncompile: {res.get('compile')}\nrun: {res.get('run')}")
    out = res['run']['stdout'].strip()
    if out == 'hello':
        print('ex20: OK')
        return
    fail(f'ex20 output mismatch: got {out!r}, expected "hello"')


if __name__ == '__main__':
    main()
