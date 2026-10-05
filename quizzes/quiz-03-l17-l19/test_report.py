from report import build_search_url, merge, save_csv

def test_report(tmp_path) -> None:
    assert (
        build_search_url("http://x", "coffee latte")
        == "http://x/search?q=coffee+latte"
    )

    network = [
        {"id": 1, "name": "latte", "price": 3.5, "stock": 4},
        {"id": 2, "name": "coffee", "price": 2.5, "stock": 6},
        {"id": 3, "name": "muffin", "price": 2.0, "stock": 5},
    ]
    cached = [
        {"id": 5, "name": "donut", "price": 1.0, "stock": 3},
    ]

    items, fresh, kept = merge(network, cached)

    assert [item["id"] for item in items] == [1, 2, 3, 5]
    assert fresh == 3
    assert kept == 1

    path = tmp_path / "report.csv"
    count = save_csv(items, path)

    assert count == 4

    lines = path.read_text(encoding="utf-8").splitlines()

    assert lines[0] == "id,name,price,stock"
    assert len(lines) == 5

    print(f"Summary ({count} items):")
    for line in lines[1:]:
        print(line)