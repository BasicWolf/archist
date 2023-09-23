from __future__ import annotations

import ast
from abc import ABC, abstractmethod

from archist.model.module_node import ModuleNode


class AstProviderPort(ABC):
    @abstractmethod
    def process(self, module_node: ModuleNode) -> ModuleNodeWithAst:
        ...


class ModuleNodeWithAst(ModuleNode):
    ast: ast.Module
