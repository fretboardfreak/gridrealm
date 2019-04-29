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
"""Gridrealm sysmsg route."""

import gridrealm as GR
from gridrealm.routes.core import GRView


class SysMsg(GRView):
    """Endpoint for broadcasting system messages to all clients."""

    route = '/sysmsg'
    endpoint = 'sysmsg'

    def get(self):
        """Return the EventSource for the System Message channel."""
        return GR.SYS_MSG.subscribe()
