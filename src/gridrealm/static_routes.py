"""Gridrealm Static Routes: Use Flask instead of webserver for static files."""

from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

import gridrealm as GR
from gridrealm.config import Config


def index():
    """Static route for gridrealm client."""
    # pylint cannot find the logger object on the GR.APP
    # pylint: disable=no-member
    if request.method == 'POST':
        session['username'] = request.form['username']
        # TODO: do something to make sure user is logged in
    if 'username' in session:
        uname = session['username']
        GR.APP.logger.debug('User %s logged in.' % uname)
        response = GR.APP.make_response(
            render_template(Config().assets.client_uri))
        response.set_cookie('username', uname)
        GR.SYS_MSG.publish('New login by %s' % uname)
    else:
        GR.APP.logger.debug('New user at landing page.')
        response = GR.APP.make_response(
            render_template(Config().assets.landing_uri))
    return response


def logout():
    """Log the user out of their session."""
    # remove the username from the session if it's there
    session.pop('username', None)
    response = GR.APP.make_response(redirect(url_for('index')))
    # invalidate the username cookie
    response.set_cookie('username', '')
    return response


def assets(asset):
    """Static route for game asset files."""
    fpath = Config().assets.asset_stub % asset
    return GR.APP.send_static_file(fpath)


def docs(doc=None):
    """Static route for documentation pages."""
    if not doc:
        doc = 'index.html'
    fpath = Config().assets.docs_stub % doc
    return GR.APP.send_static_file(fpath)


def favicon():
    """Static route for the favicon icon."""
    favicon_uri = Config().assets.favicon_uri
    return GR.APP.send_static_file(favicon_uri)


def sysmsg():
    """Endpoint for broadcasting system messages to client."""
    return GR.SYS_MSG.subscribe()


STATIC_VIEWS = [
    (('/', 'index', index), {'methods': ['GET', 'POST']}),
    (('/_assets/<path:asset>', 'assets', assets), {}),
    (('/docs/', 'docs', docs), {}),
    (('/docs/<path:doc>', 'docs', docs), {}),
    (('/favicon.ico', 'favicon', favicon), {}),
    (('/logout', 'logout', logout), {}),
    (('/sysmsg', 'sysmsg', sysmsg), {})
]


def register_static_views(app):
    """Register the static views with the flask app."""
    for view_opts, view_args in STATIC_VIEWS:
        app.add_url_rule(*view_opts, **view_args)
