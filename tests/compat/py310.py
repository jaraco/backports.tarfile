try:
    from test import archiver_tests
except ImportError:
    from . import archiver_tests  # noqa: F401
