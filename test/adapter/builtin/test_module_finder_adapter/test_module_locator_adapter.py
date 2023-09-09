from pathlib import Path

from archist.adapter.builtin.module_locator_adapter import ModuleLocatorAdapter
from archist.model.module_location import ModuleLocation


def test_locates_modules_in_package(fake_module):
    fake_module('/archist', 'pkg1.sub2', 'a_module')
    modules_locations = ModuleLocatorAdapter().locate_modules('/archist')
    assert len(modules_locations) == 3


def test_module_has_correct_location(fake_module):
    fake_module('/archist', 'pkg1.sub2', 'a_module')

    modules_locations = ModuleLocatorAdapter().locate_modules('/archist')
    a_module_location = modules_locations[-1]

    assert a_module_location == ModuleLocation(
        Path('/archist/pkg1/sub2/a_module.py'),
        'pkg1.sub2'
    )


def test_locates_module_in_namespace_package(fake_ns_module):
    fake_ns_module('/archist', 'npkg1.nsub2', 'a_module')
    modules_locations = ModuleLocatorAdapter().locate_modules('/archist')
    assert len(modules_locations) == 1


def test_module_from_namespace_package_has_correct_location(fake_ns_module):
    fake_ns_module('/archist', 'npkg1.nsub2', 'a_module')

    module_locations = ModuleLocatorAdapter().locate_modules('/archist')
    a_module_location = module_locations[-1]

    assert a_module_location == ModuleLocation(
        Path('/archist/npkg1/nsub2/a_module.py'),
        'npkg1.nsub2'
    )
