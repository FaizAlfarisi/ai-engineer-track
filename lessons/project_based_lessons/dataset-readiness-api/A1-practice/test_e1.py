"""E1 suite (PROVIDED). Imports: flatten_errors from e1_flatten."""
from pydantic import ValidationError

from e1_flatten import flatten_errors
from models import Product


def _errs(data):
    try:
        Product.model_validate(data)
    except ValidationError as exc:
        return flatten_errors(exc)
    raise AssertionError("expected the data to be invalid")


def test_missing_field():
    assert _errs({"price": 1}) == [{"field": "name", "message": "Field required"}]


def test_empty_string_and_wrong_type_both_reported():
    out = _errs({"name": "", "price": "abc"})
    assert len(out) == 2
    assert {
        "field": "name",
        "message": "String should have at least 1 character",
    } in out
    assert {"field": "price", "message": PRICE_MSG} in out


def test_non_object_row_has_empty_field():
    out = _errs(5)
    assert len(out) == 1
    assert out[0]["field"] == ""


def test_plain_types_only():
    for item in _errs({"name": "", "price": 0}):
        assert set(item) == {"field", "message"}
        assert isinstance(item["field"], str)
        assert isinstance(item["message"], str)


PRICE_MSG = "Input should be a valid number, unable to parse string as a number"
