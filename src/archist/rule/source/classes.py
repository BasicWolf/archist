from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Self

from archist.provider.class_node import ClassNode
from archist.provider.module import Module
from .source import Source


class ClassesSource(Source):
    class_nodes: list[ClassNode]

    def __iter__(self) -> Iterator[ClassNode]:
        return iter(self.class_nodes)

    def sourced_from(self, modules: Iterable[Module]) -> Self:
        class_nodes = [
            class_node
            for module in modules
            for class_node in module.class_nodes
        ]
        self.class_nodes = class_nodes
        return self


classes = ClassesSource()
