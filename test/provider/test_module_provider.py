import ast
import textwrap
from pathlib import Path
from typing import cast

import pytest

from archist.model.module_node import ModuleNode
from archist.provider.module_provider import ModuleProvider, ProvidedModuleNode


def test_provides_module_node(a_module_with_a_single_import):
    pmn = ModuleProvider().provide_from('/single-import')[1]

    assert pmn.name == 'a_module'
    assert pmn.path == Path('/single-import/pkg/a_module.py')
    assert pmn.package_name == 'pkg'


def test_provides_module_node_with_ast(
    a_module_with_a_single_import,
    get_import_name
):
    pmn = ModuleProvider().provide_from('/single-import')[1]
    assert 'math' == get_import_name(pmn)


def test_provides_module_node_with_class_nodes(
    a_module_with_my_class,
    get_class_name
):
    pmn = ModuleProvider().provide_from('/my-class')[1]
    assert 'MyClass' == get_class_name(pmn)


@pytest.fixture
def a_module_with_a_single_import(fake_module):
    fake_module('/single-import', 'pkg', 'a_module', 'import math')

    return ModuleNode(
        name='a_module',
        path=Path('/single-import/pkg/a_module.py'),
        package_name='pkg'
    )


@pytest.fixture
def a_module_with_my_class(fake_module):
    fake_module('/my-class', 'pkg', 'a_module', textwrap.dedent('''\
    class MyClass:
        ...
    '''))

    return ModuleNode(
        name='a_module',
        path=Path('/my-class/pkg/a_module.py'),
        package_name='pkg'
    )


@pytest.fixture
def get_import_name():
    def _get_import_name(pmn: ProvidedModuleNode) -> str:
        ast_import_statement = cast(ast.Import, pmn.ast.body[0])
        imported_names = ast_import_statement.names
        return imported_names[0].name
    return _get_import_name


@pytest.fixture
def get_class_name():
    def _get_class_name(pmn: ProvidedModuleNode) -> str:
        return pmn.class_nodes[0].name

    return _get_class_name
