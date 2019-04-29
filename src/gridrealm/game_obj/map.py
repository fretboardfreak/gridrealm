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
"""Gridrealm Map Object."""

from enum import Enum
from enum import auto

from gridrealm.database import MapCoord
from gridrealm.database import MapTile
from gridrealm.database.ascii_map import Tile


def get_coord(xcoord, ycoord, zcoord=None):
    """Retrieve a MapCoord object from the database by coordinates."""
    if zcoord is None:
        # most commonly used z-layer is 0
        zcoord = 0
    return MapCoord.query.filter(
        MapCoord.xcoord == xcoord).filter(
            MapCoord.ycoord == ycoord).filter(
                MapCoord.zcoord == zcoord).first()


def get_tile(name):
    """Retrieve a MapTile object from the database by name."""
    return MapTile.query.filter(MapTile.name == name).first()


class Direction(Enum):
    """Enum of Map Directions."""

    north = auto()
    south = auto()
    east = auto()
    west = auto()


class MoveFlags(Enum):
    """Enum of the move flag attributes that a MapTile has."""

    enterN = auto()
    enterS = auto()
    enterE = auto()
    enterW = auto()
    exitN = auto()
    exitS = auto()
    exitE = auto()
    exitW = auto()


class MapMaps(object):
    """An object of useful maps for the maps moduleself.

    TODO: find a better name for this object. This one sucks.
    """

    # direction deltas: direction -> (x_delta, y_delta, z_delta)
    direction_coord_delta = {
        Direction.north.name: (0, 1, 0),
        Direction.south.name: (0, -1, 0),
        Direction.east.name: (1, 0, 0),
        Direction.west.name: (-1, 0, 0)}

    complimentary_move_flags = {
        MoveFlags.enterN.name: MoveFlags.exitS.name,
        MoveFlags.enterS.name: MoveFlags.exitN.name,
        MoveFlags.enterE.name: MoveFlags.exitW.name,
        MoveFlags.enterW.name: MoveFlags.exitE.name,
        MoveFlags.exitN.name: MoveFlags.enterS.name,
        MoveFlags.exitS.name: MoveFlags.enterN.name,
        MoveFlags.exitE.name: MoveFlags.enterW.name,
        MoveFlags.exitW.name: MoveFlags.enterE.name}


def get_next_coord(current, direction):
    """Get the next Map Coordinate in the given cardinal direction."""
    if isinstance(direction, Enum) and direction in Direction:
        direction = direction.name
    elif direction not in [d.name for d in Direction]:
        raise ValueError('Invalid direction value: %s' % direction)
    delta_x, delta_y, delta_z = MapMaps.direction_coord_delta[direction]
    return get_coord(xcoord=current.xcoord + delta_x,
                     ycoord=current.ycoord + delta_y,
                     zcoord=current.zcoord + delta_z)


def is_move_allowed(current, dest):
    """Compare enter and exit flags to see if movement between tiles is OK."""
    delta = (dest.xcoord - current.xcoord,
             dest.ycoord - current.ycoord,
             dest.zcoord - current.zcoord)
    direction = None
    for cardinal in Direction:
        if delta == MapMaps.direction_coord_delta[cardinal.name]:
            direction = cardinal.name
    if direction is None:
        return False  # move wasn't in a supported direction
    exit_flag = 'exit' + direction[0].upper()
    enter_flag = MapMaps.complimentary_move_flags[exit_flag]
    return (getattr(current.tile, exit_flag, False) and
            getattr(dest.tile, enter_flag, False))


def get_minimap_move_flags(current):
    """Determine if movement is allowed in the cardinal directionsself.

    This is used to enable/disable the movement icons in the client.
    """
    nloc = get_next_coord(current, Direction.north)
    sloc = get_next_coord(current, Direction.south)
    eloc = get_next_coord(current, Direction.east)
    wloc = get_next_coord(current, Direction.west)
    return {
        Direction.north.name: current.tile.exitN and nloc.tile.enterS,
        Direction.east.name: current.tile.exitE and eloc.tile.enterW,
        Direction.south.name: current.tile.exitS and sloc.tile.enterN,
        Direction.west.name: current.tile.exitW and wloc.tile.enterE}


def _sanitize_zoom(zoom=None):
    """Normalize the requseted minimap zoom levelself.

    Zoom values will always be odd so that there is a center coordinate that
    the user is standing on. Also the minimap must be 3 by 3 tiles or larger.
    """
    if zoom is None or zoom < 3:
        return 3
    if zoom % 2 == 0:
        zoom -= 1  # round down to an odd number
    return zoom


def get_minimap_assets(current, zoom=None):
    """Return the array of minimap tile resources for the client."""
    zoom = _sanitize_zoom(zoom)
    radius = int((zoom - 1) / 2)  # i.e. zoom=3 -> radius = 1
    y_deltas = [n for n in range(-1 * radius, radius + 1)]
    x_deltas = y_deltas.copy()
    y_deltas.reverse()  # map is built from top left down
    x_loc, y_loc, z_loc = current.xcoord, current.ycoord, current.zcoord
    assets = []
    for row_index, y_delta in enumerate(y_deltas):
        assets.append([])
        for x_delta in x_deltas:
            coord = get_coord(xcoord=x_loc + x_delta,
                              ycoord=y_loc + y_delta,
                              zcoord=z_loc)  # minimap does not use Z-axis
            if coord is None:  # at map edges use obstacle tile resource
                resource = get_tile(Tile.obstacle.name).resource
            else:
                resource = coord.tile.resource
            assets[row_index].append(resource.split('\n'))
    return assets


def print_minimap(map_assets):
    """Print the ASCII minimap to the terminal for testing purposes.

    The print out uses '.' chars as table borders so individual map tiles are
    easier to pick out. ::

        ..........
        .+-.--.-+.
        .| .  . |.
        .+-.--.-+.
        ..........
    """
    first, sep = True, '.'
    for tile_row in map_assets:
        row_a, row_b = sep, sep
        for column in tile_row:
            row_a += column[0] + sep
            row_b += column[1] + sep
        row_len = len(row_a)
        if first:
            print(sep * row_len)
            first = False
        print(row_a)
        print(row_b)
        print(sep * row_len)
