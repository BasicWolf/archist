import abc
from abc import abstractmethod
from typing import Iterable


class FilterRule(abc.ABC):
    @abstractmethod
    def filter(self, nodes: Iterable) -> Iterable:
        ...
