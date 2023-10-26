from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Any

from archist.provider.module_provider import Module


class AbstractSource(Iterable, ABC):
    @staticmethod
    @abstractmethod
    def sourced_from(modules: Iterable[Module]) -> Any:
        ...
