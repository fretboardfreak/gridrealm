"""Gridrealm Static Routes: Use Flask instead of webserver for static files."""

from enum import Enum
from time import time

from flask import render_template
from flask import request
from flask import session
from flask.views import MethodView

import gridrealm as GR
from gridrealm.util import ts_to_str
from gridrealm.config import Config
from gridrealm.database import User


class GRView(MethodView):
    """Base MethodView class for the Gridrealm game."""

    route = None
    endpoint = None

    @classmethod
    def register(cls, app):
        """Register the view on the given flask app."""
        if cls.route is None or cls.endpoint is None:
            raise NotImplementedError(
                'GRView classes must define a route and an endpoint value.')
        if isinstance(cls.route, str):
            app.add_url_rule(cls.route, view_func=cls.as_view(cls.endpoint))
        elif isinstance(cls.route, list):
            view_func = cls.as_view(cls.endpoint)
            for route in cls.route:
                app.add_url_rule(route, view_func=view_func)


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


class Assets(GRView):
    """Static route for game asset files."""

    route = "/_assets/<path:asset>"
    endpoint = "assets"

    def get(self, asset):
        """Retrieve the requested static asset file."""
        fpath = Config().assets.asset_stub % asset
        return GR.APP.send_static_file(fpath)


class Docs(GRView):
    """Static route for documentation pages."""

    route = ['/docs/', '/docs/<path:doc>']
    endpoint = 'docs'

    def get(self, doc=None):
        """Retrieve the static documentation file."""
        if not doc:
            doc = 'index.html'
        fpath = Config().assets.docs_stub % doc
        return GR.APP.send_static_file(fpath)


class Favicon(GRView):
    """Static route for the favicon icon."""

    route = "/favicon.ico"
    endpoint = 'favicon'

    def get(self):
        """Retrieve the static favicon icon."""
        favicon_uri = Config().assets.favicon_uri
        return GR.APP.send_static_file(favicon_uri)


class SysMsg(GRView):
    """Endpoint for broadcasting system messages to all clients."""

    route = '/sysmsg'
    endpoint = 'sysmsg'

    def get(self):
        """Return the EventSource for the System Message channel."""
        return GR.SYS_MSG.subscribe()


class Views(Enum):
    """Enum of all the non-API View classes for gridrealm."""

    index = Index
    logout = Logout
    assets = Assets
    docs = Docs
    favicon = Favicon
    sysmsg = SysMsg


def register_static_views(app):
    """Register the static views with the flask app."""
    for view in Views:
        view.value.register(app)
