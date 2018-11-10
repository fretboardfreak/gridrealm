"""Gridrealm favicon route."""

import gridrealm as GR
from gridrealm.config import Config
from gridrealm.routes.core import GRView


class Favicon(GRView):
    """Static route for the favicon icon."""

    route = "/favicon.ico"
    endpoint = 'favicon'

    def get(self):
        """Retrieve the static favicon icon."""
        favicon_uri = Config().assets.favicon_uri
        return GR.APP.send_static_file(favicon_uri)
