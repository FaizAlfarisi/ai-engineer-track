from dataclasses import dataclass

@dataclass
class Request:
    command: str
    mode: str = "normal"
    subcommand: str = ""
    number: int | None = None
    
@dataclass
class Item:
    id: int
    name: str
    price: float
    stock: int
    
    def total_value(self) -> float:
        return self.price * self.stock