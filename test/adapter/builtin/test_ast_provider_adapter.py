import ast
from pathlib import Path

import pytest

from archist.adapter.builtin.ast_provider_adapter import AstProviderAdapter
from archist.model.module_node import ModuleNode


def test_provides_ast_for_a_module_node(a_module_node):
    module_node = AstProviderAdapter().process(a_module_node)
    assert isinstance(module_node.ast, ast.Module)


@pytest.fixture
def a_module_node(fake_module):
    fake_module('/archist', 'pkg', 'a_module', 'import math')

    return ModuleNode(
        path=Path('/archist/pkg/a_module.py'),
        package_name='pkg'
    )
