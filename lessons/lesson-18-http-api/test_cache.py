import os
import json
import sys
import subprocess
from pathlib import Path

def test_cache_with_seed(tmp_path):
    cache_file = tmp_path / "cache.json"
    seeded_data = {
        "items": [
            {"id": 5, "name": "donut", "price": 1.0, "stock": 3}
        ]
    }
    cache_file.write_text(json.dumps(seeded_data))

    cli_path = str(Path(__file__).parent / "cache_cli.py")
    env = {**os.environ, "PYTHONPATH": str(Path(__file__).parent)}
    
    result = subprocess.run(
        [sys.executable, cli_path, "--refresh"],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True
    )

    assert "Cache: 5 items (fresh 4, cached 1)" in result.stdout
    assert (tmp_path / "cache.json").exists()
    assert (tmp_path / "cache.csv").exists()
    
    output_cache = json.loads((tmp_path / "cache.json").read_text(encoding="utf-8"))
    merged_ids = [item["id"] for item in output_cache["items"]]
    assert merged_ids == [1, 2, 3, 4, 5]

def test_cache_no_seed(tmp_path):
    cli_path = str(Path(__file__).parent / "cache_cli.py")
    env = {**os.environ, "PYTHONPATH": str(Path(__file__).parent)}
    
    result = subprocess.run(
        [sys.executable, cli_path, "--refresh"],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True
    )

    assert "Cache: 4 items (fresh 4, cached 0)" in result.stdout