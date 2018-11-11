"""Random Image URI Library."""

import os
import random
from enum import Enum
from flask_restful import Resource

import gridrealm as GR
from gridrealm.config import Config
from gridrealm.auth import user_required
from gridrealm.api.core import ResourceEnum


class RandomImage(Resource):
    """Return a random image from the GR assetsself.

    This is intended for use as a means of testing.
    """

    uri = '/api/randomImage'
    specific_path = None

    def _load_image_list(self, specific_path=None):
        """Load a list of images from the asset folder."""
        images = []
        assets = "_assets"
        start_path = os.path.join(GR.APP.static_folder,
                                  Config().assets.asset_path)
        if specific_path:
            start_path = os.path.join(start_path, specific_path)
        for dpath, _, fnames in os.walk(start_path):
            common = dpath[dpath.find(assets) + len(assets):]
            common = common[1:] if common.startswith('/') else common
            if common == "dev":
                continue
            for fname in fnames:
                if fname.startswith(".") or fname.startswith("_"):
                    # skip files starting with "." or "_"
                    continue
                if fname not in images:
                    img_uri = os.path.join(assets, common, fname)
                    images.append(img_uri)
        return images

    def get(self):
        """Choose and return a random image from the list of images."""
        images = self._load_image_list(self.specific_path)
        img = random.choice(images)
        return {'image': img}

    get = user_required(get)


class RandomActionImage(RandomImage):
    """Return a random image from the action pane assets."""

    uri = '/api/randomActionImage'
    specific_path = "action"


class RandomInventoryImage(RandomImage):
    """Return a random image from the multi pane inventory assets."""

    uri = '/api/randomInventoryImage'
    specific_path = "multi/inventoryIcons"


class Resources(ResourceEnum):
    """Enum of all resources in this module."""

    image = RandomImage
    action = RandomActionImage
    inventory = RandomInventoryImage
