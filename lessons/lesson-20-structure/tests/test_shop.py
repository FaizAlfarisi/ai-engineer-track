import pytest
from shop.carts import line_total

def test_total(morning_basket):
    assert line_total(morning_basket) == pytest.approx(7.50)
    
def test_count(morning_basket):
    assert len(morning_basket) == 3
    
def test_empty():
    assert line_total([]) == 0.0
