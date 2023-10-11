from dataclasses import dataclass
from pathlib import Path
from typing import TypeAlias, Protocol

PackageName: TypeAlias = str

IN_BASE_ROOT: PackageName = '.'


class BasicModuleProtocol(Protocol):
    name: str
    path: Path
    package_name: PackageName


@dataclass(kw_only=True)
class BasicModule(BasicModuleProtocol):
    name: str
    path: Path
    package_name: PackageName
