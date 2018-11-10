"""Gridrealm API core library."""

from enum import Enum


API_VERSION = "0.1"


class ResourceEnum(Enum):
    """Base API Resource object for the gridrealm API."""

    @classmethod
    def add_resources(cls, api, resource_classes=None):
        """Register the given resources on the api object."""
        if not resource_classes:
            resource_classes = [res.value for res in cls]
        for res_cls in resource_classes:
            api.add_resource(res_cls, res_cls.uri)
