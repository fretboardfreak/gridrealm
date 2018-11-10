"""Gridrealm sysmsg route."""

import gridrealm as GR
from gridrealm.routes.core import GRView


class SysMsg(GRView):
    """Endpoint for broadcasting system messages to all clients."""

    route = '/sysmsg'
    endpoint = 'sysmsg'

    def get(self):
        """Return the EventSource for the System Message channel."""
        return GR.SYS_MSG.subscribe()
