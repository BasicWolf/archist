from pathlib import Path
from typing import Union

import pytest

from archist.model.basic_module import BasicModule

FIXTURES_PATH = Path(__file__).parent / 'fixtures'

StrPath = Union[str, Path]


@pytest.fixture
def with_fake_python_package(fs):
    def _with_fake_python_package(
        root_path: StrPath,
        package_name: str
    ) -> Path:
        sub_package_path = Path(root_path)
        for sub_package_name in package_name.split('.'):
            sub_package_path = sub_package_path / sub_package_name
            fs.create_file(sub_package_path / '__init__.py')
        return sub_package_path

    return _with_fake_python_package


@pytest.fixture
def with_fake_python_module(fs, with_fake_python_package):
    def _with_fake_python_module(
        root_path: StrPath,
        package_name: str,
        module_name: str,
        module_contents: str = ''
    ) -> Path:
        root_path = Path(root_path)

        module_file_name = module_name + '.py'
        package_path = with_fake_python_package(root_path, package_name)
        module_path = package_path / module_file_name
        fs.create_file(module_path, contents=module_contents)
        return module_path

    return _with_fake_python_module


@pytest.fixture
def with_fake_python_namespace_package(fs):
    def _with_fake_python_namespace_package(
        root_path: StrPath,
        package_name: str
    ) -> Path:
        sub_package_path = Path(root_path)
        for sub_package_name in package_name.split('.'):
            sub_package_path = sub_package_path / sub_package_name
            fs.create_dir(sub_package_path)
        return sub_package_path

    return _with_fake_python_namespace_package


@pytest.fixture
def with_fake_python_namespace_module(fs, with_fake_python_namespace_package):
    def _with_fake_python_namespace_module(
        root_path: StrPath,
        package_name: str,
        module_name: str
    ) -> Path:
        root_path = Path(root_path)

        module_file_name = module_name + '.py'
        package_path = with_fake_python_namespace_package(root_path, package_name)
        module_path = package_path / module_file_name
        fs.create_file(module_path)
        return module_path

    return _with_fake_python_namespace_module


@pytest.fixture
def basic_module_from_fake_python_module(with_fake_python_module):
    def _basic_module_from_fake_python_module(
            root_path: StrPath,
            package_name: str,
            module_name: str,
            module_contents: str = ''
    ) -> BasicModule:
        fake_module_path = with_fake_python_module(
            root_path,
            package_name,
            module_name,
            module_contents
        )

        return BasicModule(
            name='a_module',
            path=fake_module_path,
            package_name=package_name
        )
    return _basic_module_from_fake_python_module


@pytest.fixture
def a_basic_module(build_basic_module) -> BasicModule:
    return build_basic_module()


@pytest.fixture
def build_basic_module():
    def _build_basic_module(
        module_name='no_matter',
        package_name='does.not.matter',
        path=Path('/archist/does/not/matter/no_matter.py')
    ) -> BasicModule:
        return BasicModule(
            name=module_name,
            package_name=package_name,
            path=path
        )
    return _build_basic_module
