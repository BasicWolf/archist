from __future__ import annotations

import ast
from typing import cast, Protocol

from archist.model.module_node import ModuleNode, ModuleNodeBase


class AstProvider:
    def provide_for(self, module_node: ModuleNode):
        with module_node.path.open() as f:
            ast_module = ast.parse(f.read())
            ret = cast(ModuleNodeWithAst, module_node)
            ret.ast = ast_module
            return ret


class ModuleNodeWithAst(ModuleNodeBase, Protocol):
    ast: ast.Module
