"""E2 suite (PROVIDED). Imports: LineCountReport, count_text_lines, app from e2_app."""
import json

from fastapi.testclient import TestClient

from e2_app import LineCountReport, app, count_text_lines

client = TestClient(app)


def _post(
    content: bytes,
    name: str = "lines.txt",
    ctype: str = "text/plain",
    source: str | None = None,
):
    data = {"source": source} if source is not None else None
    return client.post(
        "/count-lines",
        files={"file": (name, content, ctype)},
        data=data,
    )


def test_counts_lines_with_default_and_custom_form_source():
    r_default = _post(b"a\nb\nc\n")
    assert r_default.status_code == 200
    assert r_default.json() == {"source": "upload", "lines": 3}

    r_custom = _post(b"one\ntwo\n", source="batch-a")
    assert r_custom.status_code == 200
    assert r_custom.json() == {"source": "batch-a", "lines": 2}


def test_pure_service_function():
    assert count_text_lines(b"x\ny\n", "notes.txt") == 2


def test_empty_file_is_400():
    r = _post(b"   \n ")
    assert r.status_code == 400
    assert r.json() == {"detail": "empty file"}


def test_binary_file_is_400_not_500():
    r = _post(b"\x89PNG\r\n", "lines.txt", "text/plain")
    assert r.status_code == 400
    assert r.json() == {"detail": "not text"}


def test_unsupported_extension_is_415():
    r = _post(b"hello\n", "image.png", "image/png")
    assert r.status_code == 415
    assert r.json() == {"detail": "unsupported media type"}


def test_missing_file_is_422_with_consistent_detail():
    r = client.post("/count-lines")
    assert r.status_code == 422
    body = r.json()
    assert isinstance(body.get("detail"), str)


def test_response_model_is_in_openapi():
    schema = json.dumps(client.get("/openapi.json").json())
    assert "LineCountReport" in schema
    assert "lines" in schema
