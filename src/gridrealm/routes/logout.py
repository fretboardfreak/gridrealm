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
"""Gridrealm logout route."""

from time import time

from flask import session
from flask import redirect
from flask import url_for

import gridrealm as GR
from gridrealm.database import User
from gridrealm.cookies import clear_cookies
from gridrealm.routes.core import GRView


class Logout(GRView):
    """Log the user out of their session."""

    route = '/logout'
    endpoint = 'logout'

    def get(self):
        """Log the user out of the gridrealm session."""
        # pylint cannot find the logger object on the GR.APP
        # pylint: disable=no-member
        # remove the username from the session if it's there
        username = session.pop('username', None)
        session.clear()
        if username not in ['', None]:
            user = User.query.filter(User.name == username).first()
            msg = "User %s has logged out" % username
            if user:
                now = time()
                play_time = int(now - user.last_login)
                msg += " after %s seconds" % play_time
                user.last_logout = now
                GR.DBS.add(user)
                GR.DBS.commit()
            GR.SYS_MSG.publish(msg)
            GR.APP.logger.debug(msg)

        response = GR.APP.make_response(redirect(url_for('index')))
        clear_cookies(response)
        return response
