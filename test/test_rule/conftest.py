from typing import Iterable, Any

import pytest

from archist.provider.module_provider import Module
from archist.rule.implication import Implication
from archist.rule.source.source import Source
from archist.rule.validator.validator import Validator


@pytest.fixture
def dummy_source():
    return DummySource()


@pytest.fixture
def dummy_validator():
    return DummyValidator


class DummyValidator(Validator):
    def validate(self, node) -> bool:
        return True


class DummySource(Source):
    @staticmethod
    def sourced_from(modules: Iterable[Module]) -> Any:
        return DummySource()

    def should(self, validator: Validator) -> Implication:
        return Implication(self, validator)

    def __iter__(self):
        return iter(())
