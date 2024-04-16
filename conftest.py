import pathlib
from test import support


def find_file(name, subdir=None):
    return str(pathlib.Path(*filter(None, ('tests', subdir, name))).absolute())


def patch_findfile():
    """
    Early hook to ensure findfile behaves differently before test_tarfile is imported.
    """
    support.findfile = find_file


def pytest_configure():
    patch_findfile()
