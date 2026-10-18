"""Subscription tenure helpers — PROVIDED, BUGGY (H1).

Four planted bugs, one per Pitfall. Nothing else in this file is wrong.
You fix it in place: run the DEBUGGING protocol, fix each where it lives,
do not restructure the module. One 7-row chain per bug, filled as you fix.

Exports: month_of, feb_days, parse_us, normalize.
"""

from datetime import date, datetime


def month_of(text):
    """Canonical YYYY-MM bucket for a signup string."""
    return datetime.strptime(text, "%Y-%m-%d").isoformat()[:7]


def feb_days(year):
    """Days in February for the given year."""
    return (date(year, 3, 1) - date(year, 2, 1)).days


def parse_us(text):
    """Parse US MM/DD/YYYY into a date."""
    return datetime.strptime(text, "%m/%d/%Y").date()


def normalize(text):
    """Return the canonical form of any parseable date string."""
    try:
        d = datetime.strptime(text, "%Y-%m-%d").date().isoformat()
    except ValueError:
        raise ValueError("invalid date: bad value")

    if d != text:
        raise ValueError("invalid date: not canonical")
    
    return d
    