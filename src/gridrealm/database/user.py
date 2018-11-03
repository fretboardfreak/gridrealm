"""Gridrealm User."""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from gridrealm.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    last_login = Column(Float)
    last_logout = Column(Float)

    def __init__(self, name=None, last_login=None, last_logout=None):
        self.name = name
        self.last_login = last_login
        self.last_logout = last_logout

    def __repr__(self):
        return '<User %r>' % (self.name)
