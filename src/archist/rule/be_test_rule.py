from archist.predicate.be import TestFunctionType, BePredicate
from archist.rule.test_rule import TestRule


class BeTestRule(TestRule):
    be_predicate: BePredicate

    def __init__(self, test_function: TestFunctionType):
        self.be_predicate = BePredicate(test_function)

    def test(self, node) -> bool:
        return self.be_predicate.test(node)
