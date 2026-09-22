import pytest
from price_utils import format_price, signed


@pytest.mark.parametrize(
    "amount,expected",
    [
        (1000.0, "1,000.00"),
        (0.0, "0.00"),
        (-50.5, "-50.50"),
        (1234567.89, "1,234,567.89"),
        (0.1, "0.10"),
    ],
    ids=["thousand", "zero", "negative", "million", "decimal"]
)
def test_format_price(amount, expected):
    # Arrange & Act
    result = format_price(amount)
    
    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "amount,expected",
    [
        (42.0, "+42.00"),
        (-5.5, "-5.50"),
    ],
    ids=["positive", "negative"]
)
def test_signed(amount, expected):
    # Arrange & Act
    result = signed(amount)
    
    # Assert
    assert result == expected