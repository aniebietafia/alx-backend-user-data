#!/usr/bin/env python3
"""Hash password, Register user, Credentials validation, Generate UUIDs,
Find user by session ID, Destroy session, Generate reset password token,
Update password"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """Takes in a password string arguments and returns a string
    The returned string is a salted hash of the input password,
    hashed with bcrypt.hashpw"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Takes mandatory email and password string arguments and return a User object"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user
        else:
            raise ValueError('User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """credentials validation, return a boolean"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password=password.encode('utf-8'),
                    hashed_password=user.hashed_password)
