from dataclasses import dataclass

@dataclass
class Transaction:
    date: str
    category: str
    kind: str
    amount: float
    
    def signed_amount(self) -> float:
        return self.amount if self.kind == "income" else -self.amount
    
    