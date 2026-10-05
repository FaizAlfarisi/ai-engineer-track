from src.tracker.domain.entities import Request
from src.shared.utils.system_utils import fail


def argv_parser(argv: list[str]) -> Request:
    if len(argv) < 2:
        fail("usage: python main.py [sync | report]")

    command = argv[1]

    if command == "sync":
        if len(argv) == 2:
            return Request(command=command)

        if len(argv) == 3:
            log_mode = argv[2]

            if log_mode not in {"quiet", "normal", "verbose"}:
                fail(f"bad request:\ninvalid sync mode {log_mode!r}")

            return Request(
                command=command,
                mode=log_mode,
            )

        fail("bad request:\ninvalid arguments for sync")

    if command == "report":
        if len(argv) < 3:
            fail("usage: python main.py report [value | low N | summary | restock N]")

        subcommand = argv[2]

        if subcommand in {"value", "summary"}:
            if len(argv) != 3:
                fail(f"bad request:\nreport {subcommand!r} takes no arguments")

            return Request(
                command=command,
                subcommand=subcommand,
            )

        if subcommand in {"low", "restock"}:
            if len(argv) != 4:
                fail(f"bad request:\nreport {subcommand!r} requires N")

            try:
                threshold = int(argv[3])
            except ValueError:
                fail("bad request:\nN must be a non-negative integer")

            if threshold < 0:
                fail("bad request:\nN must be a non-negative integer")

            return Request(
                command=command,
                subcommand=subcommand,
                number=threshold,
            )

        fail(f"bad request: unknown report command {subcommand!r}")

    fail(f"bad request: unknown command {command!r}")
