from abc import abstractmethod

from archist.port.predicate.predicate import Predicate
from archist.port.provider.class_node_provider_port import ClassNode


class ClassResidesInAPackagePort(Predicate):
    @abstractmethod
    def test(self, class_node: ClassNode) -> bool:
        ...
