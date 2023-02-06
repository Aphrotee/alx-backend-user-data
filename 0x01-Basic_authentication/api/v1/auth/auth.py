#!/usr/bin/env python3

"""
This module provides the class Auth
"""

from flask import request
from typing import (
        List,
        TypeVar
    )


class Auth:
    """ Auth class for authentication operations """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if a resource defined by
        `path` needs authentication
        """
        if path is None or excluded_paths is None:
            return True
        if path[len(path) - 1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets and returns the authorization header of the request
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets and returns the current user object"""
        return None
