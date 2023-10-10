from abc import ABC, abstractmethod


class TestRule(ABC):
    @abstractmethod
    def test(self, node) -> bool:
        ...
