from abc import abstractmethod

from archist.port.predicate.predicate import Predicate
from archist.port.provider.class_node_provider_port import ClassNode


class ClassHasANameLikePredicatePort(Predicate):
    name_pattern: str

    @abstractmethod
    def test(self, node: ClassNode) -> bool:
        ...
