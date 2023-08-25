from archist.model.import_node import ImportNode
from src.archist.module_scanner import ModuleScanner


def test_import_single_module(module_with_one_import_path):
    assert ModuleScanner().scan_module(module_with_one_import_path).import_nodes == [ImportNode('math')]
