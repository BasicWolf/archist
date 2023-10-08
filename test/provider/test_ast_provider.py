import ast

import pytest

from archist.provider.ast_provider import AstProvider


def test_provides_ast_for_a_module_node(a_module_node):
    module_node = AstProvider().provide_for(a_module_node)
    assert isinstance(module_node.ast, ast.Module)


@pytest.fixture
def a_module_node(fake_module_node):
    return fake_module_node('/archist', 'pkg', 'a_module', 'import math')
