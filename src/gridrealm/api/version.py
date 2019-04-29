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
