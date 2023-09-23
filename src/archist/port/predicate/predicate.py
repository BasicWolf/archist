from typing import Protocol, Any


class Predicate(Protocol):
    def test(self, node: Any) -> bool:
        ...
