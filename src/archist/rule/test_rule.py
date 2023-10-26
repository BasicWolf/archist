from __future__ import annotations

from abc import abstractmethod, ABC
from collections.abc import Iterable


class TestRule(ABC):
    @abstractmethod
    def test(self, node) -> TestResult:
        ...


class TestResult:
    success: bool
    reasons: Iterable[str]

    def __init__(self, success: bool, reasons: Iterable[str] = ()):
        self.success = success
        self.reasons = reasons


class Ok(TestResult):
    def __init__(self, reasons: Iterable[str] = ()):
        super().__init__(True, reasons)


class Fail(TestResult):
    def __init__(self, reasons: Iterable[str] = ()):
        super().__init__(False, reasons)
