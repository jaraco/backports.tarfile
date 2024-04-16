import contextlib
import sys
from .py39 import support as std_support
from .py39 import os_helper as std_os_helper
import types
import warnings as std_warnings



try:
    from test import archiver_tests
except ImportError:
    from . import archiver_tests  # noqa: F401


class os_helper_compat:
    def skip_unless_working_chmod(test):
        """Never skip"""
        return test

    def can_chmod():
        return True


os_helper = types.SimpleNamespace(**{**vars(os_helper_compat), **vars(std_os_helper)})


class support_compat:
    def is_emscripten():
        return False

    def is_wasi():
        return False


support = types.SimpleNamespace(**{**vars(support_compat), **vars(std_support)})


class warnings_compat:
    if sys.version_info < (3, 11):
        @contextlib.contextmanager
        def catch_warnings(*, record=False, module=None, action=None, **kwargs):
            with std_warnings.catch_warnings(record=record, module=module) as val:
                if action:
                    std_warnings.simplefilter(action, **kwargs)
                yield val

warnings = types.SimpleNamespace(**{**vars(std_warnings), **vars(warnings_compat)})
