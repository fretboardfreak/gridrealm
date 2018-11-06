"""Gridrealm ASCII Map.

This is a basic map type, that does not require external assets and uses text
characters rendered for the browser as basic graphics.
"""


from enum import Enum

import gridrealm
import gridrealm.database as db


# def create_tiles():
#     """Create a set of text based tiles to build the map from."""
#     tiles = {}
class TileSet(Enum):
    """A map tile set using 2x2 arrays of ascii characters."""

    # "  "   ground
    # "  "
    ground = db.MapTile(
        name="ground", tile_type=db.TileType.text, resource="  \n  ",
        enterN=True, enterE=True, enterS=True, enterW=True,
        exitN=True, exitE=True, exitS=True, exitW=True)

    # "+-"   nw-corner
    # "| "
    nw_corner = db.MapTile(
        name="nw-corner", tile_type=db.TileType.text, resource="+-\n| ",
        enterN=False, enterE=True, enterS=True, enterW=False,
        exitN=False, exitE=True, exitS=True, exitW=False)

    # "-+"   ne-corner
    # " |"
    ne_corner = db.MapTile(
        name="ne-corner", tile_type=db.TileType.text, resource="-+\n |",
        enterN=False, enterE=False, enterS=True, enterW=True,
        exitN=False, exitE=False, exitS=True, exitW=True)

    # "| "   sw-corner
    # "+-"
    sw_corner = db.MapTile(
        name="sw-corner", tile_type=db.TileType.text, resource="| \n+-",
        enterN=True, enterE=True, enterS=False, enterW=False,
        exitN=True, exitE=True, exitS=False, exitW=False)

    # " |"   se-corner
    # "-+"
    se_corner = db.MapTile(
        name="se-corner", tile_type=db.TileType.text, resource=" |\n-+",
        enterN=True, enterE=False, enterS=False, enterW=True,
        exitN=True, exitE=False, exitS=False, exitW=True)

    # "--"   n-wall
    # "  "
    n_wall = db.MapTile(
        name="n-wall", tile_type=db.TileType.text, resource="--\n  ",
        enterN=False, enterE=True, enterS=True, enterW=True,
        exitN=False, exitE=True, exitS=True, exitW=True)

    # "  "   s-wall
    # "--"
    s_wall = db.MapTile(
        name="s-wall", tile_type=db.TileType.text, resource="  \n--",
        enterN=True, enterE=True, enterS=False, enterW=True,
        exitN=True, exitE=True, exitS=False, exitW=True)

    # "| "   w-wall
    # "| "
    w_wall = db.MapTile(
        name="w-wall", tile_type=db.TileType.text, resource="| \n| ",
        enterN=True, enterE=True, enterS=True, enterW=False,
        exitN=True, exitE=True, exitS=True, exitW=False)

    # " |"   e-wall
    # " |"
    e_wall = db.MapTile(
        name="e-wall", tile_type=db.TileType.text, resource=" |\n |",
        enterN=True, enterE=False, enterS=True, enterW=True,
        exitN=True, exitE=False, exitS=True, exitW=True)

    # "XX"   obstacle
    # "XX"
    obstacle = db.MapTile(
        name="obstacle", tile_type=db.TileType.text, resource="XX\nXX",
        enterN=False, enterE=False, enterS=False, enterW=False,
        exitN=False, exitE=False, exitS=False, exitW=False)


def generate_map():
    """Create a set of map coordinates representing the world."""
    # Note: to start there is no change in z coordinate.
    #  "+------+" [-1,1]nw-corner,[0,1]n-wall,[1,1]n-wall,[2,1]ne-corner
    #  "|      |"
    #  "|      |" [-1,0]w-wall,[0,0]ground,[1,0]ground,[2,0]e-wall
    #  "|      |"
    #  "| XX   |" [-1,-1]w-wall,[0,-1]obstacle,[1,-1]ground,[2,-1]e-wall
    #  "| XX   |"
    #  "|      |" [-1,-2]sw-corner,[0,-2]s-wall,[1,-2]s-wall,[2,-2]se-corner
    #  "+------+"

    zcoord = 0

    yield db.MapCoord(xcoord=-1, ycoord=1, zcoord=zcoord,
                      tile_id=TileSet.nw_corner.value.id)
    yield db.MapCoord(xcoord=0, ycoord=1, zcoord=zcoord,
                      tile_id=TileSet.n_wall.value.id)
    yield db.MapCoord(xcoord=1, ycoord=1, zcoord=zcoord,
                      tile_id=TileSet.n_wall.value.id)
    yield db.MapCoord(xcoord=2, ycoord=1, zcoord=zcoord,
                      tile_id=TileSet.ne_corner.value.id)
    yield db.MapCoord(xcoord=-1, ycoord=0, zcoord=zcoord,
                      tile_id=TileSet.w_wall.value.id)
    yield db.MapCoord(xcoord=0, ycoord=0, zcoord=zcoord,
                      tile_id=TileSet.ground.value.id)
    yield db.MapCoord(xcoord=1, ycoord=0, zcoord=zcoord,
                      tile_id=TileSet.ground.value.id)
    yield db.MapCoord(xcoord=2, ycoord=0, zcoord=zcoord,
                      tile_id=TileSet.e_wall.value.id)
    yield db.MapCoord(xcoord=-1, ycoord=-1, zcoord=zcoord,
                      tile_id=TileSet.w_wall.value.id)
    yield db.MapCoord(xcoord=0, ycoord=-1, zcoord=zcoord,
                      tile_id=TileSet.obstacle.value.id)
    yield db.MapCoord(xcoord=1, ycoord=-1, zcoord=zcoord,
                      tile_id=TileSet.ground.value.id)
    yield db.MapCoord(xcoord=2, ycoord=-1, zcoord=zcoord,
                      tile_id=TileSet.e_wall.value.id)
    yield db.MapCoord(xcoord=-1, ycoord=-2, zcoord=zcoord,
                      tile_id=TileSet.sw_corner.value.id)
    yield db.MapCoord(xcoord=0, ycoord=-2, zcoord=zcoord,
                      tile_id=TileSet.s_wall.value.id)
    yield db.MapCoord(xcoord=1, ycoord=-2, zcoord=zcoord,
                      tile_id=TileSet.s_wall.value.id)
    yield db.MapCoord(xcoord=2, ycoord=-2, zcoord=zcoord,
                      tile_id=TileSet.se_corner.value.id)


def create_map():
    """Create the database entries to describe the basic ASCII map."""
    logger = gridrealm.APP.logger
    # pylint doesn't know what value DBS gets set as after load
    # pylint: disable=no-member
    logger.debug('Creating Tile Set...')
    for tile in TileSet:  # enum of MapTile objs
        logger.debug(' -', tile.value.name)
        gridrealm.DBS.add(tile.value)

    gridrealm.DBS.commit()
    logger.debug('...commited')

    logger.debug('Creating Map Coordinates...')
    for coord in generate_map():  # yields MapCoord objs
        logger.debug(' -', coord.xcoord, coord.ycoord, coord.tile_id)
        gridrealm.DBS.add(coord)

    gridrealm.DBS.commit()
    logger.debug('...commited')
