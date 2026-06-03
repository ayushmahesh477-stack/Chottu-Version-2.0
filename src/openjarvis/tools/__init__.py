"""Tools primitive — tool system with ABC interface and built-in tools."""

from __future__ import annotations

from Chottu.tools._stubs import BaseTool, ToolExecutor, ToolSpec

# Import built-in tools to trigger @ToolRegistry.register() decorators.
# Each is wrapped in try/except so the package loads even before the
# individual tool modules are created.
try:
    import Chottu.tools.calculator  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.think  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.retrieval  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.llm_tool  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.file_read  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.web_search  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.code_interpreter  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.code_interpreter_docker  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.repl  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.storage_tools  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.mcp_adapter  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.channel_tools  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.http_request  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.docker_shell_exec  # noqa: F401
    import Chottu.tools.shell_exec  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.memory_manage  # noqa: F401
except ImportError:
    pass
try:
    import Chottu.tools.user_profile_manage  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.skill_manage  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.file_write  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.apply_patch  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.git_tool  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.db_query  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.pdf_tool  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.image_tool  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.audio_tool  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.knowledge_tools  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.text_to_speech  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.tools.digest_collect  # noqa: F401
except ImportError:
    pass

__all__ = ["BaseTool", "ToolExecutor", "ToolSpec"]
