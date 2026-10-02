import logging
from pathlib import Path

def setup_logging(mode: str = "normal") -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    
    if logger.handlers:
        logger.handlers.clear()
        
    formatter = logging.Formatter("%(filename)s %(name)s %(message)s")
    
    match mode:
        case "quiet":
            log_mode = logging.CRITICAL
        case "verbose":
            log_mode = logging.DEBUG
        case _:
            log_mode = logging.INFO
    
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_mode)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    file_path = Path(__file__).with_name("service.log")
    file_handler = logging.FileHandler(filename=file_path, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
    