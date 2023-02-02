#!/usr/bin/env python3

"""
This module provides the `filter_datum` function
"""

import logging
import re
from typing import List

PII_FIELDS = (
    'email',
    'phone',
    'ssn',
    'password',
    'ip'
)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    This is a function that returns
    a log message obfuscated
    """
    for field in fields:
        message = re.sub(fr'{field}=[^{separator}]*',
                         f'{field}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """ Initialize instance """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """
        This method filter values in incoming
        log records using `filter_datum`
        """
        msg = super(RedactingFormatter, self).format(record)
        filtered = filter_datum(self.fields, self.REDACTION,
                                msg, self.SEPARATOR)
        return filtered


def get_logger() -> logging.Logger:
    """ Returns a `logging.Logger` object """
    logger = logging.getLogger('user_data')
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
