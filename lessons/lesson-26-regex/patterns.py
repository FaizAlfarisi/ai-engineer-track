import re
from collections.abc import Iterator

PING: re.Pattern[str] = re.compile(r"ping (\d+)")

def found_anywhere(line: str) -> str | None :
    m = PING.search(line)
    return m.group(1) if m else None

def found_at_start(line: str) -> str | None :
    m = PING.match(line)
    return m.group(1) if m else None

def fully_matches(line: str) -> str | None :
    m = PING.fullmatch(line)
    return m.group(1) if m else None


ERROR_IDS: re.Pattern[str] = re.compile(r"error (\d+)")

def all_ids(block: str) -> list[str]:
    return ERROR_IDS.findall(block)

def iter_ids(block: str) -> Iterator[str]:
    return (i.group(1) for i in ERROR_IDS.finditer(block))


ANY_ERROR: re.Pattern[str] = re.compile(r"^error (\d+)", re.IGNORECASE | re.MULTILINE)

def count_errors(block: str) -> int:
    return len(ANY_ERROR.findall(block))
    
PARSER_PATTERN: re.Pattern[str] = re.compile(r"^(error|skip) (\d+): (.+)$", re.IGNORECASE)
def parse_line(line: str) -> tuple[str, int, str]:
    result = PARSER_PATTERN.fullmatch(line.strip())
    
    if not result:
        raise ValueError("invalid line: bad shape")
    
    kind = result.group(1).lower()
    line_id = result.group(2)
    message = result.group(3)
    
    
    return (kind, int(line_id), message)
    
    
ERROR_M1 = re.compile(r"^error (\d+): (.+)$", re.IGNORECASE)
TEMP_M1 = re.compile(r"^temp (-?\d+(?:\.\d+)?)$", re.IGNORECASE)
def classify(line: str) -> tuple[str, int | float, str | None]:
    line = line.strip()
    
    m = ERROR_M1.fullmatch(line)
    if m:
        return ("error", int(m.group(1)), m.group(2))
    
    m = TEMP_M1.fullmatch(line)
    if m:
        return ("temp", float(m.group(1)), None)
    
    raise ValueError("invalid line: bad shape")
        

def summarize(block: str) -> tuple[list[tuple[int, str]], int]:
    errors = []
    skipped = 0
    for line in block.splitlines():
        kind, line_id, message = parse_line(line.strip())
        if kind == "error":
            errors.append((line_id, message))
        else: 
            skipped += 1
    
    return (errors, skipped)