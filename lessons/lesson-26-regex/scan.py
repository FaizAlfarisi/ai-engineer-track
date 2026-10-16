
import sys
from pathlib import Path

from extract import build_extract
from patterns import classify


def main(argv) -> None:
    if len(argv) != 3:
        sys.stderr.write("usage: scan.py <service.log> <incidents.txt>\n")
        sys.exit(1)

    service_path = Path(argv[1])
    incidents_path = Path(argv[2])

    if not service_path.exists() or not service_path.is_file():
        sys.stderr.write("bad log: not found\n")
        sys.exit(1)

    lines = []

    with service_path.open("r", encoding="utf-8") as file:
        for i, raw in enumerate(file):
            try:
                kind, num, msg = classify(raw)
            except ValueError:
                lines.append(f"skip {i}: invalid line: bad shape")
                continue

            if kind == "error":
                lines.append(f"error {i}: {num}: {msg}")

            elif kind == "temp":
                if num > 40.0:
                    lines.append(f"alert {i}: {num}")
                else:
                    lines.append(f"skip {i}: invalid line: bad shape")

    text = build_extract(lines)

    incidents_path.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main(sys.argv)
