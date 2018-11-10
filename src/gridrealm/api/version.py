"""Gridrealm API Version Endpoint."""

from flask_restful import Resource

from gridrealm.api.core import ResourceEnum
from gridrealm.api.core import API_VERSION


class Version(Resource):
    """Return the API version so the client can verify it is compatible."""

    uri = '/api/version'

    def get(self):
        """API endpoint to return the version of the in use API schema."""
        return {'version': API_VERSION}


class Resources(ResourceEnum):
    """Enum of all resources in this module."""

    version = Version
