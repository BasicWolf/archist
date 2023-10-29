import re

from archist.provider.class_node import ClassNode


class HaveANameLikePredicate:
    name_pattern: str

    def __init__(self, name_pattern: str):
        self.name_pattern = name_pattern

    def test(self, node: ClassNode) -> bool:
        return re.match(self.name_pattern, node.name) is not None
