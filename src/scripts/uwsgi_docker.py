"""UWSGI entrypoint for the gunicorn server."""
import sys
import os

# add project directory to the sys.path
project_home = u'/gridrealm/'

if project_home not in sys.path:
    sys.path = [project_home] + sys.path

import gridrealm

gridrealm.load_uwsgi('/gridrealm_config/docker.cfg')

# import flask app but need to call it "application" for WSGI to work
application = gridrealm.APP
