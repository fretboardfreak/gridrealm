"""Gridrealm Database Core."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

import gridrealm
import gridrealm.database as database


def load_db(db_url):
    gridrealm.DBE = create_engine(db_url, convert_unicode=True)
    gridrealm.DBS = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=gridrealm.DBE))
    database.Base.query = gridrealm.DBS.query_property()


def init_db():
    from gridrealm.database.user import User
    database.Base.metadata.create_all(bind=gridrealm.DBE)
