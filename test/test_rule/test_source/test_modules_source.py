from archist.provider.module import Module
from archist.rule.source.modules import ModuleSource


def test_modules_source_yields_modules(build_basic_module):
    module_source = ModuleSource().sourced_from([
        build_basic_module(module_name='first'),
        build_basic_module(module_name='second')
    ])
    modules = list(module_source)
    assert ['first', 'second'] == extracting_module_names(modules)


def extracting_module_names(modules: list[Module]) -> list[str]:
    return [module.name for module in modules]
