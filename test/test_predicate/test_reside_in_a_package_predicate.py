import os
from pathlib import Path

import pytest

from archist.predicate import ResideInAPackagePredicate
from archist.provider.class_node import ClassNode


def test_class_resides_in_a_package(class_in_a_package):
    assert ResideInAPackagePredicate('pkg.sub') \
        .test(class_in_a_package('pkg.sub'))


def test_class_resides_in_a_sub_package(class_in_a_package):
    assert ResideInAPackagePredicate('pkg') \
        .test(class_in_a_package('pkg.sub'))


def test_class_in_another_package_does_not_reside_in_this_package(class_in_a_package):
    assert not ResideInAPackagePredicate('topman') \
        .test(class_in_a_package('pkg'))


def test_class_in_another_sub_package_does_not_reside_in_this_package(class_in_a_package):
    assert not ResideInAPackagePredicate('pkg.sub') \
        .test(class_in_a_package('pkg.sub_other'))


@pytest.fixture
def class_in_a_package(build_basic_module):
    def _class_in_a_package(package_name: str) -> ClassNode:
        package_path = package_name.replace('.', os.sep)

        return ClassNode(
            name='DoesNotMatter',
            module=build_basic_module(
                package_name=package_name,
                path=Path('/does/not/matter') / package_path / 'no_matter.py'
            )
        )
    return _class_in_a_package
