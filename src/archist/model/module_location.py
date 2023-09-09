from dataclasses import dataclass
from pathlib import Path
from typing import TypeAlias

PackageName: TypeAlias = str

IN_BASE_ROOT: PackageName = '.'


@dataclass
class ModuleLocation:
    path: Path
    package: PackageName
