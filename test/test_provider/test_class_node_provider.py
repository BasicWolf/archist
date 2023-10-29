import ast
import textwrap
from typing import cast

import pytest

from archist.provider.ast import ModuleWithAst
from archist.provider.class_node import ClassNodeProvider
from helper import extracting_names_from


def test_provides_two_class_nodes_when_source_has_two_class_definitions(
    module_node_with_two_classes_in_ast
):
    module_with_class_nodes = ClassNodeProvider().provide_for(
        module_node_with_two_classes_in_ast
    )
    assert len(module_with_class_nodes.class_nodes) == 2


def test_provided_class_nodes_have_same_names_as_class_definitions(
    module_node_with_two_classes_in_ast
):
    module_with_class_nodes = ClassNodeProvider().provide_for(
        module_node_with_two_classes_in_ast
    )

    assert extracting_names_from(module_with_class_nodes.class_nodes) \
           == ['MyClass', 'MyOtherClass']


@pytest.fixture
def module_node_with_two_classes_in_ast(a_basic_module) -> ModuleWithAst:
    a_basic_module.ast = ast.parse(textwrap.dedent("""
        class MyClass:
            ...

        class MyOtherClass:
            ...
    """))
    return cast(ModuleWithAst, a_basic_module)
