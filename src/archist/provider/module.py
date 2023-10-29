from pathlib import Path
from typing import Protocol, cast

from archist.model.basic_module import BasicModuleProtocol
from archist.provider.ast import AstProvider, ModuleWithAst
from archist.provider.basic_module import BasicModuleProvider
from archist.provider.class_node import ModuleWithClassNodes, ClassNodeProvider


class Module(
    ModuleWithAst,
    ModuleWithClassNodes,
    BasicModuleProtocol,
    Protocol
):
    ...


class ModuleProvider:
    def __init__(self):
        self.basic_module_provider = BasicModuleProvider()
        self.ast_provider = AstProvider()
        self.class_node_provider = ClassNodeProvider()

    def provide_from(self, path: str | Path) -> list[Module]:
        basic_modules = self.basic_module_provider.provide_from(path)
        for module in basic_modules:
            self.ast_provider.provide_for(module)
            self.class_node_provider.provide_for(cast(ModuleWithAst, module))

        ret = cast(list[Module], basic_modules)
        return ret
