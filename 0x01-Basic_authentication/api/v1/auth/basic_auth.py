#!/usr/bin/env python3

"""
This module provides the class BasicAuth
"""

from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """
    A class `BasicAuth` for all Basic
    authentication operations
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        This method extracts the authentication
        credentials from the Authorization header
        """
        if authorization_header is None:
            return
        if not isinstance(authorization_header, str):
            return
        if not bool(re.match(r'^Basic \w*', authorization_header)):
            return
        return authorization_header[6:]
