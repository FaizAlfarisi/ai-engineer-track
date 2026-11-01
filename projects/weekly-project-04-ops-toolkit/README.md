# Ops Log Toolkit

## Problem
Large Log &rarr; Querying &rarr; Time Window

## Solution
CLI:
- Ingest .log &rarr; .json
- Time window result
- Report by latency
- Pull (fetching 'incident')

## Data Flow
```
app.log 
  ↓ [ingest] 
clean.json 
  ├──> [window start end] ──> bounded from start to end ──> str
  └──> [report slow N]    ──> sort descending by 'latency' ──> str

[fetch] ──> state.json
```
```
[ingest] & [fetch] ──> [quiet | normal | verbose] ──> ops.log
                       (quiet)   ──> stderr silent
                       (normal)  ──> INFO + on stderr (default)
                       (verbose) ──> DEBUG + on stderr

```

## Setup
```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

## Usage
```
1. Ingestion: python main.py ingest [quiet | normal | verbose]
└──> ingest logs/app.log to clean.json ─ as main file to reporting by time window and slowest

2. Time window result: python main.py window START END 
└──> report record in interval start to end (HH:MM:SS)

3. Report N slowest: python main.py report slow N
└──> report N slowest record sorted descending by 'latency'

4. Pull incident: python main.py fetch [quiet | normal | verbose]
└──> fetching 'incident' then write state.json
```

## Configuration
Override the API URL with `FEED_API_BASE`:
```bash
FEED_API_BASE=http://127.0.0.1:1 python main.py fetch
```

**Generated files:** `clean.json`, `state.json`, and `ops.log`.