from __future__ import annotations

from abc import ABC, abstractmethod

from archist.rule.evaluation import EvaluationResult


class ExpectationRule(ABC):
    @abstractmethod
    def evaluate(self, node) -> EvaluationResult:
        ...
