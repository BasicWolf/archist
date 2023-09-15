from __future__ import annotations

import ast
from typing import Protocol

from archist.model.module_node import ModuleNode


class AstProviderPort(Protocol):
    def process(self, module_node: ModuleNode) -> ModuleNodeWithAst:
        ...


class ModuleNodeWithAst(Protocol):
    ast: ast.Module
