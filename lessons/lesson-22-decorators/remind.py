import json
import sys
from pathlib import Path

from clinic import confirm, send_sms, build_report


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        print("usage: remind.py <inbox.json> <report.txt>", file=sys.stderr)
        sys.exit(1)

    inbox = Path(argv[1])
    report = Path(argv[2])

    if not inbox.exists() or not inbox.is_file():
        print("bad inbox: not found", file=sys.stderr)
        sys.exit(1)

    records = json.loads(inbox.read_text(encoding="utf-8"))

    lines = []

    for i, appt in enumerate(records):
        try:
            confirmed = confirm(appt)
            send_sms(confirmed)
        except ValueError as err:
            lines.append(f"skip {i}: {err}")
            continue

        lines.append(
            f"ok {confirmed['phone']}: {confirmed['name']} {confirmed['time']}"
        )

    text = build_report(lines)

    report.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main(sys.argv)
