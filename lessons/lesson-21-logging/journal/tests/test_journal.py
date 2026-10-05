import json
import sys
import os
import logging
from journal.main import merge, setup_verbosity, main

def test_skip_counts_invalid(tmp_path, capsys):
    d = tmp_path / "data"
    d.mkdir()
    feed = d / "feed.json"
    feed.write_text(json.dumps({
        "items": [
            {"id": 1, "price": 10, "stock": 5},
            {"id": 2, "price": 20, "stock": 5},
            {"id": 3, "price": 30, "stock": 5},
            {"id": 4, "price": 40, "stock": 5},
            {"price": 99, "stock": 0}  # invalid (missing id)
        ]
    }), encoding="utf-8")
    
    cache = d / "cache.json"
    cache.write_text(json.dumps({
        "items": [
            {"id": 3, "price": 99, "stock": 0},  # stale overlap
            {"id": 5, "price": 50, "stock": 2}   # offline-only
        ]
    }), encoding="utf-8")
    
    old_argv = sys.argv
    sys.argv = ["journal.main", "sync", str(d)]
    original_cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        main(sys.argv)
    finally:
        os.chdir(original_cwd)
        sys.argv = old_argv
        
    captured = capsys.readouterr()
    assert "Ledger: 5 items (fresh 4, cached 1, skipped 1)" in captured.out

def test_level_filter():
    logger = setup_verbosity("quiet")
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 2
    
    log_normal = setup_verbosity("normal")
    stream_handler = [h for h in log_normal.handlers if isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler)][0]
    assert stream_handler.level == logging.INFO

def test_merge_keeps_cached():
    network = [{"id": 1, "price": 100, "stock": 10}]
    cached = [
        {"id": 1, "price": 50, "stock": 5},
        {"id": 2, "price": 200, "stock": 20}
    ]
    items, fresh, kept = merge(network, cached)
    assert fresh == 1
    assert kept == 1
    assert len(items) == 2
    assert items[0]["id"] == 1
    assert items[0]["price"] == 100
    assert items[1]["id"] == 2
    assert items[1]["price"] == 200