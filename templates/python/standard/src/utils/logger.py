import logging
import sys
import os
from typing import Literal, Optional, Union

COLORS = {
    "RESET": "\033[0m",
    "DEBUG": "\033[94m",
    "INFO": "\033[92m",
    "WARNING": "\033[93m",
    "ERROR": "\033[05m",
    "CRITICAL": "\033[95m",
    "BOLD": "\033[1m",
    "DIM": "\033[2m",
    "UNDERLINE": "\033[4m"
}

class ColoredFormatter(logging.Formatter):
    """
    Custom formatter to add ANSI escape codes for colored log output.
    """
    def __init__(self, fmt: str, datefmt: Optional[str] = None, style: Literal['%'] = '%', log_colors: bool = True):
        super().__init__(fmt, datefmt, style)
        self.log_colors = log_colors

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)

        if self.log_colors:
            levelname = record.levelname
            color = COLORS.get(levelname, COLORS["RESET"])
            return f"{color}{message}{COLORS['RESET']}"
        else:
            return message

class LevelFilter(logging.Filter):
    """
    Filter to direct specific log levels to different handlers.
    """
    def __init__(self, min_level: Optional[int] = None, max_level: Optional[int] = None):
        super().__init__()
        self.min_level = min_level
        self.max_level = max_level

    def filter(self, record: logging.LogRecord) -> bool:
        if self.min_level is not None and record.levelno < self.min_level:
            return False
        if self.max_level is not None and record.levelno > self.max_level:
            return False
        return True

_configured_loggers = set()

def setup_logger(
        name: str = "logger",
        level: int = logging.INFO,
        log_format: str = '%(asctime)s.%(msecs)03d | %(levelname)-8s | %(name)-2s | %(message)s',
        date_format: str = '%Y-%m-%d %H:%M:%S',
        log_colors: bool = True,
        use_stderr: bool = True
) -> logging.Logger:
    logger = logging.getLogger(name)
    if name in _configured_loggers:
        return logger
    logger.setLevel(level)
    logger.propagate = False
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        handler.close()
    formatter: Union[ColoredFormatter, logging.Formatter]
    if log_colors:
        formatter = ColoredFormatter(log_format, datefmt=date_format, log_colors=True)
    else:
        formatter = logging.Formatter(log_format, datefmt=date_format)
    if use_stderr:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.addFilter(LevelFilter(max_level=logging.WARNING))
        stdout_handler.setLevel(level)
        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)

        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setLevel(logging.ERROR)
        stderr_handler.setFormatter(formatter)
        logger.addHandler(stderr_handler)
    else:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    _configured_loggers.add(name)
    return logger

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)