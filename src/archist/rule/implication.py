from __future__ import annotations

import typing
from collections.abc import Iterable

from archist.provider.module import Module
from archist.rule.evaluation import EvaluationResult, Ok, Fail
from archist.rule.expectation import ExpectationRule

if typing.TYPE_CHECKING:
    from archist.rule.source.source import Source


class Implication:
    def __init__(self, source: Source, expectation_rule: ExpectationRule):
        self.source = source
        self.expectation_rule = expectation_rule

    def evaluate(self, modules: Iterable[Module]) -> EvaluationResult:
        for node in self.source.sourced_from(modules):
            evaluation_result = self.expectation_rule.evaluate(node)
            match evaluation_result:
                case Ok(): continue
                case Fail(): return evaluation_result
        return Ok()
