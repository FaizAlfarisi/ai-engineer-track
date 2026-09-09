from pathlib import Path
import json
from ledger import Ledger
from transaction import Transaction

class Session:
    def __init__(self, ledger: Ledger, path: Path) -> None:
        self.ledger = ledger
        self.path = path
        
    def add(self, date: str, category: str, kind: str, amount: float) -> None:
        txn = Transaction(date, category, kind, amount)
        self.ledger.add(txn)

    def net(self) -> float:
        return self.ledger.net()
    
    def save(self) -> None:
        owner = self.ledger.owner
        net = self.net()
        data = {
            "owner": owner,
            "net": net
        }
        self.path.write_text(json.dumps(data), encoding="utf-8")
        