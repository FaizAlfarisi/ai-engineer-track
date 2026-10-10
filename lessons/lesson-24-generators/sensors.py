from collections.abc import Iterator, Iterable


def batches(source: Iterable[object], size: int) -> Iterator[list[str]]:
    if size < 1:
        raise ValueError("window size must be >= 1")
    
    window = []
    for item in source:
        window.append(item)
        if len(window) == size:
            yield window
            window = []
    if window:
        yield window
        
def over(source: Iterable[float], threshold: float) -> Iterator[float]:
    return (x for x in source if x > threshold)

def ticks(start: int = 0) -> Iterator[int]:
    n = start
    while True:
        yield n
        n += 1
        
def harvest(pred, stream: Iterable[int], limit: int) -> list[int]:
    found = []
    
    if limit == 0:
        return found
    
    for item in stream:
        if pred(item):
            found.append(item)
            if len(found) == limit:
                break
    return found

def parse_one(x: object) -> float:
    if isinstance(x, bool):
        raise ValueError("invalid reading: not a number")
        
    if isinstance(x, (float, int)):
        return float(x)
    
    if isinstance(x, str):
        x_strip = x.strip()
        
        if not x_strip:
            raise ValueError("invalid reading: empty")
        
        try:
            return float(x_strip)
        except ValueError:
            raise ValueError("invalid reading: not a number")
    
    raise ValueError("invalid reading: not a number")
            

def parse_valid(source: Iterable[object]) -> Iterator[float]:
    for item in source:
        try:
            yield parse_one(item)
        except ValueError:
            continue
    pass

def alert_windows(source: Iterable[object], size: int, threshold: float) -> Iterator[list[float]]:
    windows = batches(parse_valid(source), size)
    
    return (w for w in windows if any(r > threshold for r in w))
    