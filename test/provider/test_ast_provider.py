import ast

from archist.provider.ast_provider import AstProvider


def test_provides_ast_for_a_module_node(basic_module_from_fake_python_module):
    module = basic_module_from_fake_python_module()
    module_node = AstProvider().provide_for(module)
    assert isinstance(module_node.ast, ast.Module)
