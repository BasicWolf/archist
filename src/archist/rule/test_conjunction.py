from archist.provider.module_provider import ProvidedModuleNode
from archist.rule.filter_rule import FilterRule
from archist.rule.test_rule import TestRule


class TestConjunction(TestRule):
    first_rule: TestRule
    second_rule: TestRule
    filter_rule: FilterRule

    def __init__(self, first_rule, second_rule, filter_rule: FilterRule):
        self.filter_rule = filter_rule
        self.first_rule = first_rule
        self.second_rule = second_rule

    def test(self, node) -> bool:
        return self.first_rule.test(node) and self.second_rule.test(node)

    def check(self, module_nodes: list[ProvidedModuleNode]):
        filtered_nodes = self.filter_rule.filter(module_nodes)
        return all(self.test(mn) for mn in filtered_nodes)
