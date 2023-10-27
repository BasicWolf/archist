from __future__ import annotations

import typing
from collections.abc import Iterable

from archist.provider.module_provider import Module
from archist.rule.test_rule import ExpectationRule

if typing.TYPE_CHECKING:
    from archist.rule.source.source import Source


class Implication:
    def __init__(self, source: Source, validator: ExpectationRule):
        self.source = source
        self.validator = validator

    def evaluate(self, modules: Iterable[Module]) -> bool:
        return all(
            self.validator.test(node)
            for node in self.source.sourced_from(modules)
        )
