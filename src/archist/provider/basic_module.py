import os
from pathlib import Path

from archist.model.basic_module import BasicModule, IN_BASE_ROOT, PackageName


class BasicModuleProvider:
    def provide_from(self, search_path: str | Path) -> list[BasicModule]:
        search_path = Path(search_path)

        found_modules_paths = (
            Path(root, file)
            for root, _, files in os.walk(search_path)
            for file in files
            if file.endswith('.py')
        )

        return [
            BasicModule(
                name=self._get_module_name(module_path),
                path=module_path,
                package_name=self._get_package_name(search_path, module_path)
            )
            for module_path in found_modules_paths
        ]

    def _get_package_name(self, base_path: Path, module_path: Path) -> PackageName:
        relative_module_path = module_path.relative_to(base_path)
        if relative_module_path == module_path.name:
            return IN_BASE_ROOT
        else:
            return PackageName(relative_module_path.parent).replace(os.sep, '.')

    def _get_module_name(self, module_path: Path) -> str:
        return module_path.stem
