"""Move API Endpoint."""

from http import HTTPStatus

from flask import request
from flask import abort
from flask import redirect
from flask import url_for
from flask import g as flask_g
from flask_restful import Resource

import gridrealm as GR
from gridrealm.auth import user_required
from gridrealm.game_obj import map as grmap  # don't override python builtins
from gridrealm.api.core import ResourceEnum


class Move(Resource):
    """Endpoint for changing the user's location."""

    uri = '/api/move'

    def post(self):
        """API endpoint to change the user's location."""
        if 'direction' not in request.form:
            abort(HTTPStatus.CONFLICT.value)
        if (request.form['direction'].lower() not in
                [d.name for d in grmap.Direction]):
            abort(HTTPStatus.CONFLICT.value)
        direction = request.form['direction'].lower()
        # get current location
        current = grmap.get_coord(flask_g.user.xcoord, flask_g.user.ycoord,
                                  flask_g.user.zcoord)
        # get coord trying to move to
        dest = grmap.get_next_coord(current, direction)

        # determine if movement is allowed; fail if not
        # if at edge of map, dest will be None, move is then not allowed
        if not dest or not grmap.is_move_allowed(current, dest):
            abort(HTTPStatus.BAD_REQUEST.value)

        # move allowed, update user's location in the database
        flask_g.user.xcoord = dest.xcoord
        flask_g.user.ycoord = dest.ycoord
        flask_g.user.zcoord = dest.zcoord

        # pylint doesn't like the DBS global
        # pylint: disable=no-member
        GR.DBS.add(flask_g.user)
        GR.DBS.commit()
        # redirect to the location API to populate the client with
        # the new location
        return GR.APP.make_response(redirect(url_for('location')))

    post = user_required(post)


class Resources(ResourceEnum):
    """Enum of all resources in this module."""

    location = Move
