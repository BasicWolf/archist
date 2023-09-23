import ast
import textwrap
from typing import cast

import pytest

from archist.adapter.provider.class_node_provider_adapter import ClassNodeProviderAdapter
from archist.model.module_node import ModuleNode
from archist.port.provider.ast_provider_port import ModuleNodeWithAst
from archist.port.provider.class_node_provider_port import ClassNode


def test_provides_two_class_nodes_when_source_has_two_class_definitions(module_node_with_a_class):
    module_with_class_nodes = ClassNodeProviderAdapter().process(module_node_with_a_class)
    assert len(module_with_class_nodes.class_nodes) == 2


def test_provided_class_nodes_have_same_names_as_class_definitions(module_node_with_a_class):
    module_with_class_nodes = ClassNodeProviderAdapter().process(module_node_with_a_class)
    assert ['MyClass', 'MyOtherClass'] == _extract_class_names(module_with_class_nodes.class_nodes)


def _extract_class_names(class_nodes: list[ClassNode]) -> list[str]:
    return [class_node.name for class_node in class_nodes]


@pytest.fixture
def module_node_with_a_class(a_module_node) -> ModuleNodeWithAst:
    a_module_node.ast = ast.parse(textwrap.dedent("""\
    class MyClass:
        ...
      
    class MyOtherClass:
        ...
    """))
    return cast(ModuleNodeWithAst, a_module_node)


@pytest.fixture
def a_module_node() -> ModuleNode:
    return ModuleNode(
        name='does_not_matter',
        path='/archist/dnm/does_not_matter.py',
        package_name='dnm'
    )

