"""H2 suite — do NOT modify. Build report_tool/ so all 4 pass."""

import subprocess
import sys
from pathlib import Path

LESSON = Path(__file__).resolve().parent
GRADES = LESSON / "report_tool_flat" / "grades.csv"


def test_package_imports_clean(capsys):
    import report_tool

    assert capsys.readouterr().out == ""
    assert hasattr(report_tool, "__file__")


def test_summarize_exact():
    from report_tool.compute import summarize

    rows = [
        {"team": "red", "score": "10.0"},
        {"team": "blue", "score": "5.0"},
        {"team": "red", "score": "2.5"},
    ]
    assert summarize(rows) == {"red": 12.5, "blue": 5.0}


def test_cli_module_run(tmp_path):
    import shutil

    target = tmp_path / "grades.csv"
    shutil.copy(GRADES, target)
    r = subprocess.run(
        [sys.executable, "-m", "report_tool.main", str(target)],
        capture_output=True, text=True, cwd=LESSON,
    )
    assert r.returncode == 0
    assert r.stdout.strip() == "Summary (2 teams, 6 rows)"
    assert (tmp_path / "summary.csv").exists()


def test_readme_names_entry():
    text = (LESSON / "report_tool" / "README.md").read_text(encoding="utf-8")
    assert "python -m report_tool.main" in text
