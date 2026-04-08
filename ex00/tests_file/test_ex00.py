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
    tar_path = os.path.join(ROOT, 'ex00', 'exo.tar')
    if not os.path.exists(tar_path):
        fail('exo.tar not found in ex00')
    ok, members_or_msg = tl.tar_contains_expected(tar_path, ['test0', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6'])
    if not ok:
        fail('tar content error: ' + str(members_or_msg))
    members = members_or_msg
    if 'test6' not in members:
        fail('test6 missing in tar')
    sym = members['test6']
    try:
        is_sym = sym.issym()
        link = sym.linkname
    except Exception:
        fail('cannot inspect test6 metadata')
    if not is_sym or 'test0' not in (link or ''):
        fail('test6 is not a symlink to test0 (linkname=%s)' % (link,))
    print('ex00: OK')


if __name__ == '__main__':
    main()
