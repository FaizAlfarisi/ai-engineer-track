import logging

from src.tracker.domain.entities import Item
from src.tracker.services.storage import write_csv, load_csv
from src.tracker.use_cases.report_generator import (
    report_value,
    report_low,
    report_summary,
    report_restock,
)


def make_items():
    return [
        Item(id=1, name="coffee", price=2.5, stock=40),
        Item(id=2, name="tea", price=1.8, stock=5),
    ]


def test_write_and_load_csv(tmp_path):
    path = tmp_path / "items.csv"
    items = make_items()

    write_csv(str(path), items)

    loaded = load_csv(str(path))

    assert len(loaded) == 2
    assert loaded[0].name == "coffee"
    assert loaded[1].stock == 5


def test_report_value(tmp_path):
    csv_path = tmp_path / "items.csv"
    json_path = tmp_path / "report.json"

    write_csv(str(csv_path), make_items())

    result = report_value(str(csv_path), str(json_path))

    assert "coffee: 40 x 2.50 = 100.00" in result
    assert "tea: 5 x 1.80 = 9.00" in result
    assert "Total: 109.00" in result


def test_report_low(tmp_path):
    csv_path = tmp_path / "items.csv"

    write_csv(str(csv_path), make_items())

    result = report_low(str(csv_path), 10)

    assert "tea: 5 left" in result
    assert "coffee: 40 x 2.50" not in result


def test_report_summary(tmp_path):
    csv_path = tmp_path / "items.csv"

    write_csv(str(csv_path), make_items())

    result = report_summary(str(csv_path))

    assert "Summary (2 items):" in result
    assert "total value: 109.00" in result
    assert "low stock: 1" in result


def test_logging_caplog(tmp_path, caplog):
    missing_path = tmp_path / "missing.csv"

    with caplog.at_level(logging.WARNING, logger="src.tracker.services.storage"):
        result = load_csv(str(missing_path))

    assert result == []
    assert "file not found" in caplog.text
    assert str(missing_path) in caplog.text
