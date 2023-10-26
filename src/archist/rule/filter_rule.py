from abc import ABC, abstractmethod
from collections.abc import Iterable


class FilterRule(ABC):
    @abstractmethod
    def filter(self, nodes: Iterable) -> Iterable:
        ...
