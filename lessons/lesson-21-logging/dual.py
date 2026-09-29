import logging

def setup(level_name: str, path: str, stream) -> logging.Logger:
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.propagate = False
    
    if log.handlers:
        log.handlers.clear()
    
    stream_handler = logging.StreamHandler(stream)
    stream_handler.setLevel(level=getattr(logging, level_name.upper()))
    stream_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    log.addHandler(stream_handler)
    
    file_handler = logging.FileHandler(filename=path, mode="w", encoding="utf-8")
    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(name)s %(message)s"))
    
    log.addHandler(file_handler)
        
    return log