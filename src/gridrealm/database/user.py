"""Gridrealm User."""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from gridrealm.database import Base


class User(Base):
    """A user of the game gridrealm."""

    # pylint: disable=invalid-name
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    last_login = Column(Float)
    last_logout = Column(Float)

    def __init__(self, name=None, last_login=None, last_logout=None):
        """Create an instance of the User database model."""
        self.name = name
        self.last_login = last_login
        self.last_logout = last_logout

    def __repr__(self):
        """Return a representation of the User database model."""
        return '<User %r>' % (self.name)
