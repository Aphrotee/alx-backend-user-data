#!/usr/bin/env python3
""" Module for login feature
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from os import getenv
from models.user import User


@app_views.route('/auth_session/login',
                 methods=['POST'], strict_slashes=False)
def login():
    """
    Logs-in a user based on a session created for such user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or not len(email):
        return jsonify({'error': 'email missing'}), 400
    if password is None or not len(password):
        return jsonify({'error': 'password missing'}), 400
    users = User.search({'email': email})
    if users is None or not len(users):
        return jsonify({'error': 'no user found for this email'}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME', '_my_session_id'),
                                session_id)
            return response
    return jsonify({'error': 'wrong password'}), 401