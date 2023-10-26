from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Any

from archist.provider.module_provider import Module
from archist.rule.implication import Implication
from archist.rule.validation.validator import Validator


class Source(Iterable, ABC):
    @staticmethod
    @abstractmethod
    def sourced_from(modules: Iterable[Module]) -> Any:
        ...

    @abstractmethod
    def should(self, validator: Validator) -> Implication:
        ...
