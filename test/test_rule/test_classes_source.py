import textwrap

import pytest

from archist.provider.module_provider import ModuleProvider
from archist.rule.source import classes


def test_classes_source_yields_class_nodes(a_module_with_two_classes):
    source_class_nodes = classes.sourced_from([a_module_with_two_classes])
    assert 2 == len(list(source_class_nodes))


@pytest.fixture
def a_module_with_two_classes(with_fake_python_module):
    with_fake_python_module(root_path='/my-class', module_contents=textwrap.dedent('''
        class MyClass:
            ...

        class OtherClass:
            ...
        '''))
    return ModuleProvider().provide_from('/my-class')[1]
