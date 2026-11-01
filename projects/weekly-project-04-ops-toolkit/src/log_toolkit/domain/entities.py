from dataclasses import dataclass
from datetime import time, date, datetime

@dataclass
class RequestArgv:
    command: str
    subcommand: str = ""
    mode: str = "normal"
    number: int | None = None
    start: time | None = None
    end: time | None = None
    
@dataclass
class ServiceLog:
    date: date
    time: time
    level: str
    service: str
    latency: int
    status: int
    path: str
    