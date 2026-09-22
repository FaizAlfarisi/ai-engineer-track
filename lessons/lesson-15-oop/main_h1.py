import json
from pathlib import Path
from summary import Summary


def main() -> None:
    path = Path("fixture.json")
    records = json.loads(path.read_text(encoding="utf-8"))
    report = Summary(records)
    report.print_report()


if __name__ == "__main__":
    main()