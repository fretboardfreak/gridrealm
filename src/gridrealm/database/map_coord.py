"""Gridrealm Map Coordinate."""


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from gridrealm.database import Base


class MapCoord(Base):
    """Table to represent the map details at each coordinate."""

    __tablename__ = 'map_coords'

    xcoord = Column(Integer, primary_key=True, nullable=False)
    ycoord = Column(Integer, primary_key=True, nullable=False)
    zcoord = Column(Integer, primary_key=True, nullable=False)
    tile_id = Column(Integer, ForeignKey('map_tiles.id'), nullable=False)

    tile = relationship('MapTile', back_populates='coords')
    users = relationship('User', backref='coord')

    def __init__(self, xcoord, ycoord, zcoord, tile_id):
        """Create an instance of the MapTile database model."""
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.zcoord = zcoord
        self.tile_id = tile_id

    def __repr__(self):
        """Return a representation of the MapTile database model."""
        return '<MapCoord: X=%d, Y=%d, Z=%d>' % (
            self.xcoord, self.ycoord, self.zcoord)
