import pytest
from price_utils import report_from_file


@pytest.mark.parametrize(["data", "expected"],
    [
        ("salary,+1000\nfood,-54.25\ncigarette,-24.99", "net: +920.76"),
        ("salary,+1000", "net: +1000.00"),
        ("salary,+1000\nfood,-54.25\nfood,-54.25\ncigarette,-24.99", "net: +866.51"),
    ],
    ids=["mixed", "single", "duplicated"]
)
def test_report_from_file_parametrize(data, expected, tmp_path):
    source = tmp_path / "parametrize_test.txt"
    source.write_text(data, encoding="utf-8")
    
    result = report_from_file(source)
    
    assert result.splitlines()[-1] == expected
    
    
def test_report_from_file_blank_line(tmp_path):
    source = tmp_path / "blank_line.txt"
    source.write_text("salary,+1000\nfood,-54.25\nfood,-54.25\n\n\ncigarette,-24.99", encoding="utf-8")
    
    result = report_from_file(source)
    
    assert len(result.splitlines()) == 5