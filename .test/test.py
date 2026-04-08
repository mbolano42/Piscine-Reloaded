#!/usr/bin/env python3
import os
import sys
import subprocess

# Repository root is the parent directory of this file
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def run_test(ex_name, timeout=20):
    test_path = os.path.join(REPO_ROOT, ex_name, 'tests_file', f'test_{ex_name}.py')
    if not os.path.exists(test_path):
        print(f"{ex_name}: MISSING test file at {test_path}")
        return False
    print(f"Running {ex_name} ...")
    try:
        # ensure the child Python processes can import the helpers in .test
        env = os.environ.copy()
        test_pkg_dir = os.path.join(REPO_ROOT, '.test')
        existing_py = env.get('PYTHONPATH', '')
        env['PYTHONPATH'] = test_pkg_dir + (os.pathsep + existing_py if existing_py else '')
        p = subprocess.run(['python3', test_path], cwd=REPO_ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
        ok = p.returncode == 0
        if ok:
            print(f"{ex_name}: PASS")
            if p.stdout.strip():
                print(p.stdout)
            return True
        else:
            print(f"{ex_name}: FAIL (exit {p.returncode})")
            if p.stdout.strip():
                print("STDOUT:\n" + p.stdout)
            if p.stderr.strip():
                print("STDERR:\n" + p.stderr)
            return False
    except subprocess.TimeoutExpired:
        print(f"{ex_name}: TIMEOUT (> {timeout}s)")
        return False


def main():
    args = sys.argv[1:]
    ex_list = [f"ex{str(i).zfill(2)}" for i in range(28)]
    if len(args) == 1:
        ex_arg = args[0]
        if ex_arg not in ex_list:
            print(f"Unknown exercise '{ex_arg}'")
            sys.exit(2)
        ex_list = [ex_arg]
    results = {}
    for ex in ex_list:
        ok = run_test(ex, timeout=20)
        results[ex] = ok
    print("\nSummary:")
    for ex, ok in results.items():
        print(f"- {ex}: {'PASS' if ok else 'FAIL'}")
    sys.exit(0 if all(results.values()) else 1)


if __name__ == '__main__':
    main()
