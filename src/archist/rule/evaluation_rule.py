from __future__ import annotations

from abc import abstractmethod, ABC
from collections.abc import Iterable


class ExpectationRule(ABC):
    @abstractmethod
    def evaluate(self, node) -> EvaluationResult:
        ...


class EvaluationResult:
    success: bool
    reason: Iterable[str]

    def __init__(self, success: bool, reason: str = ""):
        self.success = success
        self.reason = reason

    def __bool__(self):
        return self.success


class Ok(EvaluationResult):
    def __init__(self):
        super().__init__(True, "")

    def __eq__(self, other):
        return isinstance(other, Ok)

    def __repr__(self):
        return "Ok()"


class Fail(EvaluationResult):
    def __init__(self, reason: str = ""):
        super().__init__(False, reason)

    def __repr__(self):
        return f"Fail(\"{self.reason}\")"
