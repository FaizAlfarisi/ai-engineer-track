from dataclasses import dataclass
from enum import Enum

class Kind(Enum):
    INCOME = "income"
    EXPENSE = "expense"
    
@dataclass(frozen=True)
class Transaction:
    date: str
    category: str
    kind: Kind
    amount: float
    
    def signed_amount(self) -> float:
        return self.amount if self.kind is Kind.INCOME else -self.amount