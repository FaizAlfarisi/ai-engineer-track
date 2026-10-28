import pytest
from src.log_toolkit.services.storage import _is_valid_line, load_log

@pytest.mark.parametrize(
    "line, expected",
    [
        ("not a log line at all", False), 
        ("2026-02-30 09:14:07 INFO service=worker latency=430 status=200 path=/jobs", False),
        ("2026-10-19 09:14:15 WARN service=api latency=760 status=429 path=/re port", False),
        ("2026-10-19 09:14:04 INFO service=api latency=940 status=503 path=/report", True),
    ],
    ids=["fully_invalid", "date_invalid", "negative_digit", "valid"],
)
def test_is_valid_line(line, expected):
    result = _is_valid_line(line)
    
    assert result == expected
    
def test_load_log(tmp_path):
    logs = "not a log line at all\n2026-10-19 09:14:04 INFO service=api latency=940 status=503 path=/report"
    p = tmp_path / "sample.log"
    p.write_text(logs, encoding="utf-8")
    
    loaded = load_log(p)
    assert loaded == logs