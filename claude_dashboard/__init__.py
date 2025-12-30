"""Claude Code Dashboard and Logging Library."""

__version__ = "0.1.0"

from claude_dashboard.logging import get_logger, log_event, PluginJsonFormatter

__all__ = ["get_logger", "log_event", "PluginJsonFormatter", "__version__"]
