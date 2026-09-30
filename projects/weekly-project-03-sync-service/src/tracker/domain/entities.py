from dataclasses import dataclass

@dataclass
class Request:
    command: str
    mode: str = "normal"
    subcommand: str = ""
    number: int | None = None