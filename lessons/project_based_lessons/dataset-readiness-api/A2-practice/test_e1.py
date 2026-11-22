"""Suite for E1 (NumPy length stats and outlier counts)."""
import json

import pytest

from e1_stats import compute_length_stats, count_outliers
from models import EmptyDataError, LengthStats


def test_length_stats_basic_and_odd_median():
    stats = compute_length_stats(["hi", "hello", "excellent!"])
    assert isinstance(stats, LengthStats)
    assert stats.min == 2
    assert stats.max == 10
    assert stats.mean == pytest.approx(5.67, abs=0.01)
    assert stats.median == 5.0


def test_length_stats_even_median_and_native_types():
    stats = compute_length_stats(["a", "abcd", "abcdef", "abcdefghij"])
    assert type(stats.min) is int
    assert type(stats.max) is int
    assert type(stats.mean) is float
    assert type(stats.median) is float
    assert stats.min == 1
    assert stats.max == 10
    assert stats.mean == 5.25
    assert stats.median == 5.0
    # Must serialize with strict json.dumps without NumPy scalar errors
    serialized = json.dumps(stats.model_dump(), allow_nan=False)
    assert '"median": 5.0' in serialized


def test_length_stats_empty_raises_domain_error():
    with pytest.raises(EmptyDataError):
        compute_length_stats([])


def test_count_outliers_inclusive_bounds():
    texts = ["ab", "abc", "abcdef", "abcdefghij", "abcdefghijk"]
    # lengths: 2, 3, 6, 10, 11 -> outside [3, 10] are 2 and 11
    count = count_outliers(texts, min_len=3, max_len=10)
    assert type(count) is int
    assert count == 2


def test_count_outliers_empty_returns_zero():
    assert count_outliers([], min_len=3, max_len=10) == 0
