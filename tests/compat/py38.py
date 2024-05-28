import contextlib
import random
import sys
import test.support
import types
import unittest

from jaraco.test.cpython import from_test_support, try_import


warnings_helper = try_import('warnings_helper') or from_test_support('check_warnings')


class support_compat:
    if sys.version_info < (3, 9):
        def requires_zlib(reason='requires zlib'):
            try:
                import zlib
            except ImportError:
                zlib = None
            return unittest.skipUnless(zlib, reason)

        def requires_gzip(reason='requires gzip'):
            try:
                import gzip
            except ImportError:
                gzip = None
            return unittest.skipUnless(gzip, reason)

        def requires_bz2(reason='requires bz2'):
            try:
                import bz2
            except ImportError:
                bz2 = None
            return unittest.skipUnless(bz2, reason)

        def requires_lzma(reason='requires lzma'):
            try:
                import lzma
            except ImportError:
                lzma = None
            return unittest.skipUnless(lzma, reason)


support = types.SimpleNamespace(**{**vars(test.support), **vars(support_compat)})


class RandomCompat(random.Random):
    def randbytes(self, n):
        """Generate n random bytes."""
        return self.getrandbits(n * 8).to_bytes(n, 'little')


Random = RandomCompat if sys.version_info < (3, 9) else random.Random


if sys.version_info < (3, 9):

    def removesuffix(self, suffix):
        # suffix='' should not call self[:-0].
        if suffix and self.endswith(suffix):
            return self[: -len(suffix)]
        else:
            return self[:]

    def removeprefix(self, prefix):
        if self.startswith(prefix):
            return self[len(prefix) :]
        else:
            return self[:]
else:

    def removesuffix(self, suffix):
        return self.removesuffix(suffix)

    def removeprefix(self, prefix):
        return self.removeprefix(prefix)


@contextlib.contextmanager
def temp_tarfile_open(DIR, tarname):
    """
    Syntax compatibility for Python 3.8 for:

    ```
    with (
        os_helper.temp_dir(DIR),
        tarfile.open(tarname, encoding="iso8859-1") as tar
    ):
    ```
    """
    from .py310 import os_helper
    import tarfile
    with os_helper.temp_dir(DIR), tarfile.open(tarname, encoding="iso8859-1") as tar:
        yield tar
