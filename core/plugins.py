"""Simple plugin system for trynix."""

from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import List


PLUGINS_DIR = Path("plugins")


class Plugin:
    """Base class for plugins."""

    def register(self, app) -> None:  # pragma: no cover - interface method
        """Hook to extend the application."""
        raise NotImplementedError


def load_plugins(app, plugins_dir: Path | str = PLUGINS_DIR) -> List[Plugin]:
    """Import all plugin modules and call their register() functions."""

    plugins: List[Plugin] = []
    plugins_path = Path(plugins_dir)
    if not plugins_path.exists():
        return plugins

    for file in plugins_path.glob("*.py"):
        if file.name.startswith("_"):
            continue
        module_name = f"plugins.{file.stem}"
        module = import_module(module_name)
        plugin_cls = getattr(module, "Plugin", None)
        if plugin_cls is None:
            continue
        plugin: Plugin = plugin_cls()
        try:
            plugin.register(app)
            plugins.append(plugin)
        except Exception as exc:  # pragma: no cover - best effort loading
            print(f"Failed to load plugin {module_name}: {exc}")

    return plugins
