"""Gridrealm engine package."""
# Copyright Curtis Sand, Dennison Gaetz - 2018

from .main import cli_main
from .main import uwsgi_main
from .config import Config

# set by the main methods so that the APP object can be accessed from anywhere.
APP = None
