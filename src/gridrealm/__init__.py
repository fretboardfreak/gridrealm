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
"""Gridrealm engine package."""

from .main import cli_main
from .main import load_uwsgi
from .config import Config


# These Globals are set by the main methods so that they can be accessed from
# anywhere.

# Flask app and Flask-Restful API objects
APP = None
API = None

# Message broadcast channel for server to client messages
SYS_MSG = None


DBE = None  # Backend Database Engine
DBS = None  # Backend Database Session
