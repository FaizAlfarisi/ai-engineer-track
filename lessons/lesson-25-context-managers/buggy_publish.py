"""Dawn publish guards — PROVIDED, BUGGY (H1).

Four planted bugs, one per Pitfall. Nothing else in this file is wrong.
You fix it in place: run the DEBUGGING protocol, fix each where it lives,
do not restructure the module. One 7-row chain per bug, filled as you fix.

Exports: Timer, AtomicWriter, Opener, timed.
"""

import time
from contextlib import contextmanager
from pathlib import Path


class Timer:
    """Elapsed wall time of a block, even when it raises."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        return False


class AtomicWriter:
    """Whole-or-absent file replacement via a temp sibling."""

    def __init__(self, target):
        self._target = Path(target)
        self._draft = self._target.with_suffix(".tmp")

    def __enter__(self):
        self._handle = self._draft.open("w", encoding="utf-8")
        return self._handle

    def __exit__(self, exc_type, exc_value, traceback):
        self._handle.close()
        if exc_type is None:
            self._draft.replace(self._target)
        else:
            self._draft.unlink(missing_ok=True)
        return False


class Opener:
    """Open a path for writing and hand over the handle."""

    def __init__(self, path):
        self._path = Path(path)

    def __enter__(self):
        self._handle = self._path.open("w", encoding="utf-8")
        return self._handle

    def __exit__(self, exc_type, exc_value, traceback):
        self._handle.close()
        return False


@contextmanager
def timed():
    """Elapsed wall time of a block, on any exit path."""
    record = {"elapsed": 0.0}
    start = time.perf_counter()
    try:
        yield record
    finally:
        record["elapsed"] = time.perf_counter() - start
