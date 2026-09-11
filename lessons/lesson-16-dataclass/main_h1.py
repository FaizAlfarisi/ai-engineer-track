from pathlib import Path
import json
from budget import Budget, Kind, Transaction


def main() -> None:
    records = json.loads(Path("budget.json").read_text(encoding="utf-8"))
    book = Budget("ada")
    for record in records:
        txn = Transaction(
            record["date"], record["category"], Kind(record["kind"]), record["amount"]
        )
        txn = txn.mark_spent(txn.amount)
        book.add(txn)
    print(f"owner: {book.owner}")
    print(f"net: {book.net():.2f}")


if __name__ == "__main__":
    main()