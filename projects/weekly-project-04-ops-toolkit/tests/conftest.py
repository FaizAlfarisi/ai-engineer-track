import pytest

@pytest.fixture
def log_file_factory(tmp_path):
    def _create_file(content: str, filename: str = "app.log"):
        log_file = tmp_path / filename
        log_file.write_text(content, encoding="utf-8")
        return log_file
    
    return _create_file