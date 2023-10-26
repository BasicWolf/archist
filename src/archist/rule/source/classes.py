from __future__ import annotations

from collections.abc import Iterable

from archist.provider.class_node_provider import ClassNode
from archist.provider.module_provider import Module
from archist.rule.implication import Implication
from archist.rule.source.source import Source
from archist.rule.validation.validator import Validator


class Classes(Source):
    class_nodes: list[ClassNode]

    def __init__(self, class_nodes: list[ClassNode] | None = None):
        if class_nodes is None:
            class_nodes = []

        self.class_nodes = class_nodes

    def __iter__(self):
        return iter(self.class_nodes)

    def should(self, validator: Validator) -> Implication:
        return Implication(self, validator)

    @staticmethod
    def sourced_from(modules: Iterable[Module]) -> Classes:
        class_nodes = [
            class_node
            for module in modules
            for class_node in module.class_nodes
        ]
        return Classes(class_nodes)


classes = Classes()
