from enum import Enum

class Kind(Enum):
    INCOME = "income"
    EXPENSE = "expense"
    
class Transaction:
    def __init__(self, date: str, category: str, kind: Kind, amount: float) -> None:
        self.date = date
        self.category = category
        self.kind = kind
        self.amount = amount
        
    def signed_amount(self) -> float:
        if self.kind is Kind.INCOME:
            return self.amount
        return -self.amount
        
        