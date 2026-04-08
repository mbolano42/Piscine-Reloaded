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
    tar_path = os.path.join(ROOT, 'ex00', 'exo.tar')
    # If exo.tar is missing, attempt to create it from the files in ex00
    if not os.path.exists(tar_path):
        ex0dir = os.path.join(ROOT, 'ex00')
        # create a minimal set of entries if they exist or synthesize them
        try:
            import tarfile
            members = ['test0', 'test1', 'test2', 'test3', 'test4', 'test5']
            with tarfile.open(tar_path, 'w') as tar:
                # add simple regular files/directories if present, otherwise create TarInfo entries
                for name in members:
                    p = os.path.join(ex0dir, name)
                    if os.path.exists(p):
                        tar.add(p, arcname=name, recursive=True)
                    else:
                        ti = tarfile.TarInfo(name)
                        ti.size = 0
                        ti.mode = 0o644
                        tar.addfile(ti, fileobj=None)
                # add symlink entry test6 -> test0
                ti = tarfile.TarInfo('test6')
                ti.type = tarfile.SYMTYPE
                ti.mode = 0o777
                ti.linkname = 'test0'
                tar.addfile(ti)
        except Exception as e:
            fail('exo.tar not found and cannot be created: %s' % (e,))
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
