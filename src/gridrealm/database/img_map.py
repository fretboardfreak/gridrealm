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
"""Gridrealm Image Map.

This is a basic map type that uses PNG image files to build a map.
"""


from enum import Enum
from enum import auto

import gridrealm
import gridrealm.database as db


class Tile(Enum):
    """The set of names used to identify the tiles in the TileSet."""

    ground = auto()  # 00
    obstacle = auto()  # 01
    wall_narrow_corner_nw = auto()  # 02
    wall_narrow_corner_ne = auto()  # 03
    wall_narrow_corner_sw = auto()  # 04
    wall_narrow_corner_se = auto()  # 05
    wall_narrow_n = auto()  # 06
    wall_narrow_s = auto()  # 07
    wall_narrow_w = auto()  # 08
    wall_narrow_e = auto()  # 09
    hallway_ew = auto()  # 10
    hallway_ns = auto()  # 11
    hallway_end_w = auto()  # 12
    hallway_end_e = auto()  # 13
    hallway_end_s = auto()  # 14
    hallway_end_n = auto()  # 15
    hallway_corner_nw = auto()  # 16
    hallway_corner_ne = auto()  # 17
    hallway_corner_se = auto()  # 18
    hallway_corner_sw = auto()  # 19
    wall_wide_corner_nw = auto()  # 20
    wall_wide_corner_ne = auto()  # 21
    wall_wide_corner_se = auto()  # 22
    wall_wide_corner_sw = auto()  # 23
    wall_wide_w = auto()  # 24
    wall_wide_e = auto()  # 25
    wall_wide_n = auto()  # 26
    wall_wide_s = auto()  # 27


class TileSet(Enum):
    """The tile objects for the tile set."""

    ground = db.MapTile(
        name=Tile.ground.name, tile_type=db.TileType.image,
        resource="00.png",
        enterN=True, enterE=True, enterS=True, enterW=True,
        exitN=True, exitE=True, exitS=True, exitW=True)

    obstacle = db.MapTile(
        name=Tile.obstacle.name, tile_type=db.TileType.image,
        resource="01.png",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)

    wall_narrow_corner_nw = db.MapTile(
        name=Tile.wall_narrow_corner_nw.name,
        tile_type=db.TileType.image, resource="02.png",
        enterN=False, enterE=True, enterS=True, enterW=False,
        exitN=False, exitE=True, exitS=True, exitW=False)

    wall_narrow_corner_ne = db.MapTile(
        name=Tile.wall_narrow_corner_ne.name,
        tile_type=db.TileType.image, resource="03.png",
        enterN=False, enterE=False, enterS=True, enterW=True,
        exitN=False, exitE=False, exitS=True, exitW=True)

    wall_narrow_corner_sw = db.MapTile(
        name=Tile.wall_narrow_corner_sw.name,
        tile_type=db.TileType.image, resource="04.png",
        enterN=True, enterE=True, enterS=False, enterW=False,
        exitN=True, exitE=True, exitS=False, exitW=False)

    wall_narrow_corner_se = db.MapTile(
        name=Tile.wall_narrow_corner_se.name,
        tile_type=db.TileType.image, resource="05.png",
        enterN=True, enterE=False, enterS=False, enterW=True,
        exitN=True, exitE=False, exitS=False, exitW=True)

    wall_narrow_n = db.MapTile(
        name=Tile.wall_narrow_n.name,
        tile_type=db.TileType.image, resource="06.png",
        enterN=False, enterE=True, enterS=True, enterW=True,
        exitN=False, exitE=True, exitS=True, exitW=True)

    wall_narrow_s = db.MapTile(
        name=Tile.wall_narrow_s.name,
        tile_type=db.TileType.image, resource="07.png",
        enterN=True, enterE=True, enterS=False, enterW=True,
        exitN=True, exitE=True, exitS=False, exitW=True)

    wall_narrow_w = db.MapTile(
        name=Tile.wall_narrow_w.name,
        tile_type=db.TileType.image, resource="08.png",
        enterN=True, enterE=True, enterS=True, enterW=False,
        exitN=True, exitE=True, exitS=True, exitW=False)

    wall_narrow_e = db.MapTile(
        name=Tile.wall_narrow_e.name,
        tile_type=db.TileType.image, resource="09.png",
        enterN=True, enterE=False, enterS=True, enterW=True,
        exitN=True, exitE=False, exitS=True, exitW=True)

    hallway_ew = db.MapTile(
        name=Tile.hallway_ew.name,
        tile_type=db.TileType.image, resource="10.png",
        enterN=False, enterE=True, enterS=False, enterW=True,
        exitN=False, exitE=True, exitS=False, exitW=True)

    hallway_ns = db.MapTile(
        name=Tile.hallway_ns.name,
        tile_type=db.TileType.image, resource="11.png",
        enterN=True, enterE=False, enterS=True, enterW=False,
        exitN=True, exitE=False, exitS=True, exitW=False)

    hallway_end_w = db.MapTile(
        name=Tile.hallway_end_w.name,
        tile_type=db.TileType.image, resource="12.png",
        enterN=False, enterE=True, enterS=False, enterW=False,
        exitN=False, exitE=True, exitS=False, exitW=False)

    hallway_end_e = db.MapTile(
        name=Tile.hallway_end_e.name,
        tile_type=db.TileType.image, resource="13.png",
        enterN=False, enterE=False, enterS=False, enterW=True,
        exitN=False, exitE=False, exitS=False, exitW=True)

    hallway_end_s = db.MapTile(
        name=Tile.hallway_end_s.name,
        tile_type=db.TileType.image, resource="14.png",
        enterN=True, enterE=False, enterS=False, enterW=False,
        exitN=True, exitE=False, exitS=False, exitW=False)

    hallway_end_n = db.MapTile(
        name=Tile.hallway_end_n.name,
        tile_type=db.TileType.image, resource="15.png",
        enterN=False, enterE=False, enterS=True, enterW=False,
        exitN=False, exitE=False, exitS=True, exitW=False)

    hallway_corner_nw = db.MapTile(
        name=Tile.hallway_corner_nw.name,
        tile_type=db.TileType.image, resource="16.png",
        enterN=False, enterE=True, enterS=True, enterW=False,
        exitN=False, exitE=True, exitS=True, exitW=False)

    hallway_corner_ne = db.MapTile(
        name=Tile.hallway_corner_ne.name,
        tile_type=db.TileType.image, resource="17.png",
        enterN=False, enterE=False, enterS=True, enterW=True,
        exitN=False, exitE=False, exitS=True, exitW=True)

    hallway_corner_se = db.MapTile(
        name=Tile.hallway_corner_se.name,
        tile_type=db.TileType.image, resource="18.png",
        enterN=True, enterE=False, enterS=False, enterW=True,
        exitN=True, exitE=False, exitS=False, exitW=True)

    hallway_corner_sw = db.MapTile(
        name=Tile.hallway_corner_sw.name,
        tile_type=db.TileType.image, resource="19.png",
        enterN=True, enterE=True, enterS=False, enterW=False,
        exitN=True, exitE=True, exitS=False, exitW=False)

    wall_wide_corner_nw = db.MapTile(
        name=Tile.wall_wide_corner_nw.name,
        tile_type=db.TileType.image, resource="20.png",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)

    wall_wide_corner_ne = db.MapTile(
        name=Tile.wall_wide_corner_ne.name,
        tile_type=db.TileType.image, resource="21.png",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)

    wall_wide_corner_se = db.MapTile(
        name=Tile.wall_wide_corner_se.name,
        tile_type=db.TileType.image, resource="22.png",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)

    wall_wide_corner_sw = db.MapTile(
        name=Tile.wall_wide_corner_sw.name,
        tile_type=db.TileType.image, resource="23.png",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)

    wall_wide_w = db.MapTile(
        name=Tile.wall_wide_w.name,
        tile_type=db.TileType.image, resource="24.png",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)

    wall_wide_e = db.MapTile(
        name=Tile.wall_wide_e.name,
        tile_type=db.TileType.image, resource="25.png",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)

    wall_wide_n = db.MapTile(
        name=Tile.wall_wide_n.name,
        tile_type=db.TileType.image, resource="26.png",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)

    wall_wide_s = db.MapTile(
        name=Tile.wall_wide_s.name,
        tile_type=db.TileType.image, resource="27.png",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)


def query_tiles(name):
    """Return Tile objects from the database with a given name."""
    return db.MapTile.query.filter(
        db.MapTile.name == TileSet[name].name).first()


def generate_test_map_coords():
    """Create a set of map coordinates for a small test map.

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
    tile = query_tiles(Tile.wall_narrow_corner_nw.name)
    yield db.MapCoord(xcoord=-1, ycoord=1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_n.name)
    yield db.MapCoord(xcoord=0, ycoord=1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_n.name)
    yield db.MapCoord(xcoord=1, ycoord=1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_corner_ne.name)
    yield db.MapCoord(xcoord=2, ycoord=1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_w.name)
    yield db.MapCoord(xcoord=-1, ycoord=0, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.ground.name)
    yield db.MapCoord(xcoord=0, ycoord=0, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.ground.name)
    yield db.MapCoord(xcoord=1, ycoord=0, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_e.name)
    yield db.MapCoord(xcoord=2, ycoord=0, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_w.name)
    yield db.MapCoord(xcoord=-1, ycoord=-1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.obstacle.name)
    yield db.MapCoord(xcoord=0, ycoord=-1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.ground.name)
    yield db.MapCoord(xcoord=1, ycoord=-1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_e.name)
    yield db.MapCoord(xcoord=2, ycoord=-1, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_corner_sw.name)
    yield db.MapCoord(xcoord=-1, ycoord=-2, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_s.name)
    yield db.MapCoord(xcoord=0, ycoord=-2, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_s.name)
    yield db.MapCoord(xcoord=1, ycoord=-2, zcoord=zcoord, tile_id=tile.id)
    tile = query_tiles(Tile.wall_narrow_corner_se.name)
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
    for coord in generate_test_map_coords():  # yields MapCoord objs
        print(' - %s, %s, %s' % (
            coord.xcoord, coord.ycoord, coord.tile_id))
        gridrealm.DBS.add(coord)

    gridrealm.DBS.commit()
    print('...commited')


def create_map():
    """Create the database entries to describe the basic ASCII map."""
    create_tile_set()
    create_map_coords()
