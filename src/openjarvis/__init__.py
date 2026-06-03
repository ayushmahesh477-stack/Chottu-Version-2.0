"""Chottu — modular AI assistant backend with composable intelligence primitives."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

from Chottu.sdk import Chottu, ChottuSystem, MemoryHandle, SystemBuilder

try:
    __version__ = _pkg_version("Chottu")
except PackageNotFoundError:  # pragma: no cover — uninstalled source tree
    __version__ = "0.0.0+unknown"

__all__ = ["Chottu", "ChottuSystem", "MemoryHandle", "SystemBuilder", "__version__"]
