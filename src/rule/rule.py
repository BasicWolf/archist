from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


class Rule:
    def validate(self) -> ValidationResult:
        return ValidResult()


@dataclass
class ValidationResult:
    valid: bool
    reasons: Iterable[str] = field(default_factory=tuple)


@dataclass
class ValidResult(ValidationResult):
    valid: bool = True
