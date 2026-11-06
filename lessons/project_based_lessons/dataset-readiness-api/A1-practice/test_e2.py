"""E2 suite (PROVIDED). Imports: app from e2_app. Needs fastapi + httpx."""
import json

from fastapi.testclient import TestClient

from e2_app import app

client = TestClient(app)


def _post(content: bytes, name="lines.txt", ctype="text/plain"):
    return client.post("/count-lines", files={"file": (name, content, ctype)})


def test_counts_lines():
    r = _post(b"a\nb\nc\n")
    assert r.status_code == 200
    assert r.json() == {"lines": 3}


def test_empty_file_is_400():
    r = _post(b"")
    assert r.status_code == 400
    assert r.json() == {"detail": "empty file"}


def test_binary_file_is_400_not_500():
    r = _post(b"\x89PNG\r\n", "a.png", "image/png")
    assert r.status_code == 400
    assert r.json() == {"detail": "not text"}


def test_missing_file_is_422():
    assert client.post("/count-lines").status_code == 422


def test_response_model_is_in_openapi():
    schema = json.dumps(client.get("/openapi.json").json())
    assert "lines" in schema
