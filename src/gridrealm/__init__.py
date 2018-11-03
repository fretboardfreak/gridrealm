"""Gridrealm engine package."""
# Copyright Curtis Sand, Dennison Gaetz - 2018

from .main import cli_main
from .main import uwsgi_main
from .config import Config


# These Globals are set by the main methods so that they can be accessed from
# anywhere.

# Flask app object
APP = None

# Message broadcast channel for server to client messages
SYS_MSG = None


DBE = None  # Backend Database Engine
DBS = None  # Backend Database Session
