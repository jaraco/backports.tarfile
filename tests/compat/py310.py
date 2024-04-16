import test.support
import test.support.os_helper
import types


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


os_helper = types.SimpleNamespace(**{**vars(os_helper_compat), **vars(test.support.os_helper)})


class support_compat:
    def is_emscripten():
        return False

    def is_wasi():
        return False


support = types.SimpleNamespace(**{**vars(support_compat), **vars(test.support)})
