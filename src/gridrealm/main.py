"""
Grid Realm

This is the main entry point for the game Grid Realm. This is a WSGI
application that serves the game assets, client and performs the backend game
server activities.
"""
import os
import random
from flask import Flask
from flask import send_file
from flask import abort
from flask_restful import Resource, Api

API_VERSION="0.0"

# app and api are required by flask and flask_restful
APP = Flask(__name__)
API = Api(APP)

class Config(object):
    """A set of configuration options for the API server."""
    debug = True
    asset_path = "client/_assets"
    css_stub = "client/css/%s"
    js_stub = "client/js/%s"
    asset_stub = asset_path + "/%s"
    asset_uri = '_assets'
    docs_stub = "docs/%s"


def _abort_if_file_missing(path, errno=404):
    if not os.path.exists(path):
        abort(errno)

@APP.route('/')
def index():
    client = "client/client.html"
    _abort_if_file_missing(client)
    return send_file(client)

@APP.route('/css/<path:stylesheet>')
def stylesheet(stylesheet):
    fpath = Config.css_stub % stylesheet
    _abort_if_file_missing(fpath)
    return send_file(fpath)

@APP.route('/js/<path:script>')
def script(script):
    fpath = Config.js_stub % script
    _abort_if_file_missing(fpath)
    return send_file(fpath)

@APP.route('/_assets/<path:asset>')
def asset(asset):
    fpath = Config.asset_stub % asset
    _abort_if_file_missing(fpath)
    return send_file(fpath)

@APP.route('/docs/')
@APP.route('/docs/<path:doc>')
def docs(doc=None):
    if not doc:
        doc = 'index.html'
    fpath = Config.docs_stub % doc
    _abort_if_file_missing(fpath)
    return send_file(fpath)

# ---- REST API ----

class Version(Resource):
    """Return the API version so the client can verify it is compatible."""

    def get(self):
        return {'version': API_VERSION}


class RandomImage(Resource):
    """Return a random image from the GR assetsself.

    This is intended for use as a means of testing.
    """

    def _load_image_list(self):
        images = []
        assets = "_assets"
        for dpath, dnames, fnames in os.walk(Config.asset_path):
            common = dpath[dpath.find(assets) + len(assets):]
            common = common[1:] if common.startswith('/') else common
            for fname in fnames:
                if fname.startswith(".") or fname.startswith("_"):
                    continue
                if fname not in images:
                    images.append(os.path.join(Config.asset_uri, common, fname))
        return images

    def get(self):
        return {'randomImage': random.choice(self._load_image_list())}


API.add_resource(Version, '/api/version')
API.add_resource(RandomImage, '/api/randomImage')

# ---- / REST API ----

if __name__ == '__main__':
    APP.run(debug=True)
