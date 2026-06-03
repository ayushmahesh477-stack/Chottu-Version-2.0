"""Smoke test that the tmp_Chottu_home fixture works."""

from __future__ import annotations

from pathlib import Path

from Chottu.core import config as config_mod


def test_fixture_redirects_default_config_dir(tmp_Chottu_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_DIR == tmp_Chottu_home
    assert tmp_Chottu_home.exists()
    assert (tmp_Chottu_home / ".state").exists()
    assert (tmp_Chottu_home / ".state" / "models").exists()


def test_fixture_redirects_config_path(tmp_Chottu_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_PATH == tmp_Chottu_home / "config.toml"
