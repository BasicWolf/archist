from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import cast, Protocol

from archist.model.basic_module import BasicModuleProtocol
from archist.provider.ast import ModuleWithAst


class ClassNodeProvider:
    def provide_for(self, module: ModuleWithAst) -> ModuleWithClassNodes:
        ast_classdef_statements = [
            statement
            for statement in module.ast.body
            if isinstance(statement, ast.ClassDef)
        ]

        ret = cast(ModuleWithClassNodes, module)
        ret.class_nodes = [
            ClassNode(
                module=module,
                name=classdef.name
            )
            for classdef in ast_classdef_statements
        ]
        return ret


class ModuleWithClassNodes(BasicModuleProtocol, Protocol):
    class_nodes: list[ClassNode]


@dataclass(kw_only=True)
class ClassNode:
    name: str
    module: ModuleWithAst
