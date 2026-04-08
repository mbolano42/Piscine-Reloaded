#!/usr/bin/env python3
"""
Root shim for `tests_lib`.

This file lets editors and quick imports resolve `import tests_lib` even when the
real implementation lives in `.test/tests_lib.py`. At runtime it attempts to
load and re-export the implementation from `.test/tests_lib.py`; if that file
is missing it provides lightweight stubs that raise a clear ImportError when
used.
"""
from __future__ import annotations

import importlib.util
import os
import sys

__all__ = []

_impl_path = os.path.join(os.path.dirname(__file__), '.test', 'tests_lib.py')

if os.path.exists(_impl_path):
    try:
        spec = importlib.util.spec_from_file_location('_tests_lib_impl', _impl_path)
        module = importlib.util.module_from_spec(spec)
        # execute the implementation module in its own namespace
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
        # copy public names into this module namespace
        for _name, _val in vars(module).items():
            if _name.startswith('__'):
                continue
            globals()[_name] = _val
            __all__.append(_name)
    except Exception as _e:
        # fall back to clear runtime errors so users see why imports fail
        def _missing(*args, **kwargs):
            raise ImportError("Could not load tests_lib implementation from .test/tests_lib.py: %s" % (_e,))

        run_cmd = _missing
        compile_c = _missing
        compile_and_run_c_test = _missing
        find_file_with_substr = _missing
        tar_contains_expected = _missing
        looks_like_mac = _missing
        __all__ = [
            'run_cmd', 'compile_c', 'compile_and_run_c_test',
            'find_file_with_substr', 'tar_contains_expected', 'looks_like_mac'
        ]
else:
    def _missing(*args, **kwargs):
        raise ImportError("tests_lib implementation not found. Ensure .test/tests_lib.py exists or run tests via the runner (make test).")

    run_cmd = _missing
    compile_c = _missing
    compile_and_run_c_test = _missing
    find_file_with_substr = _missing
    tar_contains_expected = _missing
    looks_like_mac = _missing
    __all__ = [
        'run_cmd', 'compile_c', 'compile_and_run_c_test',
        'find_file_with_substr', 'tar_contains_expected', 'looks_like_mac'
    ]
