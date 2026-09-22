"""Lesson 17 H1 debug drill — final fixed state.

The original file carried four planted bugs: a missing `import pytest`
(collection error), an assertion-free test, a wrong expected value, and
a module-scoped mutable fixture. All four are resolved here.
"""

import pytest
from budget import total_spend, top_spend


@pytest.fixture(scope="function")
def spending():
    return []


def test_total_spend_empty(spending):
    assert total_spend(spending) == 0.0


def test_total_spend_returns_float():
    amounts = [1.5, 2.5]
    
    result = total_spend(amounts)
    
    assert isinstance(result, float)


def test_total_spend_appends(spending):
    spending.append(-10.0)
    assert total_spend(spending) == -10.0


def test_total_spend_clean_again(spending):
    assert spending == []


def test_top_spend_finds_largest():
    items = [("food", 5.0), ("ride", 10.0), ("salary", 100.0)]
    assert top_spend(items) == ("salary", 100.0)