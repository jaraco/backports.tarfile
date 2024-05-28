import pathlib
import sys
from test import support


def find_file(name, subdir=None):
    return str(pathlib.Path(*filter(None, ('tests', subdir, name))).absolute())


def patch_findfile():
    """
    Early hook to ensure findfile behaves differently before test_tarfile is imported.
    """
    support.findfile = find_file


def backport_as_std():
    """
    Make sure 'import tarfile' gets the backport.
    """
    from backports import tarfile
    sys.modules['tarfile'] = tarfile


def patch_bz2():
    """
    Ensure bz2.BZ2File reflects the name.
    """
    if sys.version_info > (3, 13):
        return
    try:
        import bz2
    except ImportError:
        return

    bz2.BZ2File.name = property(lambda self: self._fp.name)


def patch_lzma():
    """
    Ensure lzma.LZMAFile reflects the name.
    """
    if sys.version_info > (3, 13):
        return
    try:
        import lzma
    except ImportError:
        return

    lzma.LZMAFile.name = property(lambda self: self._fp.name)


def pytest_configure():
    patch_findfile()
    backport_as_std()
    patch_bz2()
    patch_lzma()
