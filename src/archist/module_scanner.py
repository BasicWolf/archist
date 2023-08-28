import ast
from pathlib import Path

from archist.model.import_node import ImportNode
from archist.model.module_node import ModuleNode


class ModuleScanner:
    def scan_module(self, path: Path):
        with path.open() as f:
            ast_body = ast.parse(f.read()).body

        ast_import_statements = [
            statement
            for statement in ast_body
            if isinstance(statement, (ast.Import, ast.ImportFrom))
        ]

        import_nodes = [
            ImportNode(import_name.name)
            for ast_import_node in ast_import_statements
            for import_name in ast_import_node.names
        ]

        return ModuleNode(import_nodes=import_nodes)