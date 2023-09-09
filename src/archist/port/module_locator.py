from pathlib import Path
from typing import Protocol

from archist.model.module_location import ModuleLocation


class ModuleLocatorPort(Protocol):
    def locate_modules(self, base_path: str | Path) -> list[ModuleLocation]:
        ...
