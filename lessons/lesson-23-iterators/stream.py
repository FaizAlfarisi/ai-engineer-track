from collections.abc import Iterable, Iterator


def take(stream: Iterable[str] | Iterator[str], n: int) -> list[str]:
    if n < 0:
        raise ValueError("take needs n >= 0")
    
    out = []
    it = iter(stream)
    for _ in range(n):
        try:
            item = next(it)
        except StopIteration:
            return out
        else:
            out.append(item)
    return out

def kind(stream: Iterable[str] | Iterator[str]) -> str:
    return "iterator" if iter(stream) is stream else "iterable"

def validate_line(line: str) -> str:
    if not isinstance(line, str):
        raise ValueError("invalid line: not a string")
    
    stripped_line = line.strip()
    if not stripped_line:
        raise ValueError("invalid line: empty")
    
    return stripped_line

def first_valid(stream: Iterable[str] | Iterator[str]) -> str | None:
    for it in stream:
        try:
            return validate_line(it)
        except ValueError:
            continue
    
    return None

class WindowReader:
    def __init__(self, source, size):
        if not isinstance(size, int) or size < 1:
            raise ValueError("window size must be >= 1")
        
        self._cursor = iter(source)
        self._size = size
        
    def __iter__(self):
        return self
        
    def __next__(self):
        window = []
        try: 
            for _ in range(self._size):
                window.append(next(self._cursor))
        except StopIteration:
            pass
        if not window:
            raise StopIteration
        return window
            
def clean_windows(source: Iterable[str] | Iterator[str], size: int) -> list[list[str]]:
    # Materializes validated lines in memory before building windows.
    validated = []
    for it in source:
        try:
            validated.append(validate_line(it))
        except ValueError:
            continue
        
    r = WindowReader(validated, size)
    
    return list(r)
        
    