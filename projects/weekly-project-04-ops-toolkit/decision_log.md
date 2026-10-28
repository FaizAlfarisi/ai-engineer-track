# Decisions Log — Weekly Project 4

Filled by learner during build. One row per real decision.

| Decision | Why | Alternative Considered |
|----------|-----|------------------------|
| layered project structure with clean separation of concern; config as the single source of truth; domain for data transfer; services technical side; use_cases orchestrator of service; utils as shared reusable module | separating the concern each on layer let the development being easier and testable | flat project structure as the project scope is still small |
| regex sits in service layer | the usage of regex is exclusively for parsing log, not a reusable format | set new layer for regex as helper |
| error strategy with custom exception sits in utils | set the error handling with clean and consistent exception | set every exception with default class |
| build regex with named capturing group exclusively for date and time to parse it with datetime lib | only capture the date and time because the validation also work for format and int validation, so that after validating each line, the valid line could be split using space to get each value | capture each value for direct execution mapping and writing json, but the func cant be testable easily |
| 
