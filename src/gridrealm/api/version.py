"""Random Image URI Library."""

from enum import Enum
from flask_restful import Resource


API_VERSION = "0.1"


class Version(Resource):
    """Return the API version so the client can verify it is compatible."""

    uri = '/api/version'

    def get(self):
        """API endpoint to return the version of the in use API schema."""
        return {'version': API_VERSION}


class Resources(Enum):
    """Enum of all resources in this module."""

    version = Version

    @classmethod
    def add_resources(cls, api, resource_classes=None):
        """Register the given resources on the api object."""
        if not resource_classes:
            resource_classes = [res.value for res in cls]
        for res_cls in resource_classes:
            api.add_resource(res_cls, res_cls.uri)
