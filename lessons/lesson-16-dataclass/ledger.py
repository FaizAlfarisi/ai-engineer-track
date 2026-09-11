from dataclasses import dataclass, field
from kind import Transaction

def get_date(txn: Transaction) -> str:
    return txn.date
    

@dataclass
class Ledger:
    owner: str
    transactions: list[Transaction] = field(default_factory=list)
    
    def add(self, txn: Transaction) -> None:
        self.transactions.append(txn)
        
    def net(self) -> float:
        return sum(txn.signed_amount() for txn in self.transactions)
    
    def report(self) -> str:
        lines = [f"{self.owner}: {self.net():.2f}"]
        
        for txn in sorted(self.transactions, key=get_date):
            lines.append(f"{txn.date} {txn.category} {txn.signed_amount():+.2f}")
            
        return '\n'.join(lines)