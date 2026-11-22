"""Suite for E2 (Pandas cleaning, trimming, deduplication, and missing ratio)."""
import pandas as pd
import pytest

from e2_clean import clean_reviews
from models import EmptyDataError, ReviewRecord


def test_clean_reviews_trims_and_deduplicates_keep_first():
    records = [
        ReviewRecord(title="  Great  ", body="  Loved it  ", note="  first  "),
        ReviewRecord(title="Great", body="Loved it", note="second copy"),
        ReviewRecord(title="Okay", body="Fine product", note=None),
    ]
    cleaned_df, dup_count, missing_ratio = clean_reviews(records)

    assert isinstance(cleaned_df, pd.DataFrame)
    assert list(cleaned_df.index) == [0, 1]
    assert len(cleaned_df) == 2
    assert cleaned_df.loc[0, "title"] == "Great"
    assert cleaned_df.loc[0, "body"] == "Loved it"
    assert cleaned_df.loc[0, "note"] == "first"
    assert pd.isna(cleaned_df.loc[1, "note"])
    assert type(dup_count) is int
    assert dup_count == 1
    assert type(missing_ratio) is float
    assert missing_ratio == pytest.approx(1 / 3, abs=0.0001)


def test_clean_reviews_triple_duplicate_counts_two_extra():
    records = [
        ReviewRecord(title="Same", body="Text", note=None),
        ReviewRecord(title="  Same ", body="Text ", note=None),
        ReviewRecord(title="Same", body="  Text", note="keep? no"),
    ]
    cleaned_df, dup_count, missing_ratio = clean_reviews(records)

    assert len(cleaned_df) == 1
    assert dup_count == 2
    assert missing_ratio == pytest.approx(2 / 3, abs=0.0001)


def test_clean_reviews_no_duplicates_and_no_missing_notes():
    records = [
        ReviewRecord(title="One", body="First review", note="ok"),
        ReviewRecord(title="Two", body="Second review", note="great"),
    ]
    cleaned_df, dup_count, missing_ratio = clean_reviews(records)

    assert len(cleaned_df) == 2
    assert dup_count == 0
    assert missing_ratio == 0.0


def test_clean_reviews_empty_raises():
    with pytest.raises(EmptyDataError):
        clean_reviews([])
