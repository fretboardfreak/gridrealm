"""Load gridrealm objects for manual development.

Import the module using "from manual import *" inside the ipython environment
given by "make ipy".
"""

import gridrealm as GR
import gridrealm.database as DB
import gridrealm.main as M


DEFAULT_CLI_ARGS = ['--config', '../dev.cfg', '--debug']
ARGS = None


def load(cliargs=None):
    """Load enough of the game that manual debugging can start."""
    if cliargs is None:
        cliargs = DEFAULT_CLI_ARGS
    global ARGS
    ARGS = M.parse_args(cliargs)

    M.load_config(ARGS)
    M.load_flask(ARGS)
    M.prep_db(ARGS)


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
