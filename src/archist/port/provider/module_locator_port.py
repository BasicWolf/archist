from abc import ABC, abstractmethod
from pathlib import Path

from archist.model.module_node import ModuleNode


class ModuleLocatorPort(ABC):
    @abstractmethod
    def locate_modules(self, search_path: str | Path) -> list[ModuleNode]:
        ...
