"""Gridrealm Database Core."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

import gridrealm
import gridrealm.database as db


def load_db(db_url):
    """Load the database engine and create a threadsafe session."""
    gridrealm.DBE = create_engine(db_url, convert_unicode=True)
    gridrealm.DBS = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=gridrealm.DBE))
    db.Base.query = gridrealm.DBS.query_property()


def init_db():
    """Create the database schema in a new database."""
    # pylint: disable=unused-variable
    from gridrealm.database.user import User
    from gridrealm.database.map_tile import MapTile
    from gridrealm.database.map_coord import MapCoord
    db.Base.metadata.create_all(bind=gridrealm.DBE)
    # pylint: disable=no-member
    gridrealm.DBS.commit()
