"""
Backward-compatability shims to support Python 3.9 and earlier.
"""

import sys
from .py38 import support as std_support
import types

from jaraco.test.cpython import from_test_support, try_import

os_helper = try_import('os_helper') or from_test_support(
    'TESTFN',
    'temp_cwd',
    'skip_unless_symlink',
    'unlink',
    'rmtree',
    'temp_dir',
    'change_cwd',
    'create_empty_file',
    'rmdir',
)


class FakePath:
    """Simple implementation of the path protocol.
    """
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f'<FakePath {self.path!r}>'

    def __fspath__(self):
        if (isinstance(self.path, BaseException) or
            isinstance(self.path, type) and
                issubclass(self.path, BaseException)):
            raise self.path
        else:
            return self.path


os_helper.FakePath = getattr(os_helper, 'FakePath', FakePath)


class support_compat:
    if sys.version_info < (3, 10):
        def check__all__(test_case, mod, *, not_exported=(), **kwargs):
            kwargs.update(blacklist=not_exported)
            return std_support.check__all__(test_case, mod, **kwargs)


support = types.SimpleNamespace(**{**vars(std_support), **vars(support_compat)})
