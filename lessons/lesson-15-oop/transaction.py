class Transaction:
    def __init__(self, date: str, category: str, kind: str, amount: float) -> None:
        self.date = date
        self.category = category
        self.kind = kind
        self.amount = amount
        
    def signed_amount(self) -> float:
        if self.kind == "income":
            return self.amount
        return -self.amount
    
    