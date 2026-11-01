"""Buggy clinic pipeline — PROVIDED, BUGGY (H1b).

Four planted bugs, one per H1 pattern. Nothing else in this file is wrong.
You fix it in place: run the DEBUGGING protocol, fix each where it lives,
do not restructure the module.

Exports: log_call, timed, retry, greet, confirm, send, flaky_send.
"""

import functools
import logging
import time

_ATTEMPTS = {}


def log_call(func):
    """Log entry and exit at INFO. Return contract unchanged."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):        
        logging.getLogger("clinic").info("call %s", func.__name__)
        result = func(*args, **kwargs)
        logging.getLogger("clinic").info("done %s", func.__name__)
        return result
    return wrapper


def timed(func):
    """Measure wall time. Result unchanged. Elapsed on wrapper.last_elapsed."""    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_elapsed = time.perf_counter() - start
    wrapper.last_elapsed = 0.0
    return wrapper


def retry(attempts, exc=(ConnectionError,)):
    """Retry on exc, total attempts times. Re-raise the last error."""
    if attempts < 1:
        raise ValueError("attempts must be >= 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):            
            last = None
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exc as err:
                    last = err
            raise last
        return wrapper
    return decorator


@log_call
def greet(appt, channel="sms"):
    """Greet one appointment over a channel."""
    return channel + ":" + appt["phone"]


@log_call
@timed
def confirm(appt):
    """Confirm one appointment."""
    return appt["phone"]


def _deliver(appt, channel):
    return channel + ":" + appt["phone"]


def send(appt, channel="sms"):
    """Send one reminder."""
    logging.getLogger("clinic").info("call send")    
    result = _deliver(appt, channel)
    logging.getLogger("clinic").info("done send")
    return result

@retry(attempts=3)
def flaky_send(appt):
    """Send with a gateway that drops the first two tries."""
    n = _ATTEMPTS.get(appt["phone"], 0) + 1
    _ATTEMPTS[appt["phone"]] = n
    if n < 3:
        raise ConnectionError("drop")
    return "sent:" + appt["phone"]
