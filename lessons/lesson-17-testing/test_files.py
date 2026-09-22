import pytest
from price_utils import report_from_file

def test_report_from_file_builds_net(tmp_path):
    file_path = tmp_path / "finance.txt"
    file_path.write_text("donation,2500\ncigarette,-1500", encoding="utf-8")
    
    result = report_from_file(file_path)
    
    assert result == "donation: +2500.00\ncigarette: -1500.00\nnet: +1000.00\n"
    
def test_report_from_file_not_found(tmp_path):
    file_path = tmp_path / "not_found.txt"
    
    with pytest.raises(FileNotFoundError) as exc_info:
        report_from_file(file_path)
        
    assert str(exc_info.value) == f"report file not found: {file_path}"
    