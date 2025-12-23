import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger(config: dict):
    """
    Configure application-wide logging.
    Should be called ONCE at app startup.
    """

    log_config = config.get("logging", {})

    log_level = log_config.get("level", "INFO")
    log_file = log_config.get("file", "app.log")
    max_size_mb = log_config.get("max_size_mb", 1)
    backup_count = log_config.get("backup_count", 3)
    log_format = log_config.get(
        "format",
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Ensure logs directory exists
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # Convert MB → bytes
    max_bytes = max_size_mb * 1024 * 1024

    handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count
    )

    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # Prevent duplicate handlers
    if not root_logger.handlers:
        root_logger.addHandler(handler)
