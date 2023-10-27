from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Any

from archist.provider.module_provider import Module
from archist.rule.evaluation_rule import ExpectationRule
from archist.rule.implication import Implication


class Source(Iterable, ABC):
    @abstractmethod
    def sourced_from(self, modules: Iterable[Module]) -> Any:
        ...

    @abstractmethod
    def should(self, validator: ExpectationRule) -> Implication:
        ...
