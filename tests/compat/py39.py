"""
Backward-compatability shims to support Python 3.9 and earlier.
"""

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
