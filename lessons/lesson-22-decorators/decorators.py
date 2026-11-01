import logging
import time
import functools


def log_call(func):
    """Log entry"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger("clinic")
        logger.info("call %s", func.__name__)
        result = func(*args, **kwargs)
        logger.info("done %s", func.__name__)
        return result
    return wrapper

def timed(func):
    """Record the time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_elapsed = time.perf_counter() - start
        
    wrapper.last_elapsed = 0.0
    return wrapper

def validate_appointment(func):
    """Inspect and validate the appointment data"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        appt = None
        
        if args:
            appt = args[0]
                
        elif "appt" in kwargs:
            appt = kwargs["appt"]
        
        if not isinstance(appt, dict):
            raise ValueError("invalid appointment: not a dict")
        
        def is_empty(val):
            if not isinstance(val, str):
                return True
            return not val.strip()
        
        if is_empty(appt.get("name")):
            raise ValueError("invalid name: empty")
        if is_empty(appt.get("phone")):
            raise ValueError("invalid phone: empty")
        if is_empty(appt.get("time")):
            raise ValueError("invalid time: empty")

        return func(*args, **kwargs)
    
    return wrapper
        
def retry(attempts, exc=(ConnectionError,)):
    """Retry on exc, total attempts times. Re-raise the last error"""
    if attempts < 1:
        raise ValueError("attempts must be >= 1")
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(attempts):
                last = None
                try:
                    return func(*args, **kwargs)
                except exc as err:
                    last = err
            raise last
        return wrapper
    return decorator