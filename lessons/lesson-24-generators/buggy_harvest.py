"""Greenhouse harvest helpers — PROVIDED, BUGGY (H1).

Four planted bugs, one per Pitfall. Nothing else in this file is wrong.
You fix it in place: run the DEBUGGING protocol, fix each where it lives,
do not restructure the module. One 7-row chain per bug, filled as you fix.

Exports: harvest_count, hot_lines, lazy_valid, collect.
"""


def harvest_count(stream):
    """(total items, collected items) from one pass."""
    total = 0
    got = []
    
    for item in stream:
        total += 1
        got.append(item)
    
    return total, got


def hot_lines(readings, threshold):
    """Yield readings strictly over threshold."""
    return (r for r in readings if r > threshold)


def lazy_valid(source):
    """Yield items over zero, pulling the source minimally."""
    return (x for x in source if x > 0)


def collect(source):
    """Collect source items into a fresh list."""
    acc = []
    for x in source:
        acc.append(x)
    return acc
