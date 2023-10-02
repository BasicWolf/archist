import pytest

from archist.adapter.predicate.class_resides_in_a_package import ClassResidesInAPackage
from archist.port.provider.class_node_provider_port import ClassNode


def test_class_resides_in_a_package(class_in_a_package):
    assert ClassResidesInAPackage('pkg.sub') \
        .test(class_in_a_package('pkg.sub'))


def test_class_resides_in_a_sub_package(class_in_a_package):
    assert ClassResidesInAPackage('pkg') \
        .test(class_in_a_package('pkg.sub'))


def test_class_in_another_package_does_not_reside_in_this_package(class_in_a_package):
    assert not ClassResidesInAPackage('topman') \
        .test(class_in_a_package('pkg'))


def test_class_in_another_sub_package_does_not_reside_in_this_package(class_in_a_package):
    assert not ClassResidesInAPackage('pkg.sub') \
        .test(class_in_a_package('pkg.sub_other'))


@pytest.fixture
def class_in_a_package(module_node_in_package):
    def _class_in_a_package(package_name: str) -> ClassNode:
        return ClassNode(
            name='DoesNotMatter',
            module_node=module_node_in_package(package_name)
        )
    return _class_in_a_package
