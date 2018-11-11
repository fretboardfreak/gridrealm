"""Location API Endpoint."""

from flask import g as flask_g
from flask_restful import Resource

from gridrealm.auth import user_required
from gridrealm.api.core import ResourceEnum
from gridrealm.game_obj import map as grmap  # don't override python builtins


class Location(Resource):
    """Endpoint for querying information about the user's location."""

    uri = '/api/location'

    def get(self):
        """API endpoint to return the version of the in use API schema."""
        response = {}
        location = grmap.get_coord(xcoord=flask_g.user.xcoord,
                                   ycoord=flask_g.user.ycoord,
                                   zcoord=flask_g.user.zcoord)
        response['minimap'] = grmap.get_minimap_assets(location)
        response['movement'] = grmap.get_minimap_move_flags(location)
        return response

    get = user_required(get)


class Resources(ResourceEnum):
    """Enum of all resources in this module."""

    location = Location
