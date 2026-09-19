from price_utils import format_price

def test_format_price_two_decimal(sample_prices):
    price = sample_prices[0]
    
    result = format_price(price)
    
    assert result == "2.50"
    
def test_format_price_zero(sample_prices):
    price = sample_prices[1]
    
    result = format_price(price)
    
    assert result == "0.00"
    
def test_format_price_negative(sample_prices):
    price = sample_prices[2]
    
    result = format_price(price)
    
    assert result == "-12.50"