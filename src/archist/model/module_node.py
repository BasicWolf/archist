from dataclasses import dataclass
from typing import List

from archist.model.import_node import ImportNode


@dataclass(kw_only=True)
class ModuleNode:
    import_nodes: List[ImportNode]