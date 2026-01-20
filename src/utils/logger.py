"""Structured logging utility"""

import logging
import sys
from typing                                                                          import Optional


def setup_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    """
    Setup structured logger
    
    Args:
        name: Logger name
        level: Log level (DEBUG, INFO, WARNING, ERROR)
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Set level
    log_level = getattr(logging, level.upper() if level else 'INFO')
    logger.setLevel(log_level)
    
    # Create handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(log_level)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)
    
    # Add handler
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger
