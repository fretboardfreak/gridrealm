"""Location API Endpoint."""

from flask import session
from flask_restful import Resource

import gridrealm.database as DB
from gridrealm.api.core import ResourceEnum


class Location(Resource):
    """Endpoint for querying information about the user's location."""

    uri = '/api/location'

    def post(self):
        """API endpoint to return the version of the in use API schema."""
        # TODO: do something to make sure user is logged in
        if 'username' not in session:
            print('LOC: username not in session')
            # return {'error', 'User is not logged in'}
            return {}, 401
        uname = session['username']
        print('LOC: username in session: %s' % uname)
        # see if username is in database
        user = DB.User.query.filter(DB.User.name == uname).first()
        if user is None:
            print('LOC: user not in database')
            # return {'error', 'User is not logged in'}, 404
            return {}, 401
        print('LOC: user in database')
        response = {}
        index_map = [[(-1, 1), (0, 1), (1, 1)],
                     [(-1, 0), (0, 0), (1, 0)],
                     [(-1, -1), (0, -1), (1, -1)]]
        map_assets = []
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


class Resources(ResourceEnum):
    """Enum of all resources in this module."""

    location = Location
