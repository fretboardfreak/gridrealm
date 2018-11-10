"""Gridrealm logout route."""

from time import time

from flask import render_template
from flask import session

import gridrealm as GR
from gridrealm.config import Config
from gridrealm.database import User
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
        response = GR.APP.make_response(
            render_template(Config().assets.landing_uri))
        # invalidate the session cookies
        response.set_cookie('username', '', expires=0)
        response.set_cookie('last_login', '', expires=0)
        response.set_cookie('xcoord', '', expires=0)
        response.set_cookie('ycoord', '', expires=0)
        response.set_cookie('zcoord', '', expires=0)

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
        return response
