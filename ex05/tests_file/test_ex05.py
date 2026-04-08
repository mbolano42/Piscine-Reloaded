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
    exdir = os.path.join(ROOT, 'ex05')
    # Expected literal filename as specified in the README:
    # "\?$*'MaRViN'*$?\"
    expected = '"' + '\\' + '?' + '$' + '*' + "'" + 'MaRViN' + "'" + '*' + '$' + '?' + '\\' + '"'
    expected_path = os.path.join(exdir, expected)
    if not os.path.exists(expected_path):
        fail(f'Expected file not found: {expected!r} under ex05')
    with open(expected_path, 'rb') as f:
        data = f.read()
    if data == b'42':
        print('ex05: OK')
        return
    fail(f'file {expected_path} does not contain exactly "42"')


if __name__ == '__main__':
    main()
