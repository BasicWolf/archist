from collections.abc import Iterable
from typing import Self

from archist.provider.module import Module
from .source import Source


class ModuleSource(Source):
    modules: Iterable[Module]

    def sourced_from(self, modules: Iterable[Module]) -> Self:
        self.modules = modules
        return self

    def __iter__(self):
        return iter(self.modules)


modules = ModuleSource()
