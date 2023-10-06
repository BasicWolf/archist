from __future__ import annotations

import ast
from typing import cast

from archist.model.module_node import ModuleNode


class AstProvider:
    def provide_from(self, module_node: ModuleNode) -> ModuleNodeWithAst:
        with module_node.path.open() as f:
            ast_module = ast.parse(f.read())
            ret = cast(ModuleNodeWithAst, module_node)
            ret.ast = ast_module
            return ret


class ModuleNodeWithAst(ModuleNode):
    ast: ast.Module
