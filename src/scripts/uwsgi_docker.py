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
