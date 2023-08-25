import pytest
from pathlib import Path

FIXTURES_PATH = Path(__file__).parent / 'fixtures'


@pytest.fixture
def module_with_one_import_path():
    path = FIXTURES_PATH / 'modules/a_module_with_one_import.py'
    assert path.exists()
    return path
