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
"""Gridrealm cookies library."""

from enum import Enum
from enum import auto


class Cookies(Enum):
    """An Enum of cookies used in the gridrealm client."""

    username = auto()
    last_login = auto()


def clear_cookies(response):
    """Clear out all gridrealm client cookies in the response."""
    for cookie in Cookies:
        response.set_cookie(cookie.name, '', expires=0)


def set_cookies(response, username=None, last_login=None):
    """Set the gridrealm client cookies on the response."""
    if username:
        response.set_cookie(Cookies.username.name, username)
    if last_login:
        response.set_cookie(Cookies.last_login.name, last_login)
