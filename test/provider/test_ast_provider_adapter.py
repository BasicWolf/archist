import ast
from pathlib import Path

import pytest

from archist.model.module_node import ModuleNode
from archist.provider.ast_provider import AstProvider


def test_provides_ast_for_a_module_node(a_module_node):
    module_node = AstProvider().process(a_module_node)
    assert isinstance(module_node.ast, ast.Module)


@pytest.fixture
def a_module_node(fake_module):
    fake_module('/archist', 'pkg', 'a_module', 'import math')

    return ModuleNode(
        name='a_module',
        path=Path('/archist/pkg/a_module.py'),
        package_name='pkg'
    )
