import pytest 
from pathlib import Path

@pytest.fixture
def sample_prices():
    return [2.5, 0.0, -12.5]

@pytest.fixture
def clean_tx_file(tmp_path: Path) -> Path:
    p = tmp_path / "transactions.txt"
    p.write_text("Food, -10.50\nSalary, 1000.00\nTransport, -20.00\n", encoding="utf-8")
    return p