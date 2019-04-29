# Copyright 2019 Curtis Sand <curtissand@gmail.com>,
#                Dennison Gaetz <djgaetz@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
