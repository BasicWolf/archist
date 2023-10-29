from archist.rule.source.modules import ModuleSource
from helper import extracting_names_from


def test_modules_source_yields_modules(build_basic_module):
    module_source = ModuleSource().sourced_from([
        build_basic_module(module_name='first'),
        build_basic_module(module_name='second')
    ])

    modules = list(module_source)

    assert extracting_names_from(modules) == ['first', 'second']
