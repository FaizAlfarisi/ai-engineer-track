class Account:
    def __init__(self, name: str, balance: float = 0.0) -> None:
        self.name = name
        self.balance = balance
        
    def deposit(self, amount: float) -> None:
        self.balance += amount
        
    def status(self) -> str:
        return f"{self.name}: {self.balance:.2f}"