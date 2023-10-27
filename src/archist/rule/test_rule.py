from __future__ import annotations

from abc import abstractmethod, ABC
from collections.abc import Iterable


class ExpectationRule(ABC):
    @abstractmethod
    def test(self, node) -> ExpectationRuleResult:
        ...


class ExpectationRuleResult:
    success: bool
    reasons: Iterable[str]

    def __init__(self, success: bool, reasons: Iterable[str] = ()):
        self.success = success
        self.reasons = reasons


class Ok(ExpectationRuleResult):
    def __init__(self, reasons: Iterable[str] = ()):
        super().__init__(True, reasons)


class Fail(ExpectationRuleResult):
    def __init__(self, reasons: Iterable[str] = ()):
        super().__init__(False, reasons)
