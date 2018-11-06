"""
gridrealm main entry point.

This is the main entry point for the game Grid Realm. This is a WSGI
application that serves the game assets, client and performs the backend game
server activities. A CLI main method is also provided for testing and offline
use.
"""

import sys
from argparse import ArgumentParser

from flask import Flask
from flask_restful import Api
import gevent.monkey

import gridrealm
from gridrealm.static_routes import register_static_views
from gridrealm.api import random_image
from gridrealm.api import version
from gridrealm.config import Config
from gridrealm.config import guess_a_config_location
from gridrealm.server_events import Channel
from gridrealm.database import init_db
from gridrealm.database import load_db
from gridrealm.database.ascii_map import create_map


def cli_main():
    """The main method for the Netify app, when called from the CLI."""
    parser = ArgumentParser(description=__doc__)
    discovered_configs = '\n  - '.join(guess_a_config_location())
    parser.add_argument(
        '-c', '--config', action='store', required=True,
        help=("Specify a path to the config file that you wish to use. "
              "Some available config files that were discovered:\n%s" %
              discovered_configs))
    parser.add_argument(
        '--debug', action='store_true',
        help=("Enable debug in Netify and Flask. (Not suitable for "
              "production.)"))
    default_port = 5000
    parser.add_argument(
        '-p', '--port', action='store', type=int, default=default_port,
        help="Use a different port. [Default: %s]" % default_port)
    parser.add_argument(
        '--public', action='store_true',
        help=("Accept connections from external requests using the "
              "dev server."))
    parser.add_argument(
        '--initdb', action='store_true',
        help="Initialize the database and exit."
    )
    args = parser.parse_args()

    host = None
    if args.public:
        host = '0.0.0.0'

    # This patches the python threading stuff with greenlets from gevent
    gevent.monkey.patch_all()

    flask_app = Flask(__name__)
    rest_api = Api(flask_app)

    # save the flask app to a global var for the rest of the system
    gridrealm.APP = flask_app
    gridrealm.SYS_MSG = Channel()

    config = Config(args.config)
    config.update_flask(flask_app)

    load_db(config.gridrealm.database_url)

    if args.initdb:
        print('Initializing Game Database and Exiting.')
        init_db()
        create_map()
        sys.exit(0)

    # pylint: disable=unused-variable
    @gridrealm.APP.teardown_appcontext
    def shutdown_session(exception=None):
        # pylint: disable=unused-argument
        gridrealm.DBS.remove()

    register_static_views(flask_app)
    # Register the REST API Resources
    random_image.Resources.add_resources(rest_api)
    version.Resources.add_resources(rest_api)

    flask_app.run(host=host, port=args.port, debug=args.debug)


def uwsgi_main(config_file):
    """The main method for the Netify app, when started via UWSGI."""
    print(config_file)
    # TODO: rewrite for gridrealm
    # netify_app = NetifyApp(Config.load_config(config_file))
    # netify_app.register_views(Views)
    # # netify_app.flask_app.logger.info('NETIFY Loaded.')
    #
    # return netify_app.flask_app
