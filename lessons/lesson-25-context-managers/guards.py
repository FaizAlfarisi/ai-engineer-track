from contextlib import contextmanager
from pathlib import Path
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        return False

@contextmanager
def timed():
    record = {"elapsed": 0.0}
    start = time.perf_counter()
    
    try:
        yield record
    finally:
        record["elapsed"] = time.perf_counter() - start
        
class Trail():
    def __init__(self, events: list):
        self.events = events
        
    def __enter__(self):
        self.events.append("enter")
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.events.append("exit")
        return False
    
def read_first(path):
    with path.open(encoding="utf-8") as handle:
        return handle.readline().strip()
        

class AtomicWriter:
    def __init__(self, target):
        self._target = Path(target)
        self._temp = self._target.with_suffix(".tmp")
        self._file = None
        
    def __enter__(self):
        self._file = self._temp.open("w", encoding="utf-8")
        return self._file
    
    def __exit__(self, exc_type, exc, tb):
        if self._file:
            self._file.close()
        
        if exc_type is None:
            self._temp.replace(self._target)
        else:
            self._temp.unlink(missing_ok=True)
        
        return False
    
def timed_publish(lines, target):
    with timed() as t:
        # Collect-then-write keeps small driver data simple; the Challenge proves the streaming approach
        draft = []
        for line in lines:
            line = line.strip()
            if not line:
                raise ValueError("blank line in draft")
            draft.append(line + "\n")
        
        with AtomicWriter(target) as file:
            file.write("".join(draft))
        
        return t['elapsed']
                