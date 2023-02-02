#!/usr/bin/env python3

"""
This module provides the `filter_datum` function
"""

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
                         '{}={}{}'.format(field, redaction, separator),
                         message)
    return message
