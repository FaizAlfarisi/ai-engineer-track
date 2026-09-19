from discounter import apply_discount

def test_apply_discount_standard():
    assert apply_discount(100.0, 10) == 90.0
    
def test_apply_discount_rounding():
    assert apply_discount(75.0, 5) == 71.25