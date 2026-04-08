#!/usr/bin/env python3
import os
import sys
import subprocess

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
    student = os.path.join('ex18', 'ft_print_params.c')
    build = os.path.join(ROOT, 'ex18', 'tests_file', 'build_ex18')
    if os.path.exists(build):
        import shutil
        shutil.rmtree(build)
    os.makedirs(build)
    src_path = os.path.join(ROOT, student)
    if not os.path.exists(src_path):
        fail('ft_print_params.c missing')
    import shutil
    shutil.copy2(src_path, os.path.join(build, 'ft_print_params.c'))
    res = tl.compile_c(['ft_print_params.c'], 'a.out', cwd=build, timeout=8)
    if res['returncode'] != 0 or res['timed_out']:
        fail(f'compile failed: {res}')
    run = tl.run_cmd(['./a.out', 'one', 'two', 'three'], cwd=build, timeout=6)
    if run['timed_out']:
        fail('program timed out')
    out = run['stdout'].splitlines()
    if out == ['one', 'two', 'three']:
        print('ex18: OK')
        return
    fail(f'ex18 output mismatch: got {out!r}')


if __name__ == '__main__':
    main()
