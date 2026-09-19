from price_utils import load_amounts, report_from_file, signed

def test_load_amounts_integrated(tmp_path):
    source = tmp_path / "integrated.txt"
    source.write_text("12.5\n-3\n\nabc\n42\n")
    
    amounts = load_amounts(source)
    
    assert amounts == [12.5, -3.0, 42.0]
    
    sum_signed = signed(sum(amounts))
    
    assert sum_signed == "+51.50"
    
    
def test_report_from_file_integrated(tmp_path):
    source = tmp_path / "integrated.txt"
    source.write_text("food,-12.50\nsalary,100.00\nride,-8.00\n")
    
    results = report_from_file(source)
    
    assert results == "food: -12.50\nsalary: +100.00\nride: -8.00\nnet: +79.50\n"
    
