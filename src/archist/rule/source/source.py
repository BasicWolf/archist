from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable

from archist.provider.module import Module


class Source(Iterable, ABC):
    @abstractmethod
    def sourced_from(self, modules: Iterable[Module]) -> Source:
        ...
