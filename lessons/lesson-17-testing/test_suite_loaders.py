import pytest
from price_utils import load_amounts, report_from_file


def test_load_amounts_with_clean_tx_file(clean_tx_file):
    # Arrange & Act: clean_tx_file is a CSV, so load_amounts skips non-numeric lines gracefully
    result = load_amounts(clean_tx_file)
    
    # Assert
    assert result == []


def test_load_amounts_valid_numbers(tmp_path):
    # Arrange
    p = tmp_path / "numbers.txt"
    p.write_text("10.5\n-20.0\n30.0\n", encoding="utf-8")
    
    # Act
    result = load_amounts(p)
    
    # Assert
    assert result == [10.5, -20.0, 30.0]


def test_load_amounts_missing_file(tmp_path):
    # Arrange
    missing = tmp_path / "missing.txt"
    
    # Act
    result = load_amounts(missing)
    
    # Assert
    assert result == []


def test_report_from_file_raises_on_missing(tmp_path):
    # Arrange
    missing = tmp_path / "missing.txt"
    
    # Act & Assert
    with pytest.raises(FileNotFoundError):
        report_from_file(missing)