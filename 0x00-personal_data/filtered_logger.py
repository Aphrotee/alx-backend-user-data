#!/usr/bin/env python3

"""
This module provides the `filter_datum` function
"""

import logging
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    This is a function that returns
    a log message obfuscated
    """
    for field in fields:
        message = re.sub(fr'{field}=[a-zA-Z0-9\W^{separator}]*{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, field: List[str]) -> None:
        """ Initialize instance """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.field = field

    def format(self, record: logging.LogRecord) -> str:
        """
        This method filter values in incoming
        log records using `filter_datum`
        """
        return filter_datum(self.field, '***',
                            record.getMessage(), ';')
