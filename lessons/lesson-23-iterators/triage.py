import sys
from pathlib import Path
from stream import WindowReader, validate_line
from incidents import build_incidents

def main(argv) -> None:
    if len(argv) != 3: 
        sys.stderr.write("usage: triage.py <server.log> <incidents.txt>\n")
        sys.exit(1)
    
    log_path = Path(argv[1])
    txt_path = Path(argv[2])
    
    if not log_path.exists() or not log_path.is_file():
        sys.stderr.write("bad log: not found\n")
        sys.exit(1)
        
    lines = []
        
    with log_path.open(encoding="utf-8") as handle:
        r = WindowReader(enumerate(handle), 3)
        for window in r:
            for i, raw in window:
                try:
                    validated = validate_line(raw)
                except ValueError as exc:
                    lines.append(f"skip {i}: {exc}\n")
                    continue
                else:
                    if "ERROR" in validated:
                        lines.append(f"error {i}: {validated}\n")
    
    
    text = build_incidents(lines)
    
    txt_path.write_text(text, encoding="utf-8")
    print(text, end="")

if __name__ == "__main__":
    main(sys.argv)