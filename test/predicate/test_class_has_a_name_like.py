import pytest

from archist.predicate import ClassHasANameLikePredicate
from archist.provider.class_node_provider import ClassNode


def test_class_name_corresponds_to_predicate_pattern(class_node):
    assert ClassHasANameLikePredicate('^.*Figure') \
        .test(class_node('MyFigure'))


def test_class_name_does_not_correspond_to_predicate_pattern(class_node):
    assert not ClassHasANameLikePredicate('^.*Spot') \
        .test(class_node('MyFigure'))


@pytest.fixture
def class_node(a_module_node):
    def _make_a_class_node(name: str):
        return ClassNode(
            name=name,
            module_node=a_module_node
        )

    return _make_a_class_node
