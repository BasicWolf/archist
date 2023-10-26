from typing import Iterable

from archist.predicate.be import TestFunctionType, BePredicate
from archist.rule.filter_rule import FilterRule
from archist.rule.test_rule import TestRule, TestResult, Fail, Ok


class BeRule(FilterRule, TestRule):
    be_predicate: BePredicate

    def __init__(self, test_function: TestFunctionType):
        self.be_predicate = BePredicate(test_function)

    def test(self, node) -> TestResult:
        if not self.be_predicate.test(node):
            return Fail()
        return Ok()

    def filter(self, nodes: Iterable) -> Iterable:
        yield from (
             node
             for node in nodes
             if self.be_predicate.test(node)
        )


def be(test_function: TestFunctionType) -> BeRule:
    return BeRule(test_function)
