from dataclasses import dataclass
from datetime import time

@dataclass
class RequestArgv:
    command: str
    subcommand: str = ""
    mode: str = "normal"
    number: int | None = None
    start: time | None = None
    end: time | None = None