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
"""Gridrealm Map Tile."""

import enum

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Enum
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship

from gridrealm.database import Base


class TileType(enum.Enum):
    """Identifies the type of map tile."""

    text = enum.auto()
    image = enum.auto()
    trigger = enum.auto()  # trigger type triggers additional actions


class MapTile(Base):
    """A tile that makes up the world map."""

    __tablename__ = 'map_tiles'

    # pylint doesn't like the name id
    # pylint: disable=invalid-name
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    tile_type = Column(Enum(TileType), nullable=False)
    resource = Column(String(256), nullable=False)
    enterN = Column(Boolean, nullable=False)
    enterE = Column(Boolean, nullable=False)
    enterS = Column(Boolean, nullable=False)
    enterW = Column(Boolean, nullable=False)
    exitN = Column(Boolean, nullable=False)
    exitE = Column(Boolean, nullable=False)
    exitS = Column(Boolean, nullable=False)
    exitW = Column(Boolean, nullable=False)

    coords = relationship('MapCoord', back_populates='tile')

    def __init__(self, name, tile_type, resource,
                 enterN, enterE, enterS, enterW,
                 exitN, exitE, exitS, exitW):
        """Create an instance of the MapTile database model."""
        self.name = name
        self.tile_type = tile_type
        self.resource = resource
        self.enterN = enterN
        self.enterE = enterE
        self.enterS = enterS
        self.enterW = enterW
        self.exitN = exitN
        self.exitE = exitE
        self.exitS = exitS
        self.exitW = exitW

    def __repr__(self):
        """Return a representation of the MapTile database model."""
        return '<MapTile %r: %r>' % (self.id, self.name)
