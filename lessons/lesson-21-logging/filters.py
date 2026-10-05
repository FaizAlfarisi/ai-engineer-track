def visible(level: str, threshold: str) -> bool:
    LEVELS = {
        "DEBUG": 10,
        "INFO": 20,
        "WARNING": 30,
        "ERROR": 40,
        "CRITICAL": 50,
    }
    
    return LEVELS[level] >= LEVELS[threshold]
