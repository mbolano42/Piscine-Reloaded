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
    path = os.path.join(ROOT, 'ex01', 'z')
    if not os.path.exists(path):
        fail('z not found in ex01')
    with open(path, 'rb') as f:
        data = f.read()
    if data == b'Z\n':
        print('ex01: OK')
        return
    fail('z content incorrect (expected exactly "Z\\n")')


if __name__ == '__main__':
    main()
