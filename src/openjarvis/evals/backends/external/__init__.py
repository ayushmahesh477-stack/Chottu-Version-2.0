"""External-framework subprocess backends (Hermes Agent, OpenClaw)."""

from Chottu.evals.backends.external.hermes_agent import HermesBackend
from Chottu.evals.backends.external.openclaw import OpenClawBackend

__all__ = ["HermesBackend", "OpenClawBackend"]
