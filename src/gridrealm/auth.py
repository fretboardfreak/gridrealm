"""Auth Library for the Gridrealm server."""

from flask import session
from flask import abort
from flask import g as flask_g

import gridrealm.database as DB


def user_required(view_func):
    """Check whether user is logged in or raises error 401."""
    # TODO: do something even better to make sure user is logged in
    def decorator(*args, **kwargs):
        """Wrap a view function with a check for user authorization."""
        # check username is in the session cookie
        if 'username' not in session:
            abort(401)
        flask_g.user = DB.User.query.filter(
            DB.User.name == session['username'])
        if flask_g.user is None:
            abort(401)
        return view_func(*args, **kwargs)
    return decorator
