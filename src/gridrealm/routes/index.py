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
"""Gridrealm index route."""

from time import time

from flask import render_template
from flask import request
from flask import session
from flask import g as flask_g

import gridrealm as GR
import gridrealm.database as DB
from gridrealm.util import ts_to_str
from gridrealm.config import Config
from gridrealm.database import User
from gridrealm.auth import is_user_logged_in
from gridrealm.routes.core import GRView
from gridrealm.cookies import clear_cookies
from gridrealm.cookies import set_cookies


def get_client_template():
    """Choose a client template based on the debug setting state."""
    template = Config().assets.client_uri
    if Config().gridrealm.debug:
        template = Config().assets.debug_client_uri
    return template


class Index(GRView):
    """Top Level Client Index route for gridrealm client."""

    route = '/'
    endpoint = 'index'

    def get(self):
        """Perform a GET request for the index context."""
        # pylint cannot find the logger on the APP
        # pylint: disable=no-member
        if flask_g.user is not None:  # User is logged in
            GR.APP.logger.debug('User is logged in: %s' % flask_g.user.name)
            response = GR.APP.make_response(render_template(
                get_client_template()))
        else:  # No user is logged in
            GR.APP.logger.debug('No user is logged in.')
            response = GR.APP.make_response(render_template(
                Config().assets.landing_uri))
            clear_cookies(response)
        return response

    get = is_user_logged_in(get)

    def post(self):
        """Perform a POST request for the index context."""
        # pylint cannot find the logger on the APP
        # pylint: disable=no-member
        if 'username' in request.form and request.form['username'] != "":
            # TODO: do something better to let the user log in
            session['username'] = request.form['username']
            response = GR.APP.make_response(render_template(
                get_client_template()))
        else:  # misformed/missing form data, return back the landing page
            response = GR.APP.make_response(render_template(
                Config().assets.landing_uri))
            # clear cookies in case they haven't been cleared at this point
            clear_cookies(response)
            return response

        # query database for user, since username was not in session before
        flask_g.user = DB.User.query.filter(
            DB.User.name == session['username']).first()
        if flask_g.user is not None:  # User has logged back in
            msg = '%s is back. last logout was at %s' % (
                flask_g.user.name, ts_to_str(flask_g.user.last_logout))
            GR.SYS_MSG.publish(msg)
            GR.APP.logger.debug(msg)
        else:  # New user is being created
            uname = session['username']
            msg = 'New player named %s' % uname
            GR.SYS_MSG.publish(msg)
            GR.APP.logger.debug(msg)
            flask_g.user = User(uname, time())

        # update user's last login time to now
        old_last_login = flask_g.user.last_login
        flask_g.user.last_login = time()

        # add new user or update existing user in the database
        GR.DBS.add(flask_g.user)
        GR.DBS.commit()

        set_cookies(response=response,
                    username=str(flask_g.user.name),
                    last_login=ts_to_str(old_last_login))

        return response

    post = is_user_logged_in(post)
