import sys
from typing import NoReturn

def fail(message: str) -> NoReturn:
    sys.stderr.write(message + '\n')
    sys.exit(1)