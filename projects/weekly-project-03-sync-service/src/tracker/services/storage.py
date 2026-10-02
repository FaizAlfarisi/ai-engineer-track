import json
import csv
from typing import Any
from pathlib import Path
from src.tracker.domain.entities import Item
from src.shared.utils.exceptions import CorruptDataError
import logging

logger = logging.getLogger(__name__)

def item_decoder(dtc: dict[str, Any]) -> Item | dict[str, Any]:
    if "id" in dtc and "name" in dtc and "price" in dtc and "stock" in dtc:
        
        raw_id = dtc.get('id')
        try:
            id = int(raw_id)
        except ValueError:
            raise CorruptDataError(f"Invalid id: '{raw_id!r}'. Expected a number")
        
        raw_name = dtc.get('name')
        name = raw_name.strip() if isinstance(raw_name, str) else ""
        if not name:
            raise CorruptDataError(f"Invalid name: '{raw_name!r}. Expected non empty string")

        
        raw_price = dtc.get("price")
        try:
            price = float(raw_price)
        except (ValueError, TypeError):
            raise CorruptDataError(f"Invalid price: '{raw_price!r}. Expected a positive number")
        if price < 0.0:
            raise CorruptDataError(f"Invalid price: '{raw_price!r}. Expected a positive number")
        
        raw_stock = dtc.get("stock")
        try:
            stock = int(raw_stock)
        except ValueError:
            raise CorruptDataError(f"Invalid stock: '{raw_stock}. Expected a number")
        
        return Item(
            id=id,
            name=name, 
            price=price,
            stock=stock
        )
    
    return dtc

def merge_data(network: list[Item], cached: list[Item]) -> tuple[list[Item], int, int]:
    merged = {item["id"]: item for item in cached}
    
    network_ids = set()
    for item in network:
        item_id = item["id"]
        merged[item_id] = item
        network_ids.add(item_id)
        
    fresh = len(network)
    kept = sum(1 for item in cached if item["id"] not in network_ids)
    clean_merged = sorted([item_decoder(item) for item in merged.values()], key=lambda x: x["id"])
    logger.debug("merged fresh %s items and kept %s items successfully: %s", fresh, kept, clean_merged)
    
    return clean_merged, fresh, kept


def load_json(path: str | Path) -> list[Item]:
    if not isinstance(path, (str, Path)) or not path:
        return []
    
    path = Path(path)
    
    if not path.is_file():
        logger.warning("file not found: %s", path)
        return []
    
    try:
        root_data = json.loads(path.read_text(encoding="utf-8"), object_hook=item_decoder)
        
        if isinstance(root_data, dict) and "items" in root_data:
            records = root_data["items"]
            
            if isinstance(records, list):
                logger.info("loaded %d items from %s", len(records), path)
                return records
            
    except json.JSONDecodeError as exc:
        logger.error("failed to load json: %s", path, exc_info=True)
        raise CorruptDataError(exc)

def load_csv(path: str | Path) -> list[dict[str, Any]]:
    if not isinstance(path, (str, Path)) or not path:
        return {}
        
    path = Path(path)
    
    if not path.is_file():
        logging.warning("file not found %s", path)
        return {}
    
    with path.open(encoding="utf-8", newline="") as f:
        rows = csv.DictReader(f)
        return [item_decoder(r) for r in rows]

def write_json(items: list[Item], path: str | Path) -> None:
    path = Path(path)
 
    path.write_text(
        json.dumps({"items": items}, indent=2),
        encoding="utf-8"
    )

def write_csv(path: str | Path, items: list[Item]) -> None:
    path = Path(path)
    
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "price", "stock"], extrasaction="ignore")
        writer.writeheader()
        writer.writerows(items)