"""Gridrealm assets route."""

import gridrealm as GR
from gridrealm.config import Config
from gridrealm.routes.core import GRView


class Assets(GRView):
    """Static route for game asset files."""

    route = "/_assets/<path:asset>"
    endpoint = "assets"

    def get(self, asset):
        """Retrieve the requested static asset file."""
        fpath = Config().assets.asset_stub % asset
        return GR.APP.send_static_file(fpath)
