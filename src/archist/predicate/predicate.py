from abc import ABC, abstractmethod
from typing import Any


class Predicate(ABC):
    @abstractmethod
    def test(self, node: Any) -> bool:
        ...
