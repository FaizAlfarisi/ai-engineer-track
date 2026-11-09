"""H1-[DEBUG] - PROVIDED, contains planted bugs. Fix this file only."""
import json

from pydantic import ValidationError

from models import BadUpload, Product


def check_products(raw: bytes) -> dict:
    try:
        rows = json.loads(raw)
    except json.JSONDecodeError:
        raise BadUpload("not valid JSON")
    if not isinstance(rows, list):
        raise BadUpload("expected a JSON array")

    ok = 0
    invalid = 0
    for row in rows:
        if not row:
            continue
        try:
            ok += 1
            Product.model_validate(row)
        except ValidationError:
            invalid += 1
    return {"total": len(rows), "ok": ok, "invalid": invalid}
