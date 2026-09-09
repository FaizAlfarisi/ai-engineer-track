from transaction import Transaction

def get_date(txn: Transaction) -> str:
    return txn.date

class Ledger:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.transactions: list[Transaction] = []
        
    def add(self, txn: Transaction) -> None:
        self.transactions.append(txn)
        
    def net(self) -> float:
        return sum(txn.signed_amount() for txn in self.transactions)
        
    def report(self) -> str:
        lines = [f"{self.owner}: {self.net():.2f}"]
        sorted_txn_by_date = sorted(self.transactions, key=get_date)
        for txn in sorted_txn_by_date:
            lines.append(f"{txn.date} {txn.category} {txn.signed_amount():+.2f}")
            
        return "\n".join(lines)
            