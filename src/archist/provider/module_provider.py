from pathlib import Path
from typing import Protocol, cast

from archist.model.module_node import ModuleNode, ModuleNodeBase
from archist.provider.ast_provider import AstProvider, ModuleNodeWithAst
from archist.provider.class_node_provider import ModuleWithClassNodes, ClassNodeProvider
from archist.provider.module_node_provider import ModuleNodeProvider

RichModuleNode = ModuleNode | ModuleNodeWithAst


class ProvidedModuleNode(
    ModuleNodeWithAst,
    ModuleWithClassNodes,
    ModuleNodeBase,
    Protocol
):
    ...


class ModuleProvider:
    def __init__(self):
        self.module_node_provider = ModuleNodeProvider()
        self.ast_provider = AstProvider()
        self.class_node_provider = ClassNodeProvider()

    def provide_from(self, path: str | Path) -> list[ProvidedModuleNode]:
        module_nodes = self.module_node_provider.provide_from(path)
        for module_node in module_nodes:
            module_node_with_ast = self.ast_provider.provide_for(module_node)

            self.class_node_provider.provide_for(module_node_with_ast)

        ret = cast(list[ProvidedModuleNode], module_nodes)
        return ret
