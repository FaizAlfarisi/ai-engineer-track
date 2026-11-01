import pytest
import logging
from src.log_toolkit.use_cases.ingestion import ingest

@pytest.mark.parametrize(
    "raw_log_content, file_exist, expected",
    [
        (
            '',
            True,
            "Ingest: 0 valid, 0 skipped"
        ),
        (
            "2026-10-19 09:14:04 INFO service=api latency=940 status=503 path=/report\n2026-10-19 09:14:15 WARN service=api latency=760 status=429 path=/re port",
            True,
            "Ingest: 1 valid, 1 skipped"
        ),
        (
            None,
            False,
            "Ingest: 0 valid, 0 skipped"
        )
    ],
    ids=["empty-file", "normal-file", "file-does-not-exist"]
)

def test_ingest(raw_log_content, file_exist, expected, tmp_path, log_file_factory):
    if file_exist:
        log_path = log_file_factory(raw_log_content)
    else:
        log_path = tmp_path / "not_found.log"
        
    target_path = tmp_path / "clean.json"
    
    ingested = ingest(log_path, target_path)
    
    assert ingested == expected

def test_ingest_logs(caplog, tmp_path):
    empty_log = tmp_path / "empty.log"
    target_path = tmp_path / "clean.json"
    
    with caplog.at_level(logging.INFO):
        ingest(empty_log, target_path)
        
    assert caplog.messages == [
        f"invalid file path: {empty_log}",
        f"loaded 0 record of logs from {empty_log}",
        "total skipped line: 0",
        "total valid line: 0"
    ]