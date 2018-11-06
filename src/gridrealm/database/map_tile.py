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

    # pylint: disable=invalid-name
    __tablename__ = 'map_tiles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    tile_type = Column(Enum(TileType))
    resource = Column(String(256))
    enterN = Column(Boolean)
    enterE = Column(Boolean)
    enterS = Column(Boolean)
    enterW = Column(Boolean)
    exitN = Column(Boolean)
    exitE = Column(Boolean)
    exitS = Column(Boolean)
    exitW = Column(Boolean)
    # map = relationship('Map', uselist=False, back_populates="map_tiles")
    # map_coords = relationship(
    #     'MapCoord', backref=backref("map_tiles", uselist=False))
    coords = relationship('MapCoord', back_populates='tile')

    def __init__(self, name, tile_type, resource,
                 enterN, enterE, enterS, enterW,
                 exitN, exitE, exitS, exitW):
        """Create an instance of the MapTile database model."""
        # self.id = id
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
