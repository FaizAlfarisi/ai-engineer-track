import sys
from pathlib import Path
from sensors import batches, parse_one
from alerts import build_alerts

def main(argv) -> None:
    if len(argv) != 3: 
        sys.stderr.write("usage: harvest.py <telemetry.log> <alerts.txt>\n")
        sys.exit(1)
    
    log_path = Path(argv[1])
    txt_path = Path(argv[2])
    
    if not log_path.exists() or not log_path.is_file():
        sys.stderr.write("bad telemetry: not found\n")
        sys.exit(1)
        
    lines = []
        
    with log_path.open(encoding="utf-8") as handle:
        r = batches(enumerate(handle), 3)
        for window in r:
            for i, raw in window:
                try:
                    value = parse_one(raw)
                except ValueError as exc:
                    lines.append(f"skip {i}: {exc}\n")
                    continue
                else:
                    if value > 40.0:
                        lines.append(f"alert {i}: {value}\n")
    
    
    text = build_alerts(lines)
    
    txt_path.write_text(text, encoding="utf-8")
    print(text, end="")

if __name__ == "__main__":
    main(sys.argv)