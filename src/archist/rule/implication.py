from __future__ import annotations

import typing

from .be_test_rule import BeTestRule
from .filter_rule import FilterRule
from .test_conjunction import TestConjunction
from .test_rule import TestRule
from ..predicate.be import TestFunctionType

if typing.TYPE_CHECKING:
    pass


class Implication(TestRule):
    def __init__(self, filter_rule: FilterRule):
        self.filter_rule = filter_rule

    def be(self, test_function: TestFunctionType) -> TestConjunction:
        return TestConjunction(self, BeTestRule(test_function), self.filter_rule)

    def test(self, node) -> bool:
        return True
