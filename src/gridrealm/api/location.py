"""Location API Endpoint."""

from flask import g as flask_g
from flask_restful import Resource

import gridrealm.database as DB
from gridrealm.auth import user_required
from gridrealm.api.core import ResourceEnum


class Location(Resource):
    """Endpoint for querying information about the user's location."""

    uri = '/api/location'

    def get(self):
        """API endpoint to return the version of the in use API schema."""
        response = {}
        index_map = [[(-1, 1), (0, 1), (1, 1)],
                     [(-1, 0), (0, 0), (1, 0)],
                     [(-1, -1), (0, -1), (1, -1)]]
        map_assets = []
        user = flask_g.user
        for i, row in enumerate(index_map):
            map_assets.append([])
            for col in row:
                coord = DB.MapCoord.query.filter(
                    DB.MapCoord.xcoord == user.xcoord + col[0]).filter(
                        DB.MapCoord.ycoord == user.ycoord + col[1]).first()
                map_assets[i].append(coord.tile.resource.split('\n'))
        response['minimap'] = map_assets
        loc = DB.MapCoord.query.filter(
            DB.MapCoord.xcoord == user.xcoord).filter(
                DB.MapCoord.ycoord == user.ycoord).first()
        nloc = DB.MapCoord.query.filter(
            DB.MapCoord.xcoord == user.xcoord).filter(
                DB.MapCoord.ycoord == user.ycoord + 1).first()
        sloc = DB.MapCoord.query.filter(
            DB.MapCoord.xcoord == user.xcoord).filter(
                DB.MapCoord.ycoord == user.ycoord + 1).first()
        wloc = DB.MapCoord.query.filter(
            DB.MapCoord.xcoord == user.xcoord - 1).filter(
                DB.MapCoord.ycoord == user.ycoord).first()
        eloc = DB.MapCoord.query.filter(
            DB.MapCoord.xcoord == user.xcoord + 1).filter(
                DB.MapCoord.ycoord == user.ycoord).first()
        response['movement'] = {'north': loc.tile.exitN and nloc.tile.enterS,
                                'east': loc.tile.exitE and eloc.tile.enterW,
                                'south': loc.tile.exitS and sloc.tile.enterN,
                                'west': loc.tile.exitW and wloc.tile.enterE}
        return response

    get = user_required(get)


class Resources(ResourceEnum):
    """Enum of all resources in this module."""

    location = Location
