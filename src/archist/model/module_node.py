from dataclasses import dataclass
from pathlib import Path
from typing import TypeAlias, Protocol

PackageName: TypeAlias = str

IN_BASE_ROOT: PackageName = '.'


class ModuleNodeBase(Protocol):
    name: str
    path: Path
    package_name: PackageName


@dataclass(kw_only=True)
class ModuleNode(ModuleNodeBase):
    name: str
    path: Path
    package_name: PackageName
