from pathlib import Path

from archist.model.basic_module import BasicModule
from archist.provider.basic_module_provider import BasicModuleProvider


def test_locates_modules_in_package(with_fake_module):
    with_fake_module('/archist', 'pkg1.sub2', 'a_module')
    module_nodes = BasicModuleProvider().provide_from('/archist')
    assert len(module_nodes) == 3


def test_module_has_correct_location(with_fake_module):
    with_fake_module('/archist', 'pkg1.sub2', 'a_module')

    module_nodes = BasicModuleProvider().provide_from('/archist')
    a_module_node = module_nodes[-1]

    assert a_module_node == BasicModule(
        path=Path('/archist/pkg1/sub2/a_module.py'),
        package_name='pkg1.sub2',
        name='a_module'
    )


def test_locates_module_in_namespace_package(with_fake_ns_module):
    with_fake_ns_module('/archist', 'npkg1.nsub2', 'a_module')
    module_nodes = BasicModuleProvider().provide_from('/archist')
    assert len(module_nodes) == 1


def test_module_from_namespace_package_has_correct_location(with_fake_ns_module):
    with_fake_ns_module('/archist', 'npkg1.nsub2', 'a_module')

    module_nodes = BasicModuleProvider().provide_from('/archist')
    a_module_node = module_nodes[-1]

    assert a_module_node == BasicModule(
        name='a_module',
        path=Path('/archist/npkg1/nsub2/a_module.py'),
        package_name='npkg1.nsub2'
    )
