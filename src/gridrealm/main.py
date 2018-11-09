"""
gridrealm main entry point.

This is the main entry point for the game Grid Realm. This is a WSGI
application that serves the game assets, client and performs the backend game
server activities. A CLI main method is also provided for testing and offline
use.
"""

import os
import sys
from argparse import ArgumentParser
from subprocess import check_call

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


def parse_args(cliargs=None):
    """Parse the command line arguments."""
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
        help="Initialize the database and exit.")
    parser.add_argument(
        '--removedb', action='store_true',
        help="Remove the database file specified in the config file.")
    if cliargs is None:
        return parser.parse_args()
    else:
        return parser.parse_args(cliargs)


def load_flask(args):
    """Load the gridrealm flask app."""
    host = None
    if args.public:
        host = '0.0.0.0'
    args.host = host

    # save the flask app and api objects to a global var for the rest of the
    # system
    gridrealm.APP = Flask(__name__)
    gridrealm.API = Api(gridrealm.APP)


def load_config(args):
    """Load the configuration file."""
    config = Config(args.config)
    # set Config().gridrealm.debug to True if passed in at cmd line.
    if config.gridrealm.debug != args.debug:
        config.update_option('gridrealm', 'debug', args.debug)
    return


def prep_db(args):
    """Prepare the database engine and sessions for use."""
    config = Config()
    if args.removedb:
        path = config.gridrealm.database_url
        path = path.replace('sqlite:///', '')
        if os.path.exists(path):
            print('Removing database file: %s' % path)
            check_call(['rm', '-f', path])
        sys.exit(0)

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


def register_flask_views():
    """Register the views and API resources on the flask app."""
    register_static_views(gridrealm.APP)
    # Register the REST API Resources
    random_image.Resources.add_resources(gridrealm.API)
    version.Resources.add_resources(gridrealm.API)


def run_flask_server(args):
    """Execute the flask development server."""
    # This patches the python threading stuff with greenlets from gevent
    gevent.monkey.patch_all()

    Config().update_flask(gridrealm.APP)

    # prep a global system message server sent event channel
    gridrealm.SYS_MSG = Channel()

    gridrealm.APP.run(host=args.host, port=args.port, debug=args.debug)


def cli_main():
    """The main method for the Netify app, when called from the CLI."""
    args = parse_args()
    load_config(args)
    load_flask(args)
    prep_db(args)
    register_flask_views()
    run_flask_server(args)


def uwsgi_main(config_file):
    """The main method for the Netify app, when started via UWSGI."""
    print(config_file)
    # TODO: rewrite for gridrealm
    # netify_app = NetifyApp(Config.load_config(config_file))
    # netify_app.register_views(Views)
    # # netify_app.flask_app.logger.info('NETIFY Loaded.')
    #
    # return netify_app.flask_app
