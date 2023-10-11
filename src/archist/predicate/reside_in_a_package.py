from archist.provider.class_node_provider import ClassNode


class ResideInAPackagePredicate:
    parent_package_name: str

    def __init__(self, parent_package_name: str):
        self.parent_package_name = parent_package_name

    def test(self, class_node: ClassNode) -> bool:
        class_package_stack = class_node.module.package_name.split('.')
        test_package_stack = self.parent_package_name.split('.')
        return all(cls_package == test_package
                   for (cls_package, test_package) in
                   zip(class_package_stack, test_package_stack))
