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
"""Gridrealm Server Events.

Provide a method for the game server to generate Event Stream messages that can
be subscribed to by the clients.
"""

import random
import string
from collections import deque

from flask import request
from flask import Response
import gevent
from gevent.queue import Queue

from gridrealm.util import ts_to_str


def generate_id(size=6, chars=string.ascii_lowercase + string.digits):
    """Generate a short alphanumeric ID string."""
    return ''.join(random.choice(chars) for _ in range(size))


class ServerSentEvent(object):
    """Class to handle server-sent events."""

    def __init__(self, data, event):
        """Construct a Server Sent Event object."""
        self.data = data
        self.event = event
        self.event_id = generate_id()
        self.desc_map = {
            self.data: "data",
            self.event: "event",
            self.event_id: "id"
        }

    def encode(self):
        """Encode the event as a string."""
        if not self.data:
            return ""
        lines = ["{}: {}".format(name, key)
                 for key, name in self.desc_map.items() if key]

        return "{}\n\n".format("\n".join(lines))


class Channel(object):
    """Message Channel for publishing text to multiple subscribers."""

    def __init__(self, history_size=32):
        """Construct a channel with some message history."""
        self.subscriptions = []
        self.history = deque(maxlen=history_size)
        self.history.append(ServerSentEvent('start_of_history', None))

    def notify(self, message):
        """Notify all subscribers with message."""
        for sub in self.subscriptions[:]:
            sub.put(message)

    def event_generator(self, last_id):
        """Yield encoded ServerSentEvents."""
        queue = Queue()
        self._add_history(queue, last_id)
        self.subscriptions.append(queue)
        try:
            while True:
                yield queue.get()
        except GeneratorExit:
            self.subscriptions.remove(queue)

    def subscribe(self):
        """Subscribe the client of the request context to the channel."""
        def gen(last_id):
            """Generate an encoded Server Sent Event object."""
            for sse in self.event_generator(last_id):
                yield sse.encode()
        return Response(
            gen(request.headers.get('Last-Event-ID')),
            mimetype="text/event-stream")

    def _add_history(self, queue, last_id):
        """Add a Server Sent Event object to the message history."""
        add = False
        for sse in self.history:
            if add:
                queue.put(sse)
            if sse.event_id == last_id:
                add = True

    def publish(self, message, time_prefix=True):
        """Publish a message to the subscribersself.

        If time_prefix is true include a timestamp at the beginning of the
        message.
        """
        if time_prefix:
            message = "%s: %s" % (ts_to_str(), message)
        sse = ServerSentEvent(str(message), None)
        self.history.append(sse)
        gevent.spawn(self.notify, sse)

    def get_last_id(self):
        """Find the ID of the last event in the channel's history."""
        return self.history[-1].event_id
