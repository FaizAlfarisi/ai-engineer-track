"""H2 suite — do NOT modify. Build tracked/ so all 4 pass."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

LESSON = Path(__file__).resolve().parent


def run(args, **kwargs):
    env = {**os.environ, "PYTHONPATH": str(LESSON)}
    return subprocess.run(
        [sys.executable, *args], capture_output=True, text=True, env=env,
        **kwargs,
    )


def test_package_imports_silent():
    r = run(["-c", "import tracked"], cwd=LESSON)
    assert r.returncode == 0
    assert r.stdout == ""
    assert r.stderr == ""


def test_totals_exact():
    r = run(["-c",
             "from tracked.compute import totals; "
             "rows = [{'team': 'red', 'score': '10.0'}, "
             "        {'team': 'blue', 'score': '5.0'}, "
             "        {'team': 'red', 'score': '2.5'}]; "
             "print(totals(rows))"], cwd=LESSON)
    assert r.returncode == 0
    assert r.stdout.strip() == "{'red': 12.5, 'blue': 5.0}"


def test_cli_separates_streams():
    with tempfile.TemporaryDirectory() as td:
        import shutil

        target = Path(td) / "data.csv"
        shutil.copy(LESSON / "plain_run" / "data.csv", target)
        r = run(["-m", "tracked.main", str(target)], cwd=td)
        assert r.returncode == 0
        assert r.stdout.strip() == "Summary (2 teams, 4 rows)"
        assert "INFO" in r.stderr
        assert "Summary" not in r.stderr
        module_log = LESSON / "tracked" / "tracked.log"
        try:
            assert module_log.exists()
            assert "DEBUG" in module_log.read_text(encoding="utf-8")
        finally:
            if module_log.exists():
                module_log.unlink()


def test_readme_names_entry():
    text = (LESSON / "tracked" / "README.md").read_text(encoding="utf-8")
    assert "python -m tracked.main" in text
