from dataclasses import dataclass, field

@dataclass
class Category:
    name: str
    budget: float = 0.0
    tags: list[str] = field(default_factory=list)