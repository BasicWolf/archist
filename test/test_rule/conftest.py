from typing import Iterable, Any

import pytest

from archist.provider.module_provider import Module
from archist.rule.implication import Implication
from archist.rule.source.source import Source
from archist.rule.test_rule import TestRule, TestResult, Ok


@pytest.fixture
def dummy_source():
    return DummySource()


@pytest.fixture
def dummy_validator():
    return DummyValidatorRule


class DummyValidatorRule(TestRule):

    def test(self, node) -> TestResult:
        return Ok()


class DummySource(Source):
    @staticmethod
    def sourced_from(modules: Iterable[Module]) -> Any:
        return DummySource()

    def should(self, validator: TestRule) -> Implication:
        return Implication(self, validator)

    def __iter__(self):
        return iter(())
