"""
Grid Realm API Server

This is how the GR webrowser client talks to the game logic.
"""
import os
import random
from flask import Flask
from flask_restful import Resource, Api

API_VERSION="0.0"

# app and api are required by flask and flask_restful
APP = Flask(__name__)
API = Api(APP)


class Config(object):
    """A set of configuration options for the API server."""
    debug = True
    asset_path = os.path.expanduser("~/gridrealm/src/gridrealm/client/_assets")
    asset_server = "127.0.0.1/client/_assets/"


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
        for dpath, dnames, fnames in os.walk(Config.asset_path):
            common = os.path.commonprefix([Config.asset_path, dpath])
            for fname in fnames:
                if fname.startswith(".") or fname.startswith("_"):
                    continue
                if fname not in images:
                    images.append(os.path.join(Config.asset_server,
                                               dpath[len(common):], fname))
        return images

    def get(self):
        return {'randomImage': random.choice(self._load_image_list())}


API.add_resource(Version, '/version')
API.add_resource(RandomImage, '/randomImage')


if __name__ == '__main__':
    APP.run(debug=Config.debug)
