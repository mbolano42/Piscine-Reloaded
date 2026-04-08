#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def fail(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def main():
    exdir = os.path.join(ROOT, 'ex27')
    makefile = os.path.join(exdir, 'Makefile')
    if not os.path.exists(makefile):
        fail('Makefile not found in ex27')
    with tempfile.TemporaryDirectory() as td:
        shutil.copy2(makefile, os.path.join(td, 'Makefile'))
        # Copy all source files from ex27 except tests
        for name in os.listdir(exdir):
            if name.endswith('.c') or name.endswith('.h') or name == 'Makefile':
                src = os.path.join(exdir, name)
                if os.path.isfile(src) and name != 'Makefile':
                    shutil.copy2(src, os.path.join(td, name))
        p = subprocess.run(['make'], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=15)
        if p.returncode != 0:
            fail('make failed: ' + p.stderr)
        bin_path = os.path.join(td, 'ft_display_file')
        if not os.path.exists(bin_path):
            fail('ft_display_file binary not created')
        sample = os.path.join(td, 'sample.txt')
        with open(sample, 'w') as f:
            f.write('abc\nxyz\n')
        r = subprocess.run([bin_path, sample], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        if r.stdout == 'abc\nxyz\n':
            noarg = subprocess.run([bin_path], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            if noarg.stderr.strip() != 'File name missing.':
                fail(f'ex27 missing-arg error mismatch: {noarg.stderr!r}')
            many = subprocess.run([bin_path, sample, sample], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            if many.stderr.strip() != 'Too many arguments.':
                fail(f'ex27 too-many-args error mismatch: {many.stderr!r}')
            missing = subprocess.run([bin_path, os.path.join(td, 'no_such_file.txt')], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            if missing.stderr.strip() != 'Cannot read file.':
                fail(f'ex27 unreadable-file error mismatch: {missing.stderr!r}')
            print('ex27: OK')
            return
        fail(f'ex27 output mismatch: {r.stdout!r}')


if __name__ == '__main__':
    main()
