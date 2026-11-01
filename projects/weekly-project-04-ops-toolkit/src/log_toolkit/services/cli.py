import sys
from datetime import datetime
from src.utils.system_utils import fail
from src.log_toolkit.domain.entities import RequestArgv

def argv_parser(argv: list[str]) -> RequestArgv:
    if len(argv) < 2:
        fail("usage: python main.py [ingest | fetch | window | report]")
    
    command = argv[1]
    
    if command == "ingest" or command == "fetch":
        if len(argv) == 2:
            return RequestArgv(command=command)
        
        if len(argv) == 3:
            log_mode = argv[2]
            
            if log_mode not in ["quiet", "normal", "verbose"]:
                fail(f"bad request:\ninvalid logging mode {log_mode!r}")
            
            return RequestArgv(
                command=command,
                mode=log_mode
            )

        fail(f"bad request:\ninvalid arguments for {command}")
        
    if command == "window":
        if len(argv) == 4:
            raw_start = argv[2]
            raw_end = argv[3]
            
            TIME_CANON = "%H:%M:%S"
            
            try:
                start = datetime.strptime(raw_start, TIME_CANON).time()
                end = datetime.strptime(raw_end, TIME_CANON).time()
            except ValueError:
                fail("bad request:\ntimes must be HH:MM:SS")
        
            if start.strftime(TIME_CANON) != raw_start or end.strftime(TIME_CANON) != raw_end:
                fail("bad request:\ntimes must be HH:MM:SS")
        
            if start > end:
                fail("bad request:\nstart must not be after end")
            
            return RequestArgv(
                command=command,
                start=start,
                end=end
            )
        fail(f"bad request:\ninvalid arguments for window")
    
    if command == "report":
        if len(argv) == 4 and argv[2] == "slow":
            try:
                n = int(argv[3])
            except ValueError:
                fail(f"bad request:\nN must be a non-negative integer")
                
            if n < 0:
                fail(f"bad request:\nN must be a non-negative integer")
                

            return RequestArgv(
                command=command,
                subcommand=argv[2],
                number=n
            )
            
        fail(f"bad request:\ninvalid arguments for report")
    
    fail(f"bad request:\nunknown command {command!r}")