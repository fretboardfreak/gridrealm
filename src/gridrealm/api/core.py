# Copyright 2019 Curtis Sand <curtissand@gmail.com>,
#                Dennison Gaetz <djgaetz@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
