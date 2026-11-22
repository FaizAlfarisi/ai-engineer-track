"""Suite for M1 (JSONL export, env thresholds, and FastAPI download route)."""
import json

import pandas as pd
from fastapi.testclient import TestClient

from m1_export_app import app, export_jsonl, load_limits

client = TestClient(app)


def test_load_limits_defaults_and_env_override(monkeypatch):
    monkeypatch.delenv("MIN_BODY_LEN", raising=False)
    monkeypatch.delenv("MAX_BODY_LEN", raising=False)
    assert load_limits() == (5, 200)

    monkeypatch.setenv("MIN_BODY_LEN", "10")
    monkeypatch.setenv("MAX_BODY_LEN", "50")
    assert load_limits() == (10, 50)


def test_export_jsonl_preserves_utf8_and_null_notes():
    df = pd.DataFrame([
        {"title": "Café", "body": "Strong aroma", "note": None},
        {"title": "Tea", "body": "Fresh leaves", "note": "green"},
    ])
    text = export_jsonl(df)
    lines = [line for line in text.splitlines() if line.strip()]
    assert len(lines) == 2
    assert "Café" in lines[0]
    first = json.loads(lines[0])
    assert first == {"title": "Café", "body": "Strong aroma", "note": None}


def test_clean_endpoint_downloads_trimmed_deduped_filtered_jsonl(monkeypatch):
    monkeypatch.setenv("MIN_BODY_LEN", "5")
    monkeypatch.setenv("MAX_BODY_LEN", "30")

    payload = "\n".join([
        json.dumps({"title": "  Good  ", "body": "  Solid product  ", "note": None}),
        json.dumps({"title": "Good", "body": "Solid product", "note": "dup"}),
        json.dumps({"title": "Short", "body": "hi", "note": None}),
        json.dumps({"title": "Long", "body": "x" * 50, "note": None}),
        json.dumps({"title": "Nice", "body": "Works well!", "note": "café"}),
    ]).encode("utf-8")

    resp = client.post(
        "/reviews/clean",
        files={"file": ("reviews.jsonl", payload, "application/octet-stream")},
    )
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("application/x-ndjson")
    assert "attachment" in resp.headers["content-disposition"]
    assert "cleaned_reviews.jsonl" in resp.headers["content-disposition"]

    rows = [json.loads(line) for line in resp.text.splitlines() if line.strip()]
    assert rows == [
        {"title": "Good", "body": "Solid product", "note": None},
        {"title": "Nice", "body": "Works well!", "note": "café"},
    ]


def test_clean_endpoint_returns_400_when_zero_rows_survive(monkeypatch):
    monkeypatch.setenv("MIN_BODY_LEN", "100")
    monkeypatch.setenv("MAX_BODY_LEN", "200")

    payload = (
        json.dumps({"title": "Tiny", "body": "too short", "note": None}) + "\n"
    ).encode("utf-8")
    resp = client.post(
        "/reviews/clean",
        files={"file": ("reviews.jsonl", payload, "application/octet-stream")},
    )
    assert resp.status_code == 400
    assert "detail" in resp.json()
