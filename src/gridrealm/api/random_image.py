"""Random Image URI Library."""

import os
import random
from enum import Enum
from flask_restful import Resource

from gridrealm.config import Config


class RandomImage(Resource):
    """Return a random image from the GR assetsself.

    This is intended for use as a means of testing.
    """

    uri = '/api/randomImage'
    specific_path = None
    app = None

    def _load_image_list(self, specific_path=None):
        """Load a list of images from the asset folder."""
        images = []
        assets = "_assets"
        start_path = os.path.join(self.app.static_folder,
                                  Config().assets.asset_path)
        if specific_path:
            start_path = os.path.join(start_path, specific_path)
        # debug logging
        # self.app.logger.debug('RI: start path: %s' % start_path)
        for dpath, _, fnames in os.walk(start_path):
            common = dpath[dpath.find(assets) + len(assets):]
            common = common[1:] if common.startswith('/') else common
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
        # debug logging
        # self.app.logger.debug('RI: image "%s" chosen from %s items' %
        #                       (img, len(images)))
        return {'image': img}


class RandomActionImage(RandomImage):
    """Return a random image from the action pane assets."""

    uri = '/api/randomActionImage'
    specific_path = "images/action"


class RandomInventoryImage(RandomImage):
    """Return a random image from the multi pane inventory assets."""

    uri = '/api/randomInventoryImage'
    specific_path = "images/multi/inventoryIcons"


# class RandomImageResources(Enum):
class Resources(Enum):
    """Enum of all resources in this module."""

    image = RandomImage
    action = RandomActionImage
    inventory = RandomInventoryImage

    @classmethod
    def add_resources(cls, api, resource_classes=None):
        """Register the given resources on the api object."""
        if not resource_classes:
            resource_classes = [res.value for res in cls]
        for res_cls in resource_classes:
            res_cls.app = api.app
            api.add_resource(res_cls, res_cls.uri)