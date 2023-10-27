from typing import Iterable

from archist.predicate.be import TestFunctionType, BePredicate
from archist.rule.evaluation_rule import ExpectationRule, EvaluationResult, Fail, Ok
from archist.rule.filter_rule import FilterRule


class BeRule(FilterRule, ExpectationRule):
    be_predicate: BePredicate

    def __init__(self, test_function: TestFunctionType):
        self.be_predicate = BePredicate(test_function)

    def evaluate(self, node) -> EvaluationResult:
        if not self.be_predicate.test(node):
            return Fail(
                f"{self.__class__.__name__}: A node {node} was not as expected"
            )
        return Ok()

    def filter(self, nodes: Iterable) -> Iterable:
        yield from (
             node
             for node in nodes
             if self.be_predicate.test(node)
        )


def be(test_function: TestFunctionType) -> BeRule:
    return BeRule(test_function)
