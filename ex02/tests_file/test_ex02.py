#!/usr/bin/env python3
import os
import sys
import re

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
    path = os.path.join(ROOT, 'ex02', 'clean')
    if not os.path.exists(path):
        fail('clean not found in ex02')
    with open(path, 'r') as f:
        content = f.read().strip()
    if ';' in content or '&&' in content or '||' in content:
        fail('clean contains command chaining which is not allowed')
    if 'find' not in content:
        fail('clean should use find')
    # Check for patterns roughly matching deletion and temp file names
    if ('~' not in content) and ('#' not in content):
        fail('clean does not look for "~" or "#...#" temporary files')
    if ('-delete' not in content) and (r'-exec rm' not in content) and (r'-exec rm -f' not in content):
        fail('clean should remove found files (contains no -delete or -exec rm)')
    print('ex02: OK')


if __name__ == '__main__':
    main()
