from typing import Iterable, Any

import pytest

from archist.provider.module_provider import Module
from archist.rule.evaluation_rule import ExpectationRule, EvaluationResult, Ok, Fail
from archist.rule.implication import Implication
from archist.rule.source.source import Source


@pytest.fixture
def dummy_source():
    return DummySource()


class DummyExpectationRule(ExpectationRule):
    def evaluate(self, node) -> EvaluationResult:
        return Ok()


class DummySource(Source):
    modules: Iterable[Module]

    def __init__(self, modules: Iterable | None = None):
        if modules is None:
            modules = []
        self.modules = modules

    def sourced_from(self, modules: Iterable[Module]) -> Any:
        return DummySource(modules)

    def should(self, validator: ExpectationRule) -> Implication:
        return Implication(self, validator)

    def __iter__(self):
        return iter(self.modules)


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Fail) and right == Ok() and op == "==":
        return [
            str(left),
        ]
