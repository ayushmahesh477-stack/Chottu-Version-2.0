"""Tests for speech configuration."""

from Chottu.core.config import ChottuConfig, SpeechConfig


def test_speech_config_defaults():
    cfg = SpeechConfig()
    assert cfg.backend == "auto"
    assert cfg.model == "base"
    assert cfg.language == ""
    assert cfg.device == "auto"
    assert cfg.compute_type == "float16"


def test_Chottu_config_has_speech():
    cfg = ChottuConfig()
    assert hasattr(cfg, "speech")
    assert isinstance(cfg.speech, SpeechConfig)
    assert cfg.speech.backend == "auto"


def test_Chottu_system_has_speech_backend():
    """ChottuSystem has a speech_backend attribute."""
    from Chottu.system import ChottuSystem

    assert "speech_backend" in ChottuSystem.__dataclass_fields__
