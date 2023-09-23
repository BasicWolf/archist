from dataclasses import dataclass
from typing import Protocol

from archist.model.module_node import ModuleNode
from archist.port.provider.ast_provider_port import ModuleNodeWithAst


@dataclass(kw_only=True)
class ClassNode:
    name: str
    module_node: ModuleNode


class ModuleWithClassNodes:
    class_nodes: list[ClassNode]


class ClassNodeProviderPort(Protocol):
    def process(self, module_node: ModuleNodeWithAst) -> ModuleWithClassNodes:
        ...
