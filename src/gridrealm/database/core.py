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
"""Gridrealm Database Core."""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

import gridrealm
from gridrealm.database.base import Base


def load_db(db_url):
    """Load the database engine and create a threadsafe session."""
    gridrealm.DBE = create_engine(db_url, convert_unicode=True)
    gridrealm.DBS = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=gridrealm.DBE))
    Base.query = gridrealm.DBS.query_property()


def init_db():
    """Create the database schema in a new database."""
    # pylint doesn't like the unused imports or the DBS global
    # pylint: disable=unused-variable
    from gridrealm.database.user import User
    from gridrealm.database.map_tile import MapTile
    from gridrealm.database.map_coord import MapCoord
    Base.metadata.create_all(bind=gridrealm.DBE)
    # pylint: disable=no-member
    gridrealm.DBS.commit()
