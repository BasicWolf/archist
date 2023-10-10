import textwrap

import pytest

from archist.provider.module_provider import ModuleProvider
from archist.rule.classes import classes


def test_classes_rule_checks_something_something(a_module_with_my_class):
    assert classes.should.be(lambda class_node: class_node.name.startswith('My')).check([
        a_module_with_my_class
    ])


@pytest.fixture
def a_module_with_my_class(fake_module_node):
    fake_module_node('/my-class', 'pkg', 'a_module', textwrap.dedent('''\
    class MyClass:
        ...
    '''))
    return ModuleProvider().provide_from('/my-class')[1]
