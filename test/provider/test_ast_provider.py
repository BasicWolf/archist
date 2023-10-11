import ast

import pytest

from archist.provider.ast_provider import AstProvider


def test_provides_ast_for_a_module_node(a_basic_module):
    module_node = AstProvider().provide_for(a_basic_module)
    assert isinstance(module_node.ast, ast.Module)


@pytest.fixture
def a_basic_module(fake_module_node):
    return fake_module_node('/archist', 'pkg', 'a_module', 'import math')
