import csv
from ledger.compute import merge
from ledger.write import write_csv


def test_merge_keeps_cached_only():
    network = [{"id": 1, "name": "Alpha", "price": 10.0, "stock": 5}]
    cached = [{"id": 2, "name": "Beta", "price": 20.0, "stock": 3}]
    
    items, fresh, kept = merge(network, cached)
    
    assert [x["id"] for x in items] == [1, 2]
    assert fresh == 1
    assert kept == 1


def test_merge_network_wins():
    network = [{"id": 1, "name": "Updated Name", "price": 15.0, "stock": 10}]
    cached = [{"id": 1, "name": "Stale Name", "price": 10.0, "stock": 5}]
    
    items, fresh, kept = merge(network, cached)
    
    assert len(items) == 1
    assert items[0]["name"] == "Updated Name"
    assert items[0]["price"] == 15.0
    assert fresh == 1
    assert kept == 0


def test_csv_roundtrip(tmp_path):
    file_path = tmp_path / "ledger_test.csv"
    rows = [{"id": 1, "name": "Widget", "price": 9.99, "stock": 50}]
    
    write_csv(rows, file_path)
    
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        read_rows = list(reader)
        
    assert len(read_rows) == 1
    assert int(read_rows[0]["id"]) == 1
    assert read_rows[0]["name"] == "Widget"
    assert float(read_rows[0]["price"]) == 9.99
    assert int(read_rows[0]["stock"]) == 50
