import pytest
from price_utils import load_amounts, report_from_file

def test_load_amounts_success(tmp_path):
    source = tmp_path / "amounts.txt"
    source.write_text("-25.50\ninvalid_text\n\n500.0", encoding="utf-8")
    
    result = load_amounts(source)
    
    assert result == [-25.50, 500.0]

def test_load_amount_missing_file(tmp_path):
    source = tmp_path / "missing_file.txt"

    result = load_amounts(source)
    
    assert result == []
    
def test_report_from_file_success(tmp_path):
    source = tmp_path / "report.txt"
    source.write_text("food, -25.50\nsalary, 500.0", encoding="utf-8")
    
    result = report_from_file(source)
    
    assert "net: +474.50" in result
    
def test_report_from_file_missing_file(tmp_path):
    source = tmp_path / "missing_file.txt"
    
    with pytest.raises(FileNotFoundError):
        report_from_file(source)