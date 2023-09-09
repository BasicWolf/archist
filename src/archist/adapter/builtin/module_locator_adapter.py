import os
from pathlib import Path

from archist.model.module_location import ModuleLocation, PackageName, IN_BASE_ROOT
from archist.port.module_locator import ModuleLocatorPort


class ModuleLocatorAdapter(ModuleLocatorPort):
    def locate_modules(self, base_path: str | Path) -> list[ModuleLocation]:
        base_path = Path(base_path)

        found_modules_paths = (
            Path(root, file)
            for root, _, files in os.walk(base_path)
            for file in files
            if file.endswith('.py')
        )

        return [
            ModuleLocation(
                module_path,
                self._get_module_package(base_path, module_path)
            )
            for module_path in found_modules_paths
        ]

    def _get_module_package(self, base_path: Path, module_path: Path):
        relative_module_path = module_path.relative_to(base_path)
        if relative_module_path == module_path.name:
            return IN_BASE_ROOT
        else:
            return PackageName(relative_module_path.parent).replace(os.sep, '.')
