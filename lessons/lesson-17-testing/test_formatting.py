import pytest
from price_utils import format_price, signed


@pytest.mark.parametrize(
    "amount, expected",
    [
        (0.0, "0.00"),
        (2.5, "2.50"),
        (-12.5, "-12.50"),
        (1234567.891, "1,234,567.89"),
        (0.004, "0.00"),
    ],
    ids=["zero", "cents", "negative", "thousands", "sub-cent"],
)
def test_format_price_parametrize(amount, expected):
    # Arrange & Act
    result = format_price(amount)
    
    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "amount, expected",
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