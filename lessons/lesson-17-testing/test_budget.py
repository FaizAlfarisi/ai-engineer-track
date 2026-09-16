"""Lesson 17 H1 debug drill — this file is BUGGY.

Four bugs are planted somewhere in this file or its imports.
Run `pytest test_budget.py -q` from the lesson folder, read every
error message, and fix the file until the suite passes. Use the
DEBUGGING protocol from `notes/DEBUGGING.md`.
"""

from budget import total_spend, top_spend


@pytest.fixture(scope="module")
def spending():
    return []


def test_total_spend_empty(spending):
    assert total_spend(spending) == 0.0


def test_total_spend_returns_float(spending):
    result = total_spend(spending)


def test_total_spend_appends(spending):
    spending.append(-10.0)
    assert total_spend(spending) == -10.0


def test_total_spend_clean_again(spending):
    assert spending == []


def test_top_spend_finds_largest():
    items = [("food", 5.0), ("ride", 10.0), ("salary", 100.0)]
    assert top_spend(items) == ("food", 5.0)