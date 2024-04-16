"""
Backward-compatability shims to support Python 3.9 and earlier.
"""

import sys
import test.support
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


class support_compat:
    if sys.version_info < (3, 10):
        def check__all__(test_case, mod, *, not_exported=(), **kwargs):
            kwargs.update(blacklist=not_exported)
            return test.support.check__all__(test_case, mod, **kwargs)


support = types.SimpleNamespace(**{**vars(test.support), **vars(support_compat)})
