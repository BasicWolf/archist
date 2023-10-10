from typing import Iterable

from archist.provider.class_node_provider import ClassNode
from archist.provider.module_provider import ProvidedModuleNode
from archist.rule.filter_rule import FilterRule
from archist.rule.implication import Implication


class Classes(FilterRule):
    def filter(self, nodes: Iterable[ProvidedModuleNode]) -> Iterable[ClassNode]:
        return (
            class_node
            for node in nodes
            for class_node in node.class_nodes
        )

    @property
    def should(self) -> Implication:
        return Implication(self)


classes = Classes()
