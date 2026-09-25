"""H1 suite — do NOT modify. Fix messy_app/ so all 4 pass."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

LESSON = Path(__file__).resolve().parent


def run(args, **kwargs):
    return subprocess.run(
        [sys.executable, *args], capture_output=True, text=True, **kwargs
    )


def test_no_sys_path_hack():
    r = run(
        ["-c", "import sys, messy_app.main; "
               "print(sum('messy_app' in p for p in sys.path))"],
        cwd=LESSON,
    )
    assert r.stdout.strip() == "0"


def test_import_is_silent():
    r = run(["-c", "import messy_app"], cwd=LESSON)
    assert r.stdout == ""


def test_app_runs_as_script_with_root_context():
    env = {**os.environ, "PYTHONPATH": str(LESSON)}
    r = run(["messy_app/app.py"], cwd=LESSON, env=env)
    assert r.returncode == 0
    assert r.stdout.strip() == "items: 3"


def test_module_run_from_foreign_cwd():
    with tempfile.TemporaryDirectory() as td:
        env = {**os.environ, "PYTHONPATH": str(LESSON)}
        r = run(["-m", "messy_app.main"], cwd=td, env=env)
    assert r.returncode == 0
    assert r.stdout.strip() == "items: 3"
