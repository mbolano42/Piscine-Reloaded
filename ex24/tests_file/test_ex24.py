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
    makefile = os.path.join(ROOT, 'ex24', 'Makefile')
    if not os.path.exists(makefile):
        fail('Makefile not found in ex24')
    with tempfile.TemporaryDirectory() as td:
        shutil.copy2(makefile, os.path.join(td, 'Makefile'))
        os.makedirs(os.path.join(td, 'srcs'))
        os.makedirs(os.path.join(td, 'includes'))
        with open(os.path.join(td, 'srcs', 'ft_dummy.c'), 'w') as f:
            f.write('int dummy(void){return 0;}\n')
        with open(os.path.join(td, 'includes', 'ft_dummy.h'), 'w') as f:
            f.write('int dummy(void);\n')
        p = subprocess.run(['make'], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
        if p.returncode != 0:
            fail('make failed: ' + p.stderr)
        if not os.path.exists(os.path.join(td, 'libft.a')):
            fail('libft.a not created')
        if not any(name.endswith('.o') for name in os.listdir(td)) and not any(name.endswith('.o') for name in os.listdir(os.path.join(td, 'srcs'))):
            fail('no object files found after make')
        p = subprocess.run(['make', 'clean'], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
        if p.returncode != 0:
            fail('make clean failed: ' + p.stderr)
        if any(name.endswith('.o') for name in os.listdir(td)) or any(name.endswith('.o') for name in os.listdir(os.path.join(td, 'srcs'))):
            fail('object files remain after clean')
        p = subprocess.run(['make', 'fclean'], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
        if p.returncode != 0:
            fail('make fclean failed: ' + p.stderr)
        if os.path.exists(os.path.join(td, 'libft.a')):
            fail('libft.a remains after fclean')
        p = subprocess.run(['make', 're'], cwd=td, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
        if p.returncode != 0:
            fail('make re failed: ' + p.stderr)
        if not os.path.exists(os.path.join(td, 'libft.a')):
            fail('libft.a not recreated by re')
        print('ex24: OK')


if __name__ == '__main__':
    main()
