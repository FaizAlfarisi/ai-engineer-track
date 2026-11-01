"""Service-log scan helpers — PROVIDED, BUGGY (H1).

Four planted bugs, one per Pitfall. Nothing else in this file is wrong.
You fix it in place: run the DEBUGGING protocol, fix each where it lives,
do not restructure the module. One 7-row chain per bug, filled as you fix.

Exports: first_pair, is_ping, has_version, count_errors.
"""

import re

PAIR = re.compile(r"error (\d+): ([^,]+)")
PING = re.compile(r"ping (\d+)")
VERSION = re.compile(r"v1\.2")
ERRORS = re.compile(r"^error (\d+)", re.IGNORECASE | re.MULTILINE)


def first_pair(line):
    """First (id, message) pair from a line holding two incidents."""
    m = PAIR.search(line)
    return (m.group(1), m.group(2))


def is_ping(line):
    """True only for exactly 'ping N' with nothing around it."""
    return PING.fullmatch(line) is not None


def has_version(line):
    """True when the literal version v1.2 appears."""
    return VERSION.search(line) is not None


def count_errors(block):
    """Number of error lines in a block, any casing."""
    return len(ERRORS.findall(block))
