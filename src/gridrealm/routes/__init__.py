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
"""Gridrealm Routes package."""

from enum import Enum

from .core import register_views

from .index import Index
from .logout import Logout
from .assets import Assets
from .docs import Docs
from .favicon import Favicon
from .sysmsg import SysMsg


class Views(Enum):
    """Enum of all the non-API View classes for gridrealm."""

    index = Index
    logout = Logout
    assets = Assets
    docs = Docs
    favicon = Favicon
    sysmsg = SysMsg
