from dataclasses import dataclass
from typing import Protocol

from archist.port.ast_provider_port import ModuleNodeWithAst


@dataclass(kw_only=True)
class ClassNode:
    name: str


class ModuleWithClassNodes:
    class_nodes: list[ClassNode]


class ClassNodeProviderPort(Protocol):
    def process(self, module_node: ModuleNodeWithAst) -> ModuleWithClassNodes:
        ...
