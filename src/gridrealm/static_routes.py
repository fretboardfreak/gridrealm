"""Gridrealm Static Routes: Use Flask instead of webserver for static files."""

from flask import render_template

import gridrealm as GR
from gridrealm.config import Config


def index():
    """Static route for gridrealm client."""
    return render_template(Config().assets.client_uri)


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
    ('/', 'index', index),
    ('/_assets/<path:asset>', 'assets', assets),
    ('/docs/', 'docs', docs),
    ('/docs/<path:doc>', 'docs', docs),
    ('/favicon.ico', 'favicon', favicon)
]


def register_static_views(app):
    """Register the static views with the flask app."""
    for view in STATIC_VIEWS:
        app.add_url_rule(*view)
