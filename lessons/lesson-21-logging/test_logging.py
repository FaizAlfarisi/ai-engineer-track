"""H1 suite — do NOT modify. Fix noisy_shop/ so all 5 pass."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

LESSON = Path(__file__).resolve().parent
SHOP = LESSON / "noisy_shop"


def run(args, **kwargs):
    env = {**os.environ, "PYTHONPATH": str(LESSON)}
    return subprocess.run(
        [sys.executable, *args], capture_output=True, text=True, env=env,
        **kwargs,
    )


def test_reconfig_takes_effect():
    with tempfile.TemporaryDirectory() as td:
        r = run(["-c",
                 "import logging; from noisy_shop.shop import setup_logging; "
                 "setup_logging(True); a = logging.getLogger().level == 10; "
                 "setup_logging(False); b = logging.getLogger().level == 30; "
                 "n = len(logging.getLogger().handlers) == 2; "
                 "print(a and b and n)"], cwd=td)
    assert r.returncode == 0
    assert r.stdout.strip() == "True"


def test_no_duplicate_warnings():
    with tempfile.TemporaryDirectory() as td:
        r = run(["-m", "noisy_shop.main"], cwd=td)
        assert r.returncode == 0
        assert r.stdout.strip() == "summary: ok=2 skipped=1"
        warns = [ln for ln in r.stderr.splitlines() if ln.startswith("WARNING")]
        assert warns == ["WARNING noisy_shop bad row 'mystery'"]


def test_debug_is_lazy():
    with tempfile.TemporaryDirectory() as td:
        r = run(["-c",
                 "import logging; from noisy_shop import shop; "
                 "logging.getLogger('noisy_shop').setLevel(logging.WARNING); "
                 "shop.CALLS.clear(); "
                 f"shop.load({str(SHOP / 'data.csv')!r}); "
                 "print(len(shop.CALLS))"], cwd=td)
    assert r.returncode == 0
    assert r.stdout.strip() == "0"


def test_warning_carries_traceback():
    with tempfile.TemporaryDirectory() as td:
        r = run(["-c",
                 "import io, logging; "
                 "records = []; "
                 "h = logging.StreamHandler(io.StringIO()); "
                 "h.addFilter("
                 "lambda r: records.append((r.levelname, r.exc_info is not None)) or True); "
                 "logging.getLogger().addHandler(h); "
                 "from noisy_shop.shop import process; "
                 "process([{'name': 'x', 'price': 'abc'}]); "
                 "print([x for x in records if x[0] == 'WARNING'])"], cwd=td)
    assert r.returncode == 0
    assert r.stdout.strip() == "[('WARNING', True)]"


def test_log_file_lives_beside_module():
    with tempfile.TemporaryDirectory() as td:
        r = run(["-m", "noisy_shop.main"], cwd=td)
        assert r.returncode == 0
        module_log = SHOP / "shop.log"
        try:
            assert not (Path(td) / "shop.log").exists()
            assert module_log.exists()
            assert "WARNING" in module_log.read_text(encoding="utf-8")
        finally:
            if module_log.exists():
                module_log.unlink()
