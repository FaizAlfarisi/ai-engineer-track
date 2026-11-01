from pathlib import Path

from src.log_toolkit.services.api import get_incident
from src.log_toolkit.services.storage import write_json
from src.utils.exceptions import CorruptDataError

def fetch_incident(json_path: Path) -> str:
    data = get_incident()

    if "incident" not in data:
        raise CorruptDataError("incident not found")

    write_json(json_path, data)
    
    return f"Incident: {data["incident"]} (severity {data["severity"]})"