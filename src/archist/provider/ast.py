from __future__ import annotations

import ast
from typing import cast, Protocol

from archist.model.basic_module import BasicModule, BasicModuleProtocol


class AstProvider:
    def provide_for(self, basic_module: BasicModule):
        with basic_module.path.open() as f:
            ast_module = ast.parse(f.read())
            ret = cast(ModuleWithAst, basic_module)
            ret.ast = ast_module
            return ret


class ModuleWithAst(BasicModuleProtocol, Protocol):
    ast: ast.Module
