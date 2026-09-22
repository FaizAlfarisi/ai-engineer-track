from price_utils import report_from_file, print_report


def test_report_from_file_byte_exact(clean_tx_file):
    # Arrange
    expected = "Food: -10.50\nSalary: +1000.00\nTransport: -20.00\nnet: +969.50\n"
    
    # Act
    result = report_from_file(clean_tx_file)
    
    # Assert
    assert result == expected


def test_print_report_capsys(capsys):
    # Arrange
    pairs = [("Coffee", 3.5), ("Snack", -2.0)]
    
    # Act
    print_report(pairs)
    captured = capsys.readouterr()
    
    # Assert
    assert captured.out == "Coffee: +3.50\nSnack: -2.00\n"