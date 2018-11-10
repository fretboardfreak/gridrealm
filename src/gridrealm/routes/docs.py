"""Gridrealm docs route."""

import gridrealm as GR
from gridrealm.config import Config
from gridrealm.routes.core import GRView


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
