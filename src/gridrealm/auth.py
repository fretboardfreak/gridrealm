# Copyright 2019 Curtis Sand <curtissand@gmail.com>,
#                Dennison Gaetz <djgaetz@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Auth Library for the Gridrealm server."""

from http import HTTPStatus

from flask import session
from flask import abort
from flask import g as flask_g

import gridrealm.database as DB

# TODO: do something even better to make sure user is logged in


def _check_login():
    """Perform a basic login checkself.

    If user is logged in set user to flask.g.user.
    """
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
            abort(HTTPStatus.UNAUTHORIZED.value)
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
