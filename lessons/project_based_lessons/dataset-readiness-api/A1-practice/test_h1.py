"""H1 suite (PROVIDED). Imports: check_products from h1_buggy; BadUpload from models."""
import pytest

from h1_buggy import check_products
from models import BadUpload


def test_mixed_file_counts():
    raw = b'[{"name":"a","price":1},{"name":"","price":1},{"price":2}]'
    assert check_products(raw) == {"total": 3, "ok": 1, "invalid": 2}


def test_counts_add_up_with_empty_object_row():
    raw = b'[{"name":"a","price":1},{}]'
    out = check_products(raw)
    assert out == {"total": 2, "ok": 1, "invalid": 1}
    assert out["ok"] + out["invalid"] == out["total"]


def test_malformed_json_is_bad_upload():
    with pytest.raises(BadUpload):
        check_products(b"[oops")


def test_binary_bytes_are_bad_upload_not_a_crash():
    with pytest.raises(BadUpload):
        check_products(b"\x89PNG\r\n")
