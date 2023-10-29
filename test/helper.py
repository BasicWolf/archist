from collections.abc import Iterable
from typing import Protocol


class ItemWithName(Protocol):
    name: str


def extracting_names_from(items: Iterable[ItemWithName]) -> list[str]:
    return [item.name for item in items]
