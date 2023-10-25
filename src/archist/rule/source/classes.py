from __future__ import annotations

from typing import Iterable

from archist.provider.class_node_provider import ClassNode
from archist.provider.module_provider import Module


class Classes:
    class_nodes: list[ClassNode]

    def __init__(self, class_nodes: list[ClassNode] | None = None):
        if class_nodes is None:
            class_nodes = []

        self.class_nodes = class_nodes

    @staticmethod
    def sourced_from(modules: Iterable[Module]) -> Classes:
        class_nodes = [
            class_node
            for module in modules
            for class_node in module.class_nodes
        ]
        return Classes(class_nodes)

    def __iter__(self):
        return iter(self.class_nodes)


classes = Classes()
