from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import cast, Protocol

from archist.model.module_node import ModuleNodeBase
from archist.provider.ast_provider import ModuleNodeWithAst


class ClassNodeProvider:
    def provide_for(self, module_node: ModuleNodeWithAst) -> ModuleWithClassNodes:
        ast_classdef_statements = [
            statement
            for statement in module_node.ast.body
            if isinstance(statement, ast.ClassDef)
        ]

        ret = cast(ModuleWithClassNodes, module_node)
        ret.class_nodes = [
            ClassNode(
                module_node=module_node,
                name=classdef.name
            )
            for classdef in ast_classdef_statements
        ]
        return ret


class ModuleWithClassNodes(ModuleNodeBase, Protocol):
    class_nodes: list[ClassNode]


@dataclass(kw_only=True)
class ClassNode:
    name: str
    module_node: ModuleNodeWithAst
