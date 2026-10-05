# Weekly Project 3 — Feed Sync & Report Service

CLI to sync inventory from a stub API to local cache and generate stock reports.

## Install

```bash
python -m pip install -r requirements.txt
```

## Run

**Sync inventory:**
```bash
python main.py sync
```

**Logging modes:**
```bash
python main.py sync quiet
python main.py sync normal
python main.py sync verbose
```

**Report total value:**
```bash
python main.py report value
```

**Report low stock:**
```bash
python main.py report low 10
```

## Configuration

Override the API URL with `SYNC_API_BASE`:
```bash
SYNC_API_BASE=http://127.0.0.1:1 python main.py sync
```

## Test

```bash
python -m pytest tests -q
python -m mypy main.py
```

**Generated files:** `sync.json`, `sync.csv`, and `service.log`.