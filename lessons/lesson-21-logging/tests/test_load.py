import json
import pytest
import logging
from safe_load import load_logged

def test_warns_on_corrupt(tmp_path, caplog):
    corrupt_path = tmp_path / "a_corrupt_file.json"
    
    corrupt_path.write_text("{this is gonna corrupt", encoding="utf-8")
    
    with caplog.at_level(logging.ERROR, logger="safe_load"):
        assert load_logged(str(corrupt_path)) == []
    
    assert any(r.levelno == logging.ERROR and r.exc_info for r in caplog.records)

def test_empty_default_on_missing(tmp_path, caplog):
    missing_path = tmp_path / "unwritten_file.json"
    
    with caplog.at_level(logging.WARNING, logger="safe_load"):
        assert load_logged(str(missing_path)) == []
    
    assert any(r.levelno == logging.WARNING for r in caplog.records)
    
def test_info_on_ok(tmp_path, caplog):
    file_path = tmp_path / "data.json"
    file_path.write_text(json.dumps({'items': ['data_1', 'data_2']}))
    
    with caplog.at_level(logging.INFO, logger="safe_load"):
        assert load_logged(str(file_path)) == ['data_1', 'data_2']
        
    assert any(r.levelno == logging.INFO for r in caplog.records)