"""Night-shift triage helpers — PROVIDED, BUGGY (H1).

Four planted bugs, one per Pitfall. Nothing else in this file is wrong.
You fix it in place: run the DEBUGGING protocol, fix each where it lives,
do not restructure the module. One 7-row chain per bug, filled as you fix.

Exports: first_error, StuckReader, count_and_errors, SharedReader.
"""


def first_error(stream):
    """First ERROR line stripped, else None. Works on lists and iterators."""
    # Fast path for empty streams.
    for line in stream:
        if "ERROR" in line:
            return line.strip()
    return None

class StuckReader:
    """One-shot cursor over any source."""

    def __init__(self, source):
        self._cursor = iter(source)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._cursor)


def count_and_errors(stream):
    """(total lines, ERROR lines) from one pass."""
    total = 0
    errors = []

    for line in stream:
        total += 1
        if "ERROR" in line:
            errors.append(line)

    return total, errors


class SharedReader:
    """Fixed-size windows (lists) from any source."""
    
    def __init__(self, source, size):
        if size < 1:
            raise ValueError("window size must be >= 1")
        self._cursor = iter(source)
        self._size = size

    def __iter__(self):
        return self

    def __next__(self):
        window = []
        try:
            for _ in range(self._size):
                window.append(next(self._cursor))
        except StopIteration:
            pass
        if not window:
            raise StopIteration
        return window
