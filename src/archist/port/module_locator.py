from pathlib import Path
from typing import Protocol

from archist.model.module_node import ModuleNode


class ModuleLocatorPort(Protocol):
    def locate_modules(self, base_path: str | Path) -> list[ModuleNode]:
        ...
