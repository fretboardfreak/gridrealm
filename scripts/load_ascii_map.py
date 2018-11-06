"""Load ASCII Map.

The module is meant to be used manually with a python interpreter.
"""
import gridrealm as GR
import gridrealm.database as DB

# pylint: disable=unused-import
from gridrealm.database.ascii_map import create_map


DATABASE_URL = 'sqlite:////tmp/grtest.db'
DB.load_db(DATABASE_URL)


def get_game_map():
    """Query the database for the game."""
    # pylint: disable=no-member
    return GR.DBS.query(DB.MapCoord).all()


def print_map():
    """Print the game map from the database."""
    game_map = get_game_map()

    y_coords = [y for y in range(-3, 4)]
    y_coords.reverse()
    for y_coord in y_coords:
        if y_coord not in [coord.ycoord for coord in game_map]:
            continue
        row_a, row_b = '', ''
        for tile_str in [coord.tile.resource for coord in game_map
                         if coord.ycoord == y_coord]:
            part_a, part_b = tile_str.split('\n')
            row_a += part_a
            row_b += part_b
        print(row_a)
        print(row_b)
