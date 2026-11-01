# Decisions Log — Weekly Project 4

Filled by learner during build. One row per real decision.

| Decision | Why | Alternative Considered |
|----------|-----|------------------------|
| layered project structure with clean separation of concern; config as the single source of truth; domain for data transfer; services technical side; use_cases orchestrator of service; utils as shared reusable module | separating the concern each on layer let the development being easier and testable | flat project structure as the project scope is still small |
| regex sits in service layer | the usage of regex is exclusively for parsing log, not a reusable format | set new layer for regex as helper |
| error strategy with custom exception sits in utils | set the error handling with clean and consistent exception | set every exception with default class |
| build regex with named capturing group exclusively for date and time to parse it with datetime lib | only capture the date and time because the validation also work for format and int validation, so that after validating each line, the valid line could be split using space to get each value | capture each value for direct execution mapping and writing json, but the func cant be testable easily |
| parsing argv and routing to its func for main feature without stretch goal, but still considering the stretch goal development | fast developing for mvp, new approach compared to previous wp implementation | direct executing the parsing to stretch goal on parsing and routing, since the stretch goal just add a little condition anyway. |
| ingest handler with splitting data using space (' ') | loaded data already parsed with regex and have a consistent format | re capturing with regex for each data |
| create new entity RequestLog for data transfer consistencity between layer, utilize object hook on json decoder to convert each value with its expected type, raise error when violated | clean.json can be corrupt mid way of production, so object hook decoder is necessary to prevent any inconsistencity type and ensure every action isnt raising unexpected error | no json decoder would set the program error if there any corrupt data on production, so no other alternative for this approach |