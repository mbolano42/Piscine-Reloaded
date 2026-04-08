#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
import tarfile
import tempfile
import re

def run_cmd(cmd, cwd=None, timeout=10, shell=False):
    try:
        proc = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout, shell=shell)
        return {'returncode': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr, 'timed_out': False}
    except subprocess.TimeoutExpired as e:
        return {'returncode': None, 'stdout': e.stdout or '', 'stderr': e.stderr or '', 'timed_out': True}


def compile_c(sources, output, cwd=None, timeout=10):
    cmd = ['gcc', '-Wall', '-Wextra', '-Werror', '-o', output] + sources
    return run_cmd(cmd, cwd=cwd, timeout=timeout)


def compile_and_run_c_test(student_src_paths, main_source_code, helpers=None, expected_stdout=None, args=None, timeout=10, test_cwd=None):
    helpers = helpers or {}
    if test_cwd is None:
        test_cwd = os.getcwd()
    # create a unique temporary build directory per test to avoid collisions
    build_dir = tempfile.mkdtemp(prefix='build_test_', dir=test_cwd)
    try:
        sources_copied = []
        for path in student_src_paths:
            src_path = path if os.path.isabs(path) else os.path.join(test_cwd, path)
            src_path = os.path.abspath(src_path)
            if os.path.exists(src_path):
                dest = os.path.join(build_dir, os.path.basename(path))
                shutil.copy2(src_path, dest)
                sources_copied.append(os.path.basename(path))
            else:
                return {'ok': False, 'reason': f'Missing student source: {path}', 'compile': None, 'run': None}

        for fname, content in helpers.items():
            with open(os.path.join(build_dir, fname), 'w') as f:
                f.write(content)
            sources_copied.append(fname)

        main_name = 'main_test.c'
        with open(os.path.join(build_dir, main_name), 'w') as f:
            f.write(main_source_code)
        sources_copied.append(main_name)

        compile_result = compile_c(sources_copied, 'test_bin', cwd=build_dir, timeout=timeout)
        if compile_result['timed_out']:
            return {'ok': False, 'reason': 'compile_timeout', 'compile': compile_result, 'run': None}
        if compile_result['returncode'] != 0:
            return {'ok': False, 'reason': 'compile_error', 'compile': compile_result, 'run': None}

        run = run_cmd(['./test_bin'] + (args or []), cwd=build_dir, timeout=timeout)
        if run['timed_out']:
            return {'ok': False, 'reason': 'run_timeout', 'compile': compile_result, 'run': run}

        if expected_stdout is not None:
            # Compare exact output (do not strip, caller expects exact text)
            if run['stdout'] == expected_stdout:
                return {'ok': True, 'compile': compile_result, 'run': run}
            else:
                return {'ok': False, 'reason': 'output_mismatch', 'compile': compile_result, 'run': run, 'expected': expected_stdout}

        return {'ok': True, 'compile': compile_result, 'run': run}
    finally:
        try:
            shutil.rmtree(build_dir)
        except Exception:
            pass


def find_file_with_substr(root_dir, substr):
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if substr in f:
                return os.path.join(root, f)
    return None


def tar_contains_expected(tar_path, expected_names):
    try:
        with tarfile.open(tar_path) as tar:
            members = {os.path.basename(m.name): m for m in tar.getmembers()}
    except Exception as e:
        return False, f'cannot open tar: {e}'
    missing = [n for n in expected_names if n not in members]
    if missing:
        return False, f'missing entries: {missing}'
    return True, members


def looks_like_mac(text):
    # Simple MAC address regex
    m = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', text)
    return bool(m)
