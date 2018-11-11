"""Gridrealm cookies library."""

from enum import Enum
from enum import auto


class Cookies(Enum):
    """An Enum of cookies used in the gridrealm client."""

    username = auto()
    last_login = auto()


def clear_cookies(response):
    """Clear out all gridrealm client cookies in the response."""
    for cookie in Cookies:
        response.set_cookie(cookie.name, '', expires=0)


def set_cookies(response, username=None, last_login=None):
    """Set the gridrealm client cookies on the response."""
    if username:
        response.set_cookie(Cookies.username.name, username)
    if last_login:
        response.set_cookie(Cookies.last_login.name, last_login)
