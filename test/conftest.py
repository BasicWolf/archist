from pathlib import Path
from typing import Union

import pytest

from archist.model.module_node import ModuleNode

FIXTURES_PATH = Path(__file__).parent / 'fixtures'

StrPath = Union[str, Path]


@pytest.fixture
def module_with_one_import_path():
    path = FIXTURES_PATH / 'modules/a_module_with_one_import.py'
    assert path.exists()
    return path


@pytest.fixture
def fake_package(fs):
    def _fake_package(
        root_path: StrPath,
        package_name: str
    ) -> Path:
        sub_package_path = Path(root_path)
        for sub_package_name in package_name.split('.'):
            sub_package_path = sub_package_path / sub_package_name
            fs.create_file(sub_package_path / '__init__.py')
        return sub_package_path

    return _fake_package


@pytest.fixture
def fake_module(fs, fake_package):
    def _fake_module(
        root_path: StrPath,
        package_name: str,
        module_name: str,
        module_contents: str = ''
    ) -> Path:
        root_path = Path(root_path)

        module_file_name = module_name + '.py'
        package_path = fake_package(root_path, package_name)
        module_path = package_path / module_file_name
        fs.create_file(module_path, contents=module_contents)
        return module_path

    return _fake_module


@pytest.fixture
def fake_ns_package(fs):
    def _fake_ns_package(
        root_path: StrPath,
        package_name: str
    ) -> Path:
        sub_package_path = Path(root_path)
        for sub_package_name in package_name.split('.'):
            sub_package_path = sub_package_path / sub_package_name
            fs.create_dir(sub_package_path)
        return sub_package_path

    return _fake_ns_package


@pytest.fixture
def fake_ns_module(fs, fake_ns_package):
    def _fake_ns_module(
        root_path: StrPath,
        package_name: str,
        module_name: str
    ) -> Path:
        root_path = Path(root_path)

        module_file_name = module_name + '.py'
        package_path = fake_ns_package(root_path, package_name)
        module_path = package_path / module_file_name
        fs.create_file(module_path)
        return module_path

    return _fake_ns_module


@pytest.fixture
def a_module_node() -> ModuleNode:
    return ModuleNode(
        name='no_matter',
        package_name='does.not.matter',
        path=Path('/archist/does/not/matter/no_matter.py')
    )
