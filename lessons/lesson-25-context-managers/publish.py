import sys
from pathlib import Path
from release import build_release
from guards import AtomicWriter

def main(argv) -> None:
    if len(argv) != 3: 
        sys.stderr.write("usage: publish.py <draft.txt> <report.txt>\n")
        sys.exit(1)
    
    draft_path = Path(argv[1])
    report_path = Path(argv[2])
    
    if not draft_path.exists() or not draft_path.is_file():
        sys.stderr.write("bad draft: not found\n")
        sys.exit(1)
        
    lines = []
        
    with draft_path.open(encoding="utf-8") as file:
        for i, raw in enumerate(file):
            stripped = raw.strip()
            if "POISON" == stripped:
                sys.stderr.write("poison draft\n")
                sys.exit(1)
            if not stripped:
                lines.append(f"skip {i}: invalid line: empty\n")
            else:
                lines.append(f"line {i}: {stripped}\n")
    
    
    text = build_release(lines)
    
    with AtomicWriter(report_path) as handle:
        handle.write(text)
    print(text, end="")

if __name__ == "__main__":
    main(sys.argv)