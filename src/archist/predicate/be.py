from typing import TypeVar, Generic, Callable

from archist.predicate.predicate import Predicate

T = TypeVar('T')
TestFunctionType = Callable[[T], bool]


class BePredicate(Predicate, Generic[T]):
    test_function: TestFunctionType

    def __init__(self, test_function: TestFunctionType):
        self.test_function = test_function

    def test(self, node: T) -> bool:
        return self.test_function(node)
