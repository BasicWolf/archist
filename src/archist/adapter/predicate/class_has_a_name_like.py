import re

from archist.port.predicate.class_has_a_name_like_port import ClassHasANameLikePredicatePort
from archist.port.provider.class_node_provider_port import ClassNode


class ClassHasANameLikePredicate(ClassHasANameLikePredicatePort):
    name_pattern: str

    def __init__(self, name_pattern: str):
        self.name_pattern = name_pattern

    def test(self, node: ClassNode) -> bool:
        return re.match(self.name_pattern, node.name) is not None
