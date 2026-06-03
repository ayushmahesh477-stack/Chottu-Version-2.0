"""Data source connectors for Deep Research."""

from Chottu.connectors._stubs import (
    Attachment,
    BaseConnector,
    Document,
    SyncStatus,
)
from Chottu.connectors.store import KnowledgeStore

__all__ = ["Attachment", "BaseConnector", "Document", "KnowledgeStore", "SyncStatus"]

# Auto-register built-in connectors
import Chottu.connectors.obsidian  # noqa: F401

try:
    import Chottu.connectors.gmail  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.gmail_imap  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.gdrive  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import Chottu.connectors.notion  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.granola  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.gcontacts  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.imessage  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.apple_notes  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.apple_music  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.apple_contacts  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.slack_connector  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.outlook  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.gcalendar  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.dropbox  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import Chottu.connectors.whatsapp  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.oura  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.apple_health  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.strava  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.spotify  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.google_tasks  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.weather  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.github_notifications  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.hackernews  # noqa: F401
except ImportError:
    pass

try:
    import Chottu.connectors.news_rss  # noqa: F401
except ImportError:
    pass
