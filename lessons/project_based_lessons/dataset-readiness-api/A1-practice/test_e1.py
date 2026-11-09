"""E1 suite (PROVIDED). Imports: SampleRecord, flatten_errors from e1_flatten."""
from pydantic import ValidationError

from e1_flatten import SampleRecord, flatten_errors
from models import Product


def _errs(model_cls, data):
    try:
        model_cls.model_validate(data)
    except ValidationError as exc:
        return flatten_errors(exc)
    raise AssertionError("expected the data to be invalid")


def test_sample_record_valid_and_defaults():
    rec = SampleRecord.model_validate(
        {"code": "DS-10", "prompt": "  Explain HTTP 415  ", "score": 4}
    )
    assert rec.code == "DS-10"
    assert rec.prompt == "Explain HTTP 415"
    assert rec.score == 4
    assert rec.notes is None


def test_sample_record_declarative_constraints():
    errs = _errs(
        SampleRecord,
        {"code": "bad", "prompt": "ok", "score": 0},
    )
    fields = {item["field"] for item in errs}
    assert fields == {"code", "score"}


def test_sample_record_strict_and_whitespace_validator():
    errs = _errs(
        SampleRecord,
        {"code": "DS-01", "prompt": "   ", "score": "5"},
    )
    by_field = {item["field"]: item["message"] for item in errs}
    assert set(by_field) == {"prompt", "score"}
    assert "must not be blank" in by_field["prompt"]


def test_missing_field():
    assert _errs(Product, {"price": 1}) == [
        {"field": "name", "message": "Field required"}
    ]


def test_empty_string_and_wrong_type_both_reported():
    out = _errs(Product, {"name": "", "price": "abc"})
    assert len(out) == 2
    assert {
        "field": "name",
        "message": "String should have at least 1 character",
    } in out
    assert {"field": "price", "message": PRICE_MSG} in out


def test_non_object_row_has_empty_field():
    out = _errs(Product, 5)
    assert len(out) == 1
    assert out[0]["field"] == ""


def test_plain_types_only():
    for item in _errs(Product, {"name": "", "price": 0}):
        assert set(item) == {"field", "message"}
        assert isinstance(item["field"], str)
        assert isinstance(item["message"], str)


PRICE_MSG = "Input should be a valid number, unable to parse string as a number"
