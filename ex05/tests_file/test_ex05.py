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
    found = tl.find_file_with_substr(exdir, 'MaRViN')
    if not found:
        fail('No file with "MaRViN" found in filename under ex05')
    with open(found, 'rb') as f:
        data = f.read()
    if data == b'42':
        print('ex05: OK')
        return
    fail(f'file {found} does not contain exactly "42"')


if __name__ == '__main__':
    main()
