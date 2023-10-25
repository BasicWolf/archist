from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Iterable


class Rule(ABC):
    @abstractmethod
    def validate(self, node) -> ValidationResult:
        ...


@dataclass
class ValidationResult:
    valid: bool
    reasons: Iterable[str] = field(default_factory=tuple)


@dataclass
class ValidResult(ValidationResult):
    valid: bool = True


@dataclass
class InvalidResult(ValidationResult):
    valid: bool = False
