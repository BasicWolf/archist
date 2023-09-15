from dataclasses import dataclass
from pathlib import Path
from typing import TypeAlias

PackageName: TypeAlias = str

IN_BASE_ROOT: PackageName = '.'


@dataclass(kw_only=True)
class ModuleNode:
    path: Path
    package_name: PackageName
