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
"""Gridrealm ASCII Map.

This is a basic map type, that does not require external assets and uses text
characters rendered for the browser as basic graphics.
"""


from enum import Enum
from enum import auto

import gridrealm
import gridrealm.database as db


class Tile(Enum):
    """The set of names used to identify the tiles in the TileSet."""

    ground = auto()
    nw_corner = auto()
    sw_corner = auto()
    se_corner = auto()
    ne_corner = auto()
    n_wall = auto()
    s_wall = auto()
    e_wall = auto()
    w_wall = auto()
    obstacle = auto()


class TileSet(Enum):
    """A map tile set using 2x2 arrays of ascii characters."""

    # "  "   ground
    # "  "
    ground = db.MapTile(
        name=Tile.ground.name, tile_type=db.TileType.text,
        resource="  \n  ",
        enterN=True, enterE=True, enterS=True, enterW=True,
        exitN=True, exitE=True, exitS=True, exitW=True)

    # "+-"   nw-corner
    # "| "
    nw_corner = db.MapTile(
        name=Tile.nw_corner.name, tile_type=db.TileType.text,
        resource="+-\n| ",
        enterN=False, enterE=True, enterS=True, enterW=False,
        exitN=False, exitE=True, exitS=True, exitW=False)

    # "-+"   ne-corner
    # " |"
    ne_corner = db.MapTile(
        name=Tile.ne_corner.name, tile_type=db.TileType.text,
        resource="-+\n |",
        enterN=False, enterE=False, enterS=True, enterW=True,
        exitN=False, exitE=False, exitS=True, exitW=True)

    # "| "   sw-corner
    # "+-"
    sw_corner = db.MapTile(
        name=Tile.sw_corner.name, tile_type=db.TileType.text,
        resource="| \n+-",
        enterN=True, enterE=True, enterS=False, enterW=False,
        exitN=True, exitE=True, exitS=False, exitW=False)

    # " |"   se-corner
    # "-+"
    se_corner = db.MapTile(
        name=Tile.se_corner.name, tile_type=db.TileType.text,
        resource=" |\n-+",
        enterN=True, enterE=False, enterS=False, enterW=True,
        exitN=True, exitE=False, exitS=False, exitW=True)

    # "--"   n-wall
    # "  "
    n_wall = db.MapTile(
        name=Tile.n_wall.name, tile_type=db.TileType.text,
        resource="--\n  ",
        enterN=False, enterE=True, enterS=True, enterW=True,
        exitN=False, exitE=True, exitS=True, exitW=True)

    # "  "   s-wall
    # "--"
    s_wall = db.MapTile(
        name=Tile.s_wall.name, tile_type=db.TileType.text,
        resource="  \n--",
        enterN=True, enterE=True, enterS=False, enterW=True,
        exitN=True, exitE=True, exitS=False, exitW=True)

    # "| "   w-wall
    # "| "
    w_wall = db.MapTile(
        name=Tile.w_wall.name, tile_type=db.TileType.text,
        resource="| \n| ",
        enterN=True, enterE=True, enterS=True, enterW=False,
        exitN=True, exitE=True, exitS=True, exitW=False)

    # " |"   e-wall
    # " |"
    e_wall = db.MapTile(
        name=Tile.e_wall.name, tile_type=db.TileType.text,
        resource=" |\n |",
        enterN=True, enterE=False, enterS=True, enterW=True,
        exitN=True, exitE=False, exitS=True, exitW=True)

    # "XX"   obstacle
    # "XX"
    obstacle = db.MapTile(
        name=Tile.obstacle.name, tile_type=db.TileType.text,
        resource="XX\nXX",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)


def query_tiles(name):
    """Return Tile objects from the database with a given name."""
    return db.MapTile.query.filter(
        db.MapTile.name == TileSet[name].name).first()


def generate_map_coords():
    """Create a set of map coordinates representing the world.

    +------+  [-1,1]nw-corner,[0,1]n-wall,[1,1]n-wall,[2,1]ne-corner
    |      |
    |      |  [-1,0]w-wall,[0,0]ground,[1,0]ground,[2,0]e-wall
    |      |
    | XX   |  [-1,-1]w-wall,[0,-1]obstacle,[1,-1]ground,[2,-1]e-wall
    | XX   |
    |      |  [-1,-2]sw-corner,[0,-2]s-wall,[1,-2]s-wall,[2,-2]se-corner
    +------+

    """
    zcoord = 0
    tile = query_tiles(Tile.nw_corner.name)
    yield db.MapCoord(xcoord=-1, ycoord=1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.n_wall.name)
    yield db.MapCoord(xcoord=0, ycoord=1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.n_wall.name)
    yield db.MapCoord(xcoord=1, ycoord=1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.ne_corner.name)
    yield db.MapCoord(xcoord=2, ycoord=1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.w_wall.name)
    yield db.MapCoord(xcoord=-1, ycoord=0, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.ground.name)
    yield db.MapCoord(xcoord=0, ycoord=0, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.ground.name)
    yield db.MapCoord(xcoord=1, ycoord=0, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.e_wall.name)
    yield db.MapCoord(xcoord=2, ycoord=0, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.w_wall.name)
    yield db.MapCoord(xcoord=-1, ycoord=-1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.obstacle.name)
    yield db.MapCoord(xcoord=0, ycoord=-1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.ground.name)
    yield db.MapCoord(xcoord=1, ycoord=-1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.e_wall.name)
    yield db.MapCoord(xcoord=2, ycoord=-1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.sw_corner.name)
    yield db.MapCoord(xcoord=-1, ycoord=-2, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.s_wall.name)
    yield db.MapCoord(xcoord=0, ycoord=-2, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.s_wall.name)
    yield db.MapCoord(xcoord=1, ycoord=-2, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.se_corner.name)
    yield db.MapCoord(xcoord=2, ycoord=-2, zcoord=zcoord, tile_id=tile.id)


def create_tile_set():
    """Create the tile set objects in the database."""
    # pylint: disable=no-member
    print('Creating Tile Set...')
    for tile in TileSet:  # enum of MapTile objs
        print(' - %s' % tile.value.name)
        gridrealm.DBS.add(tile.value)

    gridrealm.DBS.commit()
    print('...commited')


def create_map_coords():
    """Create the map coordinate objects in the database."""
    # pylint: disable=no-member
    print('Creating Map Coordinates...')
    for coord in generate_map_coords():  # yields MapCoord objs
        print(' - %s, %s, %s' % (
            coord.xcoord, coord.ycoord, coord.tile_id))
        gridrealm.DBS.add(coord)

    gridrealm.DBS.commit()
    print('...commited')


def create_map():
    """Create the database entries to describe the basic ASCII map."""
    create_tile_set()
    create_map_coords()
