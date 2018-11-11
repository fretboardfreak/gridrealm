"""Auth Library for the Gridrealm server."""

from flask import session
from flask import abort
from flask import g as flask_g

import gridrealm as GR
import gridrealm.database as DB

# TODO: do something even better to make sure user is logged in


def _check_login():
    """Perform a basic login checkself.

    If user is logged in set user to flask.g.user.
    """
    # pylint: disable=no-member
    flask_g.user = None
    if 'username' in session:
        flask_g.user = DB.User.query.filter(
            DB.User.name == session['username']).first()


def user_required(view_func):
    """Check whether user is logged in or raises error 401.

    If the user is logged in the User object from the database is saved to
    flask.g.user.
    """
    def decorator(*args, **kwargs):
        """Wrap a view function with a check for user authorization."""
        _check_login()
        if flask_g.user is None:
            abort(401)
        return view_func(*args, **kwargs)
    return decorator


def is_user_logged_in(view_func):
    """Check whether user is logged in, without throwing an errorself.

    Used to determine if a user is logged in or if a logged out view of the
    route should be provided. If the user is logged in the User object from the
    database is saved to flask.g.user. If the user is not logged in the
    flask.g.user value will be set to None.
    """
    def decorator(*args, **kwargs):
        """Wrap a view function with a check for user authorization."""
        _check_login()
        return view_func(*args, **kwargs)
    return decorator
