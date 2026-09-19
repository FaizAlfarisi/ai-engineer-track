import pytest
from price_utils import print_report

def test_print_report_two_rows(capsys):
    data = [("food", -25.0), ("weekly salary", 400.0)]
    
    print_report(data)
    
    assert capsys.readouterr().out == "food: -25.00\nweekly salary: +400.00\n"
    
def test_print_report_monkeypatch(monkeypatch, capsys):
    monkeypatch.setattr("price_utils.signed", lambda amount: "??.??")
    
    data = [("food", -25.0), ("weekly salary", 400.0)]
    
    print_report(data)
    
    assert capsys.readouterr().out == "food: ??.??\nweekly salary: ??.??\n"
    