#!/usr/bin/env python3

"""
This module provides the function `hash_password`
"""

import bcrypt


def hash_password(string: str) -> str:
    """
    This function takes in a string argument
    and returns a salted, hashed password
    """
    salt = bcrypt.gensalt()
    string_bytes = string.encode('utf-8')
    return bcrypt.hashpw(string_bytes, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    This function validate that the provided
    password matches the hashed password
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
