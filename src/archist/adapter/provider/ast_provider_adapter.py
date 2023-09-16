import ast
from typing import cast

from archist.model.module_node import ModuleNode
from archist.port.provider.ast_provider_port import AstProviderPort, ModuleNodeWithAst


class AstProviderAdapter(AstProviderPort):
    def process(self, module_node: ModuleNode) -> ModuleNodeWithAst:
        with module_node.path.open() as f:
            ast_module = ast.parse(f.read())
            ret = cast(ModuleNodeWithAst, module_node)
            ret.ast = ast_module
            return ret


