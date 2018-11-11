"""Gridrealm User."""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKeyConstraint

from gridrealm.database.base import Base
from gridrealm.database.map_coord import MapCoord


class User(Base):
    """A user of the game gridrealm."""

    __tablename__ = 'users'

    # pylint doesn't like the name id
    # pylint: disable=invalid-name
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    last_login = Column(Float, nullable=False)
    last_logout = Column(Float)
    xcoord = Column(Integer, nullable=False)
    ycoord = Column(Integer, nullable=False)
    zcoord = Column(Integer, nullable=False)

    __table_args__ = (ForeignKeyConstraint(
        [xcoord, ycoord, zcoord],
        [MapCoord.xcoord, MapCoord.ycoord, MapCoord.zcoord]),
                      {})

    def __init__(self, name=None, last_login=None, last_logout=None):
        """Create an instance of the User database model."""
        self.name = name
        self.last_login = last_login
        self.last_logout = last_logout
        self.xcoord = 0
        self.ycoord = 0
        self.zcoord = 0

    def __repr__(self):
        """Return a representation of the User database model."""
        return '<User %r>' % (self.name)
