"""M1 suite (PROVIDED). Imports: iter_valid_products from m1_iter."""
import inspect

from m1_iter import iter_valid_products
from models import Product


def test_yields_only_valid_products_in_order():
    rows = [
        {"name": "a", "price": 1},
        {"name": "", "price": 1},
        5,
        {"name": "b", "price": 2.5, "note": "x"},
        {"price": 3},
    ]
    out = list(iter_valid_products(rows))
    assert [p.name for p in out] == ["a", "b"]
    assert all(isinstance(p, Product) for p in out)


def test_is_a_lazy_generator():
    pulled = []

    def source():
        for i in range(100):
            pulled.append(i)
            yield {"name": str(i), "price": 1}

    gen = iter_valid_products(source())
    assert inspect.isgenerator(gen)
    assert pulled == []
    next(gen)
    assert pulled == [0]
