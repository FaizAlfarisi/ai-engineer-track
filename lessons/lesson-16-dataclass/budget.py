from dataclasses import dataclass, field, replace
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
        if self.kind is Kind.INCOME:
            return self.amount
        return -self.amount

    def mark_spent(self, extra: float) -> "Transaction":
        return replace(self, amount=extra)

@dataclass
class Budget:
    owner: str
    transactions: list[Transaction] = field(default_factory=list)

    def add(self, txn: Transaction) -> None:
        self.transactions.append(txn)

    def net(self) -> float:
        return sum(txn.signed_amount() for txn in self.transactions)