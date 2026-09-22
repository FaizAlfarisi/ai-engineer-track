import pytest
from price_utils import categorize, is_affordable


@pytest.mark.parametrize(
    "amount,expected",
    [
        (10.0, "income"),
        (-10.0, "expense"),
        (0.0, "zero"),
        (-0.0, "zero"),
    ],
    ids=["income", "expense", "zero", "negative_zero"]
)
def test_categorize(amount, expected):
    # Arrange & Act
    result = categorize(amount)
    
    # Assert
    assert result == expected


def test_is_affordable_true():
    # Arrange
    balance = 100.0
    price = 50.0
    
    # Act
    result = is_affordable(balance, price)
    
    # Assert
    assert result is True


def test_is_affordable_false():
    # Arrange
    balance = 30.0
    price = 50.0
    
    # Act
    result = is_affordable(balance, price)
    
    # Assert
    assert result is False


def test_is_affordable_zero_balance():
    # Arrange
    balance = 0.0
    price = 0.0
    
    # Act
    result = is_affordable(balance, price)
    
    # Assert
    assert result is True