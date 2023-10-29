import textwrap

import pytest

from archist.provider.class_node import ClassNode
from archist.provider.module import ModuleProvider
from archist.rule.source.classes import classes
from helper import extracting_names_from


def test_classes_source_yields_class_nodes(a_module_with_two_classes):
    classes_source = classes.sourced_from([a_module_with_two_classes])
    class_nodes: list[ClassNode] = list(classes_source)

    assert extracting_names_from(class_nodes) == ['MyClass', 'OtherClass']


@pytest.fixture
def a_module_with_two_classes(with_fake_python_namespace_module):
    with_fake_python_namespace_module(
        root_path='/my-class',
        module_contents=textwrap.dedent('''
            class MyClass:
                ...

            class OtherClass:
                ...
            ''')
    )
    return ModuleProvider().provide_from('/my-class')[0]
