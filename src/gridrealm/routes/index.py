"""Gridrealm index route."""

from time import time

from flask import render_template
from flask import request
from flask import session

import gridrealm as GR
from gridrealm.util import ts_to_str
from gridrealm.config import Config
from gridrealm.database import User
from gridrealm.routes.core import GRView


class Index(GRView):
    """Top Level Client Index route for gridrealm client."""

    route = '/'
    endpoint = 'index'

    def form_index_response(self):
        """Get the client index, either landing page or the client itself."""
        # pylint cannot find the logger object on the GR.APP
        # pylint: disable=no-member
        if request.method == 'POST' and request.form['username'] != "":
            # TODO: do something better to let the user log in
            session['username'] = request.form['username']
        # TODO: do something to make sure user is logged in
        if 'username' in session:
            template = Config().assets.client_uri
            if Config().gridrealm.debug:
                template = Config().assets.debug_client_uri
            response = GR.APP.make_response(
                render_template(template))
            uname = session['username']
            # see if username is in database
            user = User.query.filter(User.name == uname).first()
            if user is None:  # username is not in database
                # new users have now as their last login
                msg = 'New player named %s' % uname
                GR.SYS_MSG.publish(msg)
                GR.APP.logger.debug(msg)
                user = User(uname, time())
            else:
                msg = '%s is back. last logout was at %s' % (
                    user.name, ts_to_str(user.last_logout))
                GR.SYS_MSG.publish(msg)
                GR.APP.logger.debug(msg)
            old_last_login = user.last_login
            user.last_login = time()
            # add new user or update existing user in the database
            GR.DBS.add(user)
            GR.DBS.commit()

            response.set_cookie('username', uname)
            response.set_cookie('last_login', ts_to_str(old_last_login))
            response.set_cookie('xcoord', str(user.xcoord))
            response.set_cookie('ycoord', str(user.ycoord))
            response.set_cookie('zcoord', str(user.zcoord))
        else:
            GR.APP.logger.debug('New user at landing page.')
            response = GR.APP.make_response(
                render_template(Config().assets.landing_uri))
            response.set_cookie('username', '', expires=0)
            response.set_cookie('last_login', '', expires=0)
            response.set_cookie('xcoord', '', expires=0)
            response.set_cookie('ycoord', '', expires=0)
            response.set_cookie('zcoord', '', expires=0)
        return response

    def get(self):
        """Perform a GET request for the index context."""
        return self.form_index_response()

    def post(self):
        """Perform a POST request for the index context."""
        return self.form_index_response()
