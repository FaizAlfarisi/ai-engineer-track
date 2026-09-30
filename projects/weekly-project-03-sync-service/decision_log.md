# Sync Service — Decisions Log

Fill during the build: every non-trivial choice gets a row (Why +
Alternative Considered). Empty rows at review time read as undesigned.

| No | Decision | Why | Alternative Considered |
|----|----------|-----|------------------------|
| 1. | Project structure: src foldering, didnt follow the wp2 project structure | Considering The scope of this cli client project, consuming api, a little process, and data reporting. <br>Src layer was chosen in consideration of *Separation of Concern*. <br>**domain** defining dataclass in this case is Item. <br>**config** as central brain of project with a single source of truth, logger set here. <br>**service** as technical service, handling api calls, load & write file. <br>**use_cases** as core logic, business logic related, handle sync and report| a single well-structured main.py or simpler src foldering, combining the service and use cases. |
| 2. | cli routing: cli.argv_parser handle the argv request, return Request entity or direct shut down the system | new service/cli.py to handle the technical layer of cli parsing, written with full validation for each command, dataclass Request for routing in main.py | no service/cli.py for simpler foldering and calling function. |