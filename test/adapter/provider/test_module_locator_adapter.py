from pathlib import Path

from archist.adapter.provider.module_locator_adapter import ModuleLocatorAdapter
from archist.model.module_node import ModuleNode


def test_locates_modules_in_package(fake_module):
    fake_module('/archist', 'pkg1.sub2', 'a_module')
    module_nodes = ModuleLocatorAdapter().locate_modules('/archist')
    assert len(module_nodes) == 3


def test_module_has_correct_location(fake_module):
    fake_module('/archist', 'pkg1.sub2', 'a_module')

    module_nodes = ModuleLocatorAdapter().locate_modules('/archist')
    a_module_node = module_nodes[-1]

    assert a_module_node == ModuleNode(
        path=Path('/archist/pkg1/sub2/a_module.py'),
        package_name='pkg1.sub2',
        name='a_module'
    )


def test_locates_module_in_namespace_package(fake_ns_module):
    fake_ns_module('/archist', 'npkg1.nsub2', 'a_module')
    module_nodes = ModuleLocatorAdapter().locate_modules('/archist')
    assert len(module_nodes) == 1


def test_module_from_namespace_package_has_correct_location(fake_ns_module):
    fake_ns_module('/archist', 'npkg1.nsub2', 'a_module')

    module_nodes = ModuleLocatorAdapter().locate_modules('/archist')
    a_module_node = module_nodes[-1]

    assert a_module_node == ModuleNode(
        name='a_module',
        path=Path('/archist/npkg1/nsub2/a_module.py'),
        package_name='npkg1.nsub2'
    )
