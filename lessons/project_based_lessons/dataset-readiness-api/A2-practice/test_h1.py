"""Suite for H1-[DEBUG] (3 planted bugs in h1_buggy.py)."""
import pytest

from h1_buggy import analyze_reviews
from models import EmptyDataError, ReviewRecord


def test_basic_no_dups_no_missing_passes_even_before_fixes():
    records = [
        ReviewRecord(title="One", body="Valid review text", note="verified"),
        ReviewRecord(title="Two", body="Hi", note="short"),
    ]
    result = analyze_reviews(records, min_len=5, max_len=50)
    assert result["rows"] == 2
    assert result["duplicate_count"] == 0
    assert result["missing_note_ratio"] == 0.0
    assert result["outlier_count"] == 1


def test_missing_note_ratio_detects_none_values():
    records = [
        ReviewRecord(title="One", body="Good item", note=None),
        ReviewRecord(title="Two", body="Great item", note="verified"),
    ]
    result = analyze_reviews(records, min_len=3, max_len=50)
    assert result["missing_note_ratio"] == 0.5


def test_duplicate_count_counts_extra_copies_only():
    records = [
        ReviewRecord(title="  Same ", body="Nice item", note="a"),
        ReviewRecord(title="Same", body="  Nice item  ", note="b"),
        ReviewRecord(title="Other", body="Different", note="c"),
    ]
    result = analyze_reviews(records, min_len=3, max_len=50)
    assert result["duplicate_count"] == 1


def test_empty_records_raises_empty_data_error():
    with pytest.raises(EmptyDataError):
        analyze_reviews([], min_len=3, max_len=50)
