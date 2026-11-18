"""M1 - write your solution here (blank on purpose).

Deliverable: iter_valid_products
"""

from pydantic import ValidationError
from models import Product


def iter_valid_products(rows):
    for item in rows:
        try:
            product = Product.model_validate(item)
        except ValidationError:
            continue
            
        yield product
            